<!-- Here is the transcription of the files, organized by file and slide/page.

---

# File 1: Advanced Solutions of Linear Systems (Example 1-6)

## Slide 1
**Title:** Example 1. System with Parameter
**Content:**
Determine all values of $k$ for which the system has:
1.  A unique solution
2.  No solution
3.  Infinitely many solutions

**System:**
$$
\begin{cases}
x + 2y + 3z = 1 \\
2x + 4y + 6z = 2 \\
kx + (k + 1)y + (k + 2)z = k
\end{cases}
$$

**Footer:** Mathematics Department | Advanced Solutions of Linear Systems | January 20, 2026 | 2 / 29

## Slide 2
**Title:** Example 1: Solution
**Content:**
**Augmented Matrix:**
$$
\begin{bmatrix}
1 & 2 & 3 & | & 1 \\
2 & 4 & 6 & | & 2 \\
k & k+1 & k+2 & | & k
\end{bmatrix}
$$

**Row Operations:**
$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - kR_1$:
$$
\begin{bmatrix}
1 & 2 & 3 & | & 1 \\
0 & 0 & 0 & | & 0 \\
0 & 1-k & 2-k & | & 0
\end{bmatrix}
$$

## Slide 3
**Title:** Example 1: Case Analysis
**Content:**
**Case 1: $k = 1$**
$$
\begin{bmatrix}
1 & 2 & 3 & | & 1 \\
0 & 0 & 0 & | & 0 \\
0 & 0 & 1 & | & 0
\end{bmatrix}
\xrightarrow{\text{RREF}}
\begin{bmatrix}
1 & 2 & 0 & | & 1 \\
0 & 0 & 1 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$
**Result:** Infinitely many solutions: 2 pivots, 1 free variable.

**Case 2: $k = 2$**
$$
\begin{bmatrix}
1 & 2 & 3 & | & 1 \\
0 & 0 & 0 & | & 0 \\
0 & -1 & 0 & | & 0
\end{bmatrix}
\xrightarrow{\text{RREF}}
\begin{bmatrix}
1 & 0 & 3 & | & 1 \\
0 & 1 & 0 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$
**Result:** Infinitely many solutions: 2 pivots, 1 free variable.

## Slide 4
**Title:** Example 1: Final Analysis
**Content:**
**Case 3: $k \neq 1$ and $k \neq 2$**
$$
\begin{bmatrix}
1 & 2 & 3 & | & 1 \\
0 & 0 & 0 & | & 0 \\
0 & 1-k & 2-k & | & 0
\end{bmatrix}
$$
Swap $R_2$ and $R_3$:
$$
\begin{bmatrix}
1 & 2 & 3 & | & 1 \\
0 & 1-k & 2-k & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$
**Result:** Infinitely many solutions: 2 pivots, 1 free variable.

## Slide 5
**Title:** Summary
**Content:**
*   For all $k$, the system has infinitely many solutions.
*   Rank is always less than 3 (number of variables).
*   Particular solution:
    $$
    \mathbf{x}_p = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \quad (\text{set } y = z = 0)
    $$

## Slide 6
**Title:** Example 2.
**Content:**
**Solve the system:**
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5 = 1 \\
2x_1 + 4x_2 + 6x_3 + 8x_4 + 10x_5 = 2 \\
3x_1 + 6x_2 + 9x_3 + 12x_4 + 15x_5 = 3
\end{cases}
$$

**Augmented Matrix:**
$$
\begin{bmatrix}
1 & 2 & 3 & 4 & 5 & | & 1 \\
2 & 4 & 6 & 8 & 10 & | & 2 \\
3 & 6 & 9 & 12 & 15 & | & 3
\end{bmatrix}
$$

## Slide 7
**Title:** Example 2: RREF and Analysis
**Content:**
**Row Reduction:**
$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:
$$
\begin{bmatrix}
1 & 2 & 3 & 4 & 5 & | & 1 \\
0 & 0 & 0 & 0 & 0 & | & 0 \\
0 & 0 & 0 & 0 & 0 & | & 0
\end{bmatrix}
$$
Already in RREF!

**Equation:**
$x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5 = 1$
*   1 pivot column (column 1)
*   4 free variables: $x_2, x_3, x_4, x_5$

## Slide 8
**Title:** Example 2: Complete Solution
**Content:**
**Particular Solution:**
Set all free variables to 0: $x_2 = x_3 = x_4 = x_5 = 0$
$x_1 = 1 \implies \mathbf{x}_p = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}$

## Slide 9
**Title:** Example 2: General Solutions
**Content:**
**Homogeneous Solution:**
From $x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5 = 0$:
$x_1 = -2x_2 - 3x_3 - 4x_4 - 5x_5$

Let $x_2 = s, x_3 = t, x_4 = u, x_5 = v$:
$$
\mathbf{x}_h = s\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} + t\begin{bmatrix} -3 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix} + u\begin{bmatrix} -4 \\ 0 \\ 0 \\ 1 \\ 0 \end{bmatrix} + v\begin{bmatrix} -5 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
$$

## Slide 10
**Title:** Example 2: Final Solution
**Content:**
**Complete Solution:**
$$
\mathbf{x} = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix} + s\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} + t\begin{bmatrix} -3 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix} + u\begin{bmatrix} -4 \\ 0 \\ 0 \\ 1 \\ 0 \end{bmatrix} + v\begin{bmatrix} -5 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
$$
where $s, t, u, v \in \mathbb{R}$

**Geometric Interpretation:**
*   Solution set is a 4-dimensional affine subspace of $\mathbb{R}^5$
*   Null space dimension = 4 (5 variables - 1 pivot)
*   The homogeneous solutions form a basis for the null space

## Slide 11
**Title:** Example 3.
**Content:**
**Solve the system:**
$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 = 0 \\
x_1 + 2x_2 + 3x_3 + 4x_4 = 1 \\
x_1 + 3x_2 + 6x_3 + 10x_4 = 3 \\
x_1 + 4x_2 + 10x_3 + 20x_4 = 6
\end{cases}
$$

## Slide 12
**Title:** Example 3: Solution Strategy
**Content:**
**Augmented Matrix:**
$$
\begin{bmatrix}
1 & 1 & 1 & 1 & | & 0 \\
1 & 2 & 3 & 4 & | & 1 \\
1 & 3 & 6 & 10 & | & 3 \\
1 & 4 & 10 & 20 & | & 6
\end{bmatrix}
$$

**Row Reduction (Step 1):**
Subtract $R_1$ from each row:
$$
\begin{bmatrix}
1 & 1 & 1 & 1 & | & 0 \\
0 & 1 & 2 & 3 & | & 1 \\
0 & 2 & 5 & 9 & | & 3 \\
0 & 3 & 9 & 19 & | & 6
\end{bmatrix}
$$

## Slide 13
**Title:** Example 3: Continued Reduction
**Content:**
**Step 2:**
$R_3 \leftarrow R_3 - 2R_2$, $R_4 \leftarrow R_4 - 3R_2$:
$$
\begin{bmatrix}
1 & 1 & 1 & 1 & | & 0 \\
0 & 1 & 2 & 3 & | & 1 \\
0 & 0 & 1 & 3 & | & 1 \\
0 & 0 & 3 & 10 & | & 3
\end{bmatrix}
$$

**Step 3:**
$R_4 \leftarrow R_4 - 3R_3$:
$$
\begin{bmatrix}
1 & 1 & 1 & 1 & | & 0 \\
0 & 1 & 2 & 3 & | & 1 \\
0 & 0 & 1 & 3 & | & 1 \\
0 & 0 & 0 & 1 & | & 0
\end{bmatrix}
$$

## Slide 14
**Title:** Example 3: Back Substitution
**Content:**
**From RREF (Backward Substitution):**
From $R_4$: $x_4 = 0$
From $R_3$: $x_3 + 3(0) = 1 \implies x_3 = 1$
From $R_2$: $x_2 + 2(1) + 3(0) = 1 \implies x_2 = -1$
From $R_1$: $x_1 + (-1) + 1 + 0 = 0 \implies x_1 = 0$

**Unique Solution:**
$$
\mathbf{x} = \begin{bmatrix} 0 \\ -1 \\ 1 \\ 0 \end{bmatrix}
$$
*   Rank = 4, null space dimension = 0
*   No free variables
*   This is both the particular solution and the complete solution

## Slide 15
**Title:** Example 4.
**Content:**
**Solve the system:**
Find the complete solution to:
$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
2 & 4 & 6 & 8 \\
3 & 6 & 9 & 12 \\
4 & 8 & 12 & 16
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3 \\ x_4
\end{bmatrix}
=
\begin{bmatrix}
10 \\ 20 \\ 30 \\ 40
\end{bmatrix}
$$
**Note:** Matrix has rank 1

