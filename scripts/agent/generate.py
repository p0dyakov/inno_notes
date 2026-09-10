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
import threading
from datetime import datetime
from pathlib import Path


from llm import complete as llm_complete
from fix_loop import fix_article

ROOT = Path(__file__).resolve().parents[2]
INNO_NOTES = ROOT
PROMPT_MD = ROOT / "scripts/agent/prompts/prompt.md"
RULES_MD = ROOT / "scripts/agent/prompts/rules.md"
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
# Theory is the most important section: Pro model preferred, strongest flash
# while Pro free quota is limit:0 (Sept 2026). Pro stays first in fallbacks,
# so it is picked up automatically if quota returns.
# Override with GEMINI_THEORY_MODEL env if the model id changes.
GEMINI_THEORY_MODEL = os.environ.get("GEMINI_THEORY_MODEL", "gemini-3.8-flash")
# Flash-only: Pro is limit:0 in practice, so it was dropped from every chain.
GEMINI_THEORY_FALLBACKS = ["gemini-3.8-flash"]
GOLDEN_W = 3  # legacy week-numbering offset, kept for reference

# semesters without course_map.json (e.g. frozen legacy semester-1/2) are never touched

SECTION_ORDER = ["Theory", "Definitions", "Formulas", "Practice"]
# Serializes fix/validate/render across parallel articles (shared report).
_VALIDATE_LOCK = threading.Lock()

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
    # --no-execute: validation render must not need R (knitr runs on Windows build).
    res = run(["quarto", "render", str(qmd), "--no-execute", "-M", "engine:markdown"])
    ok = res.returncode == 0
    log = (res.stdout or "") + (res.stderr or "")
    return ok, log


def fix_formatting_check() -> tuple[bool, str]:
    res = run([sys.executable, "scripts/fix_formatting.py"], cwd=str(ROOT))
    # fix_formatting writes formatting_report.md; check it
    report = ROOT / "scripts/formatting_report.md"
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
                return _call_gemini(prompt, api_key, m, purpose=section)
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
    if section == "Theory":
        raise RuntimeError("Theory is stitched from map parts, never single-shot")
    p = PROMPTS_DIR / f"{section.lower()}.md"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return section


def _exemplars() -> str:
    p = PROMPTS_DIR / "exemplars.md"
    try:
        return p.read_text(encoding="utf-8")[:3000]
    except OSError:
        return ""


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


SELF_STUDY_GOAL = (
    "Article goal: a reader who skipped the lecture learns EVERYTHING from "
    "this article alone. Explain from scratch where the source is terse. "
    "No water: every sentence must add understanding; generic filler is "
    "forbidden. Lose no topic from the sources."
)


def gemini_custom(
    name,
    instruction,
    payload,
    style_context,
    target_info,
    api_key,
    model=GEMINI_THEORY_MODEL,
    fallbacks=None,
):
    """One free-form generation (maps, parts) with the shared goal + style."""
    style_short = style_context[:4000]
    prompt = f"""You are writing part of a Quarto study article. Output ONLY what the instruction asks (section markdown or a JSON array as specified) — no YAML, no extra sections, no commentary.

Target: {target_info}

Goal: {SELF_STUDY_GOAL}

Instruction:
{instruction}

Style context (neighboring articles — follow density and heading style):
{style_short}

Payload:
{payload}"""
    return _call_with_fallbacks_helper(name, prompt, api_key, model, fallbacks)


def _call_with_fallbacks_helper(name, prompt, api_key, model, fallbacks):
    """Model+fallback chain with retries on 429/503/overload."""
    last_err = None
    models = [model] + (fallbacks if fallbacks is not None else GEMINI_FALLBACKS)
    for m in models:
        for attempt in range(1, 4):
            try:
                return _call_gemini(prompt, api_key, m, purpose=name)
            except Exception as e:
                last_err = e
                msg = str(e)
                if "429" in msg or "503" in msg or "overload" in msg.lower():
                    wait = min(2 ** attempt * 5, 60)
                    print(" ", name, ":", m, "failed, retry", attempt, "/3 in", str(wait) + "s...")
                    time.sleep(wait)
                    continue
                raise
        print(" ", name, ":", m, "exhausted, trying next model...")
    assert last_err is not None
    raise last_err


