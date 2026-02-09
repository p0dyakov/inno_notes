Here is the complete, formatted transcript of the documents provided, organized by file and page.

---

# File 1: Problem Set 1

## Page 1
**Problem 1**

True or false (with a counterexample if false)?

(a) The vectors $b$ that are not in the column space $C(A)$ form a subspace.
(b) If $C(A)$ contains only the zero vector, then $A$ is the zero matrix.
(c) The column space of $2A$ equals the column space of $A$.
(d) The column space of $A - I$ equals the column space of $A$.

## Page 2
**Problem 2**

Give examples of matrices $A$ for which the number of solutions to $Ax = b$ is

(a) 0 or 1, depending on $b$.
(b) $\infty$, regardless of $b$.
(c) 0 or $\infty$, depending on $b$.
(d) 1, regardless of $b$.

## Page 3
**Problem 3**

For every $c$, find $R$ and the special solutions to $Ax = 0$:

$$
A = \begin{bmatrix} 
1 & 1 & 2 & 2 \\ 
2 & 2 & 4 & 4 \\ 
1 & c & 2 & 2 
\end{bmatrix} 
\quad \text{and} \quad 
A = \begin{bmatrix} 
1 - c & 2 \\ 
0 & 2 - c 
\end{bmatrix}.
$$

## Page 4
**Problem 4**

(a) If $Ax = b$ has two solutions $x_1$ and $x_2$, find two solutions to $Ax = 0$.
(b) Then find another solution to $Ax = b$.

## Page 5
**Problem 5**

What conditions on $b_1, b_2, b_3, b_4$ make each system solvable? *Solve for $x$:*

$$
\begin{bmatrix} 
1 & 2 \\ 
2 & 4 \\ 
2 & 5 \\ 
3 & 9 
\end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} 
= \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix}
\quad
\begin{bmatrix} 
1 & 2 & 3 \\ 
2 & 4 & 6 \\ 
2 & 5 & 7 \\ 
3 & 9 & 12 
\end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} 
= \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix}.
$$

## Page 6
**Problem 6**

Write the complete solutions $x = x_p + x_n$ to these systems, as in equation (4):

$$
\begin{bmatrix} 
1 & 2 & 2 \\ 
2 & 4 & 5 
\end{bmatrix}
\begin{bmatrix} u \\ v \\ w \end{bmatrix} 
= \begin{bmatrix} 1 \\ 4 \end{bmatrix}
\quad
\begin{bmatrix} 
1 & 2 & 2 \\ 
2 & 4 & 4 
\end{bmatrix}
\begin{bmatrix} u \\ v \\ w \end{bmatrix} 
= \begin{bmatrix} 1 \\ 4 \end{bmatrix}.
$$

**Complete solution**
$$
x = x_p + x_n \quad \Rightarrow \quad
x = \begin{bmatrix} u \\ v \\ w \\ y \end{bmatrix} 
= \begin{bmatrix} -2 \\ 0 \\ 1 \\ 0 \end{bmatrix} 
+ v \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} 
+ y \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}. \quad (4)
$$

## Page 7
**Problem 7**

Write a 2 by 2 system $Ax = b$ with many solutions $x_n$ but no solution $x_p$. (Therefore the system has no solution.) Which $b$'s allow an $x_p$?

## Page 8
**Problem 8**

The complete solution to $Ax = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$ is $x = \begin{bmatrix} 1 \\ 0 \end{bmatrix} + c \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Find $A$.

## Page 9
**Problem 9**

Find the echelon form $U$, the free variables, and the special solutions:

$$
A = \begin{bmatrix} 
0 & 1 & 0 & 3 \\ 
0 & 2 & 0 & 6 
\end{bmatrix}, 
\quad b = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}.
$$

$Ax = b$ is consistent (has a solution) when $b$ satisfies $b_2 = \_\_\_\_\_$. Find the complete solution in the same form as equation (4).

**Complete solution**
$$
x = x_p + x_n \quad \Rightarrow \quad
x = \begin{bmatrix} u \\ v \\ w \\ y \end{bmatrix} 
= \begin{bmatrix} -2 \\ 0 \\ 1 \\ 0 \end{bmatrix} 
+ v \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} 
+ y \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}. \quad (4)
$$
$x_{\text{complete}} = x_{\text{particular}} + x_{\text{nullspace}}$

## Page 10
**Problem 10**

If $A$ has rank $r$, then it has an $r$ by $r$ submatrix $S$ that is invertible. Find that submatrix $S$ from the pivot rows and pivot columns of each $A$:

$$
A = \begin{bmatrix} 
1 & 2 & 3 \\ 
1 & 2 & 4 
\end{bmatrix}
\quad
A = \begin{bmatrix} 
1 & 2 & 3 \\ 
2 & 4 & 6 
\end{bmatrix}
\quad
A = \begin{bmatrix} 
0 & 1 & 0 \\ 
0 & 0 & 0 \\ 
0 & 0 & 1 
\end{bmatrix}.
$$

---

# File 2: Textbook Sections

## Page 1
**Section 4.1**