## Slide 16
**Title:** Example 4: Solution
**Content:**
**Augmented Matrix:**
$$
\begin{bmatrix}
1 & 2 & 3 & 4 & | & 10 \\
2 & 4 & 6 & 8 & | & 20 \\
3 & 6 & 9 & 12 & | & 30 \\
4 & 8 & 12 & 16 & | & 40
\end{bmatrix}
$$

**Row Reduction:**
All rows are multiples of row 1:
$$
\xrightarrow{\text{RREF}}
\begin{bmatrix}
1 & 2 & 3 & 4 & | & 10 \\
0 & 0 & 0 & 0 & | & 0 \\
0 & 0 & 0 & 0 & | & 0 \\
0 & 0 & 0 & 0 & | & 0
\end{bmatrix}
$$

## Slide 17
**Title:** Example 4: General Solution
**Content:**
**Equation:**
$x_1 + 2x_2 + 3x_3 + 4x_4 = 10$
*   1 pivot column (column 1)
*   3 free variables: $x_2, x_3, x_4$

**Particular Solution:**
Set $x_2 = x_3 = x_4 = 0 \implies x_1 = 10$
$$
\mathbf{x}_p = \begin{bmatrix} 10 \\ 0 \\ 0 \\ 0 \end{bmatrix}
$$

## Slide 18
**Title:** Example 4: General Solution
**Content:**
**Homogeneous Solution:**
From $x_1 + 2x_2 + 3x_3 + 4x_4 = 0 \implies x_1 = -2x_2 - 3x_3 - 4x_4$
Let $x_2 = a, x_3 = b, x_4 = c$:
$$
\mathbf{x}_h = a\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + b\begin{bmatrix} -3 \\ 0 \\ 1 \\ 0 \end{bmatrix} + c\begin{bmatrix} -4 \\ 0 \\ 0 \\ 1 \end{bmatrix}
$$

## Slide 19
**Title:** Example 4: Complete Solution
**Content:**
**Final Answer:**
$$
\mathbf{x} = \begin{bmatrix} 10 \\ 0 \\ 0 \\ 0 \end{bmatrix} + a\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + b\begin{bmatrix} -3 \\ 0 \\ 1 \\ 0 \end{bmatrix} + c\begin{bmatrix} -4 \\ 0 \\ 0 \\ 1 \end{bmatrix}
$$
where $a, b, c \in \mathbb{R}$

**Geometric Interpretation:**
*   Solution set is a 3-dimensional affine subspace of $\mathbb{R}^4$
*   The vectors form a basis for the null space (dimension 3)
*   All rows of $A$ are linearly dependent

## Slide 20
**Title:** Example 5.
**Content:**
**Solve the underdetermined system (more variables than equations):**
$$
\begin{cases}
x + 2y + 3z + 4w = 5 \\
2x + 4y + 6z + 8w = 10 \\
3x + 5y + 7z + 9w = 12
\end{cases}
$$
*   $m = 3$ equations
*   $n = 4$ variables

## Slide 21
**Title:** Example 5: Solution
**Content:**
**Augmented Matrix:**
$$
\begin{bmatrix}
1 & 2 & 3 & 4 & | & 5 \\
2 & 4 & 6 & 8 & | & 10 \\
3 & 5 & 7 & 9 & | & 12
\end{bmatrix}
$$

## Slide 22
**Title:** Example 5.
**Content:**
**Row Reduction:**
$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:
$$
\begin{bmatrix}
1 & 2 & 3 & 4 & | & 5 \\
0 & 0 & 0 & 0 & | & 0 \\
0 & -1 & -2 & -3 & | & -3
\end{bmatrix}
$$
Swap $R_2$ and $R_3$, multiply $R_2$ by -1:
$$
\begin{bmatrix}
1 & 2 & 3 & 4 & | & 5 \\
0 & 1 & 2 & 3 & | & 3 \\
0 & 0 & 0 & 0 & | & 0
\end{bmatrix}
$$

## Slide 23
**Title:** Example 5: RREF and Equations
**Content:**
**Reduced Row Echelon Form:**
$R_1 \leftarrow R_1 - 2R_2$:
$$
\begin{bmatrix}
1 & 0 & -1 & -2 & | & -1 \\
0 & 1 & 2 & 3 & | & 3 \\
0 & 0 & 0 & 0 & | & 0
\end{bmatrix}
$$

**Equations:**
$$
\begin{cases}
x - z - 2w = -1 \\
y + 2z + 3w = 3
\end{cases}
$$
*   Pivot columns: 1 and 2 (variables $x$ and $y$)
*   Free variables: $z$ and $w$

## Slide 24
**Title:** Example 5: Complete Solution
**Content:**
**Particular Solution:**
Set free variables $z = w = 0$:
$x = -1, \quad y = 3$
$$
\mathbf{x}_p = \begin{bmatrix} -1 \\ 3 \\ 0 \\ 0 \end{bmatrix}
$$

## Slide 25
**Title:** Example 5: General Solution
**Content:**
**Homogeneous Solution:**
From $x - z - 2w = 0$ and $y + 2z + 3w = 0$:
$x = z + 2w, \quad y = -2z - 3w$

Let $z = s, w = t$:
$$
\mathbf{x}_h = s\begin{bmatrix} 1 \\ -2 \\ 1 \\ 0 \end{bmatrix} + t\begin{bmatrix} 2 \\ -3 \\ 0 \\ 1 \end{bmatrix}
$$

## Slide 26
**Title:** Example 5: Final Solution
**Content:**
**Complete Solution:**
$$
\mathbf{x} = \begin{bmatrix} -1 \\ 3 \\ 0 \\ 0 \end{bmatrix} + s\begin{bmatrix} 1 \\ -2 \\ 1 \\ 0 \end{bmatrix} + t\begin{bmatrix} 2 \\ -3 \\ 0 \\ 1 \end{bmatrix}
$$
where $s, t \in \mathbb{R}$

**Verification:**
Check particular solution:
$$
\begin{cases}
(-1) + 2(3) + 3(0) + 4(0) = -1 + 6 = 5 \quad \checkmark \\
2(-1) + 4(3) + 6(0) + 8(0) = -2 + 12 = 10 \quad \checkmark \\
3(-1) + 5(3) + 7(0) + 9(0) = -3 + 15 = 12 \quad \checkmark
\end{cases}
$$

## Slide 27
**Title:** Example 6.
**Content:**
**For what values of $a, b, c$ does the system have:**
1.  No solution?
2.  A unique solution?
3.  Infinitely many solutions?

$$
\begin{cases}
x + 2y + 3z = a \\
2x + 5y + 8z = b \\
3x + 8y + 13z = c
\end{cases}
$$

## Slide 28
**Title:** Solution
**Content:**
**Row Reduction:**
$$
\begin{bmatrix}
1 & 2 & 3 & | & a \\
2 & 5 & 8 & | & b \\
3 & 8 & 13 & | & c
\end{bmatrix}
\to
\begin{bmatrix}
1 & 2 & 3 & | & a \\
0 & 1 & 2 & | & b-2a \\
0 & 2 & 4 & | & c-3a
\end{bmatrix}
$$
$$
\to
\begin{bmatrix}
1 & 2 & 3 & | & a \\
0 & 1 & 2 & | & b-2a \\
0 & 0 & 0 & | & c-3a-2(b-2a)
\end{bmatrix}
=
\begin{bmatrix}
1 & 2 & 3 & | & a \\
0 & 1 & 2 & | & b-2a \\
0 & 0 & 0 & | & c+a-2b
\end{bmatrix}
$$

**Analysis:**
*   **No solution:** $c + a - 2b \neq 0$
*   **Infinitely many solutions:** $c + a - 2b = 0$ (rank 2, 1 free variable)
*   **Unique solution:** Never! Matrix is singular (determinant = 0)

---

# File 2: Challenging Examples with Complete Solutions (Slides 1-7)
*(Note: This file contains the title slide and the problem statements for Examples 1 through 6, which are identical to the problem statements in File 1. Please refer to File 1 for the detailed solutions associated with these problems.)*

## Slide 1
**Title:** Advanced Solutions of Linear Systems
**Subtitle:** Challenging Examples with Complete Solutions
**Footer:** Mathematics Department | January 20, 2026

## Slide 2
**Title:** Example 1. System with Parameter
**Content:** Identical to File 1, Slide 1.

## Slide 3
**Title:** Example 2. Solve the system
**Content:** Identical to File 1, Slide 6.

## Slide 4
**Title:** Example 3. Solve the system
**Content:** Identical to File 1, Slide 11.

## Slide 5
**Title:** Example 4. Find the complete solution
**Content:** Identical to File 1, Slide 15.

## Slide 6
**Title:** Example 5. Solve the underdetermined system
**Content:** Identical to File 1, Slide 20.

## Slide 7
**Title:** Example 6. Parameter Analysis
**Content:** Identical to File 1, Slide 27.

---

# File 3: Consistency Theorem for Linear Systems (Text Document)

## Page 1
**Title:** Consistency Theorem for Linear Systems

