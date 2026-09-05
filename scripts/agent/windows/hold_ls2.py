import json, os, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import spawn_ls
W = Path(__file__).parent
holder = W / "holder.json"
if holder.exists():
    try:
        old = json.loads(holder.read_text())
        subprocess.run(["taskkill", "/PID", str(old["pid"]), "/F"], capture_output=True)
        print("old LS killed:", old["pid"], flush=True)
    except Exception as e:
        print("old kill skip:", str(e)[:80], flush=True)
proxy = os.environ.get("INNO_PROXY", "")
info = spawn_ls(proxy=proxy) if proxy else spawn_ls()
holder.write_text(json.dumps(info))
print("HELD:", info["pid"], info["address"], "proxy=", proxy or "NONE(direct)", flush=True)