def _parse_json_list(text):
    """First top-level JSON array in model output (tolerates fences/prose)."""
    start = text.find("[")
    if start < 0:
        raise ValueError("no JSON array in model output")
    obj, _ = json.JSONDecoder().raw_decode(text[start:])
    if not isinstance(obj, list):
        raise ValueError("map is not a list")
    return obj


def _gen_map(kind, transcript, style_context, target_info, api_key):
    """Task/theory map with one strict-JSON repair retry."""
    instruction = (PROMPTS_DIR / (kind + ".md")).read_text(encoding="utf-8")
    extra = ""
    last_err = None
    for _ in (1, 2):
        try:
            out = gemini_custom(
                kind, instruction + extra,
                "FULL TRANSCRIPT (authoritative): " + transcript[:100000],
                style_context, target_info, api_key,
            )
            items = _parse_json_list(out)
            print(" ", kind, ":", len(items), "entries")
            return items
        except Exception as e:
            last_err = e
            print(" ", kind, "attempt failed, retrying with strict-JSON nudge...")
            extra = "Return ONLY the JSON array. No prose, no fences."
    assert last_err is not None
    raise last_err


def gen_task_map(transcript, style_context, target_info, api_key):
    return _gen_map("taskmap", transcript, style_context, target_info, api_key)


def gen_theory_map(transcript, style_context, target_info, api_key):
    items = _gen_map("theorymap", transcript, style_context, target_info, api_key)
    if not items:
        raise ValueError("theory map is empty - refusing contentless Theory")
    return items


def force_part_heading(body, sec_num, idx, title):
    """Enforce the map-order ##### heading on a theory part."""
    want = "##### **" + str(sec_num) + "." + str(idx) + " " + str(title) + "**"
    out = []
    done = False
    for ln in body.splitlines():
        s = ln.strip()
        if (not done) and s.startswith("#####") and not s.startswith("######"):
            out.append(want)
            done = True
        else:
            out.append(ln)
    if not done:
        out = [want, ""] + out
    return chr(10).join(out)


def gen_theory_part(topic, siblings, sec_num, idx, transcript, style_context,
                    target_info, api_key, feedback=None):
    """Write one ##### theory part for a map topic."""
    instruction = (PROMPTS_DIR / "theory_part.md").read_text(encoding="utf-8") + chr(10) + chr(10) + _exemplars()
    topic_json = json.dumps(topic, ensure_ascii=False)
    sib_lines = []
    for t in siblings:
        sib_lines.append("- " + str(t))
    payload = (
        "YOUR TOPIC (heading must be exactly `##### **"
        + str(sec_num) + "." + str(idx) + " " + str(topic.get("title", "Topic"))
        + "**`): " + chr(10) + topic_json + chr(10) + chr(10)
        + "SIBLING TOPICS (covered separately - do not duplicate): " + chr(10)
        + chr(10).join(sib_lines) + chr(10) + chr(10)
        + "FULL TRANSCRIPT (source of facts): " + chr(10) + transcript[:100000]
        + (chr(10) + chr(10) + "FEEDBACK ON PREVIOUS DRAFT (fix exactly, keep everything else): "
           + chr(10) + feedback[:3000] if feedback else "")
    )
    body = gemini_custom(
        "theory-" + str(sec_num) + "." + str(idx),
        instruction, payload, style_context, target_info, api_key,
    ).strip()
    return force_part_heading(body, sec_num, idx, topic.get("title", "Topic"))


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
        f"Canonical formatting exemplars (copy heading shapes exactly, they pass validation):{chr(10)}{_exemplars()}{chr(10)}{chr(10)}"
        f"Full transcript for THIS article (use as authoritative source order and coverage checklist):\n"
        f"{transcript[:90000]}\n"
    )
    return preamble


def _call_gemini(prompt: str, api_key: str, model: str, timeout_s: int = 300,
                 purpose: str = "") -> str:
    """Single generation via the configured LLM backend (see llm.py).

    antigravity backend ignores api_key (local hub auth); apikey backend
    preserves the previous direct generativelanguage behavior for CI.
    purpose labels the call in the cost ledger (openlux backend).
    """
    return llm_complete(prompt, model, api_key=api_key, timeout_s=timeout_s,
                        purpose=purpose)


