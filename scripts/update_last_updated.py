#!/usr/bin/env python3
"""Update the Quarto website footer timestamp before rendering."""

from datetime import datetime
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
QUARTO_CONFIG = ROOT / "_quarto.yml"


def format_timestamp() -> str:
    now = datetime.now().astimezone()
    return f"{now.strftime('%B')} {now.day}, {now.year} at {now:%H:%M}"


footer = f'  page-footer: "Last updated: {format_timestamp()}"'
text = QUARTO_CONFIG.read_text(encoding="utf-8")
next_text, count = re.subn(
    r'(?m)^  page-footer:\s*".*"$',
    footer,
    text,
    count=1,
)

if count == 0:
    next_text = text.replace("website:\n", f"website:\n{footer}\n", 1)

QUARTO_CONFIG.write_text(next_text, encoding="utf-8")
