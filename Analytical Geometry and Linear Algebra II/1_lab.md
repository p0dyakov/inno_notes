Below is the complete transcript of the provided document, organized by slide (page).

---

# Slide 1: Exercise 1
**Page Number:** 3/10

### Text Content:
**Exercise 1**

Consider the following system of equations:
*   $x + 2y = 2$
*   $x - y = 2$
*   $y = 1$

**Bullet Points:**
*   Sketch these three lines and decide if the system is solvable
*   What happens when all the elements on the right hand side are zero?
*   Is there any choice of numbers on the right hand side that allows the three lines to intersect at the same point?

---

### Image Description:
**Graph and Handwritten Notes:**
A Cartesian coordinate system is shown on a yellow grid. Three lines are plotted:
1.  **Pink line:** Labeled $x + 2y = 2$. It passes through $(0, 1)$ and $(2, 0)$.
2.  **Green line:** Labeled $x - y = 2$. It passes through $(2, 0)$ and $(0, -2)$.
3.  **Red line:** Labeled $y = 1$. This is a horizontal line.
4.  **Blue line:** Represents the $x$-axis.
5.  **Intersections:** The lines form a triangle. The red and pink lines intersect at $(0, 1)$. The red and green lines intersect at $(3, 1)$. The pink and green lines intersect at $(2, 0)$. Because there is no single point where all three lines meet, the system is unsolvable.

**Handwritten Notes on the Slide:**
*   "If the right hand side is set equal to zero, then all the lines will cross at the origin."
*   "If we set the third equation equal to zero, then the point $(2, 0)$ will satisfy the system."

---

# Slide 2: Exercise 2
**Page Number:** 4/10

### Text Content:
**Exercise 2**

Consider the following system of equations:
*   $u + v + w = 2$
*   $u + 2v + 3w = 1$
*   $v + 2w = 0$

**Bullet Points:**
*   Explain why this system is singular by providing a combination of three equations that adds up to $0=1$
*   What value should be instead of 0 on the right hand side to allow the system to have any solution?
*   What is one of the solutions?

---

### Image Description:
**Mathematical Derivations (Handwritten):**
1.  **Inconsistency Proof:** The slide shows the augmented matrix $\begin{pmatrix} 1 & 1 & 1 & 2 \\ 1 & 2 & 3 & 1 \\ 0 & 1 & 2 & 0 \end{pmatrix}$. 
    *   Note: "If we perform the operation: $Row(2) - Row(1)$ then we obtain: $\begin{pmatrix} 1 & 1 & 1 & 2 \\ 0 & 1 & 2 & -1 \\ 0 & 1 & 2 & 0 \end{pmatrix}$."
    *   Note: "Here we notice our inconsistency: $0 = -1$" (pointing to the difference between the second and third rows).

2.  **Solving for a consistent case:**
    *   "If we set the right hand side of the third equation equal to negative one, we have: $\begin{pmatrix} 1 & 1 & 1 & 2 \\ 1 & 2 & 3 & 1 \\ 0 & 1 & 2 & -1 \end{pmatrix} \sim \begin{pmatrix} 1 & 1 & 1 & 2 \\ 0 & 1 & 2 & -1 \\ 0 & 1 & 2 & -1 \end{pmatrix}$."
    *   "From here we can get all the solutions:"
        *   $y + 2z = -1 \Rightarrow y = -2z - 1$
        *   $x + (-2z - 1) + (z) = 2 \Rightarrow x + 3z = 3 \Rightarrow x = 3(1 - z)$
    *   "After getting all the variables in terms of $z$: $(x, y, z) = (3(1 - z), -(2z + 1), z)$."
    *   "This system has many solutions, one is: $(3, -1, 0)$."

---

# Slide 3: Exercise 3
**Page Number:** 5/10

### Text Content:
**Exercise 3**

Normally 4 planes in a four-dimensional space meet at $*$. Normally 4 column vectors in a four dimensional space can combine to produce $b \in \mathbb{R}^4$. What combination of $(1, 0, 0, 0)$, $(1, 1, 0, 0)$, $(1, 1, 1, 0)$ and $(1, 1, 1, 1)$ produces $(3, 3, 3, 2)$? What equations for $x, y, z$ and $t$ are you solving?

---

### Image Description:
**Handwritten Notes and Matrix:**
*   The asterisk $*$ is defined as: "**at one point.**"
*   **The system of equations:**
    *   $x + y + z + t = 3$
    *   $y + z + t = 3$
    *   $z + t = 3$
    *   $t = 1$
