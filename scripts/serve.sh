#!/usr/bin/env bash
# Fast local review of the already-built static site (dev flow).
# No quarto involved: serves _site/ as-is. Rebuild changed pages first with:
#   python3 scripts/render_changed.py --base main
# Then open the printed URL. Math is pre-baked, navigation is instant.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${1:-4210}"
cd "$ROOT/_site"
echo "[serve] http://localhost:$PORT"
exec python3 -m http.server "$PORT"
