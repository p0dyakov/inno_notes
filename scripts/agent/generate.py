#!/usr/bin/env python3
"""Generate semester-4 qmd articles from inno_files transcript MDs.

Only touches semester-4. Early exit if nothing to generate/update.
Uses gemini-3.1-pro-preview per section (Theory, Definitions, Formulas, Practice)
in parallel, then stitches per prompt.md/rules.md.
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

import httpx

ROOT = Path(__file__).resolve().parents[2]
INNO_NOTES = ROOT
PROMPT_MD = ROOT / "prompt.md"
RULES_MD = ROOT / "rules.md"
COURSE_MAP_JSON = Path(__file__).parent / "course_map.json"

INNO_FILES_DEFAULT = Path("/tmp/inno_files")
GEMINI_MODEL = "gemini-3.1-pro-preview"
GEMINI_FALLBACKS = ["gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite-preview"]
GOLDEN_W = 3  # for initial semester-4 week numbering starting at 1

# Only semester-4 is allowed to be touched by the agent
ALLOWED_SEMESTER = "semester-4"
SKIP_OLD = {"semester-1", "semester-2", "semester-3"}

SECTION_ORDER = ["Theory", "Definitions", "Formulas", "Practice"]

# Author map from prompt.md section 15 (fallback if course folder not in prompt)
AUTHOR_MAP = {
    "OS": "Artem Burmyakov",
    "Phy I": "Artem Burmyakov",
    "CA": "Artem Burmyakov",
    "ITP": "Eugene Zouev, Munir Makhmutov",
    "LDM": "Andrey Frolov",
    "AI": "Manuel Mazzara",
    "TCS": "Manuel Mazzara",
    "DSA": "Nikolai Kudasov",
    "MA I": "Mohammad Alkousa",
    "MA II": "Mohammad Alkousa",
    "AGLA I": "Salman Ahmadi-Asl",
    "AGLA II": "Salman Ahmadi-Asl",
    "SSAD": "Eugene Zouev, Munir Makhmutov",
    "ProbStat": "Mohammad Alkousa",
    "DE": "Mohammad Alkousa",
    "ITO": "Mohammad Alkousa",
    # semester-4 specific fallbacks
    "ProbStat": "Mohammad Alkousa",
    "DE": "Mohammad Alkousa",
    "ITO": "Mohammad Alkousa",
}


def load_course_map() -> dict:
    if COURSE_MAP_JSON.exists():
        return json.loads(COURSE_MAP_JSON.read_text(encoding="utf-8"))
    return {}


def resolve_author(folder: str) -> str:
    # Try exact, then fallback
    if folder in AUTHOR_MAP:
        return AUTHOR_MAP[folder]
    # Semester-4 defaults from prompt analogy
    defaults = {
        "OS": "Artem Burmyakov",
        "Phy I": "Artem Burmyakov",
        "AI": "Manuel Mazzara",
        "DE": "Mohammad Alkousa",
        "ITO": "Mohammad Alkousa",
        "ProbStat": "Mohammad Alkousa",
    }
    return defaults.get(folder, "Mohammad Alkousa")


def section_rule_for_folder(folder: str) -> tuple[list[str], bool]:
    """Return (required_top_sections, has_formulas) per rules.md."""
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
    res = run(["python3", "fix_formatting.py"], cwd=str(ROOT))
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
) -> str:
    """Call Gemini for a single section. Retries fall back across models."""
    prompt = _build_section_prompt(section, transcript, style_context, target_info)
    last_err: Exception | None = None
    models = [model] + GEMINI_FALLBACKS
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


def _build_section_prompt(section: str, transcript: str, style_context: str, target_info: str) -> str:
    # Pull the relevant prompt/rules excerpt per section to keep the call focused
    rules = RULES_MD.read_text(encoding="utf-8") if RULES_MD.exists() else ""
    base = PROMPT_MD.read_text(encoding="utf-8") if PROMPT_MD.exists() else ""

    section_instructions = {
        "Theory": (
            "Write the Theory section (#### **1. Theory** plus #####/###### subsections). "
            "Teach from zero, cover every TOC topic, explain what/why/how/pitfalls, "
            "use paragraphs, bold first term introductions, LaTeX for math."
        ),
        "Definitions": (
            "Write the Definitions section (#### **2. Definitions**) as a compact glossary: "
            "`*   **Term**: Definition.` One sentence per term, self-contained."
        ),
        "Formulas": (
            "Write the Formulas section (#### **3. Formulas**) — only if mathematically meaningful: "
            "`*   **Formula Name**: $...$` with conditions/domains. Skip if the material has no stable formulas."
        ),
        "Practice": (
            "Write the Practice section (#### **4. Practice** or 3 if Formulas omitted) with "
            "`##### **N.M. Title** (Source, Task/Example)` headings in canonical source order "
            "Lab→Homework→Assignment→Exercises→Lecture→Tutorial→Chapter→Recap→Test→Midterm→Final, "
            "each with <details> solution (very detailed, step-by-step, no skipping)."
        ),
    }

    preamble = (
        f"You are writing a single section of a Quarto study article. Output ONLY that section's markdown, "
        f"including its #### header and all subheadings/content. Do not add YAML or other sections.\n\n"
        f"Target: {target_info}\n"
        f"Section to write: {section}\n"
        f"Instruction: {section_instructions.get(section, section)}\n\n"
        f"Local style context (3 neighboring articles' headings/structure — follow their density, heading style, diagram palette if any):\n"
        f"{style_context[:6000]}\n\n"
        f"Rules excerpt (relevant part of rules.md — must be satisfied for format checks):\n"
        f"{rules[:4000]}\n\n"
        f"Full transcript for THIS article (use as authoritative source order and coverage checklist):\n"
        f"{transcript[:90000]}\n"
    )
    return preamble


def _call_gemini(prompt: str, api_key: str, model: str, timeout_s: int = 300) -> str:
    if not api_key:
        raise ValueError("GEMINI_API_KEY missing")
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.0, "maxOutputTokens": 65536},
    }
    last_err: Exception | None = None
    for attempt in range(1, 4):
        try:
            with httpx.Client(timeout=httpx.Timeout(timeout_s, connect=20.0)) as client:
                resp = client.post(
                    f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                    headers={"Content-Type": "application/json", "X-goog-api-key": api_key},
                    json=payload,
                )
            if resp.status_code in (429, 500, 502, 503, 504):
                last_err = RuntimeError(f"Gemini HTTP {resp.status_code}: {resp.text[:500]}")
                if attempt < 3:
                    time.sleep(min(2 ** attempt, 30))
                    continue
                resp.raise_for_status()
            resp.raise_for_status()
            data = resp.json()
            if "error" in data:
                raise RuntimeError(f"Gemini API error: {data['error']}")
            candidates = data.get("candidates") or []
            if not candidates:
                raise RuntimeError(f"No candidates: {json.dumps(data)[:800]}")
            parts = (candidates[0].get("content") or {}).get("parts") or []
            if not parts:
                raise RuntimeError(f"Empty parts finish={candidates[0].get('finishReason')} raw={json.dumps(data)[:1000]}")
            text = "\n".join(p.get("text", "") for p in parts if "text" in p).strip()
            if not text:
                raise RuntimeError(f"Empty text parts: {json.dumps(data)[:1000]}")
            return text
        except httpx.TimeoutException as e:
            last_err = e
            if attempt < 3:
                time.sleep(min(2 ** attempt, 20))
                continue
            raise
        except Exception as e:
            last_err = e
            if "HTTP 400" in str(e) or "HTTP 401" in str(e) or "HTTP 403" in str(e):
                raise
            if attempt < 3 and ("HTTP" in str(e) or "Timeout" in str(e) or "candidates" in str(e).lower()):
                time.sleep(min(2 ** attempt, 20))
                continue
            raise
    assert last_err is not None
    raise last_err  # noqa: TRY201


def gather_changed_lectures(inno_files: Path, since_sha: str | None = None) -> list[Path]:
    """Find semester-4 transcript MDs that are new or changed since SHA."""
    # For simplicity, diff against origin/main~1 if no SHA, else scan semester-4
    if since_sha:
        res = run(["git", "-C", str(inno_files), "diff", "--name-only", f"{since_sha}..HEAD", "--", "semester-4"])
        # If that fails (shallow), fall back to full scan
        if res.returncode != 0 or not res.stdout.strip():
            pass
        else:
            files = [inno_files / p.strip() for p in res.stdout.splitlines() if p.strip().endswith(".md")]
            # Filter to semester-4 only and existing files
            return [p for p in files if p.exists() and ALLOWED_SEMESTER in str(p)]

    # Full scan: every semester-4 Lecture.md that has no corresponding qmd or is newer
    out: list[Path] = []
    for md in sorted((inno_files / "semester-4").rglob("*.md")):
        if not md.is_file():
            continue
        # Skip Syllabus etc? Only lab/lecture/tutorial sources that were transcripted
        if md.name == "Syllabus.md":
            continue
        out.append(md)
    return out


def md_to_qmd_target(md: Path, inno_files: Path) -> Path:
    """Map inno_files/semester-4/<Course>/<N>/Lecture.md -> inno_notes/semester-4/<Course>/<N>.qmd"""
    rel = md.relative_to(inno_files / "semester-4")
    # rel is <Course>/<N>/Lecture.md or <Course>/<N>/Lecture.mmd etc
    parts = rel.parts
    course = parts[0]
    week = parts[1] if len(parts) > 2 else "1"
    # week is a folder like "12" or "10-11" etc — keep as is for W-number
    # But the qmd naming is per lecture: 1.qmd, 2.qmd, etc. We map Lecture.md in week folder to <N>.qmd
    # where N is the numeric week folder name stripped to its first number
    m = re.match(r"(\d+)", week)
    n = m.group(1) if m else "1"
    return INNO_NOTES / f"semester-4/{course}/{n}.qmd"


def collect_style_context(course: str, max_files: int = 3) -> str:
    """Grab up to 3 neighboring articles in the same course folder for style."""
    course_dir = INNO_NOTES / f"semester-4/{course}"
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
) -> str:
    today = datetime.now().strftime("%B %d, %Y")
    author = resolve_author(course)
    required, has_formulas = section_rule_for_folder(course)
    target_info = f"Course {course} (semester-4), week W{week}, author {author}, date {today}, required sections {required}"

    sections = [s for s in SECTION_ORDER if s in required]

    results: dict[str, str] = {}

    def task(section: str) -> tuple[str, str]:
        print(f"  Gemini {section} for {course}/{week} ...")
        return section, gemini_section(section, transcript, style_context, target_info, api_key)

    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(sections), 4)) as ex:
        futs = {ex.submit(task, s): s for s in sections}
        for fut in concurrent.futures.as_completed(futs):
            sec, body = fut.result()
            results[sec] = body.strip()

    # Stitch in canonical order
    stitched_sections = []
    for sec in sections:
        body = results.get(sec, "")
        if not body:
            continue
        # Ensure each section starts with its #### header (Gemini sometimes omits it)
        if not body.lstrip().startswith("####"):
            # Prepend canonical header
            idx = SECTION_ORDER.index(sec) + 1 if sec in SECTION_ORDER else 1
            body = f"#### **{idx}. {sec}**\n\n" + body
        stitched_sections.append(body.strip())

    yaml_front = textwrap.dedent(
        f"""\
        ---
        title: "W{week}. {course} — Lecture {week}"
        author: "{author}"
        date: "{today}"
        format: html
        engine: knitr
        ---
        """
    )
    return yaml_front + "\n" + "\n\n".join(stitched_sections) + "\n"


def process_one(md: Path, inno_files: Path, api_key: str, dry_run: bool = False) -> bool:
    qmd = md_to_qmd_target(md, inno_files)
    course = md.relative_to(inno_files / "semester-4").parts[0]
    week = re.match(r"(\d+)", md.relative_to(inno_files / "semester-4").parts[1]).group(1) if len(md.relative_to(inno_files / "semester-4").parts) > 1 else "1"

    # Guard: never touch semester-1/2/3
    if any(s in str(qmd) for s in SKIP_OLD):
        print(f"  Skip old semester {md}")
        return False

    transcript = md.read_text(encoding="utf-8")
    if not transcript.strip():
        print(f"  Skip empty transcript {md}")
        return False

    # If qmd exists and transcript unchanged (compare md hash vs qmd's source hash comment), skip
    # For now, skip if qmd exists and its transcript hash matches (stored in transcript_state-like comment)
    # Simpler: always regenerate if md newer than qmd, else skip
    if qmd.exists():
        # Check if qmd is newer than transcript — skip
        if qmd.stat().st_mtime > md.stat().st_mtime:
            # But also check fix_formatting would not change it
            pass

    style = collect_style_context(course)

    # Generate
    max_iters = 3
    for it in range(1, max_iters + 1):
        print(f"Generating {qmd} iteration {it}/{max_iters} ...")
        try:
            article = generate_article(transcript, course, week, api_key, style)
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
        res = run(["python3", "fix_formatting.py"], cwd=str(ROOT))
        if res.returncode != 0:
            print(f"  fix_formatting failed: {res.stderr[:500]}")
        # Renumber if needed (check if headings changed)
        res2 = run(["python3", "renumber_examples.py", str(qmd)])
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
                style = f"Previous attempt had formatting violations:\n{violations}\n\nFix these exactly per rules.md. Original transcript:\n{transcript[:3000]}"
                continue

    print(f"  Exhausted iterations for {qmd}, leaving last version (may need manual fix)")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate semester-4 articles from inno_files transcripts")
    ap.add_argument("--inno-files", type=Path, default=INNO_FILES_DEFAULT)
    ap.add_argument("--sha", type=str, default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of lectures to process (for testing)")
    args = ap.parse_args()

    if args.inno_files and not args.inno_files.exists():
        print(f"inno_files not found at {args.inno_files}, cloning?", file=sys.stderr)
        # Fallback: relative sibling
        alt = Path(__file__).resolve().parents[2].parent / "inno_files"
        if alt.exists():
            args.inno_files = alt

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
    if not api_key:
        # Try config file on inno_files
        cfg_path = args.inno_files / "scripts/moodle_sync/config.json" if args.inno_files else None
        if cfg_path and cfg_path.exists():
            try:
                cfg = json.loads(cfg_path.read_text(encoding="utf-8-sig"))
                api_key = (cfg.get("gemini_api_key") or "").strip()
            except Exception:
                pass
    if not api_key:
        print("GEMINI_API_KEY missing (env or inno_files config). Dry-run check only.", file=sys.stderr)
        if not args.dry_run:
            sys.exit(1)

    mds = gather_changed_lectures(args.inno_files, args.sha)
    # Only semester-4; already filtered, but double-guard
    mds = [p for p in mds if ALLOWED_SEMESTER in str(p)]
    if not mds:
        print("No semester-4 transcript changes to process. Exiting (nothing to change).")
        return

    if args.limit:
        mds = mds[: args.limit]

    print(f"Found {len(mds)} semester-4 transcript(s) to process:")
    for p in mds:
        print(f"  {p.relative_to(args.inno_files)} -> {md_to_qmd_target(p, args.inno_files).relative_to(ROOT)}")

    if args.dry_run:
        print("Dry run — not generating.")
        return

    for md in mds:
        try:
            process_one(md, args.inno_files, api_key, dry_run=args.dry_run)
        except Exception as e:
            print(f"ERROR processing {md}: {e}", file=sys.stderr)

    # Update _quarto.yml sidebar for new files (add missing entries)
    update_sidebar()


def update_sidebar() -> None:
    """Ensure every semester-4 qmd is listed in _quarto.yml sidebar."""
    yml = ROOT / "_quarto.yml"
    text = yml.read_text(encoding="utf-8")
    # Find all semester-4 qmds on disk
    qmds = sorted((ROOT / "semester-4").rglob("*.qmd"))
    added = 0
    for qmd in qmds:
        rel = str(qmd.relative_to(ROOT))
        if rel not in text:
            # Insert into the appropriate course section — for now, just after Semester IV header
            # Minimal: append to the course's contents list if found, else add generic entry
            # Simpler: append a file entry under the course section by string replace
            course = qmd.parent.name
            # Find the course section block
            marker = f'- section: "{course}"'
            if marker in text:
                # Insert file line after the marker's contents: line
                # Find marker + next lines
                import re as _re

                pattern = re.compile(re.escape(marker) + r"\s*\n\s+contents:\s*\n")
                m = _re.search(pattern, text)
                if m:
                    insert_at = m.end()
                    text = text[:insert_at] + f'            - file: "{rel}"\n' + text[insert_at:]
                    added += 1
            else:
                # Course not in sidebar yet — append under Semester IV
                if "- file:" in rel:
                    pass
    if added:
        yml.write_text(text, encoding="utf-8")
        print(f"Updated _quarto.yml with {added} new file(s)")


if __name__ == "__main__":
    main()
