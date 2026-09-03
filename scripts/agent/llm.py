#!/usr/bin/env python3
"""Unified LLM access for inno_notes agent scripts.

Backends (``LLM_BACKEND`` env, default ``apikey`` so CI keeps working):
- ``apikey``: Google AI Studio key (GEMINI_API_KEY / GOOGLE_API_KEY),
  direct generativelanguage calls. Used in CI and as fallback.
- ``antigravity``: local Antigravity hub on this machine (logged-in account,
  subscription quota, no key). Mac: Antigravity.app running. Windows: same
  (Antigravity installed + logged in + egress to Google, e.g. Sota).

``complete()`` raises llm_antigravity.TransientError (retry) /
FatalError (don't retry) on the antigravity path and RuntimeError on apikey.
"""

from __future__ import annotations

import os
import time

import httpx

BACKEND = os.environ.get("LLM_BACKEND", "apikey").strip().lower()


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


def _call_apikey(prompt: str, api_key: str, model: str, timeout_s: int = 300) -> str:
    import json as _json
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
                raise RuntimeError(f"No candidates: {_json.dumps(data)[:800]}")
            parts = (candidates[0].get("content") or {}).get("parts") or []
            if not parts:
                raise RuntimeError(
                    f"Empty parts finish={candidates[0].get('finishReason')} "
                    f"raw={_json.dumps(data)[:1000]}")
            text = "\n".join(p.get("text", "") for p in parts if "text" in p).strip()
            if not text:
                raise RuntimeError(f"Empty text parts: {_json.dumps(data)[:1000]}")
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
