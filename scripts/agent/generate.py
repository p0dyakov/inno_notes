#!/usr/bin/env python3
"""Generate semester-N qmd articles from inno_files transcript MDs.

Works for ANY future semester: a semester is agent-managed iff it has a
<semester>/course_map.json registry (folder full names + teachers).
Only touches managed semesters. Early exit if nothing to generate/update.
Theory always uses the Pro model; other sections use the flash model.
Iterates until fix_formatting.py + quarto render pass (up to 3 attempts).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import time
import textwrap
from datetime import datetime
from pathlib import Path


from llm import complete as llm_complete

ROOT = Path(__file__).resolve().parents[2]
INNO_NOTES = ROOT
PROMPT_MD = ROOT / "prompt.md"
RULES_MD = ROOT / "rules.md"
COURSE_MAP_JSON = Path(__file__).parent / "course_map.json"


def registry_path(semester: str) -> Path:
    return ROOT / semester / "course_map.json"


def managed_semesters() -> list[str]:
    """Semesters the agent may touch: any semester-N dir with course_map.json."""
    out = []
    for d in ROOT.iterdir():
        if d.is_dir() and re.fullmatch(r"semester-\d+", d.name) and (d / "course_map.json").exists():
            out.append(d.name)
    return sorted(out, key=lambda s: int(s.split("-")[1]))


SEMESTER_ROMAN = {"1": "I", "2": "II", "3": "III", "4": "IV",
                  "5": "V", "6": "VI", "7": "VII", "8": "VIII"}


def semester_roman(semester: str) -> str:
    return SEMESTER_ROMAN.get(semester.split("-")[1], semester)
PROMPTS_DIR = Path(__file__).parent / "prompts"

# Same shape as fix_formatting.py TITLE_WEEK_RE (kept in sync manually —
# fix_formatting.py runs on import, so it cannot be imported here).
TITLE_WEEK_RE = re.compile(r"^W\d+(?:-W\d+|[AB])?\.\s+.+$")

INNO_FILES_DEFAULT = Path("/tmp/inno_files")
GEMINI_MODEL = "gemini-3.8-flash"
GEMINI_FALLBACKS = ["gemini-3.5-flash", "gemini-3.5-flash-lite"]
# Theory is the most important section: it is always written by the Pro model.
# Override with GEMINI_THEORY_MODEL env if the model id changes.
GEMINI_THEORY_MODEL = os.environ.get("GEMINI_THEORY_MODEL", "gemini-3.1-pro-preview")
GEMINI_THEORY_FALLBACKS = ["gemini-3.1-pro-preview", "gemini-3.8-flash"]
GOLDEN_W = 3  # legacy week-numbering offset, kept for reference

# semesters without course_map.json (e.g. frozen legacy semester-1/2) are never touched

SECTION_ORDER = ["Theory", "Definitions", "Formulas", "Practice"]

# Author map from prompt.md section 15 (fallback if course folder not in prompt)
AUTHOR_MAP = {
    "OS": "Giancarlo Succi",
    "Phy I": "Victor Nikiforov",
    "CA": "Artem Burmyakov",
    "ITP": "Eugene Zouev",
    "LDM": "Andrey Frolov",
    "AI": "Munir Makhmutov",
    "TCS": "Manuel Mazzara",
    "DSA": "Nikolai Kudasov",
    "MA I": "Mohammad Alkousa",
    "MA II": "Mohammad Alkousa",
    "AGLA I": "Salman Ahmadi-Asl",
    "AGLA II": "Salman Ahmadi-Asl",
    "SSAD": "Eugene Zouev",
    "ProbStat": "Mohammad Alkousa",
    "DE": "Mohammad Alkousa",
    "ITO": "Mohammad Alkousa",
}


def load_course_map() -> dict:
    if COURSE_MAP_JSON.exists():
        return json.loads(COURSE_MAP_JSON.read_text(encoding="utf-8"))
    return {}


def load_registry(semester: str) -> dict:
    path = registry_path(semester)
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def course_entry(semester: str, key: str) -> dict:
    """Lookup registry entry by short code (inno_files folder) or full name."""
    courses = load_registry(semester).get("courses", {})
    if key in courses:
        return courses[key]
    for code, entry in courses.items():
        if entry.get("name") == key:
            return entry
    return {}


def canon_code(semester: str, folder: str) -> str:
    """Normalize full folder name back to short inno_files code when known."""
    courses = load_registry(semester).get("courses", {})
    if folder in courses:
        return folder
    for code, entry in courses.items():
        if entry.get("name") == folder:
            return code
    return folder


def short_to_full(code: str, semester: str = "semester-4") -> str:
    entry = course_entry(semester, code)
    return entry.get("name", code)


# Backward-compatible wrappers (default semester-4) for existing callers/tests.
def load_sem4_registry() -> dict:
    return load_registry("semester-4")


def sem4_course_entry(key: str) -> dict:
    return course_entry("semester-4", key)


def sem4_canon_code(folder: str) -> str:
    return canon_code("semester-4", folder)


def extract_author_from_transcript(transcript: str) -> str:
    """First-page author fallback: Instructor:/Lecturer: lines or bold name header."""
    lines = transcript.splitlines()
    head = "\n".join(lines[:40])
    m = re.search(
        r"(?:Course Instructor|Prime Instructor|Instructor|Lecturer|Professor)\s*:?\s*(?:Dr\.?\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,2})",
        head,
    )
    if m:
        return m.group(1).strip()
    first = lines[:20]
    if any("innopolis" in ln.lower() for ln in first):
        for ln in first:
            mm = re.match(r"\s*\*\*([A-Z][a-z]+ [A-Z][a-z]+(?: [A-Z][a-z]+)?)\*\*\s*$", ln)
            if mm and "university" not in mm.group(1).lower():
                return mm.group(1).strip()
    return ""


UNKNOWN_AUTHOR = "\u2014"  # em-dash: shown when the teacher could not be determined


def resolve_author(folder: str, transcript: str = "", semester: str = "semester-4") -> str:
    """Priority: Moodle/manual registry entry -> transcript first page -> curated table.

    If the teacher cannot be determined with confidence at any step, returns
    an em-dash — never invent a name.
    """
    entry = course_entry(semester, folder)
    if entry and entry.get("teachers"):
        return ", ".join(entry["teachers"])
    if transcript:
        found = extract_author_from_transcript(transcript)
        if found:
            return found
    if folder in AUTHOR_MAP:
        return AUTHOR_MAP[folder]
    code = canon_code(semester, folder)
    if code in AUTHOR_MAP:
        return AUTHOR_MAP[code]
    return UNKNOWN_AUTHOR


def section_rule_for_folder(folder: str, semester: str = "semester-4") -> tuple[list[str], bool]:
    """Return (required_top_sections, has_formulas) per rules.md."""
    folder = canon_code(semester, folder)
    # rules.md mapping
    map_ = {
        "ProbStat": (["Theory", "Definitions", "Formulas", "Practice"], True),
        "DE": (["Theory", "Definitions", "Formulas", "Practice"], True),
        "ITO": (["Theory", "Definitions", "Formulas", "Practice"], True),
        "OS": (["Theory", "Definitions", "Practice"], False),  # like CA
        "AI": (["Theory", "Definitions", "Practice"], False),  # like TCS but lighter
        "Phy I": (["Theory", "Definitions", "Formulas", "Practice"], True),
    }
    if folder in map_:
        req, has_formulas = map_[folder]
        return req, has_formulas
    return (["Theory", "Definitions", "Formulas", "Practice"], True)


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kwargs)


def quarto_render_one(qmd: Path) -> tuple[bool, str]:
    res = run(["quarto", "render", str(qmd)])
    ok = res.returncode == 0
    log = (res.stdout or "") + (res.stderr or "")
    return ok, log


def fix_formatting_check() -> tuple[bool, str]:
    res = run([sys.executable, "fix_formatting.py"], cwd=str(ROOT))
    # fix_formatting writes formatting_report.md; check it
    report = ROOT / "formatting_report.md"
    if report.exists():
        txt = report.read_text(encoding="utf-8")
        if "No format-rule violations detected" in txt and "No potential AI artifacts detected" in txt:
            return True, txt[:2000]
        return False, txt[:4000]
    return False, (res.stdout + res.stderr)[:4000]


def gemini_section(
    section: str,
    transcript: str,
    style_context: str,
    target_info: str,
    api_key: str,
    model: str = GEMINI_MODEL,
    fallbacks: list[str] | None = None,
) -> str:
    """Call Gemini for a single section. Retries fall back across models."""
    prompt = _build_section_prompt(section, transcript, style_context, target_info)
    last_err: Exception | None = None
    models = [model] + (fallbacks if fallbacks is not None else GEMINI_FALLBACKS)
    for m in models:
        for attempt in range(1, 4):
            try:
                return _call_gemini(prompt, api_key, m)
            except Exception as e:
                last_err = e
                msg = str(e)
                if "429" in msg or "503" in msg or "overload" in msg.lower():
                    wait = min(2 ** attempt * 5, 60)
                    print(f"  {section}: {m} failed ({msg[:120]}), retry {attempt}/3 in {wait}s...")
                    time.sleep(wait)
                    continue
                raise
        print(f"  {section}: {m} exhausted, trying next model...")
    assert last_err is not None
    raise last_err


def _section_instruction(section: str) -> str:
    p = PROMPTS_DIR / f"{section.lower()}.md"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return section


def _title_rules() -> str:
    p = PROMPTS_DIR / "title.md"
    return p.read_text(encoding="utf-8") if p.exists() else ""


def validate_title(title: str) -> bool:
    """Post-validation for lecture titles (mirrors fix_formatting TITLE_WEEK_RE + BAD list)."""
    if not title or not TITLE_WEEK_RE.match(title):
        return False
    if re.search(r"—\s*lecture|lecture\s*\d+\s*$", title, re.IGNORECASE):
        return False
    after_dot = title.split(".", 1)[1].strip() if "." in title else title
    if re.match(r"^(OS|DE|ITO|Phy I|ProbStat|AI)\b", after_dot):
        return False
    return True


def clean_heading_topic(heading: str) -> str:
    h = re.sub(r"^#+\s*", "", heading).strip()
    h = re.sub(r"^(Lecture|Chapter|Tutorial)\s*\d+\s*[:\-–—.]?\s*", "", h, flags=re.IGNORECASE)
    h = re.sub(r"\s*[:\-–—]\s*(Lecture|Chapter)\s*\d+.*$", "", h, flags=re.IGNORECASE)
    h = re.sub(r"\s+Chapter\s+[\d.\-&, ]+$", "", h, flags=re.IGNORECASE)
    return h.strip()


def infer_topic(transcript: str, week: str, api_key: str) -> str:
    """Ask Gemini for ONE short topic noun phrase per prompts/title.md, then validate."""
    rules = _title_rules()
    head = "\n".join(transcript.splitlines()[:120])[:6000]
    prompt = (
        "Read this lecture transcript opening and return ONLY the article title, nothing else.\n\n"
        f"Title rules:\n{rules}\n\n"
        f"The week number is {week} (use it as the W-prefix).\n\n"
        f"Transcript opening:\n{head}\n"
    )
    def clean_topic(raw: str) -> str:
        topic = raw.strip().strip('"').splitlines()[0].strip()
        return re.sub(r"^W\d+(?:-W\d+)?\.\s*", "", topic).strip()

    try:
        topic = clean_topic(_call_gemini(prompt, api_key, GEMINI_MODEL))
        if topic and validate_title(f"W{week}. {topic}"):
            if len(f"W{week}. {topic}") <= 40:
                return topic
            print(f"  topic too long ({len(topic)} chars), one retry for shorter ...")
            short = clean_topic(_call_gemini(
                prompt + "\n\nPrevious answer was too long for one sidebar line. "
                "Reply with a SHORTER title, 36 characters max total.", api_key, GEMINI_MODEL))
            if short and validate_title(f"W{week}. {short}") and len(f"W{week}. {short}") <= 40:
                return short
            return topic  # keep the valid long one rather than nothing
        print(f"  topic rejected by validation: {topic[:100]}")
    except Exception as e:  # noqa: BLE001
        print(f"  topic inference failed: {e}")
    for line in transcript.splitlines():
        if line.strip().startswith("#"):
            topic = clean_heading_topic(line)
            if topic and validate_title(f"W{week}. {topic}"):
                return topic
    return f"Week {week} Notes"


def _build_section_prompt(section: str, transcript: str, style_context: str, target_info: str) -> str:
    # Section instructions live in scripts/agent/prompts/*.md (single source of truth)
    rules = RULES_MD.read_text(encoding="utf-8") if RULES_MD.exists() else ""

    preamble = (
        f"You are writing a single section of a Quarto study article. Output ONLY that section's markdown, "
        f"including its #### header and all subheadings/content. Do not add YAML or other sections.\n\n"
        f"Target: {target_info}\n"
        f"Section to write: {section}\n"
        f"Instruction:\n{_section_instruction(section)}\n\n"
        f"Local style context (3 neighboring articles' headings/structure — follow their density, heading style, diagram palette if any):\n"
        f"{style_context[:6000]}\n\n"
        f"Rules excerpt (relevant part of rules.md — must be satisfied for format checks):\n"
        f"{rules[:4000]}\n\n"
        f"Full transcript for THIS article (use as authoritative source order and coverage checklist):\n"
        f"{transcript[:90000]}\n"
    )
    return preamble


def _call_gemini(prompt: str, api_key: str, model: str, timeout_s: int = 300) -> str:
    """Single generation via the configured LLM backend (see llm.py).

    antigravity backend ignores api_key (local hub auth); apikey backend
    preserves the previous direct generativelanguage behavior for CI.
    """
    return llm_complete(prompt, model, api_key=api_key, timeout_s=timeout_s)


def gather_changed_lectures(
    inno_files: Path, since_sha: str | None = None, semesters: list[str] | None = None,
) -> list[Path]:
    """Find transcript MDs in managed semesters that are new or changed since SHA."""
    semesters = semesters or managed_semesters()
    managed = set(semesters)
    if since_sha:
        res = run(["git", "-C", str(inno_files), "diff", "--name-only", f"{since_sha}..HEAD", "--"] + semesters)
        # If that fails (shallow), fall back to full scan
        if res.returncode != 0 or not res.stdout.strip():
            pass
        else:
            files = [inno_files / p.strip() for p in res.stdout.splitlines() if p.strip().endswith(".md")]
            # Keep only existing files inside managed semesters
            return [p for p in files if p.exists() and md_semester_safe(p, inno_files) in managed]

    # Full scan: every transcript MD in managed semesters (Syllabus excluded)
    out: list[Path] = []
    for sem in semesters:
        for md in sorted((inno_files / sem).rglob("*.md")):
            if not md.is_file():
                continue
            # Skip Syllabus etc? Only lab/lecture/tutorial sources that were transcripted
            if md.name == "Syllabus.md":
                continue
            out.append(md)
    return out


def md_semester_safe(md: Path, inno_files: Path) -> str:
    try:
        return md_semester(md, inno_files)
    except ValueError:
        return ""


def md_semester(md: Path, inno_files: Path) -> str:
    """Derive the semester dir (semester-N) from a transcript path."""
    rel = md.relative_to(inno_files)
    for part in rel.parts:
        if re.fullmatch(r"semester-\d+", part):
            return part
    raise ValueError(f"no semester dir in transcript path: {md}")


def md_to_qmd_target(md: Path, inno_files: Path) -> Path:
    """Map inno_files/<sem>/<ShortCode>/<N>/Lecture.md -> inno_notes/<sem>/<Full Name>/<N>.qmd"""
    semester = md_semester(md, inno_files)
    rel = md.relative_to(inno_files / semester)
    # rel is <ShortCode>/<N>/Lecture.md or <ShortCode>/<N>/Lecture.mmd etc
    parts = rel.parts
    course = short_to_full(parts[0], semester)
    week = parts[1] if len(parts) > 2 else "1"
    # week is a folder like "12" or "10-11" etc — keep as is for W-number
    # But the qmd naming is per lecture: 1.qmd, 2.qmd, etc. We map Lecture.md in week folder to <N>.qmd
    # where N is the numeric week folder name stripped to its first number
    m = re.match(r"(\d+)", week)
    n = m.group(1) if m else "1"
    return INNO_NOTES / f"{semester}/{course}/{n}.qmd"


SOURCE_KINDS = ["Lab", "Homework", "Assignment", "Exercises", "Lecture", "Tutorial",
                "Chapter", "Recap", "Test", "Midterm", "Final"]


def source_kind(md_name: str) -> str:
    """Canonical Practice source label from transcript filename (Lecture.md -> Lecture)."""
    stem = Path(md_name).stem.lower()
    for kind in SOURCE_KINDS:
        if kind.lower() in stem:
            return kind
    return Path(md_name).stem


def group_lectures(mds: list[Path], inno_files: Path) -> list[tuple[Path, list[Path]]]:
    """Group transcript MDs by their qmd target: one article per (course, week).

    A week folder often holds several sources (Lecture.md + Tutorial.md + Lab.md);
    they must be stitched into ONE article, never overwrite each other.
    """
    groups: dict[Path, list[Path]] = {}
    for md in sorted(mds):
        qmd = md_to_qmd_target(md, inno_files)
        groups.setdefault(qmd, []).append(md)
    return sorted(groups.items(), key=lambda kv: str(kv[0]))


def combine_transcripts(mds: list[Path]) -> str:
    """Join one week's sources with explicit SOURCE headers for Practice labels."""
    parts = []
    for md in mds:
        txt = md.read_text(encoding="utf-8")
        if txt.strip():
            parts.append(f"# SOURCE FILE: {md.name} (cite as: {source_kind(md.name)})\n\n{txt.strip()}")
    return "\n\n---\n\n".join(parts)


