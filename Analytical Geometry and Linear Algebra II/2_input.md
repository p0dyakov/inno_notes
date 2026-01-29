<!-- You are absolutely correct. I apologize for the oversight. I initially grouped the second and third PDFs together because they covered related topics, but looking at the source data, there are indeed **7 distinct PDF files**.

Here is the complete text again, correctly separated into **7 files**.

---

# File 1: Assignment No. 1

## Page 1
**Header:** Analytical Geometry and Linear Algebra II
**Assignment:** Assignment No.1
**Book:** Linear Algebra and its Applications, 4th edition
**Author:** David Clay

**Table: List of Exercises**

| Section | Exercise Number | Page |
| :--- | :--- | :--- |
| 2.1 | 1, 2, 7, 8, 9, 10 | 100 |
| 2.5 | 1, 2, 3, 4, 5 | 129 |

---

# File 2: Elementary Matrices: Right Multiplication

## Page 1
**Title:** Elementary Matrices: Right Multiplication
**Subtitle:** Column Operations Instead of Row Operations

**Key Principle**
When elementary matrices multiply $A$ from the **right**, they perform **column operations** instead of row operations:
*   Left multiplication: $EA$ performs row operations on $A$
*   Right multiplication: $AE$ performs column operations on $A$

**Example**
Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ and $E_{31}(2) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix}$.

Left multiplication (row operation):
$E_{31}(2)A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 9 & 12 & 15 \end{pmatrix}$
*(Note: Row 3 becomes Row 3 + 2 * Row 1)*

## Page 2
**Title:** Permutation Matrices: Right Multiplication
**Subtitle:** Column Swaps Instead of Row Swaps

For permutation matrix $P_{ij}$ that swaps rows $i$ and $j$:
*   **Left multiplication $P_{ij}A$:** Swaps **rows** $i$ and $j$ of $A$
*   **Right multiplication $AP_{ij}$:** Swaps **columns** $i$ and $j$ of $A$

**Example**
Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ and $P_{23} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$.

**Row swap:**
$P_{23}A = \begin{pmatrix} 1 & 2 & 3 \\ 7 & 8 & 9 \\ 4 & 5 & 6 \end{pmatrix}$

**Column swap:**
$AP_{23} = \begin{pmatrix} 1 & 3 & 2 \\ 4 & 6 & 5 \\ 7 & 9 & 8 \end{pmatrix}$

## Page 3
**Title:** Permutation Matrices: Right Multiplication
**Subtitle:** Column Swaps Instead of Row Swaps

**Important:** $P_{ij}^T = P_{ij}^{-1} = P_{ij}$, so $P_{ij}$ is both orthogonal and symmetric.

## Page 4
**Title:** Complete Pivoting: $PAQ$ Form
**Subtitle:** Both Row and Column Permutations

When we need both row and column exchanges (complete pivoting), we use:
$$PAQ = LU$$
where:
*   $P$ permutes rows (left multiplication)
*   $Q$ permutes columns (right multiplication)
*   $L$ is unit lower triangular
*   $U$ is upper triangular

## Page 5
**Title:** Complete Pivoting: $PAQ$ Form
**Example**
For $A = \begin{pmatrix} 0 & 2 & 1 \\ 2 & 1 & 0 \\ 1 & 0 & 3 \end{pmatrix}$:

**Step 1:** Swap rows 1 and 2: $P_{12}A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 3 \end{pmatrix}$

**Step 2:** Swap columns 1 and 2: $P_{12}AQ_{12} = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 0 & 1 \\ 0 & 1 & 3 \end{pmatrix}$

Now Gaussian elimination works: $P_{12}AQ_{12} = LU$.

## Page 6
**Title:** Why Column Operations Matter
**Subtitle:** Applications and Implications

**Symmetric Diagonalization**
For symmetric matrix $A$, if $P$ is a permutation matrix:
$PAP^T$ is also symmetric
because $(PAP^T)^T = (P^T)^T A^T P^T = PAP^T$.

**LU with Complete Pivoting**
The decomposition $PAQ = LU$ always exists for any square matrix $A$, even when:
*   $A$ has zero in all positions of a column
*   $A$ is singular (rank-deficient)

**Matrix Equivalence**
Two matrices $A$ and $B$ are **equivalent** if there exist invertible $P$ and $Q$ such that:
$B = PAQ$

## Page 7
**Title:** Practical Example: Solving $AX = B$
**Subtitle:** When Both Sides Need Permutations

Consider solving $AX = B$ where $A$ needs both row and column permutations:
$PAQ(Q^T X) = PB$

Let $Y = Q^T X$ (permuted solution), then:
$(PAQ)Y = PB$

Now compute $PAQ = LU$, and solve:
1.  $LY = PB$ (forward substitution)
2.  $UY = Z$ (back substitution)
3.  $X = QY$ (reverse column permutation)

**Example**
If $Q$ swaps columns 1 and 3, then $X = QY$ means:
$x_1 = y_3, \quad x_2 = y_2, \quad x_3 = y_1$

## Page 8
**Title:** Determinant with Column Permutations
**Subtitle:** How Permutations Affect Determinant

**Theorem**
For permutation matrix $P_{ij}$ and any square matrix $A$:
*   $\det(P_{ij}A) = -\det(A)$ (row swap)
*   $\det(AP_{ij}) = -\det(A)$ (column swap)
*   $\det(P_{ij}AP_{ij}) = \det(A)$ (simultaneous row/column swap)

