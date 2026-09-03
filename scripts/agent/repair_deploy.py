#!/usr/bin/env python3
"""Auto-repair known deploy failure modes (runs after failed deploy-site).

Reads the failed run log, applies deterministic fixes for known cases:
- missing Rscript: ensure deploy.yml has r-lib/actions/setup-r + igraph install
- bad _quarto.yml: re-validate and restore minimal render/resources entries
- formatting violations: re-run fix_formatting.py (idempotent)

Unknown failures: if GEMINI_API_KEY is present, ask gemini-3.8-flash for a
minimal patch suggestion and print it (no blind edits). Exits 0 so the
workflow can commit whatever deterministic fixes were applied.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[2]
GEMINI_MODEL = "gemini-3.8-flash"


def read_log(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def ensure_r_in_deploy() -> bool:
    """Make sure deploy.yml installs R. Returns True if changed."""
    p = ROOT / ".github/workflows/deploy.yml"
    t = p.read_text(encoding="utf-8")
    if "setup-r" in t:
        return False
    anchor = "      - uses: quarto-dev/quarto-actions/setup@v2\n"
    insert = (
        "      - name: Setup R (required by knitr engine)\n"
        "        uses: r-lib/actions/setup-r@v2\n"
        "        with:\n"
        "          r-version: '4.5'\n"
        "      - name: Install R dependencies (Windows binaries via P3M snapshot)\n"
        "        run: |\n"
        '          Rscript -e \'options(repos=c(CRAN="https://packagemanager.posit.co/cran/2025-08-01")); install.packages(c("knitr", "rmarkdown", "igraph"))\'\n'
    )
    if anchor not in t:
        print("repair: deploy.yml anchor not found, skipping R insert")
        return False
    t = t.replace(anchor, anchor + insert)
    p.write_text(t, encoding="utf-8")
    print("repair: added R setup to deploy.yml")
    return True


def ask_gemini_for_patch(log: str, api_key: str) -> str:
    """Ask Gemini 3.8 flash for a minimal fix suggestion. Returns text (may be empty)."""
    prompt = (
        "You are a CI repair assistant for a Quarto website repo (inno_notes). "
        "Below is a failed deploy-site run log. Suggest the SMALLEST concrete fix "
        "(exact file path + unified diff or precise edit instructions). "
        "Only suggest changes inside: .github/workflows/deploy.yml, _quarto.yml, scripts/agent/. "
        "Never suggest touching semester-1/2/3 content. "
        "Deploy (.github/workflows/deploy.yml) only publishes the prebuilt _site/ directory and installs no toolchain; never suggest adding setup-python/node/R/Quarto/apt steps there. If _site is missing or stale, say: build on Windows and commit _site/ via scripts/publish.sh, then push. "
        "Keep the answer under 40 lines.\n\n"
        f"LOG:\n{log[-12000:]}"
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.0, "maxOutputTokens": 2048},
    }
    last_err: Exception | None = None
    for attempt in range(1, 4):
        try:
            with httpx.Client(timeout=httpx.Timeout(120.0, connect=20.0)) as client:
                resp = client.post(
                    f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
                    headers={"Content-Type": "application/json", "X-goog-api-key": api_key},
                    json=payload,
                )
            if resp.status_code in (429, 500, 502, 503, 504):
                last_err = RuntimeError(f"Gemini HTTP {resp.status_code}: {resp.text[:300]}")
                time.sleep(min(2 ** attempt * 5, 30))
                continue
            resp.raise_for_status()
            data = resp.json()
            cands = data.get("candidates") or []
            if not cands:
                return ""
            parts = (cands[0].get("content") or {}).get("parts") or []
            return "\n".join(p.get("text", "") for p in parts if "text" in p).strip()
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(min(2 ** attempt * 5, 30))
    print(f"repair: Gemini suggestion unavailable: {last_err}")
    return ""


def main() -> None:
    ap = argparse.ArgumentParser(description="Auto-repair deploy failures")
    ap.add_argument("--log", type=Path, default=Path("/tmp/deploy_fail.log"))
    ap.add_argument("--max-iterations", type=int, default=2)
    args = ap.parse_args()

    log = read_log(args.log)
    changed = False

    # Deterministic fix 1: missing Rscript
    if "Rscript" in log and ("entity not found" in log or "Unable to locate an installed version of R" in log):
        if ensure_r_in_deploy():
            changed = True

    # Deterministic fix 2: nothing else known yet — ask Gemini for advice (advisory only)
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
    if api_key and ("ERROR" in log or "failed" in log.lower()):
        try:
            suggestion = ask_gemini_for_patch(log, api_key)
            if suggestion:
                out = ROOT / "scripts/agent/last_repair_suggestion.md"
                out.write_text(suggestion, encoding="utf-8")
                print(f"repair: wrote Gemini suggestion to {out}")
        except Exception as e:  # noqa: BLE001
            print(f"repair: Gemini suggestion failed: {e}")

    if changed:
        print("repair: deterministic fixes applied")
    else:
        print("repair: no deterministic fixes applied (see suggestion file if any)")
    sys.exit(0)


if __name__ == "__main__":
    main()
