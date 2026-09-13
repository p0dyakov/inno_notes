#!/usr/bin/env python3
"""Deterministic gate: practice source labels must resolve to real transcript files.

Every `##### **N.M. Title** (Source K, Task|Example T)` heading in a managed
article must name a transcript file that actually exists in the article's
inno_files week folder, e.g. `(Lecture 1, Task 2)` requires a `Lecture*.md`
transcript next to the week's other sources.

Catches invented attributions (audit Sept 2026: DE/1 cited `Lecture 1` when
its week only ships `Chapter.md`).

Verifiable kinds (must match a transcript stem; `-2`/suffix variants count,
e.g. `Tutorial-2.md` satisfies `Tutorial`):
  Lab, Lecture, Tutorial, Chapter, Homework, Assignment, Exercises
Skipped (no transcript counterpart by design): Test, Midterm, Final,
  Practice Sheet, Additional Problems, Preparing for Final, Mock Midterm,
  Problem Set, Sample*, topic-style labels without Task/Example, and
  HANDWRITTEN/QUARANTINE-locked files (manual ownership: validated strictly,
  but never auto-rewritten by --fix).

Boundary: only the source KIND is verified (file existence). Task/Example
numbers for Chapter-style sources are article-local self-checks and are NOT
verified against transcript text.

Usage:
  validate_practice_sources.py --inno-files PATH [--semester S] [qmd ...]
  validate_practice_sources.py --inno-files PATH --fix [qmd ...]
Without qmd args, scans all managed-semester articles. Exit 1 on violations.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENT = Path(__file__).resolve().parent

# Kept in sync with fix_formatting.py (which runs on import, so cannot be
# imported here — same reason generate.py duplicates TITLE_WEEK_RE).
TOP_SECTION_RE = re.compile(r'^####\s+\*\*(\d+)\.\s+(.+?)\*\*\s*$')
PRACTICE_HEADING_RE = re.compile(r'^#####\s+\*\*(\d+)\.(\d+)\.\s+(.+?)(?:\*\*\s+\((.+)\))?\s*$')
SOURCE_RE = re.compile(
    r'^(Lab|Lecture|Tutorial|Chapter|Midterm|Final|Test|Homework'
    r'|Practice Sheet|Exercises|Additional Problems|Preparing for Final'
    r'|Mock Midterm|Assignment|Problem Set)'
    r'(?:\s+([^,]+))?,\s+'
    r'(?:(Example|Task|Tasks)\s+([\w\.\-& ]+)'
    r'|(.+))$'
)

VERIFIABLE = {
    'Lab': ['Lab'],
    'Lecture': ['Lecture'],
    'Tutorial': ['Tutorial'],
    'Chapter': ['Chapter'],
    'Homework': ['Homework'],
    'Assignment': ['Assignment'],
    'Exercises': ['Exercises'],
}

LOCK_MARKS = ('<!-- HANDWRITTEN -->', '<!-- QUARANTINE -->')


def load_registry(semester):
    p = ROOT / semester / 'course_map.json'
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding='utf-8')).get('courses', {})


def managed_semesters():
    return sorted(
        d.name for d in ROOT.iterdir()
        if d.is_dir() and re.fullmatch(r'semester-\d+', d.name)
        and (d / 'course_map.json').exists())


def article_course_week(qmd, semester):
    """(course_code, week_digits) for an article path, or (None, None)."""
    try:
        rel = Path(qmd).relative_to(ROOT / semester)
    except ValueError:
        return None, None
    if len(rel.parts) < 2:
        return None, None
    course_full, week = rel.parts[0], Path(rel.parts[1]).stem
    courses = load_registry(semester)
    if course_full in courses:
        return course_full, week
    for c, entry in courses.items():
        if entry.get('name') == course_full:
            return c, week
    return None, None


def week_stems(qmd, inno_files, semester):
    """Transcript stems (Lecture, Tutorial-2, ...) for the article's week dir."""
    try:
        rel = Path(qmd).relative_to(ROOT / semester)
    except ValueError:
        return None
    if len(rel.parts) < 2:
        return None
    course_full, week = rel.parts[0], Path(rel.parts[1]).stem
    courses = load_registry(semester)
    code = None
    if course_full in courses:
        code = course_full
    else:
        for c, entry in courses.items():
            if entry.get('name') == course_full:
                code = c
                break
    if code is None:
        return None
    cdir = Path(inno_files) / semester / code
    if not cdir.is_dir():
        return None
    for wd in sorted(cdir.iterdir()):
        if not wd.is_dir():
            continue
        digits = re.match(r'(\d+)', wd.name)
        if digits and digits.group(1) == week.lstrip('0') or digits and digits.group(1) == week:
            return [md.stem for md in sorted(wd.glob('*.md')) if md.name != 'Syllabus.md']
    return None


def course_week_stems(code, inno_files, semester):
    """All week dirs of a course: {week_digits: [stems]}."""
    cdir = Path(inno_files) / semester / code
    out = {}
    if not cdir.is_dir():
        return out
    for wd in sorted(cdir.iterdir()):
        if not wd.is_dir():
            continue
        m = re.match(r'(\d+)', wd.name)
        if not m:
            continue
        out[m.group(1)] = [md.stem for md in sorted(wd.glob('*.md'))
                            if md.name != 'Syllabus.md']
    return out


