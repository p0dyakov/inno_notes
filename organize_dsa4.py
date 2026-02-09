#!/usr/bin/env python3
"""Sort examples in DSA 4.qmd: Lecture 4 → Problem Set 4 → Homework Coding Exercise."""
import re

FILE_PATH = "Data Structures and Algorithms/4.qmd"

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

# Find examples header
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

# Sort preserving relative order within groups
ib = list(enumerate(blocks))
ib.sort(key=lambda x: get_sort_key(x[1][0], x[0]))
blocks = [b for _, b in ib]

# Renumber
for i, block in enumerate(blocks, 1):
    block[0] = re.sub(r'^(##### \*\*4\.)\d+(\.)', rf'\g<1>{i}\2', block[0])

# Write
result = preamble[:]
for b in blocks:
    result.extend(b)

with open(FILE_PATH, "w") as f:
    f.write("\n".join(result))

for b in blocks:
    print(f"  {b[0][:120]}")
print(f"Done! {len(result)} lines")
