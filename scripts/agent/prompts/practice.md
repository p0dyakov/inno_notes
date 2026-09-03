# Practice section prompt (STRICT layout — enforced exactly)

Write the Practice section (#### **4. Practice**, or 3 if Formulas was omitted).

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
