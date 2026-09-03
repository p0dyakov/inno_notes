#!/usr/bin/env python3
"""Gemini via the locally running Antigravity hub (no API key, subscription quota).

How it works
------------
Antigravity (logged in on this machine) runs a `language_server --subclient_type hub`
process that serves a Connect-JSON API on localhost
(`exa.language_server_pb.LanguageServerService`). This module:

1. discovers the hub (process cmdline -> csrf token, listening API port,
   project id from Antigravity app storage);
2. creates agent conversations (``new-conversation`` tier), sends the prompt;
3. waits for the run to go idle and pulls the reply via
   ``ConvertTrajectoryToMarkdown`` (last Planner Response);
4. classifies serving failures: transient (429/503/no-capacity/timeout ->
   retry with backoff) vs fatal (400 region/auth -> raise).

Windows replication: install Antigravity + log in once, run Sota (or any
egress that reaches Google), then the same discovery works via
``tasklist``/``netstat`` (see _discover_windows). Generation itself never runs
in CI — CI keeps using GEMINI_API_KEY.

No secret is ever printed or stored by this module: csrf tokens live only in
process memory / request headers.
"""

from __future__ import annotations

import json
import os
import platform
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

import httpx

SERVICE = "exa.language_server_pb.LanguageServerService"
CSRF_HEADER = "x-codeium-csrf-token"
TIERS = ("flash_lite", "flash", "pro")


class AntigravityError(RuntimeError):
    pass


class TransientError(AntigravityError):
    """Retryable: rate limits, no capacity, timeouts."""


class FatalError(AntigravityError):
    """Non-retryable: region blocks, auth, bad requests."""


def _gemini_dir() -> Path:
    home = Path(os.path.expanduser("~"))
    return home / ".gemini"


def _app_support() -> Path:
    home = Path(os.path.expanduser("~"))
    if sys.platform == "darwin":
        return home / "Library/Application Support/Antigravity"
    # Windows: Antigravity is Electron; user-data lives under AppData.
    for var in ("APPDATA", "LOCALAPPDATA"):
        base = os.environ.get(var)
        if base:
            cand = Path(base) / "Antigravity"
            if cand.exists():
                return cand
    return home / ".config/Antigravity"


def _hub_cmdlines() -> list[str]:
    """Full cmdlines of hub language_server processes (secrets stay in RAM)."""
    if sys.platform == "win32":
        out = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq language_server.exe", "/FO", "CSV", "/V"],
            capture_output=True, text=True, timeout=30).stdout
        found = [line for line in out.splitlines()
                 if "subclient_type" in line and "hub" in line]
        if found:
            return found
        out = subprocess.run(
            ["wmic", "process", "where", "name='language_server.exe'",
             "get", "CommandLine", "/format:list"],
            capture_output=True, text=True, timeout=30).stdout
        found = [line for line in out.splitlines()
                 if "subclient_type" in line and "hub" in line]
        if found:
            return found
        raise AntigravityError("hub language_server process not found (is Antigravity running?)")
    out = subprocess.run(["ps", "-o", "args", "-ax"],
                         capture_output=True, text=True, timeout=30).stdout
    found = [line for line in out.splitlines()
             if "language_server" in line and "--subclient_type" in line and "hub" in line]
    if not found:
        raise AntigravityError("hub language_server process not found (is Antigravity running?)")
    return found


def _hub_cmdline() -> str:
    return _hub_cmdlines()[0]


def _csrf_from_cmdline(cmdline: str) -> str:
    m = re.search(r"--csrf_token[=\s]+(\S+)", cmdline)
    if not m:
        raise AntigravityError("csrf token not found in hub cmdline")
    return m.group(1)


def _localhost_ports() -> list[int]:
    if sys.platform == "win32":
        out = subprocess.run(["netstat", "-ano", "-p", "TCP"],
                             capture_output=True, text=True, timeout=30).stdout
        ports: list[int] = []
        for line in out.splitlines():
            m = re.search(r"127\.0\.0\.1:(\d+)\s+0\.0\.0\.0:0\s+LISTENING", line)
            if m and int(m.group(1)) not in ports:
                ports.append(int(m.group(1)))
        return ports
    out = subprocess.run(["lsof", "-iTCP", "-sTCP:LISTEN", "-P", "-n"],
                         capture_output=True, text=True, timeout=30).stdout
    ports = []
    for line in out.splitlines():
        m = re.search(r"127\.0\.0\.1:(\d+)", line)
        if m and int(m.group(1)) not in ports:
            ports.append(int(m.group(1)))
    return ports


