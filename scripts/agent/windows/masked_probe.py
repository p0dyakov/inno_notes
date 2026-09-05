"""Masked-egress serving probe: personal LS via US HTTP proxy, tiny PRO reply.

Chain: spawned language_server.exe --(HTTPS_PROXY=http://127.0.0.1:18081)-->
ssh -L 18081--> hostkey CONNECT proxy --> Google (US egress 80.209.241.71).
Prints MASKED_OK on a real model reply. Kills the spawned LS afterwards.
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import Hub, spawn_ls

PROXY = "http://127.0.0.1:18081"

info = spawn_ls(proxy=PROXY)
print("spawned:", info["pid"], info["address"], flush=True)
try:
    hub = Hub(ls_address=info["address"], csrf=info["csrf"])
    hub.ensure_project()
    try:
        q = hub.quota()
        groups = [(g.get("displayName"), [b.get("remainingFraction") for b in g.get("buckets", [])])
                  for g in q.get("groups", [])]
        print("quota:", groups, flush=True)
    except Exception as e:
        print("quota-check failed:", str(e)[:200], flush=True)
    out = hub.complete("Reply with exactly: OK", tier="pro", title="inno-masked",
                       timeout_s=420, poll_s=15)
    print("MASKED_OK:", out.strip()[:60], flush=True)
finally:
    subprocess.run(["taskkill", "/PID", str(info["pid"]), "/F"],
                   capture_output=True)
    print("spawned LS killed", flush=True)
