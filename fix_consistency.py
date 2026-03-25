#!/usr/bin/env python3
"""Fix naming consistency in semester-2 original .qmd files.

Rules:
1. (Tutorial, X)          -> (Tutorial 1, X)      [AGLA/1.qmd]
2. (Assignment 1, Example N) -> (Assignment 1, Task N)  [AGLA/1.qmd]
3. (Lab 2, Example)       -> (Lab 2, Task)         [TCS/3.qmd]
4. bare (Task X.Y)        -> (Lecture 2, Task X.Y) [TCS/2.qmd]
5. Reorder example sections: Lab -> Assignment/Problem Set -> Lecture -> Tutorial -> Midterm/Test

Section order applies ONLY to the ##### headings inside "#### **4. Examples**".
Within each section the original relative order is preserved.
"""

import re
from pathlib import Path

BASE = Path("/Users/p0dyakov/Desktop/Projects/inno_notes/semester-2")

# ── helpers ───────────────────────────────────────────────────────────────────

def read(p): return p.read_text(encoding="utf-8")
def write(p, c): p.write_text(c, encoding="utf-8"); print(f"  Updated: {p.relative_to(BASE)}")

# ── label fixes (rules 1-4) ──────────────────────────────────────────────────

def fix_labels(path: Path, rules: list[tuple]) -> bool:
    """Apply a list of (old, new) simple string substitutions."""
    content = read(path)
    new = content
    for old, new_str in rules:
        new = new.replace(old, new_str)
    if new != content:
        write(path, new)
        return True
    print(f"  No change: {path.relative_to(BASE)}")
    return False

def fix_labels_re(path: Path, pattern: str, repl: str) -> bool:
    content = read(path)
    new = re.sub(pattern, repl, content)
    if new != content:
        write(path, new)
        return True
    print(f"  No change: {path.relative_to(BASE)}")
    return False

# ── section ordering ──────────────────────────────────────────────────────────

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
# Within a section: Example type before Task type
ITEM_TYPE_ORDER = {"Example": 0, "Concept": 1, "Practice Problem": 1}


def section_priority(label: str) -> int:
    for i, kw in enumerate(SECTION_ORDER):
        if label.startswith(kw):
            return i
    return len(SECTION_ORDER)


def sort_key(orig_idx: int, heading: str):
    """(section_prio, sec_num, item_type_prio, *item_nums, orig_idx)"""
    # The context label is always the LAST parenthesised group in the heading.
    # Using findall to get all matches and picking the last one avoids false
    # matches on LaTeX expressions like $O(2^n)$ that appear earlier in the line.
    all_matches = re.findall(r'\(([^)]+)\)', heading)
    label_full = all_matches[-1] if all_matches else ""
    parts = label_full.split(',')

    section_name = parts[0].strip()
    prio = section_priority(section_name)

    sec_num_m = re.search(r'(\d+)$', section_name)
    sec_num = int(sec_num_m.group(1)) if sec_num_m else 0

    item_type_prio = 1
    if len(parts) > 1:
        item_str = parts[1].strip()
        for kw, kprio in ITEM_TYPE_ORDER.items():
            if item_str.startswith(kw):
                item_type_prio = kprio
                break

    # Parse item numbers from last part (e.g. "Task 5.2" -> (5, 2))
    item_nums = tuple(int(x) for x in re.findall(r'\d+', parts[-1])) if len(parts) > 1 else ()
    if not item_nums:
        item_nums = (orig_idx,)

    return (prio, sec_num, item_type_prio) + item_nums


def reorder_examples_section(path: Path) -> bool:
    """
    Find the #### **4. Examples** section in the file and reorder the
    ##### **X.Y. Title** (Context, Item) headings within it.

    Each "entry" is a heading line plus the block of content that follows it
    (until the next heading or end of Examples section).
    """
    content = read(path)
    lines = content.split('\n')

    # Locate Examples section boundaries
    examples_start = None
    examples_end = len(lines)
    EXAMPLES_HEADER_RE = re.compile(r'^####\s+\*\*\d+\.\s+Examples')
    SECTION_HEADER_RE  = re.compile(r'^####\s+\*\*')

    for i, line in enumerate(lines):
        if EXAMPLES_HEADER_RE.match(line.strip()):
            examples_start = i
        elif examples_start is not None and SECTION_HEADER_RE.match(line.strip()):
            examples_end = i
            break

    if examples_start is None:
        print(f"  No Examples section: {path.relative_to(BASE)}")
        return False

    pre   = lines[:examples_start + 1]        # everything up to and including #### header
    inner = lines[examples_start + 1 : examples_end]
    post  = lines[examples_end:]

    # Split inner into entries keyed by ##### headings
    entries = []   # list of (heading_line, [content_lines])
    pending_prefix = []  # lines before first heading

    for line in inner:
        if re.match(r'^#####\s+\*\*', line.strip()):
            if entries:
                entries[-1][1].append('')  # normalise trailing blank
            entries.append([line, []])
        elif entries:
            entries[-1][1].append(line)
        else:
            pending_prefix.append(line)

    if not entries:
        print(f"  No ##### entries in Examples: {path.relative_to(BASE)}")
        return False

    # Sort
    indexed = list(enumerate(entries))
    sorted_indexed = sorted(indexed, key=lambda t: sort_key(t[0], t[1][0]))
    sorted_entries = [e for _, e in sorted_indexed]

    if [e[0] for e in entries] == [e[0] for e in sorted_entries]:
        print(f"  Already ordered: {path.relative_to(BASE)}")
        return False

    # Renumber X.Y prefix sequentially
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

    # Rebuild
    new_inner = list(pending_prefix)
    for entry in sorted_entries:
        new_inner.append(entry[0])
        new_inner.extend(entry[1])

    new_lines = pre + new_inner + post
    new_content = '\n'.join(new_lines)

    if new_content != content:
        write(path, new_content)
        return True
    print(f"  Already ordered: {path.relative_to(BASE)}")
    return False


# ── main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Rule 1+2: AGLA II / 1.qmd
    print("=== Rule 1+2: AGLA II/1.qmd ===")
    fix_labels_re(
        BASE / "Analytical Geometry and Linear Algebra II" / "1.qmd",
        r'\(Tutorial, ',
        '(Tutorial 1, '
    )
    fix_labels_re(
        BASE / "Analytical Geometry and Linear Algebra II" / "1.qmd",
        r'\(Assignment 1, Example (\d+)\)',
        r'(Assignment 1, Task \1)'
    )

    # Rule 3: TCS / 3.qmd
    print("\n=== Rule 3: TCS/3.qmd ===")
    fix_labels(
        BASE / "Theoretical Computer Science" / "3.qmd",
        [('(Lab 2, Example)', '(Lab 2, Task)')]
    )

    # Rule 4: TCS / 2.qmd  — bare (Task X.Y) -> (Lecture 2, Task X.Y)
    print("\n=== Rule 4: TCS/2.qmd ===")
    fix_labels_re(
        BASE / "Theoretical Computer Science" / "2.qmd",
        r'\(Task (\d+\.\d+)\)',
        r'(Lecture 2, Task \1)'
    )

    # Rule 5: reorder examples in all semester-2 files
    # Skip Mathematical Analysis II/1.qmd (400 examples, by policy)
    skip = {BASE / "Mathematical Analysis II" / "1.qmd"}
    print("\n=== Rule 5: Reorder Examples sections ===")
    for qmd in sorted(BASE.rglob("*.qmd")):
        if qmd in skip:
            print(f"  Skipped (policy): {qmd.relative_to(BASE)}")
            continue
        reorder_examples_section(qmd)

    print("\nDone.")