**Task 35**
[M] Since
$$
\begin{bmatrix} 
8 & -4 & -7 & 9 \\ 
-4 & 3 & 6 & -4 \\ 
-3 & -2 & -5 & -4 \\ 
9 & -8 & -18 & 7 
\end{bmatrix}
\sim
\begin{bmatrix} 
1 & 0 & 0 & 1 \\ 
0 & 1 & 0 & -2 \\ 
0 & 0 & 1 & 1 \\ 
0 & 0 & 0 & 0 
\end{bmatrix},
$$
$\mathbf{w}$ is in the subspace spanned by $\{ \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$.

**Task 36**
[M] Since
$$
[A \quad \mathbf{y}] = 
\begin{bmatrix} 
3 & -5 & -9 & -4 \\ 
8 & 7 & -6 & -8 \\ 
-5 & -8 & 3 & 6 \\ 
2 & -2 & -9 & -5 
\end{bmatrix}
\sim
\begin{bmatrix} 
1 & 0 & 0 & -1/5 \\ 
0 & 1 & 0 & -2/5 \\ 
0 & 0 & 1 & 3/5 \\ 
0 & 0 & 0 & 0 
\end{bmatrix},
$$
$\mathbf{y}$ is in the subspace spanned by the columns of $A$.

## Page 2
**Section 4.2**

**Task 17**
The matrix $A$ is a $4 \times 2$ matrix. Thus
(a) Nul $A$ is a subspace of $\mathbb{R}^2$, and
(b) Col $A$ is a subspace of $\mathbb{R}^4$.

**Task 18**
The matrix $A$ is a $4 \times 3$ matrix. Thus
(a) Nul $A$ is a subspace of $\mathbb{R}^3$, and
(b) Col $A$ is a subspace of $\mathbb{R}^4$.

**Task 19**
The matrix $A$ is a $2 \times 5$ matrix. Thus
(a) Nul $A$ is a subspace of $\mathbb{R}^5$, and
(b) Col $A$ is a subspace of $\mathbb{R}^2$.

**Task 20**
The matrix $A$ is a $1 \times 5$ matrix. Thus
(a) Nul $A$ is a subspace of $\mathbb{R}^5$, and
(b) Col $A$ is a subspace of $\mathbb{R}^1 = \mathbb{R}$.

**Task 25**
**a.** True.
**b.** False.
**c.** True.
**d.** False.
**e.** True.
**f.** True.

**Task 26**
**a.** True.
**b.** True.
**c.** False.
**d.** True.
**e.** True.
**f.** True.

---

# File 3: Assignment Cover Sheet

## Page 1
**Analytical Geometry and Linear Algebra II**
**Assignment No.3**

**Book:** Linear Algebra and its Applications, 4th edition
**Author:** David Clay *[Note: Standard author is David Lay]*

**List of Exercises**

| Section | Exercise Number | Page |
| :--- | :--- | :--- |
| 4.1 | 35, 36 | 198 |
| 4.2 | 17, 18, 19, 20, 25, 26 | 206 |

---

# File 4: Task Questions

## Page 1
**Task 1**

Which pairs are orthogonal among the vectors $v_1, v_2, v_3, v_4$?

$$
v_1 = \begin{bmatrix} 1 \\ 2 \\ -2 \\ 1 \end{bmatrix}, \quad
v_2 = \begin{bmatrix} 4 \\ 0 \\ 4 \\ 0 \end{bmatrix}, \quad
v_3 = \begin{bmatrix} 1 \\ -1 \\ -1 \\ 1 \end{bmatrix}, \quad
v_4 = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}.
$$

## Page 2
**Task 2**

Project the vector $b$ onto the line through $a$. Check that $e$ is perpendicular to $a$:

$$
b = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix} \quad \text{and} \quad
a = \begin{bmatrix} -1 \\ -3 \\ -1 \end{bmatrix}.
$$

Here $e = b - p$.

## Page 3
**Task 3**

1.  **Basic:** Apply Gram-Schmidt to:
    $$
    \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad
    \mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}
    $$
2.  Find QR decomposition of:
    $$
    A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{bmatrix}
    $$
3.  Orthogonalize the following vectors in $\mathbb{R}^4$ and compute the corresponding QR decomposition of $A = [\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3]$:
    $$
    \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \quad
    \mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \quad
    \mathbf{v}_3 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}.
    $$

## Page 4
**Task 4**

Express the Gram-Schmidt orthogonalization of $a_1, a_2$ as $A = QR$:

$$
a_1 = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}, \quad
a_2 = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}.
$$

Given $n$ vectors $a_i$ with $m$ components, what are the shapes of $A$, $Q$, and $R$?

## Page 5
**Task 5**

From the nonorthogonal $a, b, c$, find orthonormal vectors $q_1, q_2, q_3$:

$$
a = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \quad
b = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad
c = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}.
$$

## Page 6
**Task 6**

Project the vector $b = (1, 1)$ onto the lines through $a_1 = (1, 0)$ and $a_2 = (1, 2)$. Draw the projections $p_1$ and $p_2$ and add $p_1 + p_2$. The projections do not add to $b$ because the $a$'s are not orthogonal.

## Page 7
**Task 7**

Which of the following subsets of $\mathbf{R}^3$ are actually subspaces?

(a) The plane of vectors $(b_1, b_2, b_3)$ with first component $b_1 = 0$.
(b) The plane of vectors $b$ with $b_1 = 1$.
(c) The vectors $b$ with $b_2b_3 = 0$ (this is the union of two subspaces, the plane $b_2 = 0$ and the plane $b_3 = 0$).
(d) All combinations of two given vectors $(1, 1, 0)$ and $(2, 0, 1)$.
(e) The plane of vectors $(b_1, b_2, b_3)$ that satisfy $b_3 - b_2 + 3b_1 = 0$.

## Page 8
**Task 8**

True or false for $\mathbf{M} =$ all 3 by 3 matrices (check addition using an example)?

(a) The skew-symmetric matrices in $\mathbf{M}$ (with $A^{\mathrm{T}} = -A$) form a subspace.
(b) The unsymmetric matrices in $\mathbf{M}$ (with $A^{\mathrm{T}} \neq A$) form a subspace.
(c) The matrices that have $(1, 1, 1)$ in their nullspace form a subspace.

---

# File 5: Gram-Schmidt Presentation Slides

## Page 1
**Gram-Schmidt Orthogonalization Process**

Salman Ahmadi-Asl
Innopolis University
February 6, 2026

*Footer:* Salman Ahmadi-Asl (Innopolis University) Gram-Schmidt Orthogonalization Process February 6, 2026 1 / 47

## Page 2
**Outline**

1. Vector Spaces and Subspaces
2. Introduction and Motivation
3. The Gram-Schmidt Process
4. QR Decomposition
5. Practice Problems
6. Proof of Orthonormality
7. Numerical Considerations

*Footer:* Salman Ahmadi-Asl (Innopolis University) Gram-Schmidt Orthogonalization Process February 6, 2026 2 / 47

## Page 3
**What is a Vector Space?**

**Definition**
A **vector space** $V$ over a field $\mathbb{F}$ (usually $\mathbb{R}$ or $\mathbb{C}$) is a set with two operations:
*   **Vector addition:** $+ : V \times V \to V$
*   **Scalar multiplication:** $\cdot : \mathbb{F} \times V \to V$

satisfying 8 axioms for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $a, b \in \mathbb{F}$.

