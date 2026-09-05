"""Masked-egress traced probe: keeps conversation, logs every poll state.

Usage: masked_probe2.py [tier=flash] [timeout_s=600]
Chain: spawned LS --(HTTPS_PROXY=http://127.0.0.1:18081)--> ssh -L -->
hostkey CONNECT proxy --> Google (US egress).
"""
import os
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import Hub, TransientError, spawn_ls

PROXY = os.environ.get("INNO_PROXY", "http://127.0.0.1:18081")
tier = sys.argv[1] if len(sys.argv) > 1 else "flash"
timeout_s = int(sys.argv[2]) if len(sys.argv) > 2 else 600

info = spawn_ls(proxy=PROXY)
print("spawned:", info["pid"], info["address"], flush=True)
try:
    hub = Hub(ls_address=info["address"], csrf=info["csrf"])
    hub.ensure_project()
    cid = hub.new_conversation("Reply with exactly: OK", tier, "inno-masked2")
    print("conversation:", cid, "tier:", tier, flush=True)
    print("trajectory db:", hub.trajectory_db(cid), flush=True)
    start = time.time()
    try:
        while time.time() - start < timeout_s:
            state, detail = hub.classify_db(cid)
            print(f"t={int(time.time()-start)}s state={state} detail={detail}", flush=True)
            if state != "running":
                break
            try:
                md = hub.markdown(cid)
                if "### Planner Response" in md:
                    print("MASKED_OK:", hub.last_reply(md)[:120], flush=True)
                    break
            except Exception as e:
                print("markdown not ready:", str(e)[:100], flush=True)
            time.sleep(15)
        else:
            print("POLL_TIMEOUT", flush=True)
    finally:
        try:
            db = sqlite3.connect(str(hub.trajectory_db(cid)))
            rows = db.execute("SELECT idx, substr(step_payload, 1, 200) FROM steps ORDER BY idx").fetchall()
            print(f"steps total: {len(rows)}", flush=True)
            for i, s in rows[-6:]:
                print(f"step {i}: {s}", flush=True)
        except Exception as e:
            print("step dump failed:", str(e)[:150], flush=True)
        print("conversation KEPT:", cid, flush=True)
finally:
    subprocess.run(["taskkill", "/PID", str(info["pid"]), "/F"], capture_output=True)
    print("spawned LS killed", flush=True)
