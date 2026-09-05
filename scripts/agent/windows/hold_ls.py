import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_antigravity import spawn_ls
import os
info = spawn_ls(proxy=os.environ.get("INNO_PROXY", "http://127.0.0.1:18081"))
Path(__file__).parent.joinpath("holder.json").write_text(json.dumps(info))
print("HELD:", info["pid"], info["address"], flush=True)
