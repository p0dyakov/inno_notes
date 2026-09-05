import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import Hub
hub = Hub(ls_address="http://127.0.0.1:57919", csrf="9a9f0db1b30064cc82debd8534de7351")
hub.ensure_project()
try:
    cid = hub.new_conversation("Reply with exactly: OK", "flash_lite", "tun-retry")
    print("conv:", cid[:8], flush=True)
except Exception as e:
    print("RETRY_FAIL:", str(e)[:200], flush=True)
    raise SystemExit
start = time.time()
while time.time() - start < 40:
    state, detail = hub.classify_db(cid)
    print(f"t={int(time.time()-start)}s {state} {detail}", flush=True)
    if state != "running":
        break
    try:
        md = hub.markdown(cid)
        if "### Planner Response" in md:
            print("TUN_OK:", hub.last_reply(md)[:80], flush=True)
            break
    except Exception as e:
        print("md-wait:", str(e)[:60], flush=True)
    time.sleep(5)
else:
    print("TUN_TIMEOUT", flush=True)