def gather_changed_lectures(
    inno_files: Path, since_sha: str | None = None, semesters: list[str] | None = None,
) -> list[Path]:
    """Find transcript MDs in managed semesters that are new or changed since SHA."""
    semesters = semesters or managed_semesters()
    managed = set(semesters)
    if since_sha:
        # Scope = the triggering commit itself (what this push added/changed).
        # NOTE: callers check out exactly since_sha, so `since_sha..HEAD` would
        # always be empty and silently degrade to a full regen of every article
        # (observed: multi-hour runs re-rolling the whole semester). Compare
        # against the first parent instead; full scan stays for manual runs
        # without --sha.
        res = run(["git", "-C", str(inno_files), "diff", "--name-only",
                   f"{since_sha}^..{since_sha}", "--"] + semesters)
        if res.returncode != 0 or not res.stdout.strip():
            pass
        else:
            files = [inno_files / p.strip() for p in res.stdout.splitlines() if p.strip().endswith(".md")]
            # Keep only existing files inside managed semesters
            picked = [p for p in files if p.exists() and md_semester_safe(p, inno_files) in managed]
            if picked:
                return picked
            print(f"  push {since_sha[:12]} touched no transcripts; falling back to full scan")
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


def _source_number(stem: str, kind: str) -> str:
    i = stem.lower().find(kind.lower()) + len(kind)
    digits = ""
    for ch in stem[i:]: 
        if ch.isdigit():
            digits += ch
        elif digits:
            break
    return digits or "1"


def source_kind(md_name: str) -> str:
    """Canonical Practice source label WITH number (Tutorial-2.md -> Tutorial 2)."""
    stem = Path(md_name).stem
    for kind in SOURCE_KINDS:
        if kind.lower() in stem.lower():
            if kind == "Homework":
                return kind
            return kind + " " + _source_number(stem, kind)
    return stem


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



TASK_MARKER_RE = re.compile(
    r"(?i)(?:example|task|exercise|problem|вопрос|задач[аи]|пример)\s*\d"
    r"|(?:Example|Task|Exercise|Problem)\s+\d"
)
# Transcript section headings like "### Example" / "## Task" (singular item
# headings, NOT topic titles like "Jobs Are Collections of Tasks" or prose
# "for example, ..."): also explicit items. Lecture slides often number
# nothing but still carry worked examples under such headings.
TASK_HEADING_RE = re.compile(r"(?im)^#{1,4}\s*(example|task|exercise|problem)\b(?!s\b)")

def transcript_has_explicit_tasks(transcript: str) -> bool:
    """True only if the source transcript names explicit tasks/examples.

    Two shapes count: numbered markers ("Problem 7", "Task 3.1") and singular
    item headings ("### Example"). No explicit tasks -> the article gets NO
    Practice section at all (never author synthetic tasks)."""
    return bool(TASK_MARKER_RE.search(transcript)
                or TASK_HEADING_RE.search(transcript))


def article_context(transcript, course, week, api_key, sources=None, semester="semester-4"):
    """Title/author/sections/target block shared by fresh and retry generations."""
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
            f"in canonical order Lab-Homework-Assignment-Exercises-Lecture-Tutorial-Chapter-Recap-Test-Midterm-Final."
        )
    target_info = (
        f"Course {full_name} ({semester}), week W{week}, author {author}, date {today}, "
        f"required sections {required}. Article title is {title!r} - do not restate it in section bodies.{src_note} "
        f"Goal: self-study article readable from scratch: full theory, no fluff, no lost topics."
    )
    return {"title": title, "author": author, "required": required,
            "target_info": target_info, "today": today}