**Proof.**
Since $\det(P_{ij}) = -1$ and $\det(AB) = \det(A)\det(B)$:
$\det(P_{ij}A) = \det(P_{ij})\det(A) = -\det(A)$
Similarly for column operations.

**Application:** In $PAQ = LU$,
$\det(A) = \det(P^{-1})\det(L)\det(U)\det(Q^{-1}) = \pm \prod u_{ii}$.

## Page 9
**Title:** Summary: Right vs Left Multiplication
**Subtitle:** Key Differences

| Operation | Left Multiply $EA$ | Right Multiply $AE$ |
| :--- | :--- | :--- |
| **Row swap $P_{ij}$** | Swaps rows $i$ and $j$ | Swaps columns $i$ and $j$ |
| **Row scale $D_i(\alpha)$** | Scales row $i$ by $\alpha$ | Scales column $i$ by $\alpha$ |
| **Row add $E_{ij}(\alpha)$** | Adds $\alpha \times$ row $j$ to row $i$ | Adds $\alpha \times$ col $i$ to col $j$ |
| **Effect on** | Row space | Column space |
| **Preserves** | Column relations | Row relations |
| **Use case** | Solving $Ax = b$ | Solving $xA = b$ |

**Important Special Case**
For symmetric matrices, we often use **symmetric permutations**:
$PAP^T$ (simultaneous row and column permutations)
This preserves symmetry and eigenvalue structure.

---

# File 3: Pivoting in Gaussian Elimination

## Page 1
**Title:** Pivoting in Gaussian Elimination
**Subtitle:** Why Pivoting is Essential

**The Problem with Naive Gaussian Elimination**
Without pivoting, elimination can fail or become numerically unstable when:
*   Pivot element $a_{kk} = 0$ (division by zero)
*   Pivot element $|a_{kk}|$ is very small (large round-off errors)
*   Ill-conditioned systems (sensitive to small changes)

**Example (Breakdown with Zero Pivot)**
$A = \begin{pmatrix} 0 & 2 & 3 \\ 1 & 4 & 5 \\ 2 & 1 & 6 \end{pmatrix}$
First step: $R_2 \leftarrow R_2 - (1/0)R_1$ fails!

## Page 2
**Title:** Pivoting in Gaussian Elimination
**Subtitle:** Why Pivoting is Essential

**Solution: Pivoting**
Swap rows (and possibly columns) to place a "good" pivot in position $(k, k)$.

## Page 3
**Title:** Partial Pivoting
**Subtitle:** Row Exchanges Only

**Algorithm**
At step $k$ of elimination:
1.  Find index $p$ such that $|a_{pk}| = \max_{i \ge k} |a_{ik}|$
2.  Swap rows $k$ and $p$ (using permutation matrix $P$)
3.  Continue elimination

**Example (Partial Pivoting Example)**
$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 0.001 & 3 & 7 \end{pmatrix}$
Step 1: Column 1: $\max(|1|, |2|, |0.001|) = 2$ at row 2
Swap rows 1 and 2:
$\begin{pmatrix} 2 & 4 & 5 \\ 1 & 2 & 3 \\ 0.001 & 3 & 7 \end{pmatrix}$

## Page 4
**Title:** Complete Pivoting
**Subtitle:** Row and Column Exchanges

**Algorithm**
At step $k$ of elimination:
1.  Find indices $(p, q)$ such that $|a_{pq}| = \max_{i,j \ge k} |a_{ij}|$
2.  Swap rows $k$ and $p$ (using $P$)
3.  Swap columns $k$ and $q$ (using $Q$)
4.  Continue elimination

## Page 5
**Title:** Complete Pivoting
**Subtitle:** Row and Column Exchanges

**Example (Complete Pivoting Example)**
$A = \begin{pmatrix} 1 & 2 & 100 \\ 2 & 4 & 5 \\ 3 & 6 & 7 \end{pmatrix}$
Step 1: Largest entry in entire matrix is $a_{13} = 100$
*   Swap rows? Not needed (already in first row)
*   Swap columns 1 and 3: $AQ_{13} = \begin{pmatrix} 100 & 2 & 1 \\ 5 & 4 & 2 \\ 7 & 6 & 3 \end{pmatrix}$
Now $a_{11} = 100$ is the largest possible pivot.

## Page 6
**Title:** Numerical Stability Comparison
**Subtitle:** Why Complete Pivoting is More Stable

**Growth Factor**
Define growth factor: $\rho = \frac{\max_{i,j} |a_{ij}^{(k)}|}{\max_{i,j} |a_{ij}|}$
*   **No pivoting:** $\rho$ can be as large as $2^{n-1}$ (exponential!)
*   **Partial pivoting:** $\rho \le 2^{n-1}$ (still exponential in worst case)
*   **Complete pivoting:** $\rho \le n^{1/2} (2 \cdot 3^{1/2} \cdots n^{1/(n-1)}) \sim O(n^{\frac{1}{2} \log n})$

**Example (Wilkinson’s Famous Example)**
For $n = 20$, partial pivoting gives $\rho \approx 2^{19} \approx 5 \times 10^5$, while complete pivoting gives $\rho \approx 20$.

## Page 7
**Title:** Numerical Stability Comparison
**Subtitle:** Why Complete Pivoting is More Stable

**Practical Advice**
*   Partial pivoting is usually sufficient
*   Complete pivoting is more expensive ($O(n^3)$ search vs $O(n^2)$)

Use complete pivoting for:
*   Ill-conditioned matrices
*   Rank-deficient matrices
*   When high accuracy is critical

