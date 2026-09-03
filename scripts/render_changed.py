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
import concurrent.futures
import html as html_module
import json
import os
import re
import shutil
import subprocess
import sys
import time
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(os.environ.get("INNO_NOTES_ROOT", Path(__file__).resolve().parents[1]))
SITE = ROOT / "_site"
SEARCH = SITE / "search.json"
QUARTO_YML = ROOT / "_quarto.yml"
SUPPRESSED_LINES = [
    "    - scripts/update_last_updated.py\n",
    "    - scripts/update_index.py\n",
    "    - bash scripts/bake-static-html.sh\n",
]


def suppress_yml(text: str) -> str:
    """Drop pre/post-render script lines; drop headers left completely empty
    (quarto rejects `pre-render:` with a null value, comments don't count)."""
    body = [ln for ln in text.splitlines(keepends=True) if ln not in SUPPRESSED_LINES]
    res: list[str] = []
    i = 0
    while i < len(body):
        if body[i] in ("  pre-render:\n", "  post-render:\n"):
            j = i + 1
            while j < len(body) and body[j].startswith("    - "):
                j += 1
            if j == i + 1:
                i += 1
                continue
        res.append(body[i])
        i += 1
    return "".join(res)


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


def qmd_to_html(rel: str) -> Path:
    return SITE / Path(rel).with_suffix(".html")


class _MainText(HTMLParser):
    """Collect visible text inside <main>, skipping nav/script/style/header."""

    def __init__(self) -> None:
        super().__init__()
        self.depth = 0
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == "main":
            self.depth += 1
        elif self.depth and tag in ("nav", "script", "style", "header"):
            self.skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "main" and self.depth:
            self.depth -= 1
        elif self.depth and tag in ("nav", "script", "style", "header") and self.skip:
            self.skip -= 1
        elif self.depth and not self.skip and tag in (
            "p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "div", "section",
            "details", "summary", "figure", "table", "tr", "blockquote", "pre",
        ):
            self.parts.append("\n\n")

    def handle_data(self, data: str) -> None:
        if self.depth and not self.skip:
            text = data.strip()
            if text:
                self.parts.append(text + " ")


def sidebar_crumbs() -> dict[str, list[str]]:
    """Map sidebar file path -> [Semester, Course] via _quarto.yml indentation."""
    mapping: dict[str, list[str]] = {}
    semester = course = ""
    for line in (ROOT / "_quarto.yml").read_text(encoding="utf-8").splitlines():
        m = re.match(r'^ {6}- section: "Semester ([IVX]+)"', line)
        if m:
            semester, course = "Semester " + m.group(1), ""
            continue
        m = re.match(r'^ {8}- section: "(.+)"', line)
        if m:
            course = m.group(1)
            continue
        m = re.match(r'^\s+- file: "(.+\.qmd)"', line)
        if m and m.group(1) != "index.qmd" and semester:
            mapping[m.group(1)] = [semester, course]
    return mapping


def qmd_title(rel: str) -> str:
    for line in (ROOT / rel).read_text(encoding="utf-8").splitlines()[1:12]:
        if line == "---":
            break
        m = re.match(r'title:\s*"(.*)"', line)
        if m:
            return m.group(1)
    if rel == "index.qmd":
        m = re.search(r'^project:\s*\n(?:  \S.*\n)*?  title: "([^"]+)"',
                      (ROOT / "_quarto.yml").read_text(encoding="utf-8"), re.M)
        if m:
            return m.group(1)
    return Path(rel).stem


def build_search_entry(rel: str, crumbs_map: dict[str, list[str]]) -> dict:
    """Reconstruct quarto's search entry for a freshly rendered page.

    Same shape as quarto's own entries (href/title/section/text/crumbs);
    text comes from pre-bake HTML, exactly what quarto itself indexes.
    """
    href = Path(rel).with_suffix(".html").as_posix()
    parser = _MainText()
    parser.feed((SITE / href).read_text(encoding="utf-8"))
    text = html_module.unescape(re.sub(r"\n{3,}", "\n\n", re.sub(r"[^\S\n]+", " ", "".join(parser.parts)))).strip()
    if rel == "index.qmd":
        crumbs = ["Home"]
    else:
        crumbs = crumbs_map.get(rel, []) + [qmd_title(rel)]
    return {"objectID": href, "href": href, "title": qmd_title(rel),
            "section": "", "text": text, "crumbs": crumbs}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--full", action="store_true", help="force full quarto render")
    ap.add_argument("--dry-run", action="store_true", help="print plan, change nothing")
    ap.add_argument("--jobs", type=int, default=4, help="parallel quarto renders")
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
    run([sys.executable, str(ROOT / "scripts" / "update_last_updated.py")])
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

    # Suppress project pre/post-render during parallel renders: update scripts
    # already ran once above (serially, race-free); bake runs per file after.
    yml_text = QUARTO_YML.read_text(encoding="utf-8")
    stripped = suppress_yml(yml_text)
    suppressed = stripped != yml_text
    if suppressed:
        QUARTO_YML.write_text(stripped, encoding="utf-8")

    def render_one(rel: str) -> str:
        # Concurrent quarto processes can collide copying shared site_libs
        # (transient lstat race in copyToProjectFreezer) — retry a few times.
        last_tail = ""
        for attempt in range(1, 4):
            res = subprocess.run(["quarto", "render", rel], cwd=str(ROOT),
                                 capture_output=True, text=True)
            if res.returncode == 0:
                return rel
            last_tail = (res.stderr or res.stdout or "")[-1500:]
            print(f"  retry {attempt}/3 for {rel}")
            time.sleep(2 * attempt)
        raise RuntimeError(f"quarto render failed for {rel}:\n{last_tail}")

    rendered_html: list[str] = []
    jobs = max(1, min(args.jobs, len(qmds))) if qmds else 1
    try:
        if qmds:
            print(f"rendering {len(qmds)} file(s) with {jobs} parallel job(s) ...")
            with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as ex:
                for rel in ex.map(render_one, sorted(qmds)):
                    html = qmd_to_html(rel)
                    if html.exists():
                        rendered_html.append(str(html.relative_to(SITE).as_posix()))
                    print(f"  rendered {rel}")
    finally:
        if suppressed:
            QUARTO_YML.write_text(yml_text, encoding="utf-8")

    # Rebuild search entries for rendered pages from built HTML (pre-bake,
    # exactly what quarto itself indexes); drop stale href + href#* entries.
    if rendered_html:
        crumbs_map = sidebar_crumbs()
        for rel in sorted(qmds):
            href = Path(rel).with_suffix(".html").as_posix()
            snap = {h: e for h, e in snap.items()
                    if h != href and not h.startswith(href + "#")}
            snap[href] = build_search_entry(rel, crumbs_map)
        SEARCH.write_text(json.dumps(list(snap.values()), ensure_ascii=False), encoding="utf-8")
        print(f"  search index rebuilt for {len(rendered_html)} page(s)")

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
            href = Path(rel).with_suffix(".html").as_posix()
            for h in [h for h in snap2 if h == href or h.startswith(href + "#")]:
                snap2.pop(h, None)
        SEARCH.write_text(json.dumps(list(snap2.values()), ensure_ascii=False), encoding="utf-8")
        print(f"dropped {dropped} stale outputs")

    print(f"done: rendered {len(rendered_html)}, baked {len(rendered_html)}, "
          f"injects {len(includes)}, copies {len(styles) + len(assets)}")


if __name__ == "__main__":
    main()
