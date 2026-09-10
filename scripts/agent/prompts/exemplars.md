# Canonical formatting exemplars — copy these shapes EXACTLY

Theory subsections use NO dot after the number. Practice items use a dot
after BOTH numbers, a NUMBERED source in parentheses, the statement visible,
and the solution inside details.

##### **1.2 Models and Their Assumptions**

Body text here. New terms in **bold** on first definition.

###### **1.2.1 When a Model Is Good Enough**

Nested body text here.

##### **4.1. Falling Object Solution Check** (Lecture 1, Task 1)

Verify by substitution that the function v(t) = 5 + C exp(-2t) solves
m dv/dt = mg - kv for the given constants.

<details>
<summary>Click to see the solution</summary>

**Key Concept:** Direct substitution proves a candidate solution.

1.  **Differentiate the candidate.**
    *   dv/dt = -2C exp(-2t).
    *   **Answer: dv/dt found.**
2.  **Substitute into both sides.**
    *   LHS equals RHS after simplification.
    *   **Answer: both sides match.**

**Answer:** The function satisfies the equation, so it is a solution.
</details>

##### **4.2. Tossing a Fair Coin** (Tutorial 2, Example 3)

A fair coin is tossed twice. List the sample space.

<details>
<summary>Click to see the solution</summary>

**Key Concept:** The sample space lists every possible outcome.

**Answer:** HH, HT, TH, TT.
</details>

### Diagrams: mermaid (flows, pipelines, relations)

Copy this shape exactly for flowcharts and process diagrams:

```{mermaid}
%%| fig-width: 6
flowchart LR
    A["First step"] --> B{"Decision"}
    B -->|Yes| C["Result one"]
    B -->|No| D["Result two"]
```

Rules: node text always in double quotes; one idea per node; keep the
%%| fig-width first line so labels stay readable; never leave a node
empty; never draw a diagram as plain quoted words.

### Diagrams: tikz (plots, geometry, coordinate drawings)

Copy this shape exactly for plots and coordinate geometry:

```{tikz}
%| fig-width: 5
%| out-width: 100%
\begin{tikzpicture}[scale=0.9, every node/.style={font=\small}]
  \draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};
  \draw[thick] (0,0) -- (4,3) node[midway, above] {label};
\end{tikzpicture}
```

Rules: axes always drawn with arrows and labels placed OUTSIDE the tips
(node[right], node[above]); every plotted element gets a label in
whitespace (midway, above right); labels never overlap lines or each
other; keep scale at most 1 so the figure fits the column.