## Page 8
**Title:** LU Decomposition with Pivoting
**Subtitle:** $PA = LU$ vs $PAQ = LU$

**Partial Pivoting: $PA = LU$**
$PA = LU$
*   $P$: permutation matrix (row swaps only)
*   $L$: unit lower triangular, $|l_{ij}| \le 1$
*   $U$: upper triangular
*   Always exists for invertible $A$

## Page 9
**Title:** LU Decomposition with Pivoting
**Subtitle:** $PA = LU$ vs $PAQ = LU$

**Complete Pivoting: $PAQ = LU$**
$PAQ = LU$
*   $P, Q$: permutation matrices (row and column swaps)
*   $L$: unit lower triangular
*   $U$: upper triangular
*   Always exists for any $A$ (even singular)
*   More numerically stable

**Cost:** Partial pivoting adds $O(n^2)$ comparisons, complete pivoting adds $O(n^3)$ comparisons.

## Page 10
**Title:** MATLAB/NumPy Comparison
**Subtitle:** Implementation in Practice

**MATLAB**
*   Partial pivoting (default): `[L, U, P] = lu(A); P*A = L*U`
*   Complete pivoting: `[L, U, P, Q] = lu(A, 'vector');`

**Python NumPy/SciPy**
*   `P, L, U = lu(A)` implies $A = P @ L @ U$ (from `scipy.linalg import lu` Partial pivoting)

**Key Difference**
MATLAB returns $P$ such that $PA = LU$, while SciPy returns $P$ such that $A = PLU$.

## Page 11
**Title:** Special Cases and Considerations
**Subtitle:** When to Use Which Method

**When Partial Pivoting Suffices**
*   Most well-conditioned problems
*   Diagonally dominant matrices
*   Symmetric positive definite matrices (no pivoting needed!)
*   Applications where speed is more important than maximum accuracy

**When Complete Pivoting is Needed**
*   Ill-conditioned matrices ($\kappa(A) \gg 1$)
*   Rank-deficient matrices (determining rank)
*   Computing matrix rank or null space
*   When backward stability is critical
*   Sparse matrices with unusual structure

## Page 12
**Title:** When Partial Pivoting Suffices
**Subtitle:** Rook Pivoting (Compromise)

Search both row and column but stop at first "sufficiently large" element.
*   Almost as stable as complete pivoting
*   Lower cost: $O(n^2)$ expected time
*   Used in some sparse solvers

## Page 13
**Title:** Summary: Partial vs Complete Pivoting
**Subtitle:** Key Differences

| | Partial | Complete |
| :--- | :--- | :--- |
| **Op** | Row swaps | Row + col swaps |
| **Search** | Col: $O(n)$ | Matrix: $O(n^2)$ |
| **Cost** | $+O(n^2)$ | $+O(n^3)$ |
| **Stability** | Usually OK | Best |
| **Growth** | $\le 2^{n-1}$ | $\sim O(n^{\log n})$ |
| **Form** | $PA = LU$ | $PAQ = LU$ |
| **Use** | Default | Ill-conditioned |
| **Solve** | $x = U^{-1}L^{-1}Pb$ | $x = Q(U^{-1}L^{-1}Pb)$ |

**Modern Practice**
*   Partial pivoting is the **default** in almost all linear algebra packages
*   Complete pivoting is used for **specialized applications**
*   **Rook pivoting** offers a good compromise for difficult problems
*   For **symmetric** matrices, specialized pivoting strategies exist

---

# File 4: Task Solutions

## Page 1: Section 2.1
**Task 1**
1. $-2A = (-2)\begin{bmatrix} 2 & 0 & -1 \\ 4 & -5 & 2 \end{bmatrix} = \begin{bmatrix} -4 & 0 & 2 \\ -8 & 10 & -4 \end{bmatrix}$. Next, use $B - 2A = B + (-2A)$:
$B - 2A = \begin{bmatrix} 7 & -5 & 1 \\ 1 & -4 & -3 \end{bmatrix} + \begin{bmatrix} -4 & 0 & 2 \\ -8 & 10 & -4 \end{bmatrix} = \begin{bmatrix} 3 & -5 & 3 \\ -7 & 6 & -7 \end{bmatrix}$
The product $AC$ is not defined because the number of columns of $A$ does not match the number of rows of $C$.
$CD = \begin{bmatrix} 1 & 2 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 3 & 5 \\ -1 & 4 \end{bmatrix} = \begin{bmatrix} 1 \cdot 3 + 2(-1) & 1 \cdot 5 + 2 \cdot 4 \\ -2 \cdot 3 + 1(-1) & -2 \cdot 5 + 1 \cdot 4 \end{bmatrix} = \begin{bmatrix} 1 & 13 \\ -7 & -6 \end{bmatrix}$.

**Task 2**
2. $A + 3B = \begin{bmatrix} 2 & 0 & -1 \\ 4 & -5 & 2 \end{bmatrix} + 3\begin{bmatrix} 7 & -5 & 1 \\ 1 & -4 & -3 \end{bmatrix} = \begin{bmatrix} 2+21 & 0-15 & -1+3 \\ 4+3 & -5-12 & 2-9 \end{bmatrix} = \begin{bmatrix} 23 & -15 & 2 \\ 7 & -17 & -7 \end{bmatrix}$
The expression $2C - 3E$ is not defined because $2C$ has 2 columns and $-3E$ has only 1 column.
$DB = \begin{bmatrix} 3 & 5 \\ -1 & 4 \end{bmatrix}\begin{bmatrix} 7 & -5 & 1 \\ 1 & -4 & -3 \end{bmatrix} = \begin{bmatrix} 3(7)+5(1) & 3(-5)+5(-4) & 3(1)+5(-3) \\ -1(7)+4(1) & -1(-5)+4(-4) & -1(1)+4(-3) \end{bmatrix} = \begin{bmatrix} 26 & -35 & -12 \\ -3 & -11 & -13 \end{bmatrix}$
The product $EC$ is not defined because the number of columns of $E$ does not match the number of rows of $C$.

