#!/usr/bin/env python3
"""Update the home page footer timestamp before rendering."""

from datetime import datetime
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
HOME_PAGE = ROOT / "index.qmd"


def format_timestamp() -> str:
    now = datetime.now().astimezone()
    return f"{now.strftime('%B')} {now.day}, {now.year} at {now:%H:%M}"


footer = f'<div class="inn-home-last-updated">Last updated: {format_timestamp()}</div>'
text = HOME_PAGE.read_text(encoding="utf-8")
next_text, count = re.subn(
    r'(?m)^<div class="inn-home-last-updated">Last updated: .*?</div>$',
    footer,
    text,
    count=1,
)

if count == 0:
    next_text = text.rstrip() + f"\n\n{footer}\n"

HOME_PAGE.write_text(next_text, encoding="utf-8")
