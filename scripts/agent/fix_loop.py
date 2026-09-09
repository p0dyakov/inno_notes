#!/usr/bin/env python3
"""Block-level auto-fix loop for generated qmd articles.

Flow per article (rounds = 3):
  collect violations -> send ONLY the failing code regions as numbered
  blocks (up to 10 blocks per LLM request, flash fixes each block
  separately) -> splice fixes back -> rebuild (fix_formatting + quarto).
If errors remain after 3 rounds, the article is QUARANTINED, never deleted:
  `draft: true` in front matter + sidebar entry removed + `<stem>.log`
  alongside with error codes. The run still pushes everything; quarantined
  pages stay out of prod build/render/search until a human finishes them.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULES_MD = Path(__file__).resolve().parent / "prompts" / "rules.md"
EXEMPLARS_MD = Path(__file__).resolve().parent / "prompts" / "exemplars.md"
REPORT = ROOT / "scripts" / "formatting_report.md"

WINDOW = 12
BLOCKS_PER_CALL = 10
MAX_CALLS_PER_ROUND = 5
QUAR_MARK = "<!-- QUARANTINE: block-fix loop failed, manual finish needed -->"


def _read_rules() -> str:
    try:
        return RULES_MD.read_text(encoding="utf-8")[:6000]
    except OSError:
        return ""


def _read_exemplars() -> str:
    try:
        return EXEMPLARS_MD.read_text(encoding="utf-8")[:3000]
    except OSError:
        return ""


def _leading_line_no(s: str) -> int:
    if not s.startswith("Line "):
        return 0
    digits = ""
    for ch in s[5:]:
        if ch.isdigit():
            digits += ch
        else:
            break
    return int(digits) if digits else 0


def violation_lines(report_txt: str, qmd: Path) -> tuple[list[str], list[int]]:
    """Our file's violation bullets + anchored 1-based line numbers."""
    bullets: list[str] = []
    nums: list[int] = []
    mine = False
    for ln in report_txt.splitlines():
        if ln.startswith("### "):
            cur = ln[4:].strip()
            mine = bool(cur) and str(qmd).endswith(cur)
            continue
        if ln.startswith("## "):
            mine = False
            continue
        s = ln.strip()
        if mine and s.startswith("-"):
            bullets.append(s)
            n = _leading_line_no(s[2:].strip())
            if n:
                nums.append(n)
    return bullets, nums


def _render_line_refs(log: str) -> list[int]:
    out: list[int] = []
    for ln in log.splitlines():
        if "line" not in ln.lower():
            continue
        tok = ""
        for ch in ln + " ":
            if ch.isdigit():
                tok += ch
            elif tok:
                v = int(tok)
                if 0 < v < 100000 and v not in out:
                    out.append(v)
                tok = ""
    return out[:20]


def _windows(idxs: list[int], total: int, rad: int = WINDOW) -> list[tuple[int, int]]:
    spans = []
    for n in sorted(set(idxs)):
        spans.append((max(1, n - rad), min(total, n + rad)))
    spans.sort()
    merged: list[list[int]] = []
    for a, b in spans:
        if merged and a <= merged[-1][1] + 2:
            if b > merged[-1][1]:
                merged[-1][1] = b
        else:
            merged.append([a, b])
    return [(a, b) for a, b in merged]


def _file_blocks(total: int, size: int = 60) -> list[tuple[int, int]]:
    out = []
    a = 1
    while a <= total:
        out.append((a, min(total, a + size - 1)))
        a += size
    return out


def _fix_prompt(rules: str, violations: list[str], render_excerpt: str,
                blocks: list[tuple[int, int, str]]) -> str:
    parts = ["You fix formatting/build errors in a Quarto article. Style rules:",
             rules,
             "FORMAT EXEMPLARS (shapes that pass validation, imitate exactly):", _read_exemplars(), "VIOLATIONS (authoritative, fix exactly these):"]
    if violations:
        parts.append(chr(10).join(violations))
    else:
        parts.append("(no format violations; fix the render error below)")
    if render_excerpt:
        parts.append("RENDER ERROR:")
        parts.append(render_excerpt[:3000])
    parts.append("CODE BLOCKS (original file line numbers as LNNN: text):")
    for i, (a, b, _t) in enumerate(blocks, 1):
        parts.append("<<<BLOCK " + str(i) + " LINES " + str(a) + "-" + str(b) + ">>>")
        parts.append(_t)
        parts.append("<<<END>>>")
    parts.append("Return ONLY the fixed blocks: repeat each header line exactly, then the FULL corrected lines (no LNNN: prefixes), then <<<END>>>. Fix every block separately. No explanations, no fences.")
    return chr(10).join(parts)