def collect_style_context(course: str, max_files: int = 3, semester: str = "semester-4") -> str:
    """Grab up to 3 neighboring articles in the same course folder for style."""
    course_dir = INNO_NOTES / f"{semester}/{course}"
    files = sorted(course_dir.glob("*.qmd"))[:max_files] if course_dir.exists() else []
    # Fallback: use semester-2 examples with similar course type
    if not files:
        fallbacks = list((INNO_NOTES / "semester-2/Software Systems Analysis and Design").glob("*.qmd"))[:1]
        files = fallbacks
    parts: list[str] = []
    for f in files[:max_files]:
        txt = f.read_text(encoding="utf-8")
        # First 80 lines are enough for style (YAML + Theory header + a few definitions)
        parts.append(f"--- {f.name} ---\n" + "\n".join(txt.splitlines()[:80]))
    return "\n\n".join(parts) if parts else "No neighboring articles yet — follow prompt.md and rules.md strictly."


def generate_article(
    transcript: str,
    course: str,
    week: str,
    api_key: str,
    style_context: str,
    sources: list[str] | None = None,
    semester: str = "semester-4",
) -> str:
    today = datetime.now().strftime("%B %d, %Y")
    full_name = short_to_full(canon_code(semester, course), semester)
    author = resolve_author(course, transcript, semester)
    topic = infer_topic(transcript, week, api_key)
    title = f"W{week}. {topic}"
    assert validate_title(title), f"generated title failed validation: {title!r}"
    required, has_formulas = section_rule_for_folder(course, semester)
    src_note = ""
    if sources:
        kinds = ", ".join(f"{s} ({source_kind(s)})" for s in sources)
        src_note = (
            f" This article combines {len(sources)} transcript sources: {kinds}. "
            f"Cover all of them; in Practice headings cite these exact source names "
            f"in canonical order Lab→Homework→Assignment→Exercises→Lecture→Tutorial→Chapter→Recap→Test→Midterm→Final."
        )
    target_info = (
        f"Course {full_name} ({semester}), week W{week}, author {author}, date {today}, "
        f"required sections {required}. Article title is {title!r} — do not restate it in section bodies.{src_note}"
    )

    sections = [s for s in SECTION_ORDER if s in required]

    results: dict[str, str] = {}

    def task(section: str) -> tuple[str, str]:
        # Every content section (Theory/Definitions/Formulas/Practice/...) is
        # written by the PRO model; flash is only for title/shorten and fixes.
        print(f"  Gemini {section} (PRO model) for {course}/{week} ...")
        return section, gemini_section(
            section, transcript, style_context, target_info, api_key,
            model=GEMINI_THEORY_MODEL,
            fallbacks=GEMINI_THEORY_FALLBACKS + GEMINI_FALLBACKS,
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(sections), 4)) as ex:
        futs = {ex.submit(task, s): s for s in sections}
        for fut in concurrent.futures.as_completed(futs):
            sec, body = fut.result()
            results[sec] = body.strip()

    # Stitch in canonical order. Numbers are SEQUENTIAL among the sections
    # actually present in this article (no Formulas -> Practice is 3., etc.),
    # never the position in the global SECTION_ORDER.
    stitched_sections = []
    for sec in sections:
        body = results.get(sec, "")
        if not body:
            continue
        idx = sections.index(sec) + 1
        mh = re.match(r"(\s*####\s+\*\*)(\d+)(\.\s+)", body)
        if mh:
            # Model emitted its own header — normalize the number, keep the rest
            body = f"{mh.group(1)}{idx}{mh.group(3)}" + body[mh.end():]
        else:
            # Gemini sometimes omits the header — prepend canonical one
            body = f"#### **{idx}. {sec}**\n\n" + body
        stitched_sections.append(body.strip())

    yaml_front = textwrap.dedent(
        f"""\
        ---
        title: "{title}"
        author: "{author}"
        date: "{today}"
        format: html
        engine: knitr
        ---
        """
    )
    return yaml_front + "\n" + "\n\n".join(stitched_sections) + "\n"