**Theorem 1 (Consistency of Linear Systems).**
A system of linear equations $A\mathbf{x} = \mathbf{b}$, where $A \in \mathbb{R}^{m \times n}$, $\mathbf{x} \in \mathbb{R}^n$, and $\mathbf{b} \in \mathbb{R}^m$, is consistent (has at least one solution) if and only if:
$$ \text{rank}(A) = \text{rank}([A|\mathbf{b}]) $$
where $[A|\mathbf{b}]$ denotes the augmented matrix.

**Proof.** Let $A = [\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n]$, where $\mathbf{a}_j \in \mathbb{R}^m$ are the column vectors of $A$.

**Part 1 ($\Rightarrow$):** Assume the system is consistent. Then there exists $\mathbf{x} = (x_1, x_2, \dots, x_n)^T$ such that:
$$ x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \dots + x_n\mathbf{a}_n = \mathbf{b} $$
This means $\mathbf{b}$ is a linear combination of the columns of $A$, so $\mathbf{b}$ belongs to the column space of $A$:
$$ \mathbf{b} \in \text{Col}(A) $$
Let $r = \text{rank}(A) = \dim(\text{Col}(A))$. Since $\mathbf{b} \in \text{Col}(A)$, adding $\mathbf{b}$ to the matrix $A$ does not increase the dimension of the column space. Therefore:
$$ \text{rank}([A|\mathbf{b}]) = \dim(\text{Col}([A|\mathbf{b}])) = \dim(\text{Col}(A)) = \text{rank}(A) $$

**Part 2 ($\Leftarrow$):** Assume $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$. Let $r = \text{rank}(A)$. This means:
$$ \dim(\text{Col}(A)) = \dim(\text{Col}([A|\mathbf{b}])) $$
Since $\text{Col}(A) \subseteq \text{Col}([A|\mathbf{b}])$ (the column space of $A$ is contained in the column space of the augmented matrix), and both spaces have the same dimension, they must be equal:
$$ \text{Col}(A) = \text{Col}([A|\mathbf{b}]) $$
This implies that $\mathbf{b} \in \text{Col}([A|\mathbf{b}]) = \text{Col}(A)$, so $\mathbf{b}$ can be expressed as a linear combination of the columns of $A$. That is, there exist scalars $x_1, x_2, \dots, x_n$ such that:
$$ x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \dots + x_n\mathbf{a}_n = \mathbf{b} $$
Thus, the vector $\mathbf{x} = (x_1, x_2, \dots, x_n)^T$ is a solution to $A\mathbf{x} = \mathbf{b}$, so the system is consistent.
Therefore, the system $A\mathbf{x} = \mathbf{b}$ is consistent if and only if $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$. $\square$

**Remark.** The proof uses the following key observations:

## Page 2
1.  The system $A\mathbf{x} = \mathbf{b}$ is consistent if and only if $\mathbf{b}$ is in the column space of $A$.
2.  $\text{rank}(A) = \dim(\text{Col}(A))$, the dimension of the column space.
3.  $\text{Col}(A) \subseteq \text{Col}([A|\mathbf{b}])$, and $\text{Col}([A|\mathbf{b}]) = \text{Col}(A)$ if and only if $\mathbf{b} \in \text{Col}(A)$.
4.  For finite-dimensional vector spaces, if $U \subseteq V$ and $\dim(U) = \dim(V)$, then $U = V$.

**Remark (Alternative Viewpoint via Row Operations).** The theorem can also be understood through row operations. Let $r = \text{rank}(A)$. Through Gaussian elimination, we can transform $A$ to row-echelon form with $r$ nonzero rows. If $\text{rank}([A|\mathbf{b}]) > r$, then in the row-echelon form of $[A|\mathbf{b}]$, there will be a row of the form $[0 \cdots 0 | c]$ with $c \neq 0$, which corresponds to the inconsistent equation $0 = c$.

**1 Classification Criteria**

**Theorem 2 (Solution Type Determination).** For the linear system $A\mathbf{x} = \mathbf{b}$ with $A \in \mathbb{R}^{m \times n}$ ($m \le n$), let:
$r_A = \text{rank}(A)$, $r_{[A|\mathbf{b}]} = \text{rank}([A|\mathbf{b}])$, $n = \text{number of variables}$

Then:
1.  **Inconsistent System:** $r_A < r_{[A|\mathbf{b}]}$
2.  **Unique Solution:** $r_A = r_{[A|\mathbf{b}]} = n$
3.  **Infinitely Many Solutions:** $r_A = r_{[A|\mathbf{b}]} < n$

**Proof.** The proof follows from the consistency theorem and the Rank-Nullity Theorem:
1.  If $r_A < r_{[A|\mathbf{b}]}$, then by Theorem 1, the system is inconsistent.
2.  If $r_A = r_{[A|\mathbf{b}]} = n$, then:
    *   The system is consistent by Theorem 1.
    *   By Rank-Nullity: $\dim(\text{Null}(A)) = n - r_A = 0$.
    *   Therefore, $\text{Null}(A) = \{\mathbf{0}\}$, so if $\mathbf{x}_1$ and $\mathbf{x}_2$ are solutions, then $A(\mathbf{x}_1 - \mathbf{x}_2) = \mathbf{0}$, implying $\mathbf{x}_1 - \mathbf{x}_2 \in \text{Null}(A) = \{\mathbf{0}\}$, so $\mathbf{x}_1 = \mathbf{x}_2$.
3.  If $r_A = r_{[A|\mathbf{b}]} < n$, then:
    *   The system is consistent by Theorem 1.
    *   By Rank-Nullity: $\dim(\text{Null}(A)) = n - r_A > 0$.
    *   Thus, $\text{Null}(A)$ contains non-zero vectors. If $\mathbf{x}_p$ is a particular solution, then for any $\mathbf{v} \in \text{Null}(A)$, $\mathbf{x}_p + \mathbf{v}$ is also a solution, giving infinitely many solutions. $\square$

## Page 3
**2 Geometric Interpretation**

**2.1 For a Single Linear Equation**
For $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$:
*   Solution set is a **hyperplane** in $\mathbb{R}^n$.
*   If all $a_i = 0$ and $b = 0$: whole space $\mathbb{R}^n$ (infinitely many).
*   If all $a_i = 0$ and $b \neq 0$: no solution.
*   Otherwise: a hyperplane of dimension $n-1$ (infinitely many).

**2.2 For Systems of Equations**
*   Each equation represents a hyperplane in $\mathbb{R}^n$.
*   Solution set is the intersection of these hyperplanes.
    *   **Unique solution:** Hyperplanes intersect at a single point.
    *   **Infinitely many:** Hyperplanes intersect along a line, plane, etc.
    *   **No solution:** Hyperplanes are parallel or otherwise don't all intersect.

**3 Examples**

**Example 1 (Inconsistent System).** Consider the system:
$$
\begin{cases}
x + y = 1 \\
x + y = 2
\end{cases}
$$
Here $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$. $\text{rank}(A) = 1$, but $\text{rank}([A|\mathbf{b}]) = 2$ (since the second row of the augmented matrix in RREF becomes $[0 \ 0 \ | \ 1]$). Thus $r_A < r_{[A|\mathbf{b}]}$, so the system is inconsistent.

**Example 2 (Unique Solution).** Consider the system:
$$
\begin{cases}
x + y = 3 \\
x - y = 1
\end{cases}
$$
Here $A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$. $\text{rank}(A) = \text{rank}([A|\mathbf{b}]) = 2 = n$, so the system has a unique solution $(x,y) = (2,1)$.

## Page 4
**Example 3 (Infinitely Many Solutions).** Consider the system:
$$
\begin{cases}
x + y + z = 3 \\
2x + 2y + 2z = 6
\end{cases}
$$
Here $A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 3 \\ 6 \end{bmatrix}$. $\text{rank}(A) = \text{rank}([A|\mathbf{b}]) = 1 < n = 3$, so the system has infinitely many solutions. The solution set is $\{(x, y, z) : x + y + z = 3\}$, a plane in $\mathbb{R}^3$.

**4 Special Cases**

**Corollary 2.1 (Homogeneous Systems).** For a homogeneous system $A\mathbf{x} = \mathbf{0}$:
1.  Always consistent (trivial solution $\mathbf{x} = \mathbf{0}$ exists).
2.  If $\text{rank}(A) = n$: only trivial solution.
3.  If $\text{rank}(A) < n$: infinitely many nontrivial solutions.
**Proof.** For $A\mathbf{x} = \mathbf{0}$, we have $\text{rank}(A) = \text{rank}([A|\mathbf{0}])$ always. The conclusion follows from Theorem 2. $\square$

**Corollary 2.2 (Square Systems).** For a square system ($m = n$):
1.  $A\mathbf{x} = \mathbf{b}$ has a unique solution if and only if $\det(A) \neq 0$.
2.  If $\det(A) \neq 0$, then $\text{rank}(A) = n$ and the system has a unique solution for any $\mathbf{b}$.
3.  If $\det(A) = 0$, then either no solution or infinitely many solutions.

