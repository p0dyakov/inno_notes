import sqlite3,sys,re,io
out = io.open("C:/Users/usful/Desktop/Projects/inno_notes/scripts/agent/windows/steps3.txt","w",encoding="utf-8")
db = sqlite3.connect(sys.argv[1])
for (i, b) in db.execute("SELECT idx, step_payload FROM steps ORDER BY idx"):
    t = bytes(b).decode("utf-8", errors="ignore")
    printable = re.sub(r"[^\x20-\x7e\n]", "|", t)
    printable = re.sub(r"\|+", "|", printable)
    out.write(f"=== step {i} ({len(bytes(b))}B):\n{printable}\n")
out.close(); print("ok")
