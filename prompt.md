You are writing a Quarto study article (`.qmd`) from raw source transcripts. Your output must match the established style of this repository as closely as possible and must be optimized for students who study independently.

## 1. Mission

Create one complete study article from the provided input. The article must:

- cover all topics from the input
- be understandable from zero, without attending the original classes
- explain enough theory for the reader to solve all included practice tasks
- preserve the real source order and source identity
- match the local style of existing articles in the same folder

Treat this as textbook writing, not note-taking.

Write in clear professional English.

## 2. Inputs You Receive

The input will contain:

- the full table of contents at the very top
- transcripts from all relevant source files
- source names such as `Lecture`, `Lab`, `Tutorial`, `Homework`, `Assignment`, `Quiz`, `Test`, `Midterm`, `Final`, `Exercises`

The table of contents is authoritative. Use it as a coverage checklist so that no topic is omitted from the Theory section.

## 3. Mandatory Preflight

Before writing, analyze at least 3 existing `.qmd` articles from the same target folder.

Use articles written in the same language as the target output as the naming reference. For an English article, ignore localized translation files such as `*.ru.qmd` when deriving file naming, title style, week numbering, terminology style, and date conventions. Use localized articles only when the requested output language is the same localization.

From those files, extract and follow:

- title style
- heading depth and numbering style
- author and date conventions
- paragraph density and explanation style
- whether the folder usually includes `Definitions` and `Formulas`
- how examples are titled and ordered
- how source labels are written in parentheses
- how diagrams are placed and styled

Use local folder conventions unless they conflict with the hard rules below. If local files vary, choose the dominant pattern among same-language articles and keep it consistent through the whole new article.

For title naming, infer the `W...` prefix from same-language neighboring articles, but always use a short concise topic title. Prefer one compact noun phrase such as `"W15. Maximum Flow Algorithms"` rather than listing every subtopic in the title. The repository week number may differ from the raw lecture number in the transcript; follow the folder sequence unless the user explicitly says otherwise.

## 4. Hard Output Structure

Keep the structure simple and stable.

### YAML

Use:

```yaml
---
title: "W[X]. [Concise Topic Title]"
author: "[course author]"
date: "[Month D, YYYY]"
format: html
engine: knitr
---
```

Rules:

- the title must use a short concise topic phrase
- topic names in the title must reflect the real content
- do not overstuff the title with all subtopics
- use the correct course author from the repository convention
- do not invent extra YAML fields unless local files in that folder consistently use them

### Section order

Use this order unless the local folder has a stronger established convention:

```md
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**        # only when truly useful, usually for math-heavy articles
#### **4. Practice**        # or Section 3 if Formulas are omitted
```

Do not invent extra top-level sections unless clearly required by the folder style.

## 5. Theory Rules

The Theory section is the most important part.

- It must teach from zero.
- It must cover every topic from the table of contents and all important transcript sections.
- It must be pedagogically ordered, not transcript-dumped.
- It must explain what a concept is, why it matters, how it is used, and what typical pitfalls exist.
- It must define terminology before using it.
- It must correct transcript errors and fill in missing logical links.
- It must include enough explanation so a student can later solve the Tasks section.

Heading rules:

- top-level summary subsections: `##### **1.1 ...**`
- nested subsections: `###### **1.1.1 ...**`
- headings must be concise noun phrases or short descriptive titles, not questions

Style rules:

- write in full paragraphs
- use bullets only when they genuinely improve clarity
- use **bold** for first introduction of key terms
- use *italics* sparingly for emphasis
- use LaTeX for mathematics
- never use backticks for math

## 6. Definitions Rules

The Definitions section is a compact glossary.

- Include every core term introduced in the Theory section.
- Definitions must be self-contained.
- Keep each definition concise, precise, and readable.

Format:

```md
*   **Term**: Definition.
```

## 7. Formulas Rules

Include `Formulas` only when the article is mathematical or formula-heavy enough to justify it.

- Include general reusable formulas, not one-off substitutions from worked examples.
- Include conditions, domains, and restrictions when relevant.
- Do not create a fake formulas section for non-math material.

Format:

```md
*   **Formula Name**: $...$
```

## 8. Practice Items and Tasks

This distinction is mandatory:

- `Example` = something the instructor demonstrates or solves
- `Task` = something students are expected to solve themselves