def generate_article(
    transcript,
    course,
    week,
    api_key,
    style_context,
    sources=None,
    semester="semester-4",
    ctx=None,
    task_map=None,
    theory_map=None,
    feedback=None,
):
    if ctx is None:
        ctx = article_context(transcript, course, week, api_key, sources, semester)
    title = ctx["title"]
    author = ctx["author"]
    required = list(ctx["required"])
    target_info = ctx["target_info"]
    today = ctx["today"]
    if feedback is None and style_context.startswith("Previous attempt"):
        feedback = style_context[:3000]
    sections = [s for s in SECTION_ORDER if s in required]

    # ---- Stage A (parallel): maps + Definitions + Formulas ----
    amaps = {}
    if task_map is not None:
        amaps["task"] = task_map
    if theory_map is not None:
        amaps["theory"] = theory_map
    asec = {}

    def run_defs():
        return gemini_section(
            "Definitions", transcript, style_context, target_info, api_key,
            model=GEMINI_THEORY_MODEL,
            fallbacks=GEMINI_THEORY_FALLBACKS + GEMINI_FALLBACKS)

    def run_forms():
        return gemini_section(
            "Formulas", transcript, style_context, target_info, api_key,
            model=GEMINI_THEORY_MODEL,
            fallbacks=GEMINI_THEORY_FALLBACKS + GEMINI_FALLBACKS)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futs = {}
        if "Definitions" in required:
            futs[ex.submit(run_defs)] = ("sec", "Definitions")
        if "Formulas" in required:
            futs[ex.submit(run_forms)] = ("sec", "Formulas")
        if "Practice" in required and "task" not in amaps:
            print(f"  task map (flash) for {course}/{week} ...")
            futs[ex.submit(gen_task_map, transcript, style_context, target_info, api_key)] = ("map", "task")
        if "Theory" in required and "theory" not in amaps:
            print(f"  theory map (flash) for {course}/{week} ...")
            futs[ex.submit(gen_theory_map, transcript, style_context, target_info, api_key)] = ("map", "theory")
        for fut in concurrent.futures.as_completed(futs):
            kind, name = futs[fut]
            if kind == "sec":
                asec[name] = fut.result().strip()
            else:
                amaps[name] = fut.result()

    task_map = amaps.get("task", [])
    theory_map = amaps.get("theory", [])
    if "Practice" in required and not task_map:
        print(f"  {course}/{week}: task map empty -> omitting Practice section")
        required = [s for s in required if s != "Practice"]
        sections = [s for s in SECTION_ORDER if s in required]

    # ---- Stage B (parallel): Practice from map + Theory parts from map ----
    practice_body = ""
    part_bodies = []
    bjobs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        futs2 = {}
        if "Practice" in required and task_map:
            practice_instruction = (PROMPTS_DIR / "practice.md").read_text(encoding="utf-8") + chr(10) + chr(10) + _exemplars()
            practice_payload = (
                "TASK MAP (authoritative item set, write every entry in map order): "
                + chr(10) + json.dumps(task_map, ensure_ascii=False)
                + chr(10) + chr(10)
                + "FULL TRANSCRIPT (solution details): "
                + chr(10) + transcript[:100000]
            )
            print(f"  Gemini Practice from map ({len(task_map)} items) for {course}/{week} ...")
            futs2[ex.submit(
                gemini_custom, "Practice", practice_instruction, practice_payload,
                style_context, target_info, api_key)] = ("practice", -1)
        if "Theory" in required and theory_map:
            tidx = sections.index("Theory") + 1
            siblings = [str(t.get("title", "Topic")) for t in theory_map]
            for k, topic in enumerate(theory_map, start=1):
                print(f"  Gemini theory-{tidx}.{k} ({str(topic.get('title', ''))[:50]}) for {course}/{week} ...")
                futs2[ex.submit(
                    gen_theory_part, topic, siblings, tidx, k,
                    transcript, style_context, target_info, api_key, feedback=feedback)] = ("part", k)
        for fut in concurrent.futures.as_completed(futs2):
            kind, k = futs2[fut]
            if kind == "practice":
                practice_body = fut.result().strip()
            else:
                part_bodies.append((k, fut.result().strip()))
    part_bodies.sort(key=lambda pair: pair[0])

    # ---- Stage C: deterministic stitch, sequential numbering ----
    # Numbers follow sections ACTUALLY present (EMPTY-dropped Formulas shifts
    # everything after it — no gaps like a missing 3.).
    results = dict(asec)
    if "Practice" in required and practice_body:
        results["Practice"] = practice_body
    present = []
    for sec in sections:
        if sec == "Theory":
            if part_bodies:
                present.append(sec)
            continue
        body = results.get(sec, "")
        if not body:
            continue
        if body.strip() == "<!-- EMPTY -->":
            continue
        present.append(sec)
    stitched_sections = []
    for sec in present:
        idx = present.index(sec) + 1
        if sec == "Theory":
            body = "#### **" + str(idx) + ". Theory**" + chr(10) + chr(10) + (chr(10) + chr(10)).join(
                part for _, part in part_bodies)
            stitched_sections.append(body.strip())
            continue
        body = results.get(sec, "")
        mh = re.match(r"(\s*####\s+\*\*)(\d+)(\.\s+)", body)
        if mh:
            body = mh.group(1) + str(idx) + mh.group(3) + body[mh.end():]
        else:
            body = "#### **" + str(idx) + ". " + sec + "**" + chr(10) + chr(10) + body
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
    return yaml_front + chr(10) + (chr(10) + chr(10)).join(stitched_sections) + chr(10)