**Task 7**
7. Since $A$ has 3 columns, $B$ must match with 3 rows. Otherwise, $AB$ is undefined. Since $AB$ has 7 columns, so does $B$. Thus, $B$ is $3 \times 7$.

**Task 8**
8. The number of rows of $B$ matches the number of rows of $BC$, so $B$ has 5 rows.

**Task 9**
9. $AB = \begin{bmatrix} 2 & 3 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 9 \\ -3 & k \end{bmatrix} = \begin{bmatrix} -7 & 18+3k \\ -4 & -9+k \end{bmatrix}$, while $BA = \begin{bmatrix} 1 & 9 \\ -3 & k \end{bmatrix} \begin{bmatrix} 2 & 3 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} -7 & 12 \\ -6-k & -9+k \end{bmatrix}$.
Then $AB=BA$ if and only if $18+3k=12$ and $-4=-6-k$, which happens if and only if $k=-2$.

**Task 10**
10. $AB = \begin{bmatrix} 3 & -6 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} -1 & 1 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} -21 & -21 \\ 7 & 7 \end{bmatrix}$, $AC = \begin{bmatrix} 3 & -6 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} -3 & -5 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} -21 & -21 \\ 7 & 7 \end{bmatrix}$

## Page 2: Section 2.5
**Task 1**
1. $L = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 2 & -5 & 1 \end{bmatrix}, U = \begin{bmatrix} 3 & -7 & -2 \\ 0 & -2 & -1 \\ 0 & 0 & -1 \end{bmatrix}, \mathbf{b} = \begin{bmatrix} -7 \\ 5 \\ 2 \end{bmatrix}$. First, solve $L\mathbf{y} = \mathbf{b}$.
$[L \ \mathbf{b}] = \begin{bmatrix} 1 & 0 & 0 & -7 \\ -1 & 1 & 0 & 5 \\ 2 & -5 & 1 & 2 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 0 & -7 \\ 0 & 1 & 0 & -2 \\ 0 & -5 & 1 & 16 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 0 & -7 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 6 \end{bmatrix}$, so $\mathbf{y} = \begin{bmatrix} -7 \\ -2 \\ 6 \end{bmatrix}$.
Next, solve $U\mathbf{x} = \mathbf{y}$, using back-substitution.
$[U \ \mathbf{y}] = \begin{bmatrix} 3 & -7 & -2 & -7 \\ 0 & -2 & -1 & -2 \\ 0 & 0 & -1 & 6 \end{bmatrix} \sim \dots \sim \begin{bmatrix} 1 & 0 & 0 & 3 \\ 0 & 1 & 0 & 4 \\ 0 & 0 & 1 & -6 \end{bmatrix}$. So $\mathbf{x} = \begin{bmatrix} 3 \\ 4 \\ -6 \end{bmatrix}$.

## Page 3: Section 2.5 (continued)
**Task 2**
2. $L = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}, U = \begin{bmatrix} 2 & -6 & 4 \\ 0 & -4 & 8 \\ 0 & 0 & -2 \end{bmatrix}, \mathbf{b} = \begin{bmatrix} 2 \\ -4 \\ 6 \end{bmatrix}$. First solve $L\mathbf{y}=\mathbf{b}$:
$[L \ \mathbf{b}] \sim \dots \sim \mathbf{y} = \begin{bmatrix} 2 \\ 0 \\ 6 \end{bmatrix}$.
Next solve $U\mathbf{x}=\mathbf{y}$:
$[U \ \mathbf{y}] = \begin{bmatrix} 2 & -6 & 4 & 2 \\ 0 & -4 & 8 & 0 \\ 0 & 0 & -2 & 6 \end{bmatrix} \sim \dots \sim \begin{bmatrix} 1 & 0 & 0 & -11 \\ 0 & 1 & 0 & -6 \\ 0 & 0 & 1 & -3 \end{bmatrix}$, so $\mathbf{x} = \begin{bmatrix} -11 \\ -6 \\ -3 \end{bmatrix}$.

## Page 4: Section 2.5 (continued)
**Task 3**
3. $L = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 3 & -1 & 1 \end{bmatrix}, U = \begin{bmatrix} 2 & -4 & 2 \\ 0 & -3 & 6 \\ 0 & 0 & 1 \end{bmatrix}, \mathbf{b} = \begin{bmatrix} 6 \\ 0 \\ 6 \end{bmatrix}$. First solve $L\mathbf{y}=\mathbf{b}$:
$[L \ \mathbf{b}] \sim \dots \sim \mathbf{y} = \begin{bmatrix} 6 \\ 12 \\ 0 \end{bmatrix}$.
Next solve $U\mathbf{x}=\mathbf{y}$:
$[U \ \mathbf{y}] = \begin{bmatrix} 2 & -4 & 2 & 6 \\ 0 & -3 & 6 & 12 \\ 0 & 0 & 1 & 0 \end{bmatrix} \sim \dots \sim \begin{bmatrix} 1 & 0 & 0 & -5 \\ 0 & 1 & 0 & -4 \\ 0 & 0 & 1 & 0 \end{bmatrix}$, so $\mathbf{x} = \begin{bmatrix} -5 \\ -4 \\ 0 \end{bmatrix}$.

