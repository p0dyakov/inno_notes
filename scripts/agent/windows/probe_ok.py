"""Tiny PRO-tier serving probe. Exit 0 + print OK on a real reply."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import Hub

hub = Hub()
out = hub.complete("Reply with exactly: OK", tier="pro", title="inno-watch",
                   timeout_s=420, poll_s=15)
print("OK:", out.strip()[:60])
