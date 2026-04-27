#!/usr/bin/env python3
"""Fix formatting in all .qmd files:
1. Remove blank lines between list items (numbered and bullet)
2. Add blank line after ':' before bullet lists and tables
3. Detect AI thinking artifacts and write a root Markdown report
"""
import re
import glob
from pathlib import Path
from datetime import datetime

AI_PATTERNS = [
    # hesitation / thinking aloud
    r'(?i)^(uh|um|erm)[,.]?\s',
    r'(?i)^(hmm+|mmm+|hm)[,.]?\s',
    r'(?i)^well[,.]?\s',
    r'(?i)^okay[,.]?\s',
    r'(?i)^alright[,.]?\s',

    # self-correction / revision
    r'(?i)^(actually|frankly|honestly)[,.]?\s',
    r'(?i)^to be fair[,.]?\s',
    r'(?i)^I (just )?(noticed|remembered|realized|figured out)\s',
    r'(?i)^I (may|might) have been mistaken',
    r'(?i)^I (should|need to) clarify',
    r'(?i)^let me correct (that|this)',
    r'(?i)^small correction[:\s]',
    r'(?i)^minor correction[:\s]',

    # meta reasoning / narration
    r'(?i)^let me (explain|walk you through|break this down)',
    r'(?i)^let me',
    r'(?i)^wait',
    r'(?i)^here’s how I (think about|approach) this',
    r'(?i)^the key point (is|here is)',
    r'(?i)^the important thing (is|to note)',
    r'(?i)^what’s happening here is',
    r'(?i)^what this means is',

    # discourse markers
    r'(?i)^in other words[,.]?\s',
    r'(?i)^that said[,.]?\s',
    r'(?i)^with that in mind[,.]?\s',
    r'(?i)^for clarity[,.]?\s',
    r'(?i)^at a high level[,.]?\s',

    # recap / summary signals
    r'(?i)^to summarize[,:]?\s',
    r'(?i)^to sum up[,:]?\s',
    r'(?i)^in summary[,:]?\s',
    r'(?i)^overall[,.]?\s',

    # process resets
    r'(?i)^let’s start (over|again)',
    r'(?i)^going step by step',
    r'(?i)^first of all[,.]?\s',
    r'(?i)^before we continue[,.]?\s',
]


COURSE_SECTION_RULES = [
    (r'/Mathematical Analysis I/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Mathematical Analysis II/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Software Systems Analysis and Design/', ['Theory', 'Definitions', 'Practice'], []),
    (r'/Introduction to Programming/', ['Theory', 'Definitions', 'Practice'], []),
    (r'/Theoretical Computer Science/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Data Structures and Algorithms/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Analytical Geometry and Linear Algebra I/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Analytical Geometry and Linear Algebra II/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Academic Writing and Argumentation I/', ['Theory'], []),
    (r'/Academic Writing and Argumentation II/', ['Theory'], []),
    (r'/Logic and Discrete Mathematics/', ['Theory', 'Definitions', 'Formulas', 'Practice'], []),
    (r'/Computer Architecture/', ['Theory', 'Definitions'], ['Practice']),
]

DEFAULT_ALLOWED_SECTIONS = ['Theory', 'Definitions', 'Formulas', 'Practice']
TITLE_WEEK_RE = re.compile(r'^W\d+(?:-W\d+|[AB])?\.\s+.+$')
TOP_SECTION_RE = re.compile(r'^####\s+\*\*(\d+)\.\s+(.+?)\*\*\s*$')
ANY_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*$')
THEORY_LEVEL5_RE = re.compile(r'^#####\s+\*\*1\.\d+\s+.+?\*\*\s*$')
THEORY_LEVEL6_RE = re.compile(r'^######\s+\*\*1\.\d+\.\d+\s+.+?\*\*\s*$')
PRACTICE_HEADING_RE = re.compile(r'^#####\s+\*\*(\d+)\.(\d+)\.\s+(.+?)\*\*\s+\((.+)\)\s*$')
SOURCE_RE = re.compile(r'^(Lab|Lecture|Tutorial|Chapter|Midterm|Final|Test|Homework)(?:\s+([^,]+))?,\s+(Example|Task)\s+(\d+)$')
FORBIDDEN_TITLE_WORD_RE = re.compile(r'\b(Lecture|Chapter|Lab|Tutorial|Homework|Midterm|Final|Test|Slide|Slides)\b', re.IGNORECASE)


def normalize_path(filepath):
    return '/' + filepath.replace('\\', '/')