def theory_stats(body: str) -> tuple[int, int]:
    """(total words, ##### subsection count) of a Theory section body."""
    subs = re.split(r"^##### ", body, flags=re.M)[1:]
    return sum(len(s.split()) for s in subs), len(subs)




_TOPIC_SKIP_RE = re.compile(
    r"^(innopolis university|outline|contents|table of contents|references?|pages?|"
    r"end of lecture|sources|syllabus|chapter\s+\d+)$", re.I)
_STOPWORDS = frozenset(
    "with from into over under what when where which while their there "
    "these those have has had been were are and the for vii viii iii ii iv "
    "aka etc via per our your its this that than then them they you we".split())


def _sig_words(text: str) -> list[str]:
    words = re.findall(r"[a-z]{3,}", text.lower())
    seen, out = set(), []
    for w in words:
        if w not in _STOPWORDS and w not in seen:
            seen.add(w)
            out.append(w)
    return out


def _clean_topic_line(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^\*\*|\*\*$", "", s).strip()
    s = re.sub(r"^#{1,3}\s*", "", s)
    s = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", s)
    s = re.sub(r"^[\*\-\u2022]\s+", "", s)
    s = re.sub(r"\s*(?:\.\s*){2,}\d+\s*$", "", s)
    s = re.sub(r"\s*\.{2,}\s*\d+\s*$", "", s)
    s = re.sub(r"\s*\*{0,2}\d+\s*\*{0,2}$", "", s)
    s = re.sub(r"\s*\(\s*cite as:[^)]*\)\s*$", "", s, flags=re.I)
    return s.strip(" *-_").strip()


_ADMIN_MARKERS = (
    "grade breakdown", "assessment elements", "course structure",
    "office hours", "bibliography", "course description",
)


def is_admin_only(transcript: str) -> bool:
    """True when the source holds no teachable content (course admin slides:
    schedule, grading, bibliography) — no article should be fabricated."""
    low = transcript.lower()
    words = re.findall(r"[a-z]{3,}", low)
    if len(words) >= 600:
        return False
    signals = transcript.count("$") + len(re.findall(
        r"\b(example|task|exercise|definition|theorem|proof)\b", low))
    if signals >= 3:
        return False
    return sum(1 for m in _ADMIN_MARKERS if m in low) >= 2


def transcript_topics(transcript: str) -> list[str]:
    """Checklist of examinable topics from the source.

    Prefers an explicit Contents/Outline block (dotted TOC lines or slide
    bullets); falls back to markdown headers + per-page slide titles.
    """
    lines = transcript.splitlines()
    topics: list[str] = []

    def accept(raw: str) -> None:
        c = _clean_topic_line(raw)
        if c and not _TOPIC_SKIP_RE.match(c) and len(c) > 3:
            topics.append(c)

    for i, line in enumerate(lines):
        if re.match(r"^\s*(#{1,3}\s*)?(contents|outline|table of contents|"
                     r"\u043e\u0433\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u0435|"
                     r"\u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435)\s*$", line, re.I):
            blanks = 0
            for j in range(i + 1, min(i + 60, len(lines))):
                s = lines[j].strip()
                if s.startswith(("---", "## Page", "# SOURCE")):
                    break
                if re.match(r"^# ", s):
                    break
                if not s:
                    blanks += 1
                    if blanks >= 2 and topics:
                        break
                    continue
                blanks = 0
                accept(s)
            break
    if topics:
        return topics

    for i, line in enumerate(lines):
        s = line.strip()
        if re.match(r"^#{1,3} ", s):
            accept(s)
            continue
        if re.match(r"^## Page \d+", s):
            for j in range(i + 1, min(i + 6, len(lines))):
                s2 = lines[j].strip()
                if not s2 or s2.startswith(("[Image", "---", "## Page", "# SOURCE")):
                    continue
                c = _clean_topic_line(s2)
                if (c and not _TOPIC_SKIP_RE.match(c) and len(c) > 3
                        and not re.fullmatch(r"[\d/ ]+", c)):
                    topics.append(c)
                break
    seen, out = set(), []
    for topic in topics:
        key = topic.lower()
        if key not in seen:
            seen.add(key)
            out.append(topic)
    return out


def coverage_gap(theory: str, topics: list[str]) -> list[str]:
    """Topics from the source checklist missing in the Theory body."""
    tokens = set(re.findall(r"[a-z]{3,}", theory.lower()))
    low = theory.lower()
    missing = []
    for topic in topics:
        sig = _sig_words(topic)
        if not sig:
            continue
        need = len(sig) if len(sig) <= 2 else max(2, round(len(sig) * 0.6))

        def hit(w: str) -> bool:
            if w in low:
                return True
            return any(tok.startswith(w[:5]) for tok in tokens) if len(w) >= 5 else False

        if sum(1 for w in sig if hit(w)) < need:
            missing.append(topic)
    return missing


def regen_theory(qmd: Path, inno_files: Path, api_key: str, tries: int = 3) -> bool:
    rel = qmd.relative_to(INNO_NOTES)
    semester = rel.parts[0]
    course_full, week = rel.parts[1], Path(rel.parts[2]).stem
    code = canon_code(semester, course_full)
    mds = _week_mds(code, week, inno_files, semester)
    if not mds:
        print(f"  no transcripts for {qmd}")
        return False
    transcript = combine_transcripts(mds)
    full_name = short_to_full(code, semester)
    author = resolve_author(code, transcript, semester)
    required, _ = section_rule_for_folder(code, semester)
    style = collect_style_context(course_full, semester=semester)
    old = qmd.read_text(encoding="utf-8")
    title = f"W{week}. Notes"
    for ln in old.splitlines():
        s = ln.strip()
        if s.startswith('title: "') and s.endswith('"') and len(s) > 9:
            title = s[len('title: "'):-1]
            break
    target_info = (
        f"Course {full_name} ({semester}), week W{week}, author {author}, "
        f"required sections {required}. Article title is {title!r} - do not restate it. "
        f"Regenerate ONLY the Theory section; keep full depth per the instruction."
    )
    topics = transcript_topics(transcript)
    print(f"  coverage checklist: {len(topics)} topic(s)")
    best, best_key = "", (10 ** 9, 0)
    try:
        tmap = gen_theory_map(transcript, style, target_info, api_key)
    except Exception as e:
        print(f"  theory map failed: {e}")
        return False
    for it in range(1, tries + 1):
        print(f"  Theory parts attempt {it}/{tries} for {qmd.relative_to(ROOT)} ...")
        siblings = [str(t.get("title", "Topic")) for t in tmap]
        parts = [None] * len(tmap)
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(tmap), 6)) as ex:
            futs = {}
            for k, topic in enumerate(tmap, start=1):
                futs[ex.submit(gen_theory_part, topic, siblings, 1, k,
                               transcript, style, target_info, api_key)] = k
            for fut in concurrent.futures.as_completed(futs):
                parts[futs[fut] - 1] = fut.result().strip()
        body = "#### **1. Theory**" + chr(10) + chr(10) + (chr(10) + chr(10)).join(parts)
        words, subs = theory_stats(body)
        missing = coverage_gap(body, topics)
        print(f"    stats: {words} words, {subs} subsections, "
              f"missing topics: {len(missing)}")
        for m in missing:
            print("      - MISSING: " + str(m)[:90])
        key = (len(missing), -words)
        if key < best_key:
            best, best_key = body, key
        if not missing:
            break
        time.sleep(5)
    words, subs = theory_stats(best)
    missing = coverage_gap(best, topics)
    print(f"  Theory stats: {words} words, {subs} subsections (no minimum - depth follows input size)")
    replacement = best.rstrip() + chr(10) + chr(10)
    head = "#### **1. Theory**"
    i = old.find(head)
    assert i >= 0, "Theory header not found"
    j = old.find(chr(10) + "#### ", i + len(head))
    new = old[:i] + replacement + (old[j + 1:] if j >= 0 else "")
    assert new != old, "Theory splice failed"
    qmd.write_text(new, encoding="utf-8")
    run([sys.executable, "scripts/fix_formatting.py"], cwd=str(ROOT))
    print(f"  Theory replaced: {words} words, {subs} subsections")
    return True


