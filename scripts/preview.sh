#!/usr/bin/env bash
# Preview with the full site pre-rendered (no per-click "Render" waits).
# Quarto preview alone only warms a subset of pages; navigation otherwise
# re-renders each .qmd on demand (10–15s + Render overlay).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ ! -d node_modules/mathjax-full ]]; then
	echo "[preview] npm install (mathjax bake)…" >&2
	npm install --no-fund --no-audit
fi
exec quarto preview --render all "$@"
