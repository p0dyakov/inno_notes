#!/usr/bin/env python3
"""One-off: remove ALL Pitfalls blocks (user decision: banned pattern).

Removes:
  A. headings  #####/###### containing Pitfall(s) + body up to next heading
     of same-or-higher level;
  B. top-level bullets  -/** **(Key|Common )?Pitfall(s):** + nested content
     (deeper-indented lines) + surrounding blanks (normalized later).

Safety: fence parity (even ``` count before/after, no fence inside removed
bullet ranges, no #### inside removed heading ranges). Dry-run by default;
pass --apply to write. Prints a per-file report.
"""
import re
import sys
from pathlib import Path

HEAD_RE = re.compile(r'^(#{5,6})\s.*[Pp]itfall')
BULLET_RE = re.compile(r'^[*-] \*\*(Key |Common )?Pitfalls?:\*\*')
ANY_HEAD_RE = re.compile(r'^(#{1,6})\s')


def fence_count(lines):
    return sum(1 for l in lines if l.strip().startswith('```'))


def list_indent(line):
    m = re.match(r'^(\s*)', line)
    return len(m.group(1))


def remove_from_lines(lines):
    """Return (new_lines, removed_report). removed_report: list of strings."""
    out = []
    removed = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        mh = HEAD_RE.match(line)
        mb = BULLET_RE.match(line)
        if mh:
            level = len(mh.group(1))
            j = i + 1
            while j < n:
                m2 = ANY_HEAD_RE.match(lines[j])
                if m2 and len(m2.group(1)) <= level:
                    break
                j += 1
            chunk = lines[i:j]
            for cl in chunk:
                if cl.strip().startswith('```'):
                    raise ValueError('fence inside removed heading range at line ' + str(i + 1))
                mtop = re.match(r'^(#{1,4})\s', cl)
                if mtop:
                    raise ValueError('top heading inside removed range at line ' + str(i + 1))
            removed.append('H line ' + str(i + 1) + ': ' + line.strip()[:90] + ' (+' + str(j - i - 1) + ' body lines)')
            i = j
            continue
        if mb:
            j = i + 1
            while j < n and lines[j].strip() == '':
                j += 1
            while j < n and lines[j].strip() != '' and list_indent(lines[j]) > 0:
                if lines[j].strip().startswith('```'):
                    raise ValueError('fence inside removed bullet range at line ' + str(i + 1))
                j += 1
            removed.append('B line ' + str(i + 1) + ': ' + line.strip()[:90] + ' (+' + str(j - i - 1) + ' cont lines)')
            i = j
            continue
        out.append(line)
        i += 1
    # collapse 3+ blanks -> 2 outside fences (cosmetic, markdown-safe)
    res = []
    blanks = 0
    in_fence = False
    for line in out:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            blanks = 0
            res.append(line)
            continue
        if in_fence:
            res.append(line)
            continue
        if line.strip() == '':
            blanks += 1
            if blanks <= 2:
                res.append(line)
            continue
        blanks = 0
        res.append(line)
    return res, removed


def main():
    apply = '--apply' in sys.argv
    files = sorted(Path('.').glob('semester-*/*/*.qmd'))
    total_h = 0
    total_b = 0
    for f in files:
        lines = f.read_text(encoding='utf-8').splitlines()
        before_parity = fence_count(lines) % 2
        try:
            new_lines, removed = remove_from_lines(lines)
        except ValueError as e:
            print('SKIP (' + str(e) + '): ' + str(f))
            continue
        if not removed:
            continue
        if fence_count(new_lines) % 2 != before_parity:
            print('SKIP (fence parity changed): ' + str(f))
            continue
        print('FILE ' + str(f) + ' delta_lines=' + str(len(new_lines) - len(lines)))
        for r in removed:
            print('   ' + r)
            if r.startswith('H'):
                total_h += 1
            else:
                total_b += 1
        if apply:
            f.write_text(chr(10).join(new_lines) + chr(10), encoding='utf-8')
    print('TOTAL headings=' + str(total_h) + ' bullets=' + str(total_b) + (' APPLIED' if apply else ' DRY-RUN'))


main()