def theory_stats(body: str) -> tuple[int, int]:
    """(total words, ##### subsection count) of a Theory section body."""
    subs = re.split(r"^##### ", body, flags=re.M)[1:]
    return sum(len(s.split()) for s in subs), len(subs)


def regen_theory(qmd: Path, inno_files: Path, api_key: str, tries: int = 3) -> bool:
    """Regenerate ONLY the Theory section of an existing article with the PRO model."""
    rel = qmd.relative_to(INNO_NOTES)
    semester = rel.parts[0]
    course_full, week = rel.parts[1], Path(rel.parts[2]).stem
    code = canon_code(semester, course_full)
    cdir = inno_files / semester / code
    mds = [md for wd in sorted(cdir.iterdir()) if wd.is_dir()
           and (m := re.match(r"(\d+)", wd.name)) and m.group(1) == week
           for md in sorted(wd.glob("*.md")) if md.name != "Syllabus.md"]
    if not mds:
        print(f"  no transcripts for {qmd}")
        return False
    transcript = combine_transcripts(mds)
    full_name = short_to_full(code, semester)
    author = resolve_author(code, transcript, semester)
    required, _ = section_rule_for_folder(code, semester)
    style = collect_style_context(course_full, semester=semester)
    old = qmd.read_text(encoding="utf-8")
    mt = re.search(r'title: "(.*)"', old)
    title = mt.group(1) if mt else f"W{week}. Notes"
    target_info = (
        f"Course {full_name} ({semester}), week W{week}, author {author}, "
        f"required sections {required}. Article title is {title!r} — do not restate it. "
        f"Regenerate ONLY the Theory section; keep full depth per the instruction."
    )
    best, best_score = "", -1
    for it in range(1, tries + 1):
        print(f"  Theory PRO attempt {it}/{tries} for {qmd.relative_to(ROOT)} ...")
        body = gemini_section("Theory", transcript, style, target_info, api_key,
                              model=GEMINI_THEORY_MODEL,
                              fallbacks=GEMINI_THEORY_FALLBACKS + GEMINI_FALLBACKS).strip()
        if not body.lstrip().startswith("####"):
            body = "#### **1. Theory**\n\n" + body
        words, subs = theory_stats(body)
        print(f"    stats: {words} words, {subs} subsections")
        if words > best_score:
            best, best_score = body, words
        if words >= 1200 and subs >= 4:
            best = body
            break
        time.sleep(5)
    words, subs = theory_stats(best)
    print(f"  Theory stats: {words} words, {subs} subsections (no minimum — depth follows input size)")
    replacement = best.rstrip() + "\n\n"
    new = re.sub(r"#### \*\*1\. Theory\*\*.*?(?=^#### )", lambda _: replacement,
                 old, count=1, flags=re.DOTALL | re.M)
    assert new != old, "Theory splice failed"
    qmd.write_text(new, encoding="utf-8")
    run([sys.executable, "fix_formatting.py"], cwd=str(ROOT))
    print(f"  Theory replaced: {words} words, {subs} subsections")
    return True


