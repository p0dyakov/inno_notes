#!/usr/bin/env python3
"""Pre-bake new/changed .qmd files BEFORE push (the rule in rules.md).

A broken page fails the whole deploy-site run, so every new or modified
article must be fully baked in advance, separately from the site build:

1. fix_formatting.py must report zero violations for these files;
2. each file must pass a full per-file `quarto render` (real bake).

Usage:
  python3 scripts/agent/prebake.py [file.qmd ...] [--format-only] [--base origin/main]

With no files given, checks .qmd files new/modified vs base (plus untracked).
Exit non-zero on the first failure. `--format-only` skips quarto (fast gate
suitable for pre-push hooks); full bake runs on Windows/dev machines.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kwargs)


def changed_qmd(base: str) -> list[Path]:
    out: list[Path] = []
    for args in (["git", "diff", "--name-only", f"{base}...HEAD", "--"],
                 ["git", "ls-files", "--others", "--exclude-standard", "--"]):
        res = run(args, cwd=str(ROOT))
        if res.returncode != 0:
            continue
        for line in res.stdout.splitlines():
            p = (ROOT / line.strip()).resolve()
            if line.strip().endswith(".qmd") and "_site/" not in line and "_freeze/" not in line:
                if p.is_file() and p not in out:
                    out.append(p)
    return out


def format_gate(files: list[Path]) -> bool:
    """Run repo-wide fixer, then require zero violations for our files."""
    print("prebake: fix_formatting.py ...")
    res = run([sys.executable, "fix_formatting.py"], cwd=str(ROOT))
    if res.returncode != 0:
        print(f"prebake FAIL: fix_formatting.py exited {res.returncode}\n{res.stderr[:1000]}")
        return False
    report = ROOT / "formatting_report.md"
    txt = report.read_text(encoding="utf-8") if report.exists() else ""
    ok = True
    for f in files:
        rel = str(f.relative_to(ROOT)).replace("\\", "/")
        sec = re.search(rf"^### {re.escape(rel)}\s*\n((?:- .*\n?)+)", txt, re.M)
        if sec:
            print(f"prebake FAIL: format violations in {rel}:\n{sec.group(1)[:1500]}")
            ok = False
    if ok:
        print(f"prebake: formatting clean for {len(files)} file(s)")
    return ok


def bake(files: list[Path]) -> bool:
    ok = True
    for f in files:
        rel = f.relative_to(ROOT)
        print(f"prebake: quarto render {rel} ...")
        res = run(["quarto", "render", str(f)], cwd=str(ROOT))
        tail = ((res.stdout or "") + (res.stderr or ""))[-800:]
        if res.returncode != 0:
            print(f"prebake FAIL: quarto render {rel} exited {res.returncode}\n{tail}")
            ok = False
        else:
            print(f"prebake: baked {rel}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", help=".qmd files (default: new/changed vs base)")
    ap.add_argument("--format-only", action="store_true", help="skip quarto render")
    ap.add_argument("--base", default="origin/main")
    args = ap.parse_args()
    files = [Path(f).resolve() for f in args.files] if args.files else changed_qmd(args.base)
    files = [f for f in files if f.suffix == ".qmd" and f.is_file()]
    if not files:
        print("prebake: no .qmd files to check")
        return 0
    print(f"prebake: {len(files)} file(s): " + ", ".join(str(f.relative_to(ROOT)) for f in files))
    if not format_gate(files):
        return 1
    if args.format_only:
        print("prebake: format-only OK (full bake still required before push: rerun without --format-only)")
        return 0
    return 0 if bake(files) else 1


if __name__ == "__main__":
    sys.exit(main())
