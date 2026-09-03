#!/usr/bin/env python3
"""Regenerate the home-page course table from course registries + folder scan.

Sources (in order):
- <semester>/course_map.json registry (full Moodle names + teachers) when present
- legacy author map below for semesters without a registry
- directory scan, so a brand-new semester folder appears automatically

The table body in index.qmd between <!-- COURSES:BEGIN --> and <!-- COURSES:END -->
is rewritten. Run manually or via _quarto.yml pre-render.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.qmd"

ROMAN = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII"}

LEGACY_AUTHORS = {
    "Academic Writing and Argumentation I": "Georgy Gelvanovsky",
    "Academic Writing and Argumentation II": "Georgy Gelvanovsky",
    "Analytical Geometry and Linear Algebra I": "Salman Ahmadi-Asl",
    "Analytical Geometry and Linear Algebra II": "Salman Ahmadi-Asl",
    "Mathematical Analysis I": "Mohammad Alkousa",
    "Mathematical Analysis II": "Mohammad Alkousa",
    "Data Structures and Algorithms": "Nikolai Kudasov",
    "Software Systems Analysis and Design": "Eugene Zouev",
    "Theoretical Computer Science": "Manuel Mazzara",
    "Computer Architecture": "Artem Burmyakov",
    "Introduction to Programming": "Eugene Zouev",
    "Logic and Discrete Mathematics": "Andrey Frolov",
}

LEGACY_ORDER = {
    "semester-2": [
        "Academic Writing and Argumentation II",
        "Analytical Geometry and Linear Algebra II",
        "Mathematical Analysis II",
        "Data Structures and Algorithms",
        "Software Systems Analysis and Design",
        "Theoretical Computer Science",
    ],
    "semester-1": [
        "Academic Writing and Argumentation I",
        "Analytical Geometry and Linear Algebra I",
        "Mathematical Analysis I",
        "Computer Architecture",
        "Introduction to Programming",
        "Logic and Discrete Mathematics",
    ],
}


def semester_courses(sem_dir: Path) -> list[tuple[str, str]]:
    """Return [(display name, teachers)] for one semester dir."""
    reg_file = sem_dir / "course_map.json"
    if reg_file.exists():
        try:
            reg = json.loads(reg_file.read_text(encoding="utf-8"))
            out = []
            for code, entry in reg.get("courses", {}).items():
                name = entry.get("name", code)
                teachers = ", ".join(entry.get("teachers", [])) or "—"
                out.append((name, teachers))
            if out:
                return out
        except Exception:
            pass
    names = sorted(
        (d.name for d in sem_dir.iterdir() if d.is_dir() and not d.name.startswith((".", "_"))),
        key=str.lower,
    )
    if sem_dir.name in LEGACY_ORDER:
        ordered = [n for n in LEGACY_ORDER[sem_dir.name] if n in names]
        ordered += [n for n in names if n not in ordered]
        names = ordered
    return [(n, LEGACY_AUTHORS.get(n, "—")) for n in names]


def build_tbody() -> str:
    # Chronological ascending: Semester I, II, IV — matches the sidebar order.
    sem_dirs = sorted(
        [d for d in ROOT.iterdir() if d.is_dir() and re.fullmatch(r"semester-\d+", d.name)],
        key=lambda d: int(d.name.split("-")[1]),
        reverse=False,
    )
    rows: list[str] = []
    for sem in sem_dirs:
        courses = semester_courses(sem)
        if not courses:
            continue
        roman = ROMAN.get(sem.name.split("-")[1], sem.name)
        n = len(courses)
        for i, (name, teachers) in enumerate(courses):
            border = ' style="border-top:1px solid #5a5a5a"'
            if i == 0:
                rows.append(
                    f'<tr{border}><td rowspan="{n}" style="vertical-align:middle;font-weight:bold;text-align:center;'
                    f"padding:10px 16px;border-right:1px solid #5a5a5a;font-size:1.4em\">{roman}</td>"
                    f'<td style="padding:8px 16px;border-right:1px solid #5a5a5a">{name}</td>'
                    f'<td style="padding:8px 16px">{teachers}</td></tr>'
                )
            else:
                last = ' style="border-top:1px solid #5a5a5a;border-bottom:1px solid #5a5a5a"' if i == n - 1 and sem == sem_dirs[-1] else border
                rows.append(
                    f"<tr{last}>"
                    f'<td style="padding:8px 16px;border-right:1px solid #5a5a5a">{name}</td>'
                    f"<td style=\"padding:8px 16px\">{teachers}</td></tr>"
                )
    return "\n".join(rows)


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    tbody = build_tbody()
    pattern = re.compile(r"<!-- COURSES:BEGIN -->.*?<!-- COURSES:END -->", re.DOTALL)
    replacement = f"<!-- COURSES:BEGIN -->\n{tbody}\n<!-- COURSES:END -->"
    if pattern.search(text):
        text = pattern.sub(replacement, text)
    else:
        # First run: wrap the existing <tbody> content
        text = re.sub(
            r"(<tbody>)(.*?)(</tbody>)",
            lambda m: "<tbody>\n" + replacement + "\n</tbody>",
            text,
            flags=re.DOTALL,
        )
    INDEX.write_text(text, encoding="utf-8")
    print(f"index.qmd table refreshed ({tbody.count('<tr')} rows)")


if __name__ == "__main__":
    main()