def process_one(md: Path, inno_files: Path, api_key: str, dry_run: bool = False) -> bool:
    """Legacy single-file entry kept for tests; delegates to process_week."""
    return process_week(md_to_qmd_target(md, inno_files), [md], inno_files, api_key, dry_run)


def process_week(qmd: Path, mds: list[Path], inno_files: Path, api_key: str, dry_run: bool = False) -> bool:
    first = mds[0]
    semester = md_semester(first, inno_files)
    # Guard: only managed semesters (with course_map.json) are ever touched
    if semester not in managed_semesters():
        print(f"  Skip unmanaged semester {first}")
        return False
    rel = first.relative_to(inno_files / semester)
    course = rel.parts[0]
    week = re.match(r"(\d+)", rel.parts[1]).group(1) if len(rel.parts) > 1 else "1"

    transcript = combine_transcripts(mds)
    if not transcript.strip():
        print(f"  Skip empty transcripts {mds}")
        return False

    # If qmd exists and is newer than every source transcript, regeneration still
    # runs (cheap compared to a stale article); mtime check kept for logging only.
    if qmd.exists():
        newest = max(md.stat().st_mtime for md in mds)
        if qmd.stat().st_mtime > newest:
            pass

    style = collect_style_context(short_to_full(course, semester), semester=semester)

    # Generate
    max_iters = 3
    for it in range(1, max_iters + 1):
        print(f"Generating {qmd} iteration {it}/{max_iters} ...")
        try:
            article = generate_article(transcript, course, week, api_key, style,
                                       [md.name for md in mds], semester)
        except Exception as e:
            print(f"  Gemini failed: {e}")
            if it == max_iters:
                raise
            time.sleep(5)
            continue

        # Write atomically
        qmd.parent.mkdir(parents=True, exist_ok=True)
        tmp = qmd.with_suffix(".qmd.tmp")
        tmp.write_text(article, encoding="utf-8")
        tmp.replace(qmd)

        # Fix formatting + renumber
        res = run([sys.executable, "fix_formatting.py"], cwd=str(ROOT))
        if res.returncode != 0:
            print(f"  fix_formatting failed: {res.stderr[:500]}")
        # Renumber if needed (check if headings changed)
        res2 = run([sys.executable, "renumber_examples.py", str(qmd)])
        if res2.returncode != 0:
            print(f"  renumber failed (non-fatal): {res2.stderr[:300]}")

        # Validate fix_formatting report
        report = ROOT / "formatting_report.md"
        if report.exists():
            txt = report.read_text(encoding="utf-8")
            if "No format-rule violations detected" in txt:
                # Try quarto render for this file only
                ok, log = quarto_render_one(qmd)
                if ok:
                    print(f"  OK {qmd} (fix_formatting clean + quarto render ok)")
                    return True
                else:
                    print(f"  Quarto render failed for {qmd}, feeding back to Gemini (attempt {it})...")
                    style = f"Previous attempt failed quarto render with:\n{log[:4000]}\n\nOriginal style context:\n{style[:2000]}"
                    continue
            else:
                # Feed formatting violations back
                print(f"  Formatting violations remain, feeding back (attempt {it})...")
                # Extract snippet
                violations = "\n".join(l for l in txt.splitlines() if qmd.name in l or "Line" in l)[:4000]
                style = f"Previous attempt had formatting violations:\n{violations}\n\nFix these exactly per rules.md. Original transcript(s):\n{transcript[:3000]}"
                continue

    print(f"  Exhausted iterations for {qmd}, removing failed draft so it never pushes")
    try:
        if qmd.exists():
            # Only remove if this run created it (untracked or modified in this run).
            # Keep pre-existing committed versions untouched: restore from git if tracked.
            tracked = run(["git", "ls-files", "--error-unmatch", str(qmd)], cwd=str(ROOT))
            if tracked.returncode == 0:
                run(["git", "checkout", "--", str(qmd)], cwd=str(ROOT))
            else:
                qmd.unlink()
            tmp = qmd.with_suffix(".qmd.tmp")
            if tmp.exists():
                tmp.unlink()
    except Exception as e:  # noqa: BLE001
        print(f"  cleanup failed for {qmd}: {e}")
    return False


