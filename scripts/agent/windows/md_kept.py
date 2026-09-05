import sys; sys.path.insert(0, "C:/Users/usful/Desktop/Projects/inno_notes/scripts/agent")
from llm_antigravity import Hub
hub = Hub()
md = hub.markdown("6d9fd817-5ab5-4fc4-aec8-a7f6aeb0df4d")
print("MDLEN:", len(md))
print(md[:600])
