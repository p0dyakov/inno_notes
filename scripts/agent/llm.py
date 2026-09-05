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

BACKEND = os.environ.get("LLM_BACKEND", "apikey").strip().lower()

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
             title: str = "inno-notes") -> str:
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
    max_tries = 2 + 3 * len(keys)
    tries = 0
    while tries < max_tries:
        picked = _pick_key(keys)
        if picked is None:
            wait = _cooldown_sleep()
            print(f"  apikey: all {len(keys)} keys cooling, sleep {wait:.0f}s...")
            time.sleep(wait)
            continue
        idx, key = picked
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