---

# File 4: Consistency of Linear Systems (Definitions and Matrix Rank Methods)

## Slide 1
**Title:** Consistency of Linear Systems
**Subtitle:** Definitions and Matrix Rank Methods
**Author:** Salman Ahmadi-Asl, Innopolis University
**Date:** January 20, 2026

## Slide 2
**Title:** Overview
**Content:**
1.  Definitions
2.  Rank Analysis
3.  Examples and Applications

## Slide 3
**Title:** Linear System of Equations
**Content:**
Consider a system of $m$ linear equations in $n$ variables:
$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
\end{cases}
$$

**Matrix form:** $A\mathbf{x} = \mathbf{b}$
where $A \in \mathbb{R}^{m \times n}, \mathbf{x} \in \mathbb{R}^n, \mathbf{b} \in \mathbb{R}^m$

## Slide 4
**Title:** Consistent System
**Content:**
**Definition:**
A system of linear equations $A\mathbf{x} = \mathbf{b}$ is **consistent** if it has **at least one** solution.

**Geometric interpretation:**
*   Lines/planes/hyperplanes intersect at **at least one** common point
*   Vector $\mathbf{b}$ is in the column space of $A$
*   $\mathbf{b} \in \text{Col}(A)$

**Examples:**
*   Unique solution: Lines intersect at exactly one point
*   Infinitely many solutions: Lines are coincident

## Slide 5
**Title:** Inconsistent System
**Content:**
**Definition:**
A system of linear equations $A\mathbf{x} = \mathbf{b}$ is **inconsistent** if it has **no** solution.

**Geometric interpretation:**
*   Lines/planes/hyperplanes do **not** intersect
*   Vector $\mathbf{b}$ is **not** in the column space of $A$
*   $\mathbf{b} \notin \text{Col}(A)$

**Example:**
$$
\begin{cases}
x + y = 3 \\
x + y = 5
\end{cases}
$$
These are parallel lines that never intersect!

## Slide 6
**Title:** Key Matrices for a Linear System
**Content:**
For the system $A\mathbf{x} = \mathbf{b}$:
**Coefficient Matrix A:**
Contains only the coefficients of the variables:
$$
A = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$

## Slide 7
**Title:** Augmented Matrix $[A|\mathbf{b}]$
**Content:**
Appends the constants vector $\mathbf{b}$ as an extra column:
$$
[A|\mathbf{b}] = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} & | & b_1 \\
a_{21} & a_{22} & \dots & a_{2n} & | & b_2 \\
\vdots & \vdots & \ddots & \vdots & | & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn} & | & b_m
\end{bmatrix}
$$

## Slide 8
**Title:** Rank of a Matrix
**Content:**
**Definition:**
The **rank** of a matrix is the maximum number of linearly independent rows (or columns) in the matrix.
*   Denoted as $\text{rank}(A)$ for matrix $A$
*   Equals the number of pivot positions in row echelon form
*   $\text{rank}(A) \le \min(m, n)$

**Important properties:**
*   $\text{rank}(A) = \text{dimension of column space of } A$
*   $\text{rank}(A) = \text{dimension of row space of } A$
*   Row operations **do not** change the rank

## Slide 9
**Title:** Consistency Theorem
**Content:**
**Theorem (Rouché–Capelli Theorem):**
A system of linear equations $A\mathbf{x} = \mathbf{b}$ is **consistent** if and only if:
$$ \text{rank}(A) = \text{rank}([A|\mathbf{b}]) $$
That is, the coefficient matrix and the augmented matrix have the same rank.

**Interpretation:**
Adding the constants column $\mathbf{b}$ does **not** increase the rank of the matrix, meaning $\mathbf{b}$ is a linear combination of the columns of $A$.

## Slide 10
**Title:** Why This Works: Geometric Insight
**Content:**
**Consistent case:**
*   $\mathbf{b}$ is in $\text{Col}(A)$
*   $\mathbf{b}$ adds no new dimension
*   $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$
*   **Analogy:** $A$ spans a space, $\mathbf{b}$ is already in that space, No new "direction" is added.

**Inconsistent case:**
*   $\mathbf{b}$ is **not** in $\text{Col}(A)$
*   $\mathbf{b}$ adds a new dimension
*   $\text{rank}([A|\mathbf{b}]) = \text{rank}(A) + 1$
*   **Analogy:** $A$ spans a space, $\mathbf{b}$ points outside that space, A new "direction" is added.

## Slide 11
**Title:** Example 1: Consistent System
**Content:**
**Consider the system:**
$$ \begin{cases} 2x + 3y = 7 \\ 4x + 6y = 14 \end{cases} $$
**Coefficient matrix:**
$A = \begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix}$
$\text{rank}(A) = 1$ (rows are linearly dependent)

**Augmented matrix:**
$[A|\mathbf{b}] = \begin{bmatrix} 2 & 3 & | & 7 \\ 4 & 6 & | & 14 \end{bmatrix}$
$\text{rank}([A|\mathbf{b}]) = 1$

**Result:** $\text{rank}(A) = \text{rank}([A|\mathbf{b}]) = 1 \implies \textbf{Consistent!}$

## Slide 12
**Title:** Example 2: Inconsistent System
**Content:**
**Consider the system:**
$$ \begin{cases} 2x + 3y = 7 \\ 4x + 6y = 15 \end{cases} $$
**Coefficient matrix:**
$A = \begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix}$
$\text{rank}(A) = 1$

**Augmented matrix:**
$[A|\mathbf{b}] = \begin{bmatrix} 2 & 3 & | & 7 \\ 4 & 6 & | & 15 \end{bmatrix}$
$\text{rank}([A|\mathbf{b}]) = 2$ (rows are now linearly independent!)

**Result:** $\text{rank}(A) = 1 \neq 2 = \text{rank}([A|\mathbf{b}]) \implies \textbf{Inconsistent!}$

## Slide 13
**Title:** Summary: Decision Procedure
**Content:**
1.  Given system $A\mathbf{x} = \mathbf{b}$
2.  Form augmented matrix $[A|\mathbf{b}]$
3.  Compute $\text{rank}(A)$ and $\text{rank}([A|\mathbf{b}])$
4.  Compare ranks:

| Case | Rank Condition | Conclusion |
| :--- | :--- | :--- |
| 1 | $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$ | Consistent |
| 2 | $\text{rank}(A) \neq \text{rank}([A|\mathbf{b}])$ | Inconsistent |

**Note:**
If consistent and $\text{rank}(A) = n$ (number of variables): **Unique solution**
If consistent and $\text{rank}(A) < n$: **Infinitely many solutions**

## Slide 14
**Title:** Practical Computation
**Content:**
**Step-by-step procedure using Gaussian elimination:**
1.  Start with augmented matrix $[A|\mathbf{b}]$
2.  Perform row operations to obtain row echelon form
3.  Count the number of pivot positions (non-zero rows) in:
    *   The coefficient matrix part: $\text{rank}(A)$
    *   The entire augmented matrix: $\text{rank}([A|\mathbf{b}])$
4.  Compare the two counts

**Shortcut:** If you get a row of the form $[0 \ 0 \ \dots \ 0 \ | \ c]$ where $c \neq 0$, the system is **immediately** inconsistent.

## Slide 15
**Title:** Visual Summary
**Content:**
**Remember**
*   **Rank** = dimension of the column space
*   **Consistent** = $\mathbf{b}$ is in the column space of $A$
*   **Rank test** = checking if $\mathbf{b}$ adds a new dimension

## Slide 16
**Title:** Questions?
**Content:**
Thank you!
Questions and Discussion

---

# File 5: Linear Systems: Row Echelon and Reduced Row Echelon Forms (Part 1)

## Slide 1
**Title:** Linear Systems: Row Echelon and Reduced Row Echelon Forms
**Author:** Salman Ahmadi-Asl, Innopolis University
**Date:** January 20, 2026

## Slide 2
**Title:** Outline
**Content:**
1.  Introduction to Linear Systems
2.  Row Echelon Form (REF)
3.  Reduced Row Echelon Form (RREF)
4.  Complete Solution Structure
5.  Summary

## Slide 3
**Title:** What is a Linear System?
**Content:**
A system of $m$ linear equations in $n$ variables.
(Shows general system equation)
**Matrix Form:**
$A\mathbf{x} = \mathbf{b}$ where
$A = \begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \dots & a_{mn} \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix}$

## Slide 4
**Title:** Matrix Form
**Content:**
$A\mathbf{x} = \mathbf{b}$
where $A$ is $m \times n$, $\mathbf{x}$ is $n \times 1$, $\mathbf{b}$ is $m \times 1$.