*   **Matrix Representation:** "can be rewritten as: $\begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \\ t \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \\ 3 \\ 2 \end{pmatrix}$"
*   **Note:** "Which is already in an upper triangular form, therefore after back-substitution we get: $(0, 0, 1, 2)$." (Note: there appears to be a slight mismatch between the written $b$ vector and the solution provided in the text vs the matrix).

---

# Slide 4: Exercise 4
**Page Number:** 6/10

### Text Content:
**Exercise 4**

Reduce the following system to an upper triangular form by two row operations:
*   $2x + 3y + z = 8$
*   $4x + 7y + 5z = 20$
*   $-2y + 2z = 0$

Circle the pivots. Solve it for $x, y$ and $z$ by back-substitution.

---

### Image Description:
**Row Reduction Steps (Handwritten):**
1.  "The system can be rewritten as: $\begin{pmatrix} 2 & 3 & 1 & 8 \\ 4 & 7 & 5 & 20 \\ 0 & -2 & 2 & 0 \end{pmatrix}$."
2.  "If we perform the following operation: $Row(2) - 2Row(1)$ we obtain: $\begin{pmatrix} 2 & 3 & 1 & 8 \\ 0 & 1 & 3 & 4 \\ 0 & -2 & 2 & 0 \end{pmatrix}$." 
    *   The number **2** in the first row is circled and labeled "**first pivot**".
3.  The next step shows: $\begin{pmatrix} 2 & 3 & 1 & 8 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 8 & 8 \end{pmatrix}$ after adding $2 \times Row(2)$ to $Row(3)$.
    *   The number **1** in the second row is circled and labeled "**second pivot**".
4.  "Finally, after solving it for $x, y, z$ we have: $(2, 1, 1)$."

---

# Slide 5: Exercise 5
**Page Number:** 7/10

### Text Content:
**Exercise 5**

**Bullet Points:**
*   Which number $b$ leads later to a row exchange?
*   Which $b$ leads to a missing pivot?
*   In that singular case find a nonzero solution for $x, y$ and $z$

**System of Equations:**
*   $x + by = 0$
*   $x - 2y - z = 0$
*   $y + z = 0$

**Initial Matrix:**
$\begin{pmatrix} 1 & b & 0 \\ 1 & -2 & -1 \\ 0 & 1 & 1 \end{pmatrix}$

---

### Image Description:
**Case Analysis (Handwritten):**
1.  **Row Exchange Case:** 
    *   "If we set $b = -2$: $\begin{pmatrix} 1 & -2 & 0 \\ 1 & -2 & -1 \\ 0 & 1 & 1 \end{pmatrix}$."
    *   "From which we have: $\begin{pmatrix} 1 & -2 & 0 \\ 1 & -2 & -1 \\ 0 & 1 & 1 \end{pmatrix} \sim \begin{pmatrix} 1 & -2 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 1 \end{pmatrix}$."
    *   An arrow indicates a "**row exchange**" between Row 2 and Row 3, resulting in: $\begin{pmatrix} 1 & -2 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & -1 \end{pmatrix}$.

2.  **Missing Pivot Case:**
    *   "If we set $b = -1$: $\begin{pmatrix} 1 & -1 & 0 \\ 1 & -2 & -1 \\ 0 & 1 & 1 \end{pmatrix}$."
    *   "after row operations we have: $\begin{pmatrix} 1 & -1 & 0 \\ 0 & -1 & -1 \\ 0 & 1 & 1 \end{pmatrix} \sim \begin{pmatrix} 1 & -1 & 0 \\ 0 & -1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$."
    *   "To find the solutions to this system, from the second and third row respectively we have:"
        *   $y + z = 0 \Rightarrow z = -y$
        *   $x - y = 0 \Rightarrow x = y$
    *   "Which is: $(x, y, z) = (y, y, -y)$."
    *   "for $y=1$ we get: $(1, 1, -1)$."

---

# Slide 6: Exercise 6
**Page Number:** 8/10

### Text Content:
**Exercise 6**

Construct a 3 by 3 example that has 9 different coefficients on the left hand side, but rows 2 and 3 become zero in the elimination.
*   How many solutions to your system with $b = (1, 10, 100)$?
*   And how many with $b = (0, 0, 0)$?

---

### Image Description:
**Handwritten Analysis:**
1.  **Construction:** "If we consider: $\begin{pmatrix} a & b & c \\ 4a & 4b & 4c \\ 5a & 5b & 5c \end{pmatrix}$."
    *   Note: "proportional." "we can see that after simplifications the second and the third row will be equal to zero."