def _week_mds(code, week, inno_files, semester="semester-4"):
    """Transcript .md files for one (course, week)."""
    cdir = inno_files / semester / code
    if not cdir.is_dir():
        return []
    out = []
    for wd in sorted(cdir.iterdir()):
        if not wd.is_dir():
            continue
        digits = ""
        for ch in wd.name:
            if ch.isdigit():
                digits = digits + ch
            else:
                break
        if digits != str(week):
            continue
        for md in sorted(wd.glob("*.md")):
            if md.name != "Syllabus.md":
                out.append(md)
    return out


def regen_article(qmd, inno_files, api_key):
    """Full regenerate of one article with the staged flow (maps + parts)."""
    try:
        rel = qmd.relative_to(INNO_NOTES)
    except ValueError:
        print(f"  {qmd} is outside the notes repo")
        return False
    if len(rel.parts) < 3:
        print(f"  cannot infer course/week from {qmd}")
        return False
    semester = rel.parts[0]
    course_full, week = rel.parts[1], Path(rel.parts[2]).stem
    code = canon_code(semester, course_full)
    mds = _week_mds(code, week, inno_files, semester)
    if not mds:
        print(f"  no transcripts for {qmd}")
        return False
    target = qmd if qmd.is_absolute() else ROOT / qmd
    return process_week(target, mds, inno_files, api_key, dry_run=False, force=True)


