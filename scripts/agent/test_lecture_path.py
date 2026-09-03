#!/usr/bin/env python3
"""End-to-end test: Moodle transcript -> qmd article -> sidebar/index -> _site -> live.

Repo-state checks always run. Live-site checks run with --live.
Fails non-zero on the first broken link. No Gemini calls, no writes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate import (  # noqa: E402
    combine_transcripts,
    group_lectures,
    load_sem4_registry,
    md_to_qmd_target,
    resolve_author,
    section_rule_for_folder,
    sem4_canon_code,
    short_to_full,
    validate_title,
)

ROOT = Path(__file__).resolve().parents[2]
PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    results.append((PASS if cond else FAIL, name, detail))
    print(f"[{PASS if cond else FAIL}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        raise SystemExit(f"FAILED: {name}: {detail}")


def front_matter(qmd: Path) -> dict:
    lines = qmd.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---"
    fm: dict[str, str] = {}
    for ln in lines[1:]:
        if ln == "---":
            break
        m = re.match(r'(\w+):\s*"(.*)"', ln)
        if m:
            fm[m.group(1)] = m.group(2)
    return fm


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inno-files", type=Path, default=None)
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--live-base", default="https://innonotes.ru")
    args = ap.parse_args()

    inno_files = args.inno_files or next(
        (p for p in [Path("/tmp/inno_files"), ROOT.parent / "inno_files"] if (p / "semester-4").exists()),
        None,
    )

    reg = load_sem4_registry()["courses"]
    check("registry has 6 courses", len(reg) == 6, str(sorted(reg)))
    for code, entry in reg.items():
        d = ROOT / "semester-4" / entry["name"]
        check(f"registry dir exists: {entry['name']}", d.is_dir(), code)
        check(f"teachers set: {code}", bool(entry.get("teachers")), str(entry.get("teachers")))
        check(f"code round-trip: {code}", sem4_canon_code(entry["name"]) == code, entry["name"])

    if inno_files is None:
        print("WARN: inno_files not found, skipping source checks")
    else:
        mds = [p for p in sorted((inno_files / "semester-4").rglob("*.md"))
               if p.is_file() and p.name != "Syllabus.md"]
        check("transcripts found", bool(mds), str(inno_files))
        groups = group_lectures(mds, inno_files)
        check("groups formed", bool(groups), "")
        seen_targets: dict[str, str] = {}
        for qmd, group in groups:
            check(f"target in semester-4: {qmd.name}", "semester-4" in qmd.parts, str(qmd))
            for md in group:
                rel = md.relative_to(inno_files / "semester-4")
                check(f"maps under full course name: {rel}", str(qmd.parent.name) == short_to_full(rel.parts[0]), str(qmd))
            combo = combine_transcripts(group)
            for md in group:
                check(f"source header kept: {md.name}", f"# SOURCE FILE: {md.name}" in combo, str(qmd))
            key = (qmd.parent.name, re.match(r"(\d+)", group[0].relative_to(inno_files / "semester-4").parts[1]).group(1))
            check(f"no cross-week collision: {qmd}", key not in seen_targets, str(seen_targets.get(key)))
            seen_targets[key] = str(qmd)

    yml = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    index = (ROOT / "index.qmd").read_text(encoding="utf-8")
    sidebar_order = re.findall(r'- section: "Semester ([IVX]+)"', yml)
    check("sidebar chronological: I, II, IV", sidebar_order == ["I", "II", "IV"], str(sidebar_order))
    tbody = index.split("<!-- COURSES:BEGIN -->")[1].split("<!-- COURSES:END -->")[0]
    index_order = re.findall(r'rowspan="\d+"[^>]*>([IVX]+)<', tbody)
    check("index chronological: I, II, IV", index_order == ["I", "II", "IV"], str(index_order))
    for code, entry in reg.items():
        check(f"sidebar section: {entry['name']}", f'- section: "{entry["name"]}"' in yml, code)
        check(f"index course: {entry['name']}", entry["name"] in index, code)
        for teacher in entry["teachers"]:
            check(f"index teacher {teacher} ({code})", teacher in index, code)

    qmds = sorted((ROOT / "semester-4").rglob("*.qmd"))
    check("articles exist", bool(qmds), "")
    for qmd in qmds:
        fm = front_matter(qmd)
        check(f"title valid: {qmd.parent.name}/{qmd.name}", validate_title(fm.get("title", "")), fm.get("title", ""))
        body = qmd.read_text(encoding="utf-8")
        for sec in section_rule_for_folder(qmd.parent.name)[0]:
            check(f"section {sec} in {qmd.parent.name}/{qmd.name}", f"#### **" in body and sec in body, sec)
        rel = str(qmd.relative_to(ROOT))
        check(f"sidebar lists {rel}", rel in yml, "")
        html = ROOT / "_site" / qmd.with_suffix(".html").relative_to(ROOT)
        check(f"built html present: {rel}", html.exists(), str(html))

    if args.live:
        def get(path: str) -> str:
            with urllib.request.urlopen(args.live_base + path, timeout=20) as r:
                assert r.status == 200, f"{path} -> {r.status}"
                return r.read().decode("utf-8")

        home = get("/")
        check("live index has Semester IV", "Semester IV" in home or ">IV<" in home, "")
        for code, entry in reg.items():
            check(f"live index course: {entry['name']}", entry["name"] in home, code)
        for qmd in qmds:
            fm = front_matter(qmd)
            page = get("/" + qmd.with_suffix(".html").relative_to(ROOT).as_posix().replace(" ", "%20"))
            check(f"live 200 + title: {qmd.parent.name}/{qmd.name}", fm["title"] in page, fm["title"])
            check(f"live author: {qmd.parent.name}/{qmd.name}", fm["author"] in page, fm["author"])

    n = len(results)
    print(f"\nALL {n} CHECKS PASSED")


if __name__ == "__main__":
    main()
