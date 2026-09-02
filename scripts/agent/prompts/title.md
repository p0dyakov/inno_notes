# Lecture title rules (HARD — enforced by post-validation)

Format: `W<N>. <Short Topic>` where `<N>` is the week-folder number in
`inno_notes` (`1.qmd` → `W1`), NOT the lecture number from the transcript.

- `<Short Topic>` is ONE compact noun phrase naming what the lecture is about.
- Ranges `W1-W5.` / `W9-W11.` ONLY when one file covers several weeks
  (e.g. Mathematical Analysis summary notes). Normal case: single `WN.`.
- NEVER append `— Lecture N`, NEVER duplicate the course name in the title.
- NEVER use the inno_files short code (`OS`, `DE`, `Phy I`) in the title.

GOOD:
- `W1. Introduction to Operating Systems`
- `W15. Maximum Flow Algorithms`
- `W7. Search Tree Maps`
- `W1. C++: Language Basics`
- `W1. Computation Models`
- `W1-W5. Single-Variable Calculus Review`

BAD (will be rejected by validation):
- `W1. DE — Lecture 1` (course code + Lecture suffix)
- `W1. OS — Lecture 1` (course code + Lecture suffix)
- `W3. Introduction to Optimization — Lecture 3` (Lecture suffix)
- `W2. Probability and Statistics: Lecture 2 Notes` (course name + Lecture)
- `L1. Processes` (wrong prefix, must be `W`)