def resolve_kind(code, week, kind, inno_files, semester):
    """'same-week' if the kind ships in the article's own week,
    'cross-week:<w>' if it ships in another week of the same course,
    None if the kind exists nowhere in the course (invented)."""
    weeks = course_week_stems(code, inno_files, semester)
    if kind_present(kind, weeks.get(week, []) + weeks.get(week.lstrip('0'), [])):
        return 'same-week'
    for w, stems in sorted(weeks.items()):
        if kind_present(kind, stems):
            return 'cross-week:' + w
    return None


def kind_present(kind, stems):
    return any(s == kind or s.startswith(kind + '-') or s.startswith(kind + ' ')
               for k in VERIFIABLE.get(kind, [kind]) for s in stems)


def iter_practice_labels(lines):
    """Yield (line_no, label) for practice headings carrying a source label."""
    in_practice = False
    for i, line in enumerate(lines, start=1):
        s = line.strip()
        m = TOP_SECTION_RE.match(s)
        if m:
            in_practice = (m.group(2) == 'Practice')
            continue
        if not in_practice or not s.startswith('#####'):
            continue
        pm = PRACTICE_HEADING_RE.match(s)
        if pm and pm.group(4):
            yield i, pm.group(4)


def validate_text(text, stems):
    """Legacy entry: same-week stems only. Prefer validate_mapped()."""
    out = []
    for no, label in iter_practice_labels(text.splitlines()):
        m = SOURCE_RE.match(label)
        if not m:
            continue
        kind = m.group(1)
        if kind not in VERIFIABLE:
            continue
        if not kind_present(kind, stems):
            have = sorted({s.split('-')[0].split(' ')[0] for s in stems})
            out.append(
                f'Line {no}: source `{kind}` has no transcript file '
                f'(week ships: {", ".join(have) or "nothing"}). Found `({label})`.')
    return out


def validate_mapped(text, code, week, inno_files, semester):
    """Returns (violations, notes). Cross-week refs are notes, not violations:
    the file exists, but a W<N> article practising another week's tasks
    deserves a human glance."""
    violations, notes = [], []
    for no, label in iter_practice_labels(text.splitlines()):
        m = SOURCE_RE.match(label)
        if not m:
            continue  # malformed labels are fix_formatting's gate, not ours
        kind = m.group(1)
        if kind not in VERIFIABLE:
            continue
        where = resolve_kind(code, week, kind, inno_files, semester)
        if where is None:
            weeks = course_week_stems(code, inno_files, semester)
            have = sorted({s.split('-')[0].split(' ')[0]
                           for stems in weeks.values() for s in stems})
            violations.append(
                f'Line {no}: source `{kind}` has no transcript file anywhere '
                f'in this course (course ships: {", ".join(have) or "nothing"}). '
                f'Found `({label})`.')
        elif where != 'same-week':
            notes.append(
                f'Line {no}: `({label})` resolves to week {where.split(":")[1]} '
                f'transcripts, not week {week}.')
    return violations, notes


def fix_text(text, stems):
    """Rewrite unambiguous source-KIND swaps. Returns (new_text, n_fixed)."""
    verifiable_here = sorted({k for k in VERIFIABLE if kind_present(k, stems)})
    if len(verifiable_here) != 1:
        return text, 0
    want = verifiable_here[0]
    lines = text.splitlines()
    in_practice = False
    n = 0
    for i, line in enumerate(lines):
        s = line.strip()
        m = TOP_SECTION_RE.match(s)
        if m:
            in_practice = (m.group(2) == 'Practice')
            continue
        if not in_practice or not s.startswith('#####'):
            continue
        pm = PRACTICE_HEADING_RE.match(s)
        if not pm or not pm.group(4):
            continue
        sm = SOURCE_RE.match(pm.group(4))
        if not sm or sm.group(1) not in VERIFIABLE or sm.group(1) == want:
            continue
        if not kind_present(sm.group(1), stems):
            lines[i] = line.replace('(' + sm.group(1), '(' + want, 1)
            n += 1
    return '\n'.join(lines) + '\n', n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--inno-files', required=True)
    ap.add_argument('--semester', default='semester-4')
    ap.add_argument('--fix', action='store_true')
    ap.add_argument('qmd', nargs='*')
    a = ap.parse_args()

    if a.qmd:
        qmds = [Path(q).resolve() for q in a.qmd]
    else:
        qmds = sorted((ROOT / a.semester).rglob('*.qmd'))

    violations, fixed, skipped, notes = [], 0, 0, 0
    for q in qmds:
        try:
            text = q.read_text(encoding='utf-8')
        except OSError:
            continue
        locked = any(m in text[:2000] for m in LOCK_MARKS)
        if locked:
            skipped += 1
        code, week = article_course_week(q, a.semester)
        if code is None:
            print(f'SKIP {q}: cannot map to inno_files course')
            continue
        stems = week_stems(q, a.inno_files, a.semester) or []
        if a.fix and not locked:
            new_text, n = fix_text(text, stems)
            if n:
                q.write_text(new_text, encoding='utf-8')
                fixed += n
                print(f'FIX {q.relative_to(ROOT)}: {n} source-kind swap(s)')
                text = new_text
        vv, nn = validate_mapped(text, code, week, a.inno_files, a.semester)
        for v in vv:
            violations.append(f'{q.relative_to(ROOT)}: {v}')
        for w in nn:
            print(f'NOTE {q.relative_to(ROOT)}: {w}')
            notes += 1

    for v in violations:
        print('VIOLATION ' + v)
    print(f'checked={len(qmds)} fixed={fixed} skipped_locked={skipped} notes={notes} violations={len(violations)}')
    return 1 if violations else 0


if __name__ == '__main__':
    sys.exit(main())