def _scan_localhost_ports(csrf: str) -> int:
    """Pick the hub's Connect-API port among localhost listeners.

    The LS also serves the hub UI over HTTPS on another port; the Connect API
    answers plain HTTP and (with a valid csrf) reports `trajectory not found`
    for a bogus id, which is how we tell it apart from other local servers.
    """
    ports = _localhost_ports()
    probe = {"Content-Type": "application/json", CSRF_HEADER: csrf}
    for port in ports:
        try:
            r = httpx.post(f"http://127.0.0.1:{port}/{SERVICE}/GetConversationMetadata",
                           headers=probe,
                           json={"conversation_id": "00000000-0000-0000-0000-000000000000"},
                           timeout=8)
            if "trajectory not found" in r.text:
                return port
        except Exception:
            continue
    raise AntigravityError(
        f"LS Connect API port not found among {len(ports)} localhost ports")


def _project_id() -> str:
    for cand in (_app_support() / "app_storage.json",
                 _gemini_dir() / "antigravity-state.json"):
        try:
            raw = cand.read_text(encoding="utf-8")
        except OSError:
            continue
        for key in ("new-convo-last-selected-project", "lastCreatedProjectId",
                    "projectId", "project_id"):
            m = re.search(rf'"{re.escape(key)}"\s*:\s*"([0-9a-f-]{{8,}})"', raw)
            if m:
                return m.group(1)
    raise AntigravityError("Antigravity project id not found (open Antigravity once?)")