**Addition axioms:**
1.  $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
2.  $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
3.  $\exists \mathbf{0} \in V : \mathbf{v} + \mathbf{0} = \mathbf{v}$
4.  $\forall \mathbf{v} \in V, \exists -\mathbf{v} : \mathbf{v} + (-\mathbf{v}) = \mathbf{0}$

**Scalar multiplication axioms:**
5.  $a(b\mathbf{v}) = (ab)\mathbf{v}$
6.  $1\mathbf{v} = \mathbf{v}$
7.  $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$
8.  $(a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$

## Page 4
**Examples of Vector Spaces**

**$\mathbb{R}^n$**
The classic $n$-dimensional real space:
$$
\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}
$$
with component-wise addition and scalar multiplication.

**Matrices $\mathbb{R}^{m \times n}$**
All $m \times n$ matrices:
$$
\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{pmatrix}
$$
with matrix addition and scalar multiplication.

## Page 5
**Examples of Vector Spaces**

**Polynomials $\mathcal{P}_n(\mathbb{R})$**
All polynomials of degree $\leq n$:
$$
a_0 + a_1x + a_2x^2 + \cdots + a_nx^n
$$
with polynomial addition and scalar multiplication.

**Continuous functions $C[a, b]$**
All continuous functions on $[a, b]$:
$$
\{f : [a, b] \to \mathbb{R} \mid f \text{ is continuous}\}
$$
with function addition and scalar multiplication.

## Page 6
**Inner Product Spaces**

**Definition**
An **inner product space** is a vector space $V$ equipped with an **inner product**:
$$
\langle \cdot, \cdot \rangle : V \times V \to \mathbb{F}
$$
satisfying for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $a \in \mathbb{F}$:
1.  **Conjugate symmetry:** $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$
2.  **Linearity in first argument:** $\langle a\mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = a\langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$
3.  **Positive-definiteness:** $\langle \mathbf{v}, \mathbf{v} \rangle \ge 0$, and $\langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$

## Page 7
**Standard Inner Products**

*   $\mathbb{R}^n: \langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x}^T \mathbf{y} = \sum_{i=1}^n x_i y_i$
*   $\mathbb{C}^n: \langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x}^* \mathbf{y} = \sum_{i=1}^n \overline{x}_i y_i$
*   $C[a, b]: \langle f, g \rangle = \int_a^b f(x)g(x)dx$

## Page 8
**What is a Subspace?**

**Definition**
A subset $W$ of a vector space $V$ is a **subspace** if $W$ is itself a vector space under the same operations as $V$.

*[Image Description: A diagram showing a large light blue circle labeled "Vector Space V" containing a smaller pink circle inside labeled "Subspace W".]*

## Page 9
**Key Insight**

A subspace is a "vector space within a vector space" - it inherits structure from the parent space.

## Page 10
**Subspace Test Theorem**

**Theorem (Subspace Test)**
A non-empty subset $W$ of a vector space $V$ is a subspace if and only if:
1.  **Closed under addition:** $\forall \mathbf{u}, \mathbf{v} \in W, \mathbf{u} + \mathbf{v} \in W$
2.  **Closed under scalar multiplication:**
    $\forall \mathbf{u} \in W, \forall c \in \mathbb{F}, c\mathbf{u} \in W$

## Page 11
**Proof.**

*   ($\Rightarrow$) If $W$ is a subspace, it must satisfy all vector space axioms, including closure.
*   ($\Leftarrow$) If $W$ is closed under addition and scalar multiplication:
    *   Commutativity, associativity, distributivity inherited from $V$
    *   Zero vector: $0\mathbf{u} = \mathbf{0} \in W$ (closure under scalar multiplication)
    *   Additive inverse: $(-1)\mathbf{u} = -\mathbf{u} \in W$ (closure under scalar multiplication)
*   All other axioms are inherited from $V$. $\square$

## Page 12
**Important**

You must check $W$ is non-empty! Often this is done by verifying $\mathbf{0} \in W$.

## Page 13
**Examples and Non-Examples of Subspaces**

**Subspaces of $\mathbb{R}^3$** (Green box)
*   The origin: $\{\mathbf{0}\}$
*   Any line through origin
*   Any plane through origin
*   The whole space $\mathbb{R}^3$

**NOT Subspaces of $\mathbb{R}^3$** (Red box)
*   A line not through origin
*   A plane not through origin
*   First octant: $\{(x, y, z) \mid x, y, z \ge 0\}$
    *   Closed under addition but NOT under scalar multiplication (multiply by -1)

## Page 14
**Examples and Non-Examples of Subspaces**

**Subspace of $\mathcal{P}_3(\mathbb{R})$** (Green box)
$W = \{p(x) \in \mathcal{P}_3 \mid p(0) = 0\}$
These are polynomials with zero constant term.

**NOT Subspaces of $\mathcal{P}_3(\mathbb{R})$** (Red box)
$W = \{p(x) \in \mathcal{P}_3 \mid p(0) = 1\}$
Zero polynomial not in $W$, and not closed under addition.

## Page 15
**Span of a set of columns as a vector space**

**Theorem**
If $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ are vectors in a vector space $V$, then
$$
W = \text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}
$$
is a subspace of $V$.

## Page 16
**Proof.**

Check the subspace test:
*   $\mathbf{0} \in W$ (zero vector can be written as $0\mathbf{v}_1$)
*   If $\mathbf{u}, \mathbf{v} \in W$, then $\mathbf{u} = \sum a_i \mathbf{v}_i$, $\mathbf{v} = \sum b_i \mathbf{v}_i$, so $\mathbf{u} + \mathbf{v} = \sum (a_i + b_i)\mathbf{v}_i \in W$
*   If $\mathbf{u} \in W$ and $c \in \mathbb{F}$, then $c\mathbf{u} = \sum (ca_i)\mathbf{v}_i \in W$ $\square$

## Page 17
**Span and Basis**

**Span**
The **span** of a set of vectors $S = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ is the set of all linear combinations:
$$
\text{span}(S) = \{a_1 \mathbf{v}_1 + \cdots + a_n \mathbf{v}_n \mid a_i \in \mathbb{F}\}
$$
This is always a subspace.

**Basis**
A **basis** for a subspace $W$ is a linearly independent set that spans $W$.
**Orthonormal basis:** A basis where all vectors are orthogonal and have unit length.

## Page 18
**Gram-Schmidt Creates Orthonormal Bases**