**Task 4**
4. $L = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 3 & -5 & 1 \end{bmatrix}, U = \begin{bmatrix} 1 & -1 & 2 \\ 0 & -2 & -1 \\ 0 & 0 & -6 \end{bmatrix}, \mathbf{b} = \begin{bmatrix} 0 \\ -5 \\ 7 \end{bmatrix}$. First solve $L\mathbf{y}=\mathbf{b}$:
$[L \ \mathbf{b}] \sim \dots \sim \mathbf{y} = \begin{bmatrix} 0 \\ -5 \\ -18 \end{bmatrix}$.
Next solve $U\mathbf{x}=\mathbf{y}$:
$[U \ \mathbf{y}] = \begin{bmatrix} 1 & -1 & 2 & 0 \\ 0 & -2 & -1 & -5 \\ 0 & 0 & -6 & -18 \end{bmatrix} \sim \dots \sim \begin{bmatrix} 1 & 0 & 0 & -5 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 3 \end{bmatrix}$, so $\mathbf{x} = \begin{bmatrix} -5 \\ 1 \\ 3 \end{bmatrix}$.

## Page 5: Section 2.5 (continued)
**Task 5**
5. $L = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 3 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ -3 & 4 & -2 & 1 \end{bmatrix}, U = \begin{bmatrix} 1 & -2 & -2 & -3 \\ 0 & -3 & 6 & 0 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 0 & 1 \end{bmatrix}, \mathbf{b} = \begin{bmatrix} 1 \\ 6 \\ 0 \\ 3 \end{bmatrix}$. First solve $L\mathbf{y}=\mathbf{b}$:
$[L \ \mathbf{b}] \sim \dots \sim \mathbf{y} = \begin{bmatrix} 1 \\ 3 \\ 1 \\ -4 \end{bmatrix}$.
Next solve $U\mathbf{x}=\mathbf{y}$:
$[U \ \mathbf{y}] \sim \dots \sim \begin{bmatrix} 1 & 0 & 0 & 0 & 38 \\ 0 & 1 & 0 & 0 & 16 \\ 0 & 0 & 1 & 0 & 17/2 \\ 0 & 0 & 0 & 1 & -4 \end{bmatrix}$, so $\mathbf{x} = \begin{bmatrix} 38 \\ 16 \\ 17/2 \\ -4 \end{bmatrix}$.

---

# File 5: LU and LDU Decomposition (Lecture Slides)

## Slide 1
**Title:** LU and LDU Decomposition
**Author:** Salman Ahmadi-Asl
**Affiliation:** Innopolis University
**Date:** January 27, 2026

## Slide 2
**Outline**
1. Motivation: Solving Triangular Systems
2. Elementary Matrices for Row Operations
3. Gaussian Elimination as LU Decomposition
4. Efficiency of LU Decomposition
5. Pivoting and $PA = LU$
6. Formal Definitions
7. Special Cases: $LDU$, $LDL^T$, and $LL^T$

## Slide 3
**Triangular Systems are Easy to Solve**
**Upper Triangular System**
For $Ux = b$ where $U$ is upper triangular.
**Backward substitution:** $x_n = b_n/u_{nn}$, $x_{n-1} = (b_{n-1} - u_{n-1,n}x_n)/u_{n-1,n-1}$, etc.

## Slide 4
**Triangular Systems are Easy to Solve**
**Lower Triangular System**
For $Lx = b$ where $L$ is lower triangular.
**Forward substitution:** $x_1 = b_1/l_{11}$, $x_2 = (b_2 - l_{21}x_1)/l_{22}$, etc.

## Slide 5
**Row Operations as Matrix Multiplications**
**Definition:** An elementary matrix is obtained by performing a single elementary row operation on an identity matrix.
**1- Row swap:** $P_{ij}$ swaps rows $i$ and $j$.
Example: $P_{23}$ (Image of 4x4 matrix swapping rows 2 and 3).

## Slide 6
**Row Operations as Matrix Multiplications**
**2- Row scaling:** $D_i(\alpha)$ multiplies row $i$ by $\alpha$.
**3- Row addition:** $E_{ij}(\alpha)$ adds $\alpha$ times row $j$ to row $i$.

## Slide 7
**Row Operations as Matrix Multiplications: Examples**
*   **Row Swap $P_{ij}$**: Example of $P_{13}$ (3x3) and $P_{24}$ (4x4). Verification shown multiplying by generic matrix $A$.

## Slide 8
**Row Operations as Matrix Multiplications: Examples**
*   **Row Scaling $D_i(\alpha)$**: Example of $D_2(-4)$ and $D_3(1/2)$. Verification shown.

## Slide 9
**Row Operations as Matrix Multiplications: Examples**
*   **Row Addition $E_{ij}(\alpha)$**: Example of $E_{31}(3)$ and $E_{42}(-2)$. Verification shown.

## Slide 10
**Elementary Matrices in Action**
**Sequence of Operations Example**
Goal: Transform $A = \begin{bmatrix} 0 & 2 \\ 1 & 3 \end{bmatrix}$ to $I_2$.
1. Swap rows 1 and 2: $P_{12}$.
2. Scale row 2 by $1/2$: $D_2(1/2)$.
3. Add -3 times row 2 to row 1: $E_{12}(-3)$.
Equation: $E_{12}(-3)D_2(1/2)P_{12}A = I_2$.