class Hub:
    """Authenticated handle to the local Antigravity hub."""

    def __init__(self, ls_address: str = "", csrf: str = "") -> None:
        ls_address = ls_address or os.environ.get("AGY_LS_ADDRESS", "")
        csrf = csrf or os.environ.get("AGY_CSRF_TOKEN", "")
        if ls_address and csrf:
            self._base = f"{ls_address.rstrip('/')}/{SERVICE}"
            self._csrf = csrf
        else:
            cmdline = _hub_cmdline()
            self._csrf = _csrf_from_cmdline(cmdline)
            port = _scan_localhost_ports(self._csrf)
            self._base = f"http://127.0.0.1:{port}/{SERVICE}"
        self._project = _project_id()

    def rpc(self, method: str, body: dict, timeout: float = 120) -> httpx.Response:
        return httpx.post(f"{self._base}/{method}",
                          headers={"Content-Type": "application/json",
                                   CSRF_HEADER: self._csrf},
                          json=body, timeout=timeout)

    def call(self, method: str, body: dict, timeout: float = 120) -> dict:
        r = self.rpc(method, body, timeout)
        if r.status_code == 401:
            raise FatalError("hub csrf rejected (Antigravity restarted? re-discover)")
        try:
            data = r.json()
        except Exception as e:
            raise AntigravityError(f"hub {method}: bad json: {e}")
        if data.get("error"):
            raise AntigravityError(f"hub {method}: {str(data['error'])[:300]}")
        return data.get("response", {})

    def quota(self) -> dict:
        return self.call("RetrieveUserQuotaSummary", {}, timeout=30)

    def models(self) -> dict:
        return self.call("GetAvailableModels", {}, timeout=60).get("models", {})

    def agentapi(self, *args: str, timeout: float = 600) -> dict:
        """Run the bundled `language_server agentapi` CLI against this hub."""
        if sys.platform == "win32":
            exe = str(Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
                      / "Antigravity" / "resources" / "bin" / "language_server.exe")
        else:
            exe = "/Applications/Antigravity.app/Contents/Resources/bin/language_server"
        env = dict(os.environ,
                   ANTIGRAVITY_LS_ADDRESS=self._base.rsplit("/", 1)[0],
                   ANTIGRAVITY_CSRF_TOKEN=self._csrf,
                   ANTIGRAVITY_PROJECT_ID=self._project)
        r = subprocess.run([exe, "agentapi", *args], capture_output=True, text=True,
                           env=env, timeout=timeout)
        try:
            data = json.loads(r.stdout or "{}")
        except Exception:
            raise AntigravityError(f"agentapi {' '.join(args[:1])}: {(r.stdout + r.stderr)[:300]}")
        if data.get("error"):
            raise AntigravityError(f"agentapi: {str(data['error'])[:300]}")
        return data.get("response", {})

    # -- conversations -----------------------------------------------------
    def conv_dir(self) -> Path:
        return _gemini_dir() / ("antigravity" if (_gemini_dir() / "antigravity").exists()
                                else "antigravity-ide") / "conversations"

    def new_conversation(self, prompt: str, tier: str = "pro", title: str = "inno-notes") -> str:
        if tier not in TIERS:
            raise ValueError(f"unknown tier {tier!r} (want one of {TIERS})")
        resp = self.agentapi("new-conversation", f"--model={tier}", f"--title={title}", prompt)
        try:
            return resp["newConversation"]["conversationId"]
        except KeyError:
            raise AntigravityError(f"new-conversation: unexpected response {str(resp)[:200]}")

    def trajectory_db(self, cid: str) -> Path:
        p = self.conv_dir() / f"{cid}.db"
        if not p.exists():
            raise AntigravityError(f"trajectory db missing for {cid[:8]}")
        return p

    def classify_db(self, cid: str) -> tuple[str, str]:
        """Return (state, detail): idle|running|transient|fatal + short detail."""
        try:
            db = sqlite3.connect(str(self.trajectory_db(cid)))
        except Exception:
            return "running", "db not ready"
        try:
            rows = db.execute("SELECT step_payload FROM steps ORDER BY idx").fetchall()
        except Exception:
            return "running", "steps not ready"
        blob = b"\n".join(r[0] for r in rows)
        text = blob.decode("utf-8", errors="ignore")
        for pat in ("User location is not supported", "PERMISSION_DENIED",
                    "insufficient authentication", "neither PlanModel nor RequestedModel"):
            if pat in text:
                return "fatal", pat
        m = re.search(r"No capacity available for model ([A-Za-z0-9_.-]+)", text)
        if m or "high traffic" in text or "UNAVAILABLE" in text:
            return "transient", (m.group(0)[:80] if m else "capacity")
        if "terminated due to error" in text or "Agent execution terminated" in text:
            m2 = re.search(r"(FAILED_PRECONDITION|UNAVAILABLE|RESOURCE_EXHAUSTED|INTERNAL)[^\n]{0,120}", text)
            return "transient" if not m2 or "UNAVAILABLE" in m2.group(0) else "fatal", \
                (m2.group(0)[:100] if m2 else "terminated")
        if "429" in text or "503" in text:
            return "transient", "http 429/503"
        return "running", f"{len(rows)} steps"

    def markdown(self, cid: str) -> str:
        resp = self.call("ConvertTrajectoryToMarkdown", {"conversation_id": cid}, timeout=60)
        md = resp.get("markdown", "")
        if not md:
            raise AntigravityError("empty trajectory markdown")
        return md

    def last_reply(self, md: str) -> str:
        """Last 'Planner Response' section of a trajectory transcript."""
        parts = re.split(r"^### Planner Response\s*$", md, flags=re.M)
        if len(parts) < 2:
            raise AntigravityError("no Planner Response in trajectory")
        return parts[-1].strip()

    def delete(self, cid: str) -> None:
        try:
            self.call("DeleteCascadeTrajectory", {"conversation_id": cid}, timeout=60)
        except AntigravityError as e:
            print(f"  antigravity: cleanup {cid[:8]}: {e}")

    def complete(self, prompt: str, tier: str = "pro", title: str = "inno-notes",
                 timeout_s: int = 900, poll_s: int = 15) -> str:
        """One blocking generation through Antigravity subscription quota."""
        cid = self.new_conversation(prompt, tier, title)
        print(f"  antigravity: conversation {cid[:8]} (tier {tier})")
        start = time.time()
        try:
            while True:
                if time.time() - start > timeout_s:
                    raise TransientError(f"conversation {cid[:8]} timed out")
                state, detail = self.classify_db(cid)
                if state == "fatal":
                    # Region/account gates have been observed flapping
                    # (capacity <-> region across hours), so treat them as
                    # retryable inside a bounded run instead of failing fast.
                    raise TransientError(f"conversation {cid[:8]}: {detail}")
                if state == "transient":
                    raise TransientError(f"conversation {cid[:8]}: {detail}")
                md = ""
                try:
                    md = self.markdown(cid)
                except AntigravityError:
                    pass
                if md and self._looks_done(cid, md):
                    return self.last_reply(md)
                time.sleep(poll_s)
        finally:
            self.delete(cid)

    def _looks_done(self, cid: str, md: str) -> bool:
        """Done when trajectory stopped growing AND has a Planner Response."""
        if "### Planner Response" not in md:
            return False
        try:
            n1 = sqlite3.connect(str(self.trajectory_db(cid))).execute(
                "SELECT COUNT(*) FROM steps").fetchone()[0]
        except Exception:
            return False
        time.sleep(20)
        try:
            n2 = sqlite3.connect(str(self.trajectory_db(cid))).execute(
                "SELECT COUNT(*) FROM steps").fetchone()[0]
        except Exception:
            return False
        state, _ = self.classify_db(cid)
        return n1 == n2 and state == "running"


