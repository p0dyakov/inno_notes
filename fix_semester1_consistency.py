#!/usr/bin/env python3
"""
Fix naming consistency in semester-1 original .qmd files.

Rules applied:
1. Non-Lecture sources (Lab, Tutorial, Assignment, Problem Set, etc.)
   with "Example" → rename to "Task"
2. Lecture/Chapter sources with "Task" → rename to "Example"
3. "Lecture 6 Addition Part 1" / "Lecture 6 Addition Part 2" → "Lecture 6"
4. Reorder examples: Lab → Assignment/Problem Set → Lecture/Chapter →
   Tutorial → Test/Midterm/Final Recap → Mock → Test/Midterm/Final
5. Renumber all examples after changes
"""

import re
import subprocess
import sys
from pathlib import Path

BASE = Path("/Users/p0dyakov/Desktop/Projects/inno_notes/semester-1")

LECTURE_SOURCES = re.compile(r'^(Lecture|Chapter)\b')
NON_LECTURE_SOURCES = re.compile(
    r'^(Lab|Tutorial|Assignment|Problem Set|Practice|Workshop)\b'
)

SECTION_ORDER = [
    "Lab",
    "Assignment",
    "Problem Set",
    "Lecture",
    "Chapter",
    "Tutorial",
    "Test Recap",
    "Midterm Recap",
    "Final Recap",
    "Mock Test",
    "Mock Midterm",
    "Mock Final",
    "Test",
    "Midterm",
    "Final",
]


# ── helpers ───────────────────────────────────────────────────────────────────

def read(p):
    return p.read_text(encoding="utf-8")


def write(p, c):
    p.write_text(c, encoding="utf-8")
    print(f"  Updated: {p.relative_to(BASE)}")


def get_label(heading: str) -> str:
    """Return the last parenthesised group (the source label)."""
    all_matches = re.findall(r'\(([^)]+)\)', heading)
    return all_matches[-1] if all_matches else ""


def replace_label(heading: str, old_label: str, new_label: str) -> str:
    """Replace only the last occurrence of (old_label) with (new_label)."""
    idx = heading.rfind(f"({old_label})")
    if idx == -1:
        return heading
    return heading[:idx] + f"({new_label})" + heading[idx + len(f"({old_label})"):]


# ── Rule 1+2+3: fix Example/Task and normalize Lecture 6 Addition ─────────────

def fix_labels_in_file(path: Path) -> bool:
    content = read(path)
    lines = content.splitlines()
    changed = False

    new_lines = []
    for line in lines:
        original = line
        if not re.match(r'^#####\s+\*\*', line):
            new_lines.append(line)
            continue

        label = get_label(line)
        if not label:
            new_lines.append(line)
            continue

        parts = [p.strip() for p in label.split(",")]
        source = parts[0]
        item = parts[1] if len(parts) > 1 else ""

        # Rule 3: normalize "Lecture 6 Addition Part N" → "Lecture 6"
        source_fixed = re.sub(
            r'^(Lecture\s+\d+)\s+Addition.*$', r'\1', source
        )
        if source_fixed != source:
            new_label = ", ".join([source_fixed] + parts[1:])
            line = replace_label(line, label, new_label)
            label = new_label
            parts = [p.strip() for p in label.split(",")]
            source = parts[0]
            item = parts[1] if len(parts) > 1 else ""

        # Rule 1: non-Lecture source + "Example" → "Task"
        if NON_LECTURE_SOURCES.match(source) and item:
            # Replace "Example" token (with optional number/letter suffix)
            # e.g. "Example 1", "Example 3a", "Example" → "Task ..."
            new_item = re.sub(r'\bExample\b', 'Task', item)
            if new_item != item:
                new_label = ", ".join([source] + [new_item] + parts[2:])
                line = replace_label(line, label, new_label)
                label = new_label
                parts = [p.strip() for p in label.split(",")]
                item = parts[1] if len(parts) > 1 else ""

        # Rule 2: Lecture/Chapter source + "Task" → "Example"
        if LECTURE_SOURCES.match(source) and item:
            new_item = re.sub(r'\bTask\b', 'Example', item)
            if new_item != item:
                new_label = ", ".join([source] + [new_item] + parts[2:])
                line = replace_label(line, label, new_label)

        if line != original:
            changed = True
        new_lines.append(line)

    if changed:
        write(path, "\n".join(new_lines))
    return changed


# ── Rule 4: reorder examples section ─────────────────────────────────────────

def section_priority(label: str) -> int:
    for i, kw in enumerate(SECTION_ORDER):
        if label.startswith(kw):
            return i
    return len(SECTION_ORDER)


