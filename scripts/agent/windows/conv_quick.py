# One fast conversation on the held LS. Usage: conv_quick.py [tier=flash_lite] [wait_s=12]
import json, sqlite3, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import Hub
tier = sys.argv[1] if len(sys.argv) > 1 else "flash_lite"
wait_s = int(sys.argv[2]) if len(sys.argv) > 2 else 12
info = json.loads(Path(__file__).parent.joinpath("holder.json").read_text())
hub = Hub(ls_address=info["address"], csrf=info["csrf"])
hub.ensure_project()
cid = hub.new_conversation("Reply with exactly: OK", tier, "quick")
print("conv:", cid[:8], "tier:", tier, flush=True)
start = time.time()
while time.time() - start < wait_s:
    state, detail = hub.classify_db(cid)
    print(f"t={int(time.time()-start)}s {state} {detail}", flush=True)
    if state != "running":
        break
    try:
        md = hub.markdown(cid)
        if "### Planner Response" in md:
            print("QUICK_OK:", hub.last_reply(md)[:80], flush=True)
            break
    except Exception as e:
        print("md-wait:", str(e)[:60], flush=True)
    time.sleep(4)
else:
    print("QUICK_TIMEOUT", flush=True)
