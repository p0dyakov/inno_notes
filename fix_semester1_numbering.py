#!/usr/bin/env python3
"""
Fix remaining issues in semester-1:

1. Slide N -> Example N, but renumber sequentially per (source, type) group
   (not preserving slide number)
2. Homework H1/H2/H3 in MathAn I/4 -> revert back to Homework H1 etc
   (was incorrectly changed to Task)
3. Recap Session in ITP/10 and LDM/9 -> revert back to Recap Session
   (was incorrectly reverted to Tutorial 11 then partially fixed)
4. Bare Task / Example (no number) -> add sequential number per (file, source, type)
"""

import re
import subprocess
import sys
from pathlib import Path

BASE = Path("/Users/p0dyakov/Desktop/Projects/inno_notes/semester-1")

EXAMPLES_HEADER_RE = re.compile(r'^####\s+\*\*\d+\.\s+Examples')
SECTION_HEADER_RE  = re.compile(r'^####\s+\*\*')


def get_label(line):
    m = re.findall(r'\(([^)]+)\)', line)
    return m[-1] if m else ""


def replace_label(line, old, new):
    idx = line.rfind(f"({old})")
    if idx == -1:
        return line
    return line[:idx] + f"({new})" + line[idx + len(f"({old})"):]


def renumber_file(path: Path):
    content = path.read_text(encoding="utf-8")
    m = re.search(r'^#####\s+\*\*(\d+)\.\d+\.', content, re.MULTILINE)
    if not m:
        return
    prefix = m.group(1)
    r = subprocess.run(
        [sys.executable, "renumber_examples.py", str(path), "--format", f"{prefix}.{{}}"],
        capture_output=True, text=True
    )
    if r.stdout.strip():
        print(f"    {r.stdout.strip()}")


def process_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    new_lines = []
    changed = False
    in_examples = False

    is_mathan4 = path.parts[-2] == "Mathematical Analysis I" and path.stem == "4"

    # Per-(source, type_word) counters for renumbering Slide and bare Task/Example
    slide_counters: dict[str, int] = {}
    bare_counters: dict[str, int] = {}

    for line in lines:
        s = line.strip()
        if EXAMPLES_HEADER_RE.match(s):
            in_examples = True
        elif in_examples and SECTION_HEADER_RE.match(s) and not EXAMPLES_HEADER_RE.match(s):
            in_examples = False

        if not (in_examples and re.match(r'^#####\s+\*\*', s)):
            new_lines.append(line)
            continue

        label = get_label(line)
        if not label:
            new_lines.append(line)
            continue

        parts = [p.strip() for p in label.split(",")]
        source = parts[0]
        item = parts[1] if len(parts) > 1 else ""

        # Fix 1: MathAn I/4 — restore Homework HN for (Lab 10, Category, Task)
        # Original was (Lab 10, Part X, Homework HN), now (Lab 10, Category, Task)
        # The H-number corresponds to which "round" within each category:
        # 1st Task in category -> H1, 2nd -> H2, 3rd -> H3
        if is_mathan4 and len(parts) == 3 and parts[2] == "Task":
            category = parts[1]
            key = f"mathan4_homework|{category}"
            bare_counters[key] = bare_counters.get(key, 0) + 1
            new_item = f"Homework H{bare_counters[key]}"
            new_label = ", ".join([source, category, new_item])
            line = replace_label(line, label, new_label)
            changed = True
            new_lines.append(line)
            continue

        # Fix 2: Slide N -> Example, renumber sequentially
        if re.match(r'^Slide\s+\d+$', item):
            key = f"{source}|Example"
            slide_counters[key] = slide_counters.get(key, 0) + 1
            new_item = f"Example {slide_counters[key]}"
            new_label = ", ".join([source, new_item] + parts[2:])
            line = replace_label(line, label, new_label)
            changed = True
            new_lines.append(line)
            continue

        # Fix 3: bare Task or Example (exactly, no number) -> add sequential number
        if re.match(r'^(Task|Example)$', item):
            type_word = item  # "Task" or "Example"
            key = f"{source}|{type_word}"
            bare_counters[key] = bare_counters.get(key, 0) + 1
            new_item = f"{type_word} {bare_counters[key]}"
            new_label = ", ".join([source, new_item] + parts[2:])
            line = replace_label(line, label, new_label)
            changed = True

        new_lines.append(line)

    if changed:
        path.write_text("\n".join(new_lines), encoding="utf-8")
        print(f"  Updated: {path.relative_to(BASE)}")

    return changed


if __name__ == "__main__":
    changed_files = []

    print("=== Fixing Slide numbering and bare Task/Example ===")
    for qmd in sorted(BASE.rglob("*.qmd")):
        if process_file(qmd):
            changed_files.append(qmd)

    print(f"\n=== Renumbering {len(changed_files)} files ===")
    for qmd in changed_files:
        renumber_file(qmd)

    print(f"\nDone. {len(changed_files)} files modified.")
    print("Run: python fix_formatting.py")
