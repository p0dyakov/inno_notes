#!/usr/bin/env python3
"""Unified LLM access for inno_notes agent scripts.

Backends (``LLM_BACKEND`` env, default ``apikey`` so CI keeps working):
- ``apikey``: Google AI Studio keys (GEMINI_API_KEY / GEMINI_API_KEY_2 /
  GEMINI_API_KEY_3 / GEMINI_API_KEYS / GOOGLE_API_KEY), direct
  generativelanguage calls. Used in CI and as fallback. Multiple keys are
  pooled: on HTTP 429 the key cools down for 60 s and the next key is tried
  immediately. Keys must come from DIFFERENT Google Cloud projects — limits
  are enforced per project, not per key, so extra keys in one project share
  a single quota.
- ``openlux`` (default for article generation): OpenLux relay
  (https://api.openlux.ai/v1, OpenAI-compatible) with OPENLUX_API_KEY.
  Requested model ids are remapped to OPENLUX_MODEL (default
  gemini-3.8-flash). Per-call token usage is appended to costs.jsonl
  next to this module (see _record_cost); USD estimates stay null until
  base prices are configured in OPENLUX_PRICES_USD_PER_1M.
- ``antigravity``: local Antigravity hub on this machine (logged-in account,
  subscription quota, no key). Mac: Antigravity.app running. Windows: same
  (Antigravity installed + logged in + egress to Google, e.g. Sota).

``complete()`` raises llm_antigravity.TransientError (retry) /
FatalError (don't retry) on the antigravity path and RuntimeError on apikey.
"""

from __future__ import annotations

import os
import re
import threading
import time

import httpx

BACKEND = os.environ.get("LLM_BACKEND", "openlux").strip().lower()

_KEY_ENV_VARS = ("GEMINI_API_KEYS", "GEMINI_API_KEY", "GEMINI_API_KEY_2",
                 "GEMINI_API_KEY_3", "GOOGLE_API_KEY")
_KEY_COOLDOWN_S = 60

_pool_lock = threading.Lock()
_pool_cursor = 0
_key_cooldown_until: dict[str, float] = {}


def _split_keys(explicit: str = "") -> list[str]:
    """All configured keys: explicit arg (comma/space separated) + key env vars."""
    parts: list[str] = []
    if explicit:
        parts += re.split(r"[\s,;]+", explicit)
    for var in _KEY_ENV_VARS:
        val = os.environ.get(var, "")
        if val:
            parts += re.split(r"[\s,;]+", val)
    keys: list[str] = []
    for p in parts:
        p = p.strip().strip('"').strip("'")
        if p and p not in keys:
            keys.append(p)
    return keys


def key_count(explicit: str = "") -> int:
    return len(_split_keys(explicit))


def _mask(key: str) -> str:
    return "..." + key[-4:] if len(key) > 8 else "..."


def _pick_key(keys: list[str]) -> tuple[int, str] | None:
    """Round-robin pick of a non-cooling key, or None if all are cooling."""
    global _pool_cursor
    now = time.monotonic()
    with _pool_lock:
        for _ in range(len(keys)):
            idx = _pool_cursor % len(keys)
            _pool_cursor += 1
            if _key_cooldown_until.get(keys[idx], 0.0) <= now:
                return idx, keys[idx]
    return None


def _cool_key(key: str, secs: float = _KEY_COOLDOWN_S) -> None:
    with _pool_lock:
        _key_cooldown_until[key] = time.monotonic() + secs


def _cooldown_sleep() -> float:
    with _pool_lock:
        if not _key_cooldown_until:
            return 5.0
        wait = min(_key_cooldown_until.values()) - time.monotonic()
    return max(0.0, min(wait, 30.0))


def _tier_for(model: str) -> str:
    m = (model or "").lower()
    if "pro" in m:
        return "pro"
    if "lite" in m:
        return "flash_lite"
    return "flash"


def complete(prompt: str, model: str, api_key: str = "", timeout_s: int = 900,
             title: str = "inno-notes", purpose: str = "") -> str:
    if BACKEND == "openlux":
        return _call_openlux(prompt, model, timeout_s, purpose or title)
    if BACKEND == "antigravity":
        from llm_antigravity import FatalError, Hub, TransientError
        hub = Hub()
        last: Exception | None = None
        for attempt in range(1, 4):
            try:
                return hub.complete(prompt, tier=_tier_for(model), title=title,
                                    timeout_s=timeout_s)
            except TransientError as e:
                last = e
                print(f"  antigravity: transient ({str(e)[:120]}), retry {attempt}/3 ...")
                time.sleep(min(2 ** attempt * 15, 90))
        assert last is not None
        raise last
    return _call_apikey(prompt, api_key, model, timeout_s)


class _RateLimited(RuntimeError):
    """HTTP 429 — quota exhausted on this key, try the next one."""


class _ServerTransient(RuntimeError):
    """HTTP 5xx / timeout / empty response — retryable with backoff."""


class _Fatal(RuntimeError):
    """HTTP 400/401/403 — retrying or switching keys won't help."""