Input: Linearly independent vectors $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$
Output: Orthonormal basis $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ for $\text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$
Both sets span the **same subspace** of the original vector space!

## Page 19
**Why Orthogonalization?**

**The Problem**
Given a set of linearly independent vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}$, how can we construct an **orthonormal** set $\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}$ that spans the same subspace?

**Why Orthogonal Bases?**
*   **Easier computations:** Dot products simplify
*   **Numerical stability:** Less round-off error
*   **QR decomposition:** Fundamental matrix factorization
*   **Signal processing:** Remove correlations
*   **Least squares:** Efficient solutions

## Page 20
**Goal**

Transform $\{\mathbf{v}_1, \dots, \mathbf{v}_n\} \longrightarrow \{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ where:
$$
\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}
$$

## Page 21
**Preliminary Definitions**

**Orthogonal Vectors**
Vectors $\mathbf{u}$ and $\mathbf{v}$ are **orthogonal** if their dot product is zero:
$$
\mathbf{u} \cdot \mathbf{v} = 0
$$

**Orthonormal Set**
A set of vectors $\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}$ is **orthonormal** if:
$$
\mathbf{e}_i \cdot \mathbf{e}_j = \begin{cases} 0 & \text{if } i \neq j \\ 1 & \text{if } i = j \end{cases}
$$

## Page 22
**Formula for projection formula**

**Projection Formula**
The projection of vector $\mathbf{v}$ onto vector $\mathbf{u}$ is:
$$
\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\mathbf{u}
$$

## Page 23
**The Gram-Schmidt Process: Step-by-Step**

**Input**
Linearly independent vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}$

**1- First vector:**
$$
\mathbf{u}_1 = \mathbf{v}_1, \quad \mathbf{e}_1 = \frac{\mathbf{u}_1}{\|\mathbf{u}_1\|}
$$

**2- Second vector:**
$$
\mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{u}_1}(\mathbf{v}_2), \quad \mathbf{e}_2 = \frac{\mathbf{u}_2}{\|\mathbf{u}_2\|}
$$

**3- Third vector:**
$$
\mathbf{u}_3 = \mathbf{v}_3 - \text{proj}_{\mathbf{u}_1}(\mathbf{v}_3) - \text{proj}_{\mathbf{u}_2}(\mathbf{v}_3), \quad \mathbf{e}_3 = \frac{\mathbf{u}_3}{\|\mathbf{u}_3\|}
$$

## Page 24
**The Gram-Schmidt Process: Step-by-Step**

**4- Continue:** For $j = 4, \dots, n$:
$$
\mathbf{u}_j = \mathbf{v}_j - \sum_{i=1}^{j-1} \text{proj}_{\mathbf{u}_i}(\mathbf{v}_j), \quad \mathbf{e}_j = \frac{\mathbf{u}_j}{\|\mathbf{u}_j\|}
$$

## Page 25
**Example 1: Orthogonalization in $\mathbb{R}^2$**

Given: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 2 \\ 0 \end{bmatrix}$

**Step 1: First vector**
$$
\mathbf{u}_1 = \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$
$$
\|\mathbf{u}_1\| = \sqrt{1^2 + 1^2} = \sqrt{2}
$$
$$
\mathbf{e}_1 = \frac{\mathbf{u}_1}{\|\mathbf{u}_1\|} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

**Step 2: Projection**
$$
\mathbf{v}_2 \cdot \mathbf{u}_1 = 2 \cdot 1 + 0 \cdot 1 = 2
$$
$$
\|\mathbf{u}_1\|^2 = 2
$$
$$
\text{proj}_{\mathbf{u}_1}(\mathbf{v}_2) = \frac{2}{2} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

## Page 26
**Example 1: Orthogonalization in $\mathbb{R}^2$**

**Step 3: Second orthogonal vector**
$$
\mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{u}_1}(\mathbf{v}_2) = \begin{bmatrix} 2 \\ 0 \end{bmatrix} - \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$
$$
\|\mathbf{u}_2\| = \sqrt{1^2 + (-1)^2} = \sqrt{2}
$$
$$
\mathbf{e}_2 = \frac{\mathbf{u}_2}{\|\mathbf{u}_2\|} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

## Page 27
**Example 2: Orthogonalization in $\mathbb{R}^3$**

Given: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \mathbf{v}_3 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$

**Step 1: $\mathbf{u}_1$**
$$
\mathbf{u}_1 = \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \quad \|\mathbf{u}_1\| = \sqrt{2}, \quad \mathbf{e}_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}
$$

**Step 2: Project $\mathbf{v}_2$ on $\mathbf{u}_1$**
$$
\mathbf{v}_2 \cdot \mathbf{u}_1 = 1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0 = 1
$$
$$
\|\mathbf{u}_1\|^2 = 2, \quad \text{proj}_{\mathbf{u}_1}(\mathbf{v}_2) = \frac{1}{2} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.5 \\ 0 \end{bmatrix}
$$

## Page 28
**Step 3: $\mathbf{u}_2$**

$$
\mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{u}_1}(\mathbf{v}_2) = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} - \begin{bmatrix} 0.5 \\ 0.5 \\ 0 \end{bmatrix} = \begin{bmatrix} 0.5 \\ -0.5 \\ 1 \end{bmatrix}
$$
$$
\|\mathbf{u}_2\| = \sqrt{0.5^2 + (-0.5)^2 + 1^2} = \sqrt{1.5} = \frac{\sqrt{6}}{2}
$$
$$
\mathbf{e}_2 = \frac{2}{\sqrt{6}} \begin{bmatrix} 0.5 \\ -0.5 \\ 1 \end{bmatrix} = \frac{1}{\sqrt{6}} \begin{bmatrix} 1 \\ -1 \\ 2 \end{bmatrix}
$$

## Page 29
**Example 2 Continued**

Continuing with $\mathbf{v}_3$:

**Project $\mathbf{v}_3$ on $\mathbf{u}_1$**
$$
\mathbf{v}_3 \cdot \mathbf{u}_1 = 0 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 = 1
$$
$$
\text{proj}_{\mathbf{u}_1}(\mathbf{v}_3) = \frac{1}{2} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.5 \\ 0 \end{bmatrix}
$$

