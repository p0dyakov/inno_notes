# Theory part prompt (ONE map topic — depth is mandatory)

Write ONE Theory subsection for the map topic given below (its number and
title are fixed — use them exactly as the `#####` heading).

Heading format (exact, note: NO dot after the number):
`##### **2.4 Topic Title Here**`

Goal: a reader who skipped the lecture learns this topic fully from your text.
Textbook writing, not notes.

## Grounding (hard)

- Every fact, number, name, and example must come from YOUR TOPIC scope or the
  transcript. Never add topics the sources lack.
- Clarifications of source facts are allowed; new content is not. In
  particular, FORBIDDEN unless the transcript itself teaches them:
  biographies and history anecdotes, philosophy-of-modeling essays,
  numerical methods / heuristics / convergence theory (belongs to later
  weeks), second worked examples demonstrating the same computation,
  parallel real-world catalogs (safety systems, war stories, product lists).
- PITFALLS are BANNED entirely: no Pitfalls/Common Pitfalls/Key Pitfalls
  subsections and no Key/Common Pitfall bullets anywhere. Teach the correct
  use inline; never add a dedicated pitfalls block.
- WHY-motivation is at most 1-2 sentences and only when it explains USE.
  No "Why it matters" philosophy paragraphs.
- State each fact ONCE. Never write definition-then-restatement-then-summary
  triples; never compute the same number twice (a check line may reuse it,
  not re-derive it); never narrate trivial algebra step by step
  ("substituting back", "exponentiating both sides yields" as separate steps).

## Teaching pattern (scaled to the topic's weight)

- DEFINITION first: bold each term, state it formally (math where applicable).
- ONE tiny worked illustration with real numbers/names IF the source has one
  or it demonstrates the method. One is enough.
- Stay inside scope: sibling topics (listed below) cover the rest — do not
  duplicate them, do not drift into them.

## Diagrams (mandatory shape)

NEVER draw ASCII/box-drawing diagrams (no ┌ │ ▼ ─ +-| trees). They render as
monospace garbage. Use exactly one of:

Mermaid flowchart (concept maps, taxonomies, process flows) — copy verbatim:
```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'Helvetica', 'primaryColor': '#e8f4f8', 'primaryTextColor': '#1f2d3d', 'primaryBorderColor': '#355c7d', 'lineColor': '#355c7d', 'secondaryColor': '#d6eef5', 'tertiaryColor': '#fff3cd', 'background': '#ffffff', 'mainBkg': '#e8f4f8', 'secondBkg': '#d6eef5', 'tertiaryBkg': '#fff3cd', 'clusterBkg': '#f9fbfd', 'clusterBorder': '#355c7d', 'edgeLabelBackground': '#ffffff' }}}%%
%%| fig-cap: "One-sentence caption"
%%| fig-width: 7
%%| fig-height: 4
flowchart TB
    A["First line<br/>second line"]
    B["Single"]
    A --> B
```
Rules: double-quoted labels; `<br/>` for line breaks (both lines always
render); short labels (under ~6 words per line); palette fills #e8f4f8
default, #d6eef5 secondary, #d7f0c2 success, #fff3cd active, #f9d9e2 danger.

Tikz (function graphs, coordinate plots ONLY) — copy verbatim:
```{tikz}
#| label: fig-short-name
#| fig-cap: "One-sentence caption"
#| echo: false
#| lang: tex
#| fig-height: 4
\begin{tikzpicture}[xscale=0.36, yscale=0.028]
    \draw[->] (0,0) -- (27,0) node[right] {$t$};
    \draw[->] (0,0) -- (0,215) node[above] {$N(t)$};
    \draw[blue, thick] plot coordinates {(0,20) (5,50) (10,79) (15,93) (20,99)};
\end{tikzpicture}
```
Rules: pure-tikz only (no pgfplots); short curve labels placed in EMPTY plot
regions, never on curves/axes/gridlines; verify no two labels overlap.

## Equations and formatting

- Number a display equation with `\tag{N}` ONLY if later text references
  `(N)`; tags must be unique in the file (a checker renumbers, but do it
  right the first time).
- Blank line before every list and every fenced block (a formatter enforces
  this; missing blanks render lists as run-on paragraphs).
- LaTeX for math, never backticks; full paragraphs, bullets only for real
  enumerations.
