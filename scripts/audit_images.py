#!/usr/bin/env python3
"""Audit article raster images: intrinsic size vs quality expectations.

Flags images likely to look soft: intrinsic width < 1200px (below ~retina
for a full-width figure) or < 800px (soft even at 1x). The site serves
pixel-identical files (quarto mirror-copies, CSS never upscales), so a
flag here means the SOURCE needs re-sourcing (e.g. re-render the PDF
figure at higher dpi), not a code fix.

Run: python3 scripts/audit_images.py
"""

from __future__ import annotations

import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)#?]+)")


def refs() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for qmd in list((ROOT / "semester-1").rglob("*.qmd")) + \
               list((ROOT / "semester-2").rglob("*.qmd")) + \
               list((ROOT / "semester-4").rglob("*.qmd")):
        try:
            text = qmd.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in IMG_RE.finditer(text):
            src = m.group(1).strip()
            if src.startswith(("http", "data:")):
                continue
            out.setdefault(src, []).append(str(qmd.relative_to(ROOT)))
    return out


def main() -> int:
    refs_map = refs()
    rows = []
    for src, pages in sorted(refs_map.items()):
        for base in [ROOT / p for p in pages[:1]]:
            path = (base.parent / src).resolve()
            if not path.is_file():
                rows.append((src, "MISSING", "", pages))
                break
            try:
                with Image.open(path) as im:
                    w, h = im.size
            except Exception:
                rows.append((src, "UNREADABLE", "", pages))
                break
            kb = path.stat().st_size // 1024
            flag = ""
            if min(w, h) < 800 and max(w, h) < 800:
                flag = "LOW"
            elif w < 1200:
                flag = "soft-on-retina"
            rows.append((src, f"{w}x{h}", f"{kb}KB", pages, flag))
            break
    low = [r for r in rows if "LOW" in r[-1]]
    soft = [r for r in rows if "soft" in r[-1]]
    print(f"images referenced: {len(rows)}, LOW (<800px): {len(low)}, soft-on-retina (<1200px wide): {len(soft)}")
    for r in low:
        print(f"  LOW {r[1]:>10} {r[2]:>8} {r[0]}  <- {r[3][0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