## Slide 11
**Elementary Matrices in Action**
Calculation of $A^{-1}$ using the product of the elementary matrices derived in the previous slide:
$A^{-1} = \begin{bmatrix} -1.5 & 1 \\ 0.5 & 0 \end{bmatrix}$.

## Slide 12
**Inverses of Elementary Matrices**
*   $P_{ij}^{-1} = P_{ij}$
*   $D_i(\alpha)^{-1} = D_i(1/\alpha)$
*   $E_{ij}(\alpha)^{-1} = E_{ij}(-\alpha)$
Examples shown for $E_{31}$ and $D_2$.

## Slide 13
**Inverses of Elementary Matrices**
Example: Permutation matrix $P_{23}$. $P_{23}P_{23} = I$, so $P_{23}^{-1} = P_{23}$.

## Slide 14
**From Gaussian Elimination to LU Decomposition**
Step-by-step example reducing matrix $A$ to $U$ using row operations ($E_{21}, E_{31}, E_{32}$).

## Slide 15
**Extracting L**
The equation $E_{32}E_{31}E_{21}A = U$ implies $A = (E_{21}^{-1}E_{31}^{-1}E_{32}^{-1})U$.
The product of inverses forms $L$.
Shown: $A = L U$.

## Slide 16
**Why LU Decomposition is Efficient**
Comparing Naive approach (Gaussian elimination $k$ times) vs LU approach (Factor once, solve $k$ times).
*   **GE:** $k \cdot \frac{2}{3}n^3$
*   **LU:** $\frac{2}{3}n^3 + k \cdot 2n^2$
Savings are significant for $k \gg 1$.

## Slide 17
**Example: Solving Multiple Systems**
Numerical example solving $Ax=b_1$ and $Ax=b_2$ using the LU factors.

## Slide 18
**Example: Solving Multiple Systems (Complexity)**
If $n=1000$ and 1000 different $b$ vectors:
*   LU: ~2.67 billion flops.
*   Gaussian Elimination each time: ~667 billion flops.

## Slide 19
**When Gaussian Elimination Fails**
Example of a zero pivot. Solution: Permutation Matrix (Row swap).

## Slide 20-22
**LU Decomposition with Elementary Matrices (Step-by-step)**
Detailed derivation of $L$ and $U$ for a specific matrix using elementary matrices and tracking the multipliers.

## Slide 23
**Verification**
Checking $P_{12}A = LU$.

## Slide 24
**Pivoting**
Partial Pivoting ($PA = LU$) vs Complete Pivoting ($PAQ = LU$).

## Slide 25
**Formal Definition of LU Decomposition**
$A = LU$ where $L$ is lower triangular, $U$ is upper triangular.

## Slide 26
**Alternative Definition**
Specifying that $L$ has 1's on the diagonal (Unit lower triangular).

## Slide 27
**Why 1's on the Diagonal of L?**
1. Uniqueness.
2. Natural Interpretation (correspond to Identity in elementary matrices).
3. Gaussian Elimination mechanics.

## Slide 28
**Mathematical Justification**
Theorem: Uniqueness of Unit Triangular LU. Proof provided.

## Slide 29
**Practical Example: Non-Uniqueness**
Showing multiple valid LU decompositions if the diagonal of L is not fixed.

## Slide 30-31
**Leading Principal Minors**
Definition and example calculation of $M_k$.

## Slide 32
**Formal Definition**
Theorem: An invertible matrix $A$ has an LU decomposition if and only if all its leading principal minors are nonzero.

## Slide 33
**Example: When LU Fails**
Matrix $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ is invertible but $M_1 = 0$, so standard LU fails.

## Slide 34
**Uniqueness Theorems with Pivoting**
*   $PA = LU$ exists for any invertible $A$.
*   $P$ is not unique, but once $P$ is fixed, $L$ and $U$ are unique.

## Slide 35
**Theorem (Complete Pivoting)**
$PAQ = LU$ exists for any invertible matrix.

## Slide 36
**LDU and Related Decompositions**
*   $A = LDU_0$ (Factor out diagonal from $U$).
*   Symmetric Matrices: $A = LDL^T$.

## Slide 37-38
**Example: From LU to LDU to LDL^T**
Step-by-step numerical example converting matrices.

## Slide 39-41
**More Examples**
Symmetric $LDL^T$ examples (including nonsymmetric case showing $U_0^T \neq L$).

## Slide 42-44
**Symmetric Positive Definite (SPD) Matrices**
Definition ($x^T Ax > 0$). Sylvester's Criterion (all leading principal minors > 0).

## Slide 45
**Cholesky Decomposition**
For SPD matrices: $A = LL^T$ (where $L$ has positive diagonal entries).

## Slide 46
**Why Special Cases Matter**
*   $LDL^T$: Storage efficiency, symmetry preservation.
*   Cholesky: Efficiency ($1/3 n^3$), stability (no pivoting needed), square roots.

## Slide 47
**Summary**
Recap of LU, Pivoting, Symmetry, and Special Cases.

---

# File 6: Elementary Matrices (Short Deck)

## Slide 1
**Definition**
An elementary matrix is obtained by performing a single elementary row operation on an identity matrix. Three types.

