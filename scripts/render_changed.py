#!/usr/bin/env python3
"""Incremental site build for local/Windows runs: re-render only what changed.

Flow:
  1. fix_formatting.py, update_index.py (+ update_sidebar for new files).
  2. Classify changed files vs BASE (default origin/main):
     - _quarto.yml ................. full `quarto render` (nav/sidebar is global).
     - *.qmd ........................ render each file only (+ per-file bake).
     - _includes/* ................. fast in-place patch of _site HTML, no render.
     - styles/*, page assets ........ mirror-copy into _site (stable paths).
     - deleted sources ............. delete mirrored _site outputs.
  3. search.json is snapshotted before renders (single-file renders overwrite
     it with one entry) and merged back afterwards.
  4. Post-render bake is suppressed during per-file renders (temporarily, with
     restore) and run per changed file instead — same result, much faster.

Usage: python3 scripts/render_changed.py [--base origin/main] [--full] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(os.environ.get("INNO_NOTES_ROOT", Path(__file__).resolve().parents[1]))
SITE = ROOT / "_site"
SEARCH = SITE / "search.json"
QUARTO_YML = ROOT / "_quarto.yml"
POST_RENDER_LINE = "    - bash scripts/bake-static-html.sh"


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), **kwargs)


def changed_files(base: str) -> list[str]:
    out: set[str] = set()
    st = run(["git", "status", "--porcelain=v1", "--untracked-files=all"])
    for line in st.stdout.splitlines():
        code, path = line[:2], line[3:].strip().strip('"')
        if " -> " in path:  # renames: take the new path
            path = path.split(" -> ")[1].strip().strip('"')
        if code.strip() not in ("", "!!"):
            out.add(path)
    if run(["git", "rev-parse", "--verify", "--quiet", base]).returncode == 0:
        diff = run(["git", "diff", "--name-only", f"{base}...HEAD"])
        out.update(p.strip() for p in diff.stdout.splitlines() if p.strip())
    return sorted(p for p in out if p)


def snapshot_search() -> dict[str, dict] | None:
    if not SEARCH.exists():
        return None
    try:
        data = json.loads(SEARCH.read_text(encoding="utf-8"))
        entries = data if isinstance(data, list) else data.get("articles", [])
        return {e.get("href", ""): e for e in entries if e.get("href")}
    except Exception:
        return None


def merge_search(snapshot: dict[str, dict]) -> int:
    """Fold current (partial) _site/search.json entries into the snapshot."""
    if not SEARCH.exists():
        return 0
    try:
        data = json.loads(SEARCH.read_text(encoding="utf-8"))
        entries = data if isinstance(data, list) else data.get("articles", [])
    except Exception:
        return 0
    n = 0
    for e in entries:
        if e.get("href"):
            snapshot[e["href"]] = e
            n += 1
    SEARCH.write_text(json.dumps(list(snapshot.values()), ensure_ascii=False), encoding="utf-8")
    return n


def qmd_to_html(rel: str) -> Path:
    return SITE / Path(rel).with_suffix(".html")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--full", action="store_true", help="force full quarto render")
    ap.add_argument("--dry-run", action="store_true", help="print plan, change nothing")
    args = ap.parse_args()

    if args.dry_run:
        for p in changed_files(args.base):
            print("changed:", p)
        return

    r = run([sys.executable, str(ROOT / "fix_formatting.py")])
    if r.returncode != 0:
        print("fix_formatting.py failed, aborting", file=sys.stderr)
        sys.exit(1)
    run([sys.executable, str(ROOT / "scripts" / "update_index.py")])
    try:
        sys.path.insert(0, str(ROOT / "scripts" / "agent"))
        from generate import update_sidebar  # noqa: E402

        update_sidebar()
    except Exception as e:  # noqa: BLE001
        print(f"WARN: update_sidebar skipped ({e})")

    changed = changed_files(args.base)
    qmds = [p for p in changed if p.endswith(".qmd") and not p.startswith("_site/")]
    deleted_qmds = [p for p in qmds if not (ROOT / p).exists()]
    qmds = [p for p in qmds if (ROOT / p).exists()]
    includes = [p for p in changed if p.startswith("_includes/") and (ROOT / p).exists()]
    styles = [p for p in changed if p.startswith("styles/") and (ROOT / p).exists()]
    assets = [p for p in changed
              if re.search(r"\.(png|jpe?g|gif|svg|mp4|pdf|css|js)$", p, re.I)
              and not p.startswith(("_site/", "styles/", "_includes/", "node_modules/"))
              and (ROOT / p).exists()]
    deleted_assets = [p for p in changed
                      if re.search(r"\.(png|jpe?g|gif|svg|mp4|pdf|css|js)$", p, re.I)
                      and not p.startswith(("_site/", "node_modules/"))
                      and not (ROOT / p).exists()]
    full_needed = args.full or "_quarto.yml" in changed

    print(f"changed: {len(changed)} files; qmd to render: {len(qmds)}; "
          f"includes: {len(includes)}; assets: {len(assets)}; full: {full_needed}")

    if full_needed:
        res = subprocess.run(["quarto", "render"], cwd=str(ROOT))
        sys.exit(res.returncode)

    snap = snapshot_search()
    if snap is None:
        print("WARN: _site/search.json missing, falling back to full render")
        res = subprocess.run(["quarto", "render"], cwd=str(ROOT))
        sys.exit(res.returncode)

    # Suppress project post-render during per-file renders; bake manually after.
    yml_text = QUARTO_YML.read_text(encoding="utf-8")
    suppressed = POST_RENDER_LINE in yml_text
    if suppressed:
        QUARTO_YML.write_text(yml_text.replace(POST_RENDER_LINE + "\n", ""), encoding="utf-8")
    rendered_html: list[str] = []
    try:
        for rel in qmds:
            print(f"render: {rel}")
            res = subprocess.run(["quarto", "render", rel], cwd=str(ROOT))
            if res.returncode != 0:
                print(f"ERROR rendering {rel}, aborting", file=sys.stderr)
                sys.exit(res.returncode)
            n = merge_search(snap)
            print(f"  search entries merged: {n}")
            html = qmd_to_html(rel)
            if html.exists():
                rendered_html.append(str(html.relative_to(SITE).as_posix()))
    finally:
        if suppressed:
            QUARTO_YML.write_text(yml_text, encoding="utf-8")

    if rendered_html:
        baked = [str(SITE / h) for h in rendered_html]
        res = subprocess.run(["node", str(ROOT / "scripts" / "bake-static-html.mjs"), *baked], cwd=str(ROOT))
        if res.returncode != 0:
            print("per-file bake failed", file=sys.stderr)
            sys.exit(res.returncode)

    # Fast _includes patch: replace old (BASE version) with new content in place.
    for rel in includes:
        new = (ROOT / rel).read_text(encoding="utf-8")
        old_res = run(["git", "show", f"{args.base}:{rel}"])
        if old_res.returncode != 0 or not old_res.stdout:
            print(f"WARN: {rel} is new or unreadable at {args.base}; run full render if pages miss it")
            continue
        old = old_res.stdout
        if old == new:
            continue
        patched, missed = 0, 0
        for html in SITE.rglob("*.html"):
            if "site_libs" in html.parts:
                continue
            t = html.read_text(encoding="utf-8")
            if old in t:
                html.write_text(t.replace(old, new), encoding="utf-8")
                patched += 1
            else:
                missed += 1
        print(f"inject {rel}: patched {patched} pages ({missed} without old block)")
        if patched == 0:
            print(f"WARN: {rel} matched no pages; run full render if needed")

    for rel in styles + assets:
        dst = SITE / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dst)
        print(f"copied: {rel}")

    dropped = 0
    for rel in deleted_qmds:
        html = qmd_to_html(rel)
        if html.exists():
            html.unlink()
            dropped += 1
    for rel in deleted_assets:
        dst = SITE / rel
        if dst.exists():
            dst.unlink()
            dropped += 1
    if dropped:
        snap2 = snapshot_search() or {}
        for rel in deleted_qmds:
            snap2.pop(Path(rel).with_suffix(".html").as_posix(), None)
        SEARCH.write_text(json.dumps(list(snap2.values()), ensure_ascii=False), encoding="utf-8")
        print(f"dropped {dropped} stale outputs")

    print(f"done: rendered {len(rendered_html)}, baked {len(rendered_html)}, "
          f"injects {len(includes)}, copies {len(styles) + len(assets)}")


if __name__ == "__main__":
    main()