def _post_once(prompt: str, key: str, model: str, timeout_s: int) -> str:
    import json as _json
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.0, "maxOutputTokens": 65536},
    }
    try:
        with httpx.Client(timeout=httpx.Timeout(timeout_s, connect=20.0)) as client:
            resp = client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                headers={"Content-Type": "application/json", "X-goog-api-key": key},
                json=payload,
            )
    except httpx.TimeoutException as e:
        raise _ServerTransient(f"Gemini timeout: {e}")
    except httpx.HTTPError as e:
        raise _ServerTransient(f"Gemini transport error: {e}")
    if resp.status_code == 429:
        raise _RateLimited(f"Gemini HTTP 429: {resp.text[:300]}")
    if resp.status_code in (500, 502, 503, 504):
        raise _ServerTransient(f"Gemini HTTP {resp.status_code}: {resp.text[:300]}")
    if resp.status_code in (400, 401, 403):
        raise _Fatal(f"Gemini HTTP {resp.status_code}: {resp.text[:300]}")
    try:
        resp.raise_for_status()
    except Exception as e:
        raise _Fatal(str(e))
    data = resp.json()
    if "error" in data:
        err = data["error"]
        code = err.get("code") if isinstance(err, dict) else None
        if code == 429:
            raise _RateLimited(f"Gemini API error 429: {err}")
        if code in (500, 502, 503, 504):
            raise _ServerTransient(f"Gemini API error {code}: {err}")
        raise _Fatal(f"Gemini API error: {err}")
    candidates = data.get("candidates") or []
    if not candidates:
        raise _ServerTransient(f"No candidates: {_json.dumps(data)[:800]}")
    parts = (candidates[0].get("content") or {}).get("parts") or []
    if not parts:
        raise _ServerTransient(
            f"Empty parts finish={candidates[0].get('finishReason')} "
            f"raw={_json.dumps(data)[:1000]}")
    text = "\n".join(p.get("text", "") for p in parts if "text" in p).strip()
    if not text:
        raise _ServerTransient(f"Empty text parts: {_json.dumps(data)[:1000]}")
    return text


def _call_apikey(prompt: str, api_key: str, model: str, timeout_s: int = 300) -> str:
    keys = _split_keys(api_key)
    if not keys:
        raise ValueError("GEMINI_API_KEY missing")
    if len(keys) > 1:
        print(f"  apikey: pool of {len(keys)} keys, rotating on 429")
    last_err: Exception | None = None
    # Circuit breaker: all-cooling waits do NOT consume tries (by design - quota
    # may free up), so a fully dead quota would grind forever. Fail fast instead.
    cooling_streak = 0
    max_tries = 2 + 3 * len(keys)
    tries = 0
    while tries < max_tries:
        picked = _pick_key(keys)
        if picked is None:
            cooling_streak += 1
            if cooling_streak > 20:
                raise _RateLimited(
                    f"quota exhausted on all {len(keys)} keys "
                    f"({cooling_streak} consecutive all-cooling waits) - "
                    f"failing fast; retry after quota reset")
            wait = _cooldown_sleep()
            print(f"  apikey: all {len(keys)} keys cooling, sleep {wait:.0f}s...")
            time.sleep(wait)
            continue
        idx, key = picked
        cooling_streak = 0
        try:
            return _post_once(prompt, key, model, timeout_s)
        except _RateLimited as e:
            last_err = e
            tries += 1
            _cool_key(key)
            print(f"  apikey: key {idx + 1}/{len(keys)} ({_mask(key)}) 429 -> "
                  f"cooldown {_KEY_COOLDOWN_S}s, switching key...")
            continue
        except _Fatal:
            raise
        except _ServerTransient as e:
            last_err = e
            tries += 1
            wait = min(2 ** tries, 20)
            print(f"  apikey: transient ({str(e)[:120]}), retry in {wait}s...")
            time.sleep(wait)
            continue
    assert last_err is not None
    raise last_err

OPENLUX_BASE_URL = os.environ.get("OPENLUX_BASE_URL", "https://api.openlux.ai/v1")
OPENLUX_MODEL_DEFAULT = "gemini-3.8-flash"
# Optional base prices to turn token counts into USD estimates:
# OPENLUX_PRICES_USD_PER_1M='{"input": 1.25, "output": 10.0, "reasoning": 10.0}'
LEDGER_NAME = "costs.jsonl"
_cost_totals = {"prompt": 0, "completion": 0, "reasoning": 0, "calls": 0}


def _openlux_model():
    return os.environ.get("OPENLUX_MODEL", OPENLUX_MODEL_DEFAULT)


def _ledger_path():
    from pathlib import Path as _Path
    return str(_Path(__file__).resolve().parent / LEDGER_NAME)


def _usd_estimate(prompt_t, completion_t, reasoning_t):
    import json as _json2
    raw = os.environ.get("OPENLUX_PRICES_USD_PER_1M", "")
    if not raw:
        return None
    try:
        pr = _json2.loads(raw)
        return round(prompt_t * float(pr.get("input", 0))
                     + completion_t * float(pr.get("output", 0))
                     + reasoning_t * float(pr.get("reasoning", pr.get("output", 0)))) / 1000000.0
    except Exception:
        return None