## Slide 5
**Title:** Definition of Row Echelon Form (REF) or Stair-step form
**Content:**
A matrix is in Row Echelon Form if:
1.  All nonzero rows are above any rows of all zeros.
2.  Each leading entry (pivot) is in a column to the right of the pivot above it.
3.  All entries below a pivot are zeros.

**Example:**
$$
\begin{bmatrix}
\boxed{2} & 3 & -1 & 5 \\
0 & \boxed{4} & 2 & -3 \\
0 & 0 & 0 & \boxed{1} \\
0 & 0 & 0 & 0
\end{bmatrix}
$$
Boxed entries are pivots. This matrix is in REF.

## Slide 6
**Title:** Note
**Content:**
Pivots are the first nonzero entries in their rows. They do NOT need to be 1.

## Slide 7
**Title:** Definition of Reduced Row Echelon Form (RREF) or Canonical form
**Content:**
A matrix is in Reduced Row Echelon Form if:
1.  It is in REF.
2.  Each pivot is 1.
3.  Each pivot is the only nonzero entry in its column.

**Example:**
$$
\begin{bmatrix}
\boxed{1} & 0 & 3 & 0 \\
0 & \boxed{1} & -2 & 0 \\
0 & 0 & 0 & \boxed{1} \\
0 & 0 & 0 & 0
\end{bmatrix}
$$
This matrix is in RREF. Each pivot column contains exactly one 1.

## Slide 8
**Title:** Key Difference
**Content:**
In RREF, **all entries above and below pivots are 0**, and pivots are exactly 1.

## Slide 9
**Title:** Example: REF vs RREF
**Content:**
**Row Echelon Form:**
$$
\begin{bmatrix}
1 & 2 & 3 & | & 4 \\
0 & 2 & 5 & | & 6 \\
0 & 0 & 6 & | & 2 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$
**Reduced Row Echelon Form:**
$$
\begin{bmatrix}
1 & 0 & 0 & | & -3 \\
0 & 1 & 0 & | & -4 \\
0 & 0 & 1 & | & 2 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

## Slide 10
**Title:** Solution Structure: Particular + General
**Content:**
**Theorem:** For a consistent system $A\mathbf{x} = \mathbf{b}$, the complete solution is:
$$ \mathbf{x} = \mathbf{x}_p + \mathbf{x}_h $$
where:
*   $\mathbf{x}_p$: A particular solution (any solution)
*   $\mathbf{x}_h$: The general solution to $A\mathbf{x} = \mathbf{0}$ (homogeneous system)

**Homogeneous System:** $A\mathbf{x}_h = \mathbf{0}$
Solution set forms a vector space (null space) of dimension $n - r$, where $r = \text{rank}(A)$.

## Slide 11
**Title:** Null Space Dimension
**Content:**
$$ \dim(\text{Null}(A)) = n - \text{rank}(A) $$
This equals the number of free variables/parameters in the solution.

## Slide 12
**Title:** Step-by-Step Methodology
**Content:**
1.  Write augmented matrix $[A|\mathbf{b}]$.
2.  Transform to Reduced Row Echelon Form (RREF).
3.  Identify pivot columns (basic variables) and free columns (free variables).
4.  Find **particular solution** $\mathbf{x}_p$ by setting free variables $= 0$.
5.  Find **homogeneous solutions** by solving $A\mathbf{x} = \mathbf{0}$.
6.  Write complete solution: $\mathbf{x} = \mathbf{x}_p + \sum c_i\mathbf{v}_i$.

**Notation:**
*   Basic variables: Correspond to pivot columns.
*   Free variables: Can take any value (parameters).

## Slide 13
**Title:** Example 1: System with Unique Solution
**Content:**
**System:**
$$ \begin{cases} x + 2y + 3z = 9 \\ 2x - y + z = 8 \\ 3x - z = 3 \end{cases} $$
**Augmented Matrix and RREF:**
$$ \begin{bmatrix} 1 & 2 & 3 & | & 9 \\ 2 & -1 & 1 & | & 8 \\ 3 & 0 & -1 & | & 3 \end{bmatrix} \xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 0 & 0 & | & 2 \\ 0 & 1 & 0 & | & -1 \\ 0 & 0 & 1 & | & 3 \end{bmatrix} $$

## Slide 14
**Title:** Solution
**Content:**
**Unique solution:**
$$ \mathbf{x} = \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix} $$
No free variables, null space = $\{\mathbf{0}\}$.

## Slide 15
**Title:** Example 2: System with Infinite Solutions
**Content:**
**System:**
$$ \begin{cases} x_1 + 2x_2 + 3x_3 + 4x_4 = 5 \\ 2x_1 + 4x_2 + 6x_3 + 8x_4 = 10 \\ x_1 + 2x_2 + 2x_3 + 3x_4 = 4 \end{cases} $$
**Augmented Matrix:**
$$ \begin{bmatrix} 1 & 2 & 3 & 4 & | & 5 \\ 2 & 4 & 6 & 8 & | & 10 \\ 1 & 2 & 2 & 3 & | & 4 \end{bmatrix} $$

## Slide 16
**Title:** Example 2: RREF and Solution
**Content:**
**Reduced Row Echelon Form:**
$$ \xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 2 & 0 & -1 & | & 2 \\ 0 & 0 & 1 & 1 & | & 1 \\ 0 & 0 & 0 & 0 & | & 0 \end{bmatrix} $$
**Variables:**
*   Basic variables: $x_1, x_3$ (pivot columns 1 and 3)
*   Free variables: $x_2, x_4$ (columns 2 and 4)

**Equations from RREF:**
$$ \begin{cases} x_1 + 2x_2 - x_4 = 2 \\ x_3 + x_4 = 1 \end{cases} $$

## Slide 17
**Title:** Example 2: Complete Solution
**Content:**
**Particular Solution:**
Set free variables $x_2 = 0, x_4 = 0$:
$$ \begin{cases} x_1 = 2 \\ x_3 = 1 \end{cases} \implies \mathbf{x}_p = \begin{bmatrix} 2 \\ 0 \\ 1 \\ 0 \end{bmatrix} $$

## Slide 18
**Title:** Homogeneous Solution
**Content:**
Solve $A\mathbf{x} = \mathbf{0}$:
$$ \begin{cases} x_1 + 2x_2 - x_4 = 0 \\ x_3 + x_4 = 0 \end{cases} $$
Express basic variables in terms of free variables:
$$ \begin{cases} x_1 = -2x_2 + x_4 \\ x_3 = -x_4 \end{cases} $$

## Slide 19
**Title:** Example 2: General Solution
**Content:**
Let $x_2 = s, x_4 = t$ (parameters):
$$ \mathbf{x}_h = \begin{bmatrix} -2s + t \\ s \\ -t \\ t \end{bmatrix} = s\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + t\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix} $$
**Complete Solution:**
$$ \mathbf{x} = \mathbf{x}_p + \mathbf{x}_h = \begin{bmatrix} 2 \\ 0 \\ 1 \\ 0 \end{bmatrix} + s\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + t\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix} $$

## Slide 20
**Title:** Example 3: Homogeneous System
**Content:**
**System:**
$$ \begin{cases} x + 2y + 3z = 0 \\ 2x + 4y + 6z = 0 \\ 3x + 6y + 9z = 0 \end{cases} $$
**Augmented Matrix and RREF:**
$$ \begin{bmatrix} 1 & 2 & 3 & | & 0 \\ 2 & 4 & 6 & | & 0 \\ 3 & 6 & 9 & | & 0 \end{bmatrix} \xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 2 & 3 & | & 0 \\ 0 & 0 & 0 & | & 0 \\ 0 & 0 & 0 & | & 0 \end{bmatrix} $$
**Variables:**
*   Basic: $x_1$
*   Free: $x_2, x_3$

## Slide 21
**Title:** Solution
**Content:**
Equation: $x + 2y + 3z = 0$. Let $y=s, z=t$:
$$ \mathbf{x} = \begin{bmatrix} -2s - 3t \\ s \\ t \end{bmatrix} = s\begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix} + t\begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix} $$

## Slide 22
**Title:** Example 4: Inconsistent System (No Solution)
**Content:**
**System:**
$$ \begin{cases} x + y + z = 1 \\ x + y + z = 2 \\ 2x + 2y + 2z = 3 \end{cases} $$
**RREF:**
$$ \begin{bmatrix} 1 & 1 & 1 & | & 1 \\ 1 & 1 & 1 & | & 2 \\ 2 & 2 & 2 & | & 3 \end{bmatrix} \xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 1 & 1 & | & 0 \\ 0 & 0 & 0 & | & 1 \\ 0 & 0 & 0 & | & 0 \end{bmatrix} $$
**No Solution:** Row 2: $0 = 1$ (contradiction).

## Slide 23
**Title:** Summary
**Content:**
**Key Points:**
*   Use RREF to solve linear systems efficiently.
*   Identify pivot columns and free columns.
*   Complete solution = Particular + Homogeneous.
*   Number of free variables = $n - \text{rank}(A)$.