def section_rule_for_file(filepath):
    path = normalize_path(filepath)
    for pattern, required, optional in COURSE_SECTION_RULES:
        if re.search(pattern, path):
            return required, optional
    return ['Theory'], ['Definitions', 'Formulas', 'Practice']


def should_skip_file(filepath):
    path = filepath.replace('\\', '/')
    name = Path(path).name
    return name in ('404.qmd', 'index.qmd') or name.endswith('.ru.qmd')


def extract_yaml(lines):
    if not lines or lines[0].strip() != '---':
        return None, 0

    yaml_lines = []
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return yaml_lines, i + 1
        yaml_lines.append(lines[i])

    return None, 0


def parse_yaml_pairs(yaml_lines):
    values = {}
    for line in yaml_lines:
        match = re.match(r'^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$', line)
        if not match:
            continue
        key, value = match.groups()
        values[key] = value.strip().strip('"').strip("'")
    return values


def validate_yaml(filepath, lines):
    issues = []
    yaml_lines, _ = extract_yaml(lines)
    if yaml_lines is None:
        return ["YAML: missing opening/closing front matter block."]

    yaml = parse_yaml_pairs(yaml_lines)
    required_keys = ['title', 'author', 'date', 'format', 'engine']
    for key in required_keys:
        if key not in yaml:
            issues.append(f"YAML: missing `{key}` field.")

    title = yaml.get('title')
    if title and not TITLE_WEEK_RE.match(title):
        issues.append("YAML: `title` must start with `W<N>.`, `W<N>-W<X>.`, `W<N>A.`, or `W<N>B.`.")

    if yaml.get('format') and yaml['format'] != 'html':
        issues.append("YAML: `format` must be `html`.")

    if yaml.get('engine') and yaml['engine'] != 'knitr':
        issues.append("YAML: `engine` must be `knitr`.")

    return issues


def validate_top_sections(filepath, lines):
    issues = []
    required, optional = section_rule_for_file(filepath)
    allowed_names = required + optional
    expected_numbers = {name: str(index + 1) for index, name in enumerate(allowed_names)}
    found = {}

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped.startswith('#### '):
            continue

        match = TOP_SECTION_RE.match(stripped)
        if not match:
            issues.append(f"Line {line_num}: malformed or forbidden top-level section `{stripped}`.")
            continue

        number, name = match.groups()
        if name not in allowed_names:
            issues.append(f"Line {line_num}: forbidden top-level section `{name}`.")
            continue

        expected_number = expected_numbers[name]
        if number != expected_number:
            issues.append(f"Line {line_num}: section `{name}` must be numbered `{expected_number}.`, found `{number}.`.")

        if name in found:
            issues.append(f"Line {line_num}: duplicate top-level section `{name}`; first seen on line {found[name]}.")
        else:
            found[name] = line_num

    for name in required:
        if name not in found:
            issues.append(f"Missing required top-level section `{expected_numbers[name]}. {name}`.")

    return issues


def validate_source_label(label):
    match = SOURCE_RE.match(label)
    if not match:
        return "source label must match `(<Source> <X>, Example|Task <N>)` with an allowed source."

    source, source_number, item_kind, item_number = match.groups()
    if source in ('Lab', 'Lecture', 'Tutorial', 'Chapter', 'Homework'):
        if not source_number or not re.fullmatch(r'\d+', source_number.strip()):
            return f"`{source}` source must include a numeric file/chapter number."
    elif source == 'Test':
        if not source_number or not re.fullmatch(r'I|II', source_number.strip()):
            return "`Test` source must use roman `I` or `II`."
    elif source in ('Midterm', 'Final'):
        if source_number and not re.fullmatch(r'\d{4}', source_number.strip()):
            return f"`{source}` source number must be a year like `2025` when present."

    if not re.fullmatch(r'\d+', item_number):
        return "`Example`/`Task` number must be numeric."

    return None


def validate_practice_headings(lines):
    issues = []
    in_practice = False

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()

        top_section = TOP_SECTION_RE.match(stripped)
        if top_section:
            in_practice = top_section.group(2) == 'Practice'
            continue

        if not in_practice:
            continue

        if not stripped.startswith('#####'):
            continue

        match = PRACTICE_HEADING_RE.match(stripped)
        if not match:
            issues.append(f"Line {line_num}: malformed practice heading `{stripped}`.")
            continue

        section_number, item_number, title, source_label = match.groups()
        if section_number not in ('3', '4'):
            issues.append(f"Line {line_num}: practice heading section number must be `3` or `4`, found `{section_number}`.")

        if not item_number.isdigit():
            issues.append(f"Line {line_num}: practice item number must be numeric.")

        if FORBIDDEN_TITLE_WORD_RE.search(title):
            issues.append(f"Line {line_num}: practice title must not contain source words like Lecture, Chapter, Lab, or Slide.")

        source_error = validate_source_label(source_label)
        if source_error:
            issues.append(f"Line {line_num}: {source_error} Found `({source_label})`.")

    return issues


