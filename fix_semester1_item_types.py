#!/usr/bin/env python3
"""
Fix item types and source names in semester-1 original .qmd files.

Changes applied:
SOURCE renames:
  Preparing for Final       -> Final Recap
  Practice Sheet            -> Problem Set
  Recap Session             -> Tutorial 11
  Additional Problems       -> Assignment 11
  Exercises                 -> Assignment 8
  Homework N / Homework     -> Assignment N
  Exercise 1 / Exercise 2   -> Lab 8  (ITP/8 only)

ITEM TYPE renames (in label after comma):
  Slide N                   -> Example N
  Question N                -> Task N
  Practice N                -> Task N
  Practice Problem N        -> Task N
  Warm-up N / Warm-Up N     -> Task N
  Additional Exercise N     -> Task N
  Optional Task N           -> Task N
  Tasks N                   -> Task N
  Examples N                -> Example N
  Demonstration N           -> Example N
  Theorem N                 -> Example N
  Proof N / Proof of...     -> Example N
  Lemma N                   -> Example N
  Linear Independence Example N -> Example N
  Discussion Question N     -> Task N

CA/9.qmd Part fixes:
  (Lecture 11, Part I, Concept)   -> (Lecture 11, Example N)
  (Lecture 11, Part II, Example)  -> (Lecture 11, Example N)
  (Lecture 11, Part I/II, ...)    -> strip Part, keep type

MathAn I/4.qmd Part fixes:
  Part I   -> Telescoping
  Part II  -> Nth-Term Test
  Part III -> Comparison Test
  Part IV  -> Ratio Test
  Part V   -> Root Test
  Homework H1/H2/H3 -> Task
"""

import re
import subprocess
import sys
from pathlib import Path

BASE = Path("/Users/p0dyakov/Desktop/Projects/inno_notes/semester-1")


def get_label(heading: str) -> str:
    all_matches = re.findall(r'\(([^)]+)\)', heading)
    return all_matches[-1] if all_matches else ""


def replace_label(heading: str, old_label: str, new_label: str) -> str:
    idx = heading.rfind(f"({old_label})")
    if idx == -1:
        return heading
    return heading[:idx] + f"({new_label})" + heading[idx + len(f"({old_label})"):]


