#!/usr/bin/env python3
"""Generate the tiny EN<->RU availability manifest for translated courses.

The site UI used to fetch the whole 13+ MB `search.json` (no-store) on EVERY
page load just to learn which Theoretical Computer Science articles have a
Russian sibling. That download blocked the entire UI boot (custom nav,
toggles, fonts, language) for seconds after first paint.

This script bakes the same knowledge at build time into `ru-manifest.json`
(a few KB, cacheable). Runtime (`_includes/index.html`) fetches only it.
Run manually or via _quarto.yml pre-render.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "ru-manifest.json"

# course dirs (relative to repo root) participating in EN<->RU, mirroring
# INN_TRANSLATION_PATH_PREFIX in _includes/index.html
TRANSLATED_DIRS = [Path("semester-2/Theoretical Computer Science")]

TITLE_RE = re.compile(r"^title:\s*[\"']?(.*?)[\"']?\s*$")


def qmd_title(path: Path) -> str:
    try:
        with path.open(encoding="utf-8") as f:
            in_front = False
            for i, line in enumerate(f):
                s = line.strip()
                if i == 0 and s != "---":
                    return ""
                if i > 0 and s == "---":
                    break
                if i == 0:
                    in_front = True
                    continue
                if in_front:
                    m = TITLE_RE.match(line.rstrip("\n"))
                    if m:
                        return m.group(1).strip()
    except OSError:
        pass
    return ""


def main() -> int:
    pairs: dict[str, dict[str, str]] = {}
    for d in TRANSLATED_DIRS:
        root = ROOT / d
        if not root.is_dir():
            continue
        for qmd in sorted(root.glob("*.qmd")):
            if qmd.name.endswith(".ru.qmd"):
                continue
            ru_qmd = qmd.with_name(qmd.stem + ".ru.qmd")
            if not ru_qmd.is_file():
                continue
            en_rel = (d / (qmd.stem + ".html")).as_posix()
            ru_rel = (d / (ru_qmd.stem + ".html")).as_posix()
            pairs[en_rel] = {
                "ru": ru_rel,
                "enTitle": qmd_title(qmd),
                "ruTitle": qmd_title(ru_qmd),
            }
    payload = {"version": 1, "pairs": pairs}
    text = json.dumps(payload, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if MANIFEST.is_file() and MANIFEST.read_text(encoding="utf-8") == text:
        print(f"ru-manifest: fresh ({len(pairs)} pairs)")
        return 0
    MANIFEST.write_text(text, encoding="utf-8")
    print(f"ru-manifest: wrote {len(pairs)} pairs -> {MANIFEST.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
