#!/usr/bin/env python3
"""Lossless PNG recompression for served article assets (in place).

Uses only pixel-preserving re-encoding (PIL optimize=True): DCT-free,
no quality change, no resize. Every file is gated: pixels (incl. alpha),
mode, size-count and animation frames must match, otherwise the file is
left untouched. Animated PNGs are skipped (PIL would drop frames).

Run: python3 scripts/recompress_png.py [--check]  (--check: report only)
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "semester-1", ROOT / "semester-2", ROOT / "semester-4"]


def apng(path: Path) -> bool:
    try:
        return getattr(Image.open(path), "n_frames", 1) > 1
    except Exception:
        return True


def process(path: Path, check: bool) -> tuple[str, int, int]:
    try:
        src = path.read_bytes()
        im = Image.open(io.BytesIO(src))
        if getattr(im, "n_frames", 1) > 1 or getattr(im, "is_animated", False):
            return ("animated-skip", len(src), len(src))
        mode = im.mode
        before = im.convert("RGBA").tobytes()
        buf = io.BytesIO()
        im.save(buf, format="PNG", optimize=True)
        out = buf.getvalue()
        im2 = Image.open(io.BytesIO(out))
        if im2.mode != mode or im2.convert("RGBA").tobytes() != before:
            return ("mismatch-skip", len(src), len(src))
        if not check and len(out) < len(src):
            path.write_bytes(out)
        return ("ok" if len(out) < len(src) else "kept", len(src), len(out))
    except Exception as e:  # noqa: BLE001
        return (f"error:{e}"[:60], 0, 0)


def main() -> int:
    check = "--check" in sys.argv
    files = [p for root in TARGETS for p in sorted(root.rglob("*.png"))
             if "_site" not in p.parts and "_freeze" not in p.parts]
    stats: dict[str, int] = {}
    b0 = b1 = saved_n = 0
    for p in files:
        status, a, b = process(p, check)
        stats[status] = stats.get(status, 0) + 1
        b0 += a
        b1 += b if status == "ok" else a
        if status == "ok":
            saved_n += 1
    print(f"files: {len(files)}, recompressed: {saved_n}")
    print(f"bytes: {b0 // 1024}KB -> {b1 // 1024}KB (saved {(b0 - b1) // 1024}KB)")
    print("status:", stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