def scaffold_semester(semester: str, inno_files: Path) -> Path:
    """Create <semester>/course_map.json skeleton from inno_files folders.

    Teachers start empty (teacher_source "unknown") so resolve_author falls
    back to transcript extraction and finally an em-dash — never a guess.
    Fill `name` with full Moodle course names and `teachers` once known.
    """
    if not re.fullmatch(r"semester-\d+", semester):
        raise ValueError(f"bad semester dir: {semester}")
    src = inno_files / semester
    if not src.is_dir():
        raise ValueError(f"no such inno_files semester: {src}")
    target_dir = ROOT / semester
    target_dir.mkdir(parents=True, exist_ok=True)
    courses = {}
    for code_dir in sorted(d for d in src.iterdir() if d.is_dir() and not d.name.startswith(".")):
        courses[code_dir.name] = {
            "name": code_dir.name,
            "moodle_id": "",
            "moodle_fullname": "",
            "moodle_shortname": "",
            "teachers": [],
            "teacher_source": "unknown",
            "teacher_note": "Scaffolded automatically; fill full Moodle name + teachers.",
        }
    out = {
        "_meta": {
            "semester": semester,
            "comment": "Source of truth for folder names and teachers. Teacher priority: "
                       "registry -> transcript first page -> em-dash (never guess).",
            "teacher_source_priority": ["moodle", "manual", "transcript", "unknown"],
        },
        "courses": courses,
    }
    path = target_dir / "course_map.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"scaffolded {path} with {len(courses)} course(s): {', '.join(courses)}")
    print("Next: fill each `name` with the full Moodle course name and `teachers`;")
    print("then run update_sidebar() (or generate once) to create sidebar sections.")
    return path


