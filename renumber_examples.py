#!/usr/bin/env python3
"""
Script to renumber examples in Mathematical Analysis II notes.

Usage:
    python renumber_examples.py <file_path> [--format FORMAT]

Examples:
    python renumber_examples.py "Mathematical Analysis II/1.qmd"
    python renumber_examples.py "Mathematical Analysis II/1.qmd" --format "3.{}"
    python renumber_examples.py "Mathematical Analysis II/1.qmd" --format "4.{}"
"""

import re
import sys
import argparse
from pathlib import Path


def renumber_examples(file_path: str, format_pattern: str = "4.{}") -> None:
    """
    Renumber all examples in a .qmd file.

    Args:
        file_path: Path to the .qmd file
        format_pattern: Format string for numbering (e.g., "4.{}" or "3.{}")
                       The {} will be replaced with sequential numbers
    """
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match example headings like: ##### **4.123. Title** (Source)
    # Captures: section number (4), old number (123), title, and source
    pattern = r'^(#####\s+\*\*)(\d+)\.(\d+)(\..*?\*\*.*?)$'

    counter = 1
    lines = content.split('\n')
    modified_lines = []

    for line in lines:
        match = re.match(pattern, line)
        if match:
            prefix = match.group(1)  # "##### **"
            section = match.group(2)  # "4"
            old_number = match.group(3)  # old example number
            rest = match.group(4)  # ". Title** (Source)"

            # Extract the section number from format_pattern if provided
            if '{}' in format_pattern:
                # Parse section from format_pattern (e.g., "4.{}" -> "4")
                new_section = format_pattern.split('.')[0]
                new_line = f"{prefix}{new_section}.{counter}{rest}"
            else:
                # Keep original section if format not provided properly
                new_line = f"{prefix}{section}.{counter}{rest}"

            modified_lines.append(new_line)
            counter += 1
        else:
            modified_lines.append(line)

    # Write back to file
    new_content = '\n'.join(modified_lines)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Renumbered {counter - 1} examples in {file_path}")
    print(f"  Format used: {format_pattern.format('N')}")


def main():
    parser = argparse.ArgumentParser(
        description='Renumber examples in Mathematical Analysis II notes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Mathematical Analysis II/1.qmd"
  %(prog)s "Mathematical Analysis II/1.qmd" --format "3.{}"
  %(prog)s "Mathematical Analysis II/1.qmd" --format "4.{}"
        """
    )
    parser.add_argument('file_path', help='Path to the .qmd file')
    parser.add_argument(
        '--format',
        default='4.{}',
        help='Format pattern for numbering (default: "4.{}")'
    )

    args = parser.parse_args()

    # Validate file exists
    file_path = Path(args.file_path)
    if not file_path.exists():
        print(f"Error: File not found: {args.file_path}", file=sys.stderr)
        sys.exit(1)

    if not file_path.suffix == '.qmd':
        print(f"Warning: File does not have .qmd extension: {args.file_path}", file=sys.stderr)

    # Validate format pattern
    if '{}' not in args.format:
        print(f"Error: Format pattern must contain '{{}}': {args.format}", file=sys.stderr)
        sys.exit(1)

    renumber_examples(str(file_path), args.format)


if __name__ == '__main__':
    main()