**Project $\mathbf{v}_3$ on $\mathbf{u}_2$**
$$
\mathbf{v}_3 \cdot \mathbf{u}_2 = 0 \cdot 0.5 + 1 \cdot (-0.5) + 1 \cdot 1 = 0.5
$$
$$
\|\mathbf{u}_2\|^2 = 1.5
$$
$$
\text{proj}_{\mathbf{u}_2}(\mathbf{v}_3) = \frac{0.5}{1.5} \begin{bmatrix} 0.5 \\ -0.5 \\ 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 0.5 \\ -0.5 \\ 1 \end{bmatrix} = \begin{bmatrix} 1/6 \\ -1/6 \\ 1/3 \end{bmatrix}
$$

## Page 30
**Projection of a vector to another vector**

**Step 4: $\mathbf{u}_3$**
$$
\mathbf{u}_3 = \mathbf{v}_3 - \text{proj}_{\mathbf{u}_1}(\mathbf{v}_3) - \text{proj}_{\mathbf{u}_2}(\mathbf{v}_3) = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} 0.5 \\ 0.5 \\ 0 \end{bmatrix} - \begin{bmatrix} 1/6 \\ -1/6 \\ 1/3 \end{bmatrix}
$$
$$
= \begin{bmatrix} 0 - 0.5 - 1/6 \\ 1 - 0.5 + 1/6 \\ 1 - 0 - 1/3 \end{bmatrix} = \begin{bmatrix} -2/3 \\ 2/3 \\ 2/3 \end{bmatrix}
$$

**Normalize $\mathbf{u}_3$**
$$
\|\mathbf{u}_3\| = \sqrt{(-2/3)^2 + (2/3)^2 + (2/3)^2} = \sqrt{12/9} = \frac{2}{\sqrt{3}}
$$
$$
\mathbf{e}_3 = \frac{\sqrt{3}}{2} \begin{bmatrix} -2/3 \\ 2/3 \\ 2/3 \end{bmatrix} = \frac{1}{\sqrt{3}} \begin{bmatrix} -1 \\ 1 \\ 1 \end{bmatrix}
$$

## Page 31
**QR Decomposition: Matrix Perspective**

**The QR Theorem**
Every $m \times n$ matrix $A$ with linearly independent columns can be factorized as:
$$
A = QR
$$
where:
*   $Q$ is an $m \times n$ matrix with orthonormal columns
*   $R$ is an $n \times n$ upper triangular matrix with positive diagonal entries

## Page 32
**QR Decomposition: Matrix Perspective**

**Example**
If $A = [\mathbf{v}_1 \mathbf{v}_2 \mathbf{v}_3]$, then Gram-Schmidt gives:
$$
\mathbf{v}_1 = r_{11}\mathbf{q}_1
$$
$$
\mathbf{v}_2 = r_{12}\mathbf{q}_1 + r_{22}\mathbf{q}_2
$$
$$
\mathbf{v}_3 = r_{13}\mathbf{q}_1 + r_{23}\mathbf{q}_2 + r_{33}\mathbf{q}_3
$$
So
$$
A = [\mathbf{q}_1 \mathbf{q}_2 \mathbf{q}_3] \begin{bmatrix} r_{11} & r_{12} & r_{13} \\ 0 & r_{22} & r_{23} \\ 0 & 0 & r_{33} \end{bmatrix} = QR
$$

## Page 33
**Example: QR Decomposition from Previous Example**

**From Example 2:**
$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \mathbf{v}_3 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}
$$

**We found:**
$$
\mathbf{e}_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \mathbf{e}_2 = \frac{1}{\sqrt{6}} \begin{bmatrix} 1 \\ -1 \\ 2 \end{bmatrix}, \mathbf{e}_3 = \frac{1}{\sqrt{3}} \begin{bmatrix} -1 \\ 1 \\ 1 \end{bmatrix}
$$

## Page 34
**Example: QR Decomposition from Previous Example**

**Construct $Q$ and $R$**
$$
Q = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{3}} \\ 0 & \frac{2}{\sqrt{6}} & \frac{1}{\sqrt{3}} \end{bmatrix}
$$
$$
R = \begin{bmatrix} \mathbf{e}_1 \cdot \mathbf{v}_1 & \mathbf{e}_1 \cdot \mathbf{v}_2 & \mathbf{e}_1 \cdot \mathbf{v}_3 \\ 0 & \mathbf{e}_2 \cdot \mathbf{v}_2 & \mathbf{e}_2 \cdot \mathbf{v}_3 \\ 0 & 0 & \mathbf{e}_3 \cdot \mathbf{v}_3 \end{bmatrix} = \begin{bmatrix} \sqrt{2} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ 0 & \frac{\sqrt{6}}{2} & \frac{1}{\sqrt{6}} \\ 0 & 0 & \frac{2}{\sqrt{3}} \end{bmatrix}
$$

**Verify:**
Compute $QR$ to check it equals $A = [\mathbf{v}_1 \mathbf{v}_2 \mathbf{v}_3]$

## Page 35
**Numerical Issues and Modified Gram-Schmidt**

**Problem with Classical Gram-Schmidt**
*   Round-off errors can accumulate
*   Loss of orthogonality in finite precision
*   Especially problematic for nearly linearly dependent vectors

**Modified Gram-Schmidt**
*   Numerically stable version
*   Same mathematical result
*   Different computational order
*   Subtracts projections one at a time

## Page 36
**Practice Problems**

1.  **Basic:** Apply Gram-Schmidt to:
    $$
    \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}
    $$
2.  Find QR decomposition of:
    $$
    A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{bmatrix}
    $$
3.  Orthogonalize the following vectors in $\mathbb{R}^4$ and compute the corresponding QR decomposition of $A = [\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3]$:
    $$
    \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \mathbf{v}_3 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}
    $$

## Page 37
**Solution Sketch for Problem 1**

**Step 1**
$$
\mathbf{u}_1 = \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad \|\mathbf{u}_1\| = \sqrt{2}, \quad \mathbf{e}_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
$$

**Step 2: Projection**
$$
\mathbf{v}_2 \cdot \mathbf{u}_1 = 1 \cdot 1 + 1 \cdot 0 + 0 \cdot 1 = 1, \quad \|\mathbf{u}_1\|^2 = 2
$$
$$
\text{proj}_{\mathbf{u}_1}(\mathbf{v}_2) = \frac{1}{2} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0 \\ 0.5 \end{bmatrix}
$$