def _collect_api_keys(inno_files: Path | None) -> str:
    """All configured Gemini keys, comma-joined (rotation across projects).

    Order: env (GEMINI_API_KEY, GEMINI_API_KEY_2, GEMINI_API_KEY_3,
    GEMINI_API_KEYS, GOOGLE_API_KEY), then inno_files moodle_sync config
    (gemini_api_keys / gemini_api_key). llm.py splits, dedups and
    round-robins the pool on 429. Keys must live in DIFFERENT Cloud
    projects — limits are per project, not per key.
    """
    parts: list[str] = []
    for var in ("GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3",
                "GEMINI_API_KEYS", "GOOGLE_API_KEY"):
        val = os.environ.get(var, "")
        if val:
            parts += re.split(r"[\s,;]+", val)
    if inno_files is not None:
        cfg_path = inno_files / "scripts/moodle_sync/config.json"
        if cfg_path.exists():
            try:
                cfg = json.loads(cfg_path.read_text(encoding="utf-8-sig"))
                for field in ("gemini_api_keys", "gemini_api_key"):
                    val = cfg.get(field) or ""
                    if isinstance(val, list):
                        parts += [str(v) for v in val]
                    else:
                        parts += re.split(r"[\s,;]+", str(val))
            except Exception:
                pass
    keys: list[str] = []
    for piece in parts:
        piece = piece.strip().strip('"').strip("'")
        if piece and piece not in keys:
            keys.append(piece)
    if keys:
        print(f"API key pool: {len(keys)} key(s) configured")
    return ",".join(keys)


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate semester articles from inno_files transcripts")
    ap.add_argument("--inno-files", type=Path, default=INNO_FILES_DEFAULT)
    ap.add_argument("--sha", type=str, default=None)
    ap.add_argument("--semester", action="append", default=None,
                    help="Managed semester to process (repeatable; default: all with course_map.json)")
    ap.add_argument("--scaffold-semester", default=None,
                    help="Create <semester>/course_map.json skeleton from inno_files, then exit")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of lectures to process (for testing)")
    ap.add_argument("--regen-theory", nargs="*", default=None,
                    help="Regenerate ONLY Theory (PRO model) for given qmd path(s), then exit")
    ap.add_argument("--tries", type=int, default=3)
    args = ap.parse_args()

    if args.inno_files and not args.inno_files.exists():
        print(f"inno_files not found at {args.inno_files}, cloning?", file=sys.stderr)
        # Fallback: relative sibling
        alt = Path(__file__).resolve().parents[2].parent / "inno_files"
        if alt.exists():
            args.inno_files = alt

    if args.scaffold_semester:
        scaffold_semester(args.scaffold_semester, args.inno_files)
        update_sidebar()
        return

    api_key = _collect_api_keys(args.inno_files)
    from llm import BACKEND as _LLM_BACKEND
    if not api_key and _LLM_BACKEND != "antigravity":
        print("GEMINI_API_KEY missing (env or inno_files config). Dry-run check only.", file=sys.stderr)
        if not args.dry_run:
            sys.exit(1)

    semesters = args.semester or managed_semesters()
    if not semesters:
        print("No managed semesters (no semester-N/course_map.json). "
              "Run --scaffold-semester first. Exiting (nothing to change).")
        return

    if args.regen_theory:
        # workflow dispatch passes space-separated paths; re-group tokens
        # into existing files so names with spaces survive shell splitting.
        grouped: list[str] = []
        buf = ""
        for tok in args.regen_theory:
            cand = f"{buf} {tok}".strip() if buf else tok
            if (ROOT / cand).exists() or Path(cand).exists():
                grouped.append(cand)
                buf = ""
            else:
                buf = cand
        if buf:
            grouped.append(buf)
        args.regen_theory = grouped
        ok_all = True
        for qp in args.regen_theory:
            qmd = Path(qp) if Path(qp).is_absolute() else ROOT / qp
            try:
                if not regen_theory(qmd, args.inno_files, api_key, tries=args.tries):
                    ok_all = False
            except Exception as e:
                print(f"ERROR regen {qmd}: {e}", file=sys.stderr)
                ok_all = False
        update_sidebar()
        sys.exit(0 if ok_all else 2)

    mds = gather_changed_lectures(args.inno_files, args.sha, semesters)
    if not mds:
        print(f"No transcript changes in {semesters} to process. Exiting (nothing to change).")
        return

    groups = group_lectures(mds, args.inno_files)
    print(f"Found {len(mds)} transcript(s) in {len(groups)} article group(s):")
    for qmd, group in groups:
        srcs = ", ".join(p.relative_to(args.inno_files).as_posix() for p in group)
        print(f"  {srcs} -> {qmd.relative_to(ROOT)}")

    if args.dry_run:
        print("Dry run — not generating.")
        return

    failed: list[Path] = []
    for qmd, group in (groups[: args.limit] if args.limit else groups):
        try:
            ok = process_week(qmd, group, args.inno_files, api_key, dry_run=args.dry_run)
            if not ok:
                failed.extend(group)
        except Exception as e:
            print(f"ERROR processing {qmd}: {e}", file=sys.stderr)
            failed.extend(group)

    if failed:
        print(f"{len(failed)} transcript(s) failed validation, failing the run so broken articles never push:", file=sys.stderr)
        for md in failed:
            print(f"  FAILED: {md}", file=sys.stderr)
        sys.exit(2)

    # Update _quarto.yml sidebar for new files (add missing entries)
    update_sidebar(semesters)