2.  **Inconsistent Case:** 
    *   "If we consider the $Ax=b$ system: $\begin{pmatrix} a & b & c \\ 4a & 4b & 4c \\ 5a & 5b & 5c \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 10 \\ 100 \end{pmatrix}$."
    *   "Writing the augmented matrix: $\begin{pmatrix} a & b & c & 1 \\ 4a & 4b & 4c & 10 \\ 5a & 5b & 5c & 100 \end{pmatrix} \sim \begin{pmatrix} a & b & c & 1 \\ 0 & 0 & 0 & 6 \\ 0 & 0 & 0 & 95 \end{pmatrix}$."
    *   "In this case we have an inconsistency."
3.  **Homogeneous Case:** 
    *   "If $b = (0, 0, 0)$ we have: $\begin{pmatrix} a & b & c & 0 \\ 4a & 4b & 4c & 0 \\ 5a & 5b & 5c & 0 \end{pmatrix} \sim \begin{pmatrix} a & b & c & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$."
    *   "In this case we have many solutions, e.g. $(0, 0, 0), (1, -2, 1)$" (assuming specific $a, b, c$).
    *   "to get them all, from the first row: $ax + by + cz = 0 \Rightarrow z = -\frac{1}{c}(ax + by), c \neq 0$."
    *   "and we can have a generic element in terms of $x$ and $y$: $(x, y, z) = (x, y, -\frac{1}{c}(ax + by))$."

---

# Slide 7: Exercise 7
**Page Number:** 9/10

### Text Content:
**Exercise 7**

Use elimination to solve:
$u + v + w = 6$
$u + 2v + 2w = 11$
$2u + 3v - 4w = 3$

and

$u + v + w = 7$
$u + 2v + 2w = 10$
$2u + 3v - 4w = 3$

---

### Image Description:
**Step-by-Step Elimination (Handwritten):**
1.  **First System:**
    *   "The system of equations can be rewritten as: $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 2 & 3 & -4 \end{pmatrix} \begin{pmatrix} u \\ v \\ w \end{pmatrix} = \begin{pmatrix} 6 \\ 11 \\ 3 \end{pmatrix}$."
    *   "by elimination we have: $\begin{pmatrix} 1 & 1 & 1 & 6 \\ 1 & 2 & 2 & 11 \\ 2 & 3 & -4 & 3 \end{pmatrix} \sim \begin{pmatrix} 1 & 1 & 1 & 6 \\ 0 & 1 & 1 & 5 \\ 0 & 1 & -6 & -9 \end{pmatrix} \sim \begin{pmatrix} 1 & 1 & 1 & 6 \\ 0 & 1 & 1 & 5 \\ 0 & 0 & -7 & -14 \end{pmatrix}$."
    *   "after back substitution we get: $(1, 3, 2)$." (A red checkmark is next to this). There is also a blue handwritten "(4, 1, 1)" with a checkmark nearby.

2.  **Second System:**
    *   "The system of equations can be rewritten as: $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 2 & 3 & -4 \end{pmatrix} \begin{pmatrix} u \\ v \\ w \end{pmatrix} = \begin{pmatrix} 7 \\ 10 \\ 3 \end{pmatrix}$."
    *   "by elimination we have: $\begin{pmatrix} 1 & 1 & 1 & 7 \\ 1 & 2 & 2 & 10 \\ 2 & 3 & -4 & 3 \end{pmatrix} \sim \begin{pmatrix} 1 & 1 & 1 & 7 \\ 0 & 1 & 1 & 3 \\ 0 & 1 & -6 & -11 \end{pmatrix} \sim \begin{pmatrix} 1 & 1 & 1 & 7 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & -7 & -14 \end{pmatrix}$."
    *   "after back substitution we get: $(4, 1, 2)$." (Note: The handwritten result says $(1, 3, 2)$ again, but the math for $z$ gives $w=2$, then $v+2=3 \rightarrow v=1$, then $u+1+2=7 \rightarrow u=4$).

---

# Slide 8: References
**Page Number:** 10/10

### Text Content:
**References**

*   Gilbert Strang. *Introduction to Linear Algebra*. Fourth. Wellesley, MA: Wellesley-Cambridge Press, 2009.
*   Gilbert Strang. *Linear algebra and its applications*. Belmont, CA: Thomson, Brooks/Cole, 2006. URL: [http://www.amazon.com/Linear-Algebra-Its-Applications-Edition/dp/0030105676](http://www.amazon.com/Linear-Algebra-Its-Applications-Edition/dp/0030105676).