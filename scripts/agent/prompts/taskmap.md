# Task map prompt (JSON contract — no prose)

Read the FULL transcript below and list EVERY explicit task/example it states:
numbered items ("Task 3", "Problem 7", "Example 2", "Exercise 1") AND unnumbered
item headings ("### Example", "## Task"). Topic titles ("Jobs Are Collections
of Tasks") and prose turns ("for example, ...") are NOT items.

Output ONLY a JSON array (no fences, no commentary). One object per item, in
canonical source order (Lab → Homework → Assignment → Exercises → Lecture →
Tutorial → Chapter → Recap → Test → Midterm → Final), each:
{"n": <1-based position in THIS list>, "kind": "Task" or "Example",
 "title": "<short noun phrase, no source words>",
 "source": "<Lecture|Tutorial|Lab|... plus number, e.g. 'Lecture 1'>",
 "statement": "<the task as stated, 1-3 sentences, faithful to source>"}

If the transcript states ZERO items, output exactly: []