def _record_cost(model, purpose, usage, seconds):
    import datetime as _dt
    import json as _json3
    prompt_t = int((usage or {}).get("prompt_tokens", 0) or 0)
    det = (usage or {}).get("completion_tokens_details") or {}
    reasoning_t = int(det.get("reasoning_tokens", 0) or 0)
    completion_t = int((usage or {}).get("completion_tokens", 0) or 0)
    _cost_totals["prompt"] += prompt_t
    _cost_totals["completion"] += completion_t
    _cost_totals["reasoning"] += reasoning_t
    _cost_totals["calls"] += 1
    entry = {"ts": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
             "backend": "openlux", "model": model, "purpose": purpose,
             "prompt_tokens": prompt_t, "completion_tokens": completion_t,
             "reasoning_tokens": reasoning_t, "seconds": round(seconds, 1),
             "est_usd": _usd_estimate(prompt_t, completion_t, reasoning_t)}
    try:
        with open(_ledger_path(), "a", encoding="utf-8") as f:
            f.write(_json3.dumps(entry, ensure_ascii=False) + chr(10))
    except Exception as e:
        print("  cost ledger write failed: " + str(e)[:120])


def _print_cost_totals():
    t = _cost_totals
    if not t["calls"]:
        return
    print("  [costs] openlux calls=" + str(t["calls"])
          + " prompt_tokens=" + str(t["prompt"])
          + " completion_tokens=" + str(t["completion"])
          + " reasoning_tokens=" + str(t["reasoning"])
          + " ledger=" + LEDGER_NAME)


import atexit as _atexit
_atexit.register(_print_cost_totals)


def _openlux_once(prompt, model, timeout_s):
    import json as _json4
    key = os.environ.get("OPENLUX_API_KEY", "")
    if not key:
        raise ValueError("OPENLUX_API_KEY missing")
    payload = {"model": model,
               "messages": [{"role": "user", "content": prompt}],
               "temperature": 0.0}
    try:
        with httpx.Client(timeout=httpx.Timeout(timeout_s, connect=20.0)) as client:
            resp = client.post(
                OPENLUX_BASE_URL.rstrip("/") + "/chat/completions",
                headers={"Content-Type": "application/json",
                         "Authorization": "Bearer " + key},
                json=payload,
            )
    except httpx.TimeoutException as e:
        raise _ServerTransient("openlux timeout: " + str(e)[:200])
    except httpx.HTTPError as e:
        raise _ServerTransient("openlux transport error: " + str(e)[:200])
    if resp.status_code == 429:
        raise _RateLimited("openlux HTTP 429: " + resp.text[:300])
    if resp.status_code in (500, 502, 503, 504):
        raise _ServerTransient("openlux HTTP " + str(resp.status_code) + ": " + resp.text[:300])
    if resp.status_code in (400, 401, 403):
        raise _Fatal("openlux HTTP " + str(resp.status_code) + ": " + resp.text[:300])
    try:
        resp.raise_for_status()
    except Exception as e:
        raise _Fatal(str(e))
    data = resp.json()
    if isinstance(data, dict) and data.get("error"):
        err = data["error"]
        msg = err.get("message", err) if isinstance(err, dict) else err
        low = str(msg).lower()
        if "rate" in low or "quota" in low or "429" in low:
            raise _RateLimited("openlux: " + str(msg)[:300])
        if "overload" in low or "503" in low or "500" in low:
            raise _ServerTransient("openlux: " + str(msg)[:300])
        raise _Fatal("openlux: " + str(msg)[:300])
    try:
        choice = (data.get("choices") or [])[0]
        text = (choice.get("message") or {}).get("content") or ""
    except Exception:
        text = ""
    if not (text or "").strip():
        raise _ServerTransient("openlux: empty content: " + _json4.dumps(data)[:800])
    return text.strip(), data.get("usage") or {}


def _call_openlux(prompt, model, timeout_s, purpose):
    real_model = _openlux_model()
    if real_model != model:
        print("  openlux: remap " + str(model) + " -> " + real_model)
    last_err = None
    for attempt in range(1, 4):
        t0 = time.monotonic()
        try:
            text, usage = _openlux_once(prompt, real_model, timeout_s)
            _record_cost(real_model, purpose, usage, time.monotonic() - t0)
            return text
        except _RateLimited as e:
            last_err = e
            wait = min(2 ** attempt * 10, 90)
            print("  openlux 429, retry " + str(attempt) + "/3 in " + str(wait) + "s...")
            time.sleep(wait)
        except _ServerTransient as e:
            last_err = e
            wait = min(2 ** attempt * 10, 60)
            print("  openlux transient, retry " + str(attempt) + "/3 in " + str(wait) + "s...")
            time.sleep(wait)
    assert last_err is not None
    raise last_err