def renumber(path: Path):
    content = path.read_text(encoding="utf-8")
    m = re.search(r'^#####\s+\*\*(\d+)\.\d+\.', content, re.MULTILINE)
    if not m:
        return
    prefix = m.group(1)
    result = subprocess.run(
        [sys.executable, "renumber_examples.py", str(path), "--format", f"{prefix}.{{}}"],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print(f"    {result.stdout.strip()}")


# ── per-line label transformation ─────────────────────────────────────────────

PART_MAP_MATHAN = {
    "Part I":   "Telescoping",
    "Part II":  "Nth-Term Test",
    "Part III": "Comparison Test",
    "Part IV":  "Ratio Test",
    "Part V":   "Root Test",
}

# Homework number -> Assignment number mapping (keep same week number)
def fix_homework_source(source: str) -> str:
    m = re.match(r'^Homework\s+(\d+)$', source)
    if m:
        return f"Assignment {m.group(1)}"
    if source == "Homework":
        return "Homework"  # handled separately with file context
    return source


def fix_item_type(item: str) -> str:
    """Normalize item type token, preserving trailing number/letter."""

    # Tasks N -> Task N
    item = re.sub(r'^Tasks\b', 'Task', item)
    # Examples N -> Example N
    item = re.sub(r'^Examples\b', 'Example', item)
    # Slide N -> Example N
    item = re.sub(r'^Slide\b', 'Example', item)
    # Demonstration -> Example
    item = re.sub(r'^Demonstration\b', 'Example', item)
    # Theorem N -> Example N
    item = re.sub(r'^Theorem\b', 'Example', item)
    # Proof ... -> Example N (strip "of ..." suffix, extract number if any)
    if re.match(r'^Proof\b', item):
        num = re.search(r'(\d+)', item)
        item = f"Example {num.group(1)}" if num else "Example"
    # Lemma -> Example
    item = re.sub(r'^Lemma\b', 'Example', item)
    # Linear Independence Example -> Example
    item = re.sub(r'^Linear Independence Example\b', 'Example', item)
    # Question N -> Task N
    item = re.sub(r'^Question\b', 'Task', item)
    # Discussion Question -> Task
    item = re.sub(r'^Discussion Question\b', 'Task', item)
    # Practice Problem N -> Task N
    item = re.sub(r'^Practice Problem\b', 'Task', item)
    # Practice N -> Task N
    item = re.sub(r'^Practice\b', 'Task', item)
    # Warm-up / Warm-Up -> Task
    item = re.sub(r'^Warm-[Uu]p\b', 'Task', item)
    # Additional Exercise -> Task
    item = re.sub(r'^Additional Exercise\b', 'Task', item)
    # Optional Task -> Task
    item = re.sub(r'^Optional Task\b', 'Task', item)
    # Homework HN -> Task (inside MathAn label after Part rename)
    item = re.sub(r'^Homework H\d+$', 'Task', item)

    return item


def transform_heading_default(line: str) -> str:
    """Apply source and item-type fixes to a single heading line."""
    label = get_label(line)
    if not label:
        return line

    parts = [p.strip() for p in label.split(",")]
    source = parts[0]
    changed = False

    # --- Source renames ---
    new_source = source
    if source == "Preparing for Final":
        new_source = "Final Recap"
    elif source == "Practice Sheet":
        new_source = "Problem Set"
    elif source == "Recap Session":
        new_source = "Tutorial 11"
    elif source == "Additional Problems":
        new_source = "Assignment 11"
    elif source == "Exercises":
        new_source = "Assignment 8"
    elif re.match(r'^Homework\s+\d+$', source):
        new_source = re.sub(r'^Homework', 'Assignment', source)
    elif source == "Homework":
        new_source = "Homework"  # left; handled in per-file overrides

    if new_source != source:
        parts[0] = new_source
        changed = True

    # --- Item type renames (parts[1] onward) ---
    if len(parts) > 1:
        new_item = fix_item_type(parts[1])
        if new_item != parts[1]:
            parts[1] = new_item
            changed = True

    if changed:
        new_label = ", ".join(parts)
        line = replace_label(line, label, new_label)

    return line


def transform_heading_ca9(line: str, example_counter: list) -> str:
    """CA/9: remove Part I/II, unify to (Lecture 11, Example N)."""
    label = get_label(line)
    if not label:
        return line
    parts = [p.strip() for p in label.split(",")]
    if parts[0] != "Lecture 11":
        return line
    # Remove Part I/II entries, determine final type
    filtered = [p for p in parts[1:] if not re.match(r'^Part\s+(I|II)$', p)]
    # Determine Example vs Task
    item_type = "Example"
    for p in filtered:
        if re.match(r'^(Concept|concept)', p):
            item_type = "Example"  # lecture concept demo
        elif re.match(r'^(Task|task)', p):
            item_type = "Example"  # lecture tasks are examples per rule
    example_counter[0] += 1
    new_label = f"Lecture 11, {item_type} {example_counter[0]}"
    return replace_label(line, label, new_label)


def transform_heading_mathan4(line: str) -> str:
    """MathAn I/4: rename Part I-V, Homework HN -> Task."""
    label = get_label(line)
    if not label:
        return line
    parts = [p.strip() for p in label.split(",")]
    changed = False

    new_parts = []
    for p in parts:
        orig = p
        # Part rename
        for part_key, part_val in PART_MAP_MATHAN.items():
            if p == part_key:
                p = part_val
                break
        # Homework HN -> Task
        p = re.sub(r'^Homework H\d+$', 'Task', p)
        if p != orig:
            changed = True
        new_parts.append(p)

    if changed:
        new_label = ", ".join(new_parts)
        line = replace_label(line, label, new_label)

    return line


# ── process file ──────────────────────────────────────────────────────────────

EXAMPLES_HEADER_RE = re.compile(r'^####\s+\*\*\d+\.\s+Examples')
SECTION_HEADER_RE  = re.compile(r'^####\s+\*\*')


def process_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    new_lines = []
    changed = False
    in_examples = False

    is_ca9     = path.parts[-2] == "Computer Architecture" and path.stem == "9"
    is_mathan4 = path.parts[-2] == "Mathematical Analysis I" and path.stem == "4"

    ca9_counter = [0]  # mutable for closure

    for line in lines:
        s = line.strip()
        if EXAMPLES_HEADER_RE.match(s):
            in_examples = True
        elif in_examples and SECTION_HEADER_RE.match(s) and not EXAMPLES_HEADER_RE.match(s):
            in_examples = False

        if in_examples and re.match(r'^#####\s+\*\*', s):
            if is_ca9:
                new_line = transform_heading_ca9(line, ca9_counter)
            elif is_mathan4:
                new_line = transform_heading_mathan4(line)
                new_line = transform_heading_default(new_line)  # also apply general fixes
            else:
                new_line = transform_heading_default(line)

            if new_line != line:
                changed = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if changed:
        path.write_text("\n".join(new_lines), encoding="utf-8")
        print(f"  Updated: {path.relative_to(BASE)}")

    return changed


# ── main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    changed_files = []

    print("=== Fixing item types and sources ===")
    for qmd in sorted(BASE.rglob("*.qmd")):
        if process_file(qmd):
            changed_files.append(qmd)

    print(f"\n=== Renumbering {len(changed_files)} changed files ===")
    for qmd in changed_files:
        renumber(qmd)

    print(f"\nDone. {len(changed_files)} files modified.")
    print("Run: python fix_formatting.py")
