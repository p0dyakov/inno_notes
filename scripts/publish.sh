#!/usr/bin/env bash
# Build on a Windows machine and push: CI only publishes the baked _site/.
# 1. quarto render   (needs Quarto + R with knitr/rmarkdown/igraph/magick/pdftools;
#                     on Windows R packages install as binaries in minutes)
# 2. commit _site/ + index.qmd and push -> deploy-site publishes in ~1 min.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 fix_formatting.py
quarto render
test -f _site/index.html
git add -A -f -- _site/ index.qmd _freeze/
git status --short -- _site/ index.qmd _freeze/ | head -n 20
echo "OK: review, commit and push — deploy on Actions takes ~1 min."
