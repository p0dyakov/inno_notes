#!/usr/bin/env python3
"""Fix Problem Set 4 entries in DSA 4.qmd:
- Remove duplicate Problem 1 (keep first, remove second)
- Relabel fabricated exercises as Lecture 4
- Re-sort: Lecture 4 → Problem Set 4 → Homework
- Renumber sequentially
"""
import re

FILE_PATH = "Data Structures and Algorithms/4.qmd"

# Fabricated "Problem Set 4" exercises → relabel as Lecture 4
RELABEL = {
    "Problem Set 4, Exercise": "Lecture 4, Exercise",
    "Problem Set 4, Exercise 4.5": "Lecture 4, Exercise",
    "Problem Set 4, Exercise 4.6": "Lecture 4, Exercise",
    "Problem Set 4, Exercise 4.7": "Lecture 4, Exercise",
}

def get_sort_key(header, idx):
    if "(Lecture 4" in header:
        return (0, idx)
    if "(Problem Set 4" in header:
        return (1, idx)
    if "(Homework" in header:
        return (2, idx)
    return (99, idx)

with open(FILE_PATH, "r") as f:
    lines = f.read().split("\n")

ex_idx = next(i for i, l in enumerate(lines) if l.strip() == "#### **4. Examples**")
preamble = lines[:ex_idx + 1]
rest = lines[ex_idx + 1:]

# Parse blocks
blocks = []
cur = []
in_ex = False
for line in rest:
    if re.match(r'^##### \*\*4\.\d+', line):
        if in_ex and cur:
            blocks.append(cur)
        cur = [line]
        in_ex = True
    elif in_ex:
        cur.append(line)
if in_ex and cur:
    blocks.append(cur)

print(f"Found {len(blocks)} blocks")

# Step 1: Relabel fabricated exercises
for block in blocks:
    header = block[0]
    for old_label, new_label in RELABEL.items():
        if f"({old_label})" in header:
            block[0] = header.replace(f"({old_label})", f"({new_label})")
            print(f"  Relabeled: {old_label} → {new_label}")
            break

# Step 2: Remove duplicate Problem 1
# Find all "Problem Set 4, Problem 1" blocks, keep first, remove rest
ps4_p1_indices = []
for i, block in enumerate(blocks):
    if "(Problem Set 4, Problem 1)" in block[0]:
        ps4_p1_indices.append(i)

if len(ps4_p1_indices) > 1:
    print(f"  Found {len(ps4_p1_indices)} 'Problem Set 4, Problem 1' blocks, removing duplicates")
    for idx in reversed(ps4_p1_indices[1:]):  # Keep first, remove rest
        removed = blocks.pop(idx)
        print(f"    Removed: {removed[0][:100]}")

# Step 3: Sort
ib = list(enumerate(blocks))
ib.sort(key=lambda x: get_sort_key(x[1][0], x[0]))
blocks = [b for _, b in ib]

# Step 4: Renumber
for i, block in enumerate(blocks, 1):
    block[0] = re.sub(r'^(##### \*\*4\.)\d+(\.)', rf'\g<1>{i}\2', block[0])

# Write
result = preamble[:]
for b in blocks:
    result.extend(b)

with open(FILE_PATH, "w") as f:
    f.write("\n".join(result))

print(f"\nFinal {len(blocks)} blocks:")
for b in blocks:
    print(f"  {b[0][:130]}")
print(f"Done! {len(result)} lines")