Model the article around that distinction.

Do not create a separate top-level `Tasks` section. Place both `Example` and `Task` items inside one shared `Practice` section, and order them only by the canonical source-block order.

### Core rule

If the source item is presented as a teacher demonstration, label it as `Example`.
If it is presented as student work, exercise, lab problem, homework problem, tutorial problem, quiz/test problem, or similar, label it as `Task` unless the original source clearly labels it as `Example`.

### What to include

Include all source problems that matter for study:

- all explicit source items labeled `Example`
- all explicit Tasks / Problems / Exercises / Homework items
- all worked demonstrations that should become `Example`
- all student-facing problems that should become `Task`

### Ordering

Use the repository's canonical source-block order. Do not improvise or choose a convenient order.

Rules:

- when multiple source types are present, order blocks in this exact sequence:
  - `Lab`
  - `Homework`
  - `Assignment`
  - `Exercises`
  - `Lecture`
  - `Tutorial`
  - `Chapter`
  - `Recap`
  - `Test`
  - `Midterm`
  - `Final`
- if a source type is absent, skip it; do not invent empty blocks
- inside each source-type block, preserve the original item order from the input
- inside each source file, preserve the original item order
- do not mix items across source-type blocks
- do not move a `Lab` item into a `Lecture` block, or a `Lecture` item into a `Tutorial` block, etc.
- this canonical order overrides arbitrary transcript concatenation order

### Solution policy

- `Example`: include a full worked solution inside `<details>`
- `Task`: include a full worked solution inside `<details>`
- never leave a `Task` as statement-only
- never omit a `Task` solution just because it is student-facing

This is important: the final article must be fully usable for self-study, so both `Example` and `Task` must contain complete pedagogical solutions.

### Example writing standard
- apply the same writing standard to solved `Task` items as well
- solutions must be very detailed, step-by-step, and must not skip algebraic or logical transitions that a student would need to see
- do not give compressed "answer-key style" solutions
- when a computation has multiple stages, structure the explanation so that each stage is explicit and motivated
- when a substitution, theorem, identity, or transformation is used, name it and explain why it is valid

### Example/Task heading format

Use:

```md
##### **4.N. Short Descriptive Title** (Source Block, Item Number)
```

Practice heading examples:

- `(Lecture 6, Example 3)`
- `(Tutorial 4, Task 2)`
- `(Lab 5, Task 7)`
- `(Homework 2, Task 1)`
- `(Chapter 3, Example 12)`
- `(Midterm, Task 4)`

### Example of format
Strictly follow this format exactly
```
##### **4.29. Reversing the Order of Integration** (Chapter 3, Example 9)

Calculate $I = \displaystyle\iint_R \frac{\sin x}{x}\,dA$, where $R$ is the triangle bounded by the $x$-axis, $y = x$, and $x = 1$.

<details>
<summary>Click to see the solution</summary>

**Key Concept:** The integrand $(\sin x)/x$ has no elementary antiderivative with respect to $x$. Switch to integrating $y$ first (vertically simple).

1.  **Describe $R$ as a vertically simple region:** For fixed $x \in [0,1]$, $y$ ranges from $0$ to $x$. So:
    $$I = \int_0^1\int_0^x \frac{\sin x}{x}\,dy\,dx.$$
2.  **Inner integral** (the integrand does not depend on $y$):
    $$\int_0^x \frac{\sin x}{x}\,dy = \frac{\sin x}{x}\cdot x = \sin x.$$
3.  **Outer integral:**
    $$I = \int_0^1 \sin x\,dx = [-\cos x]_0^1 = -\cos 1 + 1 = 1 - \cos 1.$$

**Answer:** $I = 1 - \cos 1$.

</details>
```

## 9. Naming, Numbering, and Metadata Rules

These rules are strict.

### Heading numbering

- numbering must be strictly increasing inside the file
- never duplicate the same heading number
- never restart numbering midway through the file
- use the course-family numbering convention already used in the repository for that subject

### Source metadata

- metadata in parentheses must be complete
- never leave incomplete labels like `(Lab 3, Task)` or `(Chapter 6)`
- never leave bare `(Homework 2)` if the source implies a task number
- never generate `Task 0` unless the source unambiguously requires it
- never generate garbage like `Task Task`, `Example Example`, or duplicate numbering labels