def _ensure_course_section_in(text: str, course: str, semester: str) -> str:
    """Add a missing course section inside the right Semester block."""
    marker = f'- section: "{course}"'
    if marker in text:
        return text
    sem_marker = f'- section: "Semester {semester_roman(semester)}"'
    anchor = sem_marker + '\n        contents: []'
    if anchor in text:
        block = (f'{sem_marker}\n        contents:\n'
                 f'        - section: "{course}"\n          contents: []\n')
        return text.replace(anchor, block, 1)
    # Semester block has contents: find its end (next same-indent section or execute:)
    pat = re.compile(re.escape(sem_marker) + r"\n        contents:\n(.*?)(?=\n      - section:|\nexecute:\n)",
                     re.DOTALL)
    m = pat.search(text)
    if m:
        block = (f'        - section: "{course}"\n          contents: []\n')
        return text[: m.end(1)] + block + text[m.end(1):]
    return _ensure_course_section(text, course)


def _ensure_course_section(text: str, course: str) -> str:
    """Add a missing `- section: "<full course name>"` block (legacy fallback)."""
    marker = f'- section: "{course}"'
    if marker in text:
        return text
    anchor = '      - section: "Semester I"'
    block = (
        f'        - section: "{course}"\n'
        f"          contents: []\n"
    )
    if anchor in text:
        return text.replace(anchor, block + anchor, 1)
    return text


