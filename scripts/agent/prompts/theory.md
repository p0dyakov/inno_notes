# Theory section prompt (STRICT — depth is mandatory)

Write the Theory section (#### **1. Theory** plus #####/###### subsections).
This is the most important part of the article. Textbook writing, not notes.

## Coverage (hard contract — omitting a topic is a failure)
- The transcript's table of contents / outline slide is a CHECKLIST:
  every listed topic MUST become a `##### 1.x` subsection (group only
  trivially related micro-topics, never drop).
- Survey and catalog material is examinable content, not background:
  history generations (dates, inventors, machines), OS/device zoos,
  hardware parts, classification dimensions — each gets a structured
  subsection with concrete facts (names, dates, numbers, examples),
  never a one-line mention or silent skip.
- Include enough theory to solve every Practice task of the article.
- Correct transcript errors and fill in missing logical links.

## Teaching pattern (one per concept, scaled to its weight)
- DEFINITION first: bold the term, state it formally (with math where
  applicable) BEFORE first use.
- WHY it matters: one or two sentences of motivation or intuition.
- WORKED mini-example: a tiny concrete case with real numbers/names
  (coin tosses, a 2x2 system, ENIAC specs) — the way old articles do
  ("Example (coin tossing): ...", short proofs inline). No water:
  every sentence must teach; generic filler is forbidden.
- PITFALLS: the typical confusion or mistake for this concept.

## Depth (hard requirements)
- Depth follows the INPUT, not a word quota: a small lecture yields a
  compact article, a dense one yields a long article. There is no minimum
  length — but there is a completeness bar (see Coverage): every input
  topic must be explained, never merely mentioned.
- Default to full explanatory paragraphs with textbook density. Thin
  bullet dumps are FORBIDDEN. Bullets only when they genuinely improve
  clarity (lists of properties, steps of an algorithm, cases).
- For every concept explain: WHAT it is, WHY it matters, HOW it is used,
  and what typical PITFALLS look like — scaled to the concept's weight
  in the input, not padded beyond it.
- Define terminology BEFORE first use. Name every theorem, substitution,
  identity or transformation you apply and explain why it is valid.
- Never compress ("answer-key style"), never skip logical transitions,
  never pad with generic filler.

## Order and fidelity
- Follow the SOURCE's order (slides / chapter flow), not a reshuffled
  "textbook-canonical" order — the lecture's framing is examinable.
- Every date, name, number and spec comes from the transcript. NEVER
  invent plausible-looking facts (ENIAC specs, cache sizes, coefficients).
- When the source gives two framings of one idea (extended machine AND
  resource manager; time AND space multiplexing), teach BOTH plus the
  contrast — collapsing them into one loses exam points.
- Bridge subsections with one logical sentence ("Raw speed comes from
  overlap"); no abrupt jumps between `#####` blocks.

## Form
- Top-level subsections: `##### **1.1 ...**`; nested: `###### **1.1.1 ...**`.
- Headings are concise noun phrases, never questions.
- **Bold** the first introduction of each key term; *italics* sparingly.
- Math in LaTeX (`$...$` / `$$...$$`), never backticks for math.
- NEVER use horizontal dividers (`---`, `***`, `___`, `<hr>`) inside
  Theory. Subsections are separated by headings alone. Dividers are
  reserved exclusively for boundaries BETWEEN top-level `####` sections.
- After each concept, an inline `* **Why it matters:**` / `* **Key Pitfall:**`
  / `* **Worked check:**` bullet where it genuinely teaches.
- Match the paragraph density and heading style of the neighboring
  articles in the style context.
