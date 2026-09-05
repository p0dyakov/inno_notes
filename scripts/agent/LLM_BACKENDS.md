# LLM backends for agent scripts (`generate.py`, `repair_deploy.py`)

`LLM_BACKEND` env selects the provider (default `apikey`, so CI is unchanged):

- `apikey` — Google AI Studio key pool from `GEMINI_API_KEY` /
  `GEMINI_API_KEY_2` / `GEMINI_API_KEY_3` / `GEMINI_API_KEYS` / `GOOGLE_API_KEY`
  (plus `gemini_api_keys` / `gemini_api_key` from the `inno_files` config),
  direct `generativelanguage` calls. Used in CI (`.github/workflows/agent.yml`).
  Round-robin with 60 s cooldown per key on HTTP 429. Keys MUST live in
  DIFFERENT Cloud projects — limits are enforced per project, not per key,
  so extra keys inside one project share a single quota.
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

## US-egress masking via hostkey (Sep 2026, working path)

Situation: direct/RU egress gets `400 User location is not supported` (fast),
Sota VPN data path is stalled, xbox-dns relay keeps RU IPs (same 400).
What works: a personal LS whose HTTPS egress rides a US exit:

- `scripts/agent/us_egress/inno_connect_proxy.py` — stdlib-only HTTP CONNECT
  proxy (single-threaded, selectors). Runs on the hostkey US box as systemd
  unit `inno-connect-proxy` (localhost-only `127.0.0.1:18081`, allow-listed to
  TCP/443 of Google API hosts, IPv4-first resolve). Deploy:
  copy file to `/opt/inno-connect-proxy.py`, install the unit from the
  docstring header, `systemctl enable --now inno-connect-proxy`.
- Windows reaches it via `ssh -L 18081:127.0.0.1:18081` (task `InnoFwd`,
  `scripts/agent/windows/start_fwd.ps1`; key `~/.ssh/hostkey_us`, hostkey IP
  pinned via `route add 80.209.241.71 … 10.243.1.1` to bypass the dead Sota TUN).
- Probe: `scripts/agent/windows/masked_probe2.py [tier] [timeout_s]`
  (`INNO_PROXY` env overrides the proxy URL) — spawns a personal LS with
  `HTTPS_PROXY` set, traces every poll, keeps the conversation for forensics.
  Runner `run_masked4.ps1` (flash_lite, clean cwd `C:\Users\usful\agywork`).

Observed (Sep 5): via US egress the region gate is GONE (no 400s, quota full)
but serving is starved server-side — streams open (`streamGenerateContent`
gets a ResponseID) then zero tokens for 600s+, all tiers (pro/flash/flash_lite),
two accounts. Transport exonerated (96 MB/s bulk, byte-exact relay).
`spawn_ls` needs no running app anymore (host_bridge copy is best-effort).
