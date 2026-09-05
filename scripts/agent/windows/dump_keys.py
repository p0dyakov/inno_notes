import sqlite3,sys,re,io
out = io.open("C:/Users/usful/Desktop/Projects/inno_notes/scripts/agent/windows/steps2.txt","w",encoding="utf-8")
db = sqlite3.connect(sys.argv[1])
for (i, b) in db.execute("SELECT idx, step_payload FROM steps ORDER BY idx"):
    t = bytes(b).decode("utf-8", errors="ignore")
    toks = sorted(set(re.findall(r"[A-Za-z][A-Za-z0-9_.-]{3,60}", t)))
    interesting = [x for x in toks if any(k in x.lower() for k in ("gemini","model","flash","pro","tier","capacity","region","location","error","fail","quota"))]
    out.write(f"--- step {i} ({len(bytes(b))}B) keywords: {interesting[:40]}\n")
out.close(); print("ok")
