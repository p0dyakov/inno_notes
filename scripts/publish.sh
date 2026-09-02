#!/usr/bin/env bash
# Local build + push: renders the full site (needs Quarto + R/knitr locally)
# and commits the baked _site/. GitHub Actions then only publishes _site/.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 fix_formatting.py
quarto render
test -f _site/index.html
git add -A -- _site/ index.qmd
git status --short -- _site/ index.qmd | head -n 20
echo "OK: review, commit and push — deploy on Actions takes ~1 min."