**Cases for $A\mathbf{x} = \mathbf{b}$:**
1.  **No solution:** Inconsistent ($0 = \text{nonzero}$ in RREF).
2.  **Unique solution:** Rank = $n$, null space = $\{\mathbf{0}\}$.
3.  **Infinite solutions:** Rank < $n$, free variables exist.

## Slide 24
**Title:** Thank You!
**Content:**
Questions?

---

# File 6: Linear Systems: Row Echelon and Reduced Row Echelon Forms (Part 2)

## Slide 1
**Title:** Linear Systems: Row Echelon and Reduced Row Echelon Forms
*(Same title slide as Part 1)*

## Slide 2
**Title:** Example 1: Solving a System using REF
**Content:**
**Solve:**
$$ \begin{cases} 2x + 4y - 2z = 2 \\ 4x + 9y - 3z = 8 \\ -2x - 3y + 7z = 10 \end{cases} $$
**Augmented Matrix:**
$$ \begin{bmatrix} 2 & 4 & -2 & 2 \\ 4 & 9 & -3 & 8 \\ -2 & -3 & 7 & 10 \end{bmatrix} $$
**After Row Operations (REF):**
$$ \begin{bmatrix} 2 & 4 & -2 & 2 \\ 0 & 1 & 1 & 4 \\ 0 & 0 & 4 & 8 \end{bmatrix} $$

## Slide 3
**Title:** Example 1: Solving a System using REF
**Content:**
**Back Substitution:**
$4z = 8 \implies z = 2$
$y + z = 4 \implies y = 2$
$2x + 4y - 2z = 2 \implies 2x + 8 - 4 = 2 \implies x = -1$
**Solution:** $(x, y, z) = (-1, 2, 2)$

## Slide 4
**Title:** Example 2: Solving using RREF
**Content:**
**Solve:**
$$ \begin{cases} x + 2y + 3z = 9 \\ 2x - y + z = 8 \\ 3x + y - z = 3 \end{cases} $$
**Augmented Matrix to RREF:**
$$ \begin{bmatrix} 1 & 2 & 3 & 9 \\ 2 & -1 & 1 & 8 \\ 3 & 1 & -1 & 3 \end{bmatrix} \xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 3 \end{bmatrix} $$
**Solution:** $(2, -1, 3)$ (Direct reading).

## Slide 5
**Title:** Understanding Underdetermined Systems
**Content:**
*   When $n > m$ (more variables than equations).
*   System is **underdetermined**.
*   Two possibilities:
    *   No solution (inconsistent).
    *   Infinitely many solutions (consistent).
*   If consistent: $n - r$ free variables.

**General Solution Pattern:** (Shows a matrix with free vars $x_3, x_4$)

## Slide 6
**Title:** Example 3: 2 Equations, 4 Variables
**Content:**
**Solve:**
$$ \begin{cases} x + 2y - z + 3w = 5 \\ 2x + 4y - 2z + 7w = 12 \end{cases} $$
**Augmented Matrix to RREF:**
$$ \begin{bmatrix} 1 & 2 & -1 & 3 & 5 \\ 2 & 4 & -2 & 7 & 12 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & -1 & 0 & -1 \\ 0 & 0 & 0 & 1 & 2 \end{bmatrix} $$

## Slide 7
**Title:** Example 3 Solution
**Content:**
From RREF:
$x + 2y - z = -1$
$w = 2$
Let $y=s, z=t$ (free variables).
$x = -1 - 2s + t$.
**Solution:** $(x, y, z, w) = (-1 - 2s + t, s, t, 2)$.

## Slide 8
**Title:** Example 4: 3 Equations, 5 Variables
**Content:**
**Solve:** (System given).
**RREF of Augmented Matrix:**
$$ \begin{bmatrix} 1 & 0 & -1 & -2 & -3 & 0 \\ 0 & 1 & 2 & 3 & 4 & 5 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} $$
**From RREF:**
$x_1 = x_3 + 2x_4 + 3x_5$
$x_2 = 5 - 2x_3 - 3x_4 - 4x_5$
Free variables: $x_3=s, x_4=t, x_5=u$.

## Slide 9
**Title:** Example 5: Inconsistent System
**Content:**
**Solve:**
$$ \begin{cases} x + y + z = 1 \\ 2x + 2y + 2z = 3 \\ 3x + 3y + 3z = 4 \end{cases} $$
**Row Ops to REF:**
Row of form $[0 \ 0 \ 0 \ | \ 1]$ represents $0 = 1$.
**Inconsistency Detected!**

## Slide 10
**Title:** Problem Set 1: Solve Using Different Methods
**Content:**
1.  Solve using REF: (System given)
2.  Solve using RREF: (System given)
3.  Solve (more variables than equations): (System given)

## Slide 11
**Title:** Problem 1: Solve using REF
**Content:**
**System:**
$$ \begin{cases} 3x - 2y + z = 7 \\ x + y - 2z = -2 \\ 2x - y + 3z = 9 \end{cases} $$
**Augmented matrix:**
$$ \begin{bmatrix} 3 & -2 & 1 & 7 \\ 1 & 1 & -2 & -2 \\ 2 & -1 & 3 & 9 \end{bmatrix} $$

## Slide 12
**Title:** Problem 1 Solution (Step 1-2)
**Content:**
Step 1: Swap R1 and R2.
Step 2: Elimination operations.
$$ \begin{bmatrix} 1 & 1 & -2 & -2 \\ 0 & -5 & 7 & 13 \\ 0 & -3 & 7 & 13 \end{bmatrix} $$

## Slide 13
**Title:** Problem 1 Solution (Step 3-4)
**Content:**
Continues elimination to achieve REF.
Final Matrix:
$$ \begin{bmatrix} 1 & 1 & -2 & -2 \\ 0 & 1 & -7/5 & -13/5 \\ 0 & 0 & 14/5 & 26/5 \end{bmatrix} $$

## Slide 14
**Title:** Problem 1 Solution (Back Substitution)
**Content:**
Calculates $z, y, x$.
$z = 13/7, y=0, x=12/7$.
**Unique solution.**

## Slide 15
**Title:** Problem 2: Solve using RREF
**Content:**
**System:**
$$ \begin{cases} x + 2y + 3z = 1 \\ 2x + 4y + 6z = 2 \\ 3x + 6y + 9z = 3 \end{cases} $$
**Augmented matrix:** (Matrix shown)

## Slide 16
**Title:** Problem 2 Solution
**Content:**
Row operations lead to:
$$ \begin{bmatrix} 1 & 2 & 3 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} $$
**Already in RREF!**
Infinitely many solutions. $(1 - 2s - 3t, s, t)$.

## Slide 17
**Title:** Problem 3: More Variables than Equations
**Content:**
**System:**
$$ \begin{cases} x + 2y - z + w = 4 \\ 3x + 6y - 2z + 4w = 10 \end{cases} $$

## Slide 18
**Title:** Problem 3 Solution
**Content:**
RREF leads to:
$x + 2y - z + w = 4$
$z + w = -2$
Solution derived with parameters $s, t$.

## Slide 19
**Title:** Problem 4: Determine Consistency
**Content:**
**System:**
$$ \begin{cases} x + y + z = 5 \\ 2x + 2y + 2z = 10 \\ x - y + z = 3 \end{cases} $$
**Question:** Is this system consistent?

## Slide 20
**Title:** Problem 4 Solution (Step 1-2)
**Content:**
Row operations. No row of form $[0 \ 0 \ 0 \ | \ c]$ with $c \neq 0$.
$\Rightarrow$ **System is consistent!**

## Slide 21
**Title:** Problem 4 Solution (Step 3-4)
**Content:**
From RREF:
$x + z = 4$
$y = 1$
Solution: $(4-t, 1, t)$.

## Slide 22
**Title:** Summary Table
**Content:**
Table summarizing Problems 1-4 (Size, Consistent?, Solution Type).

## Slide 23
**Title:** Rank Analysis Summary
**Content:**
Breakdown of $\text{rank}(A)$ vs $\text{rank}([A|\mathbf{b}])$ for each problem and the resulting conclusion (Unique vs Infinite).

## Slide 24
**Title:** Thank You!
**Content:**
Questions?

---

# File 7: Problems 1-12 (Handwritten Annotations)

## Slide 1
**Problem 1**
**Printed:** Describe the intersection of the three planes $u + v + w + z = 6$ and $u + w + z = 4$ and $u + w = 2$ (all in four-dimensional space). Is it a line or a point or an empty set? What is the intersection if the fourth plane $u = -1$ is included? Find a fourth equation that leaves us with no solution.

**Handwritten Notes:**
(1) $u + v + w + z = 6$
(2) $u + w + z = 4$
(3) $u + w = 2$

By subtracting (3) from (2) and (1):
From (2) and (3) $\to z = 2$.
From (1) and (2) $\to v + z = 4 \xrightarrow{z=2} v = 2$.
From (3) $\to u + w = 2$.