## Page 38
**Solution Sketch for Problem 1**

**Step 3: Orthogonal vector**
$$
\mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{u}_1}(\mathbf{v}_2) = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} - \begin{bmatrix} 0.5 \\ 0 \\ 0.5 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 1 \\ -0.5 \end{bmatrix}
$$
$$
\|\mathbf{u}_2\| = \sqrt{0.5^2 + 1^2 + (-0.5)^2} = \sqrt{1.5} = \frac{\sqrt{6}}{2}
$$
$$
\mathbf{e}_2 = \frac{2}{\sqrt{6}} \begin{bmatrix} 0.5 \\ 1 \\ -0.5 \end{bmatrix} = \frac{1}{\sqrt{6}} \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}
$$

## Page 39
**Proof: Mathematical Induction Setup**

**Induction Hypothesis $P(k)$**
After $n$ steps of Gram-Schmidt:
1.  $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ are orthonormal
2.  $\text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_n\} = \text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$

**Proof Structure.**
We'll prove by induction on $n$:
*   **Base case:** $n=1$ (trivial)
*   **Inductive step:** Assume $P(n-1)$ holds, prove $P(n)$

## Page 40
**Base Case ($n=1$)**

**Normalization**
$$
\mathbf{e}_1 = \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}
$$

**Orthonormality:**
$$
\langle \mathbf{e}_1, \mathbf{e}_1 \rangle = \left\langle \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}, \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|} \right\rangle = \frac{\langle \mathbf{v}_1, \mathbf{v}_1 \rangle}{\|\mathbf{v}_1\|^2} = 1
$$

**Span preservation:**
$$
\text{span}\{\mathbf{e}_1\} = \text{span}\{\mathbf{v}_1\} \quad \text{(scaling doesn't change span)}
$$
✓ Base case verified.

## Page 41
**Inductive Step: Assume $P(n-1)$ Holds**

**Induction Assumption**
$\{\mathbf{e}_1, \dots, \mathbf{e}_{n-1}\}$ are orthonormal and
$$
\text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_{n-1}\} = \text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_{n-1}\}
$$

**Construct $\mathbf{e}_n$**
$$
\mathbf{w}_n = \mathbf{v}_n - \sum_{i=1}^{n-1} \langle \mathbf{v}_n, \mathbf{e}_i \rangle \mathbf{e}_i
$$
$$
\mathbf{e}_n = \frac{\mathbf{w}_n}{\|\mathbf{w}_n\|} \quad (\text{if } \mathbf{w}_n \neq \mathbf{0})
$$
**Note:** $\mathbf{w}_n \neq \mathbf{0}$ because $\mathbf{v}_n$ is linearly independent from $\{\mathbf{v}_1, \dots, \mathbf{v}_{n-1}\}$.

## Page 42
**Proof: $\mathbf{w}_n$ is Orthogonal to All $\mathbf{e}_i$ ($i < n$)**

Take any $j$ with $1 \le j \le n-1$:
$$
\langle \mathbf{w}_n, \mathbf{e}_j \rangle = \left\langle \mathbf{v}_n - \sum_{i=1}^{k-1} \langle \mathbf{v}_n, \mathbf{e}_i \rangle \mathbf{e}_i, \mathbf{e}_j \right\rangle
$$
$$
= \langle \mathbf{v}_n, \mathbf{e}_j \rangle - \sum_{i=1}^{n-1} \langle \mathbf{v}_n, \mathbf{e}_i \rangle \langle \mathbf{e}_i, \mathbf{e}_j \rangle
$$
$$
= \langle \mathbf{v}_n, \mathbf{e}_j \rangle - \langle \mathbf{v}_n, \mathbf{e}_j \rangle \quad (\text{since } \langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij} \text{ by induction})
$$
$$
= 0
$$

$\therefore \mathbf{w}_n \perp \mathbf{e}_j$ for all $j = 1, \dots, n-1$

## Page 43
**Proof: Span Preservation**

**We need to show:**
$$
\text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_n\} = \text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}
$$

1.  **From construction:**
    $$
    \mathbf{e}_n = \frac{1}{\|\mathbf{w}_n\|} \left( \mathbf{v}_n - \sum_{i=1}^{n-1} \langle \mathbf{v}_k, \mathbf{e}_i \rangle \mathbf{e}_i \right)
    $$
    So $\mathbf{e}_n \in \text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_{n-1}, \mathbf{v}_k\}$
2.  **By induction:** $\mathbf{e}_1, \dots, \mathbf{e}_{n-1} \in \text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_{n-1}\}$
3.  **Therefore:** $\text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_n\} \subseteq \text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$
4.  **Conversely, from construction:**
    $$
    \mathbf{v}_n = \|\mathbf{w}_n\|\mathbf{e}_n + \sum_{i=1}^{n-1} \langle \mathbf{v}_n, \mathbf{e}_i \rangle \mathbf{e}_i
    $$

## Page 44
So $\mathbf{v}_n \in \text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$
By induction: $\mathbf{v}_1, \dots, \mathbf{v}_{n-1} \in \text{span}\{\mathbf{e}_1, \dots, \mathbf{e}_{n-1}\}$
Therefore: $\text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\} \subseteq \text{span}\{\mathbf{u}_1, \dots, \mathbf{u}_n\}$
✓ Spans are equal!

## Page 45
**Completing the Induction**

**We have shown:**
1.  $\mathbf{e}_n$ is orthogonal to all previous $\mathbf{e}_i$ ($i < n$)
2.  $\|\mathbf{e}_n\| = 1$ (by normalization)
3.  The span is preserved

$$
\therefore P(n-1) \Rightarrow P(n)
$$

By mathematical induction, the Gram-Schmidt algorithm produces an orthonormal set $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ with the same span as $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$.

## Page 46
**Thank You!**

Questions?

*Footer:* Salman Ahmadi-Asl (Innopolis University) Gram-Schmidt Orthogonalization Process February 6, 2026 46 / 47

---

# File 6: Handwritten Solutions

## Page 1
**Task 1**

Which pairs are orthogonal among the following vectors:

$$
v_1 = \begin{bmatrix} 1 \\ 2 \\ -2 \\ 1 \end{bmatrix} \quad v_2 = \begin{bmatrix} 4 \\ 0 \\ 4 \\ 0 \end{bmatrix} \quad v_3 = \begin{bmatrix} 1 \\ -1 \\ -1 \\ 1 \end{bmatrix} \quad v_4 = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}
$$