def _group_qmd_paths(tokens):
    # Workflow inputs are COMMA-separated (paths contain spaces, so plain
    # shell splitting cannot work; existence checks cannot work for NEW
    # articles either). Join everything back and split on commas.
    joined = " ".join(tokens or [])
    return [c.strip() for c in joined.split(",") if c.strip()]


def process_one(md: Path, inno_files: Path, api_key: str, dry_run: bool = False) -> bool:
    """Legacy single-file entry kept for tests; delegates to process_week."""
    return process_week(md_to_qmd_target(md, inno_files), [md], inno_files, api_key, dry_run)


def fix_loop_mark(qmd: Path) -> bool:
    try:
        head = qmd.read_text(encoding="utf-8")[:3000]
    except OSError:
        return False
    return "<!-- QUARANTINE" in head


def process_week(qmd: Path, mds: list[Path], inno_files: Path, api_key: str, dry_run: bool = False, force: bool = False) -> bool:
    first = mds[0]
    semester = md_semester(first, inno_files)
    # Guard: only managed semesters (with course_map.json) are ever touched
    if semester not in managed_semesters():
        print(f"  Skip unmanaged semester {first}")
        return False
    rel = first.relative_to(inno_files / semester)
    course = rel.parts[0]
    week = re.match(r"(\d+)", rel.parts[1]).group(1) if len(rel.parts) > 1 else "1"

    if qmd.exists() and "<!-- HANDWRITTEN -->" in qmd.read_text(encoding="utf-8")[:2000]:
        print(f"  Skip hand-written article (locked) {qmd.relative_to(ROOT)}")
        return True
    if qmd.exists() and not force and fix_loop_mark(qmd):
        print(f"  Skip quarantined article (manual finish pending) {qmd.relative_to(ROOT)}")
        return True
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
    ctx = article_context(transcript, course, week, api_key,
                          [md.name for md in mds], semester)
    # Maps are built ONCE per article and reused by the fix loop below.
    pre_task, pre_theory = None, None
    try:
        if "Practice" in ctx["required"]:
            pre_task = gen_task_map(transcript, style, ctx["target_info"], api_key)
        if "Theory" in ctx["required"]:
            pre_theory = gen_theory_map(transcript, style, ctx["target_info"], api_key)
    except Exception as e:
        print("  maps failed, will rebuild per iteration...")
        pre_task, pre_theory = None, None

    # Generate once (maps prebuilt above; llm_cache makes reruns cheap).
    print(f"Generating {qmd} ...")
    try:
        article = generate_article(transcript, course, week, api_key, style,
                                   [md.name for md in mds], semester,
                                   ctx=ctx, task_map=pre_task,
                                   theory_map=pre_theory)
    except Exception as e:
        print(f"  Gemini failed: {e}")
        return False

    # Write atomically
    qmd.parent.mkdir(parents=True, exist_ok=True)
    tmp = qmd.with_suffix(".qmd.tmp")
    tmp.write_text(article, encoding="utf-8")
    tmp.replace(qmd)

    # One article at a time here: fix/report/render share state.
    with _VALIDATE_LOCK:
        # Deterministic pre-pass: formatting autofix + renumber
        res = run([sys.executable, "scripts/fix_formatting.py"], cwd=str(ROOT))
        if res.returncode != 0:
            print(f"  fix_formatting failed: {res.stderr[:500]}")
        res2 = run([sys.executable, "scripts/renumber_examples.py", str(qmd)])
        if res2.returncode != 0:
            print(f"  renumber failed (non-fatal): {res2.stderr[:300]}")
        # Block-level fix loop (up to 3 rounds), then quarantine (never delete).
        status = fix_article(qmd, rounds=3)
        if status == "ok":
            print(f"  OK {qmd} (fix-loop clean + quarto render ok)")
            stale_log = qmd.with_suffix(".log")
            if stale_log.exists():
                stale_log.unlink()
                print(f"  removed stale quarantine log {stale_log.name}")
            return True
        if status.startswith("infra:"):
            print(f"  INFRA failure, failing run (no quarantine): {status[6:]}")
            return False
        print(f"  KEPT AS QUARANTINE {qmd} (pushed with .log, hidden from prod)")
        return True



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
    ap.add_argument("--regen-article", nargs="*", default=None,
                    help="Regenerate WHOLE article(s) with the staged flow (maps + parts) for given qmd path(s), then exit")
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
        args.regen_theory = _group_qmd_paths(args.regen_theory)
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

    if args.regen_article:
        args.regen_article = _group_qmd_paths(args.regen_article)
        ok_all = True
        for qp in args.regen_article:
            qmd = Path(qp) if Path(qp).is_absolute() else ROOT / qp
            try:
                if not regen_article(qmd, args.inno_files, api_key):
                    ok_all = False
            except Exception as e:
                print(f"ERROR regen-article {qmd}: {e}", file=sys.stderr)
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
    items = groups[: args.limit] if args.limit else groups

    def _one(item):
        qmd, group = item
        try:
            ok = process_week(qmd, group, args.inno_files, api_key, dry_run=args.dry_run)
            if not ok:
                return list(group)
        except Exception as e:
            print(f"ERROR processing {qmd}: {e}", file=sys.stderr)
            return list(group)
        return []

    if len(items) > 1:
        print(f"Processing {len(items)} article(s) with 2 parallel workers (validate serializes) ...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
            for res in ex.map(_one, items):
                failed.extend(res)
    else:
        for res in map(_one, items):
            failed.extend(res)

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


def _is_draft_qmd(qmd: Path) -> bool:
    """Hidden sample-based drafts (`draft: true` in YAML front matter).

    Drafts keep their sources/solutions on disk but stay out of the sidebar,
    the render set and search until real lec/tut transcripts land (see the
    SAMPLE-BASED DRAFT comment inside such files for the regen path).
    """
    try:
        parts = qmd.read_text(encoding="utf-8").split("---", 2)
    except OSError:
        return False
    return len(parts) >= 3 and re.search(r"(?m)^draft:\s*true\s*$", parts[1]) is not None


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
        if _is_draft_qmd(qmd):
            continue
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