def yml_rel(qmd: Path) -> str:
    """Repo-relative path with forward slashes (Windows gives backslashes)."""
    return qmd.relative_to(ROOT).as_posix()


def _ensure_semester_section(text: str, semester: str) -> str:
    """Add a missing `- section: "Semester X"` block before the `execute:` key."""
    roman = semester_roman(semester)
    marker = f'- section: "Semester {roman}"'
    if marker in text:
        return text
    anchor = "\nexecute:\n"
    assert anchor in text, "_quarto.yml has no top-level execute: anchor"
    block = f'      - section: "Semester {roman}"\n        contents: []\n'
    return text.replace(anchor, "\n" + block + anchor.lstrip("\n"), 1)


def update_sidebar(semesters: list[str] | None = None) -> None:
    """Ensure every managed-semester qmd is listed in _quarto.yml sidebar."""
    semesters = semesters or managed_semesters()
    yml = ROOT / "_quarto.yml"
    original = yml.read_text(encoding="utf-8")
    text = original
    qmds: list[Path] = []
    for sem in semesters:
        text = _ensure_semester_section(text, sem)
        for entry in load_registry(sem).get("courses", {}).values():
            text = _ensure_course_section_in(text, entry.get("name", ""), sem)
        # Find all qmds on disk for this semester
        qmds.extend(sorted((ROOT / sem).rglob("*.qmd")))
    added = 0
    for qmd in qmds:
        rel = yml_rel(qmd)
        if rel not in text:
            course = qmd.parent.name
            text = _ensure_course_section(text, course)
            marker = f'- section: "{course}"'
            pattern = re.compile(re.escape(marker) + r"\s*\n\s+contents:\s*\n")
            m = pattern.search(text)
            if m:
                insert_at = m.end()
                text = text[:insert_at] + f'            - file: "{rel}"\n' + text[insert_at:]
                added += 1
            else:
                # Empty `contents: []` form — expand it
                empty = re.compile(re.escape(marker) + r"\s*\n\s+contents: \[\]")
                m2 = empty.search(text)
                if m2:
                    text = (
                        text[: m2.end()]
                        + f'\n            - file: "{rel}"'
                        + text[m2.end():]
                    )
                    # fix the `contents: []` line into a list header
                    text = text.replace(
                        f'{marker}\n          contents: []\n            - file: "{rel}"',
                        f'{marker}\n          contents:\n            - file: "{rel}"',
                        1,
                    )
                    added += 1
    if text != original:
        yml.write_text(text, encoding="utf-8")
        print(f"Updated _quarto.yml: {added} new file(s), sidebar sections synced")
    # Refresh the home-page course table so new courses/semesters appear automatically
    updater = ROOT / "scripts" / "update_index.py"
    if updater.exists():
        res = run([sys.executable, str(updater)], cwd=str(ROOT))
        if res.returncode != 0:
            print(f"  update_index.py failed: {(res.stderr or '')[:500]}")
        else:
            print("  index.qmd course table refreshed")


if __name__ == "__main__":
    main()
