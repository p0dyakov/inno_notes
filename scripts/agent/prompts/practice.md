# Practice section prompt (STRICT layout — enforced exactly)

> Only write this section from EXPLICIT numbered tasks/examples stated in the
> transcript. If the source names no explicit tasks, output nothing at all —
> never invent synthetic tasks. (The pipeline omits Practice automatically.)

You are given a TASK MAP (JSON list produced from the same transcript).
Write Practice items for EVERY map entry, in map order, nothing added, nothing
dropped. Each entry's statement is authoritative — solve exactly what it states.
(The transcript is attached for solution details; the map defines the item set.)

Write the Practice section. Its number is SEQUENTIAL among the sections actually
present in THIS article: `4.` if Theory + Definitions + Formulas are all present,
`3.` if one of them was omitted, `2.` if two were omitted. Task headings use the
same number (`##### **3.1. ...**` when Practice is section 3). When in doubt,
count the sections you actually wrote, starting from 1.

Task block layout (no deviations):

```md
##### **N.M. Title** (Source, Task/Example)

<Problem statement as given — 1-3 sentences, ALWAYS visible, NEVER inside details.>

<details>
<summary>Click to see the solution</summary>

**Key Concept:** <one sentence naming the idea that unlocks the task.>

1.  **Step in bold, phrased as an action or question.**
    *   Working, formula, or short derivation.
    *   **Answer: ...** — mini-result of this step where it makes sense.
2.  ...

**Answer:** <final boxed result restated in one line.>
</details>
```

Rules:
- `<Title>` is a short noun phrase; it must NOT contain source words
  (Lecture, Chapter, Lab, Slide, Tutorial).
- Task headings in canonical source order:
  Lab → Homework → Assignment → Exercises → Lecture → Tutorial →
  Chapter → Recap → Test → Midterm → Final.
- The problem statement is OUTSIDE `<details>` so readers see what is
  asked before opening the solution.
- Inside `<details>` are ONLY solution steps — never restate the full
  problem, never add new theory.
- Every solution ends with a bold `**Answer:**` line.
- Solutions are very detailed, step-by-step, no skipped algebra.
- `<summary>` text is exactly `Click to see the solution`.
