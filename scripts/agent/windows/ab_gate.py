# A/B gate: two held LSs (tunnel-direct vs hostkey-proxy), flash_lite 75s each.
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import httpx
from llm_antigravity import Hub, SERVICE, CSRF_HEADER
CANDS = [
    ("TUN-direct", "http://127.0.0.1:57918", "http://127.0.0.1:57919",
     "9a9f0db1b30064cc82debd8534de7351"),
    ("PROXY-old", "http://127.0.0.1:63396", "http://127.0.0.1:63397",
     "6ce83f1f3f3aca77acf08e321859b7ed"),
]
for label, a1, a2, csrf in CANDS:
    addr = None
    for a in (a1, a2):
        try:
            r = httpx.post(a + f"/{SERVICE}/GetConversationMetadata",
                           headers={"Content-Type": "application/json", CSRF_HEADER: csrf},
                           json={"conversation_id": "00000000-0000-0000-0000-000000000000"},
                           timeout=5)
            if "trajectory not found" in r.text:
                addr = a
                break
        except Exception:
            continue
    print(f"{label}: addr={addr}", flush=True)
    if not addr:
        continue
    try:
        hub = Hub(ls_address=addr, csrf=csrf)
        hub.ensure_project()
        cid = hub.new_conversation("Reply with exactly: OK", "flash_lite", "ab-gate")
        print(f"{label}: conv {cid[:8]}", flush=True)
        start = time.time()
        while time.time() - start < 75:
            state, detail = hub.classify_db(cid)
            print(f"{label}: t={int(time.time()-start)}s {state} {detail}", flush=True)
            if state != "running":
                break
            try:
                md = hub.markdown(cid)
                if "### Planner Response" in md:
                    print(f"{label}: AB_OK:", hub.last_reply(md)[:80], flush=True)
                    break
            except Exception as e:
                print(f"{label}: md-wait:", str(e)[:60], flush=True)
            time.sleep(5)
        else:
            print(f"{label}: AB_TIMEOUT", flush=True)
    except Exception as e:
        print(f"{label}: AB_FAIL:", str(e)[:150], flush=True)
print("AB_DONE", flush=True)