def _parse_fixes(resp: str) -> dict[int, tuple[int, int, list[str]]]:
    out: dict[int, tuple[int, int, list[str]]] = {}
    cur = 0
    a = b = 0
    buf: list[str] = []
    for ln in resp.splitlines():
        s = ln.strip()
        if s.startswith("<<<BLOCK ") and s.endswith(">>>"):
            if cur and buf:
                out[cur] = (a, b, buf)
            inner = s[len("<<<BLOCK "):-len(">>>")].strip()
            bits = inner.split()
            try:
                cur = int(bits[0])
                rng = bits[2].split("-")
                a = int(rng[0])
                b = int(rng[1])
            except (ValueError, IndexError):
                cur = 0
                a = b = 0
            buf = []
            continue
        if s == "<<<END>>>":
            if cur and buf:
                out[cur] = (a, b, buf)
            cur = 0
            buf = []
            continue
        if cur:
            buf.append(ln)
    if cur and buf:
        out[cur] = (a, b, buf)
    return out


def _apply(sent: list[tuple[int, int]], fixes: dict, lines: list[str]) -> tuple[list[str], int]:
    if len(fixes) != len(sent):
        return lines, 0
    for i, (a, b) in enumerate(sent, 1):
        if i not in fixes or fixes[i][0] != a or fixes[i][1] != b:
            return lines, 0
    for i in sorted(range(1, len(sent) + 1), key=lambda k: sent[k - 1][0], reverse=True):
        a, b = sent[i - 1]
        lines[a - 1:b] = fixes[i][2]
    return lines, len(sent)


def _run_fix_format() -> tuple[str, str]:
    try:
        before = REPORT.stat().st_mtime if REPORT.exists() else 0.0
    except OSError:
        before = 0.0
    r = subprocess.run([sys.executable, "scripts/fix_formatting.py"], cwd=str(ROOT),
                       capture_output=True, text=True)
    try:
        after = REPORT.stat().st_mtime if REPORT.exists() else 0.0
    except OSError:
        after = 0.0
    if r.returncode != 0 or after <= before:
        err = ((r.stderr or "") + (r.stdout or ""))[-800:]
        return "", "fix_formatting did not produce a fresh report: " + err
    try:
        return REPORT.read_text(encoding="utf-8"), ""
    except OSError as e:
        return "", "report unreadable: " + str(e)[:200]


def _render_one(qmd: Path) -> tuple[bool, str]:
    try:
        r = subprocess.run(["quarto", "render", str(qmd)], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=900)
    except Exception as e:
        return False, "quarto launch failed: " + str(e)[:300]
    log = (r.stdout or "") + (r.stderr or "")
    return r.returncode == 0, log


def verify(qmd: Path) -> tuple[bool, str, list[str], list[int], str, str]:
    txt, err = _run_fix_format()
    if err:
        return False, "report-stale", [], [], "", err
    bullets, nums = violation_lines(txt, qmd)
    clean = ("No format-rule violations detected" in txt) and not bullets
    ok_render, render_log = _render_one(qmd)
    summary = "violations=" + str(len(bullets)) + " render=" + ("ok" if ok_render else "FAIL")
    return (clean and ok_render), summary, bullets, nums, render_log, ""


def remove_from_sidebar(qmd: Path) -> None:
    yml = ROOT / "_quarto.yml"
    try:
        rel = qmd.relative_to(ROOT).as_posix()
    except ValueError:
        return
    try:
        t = yml.read_text(encoding="utf-8")
    except OSError:
        return
    kept = [l for l in t.splitlines() if not ("- file:" in l and rel in l)]
    if len(kept) != len(t.splitlines()):
        yml.write_text(chr(10).join(kept) + chr(10), encoding="utf-8")
        print("  sidebar entry removed for " + rel)