## Slide 2-4
**Types of Elementary Matrices**
1.  **Row Swapping ($P_{ij}$):** Symmetric, self-inverse, det = -1.
2.  **Row Scaling ($D_i(\alpha)$):** Diagonal, inverse scales by $1/\alpha$, det = $\alpha$.
3.  **Row Addition ($E_{ij}(\alpha)$):** Triangular, inverse adds $-\alpha$, det = 1.

## Slide 5
**Fundamental Theorem**
Every invertible matrix can be expressed as a product of elementary matrices: $A = E_1 E_2 \cdots E_k$.
Inverse: $A^{-1} = E_k^{-1} \cdots E_1^{-1}$.

## Slide 6
**Matrix Inversion via Elementary Matrices**
Gauss-Jordan elimination $[A|I] \to [I|B]$ means $B = A^{-1}$.
Example calculation shown.

## Slide 7-8
**LU Decomposition via Elementary Matrices**
$A = E_1^{-1} \dots E_k^{-1} U = LU$.
Example calculation shown.

## Slide 9
**Determinant of Elementary Matrices**
Rules for P, D, and E matrices. Example calculation.

## Slide 10
**Summary**
Types, Inverses, Applications, and Fundamental Theorem.

---

# File 7: Handwritten Problem Solutions

## Page 1
**Problem 1**
The first row of $AB$ is a linear combination of all the rows of $B$. What are the coefficients, and what is the first row?
$A = \begin{bmatrix} 2 & 1 & 4 \\ 0 & -1 & 1 \end{bmatrix}$, $B = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{bmatrix}$

**Handwritten Annotation:**
$AB = \begin{bmatrix} 2 & 1 & 4 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 2(1)+1(0)+4(1) & 2(1)+1(1)+4(0) \\ 0(1)+(-1)(0)+1(1) & 0(1)+(-1)(1)+1(0) \end{bmatrix} = \begin{bmatrix} 6 & 3 \\ 1 & -1 \end{bmatrix}$ (2x2 matrix).
Equation shown: $[6 \ 3] = 2[1 \ 1] + 1[0 \ 1] + 4[1 \ 0] = \alpha_1 b_1 + \alpha_2 b_2 + \alpha_3 b_3$.

## Page 2
**Problem 2**
Describe the rows of $EA$ and the columns of $AE$ if $E = \begin{bmatrix} 1 & 7 \\ 0 & 1 \end{bmatrix}$.

**Handwritten Annotation:**
*   $1^{st}$ row of $EA = 1(1^{st} \text{ row of } A) + 7(2^{nd} \text{ row of } A)$
*   $2^{nd}$ row of $EA = 0(1^{st} \text{ row of } A) + 1(2^{nd} \text{ row of } A)$
*   $1^{st}$ column of $AE = (1^{st} \text{ col of } A)\cdot 1 + (2^{nd} \text{ col of } A)\cdot 0$
*   $2^{nd}$ column of $AE = (1^{st} \text{ col of } A)\cdot 7 + (2^{nd} \text{ col of } A)\cdot 1$

## Page 3
**Problem 3**
a) $E_{21}$ subtracts 5 times row 1 from row 2.
b) $E_{32}$ subtracts -7 times row 2 from row 3.

**Handwritten Annotation:**
*   $E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -5 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$
*   $E_{32} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 7 & 1 \end{bmatrix}$
*   Calculation of $E_{32}E_{21}b$ where $b=(1,0,0)$: Result is $\begin{bmatrix} 1 \\ -5 \\ -35 \end{bmatrix}$.
*   Calculation of $E_{21}E_{32}b$: Result is $\begin{bmatrix} 1 \\ -5 \\ 0 \end{bmatrix}$.
*   When $E_{32}$ comes first, row **3** feels no effect from row **1**.

## Page 4
**Problem 4**
Apply elimination to produce L and U.
a) $A = \begin{bmatrix} 2 & 1 \\ 8 & 7 \end{bmatrix}$. Hand notes: $R_2: R_2 - 4R_1 \to \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} = U$.
$E_{21} = \begin{bmatrix} 1 & 0 \\ -4 & 1 \end{bmatrix}$. $E_{21}^{-1} = \begin{bmatrix} 1 & 0 \\ 4 & 1 \end{bmatrix} = L$.

b) $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 4 & 4 \\ 1 & 4 & 8 \end{bmatrix}$.
Handwritten reduction shown:
Row 2 - Row 1, Row 3 - Row 1 $\to \begin{bmatrix} 1 & 1 & 1 \\ 0 & 3 & 3 \\ 0 & 3 & 7 \end{bmatrix}$.
Row 3 - Row 2 $\to \begin{bmatrix} 1 & 1 & 1 \\ 0 & 3 & 3 \\ 0 & 0 & 4 \end{bmatrix} = U$.
$L = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$.

## Page 5
**Problem 6**
What are L and D for this matrix $A = LDU$? What is U in $A = LU$?
$A = \begin{bmatrix} 2 & 4 & 8 \\ 0 & 3 & 9 \\ 0 & 0 & 7 \end{bmatrix}$.
**Handwritten Annotation:**
Matrix is already Upper Triangular.
$L = I$ (Identity).
$A = LU \implies L=\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, $U = A$.
To find D (diagonal of pivots): $D = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 7 \end{bmatrix}$.
$U_{normalized} = \begin{bmatrix} 1 & 2 & 4 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{bmatrix}$.

## Page 6
**Problem 5**
(a) Product nonsingular? $A = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} d_1 & & \\ & d_2 & \\ & & d_3 \end{bmatrix} \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix}$.
Handwritten condition: $d_1, d_2, d_3 \neq 0$.

