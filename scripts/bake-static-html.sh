#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ ! -d node_modules/mathjax-full ]]; then
	echo "[bake-static-html] installing mathjax-full (one-time)…" >&2
	npm install --no-fund --no-audit
fi
exec node scripts/bake-static-html.mjs