def quarantine(qmd: Path, history: list[str], report_tail: str, render_tail: str) -> None:
    qmd = Path(qmd)
    lines = qmd.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "---":
        head = [l.strip() for l in lines[1:40]]
        if "draft: true" not in head:
            lines.insert(1, "draft: true")
    else:
        lines = ["---", "draft: true", "---"] + lines
    body = chr(10).join(lines)
    if QUAR_MARK not in body:
        parts = body.split("---", 2)
        if len(parts) >= 3:
            body = "---" + parts[1] + "---" + chr(10) + QUAR_MARK + chr(10) + parts[2]
        else:
            body = QUAR_MARK + chr(10) + body
    if not body.endswith(chr(10)):
        body += chr(10)
    qmd.write_text(body, encoding="utf-8")
    remove_from_sidebar(qmd)
    import datetime as _dt
    logp = qmd.with_suffix(".log")
    entry = (chr(10).join(history)
             + chr(10) + chr(10) + "== violations ==" + chr(10) + report_tail[:4000]
             + chr(10) + chr(10) + "== render ==" + chr(10) + render_tail[-3000:]
             + chr(10) + chr(10) + "quarantined: "
             + _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds") + chr(10))
    logp.write_text(entry, encoding="utf-8")
    print("  QUARANTINED " + str(qmd) + " (draft:true, sidebar removed, .log alongside)")


def toolchain_ok() -> tuple[bool, str]:
    try:
        r = subprocess.run(["quarto", "--version"], capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            return False, "quarto --version failed: " + (r.stderr or "")[:200]
    except Exception as e:
        return False, "quarto missing: " + str(e)[:200]
    try:
        r = subprocess.run([sys.executable, "-c", "import fonttools, brotli"],
                           capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            return False, "fonttools/brotli missing for " + sys.executable + ": " + (r.stderr or "")[:300]
    except Exception as e:
        return False, "toolchain check failed: " + str(e)[:200]
    return True, ""


def fix_article(qmd: Path, rounds: int = 3) -> str:
    """Returns 'ok' or 'quarantined'. Never raises on validation failures."""
    ok_tool, why_tool = toolchain_ok()
    if not ok_tool:
        print("  fix-loop INFRA failure, no LLM rounds burned: " + why_tool)
        return "infra:" + why_tool
    from llm import complete as _complete
    rules = _read_rules()
    history: list[str] = []
    qmd = Path(qmd)
    last_bullets: list[str] = []
    last_render = ""
    for rnd in range(1, rounds + 1):
        ok, summary, bullets, nums, render_log, verr = verify(qmd)
        if verr:
            print("  fix-loop INFRA failure, no LLM rounds burned: " + verr)
            return "infra:" + verr
        last_bullets, last_render = bullets, render_log
        history.append("round " + str(rnd) + ": " + summary)
        print("  fix-loop round " + str(rnd) + ": " + summary)
        if ok:
            return "ok"
        lines = qmd.read_text(encoding="utf-8").splitlines()
        total = len(lines)
        spans = _windows(nums, total)
        if any(not _leading_line_no(x[2:].strip()) for x in bullets):
            spans = sorted(set(spans + [(1, min(total, 40))]))
        render_excerpt = ""
        ok_render = summary.endswith("render=ok")
        if not ok_render:
            render_excerpt = render_log if len(render_log) <= 6000 else render_log[-6000:]
            if not spans:
                refs = _render_line_refs(render_log)
                spans = _windows(refs, total) if refs else _file_blocks(total)[:30]
        if not spans:
            spans = [(1, min(total, 40))]
        payloads = []
        for (a, b) in spans:
            body = chr(10).join("L" + str(n) + ": " + lines[n - 1] for n in range(a, b + 1))
            payloads.append((a, b, body))
        applied = 0
        for ci in range(0, len(payloads), BLOCKS_PER_CALL):
            if ci // BLOCKS_PER_CALL >= MAX_CALLS_PER_ROUND:
                history.append("round " + str(rnd) + ": chunk cap hit, "
                               + str(len(payloads) - ci) + " block(s) deferred")
                break
            chunk = payloads[ci:ci + BLOCKS_PER_CALL]
            prompt = _fix_prompt(rules, bullets, render_excerpt, chunk)
            resp = _complete(prompt, "gemini-3.8-flash",
                             purpose="fix-loop " + qmd.name + " r" + str(rnd))
            fixes = _parse_fixes(resp)
            lines, n = _apply([(a, b) for (a, b, _t) in chunk], fixes, lines)
            applied += n
            if n != len(chunk):
                history.append("round " + str(rnd) + ": malformed fix response ("
                               + str(len(fixes)) + "/" + str(len(chunk)) + " blocks)")
        if applied:
            tmp = qmd.with_suffix(".qmd.tmp")
            tmp.write_text(chr(10).join(lines) + chr(10), encoding="utf-8")
            tmp.replace(qmd)
            history.append("round " + str(rnd) + ": applied " + str(applied) + " block(s)")
        else:
            history.append("round " + str(rnd) + ": nothing applied")
    ok, summary, bullets, _n, render_log, verr = verify(qmd)
    if verr:
        return "infra:" + verr
    history.append("final: " + summary)
    if ok:
        return "ok"
    rep = chr(10).join("- " + x for x in bullets)
    quarantine(qmd, history, rep, render_log)
    return "quarantined"
