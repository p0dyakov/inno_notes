# Theory map prompt (JSON contract — no prose)

Read the FULL transcript below and plan the Theory section as an ordered list
of topics that teaches the material FROM SCRATCH: a reader who skipped the
lecture must learn everything by reading the article.

Rules:
- Cover EVERY theory topic in the sources: definitions, theorems, methods,
  derivations, classifications, survey/catalog material (generations, species,
  zoos — each becomes its own topic, never a one-line mention), worked
  illustrations that carry theory.
- EXCLUDE non-teaching matter: contacts, team, grading, procedures, deadlines,
  academic-integrity boilerplate, memes without content, "next week" teasers
  (one closing topic may point forward if the source does).
- Order for learning: foundations first, then builds. Split generously — one
  focused topic per part is better than one giant part (aim 6-14 topics for a
  full lecture, fewer for thin material). No overlaps: state each part's
  boundaries so parallel writers never duplicate.
- You may reframe for clarity (better order, grouped micro-topics), but NEVER
  drop a topic and never invent one the sources lack.

Output ONLY a JSON array (no fences, no commentary), each:
{"n": <1-based>, "title": "<short topic title>",
 "scope": "<what this part must teach, 2-4 sentences: concepts, facts, numbers, boundaries>",
 "key_points": ["<fact/formula/step the part must contain>", ...]}
