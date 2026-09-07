#!/usr/bin/env python3
"""Subset self-hosted woff2 fonts to the glyphs the site actually uses.

Why: the shipped SF/Archivo/Mono files are ~1MB each (full CFF coverage),
and every article loads 4-7 of them (~5-8MB of fonts per page open).
Subsetting to latin+latin-ext+cyrillic+greek+math/tech symbols (audited
against all .qmd + includes: phonetics, ceilings/floors, box drawings,
angle brackets, check marks live in prose, not only in baked math)
shrinks each file ~10x with zero visible change.

Re-run after adding new font files: python3 scripts/subset_fonts.py
Requires: pip install fonttools brotli
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "styles" / "fonts"

UNICODES = ",".join([
    "U+0000-024F",   # Basic Latin + Latin-1 Supplement + Latin Extended A/B
    "U+02B0-02FF",   # Spacing modifier letters (phonetics in prose)
    "U+0300-036F",   # Combining diacritics
    "U+0370-03FF",   # Greek
    "U+0400-04FF",   # Cyrillic (+supplement: Ё,e dialect letters)
    "U+1D00-1D7F",   # Phonetic extensions (Academic Writing articles)
    "U+1F00-1FFF",   # Greek Extended (polytonic)
    "U+2000-206F",   # General punctuation (— – « » … × etc.)
    "U+2070-209F",   # Superscripts/subscripts
    "U+20A0-20CF",   # Currency symbols
    "U+2100-214F",   # Letterlike symbols (№)
    "U+2190-21FF",   # Arrows
    "U+2200-22FF",   # Mathematical operators
    "U+2300-23FF",   # Misc technical (ceilings/floors in prose)
    "U+2500-257F",   # Box drawings (ASCII diagrams in prose/code)
    "U+25A0-25FF",   # Geometric shapes
    "U+2600-26FF",   # Misc symbols (warning sign)
    "U+2700-27BF",   # Dingbats (check/cross marks)
    "U+2764",        # Heart (footer)
    "U+27C0-27EF",   # Math brackets (angle brackets in prose)
    "U+FB00-FB06",   # Latin ligatures
    "U+FEFF,U+FFFD",
])


def main() -> int:
    files = sorted(FONTS.glob("*.woff2"))
    if not files:
        print("no fonts found")
        return 1
    before = sum(p.stat().st_size for p in files)
    for p in files:
        r = subprocess.run(
            [sys.executable, "-m", "fontTools.subset", str(p),
             f"--unicodes={UNICODES}",
             "--layout-features=*",
             "--flavor=woff2",
             f"--output-file={p}"],
            capture_output=True, text=True)
        if r.returncode != 0:
            print(f"FAIL {p.name}: {r.stderr[-500:]}")
            return 1
        print(f"ok {p.name}: {p.stat().st_size // 1024}KB")
    after = sum(p.stat().st_size for p in files)
    print(f"total: {before // 1024}KB -> {after // 1024}KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
