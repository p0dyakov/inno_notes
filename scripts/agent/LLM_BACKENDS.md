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
local — run it on the Windows PC instead. The one-shot
`scripts/agent/windows/setup.ps1` checks everything below (run plain for
status, `powershell -ExecutionPolicy Bypass -File ... -Apply` elevated to
apply: Yandex DoH policy + proxy exclusions; also enables Tailscale SSH so
this machine becomes remotely manageable):

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

## Proxy wrapper (`xproxy.py` + spawned LS)

Google API entry points that are DNS-gated resolve differently through
`https://xbox-dns.ru/dns-query` (DoH) than through system DNS — notably
`generativelanguage.googleapis.com` (xbox returns relay IPs, system returns
the gated edge). `scripts/agent/xproxy.py` is a local CONNECT forwarder:

- Google API hosts are dialed via the xbox-DNS answers (SNI preserved);
- everything else goes direct;
- per-connection logging (`CONN host:port via ip`) shows exactly which egress
  each upstream call used.

Run it, then spawn a personal hub LS whose own Google egress rides the proxy:

```sh
python3 scripts/agent/xproxy.py  # logs to stdout; 127.0.0.1:18081
python3 - <<'EOF'
import sys; sys.path.insert(0, 'scripts/agent')
from llm_antigravity import spawn_ls
print(spawn_ls(proxy='http://127.0.0.1:18081'))
EOF
# -> {"pid": ..., "address": "http://127.0.0.1:PORT", "csrf": "..."}
AGY_LS_ADDRESS=http://127.0.0.1:PORT AGY_CSRF_TOKEN=... \
  LLM_BACKEND=antigravity python3 scripts/agent/generate.py --regen-theory ...
```

`spawn_ls` copies the running hub's `--host_bridge_*` flags so project
mapping keeps working, shares `~/.gemini` auth state, and waits until the
Connect API answers. Kill stray instances with `kill <pid>` when done.
