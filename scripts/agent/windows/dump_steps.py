import sqlite3,sys,re,io
out = io.open("C:/Users/usful/Desktop/Projects/inno_notes/scripts/agent/windows/steps.txt","w",encoding="utf-8")
db = sqlite3.connect(sys.argv[1])
for (i, b) in db.execute("SELECT idx, step_payload FROM steps ORDER BY idx"):
    t = re.sub(r"\s+", " ", bytes(b).decode("utf-8", errors="ignore"))
    out.write(f"--- step {i} ({len(bytes(b))}B): {t[:500]}\n")
out.close(); print("wrote", db.execute("SELECT COUNT(*) FROM steps").fetchone()[0], "steps")