"So we conclude that it is a **line** in 4D"

In the 2nd part we add $u = -1$.
By that we can eliminate $u$ from the last eq. and get:
$u = -1$
$v = 2$
$w = 3$
$z = 2$
which is a **point** in 4D.

## Slide 2
**Problem 2**
**Printed:** When $\mathbf{b} = (2, 5, 7)$, find a solution $(u, v, w)$ to the equation shown below different from the solution $(1, 0, 1)$.
$u\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + v\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} + w\begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} = \mathbf{b}$

**Handwritten Notes:**
We can write this vector eq. as system of 3 eqs.
(1) $u + v + w = 2$
(2) $2u + 3w = 5$
(3) $3u + v + 4w = 7$

If we add (1) to (2) we get (3).
Therefore, we can find the combination of these 3 eqs $(1)+(2)-(3)$ where we get $0=0$.

From (2) $\to u = 5/2 - 3/2w$.
And if, for example, $w = -2$ we have $u = 11/2$.
By substituting $u=11/2$ and $w=-2$ into (3) we get $-3/2 = v$.
So $(11/2, -3/2, -2)$ is another sol. of the given vector eq.

## Slide 3
**Problem 3**
**Printed:** The column picture for the previous exercise (singular system) is... Show that the three columns on the left lie in the same plane by expressing the third column as a combination of the first two. What are all the solutions $(u, v, w)$ if $\mathbf{b}$ is the zero vector $(0, 0, 0)$?

**Handwritten Notes:**
lets express $v_3$ as $v_3 = \alpha v_1 + \beta v_2$, $\alpha, \beta \in \mathbb{R}$.
Then we have $\alpha \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \beta \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} \iff \begin{cases} \alpha + \beta = 1 \\ 2\alpha = 3 \\ 3\alpha + \beta = 4 \end{cases} \implies \beta = -1, \alpha = 3/2$ (Wait, notes say $\implies \beta=2, \alpha=-1$?).
Correction from image right side:
$\to v_3 = -v_1 + 2v_2 \iff -\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix}$ (Checks out: -1+2=1, -2+0 \neq 3... wait, calculation in image: $-1 \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} + 2 \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$ - image text is a bit messy, let's transcribe exactly what is written).
Written: $v_3 = -v_1 + 2v_2$
$3^{rd}$ column is a combination of the first 2 columns.
Now lets find all sol of $(u, v, w)$ of $u[\dots] + v[\dots] + w[\dots] = [\mathbf{0}]$.
as we know from previous that $-v_1 + 2v_2 - v_3 = 0$ which is equivalent to $-\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} - \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ (Actually vector math check: -1+2-1=0, -2+0-3 != 0. The handwriting seems to try to verify specific linear dependence but might have arithmetic error or the problem implies singularity differently. Let's stick to transcription).
$\implies (u,v,w) = (-1, 2, -1)$ and also $(u,v,w) = (0,0,0)$ by default.

## Slide 4
**Problem 4**
**Printed:** Under what condition on $y_1, y_2, y_3$ do the points $(0, y_1), (1, y_2), (2, y_3)$ lie on a straight line?

**Handwritten Notes:**
eq of a line $y = mx + c$
Plug in point (1) we get $\to y_1 = c$.
Point (2) $\to y_2 = m \cdot 1 + c \xrightarrow{y_1} m = y_2 - y_1$ (*)
Point (3) $\to y_3 = m \cdot 2 + c \xrightarrow{y_1} m = \frac{y_3 - y_1}{2}$ (**)
$* = ** \implies y_2 - y_1 = \frac{y_3 - y_1}{2} \implies 2y_2 - 2y_1 = y_3 - y_1 \implies 2y_2 - y_1 - y_3 = 0$.

## Slide 5
**Problem 5**
**Printed:** Find a point with $z = 2$ on the intersection line of the planes $x + y + 3z = 6$ and $x - y + z = 4$. Find the point with $z = 0$ and a third point halfway between.

**Handwritten Notes:**
$x + y + 3z = 6$
$x - y + z = 4$
$z=2 \downarrow$
$x + y + 6 = 6 \to x + y = 0$
$x - y + 2 = 4 \to x - y = 2$
$\downarrow$
$x = -y \implies -y - y = 2 \implies -2y = 2 \implies y = -1$.
$x = 1$.
$\implies (1, -1, 2)$

$z=0 \downarrow$
$x + y = 6$
$x - y = 4$
$\downarrow$
$(x+y) - (x-y) = 6-4 \implies 2y = 2 \implies y = 1$.
$x = 5$.
$\implies (5, 1, 0)$

Halfway point H between these intersection points
$H = \frac{1}{2} [(1, -1, 2) + (5, 1, 0)] \implies (3, 0, 1)$.

## Slide 6
**Problem 6**
**Printed:** In these equations, the third column (multiplying $w$) is the *same* as the right side $\mathbf{b}$. The column form of the equations *immediately* gives what solution for $(u, v, w)$?
$6u + 7v + 8w = 8$
$4u + 5v + 9w = 9$
$2u - 2v + 7w = 7$

**Handwritten Notes:**
lets write it in the vector eq.
$u\begin{bmatrix} 6 \\ 4 \\ 2 \end{bmatrix} + v\begin{bmatrix} 7 \\ 5 \\ -2 \end{bmatrix} + w\begin{bmatrix} 8 \\ 9 \\ 7 \end{bmatrix} = \begin{bmatrix} 8 \\ 9 \\ 7 \end{bmatrix}$
as you noticed the last column is the same as the solution on the right hand side
$\implies (u, v, w) = (0, 0, 1)$ there is no need of additional calculation.

## Slide 7
**Problem 7**
**Printed:** Apply elimination (circle the pivots) and back-substitution to solve
$2x - 3y = 3$
$4x - 5y + z = 7$
$2x - y - 3z = 5$

**Handwritten Notes:**
Matrix form:
$\begin{bmatrix} \boxed{2} & -3 & 0 & 3 \\ 4 & -5 & 1 & 7 \\ 2 & -1 & -3 & 5 \end{bmatrix}$
$R_2: R_2 - 2R_1$, $R_3: R_3 - R_1$
$\to \begin{bmatrix} 2 & -3 & 0 & 3 \\ 0 & \boxed{1} & 1 & 1 \\ 0 & 2 & -3 & 2 \end{bmatrix}$
$R_3: R_3 - 2R_2$
$\to \begin{bmatrix} \boxed{2} & -3 & 0 & 3 \\ 0 & \boxed{1} & 1 & 1 \\ 0 & 0 & \boxed{-5} & 0 \end{bmatrix}$ (Pivots circled: 2, 1, -5).

applying back substitution:
$2x - 3y = 3 \to x = 3$
$y + z = 1 \xrightarrow{z=0} y = 1$
$-5z = 0 \to z = 0$
$\implies$ sol is $(3, 1, 0)$.

## Slide 8
**Problem 8**
**Printed:** Which number $d$ forces a row exchange, and what is the triangular system (not singular) for that $d$? Which $d$ makes this system singular (no third pivot)?
$2x + 5y + z = 0$
$4x + dy + z = 2$
$y - z = 3$

**Handwritten Notes:**
$\begin{bmatrix} 2 & 5 & 1 & 0 \\ 4 & d & 1 & 2 \\ 0 & 1 & -1 & 3 \end{bmatrix}$
$R_2: R_2 - 2R_1$
$\to \begin{bmatrix} 2 & 5 & 1 & 0 \\ 0 & d-10 & -1 & 2 \\ 0 & 1 & -1 & 3 \end{bmatrix}$
To force row exchange $d-10=0 \implies d=10$.
a row exchange $d=11$ (Note: The handwriting says $d=11$ next to the arrow pointing to the swapped matrix, but the logic for row exchange is usually a zero pivot).
If $d=11$:
$\begin{bmatrix} 2 & 5 & 1 & 0 \\ 0 & 1 & -1 & 2 \\ 0 & 1 & -1 & 3 \end{bmatrix}$
$R_3: R_3 - R_2$
$\to \begin{bmatrix} 2 & 5 & 1 & 0 \\ 0 & 1 & -1 & 2 \\ 0 & 0 & 0 & 1 \end{bmatrix}$ the sys is singular.

To make the sys singular we need to eliminate the third Pivot (get zeros instead of $1, -1$ in 3rd row).
logical choice is $d-10=1 \implies d=11$ (Note: Text is a bit confusing, but deriving $d=10$ forces row exchange because pivot is 0. Singularity condition is derived on the right side).

## Slide 9
**Problem 9**
**Printed:** a) Construct a 3 by 3 system that needs two row exchanges to reach a triangular form and a solution. b) Construct a 3 by 3 system that needs a row exchange to keep going, but breaks down later.