### Title style

Use short, descriptive, action-oriented titles.

Prefer:

- `Find ...`
- `Prove ...`
- `Compute ...`
- `Determine ...`
- `Show ...`
- `Classify ...`
- `Construct ...`
- `Analyze ...`
- `Evaluate ...`
- `Convert ...`

Avoid:

- vague placeholders
- generic labels like `Problem`, `Exercise`, `Practice`
- duplicate internal numbering in the title
- gerund-heavy titles when the file style is imperative
- awkward English such as `"More Than By 2"`

Bad:

- `Practice Differentiation`
- `Prove a Standard Limit`
- `Example: Line Through Two Points`
- `Orthogonal Basis — Task 3`

Good:

- `Differentiate Composite and Rational Functions`
- `Prove a Classical Sequence Limit`
- `Line Through Two Points in Polar Coordinates`
- `Construct an Orthogonal Basis`

### No structural noise

Never output:

- `continued`
- `AI artifacts`
- `⚠️`
- `placeholder`
- `draft`
- `alternative` as metadata noise unless it is genuinely part of the teaching content

## 10. Source Label Priorities

Preserve the real source type.

Use the labels that actually correspond to the source:

- `Lecture`
- `Tutorial`
- `Lab`
- `Homework`
- `Assignment`
- `Quiz`
- `Test`
- `Midterm`
- `Final`
- `Exercises`
- `Chapter`

Do not normalize everything into one label if the source corpus distinguishes them.

But write them consistently:

- `Example` means teacher-demonstrated
- `Task` means student-facing

If the original source label is ambiguous, prefer:

- `Example` for demonstrated material
- `Task` for solve-yourself material

## 11. Diagram and Illustration Rules

Illustrations are required whenever they materially improve understanding or when comparable local articles use them.

### Placement

- place diagrams where they are pedagogically helpful
- also place them where the original material clearly had one
- if you are not rendering the final diagram immediately, insert `<!-- DIAGRAM HERE -->` exactly where it belongs

### Height rule

Every rendered image must have an explicit height to avoid empty vertical space.

Use explicit height attributes, for example:

```md
![](file.png){height=260px}
```

If using embedded diagram blocks, ensure the resulting rendered block has controlled height or compact layout.

Every diagram should also have an explicit width when the default size makes labels, nodes, or relationships hard to read.

If a diagram contains text inside shapes, enlarge it until the text is readable at normal page zoom. Do not keep a diagram artificially small just to save space.

Prefer enlarging pedagogically important diagrams rather than leaving a small figure surrounded by empty whitespace.

### One visual style per article

Choose one article-wide palette and keep it consistent across all figures.

Recommended palette:

- border / line color: `#355c7d`
- primary text color inside diagrams: `#1f2d3d`
- light blue fill: `#e8f4f8`
- secondary blue fill: `#d6eef5`
- positive / accepting fill: `#d7f0c2`
- transitional / active fill: `#fff3cd`
- warning / mismatch / critical fill: `#f9d9e2`
- neutral helper fill: `#eef3f7`
- cluster / container background: `#f9fbfd`

Do not mix random palettes across figures.

Prefer light backgrounds, dark text, and medium-contrast borders.

Avoid dark blue filled nodes, dark gray panels, or any saturated accent fill behind text unless the text remains obviously readable.

Do not use low-contrast combinations such as bright blue text on dark blue or dark gray fills.

If an older or source-derived diagram color scheme conflicts with the course visual system, normalize it to the article palette instead of preserving the original colors.

### Semantic color consistency

Use colors consistently across diagrams:

- neutral structure / ordinary node: `#e8f4f8`
- secondary helper node: `#d6eef5`
- positive / accepting / success state: `#d7f0c2`
- transitional / active / in-progress state: `#fff3cd`
- warning / mismatch / danger / invalid state: `#f9d9e2`
- helper labels or operational markers: `#eef3f7`

Do not assign colors randomly from one diagram to another.

If the article contains automata, stacks, memory models, or process diagrams, keep the same semantic meaning for colors throughout the article.

### Diagram library policy

Use the fewest libraries necessary. Prefer at most 1-2 libraries per article unless the subject genuinely requires more.

Default library choices:

- `matplotlib`: function graphs, geometry plots, calculus plots, coordinate diagrams
- `Graphviz`: automata, trees, strict node-edge graphs, dependency graphs
- `Mermaid`: flowcharts, process diagrams, simple concept graphs
- `PlantUML`: UML, software design, class/sequence/state diagrams
- `ggplot2`: statistical or data-oriented plots only when that is the most natural choice

Preferred mapping by content:

- mathematical graphs and analytic geometry: `matplotlib`
- finite-state automata and formal graph structures: `Graphviz`
- software architecture / UML: `PlantUML`
- process explanations and simple structured flows: `Mermaid`

Avoid unnecessary library switching just because many tools are available.

### Rendering safety

- choose the simplest tool that will render reliably in Quarto
- avoid fragile layout-heavy diagrams if a simpler diagram communicates the same idea
- keep labels readable and compact
- prefer transparent or white backgrounds
- keep diagram text dark and immediately legible
- if a node label is hard to read, change colors or enlarge the figure; do not leave it as-is

## 12. Formatting Rules

- use LaTeX for mathematics: `$...$` and `$$...$$`
- use backticks only for code, file paths, commands, identifiers, and inline literals
- keep heading structure stable
- add blank lines before lists, code blocks, and diagram placeholders
- do not add random decorative separators unless they are already used in local articles
- match the dominant paragraph/list density of the folder you analyzed

## 13. Writing Process

Work incrementally, but the final article must be complete.

- write the file in chunks to reduce tool/write failures
- after finishing the article, run:
  - `python3 fix_formatting.py`
- if headings/examples were inserted, removed, or reordered and numbering must be updated, run:
  - `python3 renumber_examples.py`

Do not use `renumber_examples.py` as a substitute for thinking. First choose the correct local structure, then renumber only if needed.

## 14. Final Validation Checklist

Before finishing, verify all of the following:

1. Every topic from the top-level table of contents appears in the Theory section.
2. The article matches the local style of at least 3 neighboring articles.
3. Source blocks remain in original order.
4. `Example` and `Task` are assigned according to pedagogical role, not randomly.
5. Heading numbering is strictly increasing and contains no duplicates.
6. Metadata labels are complete and consistent.
7. Titles are descriptive, grammatical, and not vague.
8. There is no `continued`, AI noise, placeholder text, or numbering garbage.
9. Diagrams use one consistent palette and explicit height.
10. The theory is sufficient for a new student to solve the Tasks.

## 15. Author Map

Use this only when the folder context does not already make the author obvious.

| Course | Author(s) |
|:-------|:----------|
| Academic Writing and Argumentation I–II | Georgy Gelvanovsky |
| Analytical Geometry and Linear Algebra I–II | Salman Ahmadi-Asl |
| Mathematical Analysis I–II | Mohammad Alkousa |
| Data Structures and Algorithms | Nikolai Kudasov |
| Software Systems Analysis and Design | Eugene Zouev, Munir Makhmutov |
| Theoretical Computer Science | Manuel Mazzara |
| Computer Architecture | Artem Burmyakov |
| Operating Systems | Artem Burmyakov (fallback — verify against Moodle when instructor block appears) |
| Philosophy II (Introduction to AI) | Manuel Mazzara (fallback — verify against Moodle when instructor block appears) |
| Differential Equations | Anna Maslovskaya (Moodle F26 + transcript) |
| Introduction to Optimization | Mohammad Reza Bahrami (Moodle F26 Prime Instructor) |
| Physics I (Mechanics) | Artem Burmyakov (fallback — verify against Moodle when instructor block appears) |
| Probability and Statistics | Ramil Nasibullin (Moodle F26 Prime Instructor) |

Semester-4 teachers are resolved from `semester-4/course_map.json` first (Moodle fetch),
then the transcript first page (`Instructor:` / bold name header), and only then this table.
| Introduction to Programming | Eugene Zouev, Munir Makhmutov |
| Logic and Discrete Math | Andrey Frolov |

## 16. Non-Negotiable Principle

Do not generate a generic article template. Generate one article that looks like it belongs in this exact folder, written by the same invisible editor, with the same structure, naming discipline, and source ordering as the neighboring files. Read at least 3 neighboring `.qmd` files from the same folder and infer the dominant local style.