[Handwritten text]:
**After computing the inner product of all the given vectors, we see that just the inner product between the following pairs is equal to zero:**

[Highlighted in purple and green circles]:
$$v_2 \cdot v_3 = (4)(1) + (0)(-1) + (4)(-1) + (0)(1) = 0$$

[Highlighted in green and blue circles]:
$$v_3 \cdot v_4 = (1)(1) + (-1)(1) + (-1)(1) + (1)(1) = 0$$

**therefore the pairs $v_2, v_3$ and $v_3, v_4$ are orthogonal.**

## Page 2
**Task 2**

[Image description: A diagram showing projection. A blue vector arrow labeled $b$ points up and right. An orange vector arrow labeled $a$ points right. A black dashed line drops from the tip of $b$ perpendicularly to $a$. The vector along $a$ up to this dashed line is labeled $p$ (projection). The vector connecting the tip of $p$ to the tip of $b$ is labeled $e = b-p$.]

$$
b = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix} \quad a = \begin{bmatrix} -1 \\ -3 \\ -1 \end{bmatrix}
$$

[Handwritten text]:
**The projection of $b$ onto $a$ is:**
$$p = \frac{a^Tb}{a^Ta} a = -\frac{11}{11} (-1, -3, -1)$$
$$p = (1, 3, 1)$$

**Finally:**
$$e = b - p$$
$$e = (1, 3, 1) - (1, 3, 1)$$
$$\boxed{e = (0, 0, 0)}$$

## Page 3
**Task 4**

Express the Gram-Schmidt orthogonalization of $a_1, a_2$ as $A = QR$.
$$
a_1 = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix} \quad a_2 = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}
$$

[Handwritten text]:
**Applying the Gram-Schmidt orthogonalization process we have:**

[Highlighted in green]:
$q_1 = a_1 = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}; \quad ||q_1|| = 3$

[Highlighted in blue]:
$q_2 = a_2 - \frac{a_1^T a_2}{a_1^T a_1} a_1 = \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix} - \frac{9}{9} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}; \quad ||q_2|| = \sqrt{2}$

**Our orthonormal set is:** $\{ \hat{q}_1, \hat{q}_2 \} = \{ \frac{1}{3} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}, \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \}$, **our Q matrix has the orthonormal vectors as columns, while the matrix $R = Q^T A$**

[Highlighted in yellow for Q and pink for R]:
$Q = \begin{pmatrix} 1/3 & 0 \\ 2/3 & 1/\sqrt{2} \\ 2/3 & -1/\sqrt{2} \end{pmatrix} \quad R = \begin{pmatrix} 1/3 & 2/3 & 2/3 \\ 0 & 1/\sqrt{2} & -1/\sqrt{2} \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 2 & 3 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 0 & \sqrt{2} \end{pmatrix}$

## Page 4
**Task 5**

[Handwritten text]:
**Applying the Gram-Schmidt method we get:**

[Highlighted in orange]:
$q_1 = a = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$

[Highlighted in blue]:
$q_2 = b - \frac{q_1^T b}{q_1^T q_1} q_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix}$

[Highlighted in purple]:
$q_3 = c - \frac{q_2^T c}{q_2^T q_2} q_2 - \frac{q_1^T c}{q_1^T q_1} q_1 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \frac{1/2}{6/4} \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$

$= \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \frac{1}{3} \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + \begin{pmatrix} \frac{1}{2} (-\frac{1}{3} - 1) \\ \frac{1}{2} (\frac{1}{3} - 1) \\ -\frac{1}{3} \end{pmatrix}$

$= \begin{pmatrix} -4/6 \\ 1 - 2/6 \\ 1 - 1/3 \end{pmatrix} = \begin{pmatrix} -2/3 \\ 2/3 \\ 2/3 \end{pmatrix} = \frac{2}{3} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$

[Highlighted in green]:
**Finally, to make the vectors orthonormal we divide them by their respective norms:**
$\{ \hat{q}_i = q_i / ||q_i|| \quad i=1,2,3 \}$

## Page 5
**Task 6**

Project the vector $b = (1, 1)$ onto the lines through $a_1 = (1, 0)$ and $a_2 = (1, 2)$. Draw the projections $p_1$ and $p_2$ and add $p_1 + p_2$. The projections do not add to $b$ because the $a$'s are not orthogonal.

[Image description: A hand-drawn coordinate system.
- An orange arrow $b$ points to $(1,1)$.
- A purple arrow $a_1$ lies on the x-axis.
- A blue arrow $a_2$ points steeply to $(1,2)$.
- A dashed orange line drops from $b$ to the x-axis, marking the projection $p_1$.
- Another projection line goes from $b$ onto $a_2$, marking $p_2$.
- A vector sum calculation is shown below.]

[Handwritten text]:
**Computing the projections we have:**

$p_1 = \frac{a_1^T b}{a_1^T a_1} a_1 = \frac{1}{1} (1, 0)$

$p_2 = \frac{a_2^T b}{a_2^T a_2} a_2 = \frac{3}{5} (1, 2)$

$\rightarrow \quad p_1 + p_2 = (\frac{8}{5}, \frac{6}{5})$

## Page 6
**Task 7**

[Blue sticky note titled "A quick reminder"]:
A subset $V$ of $\mathbb{R}^n$ is said to be a **subspace** if:
- The zero vector is in $V$
- If the sum of any elements in $V$ stays in $V$, this is: $v \in V$ and $w \in V$ implies $(v+w) \in V$ (as a new vector)
- If the scalar multiplication of any vector $(\alpha v) \in V$ as a new vector

(a) The plane vectors $(b_1, b_2, b_3)$ with $b_1 = b_2$.
[Handwritten text]:
Let $u=(x, x, z)$ and $v=(y, y, w)$ be vectors in that set.
- $u+v = (x, x, z) + (y, y, w) = (x+y, x+y, z+w)$ ✓
- $\alpha \in \mathbb{R}$ so $\alpha u = \alpha(x, x, z) = (\alpha x, \alpha x, \alpha z)$ ✓
- $(0,0,0)$ is in the set ✓
**It is!**