def validate_theory_headings(lines):
    issues = []
    in_theory = False

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()

        top_section = TOP_SECTION_RE.match(stripped)
        if top_section:
            in_theory = top_section.group(2) == 'Theory'
            continue

        if not in_theory:
            continue

        heading = ANY_HEADING_RE.match(stripped)
        if not heading:
            continue

        marks = heading.group(1)
        if len(marks) <= 4:
            issues.append(f"Line {line_num}: heading inside `Theory` must be deeper than `####`.")
            continue

        if len(marks) == 5 and not THEORY_LEVEL5_RE.match(stripped):
            issues.append(f"Line {line_num}: Theory subsection must match `##### **1.1 Title**`.")
        elif len(marks) == 6 and not THEORY_LEVEL6_RE.match(stripped):
            issues.append(f"Line {line_num}: Theory nested subsection must match `###### **1.1.1 Title**`.")

    return issues


def validate_format_rules(filepath, lines):
    if should_skip_file(filepath):
        return []

    issues = []
    issues.extend(validate_yaml(filepath, lines))
    issues.extend(validate_top_sections(filepath, lines))
    issues.extend(validate_theory_headings(lines))
    issues.extend(validate_practice_headings(lines))
    return issues



def is_list_item(line):
    """Line starts with a list marker like '1. ', '- ', or '* '."""
    return bool(re.match(r'^\s*(\d+\.\s|[-*+] )', line))


def ends_with_colon(line):
    """Line ends with ':' possibly followed by bold/italic markers."""
    return bool(re.search(r':\s*[*_]{0,4}\s*$', line))


def prev_is_in_list(built_lines):
    """Look back through already-built lines to check if we're inside a list."""
    for k in range(len(built_lines) - 1, -1, -1):
        line = built_lines[k]
        if line.strip() == '':
            continue
        if is_list_item(line):
            return True
        if line[0] in (' ', '\t'):
            continue  # indented sub-content, keep looking
        return False  # non-indented, non-list → not in list
    return False


def get_prev_nonblank(built_lines):
    """Get the last non-blank line from built lines."""
    for k in range(len(built_lines) - 1, -1, -1):
        if built_lines[k].strip() != '':
            return built_lines[k]
    return None


def get_section_header(lines, line_num):
    """Find the nearest section header (##### ...) before the given line number."""
    for i in range(line_num - 1, -1, -1):
        line = lines[i].strip()
        if line.startswith('#####'):
            return line
    return None