(b) Solve $Ax=b$ starting with $Lc=b$.
Handwritten steps:
Forward elimination $Lc=b \implies c = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$.
Then $DUx = c$.
Equations:
$c_1=0, c_2=0, c_3=1$.
$x_3 = 1/d_3$.
$x_2 = 1/d_3$.
$x_1 = 1/d_3$.
Solution vector $x = \frac{1}{d_3} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ assuming $d_3 \neq 0$.

## Page 7
**Problem 7**
Show that the inverse of $A$ is $AB$ given $B = (A^2)^{-1}$.
**Handwritten Proof:**
Since $A^2$ is the inverse of $B$, we have $A^2 B = I$.
$(AA)B = I \implies A(AB) = I$.
This means the inverse of $A$ is $AB$.

## Page 8
**Problem 8**
If A is invertible, which properties remain true for $A^{-1}$?
(a) Triangular: Yes.
(b) Symmetric: Yes.
(c) Tridiagonal: No.
(d) Whole numbers: No.
(e) Fractions: Yes.
Note explaining that inverse involves dividing by determinant.

## Page 9
**Proof by Induction**
Standard text proof regarding inverses of upper triangular matrices.
Base case ($n=1$).
Inductive Step: Partitioning $A$ into blocks involving $A_{11}$ (size $n-1$) and scalar $A_{22}$.

## Page 10
**Proof by Induction (continued)**
Derivation of the inverse block matrix.
$A^{-1} = \begin{bmatrix} B_{11} & B_{12} \\ 0 & B_{22} \end{bmatrix}$.
Shows that because $B_{11}$ is upper triangular (by hypothesis) and $B_{22}$ is scalar, the result is upper triangular.

## Page 11
**Symmetric Inverse Proof**
If $A$ is symmetric ($A=A^T$), inverse is symmetric.
Proof steps shown: $(A^{-1})^T = (A^T)^{-1} = A^{-1}$.
Handwritten notes reinforce the transpose property logic.

## Page 12
**MATLAB Screenshot**
Matrix B (whole numbers) -> Inverse of B (decimals/fractions).
Example showing property (d) from Problem 8 is false.

## Page 13
**MATLAB Screenshot**
Matrix A (tridiagonal) -> Inverse (full/dense matrix).
Example showing property (c) from Problem 8 is false.

## Page 14
**Problem 11**
Invert matrix by Gauss-Jordan.
$A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 3 \\ 0 & 0 & 1 \end{bmatrix}$.
**Handwritten Steps:**
Augment $[A|I]$.
$R_2 \to R_2 - 2R_1$: $\begin{bmatrix} 1 & 0 & 0 & | & 1 & 0 & 0 \\ 0 & 1 & 3 & | & -2 & 1 & 0 \\ 0 & 0 & 1 & | & 0 & 0 & 1 \end{bmatrix}$.
$R_2 \to R_2 - 3R_3$: $\begin{bmatrix} 1 & 0 & 0 & | & 1 & 0 & 0 \\ 0 & 1 & 0 & | & -2 & 1 & -3 \\ 0 & 0 & 1 & | & 0 & 0 & 1 \end{bmatrix}$.
Result $A^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}$.

## Page 15
**Problem 10**
Find inverses of 2x2 matrices.
Formula written: $\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.
$A^{-1}$: Determinant $-12$. Result $\frac{1}{-12} \begin{bmatrix} 6 & -3 \\ -4 & 0 \end{bmatrix}$.
$B^{-1}$: Determinant $-b^2$. Result $\frac{1}{-b^2} \begin{bmatrix} 0 & -b \\ -b & a \end{bmatrix}$.
$C^{-1}$: Determinant $21-20=1$. Result $\begin{bmatrix} 7 & -4 \\ -5 & 3 \end{bmatrix}$.

## Page 16
**Problem 9**
Conditions for invertibility (Non-zero pivots).
a) Block diagonal matrix. Invertible if $a, e, i \dots \neq 0$. (Handwritten reduction shows pivots must be non-zero).
b) Matrix B. Invertible if $e \neq 0$ and $c \neq 0$ (based on the block structure determinant).
Handwritten derivation of the inverse of the block matrix is shown at the bottom.

## Page 17
**Problem 12**
Powers of matrices.
a) Powers of $\begin{bmatrix} 2 & 3 \\ 0 & 0 \end{bmatrix}$. Squared: $\begin{bmatrix} 4 & 6 \\ 0 & 0 \end{bmatrix}$. Cubed: $\begin{bmatrix} 8 & 12 \\ 0 & 0 \end{bmatrix}$. Pattern: $2^n$ and $3 \cdot 2^{n-1}$.
b) Powers of $\begin{bmatrix} 2 & 3 \\ 0 & 1 \end{bmatrix}$. Squared: $\begin{bmatrix} 4 & 9 \\ 0 & 1 \end{bmatrix}$. Cubed: $\begin{bmatrix} 8 & 21 \\ 0 & 1 \end{bmatrix}$.
c) Inverse calculation for $\begin{bmatrix} 2 & 3 \\ 0 & 1 \end{bmatrix}$.

## Page 18
**Problem 13**
Compute inverses of specific forms.
a) Matrix with $l, m$. Gauss-Jordan steps shown. Inverse involves $-l, -m$.
b) Similar structure, inverse calculated.
c) General form inverse.
Handwritten steps show row operations $R_2 - L R_1$ etc. to zero out the first column. -->