(b) The plane of vectors $(b_1, b_2, b_3)$ with $b_1 = 1$.
[Handwritten text]:
Let $u=(1, x, z)$ and $v=(1, y, w)$ be vectors in that set.
- $u+v = (1, x, z) + (1, y, w) = (2, x+y, z+w)$ X **It's not!**
**If one of the conditions fails don't mind checking the other ones, all the conditions must hold!**

(c) The vectors $(b_1, b_2, b_3)$ with $b_1 b_2 b_3 = 0$.
(Or check if you can provide a counterexample)
[Handwritten text]:
Consider the vectors $(0, 1, 1)$ and $(1, 0, 0)$, the product of their components is zero, **BUT** if you add them up then you get the vector $(1, 1, 1)$ and the product of its components is not zero.
**It's not!**

## Page 7
(d) All combinations of two given vectors $(1, 4, 0)$ and $(2, 2, 2)$.
[Handwritten text]:
**All combinations can be written as:**
$\alpha (1, 4, 0) + \beta (2, 2, 2) = (\alpha + 2\beta, 4\alpha + 2\beta, 2\beta)$
so let $u = (\alpha + 2\beta, 4\alpha + 2\beta, 2\beta)$ and $v = (\gamma + 2\delta, 4\gamma + 2\delta, 2\delta)$ be vectors in that set.
- $u+v = (\alpha + 2\beta, 4\alpha + 2\beta, 2\beta) + (\gamma + 2\delta, 4\gamma + 2\delta, 2\delta) = ((\alpha + \gamma) + 2(\beta + \delta), 4(\alpha + \gamma) + 2(\beta + \delta), 2(\beta + \delta))$ ✓
- $\eta \in \mathbb{R} \rightarrow \eta u = \eta(\alpha + 2\beta, 4\alpha + 2\beta, 2\beta) = (\eta(\alpha + 2\beta), \eta(4\alpha + 2\beta), \eta(2\beta))$ ✓
- set $\alpha$ and $\beta$ equal both to zero (**all combinations are allowed**), so we get: $(0,0,0)$ in the set.
**It is!**

(e) The plane of vectors $(b_1, b_2, b_3)$ that satisfy $b_1 + b_2 + b_3 = 0$.
[Handwritten text]:
Let $u$ and $v$ be vectors that satisfy the equation $b_1 + b_2 + b_3 = 0$ this means, $u_1 + u_2 + u_3 = 0$ and $v_1 + v_2 + v_3 = 0$ for $u$ and $v$ respectively.
- $u+v = (u_1, u_2, u_3) + (v_1, v_2, v_3) = (u_1 + v_1, u_2 + v_2, u_3 + v_3)$, which yields to: $(u_1 + v_1) + (u_2 + v_2) + (u_3 + v_3) = 0$ ✓
- let $\alpha \in \mathbb{R}$ then $\alpha u = \alpha(u_1, u_2, u_3) = (\alpha u_1, \alpha u_2, \alpha u_3)$ which conduces to $(\alpha u_1) + (\alpha u_2) + (\alpha u_3) = 0$ ✓
- The vector $(0,0,0)$ satisfies the equation of that plane, namely $(0) + (0) + (0) = 0$ so the zero is in the set. ✓
**It is!**

## Page 8
**Task 8**

(a) The skew-symmetric matrices (with $A^T = -A$) in $M$ form a subspace. **True**
[Handwritten text]:
- Let $B$ and $C$ be skew-symmetric matrices, therefore $B^T = -B$ and $A^T = -A$ [Correction: text says A, likely means C]. If we add them up we have
$A+B = -A^T - B^T = -(A^T + B^T) = -(A+B)^T \rightarrow -(A+B) = (A+B)^T$ ✓
- Let $\alpha \in \mathbb{R}$ then $\alpha A = \alpha (-A^T) = -\alpha A^T = -(\alpha A^T) = -(\alpha A)^T$, thus $\alpha (-A) = (\alpha A)^T$ ✓
- Let $C$ be the 3 by 3 zero matrix, $C^T$ is still the zero matrix and $-C$ is still the zero matrix. So the zero vector is in the set. ✓

(b) The unsymmetric matrices ($A^T \neq A$) in $M$ form a subspace. **False**
[Handwritten text]:
**Counterexample, consider the following 3 by 3 unsymmetric matrices:**
$\begin{pmatrix} 1 & 2 & 1 \\ 1 & 7 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix}$
if we add them up the result is symmetric:
$\begin{pmatrix} 1 & 2 & 1 \\ 1 & 7 & 1 \\ 0 & 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 8 & 2 \\ 1 & 2 & 1 \end{pmatrix} \leftarrow$ **it is a symmetric matrix!**

**True** [Note: The "True" likely belongs to the next question or is a mistake, the analysis concludes False].

## Page 9
(c) The matrices that have $(1, 1, 1)$ in their nullspace form a subspace.
[Handwritten text]:
[Blue sticky note titled "A quick reminder"]:
The nullspace (also called the kernel) of a matrix $A$ is the set of elements such that $Ax=0$.

- Let $B$ and $C$ be matrices such that
$\begin{pmatrix} b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23} \\ b_{31} & b_{32} & b_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$, $\begin{pmatrix} c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22} & c_{23} \\ c_{31} & c_{32} & c_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$
- If we add them up:
$\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = \left( \begin{pmatrix} b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23} \\ b_{31} & b_{32} & b_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right) + \left( \begin{pmatrix} c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22} & c_{23} \\ c_{31} & c_{32} & c_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right) =$
$= \begin{pmatrix} b_{11} + c_{11} & b_{12} + c_{12} & b_{13} + c_{13} \\ b_{21} + c_{21} & b_{22} + c_{22} & b_{23} + c_{23} \\ b_{31} + c_{31} & b_{32} + c_{32} & b_{33} + c_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$ ✓

- Let $\alpha \in \mathbb{R}$ then
$\alpha \begin{pmatrix} b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23} \\ b_{31} & b_{32} & b_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha b_{11} & \alpha b_{12} & \alpha b_{13} \\ \alpha b_{21} & \alpha b_{22} & \alpha b_{23} \\ \alpha b_{31} & \alpha b_{32} & \alpha b_{33} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$ ✓

- Let $D$ be the 3 by 3 matrix which has all its entries equal to zero, then
$\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$ ✓