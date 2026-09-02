#!/usr/bin/env bash
# Manual alternative to CI: render locally and push the baked _site/.
# Normally NOT needed — deploy-site builds on Windows runners automatically
# after every push to main. Use this for local preview or emergencies.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 fix_formatting.py
quarto render
test -f _site/index.html
git add -A -f -- _site/ index.qmd _freeze/
git status --short -- _site/ index.qmd _freeze/ | head -n 20
echo "OK: review, commit and push."