def spawn_ls(proxy: str = "", headless: bool = False,
             extra_flags: list | None = None) -> dict:
    """Spawn a personal headless-capable hub LS sharing this machine's auth.

    Returns {"pid", "address", "csrf"}. The child survives the parent
    (start_new_session). Point Hub at it via AGY_LS_ADDRESS/AGY_CSRF_TOKEN.
    `proxy` (e.g. http://127.0.0.1:18081, see xproxy.py) is passed through
    HTTPS_PROXY/HTTP_PROXY for the LS's own Google egress.
    """
    import secrets
    csrf = secrets.token_hex(16)
    logf = open("/tmp/agy_spawned_ls.log", "ab", buffering=0)
    if sys.platform == "win32":
        exe = str(Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
                  / "Antigravity" / "resources" / "bin" / "language_server.exe")
    else:
        exe = "/Applications/Antigravity.app/Contents/Resources/bin/language_server"
    args = [exe, "--standalone", "--subclient_type", "hub",
            "--override_ide_name", "antigravity", "--override_ide_version", "2.11.0",
            "--override_user_agent_name", "antigravity",
            "--https_server_port", "0", "--http_server_port", "0",
            "--csrf_token", csrf, "--app_data_dir", "antigravity",
            "--api_server_url", "https://generativelanguage.googleapis.com",
            "--cloud_code_endpoint", "https://daily-cloudcode-pa.googleapis.com",
            "--enable_sidecars"]
    # Copy the running hub's host_bridge so project mapping keeps working.
    for cl in _hub_cmdlines():
        m1 = re.search(r"--host_bridge_url=(\S+)", cl)
        if m1 and "override_model_name" not in cl and "headless" not in cl:
            args += [f"--host_bridge_url={m1.group(1)}"]
            m2 = re.search(r"--host_bridge_token=(\S+)", cl)
            if m2:
                args += [f"--host_bridge_token={m2.group(1)}"]
            break
    if headless:
        args.append("--headless")
    args += extra_flags or []
    env = dict(os.environ)
    if proxy:
        env["HTTPS_PROXY"] = proxy
        env["HTTP_PROXY"] = proxy
        env["NO_PROXY"] = "127.0.0.1,localhost"
    proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=logf,
                            stderr=subprocess.STDOUT, start_new_session=True, env=env)
    # Wait for the API port (plain HTTP answers on it).
    import time as _time
    address = ""
    for _ in range(60):
        _time.sleep(1)
        try:
            out = subprocess.run(
                ["lsof", "-p", str(proc.pid), "-iTCP", "-sTCP:LISTEN", "-P", "-n"]
                if sys.platform != "win32" else ["netstat", "-ano", "-p", "TCP"],
                capture_output=True, text=True, timeout=15).stdout
            ports = [int(m.group(1)) for m in re.finditer(r"127\.0\.0\.1:(\d+)", out)]
            for port in ports:
                try:
                    r = httpx.post(
                        f"http://127.0.0.1:{port}/{SERVICE}/GetConversationMetadata",
                        headers={"Content-Type": "application/json", CSRF_HEADER: csrf},
                        json={"conversation_id": "00000000-0000-0000-0000-000000000000"},
                        timeout=5)
                    if "trajectory not found" in r.text:
                        address = f"http://127.0.0.1:{port}"
                        break
                except Exception:
                    continue
            if address:
                break
        except Exception:
            continue
    if not address:
        raise AntigravityError("spawned LS did not open its API port in time")
    return {"pid": proc.pid, "address": address, "csrf": csrf}


def gemini_pro_preview_available() -> bool:
    """Catalog check: is a Pro-tier Gemini servable right now (quota>0)?"""
    try:
        models = Hub().models()
    except Exception:
        return False
    for key, m in models.items():
        if m.get("modelProvider") == "MODEL_PROVIDER_GOOGLE" and "pro" in key.lower():
            q = (m.get("quotaInfo") or {}).get("remainingFraction", 0)
            if q and q > 0:
                return True
    return False


if __name__ == "__main__":
    hub = Hub()
    print("hub:", hub._base.rsplit("/", 1)[0], "| project:", hub._project[:8] + "...")
    q = hub.quota()
    for g in q.get("groups", []):
        for b in g.get("buckets", []):
            print(f"{g['displayName']}/{b['displayName']}: {b.get('remainingFraction')}")
