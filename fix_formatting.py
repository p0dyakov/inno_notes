#!/usr/bin/env python3
"""Fix formatting in all .qmd files:
1. Remove blank lines between list items (numbered and bullet)
2. Add blank line after ':' before bullet lists
3. Detect AI thinking artifacts, evaluate with Claude, and optionally remove
"""
import re
import glob
import subprocess
import json
import os
from pathlib import Path

AI_PATTERNS = [
    # hesitation / thinking aloud
    r'(?i)^(uh|um|erm)[,.]?\s',
    r'(?i)^(hmm+|mmm+)[,.]?\s',
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



def is_list_item(line):
    """Line starts with a list marker like '1. ' or '- '."""
    return bool(re.match(r'^\s*(\d+\.\s|- )', line))


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


def get_all_examples(lines):
    """Extract all example headers (##### **X.Y ...) from Examples sections."""
    examples = []
    in_examples = False

    for i, line in enumerate(lines):
        s = line.strip()

        # Check if entering Examples section
        if s.startswith('#### **') and 'Examples' in s:
            in_examples = True
            continue

        # Check if leaving Examples section (new section header at same level or higher)
        if in_examples and s.startswith('#### **') and 'Examples' not in s:
            in_examples = False
            continue

        # Collect example headers
        if in_examples and s.startswith('#####'):
            examples.append({
                'line_num': i + 1,
                'text': s
            })

    return examples




def process_file(filepath):
    with open(filepath) as f:
        content = f.read()
    lines = content.split('\n')

    # === Extract all examples ===
    all_examples = get_all_examples(lines)

    # === Detect AI artifacts ===
    in_code = False
    ai_found = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        for pat in AI_PATTERNS:
            if re.search(pat, s):
                # Store full line context and section header for Claude review
                section = get_section_header(lines, i)
                ai_found.append({
                    'line_num': i + 1,
                    'line': line,
                    'text': s[:200],
                    'section': section
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

        # If line ends with ':' and is not a list item,
        # and next line is a bullet list item with no blank line between
        if (line.strip()
                and ends_with_colon(line)
                and not is_list_item(line)
                and i + 1 < len(lines)
                and re.match(r'^\s*- ', lines[i + 1])):
            result.append('')
            added += 1

    # Write back
    new_content = '\n'.join(result)
    changed = new_content != content
    if changed:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return removed, added, ai_found, changed, all_examples


# ─── Main ───
REVIEW_FOLDER = "ai_artifacts_review"

qmd_files = sorted(glob.glob('**/*.qmd', recursive=True))
print(f"Processing {len(qmd_files)} .qmd files\n")

total_removed = 0
total_added = 0
total_ai_detected = 0
files_changed = 0
all_artifacts = {}  # file -> list of artifacts
all_examples_map = {}  # file -> list of all examples

for fp in qmd_files:
    removed, added, ai, changed, examples = process_file(fp)
    total_removed += removed
    total_added += added
    total_ai_detected += len(ai)
    if changed:
        files_changed += 1

    # Store examples for later
    if examples:
        all_examples_map[fp] = examples

    if removed or added or ai:
        print(f"{'=' * 70}")
        print(f"  {fp}")
        if removed:
            print(f"  [-] Removed {removed} blank lines between list items")
        if added:
            print(f"  [+] Added {added} blank lines after ':' before lists")
        if ai:
            print(f"  [!] {len(ai)} potential AI artifact(s) detected:")
            for artifact in ai:
                print(f"      Line {artifact['line_num']}: {artifact['text']}")
            all_artifacts[fp] = ai
        print()

# === Create review folder structure ===
if all_examples_map or all_artifacts:
    print(f"{'=' * 70}")
    print(f"Creating review folder: {REVIEW_FOLDER}/")
    print(f"{'=' * 70}\n")

    # Create base review folder
    Path(REVIEW_FOLDER).mkdir(exist_ok=True)

    # Create review files for each file with examples or artifacts
    for file_path in set(list(all_examples_map.keys()) + list(all_artifacts.keys())):
        # Create directory structure
        review_file = Path(REVIEW_FOLDER) / file_path
        review_file.parent.mkdir(parents=True, exist_ok=True)

        # Get all examples and artifacts for this file
        examples = all_examples_map.get(file_path, [])
        artifacts = all_artifacts.get(file_path, [])

        # Create set of artifact line numbers for quick lookup
        artifact_lines = {a['line_num'] for a in artifacts}

        # Write review file with all examples
        review_content = f"# All Examples: {file_path}\n\n"
        review_content += f"Total examples: {len(examples)}\n"
        if artifacts:
            review_content += f"Examples with AI artifacts: {len([a for a in artifacts if a['line_num'] in artifact_lines])}\n\n"
        review_content += "---\n\n"

        for example in examples:
            # Check if this example has an artifact
            has_artifact = any(
                artifact['line_num'] >= example['line_num'] and
                artifact['line_num'] <= example['line_num'] + 50  # Within ~50 lines of header
                for artifact in artifacts
            )
            marker = "⚠️ " if has_artifact else ""
            review_content += f"{marker}{example['text']}\n\n"

        with open(review_file, 'w') as f:
            f.write(review_content)

        print(f"  ✓ Created: {review_file}")

    print(f"\n{'=' * 70}\n")

print(f"{'=' * 70}")
print(f"SUMMARY:")
print(f"  Files processed:  {len(qmd_files)}")
print(f"  Files changed:    {files_changed}")
print(f"  Blank lines removed (list gaps):  {total_removed}")
print(f"  Blank lines added (colon → list): {total_added}")
print(f"  AI artifacts detected:            {total_ai_detected}")

if all_artifacts:
    # Add review folder to .gitignore
    gitignore_path = ".gitignore"
    gitignore_entry = f"/{REVIEW_FOLDER}\n"

    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_content = f.read()
        if REVIEW_FOLDER not in gitignore_content:
            with open(gitignore_path, 'a') as f:
                f.write(gitignore_entry)
            print(f"✓ Added '/{REVIEW_FOLDER}' to .gitignore\n")
    else:
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_entry)
        print(f"✓ Created .gitignore with '/{REVIEW_FOLDER}'\n")

    print(f"\n{'=' * 70}")
    print("AI ARTIFACTS FOUND - Sending to Claude for optimization...")
    print(f"{'=' * 70}\n")

    # Build prompt for Claude
    artifact_text = "# AI ARTIFACTS DETECTED IN NOTES\n\n"
    for file_path, artifacts in all_artifacts.items():
        artifact_text += f"## File: {file_path}\n\n"
        for artifact in artifacts:
            section = artifact.get('section', '(no section header found)')
            artifact_text += f"**Section:** {section}\n"
            artifact_text += f"**Line {artifact['line_num']}:**\n```\n{artifact['line']}\n```\n\n"

    prompt = f"""Review these educational notes with AI thinking artifacts (self-corrections, hesitations, meta-commentary).

{artifact_text}

Your task:
1. Identify each AI artifact (hesitation phrases, self-corrections, unnecessary reasoning)
2. Optimize each solution by REMOVING only the unnecessary thinking/reasoning
3. KEEP the correct final solution in the exact same format (formulas, structure, everything)

Do NOT change the mathematical content or format. Only remove AI thinking artifacts like:
- "Actually, correcting:", "Let me recalculate:", "Hmm, let me reconsider:"
- "In other words," when it's just rephrasing (keep it if it's essential explanation)
- Intermediate failed attempts
- "I think", "I realized", etc.

Please proceed:"""

    print("=" * 70)
    print("CLAUDE OPTIMIZATION PROMPT:")
    print("=" * 70)
    print(prompt)
    print("\n" + "=" * 70)
    print("Please copy the above prompt and paste it to Claude to optimize the solutions.")
    print("Then copy the response and save it for applying the fixes.")
    print("=" * 70)
else:
    print("\nNo AI artifacts detected!")

print("\nDone!")