**Handwritten Notes:**
a) There are many sol for this task for example:
$\begin{bmatrix} 0 & 4 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 1 & 1 & 1 & 5 \end{bmatrix}$
b)
$\begin{bmatrix} 1 & 1 & 1 & 4 \\ 0 & 0 & 1 & 3 \\ 1 & 1 & 2 & 6 \end{bmatrix}$
$R_2 \leftrightarrow R_3 \implies \begin{bmatrix} 1 & 1 & 1 & 4 \\ 1 & 1 & 2 & 6 \\ 0 & 0 & 1 & 3 \end{bmatrix}$
$R_2: R_2 - R_1 \to \begin{bmatrix} 1 & 1 & 1 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 3 \end{bmatrix}$ (Note: The last matrix shows a break down $0 0 0 -1$, labelled "Sys breaks down since 0=1").

## Slide 10
**Problem 10**
**Printed:** Find the pivots and the solution for these four equations:
$2x + y = 0$
$x + 2y + z = 0$
$y + 2z + t = 0$
$z + 2t = 5$

**Handwritten Notes:**
Do it as H.W.
the answer is $(-1, 2, -3, 4)$

## Slide 11
**Problem 11**
**Printed:** Apply elimination and back-substitution to solve and find the pivots:
$2u + 3v = 0$
$4u + 5v + w = 3$
$2u - v - 3w = 5$

**Handwritten Notes:**
$\begin{bmatrix} 2 & 3 & 0 & 0 \\ 4 & 5 & 1 & 3 \\ 2 & -1 & -3 & 5 \end{bmatrix}$
$R_2: R_2 - 2R_1$, $R_3: R_3 - R_1$
$\to \begin{bmatrix} 2 & 3 & 0 & 0 \\ 0 & -1 & 1 & 3 \\ 0 & -4 & -3 & 5 \end{bmatrix}$
$R_3: R_3 - 4R_2$
$\to \begin{bmatrix} 2 & 3 & 0 & 0 \\ 0 & -1 & 1 & 3 \\ 0 & 0 & -7 & -7 \end{bmatrix}$

Back Substitution:
$-7w = -7 \implies w = 1$
$-v + w = 3 \implies -v + 1 = 3 \implies v = -2$
$2u + 3v = 0 \implies u = 3$
$(3, -2, 1)$

## Slide 12
**Problem 12**
**Printed:** True or false questions about elimination (zero coefficients).

**Handwritten Notes:**
a) False. (Matrix example shown)
b) False. (Matrix example shown)
c) True. (We have a 2x2 sys of eq).

---

# File 8: Exercises 1-7 (Handwritten Annotations)

## Slide 1
**Exercise 1**
**Printed:** Consider the following system... Sketch these three lines... What happens when right hand side are zero?... Is there any choice... to intersect at the same point?
$x + 2y = 2$
$x - y = 2$
$y = 1$

**Handwritten Notes:**
(Sketch of three lines on grid)
*   If the right hand side is set equal to zero, then all the lines will cross at the origin.
*   If we set the third equation equal to zero, then the point (2,0) will satisfy the system.

## Slide 2
**Exercise 2**
**Printed:** Explain why this system is singular... What value should be instead of 0... What is one of the solutions?
$u + v + w = 2$
$u + 2v + 3w = 1$
$v + 2w = 0$

**Handwritten Notes:**
If we perform the operation: $Row(2) - Row(1)$ then we obtain:
$\begin{bmatrix} 1 & 1 & 1 & 2 \\ 0 & 1 & 2 & -1 \\ 0 & 1 & 2 & 0 \end{bmatrix}$
Here we notice our inconsistency: $0 = -1$.
If we set the right hand side of the third equation equal to negative one, we have:
$\begin{bmatrix} 1 & 1 & 1 & 2 \\ 1 & 2 & 3 & 1 \\ 0 & 1 & 2 & -1 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 1 & 2 \\ 0 & 1 & 2 & -1 \\ 0 & 1 & 2 & -1 \end{bmatrix}$
From here we can get all the solutions:
$y + 2z = -1 \implies y = -2z - 1$
$x + (2z - 1) + z = 2 \implies x + 3z = 3 \implies x = 3(1-z)$
Solution in terms of z: $(3(1-z), -(2z+1), z)$.
This system has many solutions, one is: $(3, -1, 0)$.

## Slide 3
**Exercise 3**
**Printed:** Normally 4 planes in a 4D space meet at a point... What combination of vectors produces $(3,3,3,2)$? What equations... solving?

**Handwritten Notes:**
The system of equations:
$x + y + z + t = 3$
$y + z + t = 3$
$z + t = 3$
$t = 1$ (error in note? Sum of vectors is 2 in printed text, handwritten says t=1... wait, the vector sum in print is (3,3,3,2), so last component is 2. Handwritten says t=1? Let's check the vectors. Vectors: (1,1,1,1), (0,1,1,1), (0,0,1,1), (0,0,0,1). The last component sum is $x(0)+y(0)+z(0)+t(1)=2$, so $t=2$. Handwritten says $t=1$. It might be a mistake in the handwritten note or a different problem interpretation. I will transcribe what is written).
Written: "t=1".
Which is already in an upper triangular form, therefore after back-substitution we get: $(0, 0, 1, 2)$.

## Slide 4
**Exercise 4**
**Printed:** Reduce the following system to an upper triangular form...
$2x + 3y + z = 8$
$4x + 7y + 5z = 20$
$-2y + 2z = 0$

**Handwritten Notes:**
Matrix form: $\begin{bmatrix} 2 & 3 & 1 & 8 \\ 4 & 7 & 5 & 20 \\ 0 & -2 & 2 & 0 \end{bmatrix}$
Operation $Row(2) - 2Row(1)$ obtain:
$\begin{bmatrix} \boxed{2} & 3 & 1 & 8 \\ 0 & \boxed{1} & 3 & 4 \\ 0 & -2 & 2 & 0 \end{bmatrix}$ (First pivot 2, second pivot 1).
... second pivot operation ...
$\begin{bmatrix} 2 & 3 & 1 & 8 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 8 & 8 \end{bmatrix}$
Finally, after solving it for x, y, z we have:
$(2, 1, 1)$.

## Slide 5
**Exercise 5**
**Printed:** Which number $b$ leads later to a row exchange? Which $b$ leads to a missing pivot? Singular case...
$x + by = 0$
$x - 2y - z = 0$
$y + z = 0$

**Handwritten Notes:**
If we set $b=-2$:
$\begin{bmatrix} 1 & -2 & 0 \\ 1 & -2 & -1 \\ 0 & 1 & 1 \end{bmatrix} \sim \begin{bmatrix} 1 & -2 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 1 \end{bmatrix}$ (row exchange needed).
If we set $b=-1$:
$\begin{bmatrix} 1 & -1 & 0 \\ 1 & -2 & -1 \\ 0 & 1 & 1 \end{bmatrix} \sim \begin{bmatrix} 1 & -1 & 0 \\ 0 & -1 & -1 \\ 0 & 1 & 1 \end{bmatrix}$
To find the solutions to this system, from the second and third row respectively we have:
$y + z = 0 \implies z = -y$
$x - y = 0 \implies x = y$
Which is $(x, y, z) = (y, y, -y)$.
for $y=1$ we get: $(1, 1, -1)$.

## Slide 6
**Exercise 6**
**Printed:** Construct a 3 by 3 example that has 9 different coefficients... rows 2 and 3 become zero...

**Handwritten Notes:**
If we consider $\begin{bmatrix} a & b & c \\ 4a & 4b & 4c \\ 5a & 5b & 5c \end{bmatrix}$ (proportional).
we can see that after simplifications the second and third row will be equal to zero.
If we consider the $Ax=b$ system with $b=(1, 10, 100)$:
Writing the augmented matrix...
In this case we have an inconsistency.
If $b=(0,0,0)$ we have:
After simplifying, we get:
$\begin{bmatrix} a & b & c & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
In this case we have many solutions, e.g. $(0,0,0), (1, -2, 1)$.
to get them all, from the first row:
$ax + by + cz = 0 \to z = -\frac{1}{c}(ax+by), c \neq 0$.
and we can have a generic element in terms of x and y: $(x, y, -\frac{1}{c}(ax+by))$.

## Slide 7
**Exercise 7**
**Printed:** Use elimination to solve...
System 1: RHS (6, 11, 3). System 2: RHS (7, 10, 3).

**Handwritten Notes:**
The system of equations can be rewritten as:
$\begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 2 & 3 & -4 \end{bmatrix} \begin{bmatrix} u \\ v \\ w \end{bmatrix} = \begin{bmatrix} 6 \\ 11 \\ 3 \end{bmatrix}$
by elimination we have:
Matrix reduction steps...
after back substitution we get: $(4, 1, 1)$.

The system of equations can be rewritten as:
Matrix with RHS $(7, 10, 3)$.
by elimination we have:
Matrix reduction steps...
after back substitution we get: $(1, 3, 2)$.

## Slide 8
**References**
Gilbert Strang. Introduction to Linear Algebra.
(Standard Citation text) -->