def sort_key(orig_idx: int, heading: str):
    all_matches = re.findall(r'\(([^)]+)\)', heading)
    label_full = all_matches[-1] if all_matches else ""
    parts = label_full.split(',')
    section_name = parts[0].strip()
    prio = section_priority(section_name)
    sec_num_m = re.search(r'(\d+)$', section_name)
    sec_num = int(sec_num_m.group(1)) if sec_num_m else 0
    item_type_prio = 0 if re.search(r'\bExample\b', parts[1] if len(parts) > 1 else '') else 1
    item_nums = tuple(int(x) for x in re.findall(r'\d+', parts[-1])) if len(parts) > 1 else ()
    if not item_nums:
        item_nums = (orig_idx,)
    return (prio, sec_num, item_type_prio) + item_nums


def reorder_examples_section(path: Path) -> bool:
    content = read(path)
    lines = content.split('\n')

    EXAMPLES_HEADER_RE = re.compile(r'^####\s+\*\*\d+\.\s+Examples')
    SECTION_HEADER_RE  = re.compile(r'^####\s+\*\*')

    examples_start = None
    examples_end = len(lines)

    for i, line in enumerate(lines):
        if EXAMPLES_HEADER_RE.match(line.strip()):
            examples_start = i
        elif examples_start is not None and SECTION_HEADER_RE.match(line.strip()):
            examples_end = i
            break

    if examples_start is None:
        return False

    pre   = lines[:examples_start + 1]
    inner = lines[examples_start + 1 : examples_end]
    post  = lines[examples_end:]

    entries = []
    pending_prefix = []

    for line in inner:
        if re.match(r'^#####\s+\*\*', line.strip()):
            entries.append([line, []])
        elif entries:
            entries[-1][1].append(line)
        else:
            pending_prefix.append(line)

    if not entries:
        return False

    indexed = list(enumerate(entries))
    sorted_indexed = sorted(indexed, key=lambda t: sort_key(t[0], t[1][0]))
    sorted_entries = [e for _, e in sorted_indexed]

    if [e[0] for e in entries] == [e[0] for e in sorted_entries]:
        return False

    # Detect prefix number (e.g. 4 or 3)
    file_prefix = None
    for entry in sorted_entries:
        m = re.search(r'\*\*(\d+)\.(\d+)\.', entry[0])
        if m:
            file_prefix = m.group(1)
            break

    if file_prefix:
        for idx, entry in enumerate(sorted_entries, start=1):
            entry[0] = re.sub(
                r'(\*\*)' + re.escape(file_prefix) + r'\.\d+\.',
                rf'\g<1>{file_prefix}.{idx}.',
                entry[0], count=1
            )

    new_inner = list(pending_prefix)
    for entry in sorted_entries:
        new_inner.append(entry[0])
        new_inner.extend(entry[1])

    new_lines = pre + new_inner + post
    new_content = '\n'.join(new_lines)

    if new_content != content:
        write(path, new_content)
        return True
    return False


# ── Rule 5: renumber using renumber_examples.py ───────────────────────────────

def renumber(path: Path):
    # Detect prefix from first ##### **N.M. heading
    content = read(path)
    m = re.search(r'^#####\s+\*\*(\d+)\.\d+\.', content, re.MULTILINE)
    if not m:
        return
    prefix = m.group(1)
    result = subprocess.run(
        [sys.executable, "renumber_examples.py", str(path), "--format", f"{prefix}.{{}}"],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print(f"  {result.stdout.strip()}")


# ── main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    changed_files = set()

    print("=== Rule 1+2+3: Fix Example/Task labels and Lecture 6 Addition ===")
    for qmd in sorted(BASE.rglob("*.qmd")):
        if fix_labels_in_file(qmd):
            changed_files.add(qmd)

    print(f"\n=== Rule 4: Reorder examples sections ===")
    for qmd in sorted(BASE.rglob("*.qmd")):
        if reorder_examples_section(qmd):
            changed_files.add(qmd)
        # If already ordered but labels changed, still renumber

    print(f"\n=== Rule 5: Renumber changed files ===")
    # Renumber ALL files that had label changes OR reordering
    # Also renumber files that had label changes (numbering may now be inconsistent)
    all_qmds = sorted(BASE.rglob("*.qmd"))
    for qmd in all_qmds:
        content = read(qmd)
        if re.search(r'^#####\s+\*\*\d+\.\d+\.', content, re.MULTILINE):
            renumber(qmd)

    print(f"\n=== Done. {len(changed_files)} files modified (labels/order). ===")
    print("Run python fix_formatting.py to regenerate ai_artifacts_review.")
