#!/usr/bin/env bash
# Local incremental build (same result as CI, but only changed files):
# re-renders ONLY changed files (seconds),
# fast-patches _includes into built HTML, then stages everything.
# Full `quarto render` runs only when _quarto.yml itself changed.
# CI just publishes the committed _site/ (~1 min).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/render_changed.py "$@"
git add -A -f -- _site/ index.qmd _freeze/
git status --short -- _site/ index.qmd _freeze/ | head -n 20
echo "OK: review, commit and push — deploy on Actions takes ~1 min."
