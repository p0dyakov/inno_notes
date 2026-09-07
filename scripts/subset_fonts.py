#!/usr/bin/env python3
"""Subset self-hosted woff2 fonts from full sources (+ auto new-glyph pickup).

Why: full SF/Archivo/Mono files are ~1MB each; every article loads 4-7 of
them (~5-8MB of fonts per page open). Subsetting to what the site uses
shrinks each file ~10x with zero visible change.

How new glyphs get picked up automatically: every run audits ALL .qmd +
_includes sources for used codepoints and unions them with the base
blocks. A newly used symbol (e.g. ★ or a CJK char) lands in the next
build by itself — no manual range edits.

Layout: full originals live in styles/fonts-src/ (committed, ~17MB);
built subsets go to styles/fonts/ (what the site serves).
Runs in _quarto.yml pre-render and render_changed serial section; a
fingerprint (scripts/subset-fonts-fingerprint.json) makes no-op runs
take ~1s. Deterministic: files are rewritten only on byte change.

Requires: pip install "fonttools==4.61.1" "brotli==1.2.0"
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "styles" / "fonts-src"
DST = ROOT / "styles" / "fonts"
FINGERPRINT = ROOT / "scripts" / "subset-fonts-fingerprint.json"
FONTTOOLS_PIN = "4.61.1"

# Always-kept blocks (audited baseline: latin, phonetics, greek, cyrillic,
# punctuation, math/tech symbols, checks, box drawings — see git history).
BASE_RANGES = [
    (0x0000, 0x024F), (0x02B0, 0x02FF), (0x0300, 0x036F), (0x0370, 0x03FF),
    (0x0400, 0x04FF), (0x1D00, 0x1D7F), (0x1F00, 0x1FFF), (0x2000, 0x206F),
    (0x2070, 0x209F), (0x20A0, 0x20CF), (0x2100, 0x214F), (0x2190, 0x21FF),
    (0x2200, 0x22FF), (0x2300, 0x23FF), (0x2500, 0x257F), (0x25A0, 0x25FF),
    (0x2600, 0x26FF), (0x2700, 0x27BF), (0x2764, 0x2764), (0x27C0, 0x27EF),
    (0xFB00, 0xFB06), (0xFEFF, 0xFEFF), (0xFFFD, 0xFFFD),
]

AUDIT_GLOBS = ["semester-1/**/*.qmd", "semester-2/**/*.qmd",
               "semester-4/**/*.qmd", "index.qmd", "_includes/*.html"]


def audited_codepoints() -> set[int]:
    used: set[int] = set()
    for pattern in AUDIT_GLOBS:
        for p in sorted(ROOT.glob(pattern)):
            if "_site" in p.parts or "_freeze" in p.parts:
                continue
            try:
                used.update(map(ord, p.read_text(encoding="utf-8")))
            except OSError:
                pass
    return used


def compress_ranges(points: set[int]) -> list[tuple[int, int]]:
    pts = sorted(points)
    out: list[tuple[int, int]] = []
    for cp in pts:
        if out and cp == out[-1][1] + 1:
            out[-1] = (out[-1][0], cp)
        else:
            out.append((cp, cp))
    return out


def unicodes_arg(used: set[int]) -> str:
    in_base = lambda cp: any(a <= cp <= b for a, b in BASE_RANGES)  # noqa: E731
    extra = {cp for cp in used if not in_base(cp)}
    parts = [f"U+{a:04X}" + (f"-{b:04X}" if b > a else "")
             for a, b in BASE_RANGES]
    parts += [f"U+{a:04X}" + (f"-{b:04X}" if b > a else "")
              for a, b in compress_ranges(extra)]
    return ",".join(parts)


def file_hash(p: Path) -> str:
    h = hashlib.sha1()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fingerprint(unicodes: str) -> dict:
    try:
        import fontTools
        tool_ver = str(getattr(fontTools, "version", "?"))
    except ImportError:
        tool_ver = "missing"
    fonts = sorted(SRC.glob("*.woff2"))
    fh = {p.name: file_hash(p) for p in fonts}
    sh = hashlib.sha1()
    for pattern in AUDIT_GLOBS:
        for p in sorted(ROOT.glob(pattern)):
            if "_site" in p.parts or "_freeze" in p.parts:
                continue
            try:
                sh.update(str(p.relative_to(ROOT)).encode())
                sh.update(p.read_bytes())
            except OSError:
                pass
    return {"fonttools": tool_ver, "fonts": fh, "sources": sh.hexdigest(),
            "unicodes": unicodes}


def main() -> int:
    try:
        import fontTools  # noqa: F401
        if str(getattr(fontTools, "version", "?")) != FONTTOOLS_PIN:
            print(f"WARN: fontTools {fontTools.version} != pin {FONTTOOLS_PIN}; "
                  f"bytes may differ. pip install \"fonttools=={FONTTOOLS_PIN}\"")
    except ImportError:
        print("ERROR: fonttools missing. pip install \"fonttools==4.61.1\" \"brotli==1.2.0\"")
        return 1
    if not SRC.is_dir() or not list(SRC.glob("*.woff2")):
        print("ERROR: styles/fonts-src/ missing full fonts")
        return 1
    used = audited_codepoints()
    unicodes = unicodes_arg(used)
    fp = fingerprint(unicodes)
    if FINGERPRINT.is_file():
        try:
            if json.loads(FINGERPRINT.read_text(encoding="utf-8")) == fp:
                print(f"subset-fonts: fresh ({len(used)} codepoints audited)")
                return 0
        except (OSError, ValueError):
            pass
    DST.mkdir(parents=True, exist_ok=True)
    changed = 0
    for name in sorted(fp["fonts"]):
        src, dst = SRC / name, DST / name
        tmp = dst.with_suffix(".woff2.tmp")
        r = subprocess.run(
            [sys.executable, "-m", "fontTools.subset", str(src),
             f"--unicodes={unicodes}", "--layout-features=*",
             "--flavor=woff2", f"--output-file={tmp}"],
            capture_output=True, text=True)
        if r.returncode != 0:
            print(f"FAIL {name}: {r.stderr[-400:]}")
            tmp.unlink(missing_ok=True)
            return 1
        new_bytes = tmp.read_bytes()
        old_bytes = dst.read_bytes() if dst.is_file() else b""
        if new_bytes != old_bytes:
            tmp.replace(dst)
            changed += 1
            print(f"subset {name}: {len(old_bytes) // 1024}KB -> {len(new_bytes) // 1024}KB")
        else:
            tmp.unlink()
    FINGERPRINT.write_text(json.dumps(fp, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"subset-fonts: {changed} file(s) updated, fingerprint written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
