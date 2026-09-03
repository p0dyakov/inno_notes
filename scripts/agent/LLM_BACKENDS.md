# LLM backends for agent scripts (`generate.py`, `repair_deploy.py`)

`LLM_BACKEND` env selects the provider (default `apikey`, so CI is unchanged):

- `apikey` — Google AI Studio key from `GEMINI_API_KEY`/`GOOGLE_API_KEY`,
  direct `generativelanguage` calls. Used in CI (`.github/workflows/agent.yml`).
- `antigravity` — local Antigravity hub on the machine running the script
  (logged-in account, Google AI Pro subscription quota, **no key, no billing**).
  Conversations are created per call and deleted afterwards.

## Using `antigravity` on this Mac

Requirements: `Antigravity.app` running and logged in; egress to Google
(Sota VPN is the default route — nothing to configure in code).

```sh
LLM_BACKEND=antigravity python3 scripts/agent/generate.py \
  --regen-theory "semester-4/Operating Systems/1.qmd" --tries 3
```

Tiers: Theory always uses `pro`; other sections `flash`/`flash_lite`
(mapped from model names in `llm.py:_tier_for`).

Health check (no quota spent):

```sh
python3 scripts/agent/llm_antigravity.py   # hub discovery + quota buckets
```

## Replicating on Windows (your PC, not CI)

CI runners cannot do the interactive Antigravity login, so generation stays
local — run it on the Windows PC instead:

1. Install Antigravity for Windows, log in with the same Google account.
2. Ensure egress to Google (run Sota there, same as on the Mac).
3. Install Python 3.11+ and `pip install httpx`; clone the repo
   (inno_notes + inno_files side by side, or pass `--inno-files`).
4. Discover + generate with the same commands:
   ```powershell
   $env:LLM_BACKEND = "antigravity"
   python scripts/agent/llm_antigravity.py
   python scripts/agent/generate.py --regen-theory "semester-4/Operating Systems/1.qmd"
   ```
   Discovery on Windows uses `tasklist` (hub process + csrf), `netstat`
   (Connect-API port) and `%APPDATA%/Antigravity/app_storage.json`
   (project id) — same logic as on macOS (`_localhost_ports`,
   `_hub_cmdline`, `_project_id` in `llm_antigravity.py`).

## Serving reality (September 2026)

The subscription pool is full (weekly ~99.9%), but Google serving currently
refuses many calls: `503 No capacity` (flash_lite, transient) and
`400 User location is not supported` (flash/pro direct-API routing).
The module classifies them (`TransientError` → retried with backoff,
`FatalError` → fail fast) — just re-run later; nothing is committed on
failure (`process_week` restores/deletes drafts).