def process_file(filepath):
    with open(filepath) as f:
        content = f.read()
    lines = content.split('\n')

    format_issues = validate_format_rules(filepath, lines)

    # === Detect AI artifacts ===
    ai_found = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        for pattern in AI_PATTERNS:
            if re.match(pattern, stripped):
                section = get_section_header(lines, i)
                ai_found.append({
                    'line_num': i + 1,
                    'line': line,
                    'text': stripped[:120],
                    'section': section,
                })
                break

    # === Pass 1: Remove blank lines within lists ===
    result = []
    i = 0
    in_code = False
    removed = 0

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('```'):
            in_code = not in_code
            result.append(line)
            i += 1
            continue
        if in_code:
            result.append(line)
            i += 1
            continue

        if line.strip() == '':
            # Find next non-blank line
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1

            should_remove = False
            if j < len(lines) and is_list_item(lines[j]) and prev_is_in_list(result):
                prev = get_prev_nonblank(result)
                # Exception: keep blank if prev ends with ':' and is NOT a list item
                # (user wants blank line after colon before list)
                if prev and ends_with_colon(prev) and not is_list_item(prev):
                    should_remove = False
                else:
                    should_remove = True

            if should_remove:
                removed += (j - i)
                i = j
                continue
            else:
                result.append(line)
                i += 1
        else:
            result.append(line)
            i += 1

    lines = result

    # === Pass 2: Add blank line after ':' before bullet list ===
    result = []
    in_code = False
    added = 0

    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            in_code = not in_code

        result.append(line)

        if in_code:
            continue

        # If line ends with ':' and next line is a bullet list item — skip if
        # current line is itself a list item (to avoid spurious blank lines).
        # But always add a blank line before a table row regardless.
        if (line.strip()
                and ends_with_colon(line)
                and i + 1 < len(lines)):
            next_line = lines[i + 1]
            next_is_bullet = bool(re.match(r'^\s*[-*+] ', next_line))
            next_is_table = bool(re.match(r'^\s*\|', next_line))
            if (next_is_table or (next_is_bullet and not is_list_item(line))):
                result.append('')
                added += 1

    lines = result

    # === Pass 3: Ensure '---' before top-level numbered section headers ===
    # Matches: #### **N. SectionName** (e.g. #### **2. Definitions**)
    SECTION_HEADER_RE = re.compile(r'^####\s+\*\*\d+\.')
    result = []
    in_code = False
    separators_added = 0

    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            in_code = not in_code

        if not in_code and SECTION_HEADER_RE.match(line):
            section_num = int(re.search(r'####\s+\*\*(\d+)\.', line).group(1))
            if section_num > 1:
                # Ensure there's a '***' immediately before this header
                last_nonblank_idx = None
                for k in range(len(result) - 1, -1, -1):
                    if result[k].strip() != '':
                        last_nonblank_idx = k
                        break

                if last_nonblank_idx is None or result[last_nonblank_idx].strip() not in ('---', '***'):
                    while result and result[-1].strip() == '':
                        result.pop()
                    result.append('')
                    result.append('***')
                    result.append('')
                    separators_added += 1

        result.append(line)

    # Write back
    new_content = '\n'.join(result)
    changed = new_content != content
    if changed:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return removed, added + separators_added, ai_found, changed, format_issues


def build_report(stats, artifacts_by_file, format_issues_by_file):
    """Build the root Markdown report."""
    lines = [
        "# Formatting Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## AI Artifacts",
        "",
    ]

    if artifacts_by_file:
        for file_path in sorted(artifacts_by_file):
            lines.append(f"### {file_path}")
            lines.append("")
            for artifact in artifacts_by_file[file_path]:
                section = artifact.get('section') or '(no section header found)'
                lines.append(f"- Line {artifact['line_num']}; section: `{section}`")
                lines.append("")
                lines.append("```md")
                lines.append(artifact['line'])
                lines.append("```")
                lines.append("")
    else:
        lines.append("No potential AI artifacts detected.")
        lines.append("")

    lines.extend([
        "## Format Checks",
        "",
    ])

    if format_issues_by_file:
        for file_path in sorted(format_issues_by_file):
            lines.append(f"### {file_path}")
            lines.append("")
            for issue in format_issues_by_file[file_path]:
                lines.append(f"- {issue}")
            lines.append("")
    else:
        lines.append("No format-rule violations detected.")
        lines.append("")

    lines.extend([
        "## Formatting Changes",
        "",
        f"- Files processed: {stats['files_processed']}",
        f"- Files changed: {stats['files_changed']}",
        f"- Blank lines removed between list items: {stats['blank_lines_removed']}",
        f"- Blank lines/separators added: {stats['blank_lines_added']}",
        f"- Potential AI artifacts detected: {stats['ai_artifacts_detected']}",
        "",
    ])

    return '\n'.join(lines)


# ─── Main ───
REPORT_FILE = "formatting_report.md"

qmd_files = sorted(
    fp for fp in glob.glob('**/*.qmd', recursive=True)
    if not fp.startswith('_site/') and not fp.startswith('_freeze/') and not should_skip_file(fp)
)

total_removed = 0
total_added = 0
total_ai_detected = 0
files_changed = 0
all_artifacts = {}  # file -> list of artifacts
format_issues = {}  # file -> list of format issues

for fp in qmd_files:
    removed, added, ai, changed, file_format_issues = process_file(fp)
    total_removed += removed
    total_added += added
    total_ai_detected += len(ai)
    if changed:
        files_changed += 1

    if ai:
        all_artifacts[fp] = ai

    if file_format_issues:
        format_issues[fp] = file_format_issues

stats = {
    'files_processed': len(qmd_files),
    'files_changed': files_changed,
    'blank_lines_removed': total_removed,
    'blank_lines_added': total_added,
    'ai_artifacts_detected': total_ai_detected,
}

Path(REPORT_FILE).write_text(
    build_report(stats, all_artifacts, format_issues),
    encoding='utf-8',
)

print(f"Processed {len(qmd_files)} .qmd files.")
print(f"Changed {files_changed} file(s).")
print(f"Report written to {REPORT_FILE}.")
