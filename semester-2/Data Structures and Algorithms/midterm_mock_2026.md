Here is the complete, line-by-line transcription of the document with detailed formatting and image descriptions. 

*General Image Description across all pages:* Every page features a faint, semi-transparent background watermark. The watermark depicts a stylized tree where the branches and roots resemble a brain and neural networks. Diagonally across the page, faintly written in large letters, is the text: "Innopolis University Data Structures and Algorithms Spring 2026 mock exam".

---

### Page 1

*Image Description:* The top of the page contains input fields formed by rectangular boxes for the student to fill in their Group, Name, and Email. Below the header is the main title and a bulleted list of instructions.

Group: `[ BS25 ]` `[ - ]` `[   ]` `[   ]` `[ - ]` `[ 0 ]` `[   ]` Name: `[ Empty text box for Name ]`
Email: `[ 15 empty single-character boxes ]` `@innopolis.university`

# Data Structures and Algorithms — Spring 2026
## Mock Midterm Exam

Dear student, this is a **mock** exam for practice.

Please read the following:
* This mock contains 14 questions.
* Format and style are similar to the real midterm; content is varied.
* You may use it under exam-like conditions or for revision.
* Note that the midterm exam may contain questions that do not appear in this mock exam.

This mock exam has 14 questions. \hfill Page 1 of 9

---

### Page 2

*Image Description:* The top features the course and exam title. The middle contains a framed code block showing an algorithm written in pseudocode with line numbers from 1 to 20. Below the code block are two single-line text boxes for math answers and one large rectangular text box for a written justification.

IU DSA Spring 2026 — Mock Midterm Exam

## Question A

Compute asymptotic worst case time complexity of the `Solve` procedure:

1. Express the running time $T(n)$ as a recurrence relation.
2. Find the asymptotic complexity of $T(n)$ using the master method. Specify which case applies and give a brief justification.

*Image Description: A rectangular frame containing the following pseudocode:*
```text
1  /* A is a 1-indexed array; n is the number of elements in A */
2  Solve(A, n):
3      return Helper(A, 1, n)
4
5  Helper(A, l, r):
6      if r - l <= 50
7          return l
8      else
9          low := l; high := r
10         while low < high:
11             mid := ⌊(low + high) / 2⌋
12             count := 0
13             for i from l to r:
14                 if A[i] > A[mid]: count := count + 1
15             if count > (r - l + 1) / 2 then high := mid else low := mid + 1
16         k := ⌈(r - l + 1) / 3⌉
17         a := Helper(A, l,          l + k - 1)
18         b := Helper(A, l + k,      l + 2*k - 1)
19         c := Helper(A, l + 2*k,    r)
20         return low
```

**Recurrence relation** $T(n) =$ `[ Empty rectangular box ]`

**Asymptotic complexity** $T(n) =$ `[ Empty rectangular box ]`

**Case and justification**
*Image Description: A large empty rectangular box provided for the student's written justification.*
`[ Large empty box ]`

This mock exam has 14 questions. \hfill Page 2 of 9

---

### Page 3

*Image Description:* The top contains the same Group, Name, and Email input fields as Page 1. Below are two questions. Question B features two columns of mathematical relations with empty square boxes where the student must insert a symbol. Question C features a large rectangular box for writing pseudocode, two small boxes for complexities, and another large box for text.

Group: `[ BS25 ]` `[ - ]` `[   ]` `[   ]` `[ - ]` `[ 0 ]` `[   ]` Name: `[ Empty text box for Name ]`
Email: `[ 15 empty single-character boxes ]` `@innopolis.university`

## Question B

Use the **most precise** asymptotic notation ($O, \Theta, \Omega$) in the relations below.
If none applies, use $X$.

$\sqrt{n} \cdot \log_2 n =$ `[ Box ]` $(n^{3/4})$
$n^{1.001} =$ `[ Box ]` $(n \log^2 n)$
$\log_2(n!) =$ `[ Box ]` $(n \log_2 n)$
$\sqrt[4]{n} =$ `[ Box ]` $(\log_2 n)$

$\left(1 + \frac{2}{n}\right)^n =$ `[ Box ]` $(n^2)$
$3^n + 2^n =$ `[ Box ]` $(3^n)$
$\frac{n^2}{\log n} =$ `[ Box ]` $(n\sqrt{n})$
$(n + 1)! =$ `[ Box ]` $(n!)$

## Question C

Given a set $A$ of $n$ integers and a target number $k$, consider the problem of finding a **subset of $A$ of maximum size** whose elements sum to exactly $k$. A brute-force algorithm enumerates all subsets of $A$, checks the sum of each, and among those that sum to $k$, picks one with the largest number of elements.

1. Give **pseudocode** for such a brute-force algorithm (iterative or recursive), or a clear step-by-step description.
*Image Description: A large empty rectangular box spanning the width of the page for writing pseudocode.*
`[ Large empty box ]`

2. What is the worst case time complexity of this algorithm in terms of $n$?
`[ Small empty box aligned to the right ]`

3. Brief justification for the time complexity:
*Image Description: A large empty rectangular box for writing justification.*
`[ Large empty box ]`

4. What is the worst case space complexity (excluding the input) if we use an iterative enumeration (e.g. a single array of length $n$ to represent the current subset)?
`[ Small empty box aligned to the right ]`

This mock exam has 14 questions. \hfill Page 3 of 9

---

### Page 4

*Image Description:* Page header. Question D contains an empty 3x3 grid table for students to fill out, followed by a large empty box. Question E features text with two small empty boxes for formulas and a large box for justification.

IU DSA Spring 2026 — Mock Midterm Exam

## Question D

We have $n$ sorted lists containing $m$ elements in total. We want to merge them into one sorted list of $m$ elements.
Fill in the table with the asymptotic worst case time complexity of merging, depending on how the **input lists** and the **output list** are represented.

*Image Description: A 4-row by 4-column table. The top row and left column act as headers. The 9 internal cells are completely empty for the student to write in.*

| Input lists / Output list | Array | Singly-linked (with tail) | Doubly-linked |
| :--- | :--- | :--- | :--- |
| **Array** (each list contiguous) | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |
| **Singly-linked** (with tail) | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |
| **Doubly-linked** | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |

**Brief justification:**
*Image Description: A large empty rectangular box.*
`[ Large empty box ]`

## Question E

Consider a **hybrid** sorting algorithm that runs QUICK-SORT but stops recursion when the current subarray has size $\le k$; then applies COUNTING-SORT to each such small block (keys in a fixed range $[0, R]$) and concatenates the results.

1. What is the worst case time complexity of this hybrid in terms of $n$, $k$, and $R$?
`[ Rectangular empty box aligned to the right ]`

2. If we choose $k = \Theta(\log n)$ and $R = O(n)$, what is the overall worst case time complexity?
`[ Rectangular empty box aligned to the right ]`

**Brief justification:**
*Image Description: A large empty rectangular box.*
`[ Large empty box ]`

This mock exam has 14 questions. \hfill Page 4 of 9

---

### Page 5

*Image Description:* Header identical to Page 1 and 3. Question F has a list of numbers and two large empty boxes. Question G consists of 10 enumerated statements, each with an empty rectangular box to the right for the student to write "TRUE" or "FALSE".

Group: `[ BS25 ]` `[ - ]` `[   ]` `[   ]` `[ - ]` `[ 0 ]` `[   ]` Name: `[ Empty text box for Name ]`
Email: `[ 15 empty single-character boxes ]` `@innopolis.university`

## Question F

Apply BUCKET-SORT to the following numbers in $[0, 1)$:

$$0.92, \quad 0.21, \quad 0.03, \quad 0.55, \quad 0.07, \quad 0.41, \quad 0.25, \quad 0.12, \quad 0.67, \quad 0.05$$

1. Show the **contents of each bucket** (before sorting inside buckets).
*Image Description: A large empty rectangular box.*
`[ Large empty box ]`

2. Give the **sorted sequence** (after sorting each bucket and concatenating).
*Image Description: A long, narrow rectangular empty box.*
`[ Long empty box ]`

## Question G

For each statement, write **TRUE** or **FALSE**.

1. $n^2 = O(n^{3/2})$.
`[ Empty box ]`

2. In a binary search tree, the node with the maximum key has no left child.
`[ Empty box ]`

3. HEAP-SORT has $O(n)$ worst case time complexity.
`[ Empty box ]`

4. RADIX-SORT (with a fixed digit range) sorts $n$ integers in $\Theta(n)$ time regardless of the number of digits.
`[ Empty box ]`

5. In ARRAYQUEUE, ENQUEUE($x$) has $\Theta(n)$ worst case time complexity.
`[ Empty box ]`

6. The height of an AVL tree with $n$ nodes is $\Theta(\log n)$.
`[ Empty box ]`

7. For the recurrence $T(n) = 2T(n/2) + n$, the master theorem gives $T(n) = \Theta(n)$.
`[ Empty box ]`

8. In dynamic programming, overlapping subproblems are solved at least twice.
`[ Empty box ]`

9. MERGE-SORT is a comparison-based sorting algorithm.
`[ Empty box ]`

10. A red-black tree with $n$ internal nodes has height at least $2 \log_2(n + 1)$.
`[ Empty box ]`

This mock exam has 14 questions. \hfill Page 5 of 9

---

### Page 6

*Image Description:* Header. Question H involves Binary Search Trees (BST). It contains two large drawing boxes and three linear array tables representing the tree structure. The arrays have indices 0 to 15 on top and empty boxes directly beneath them.

IU DSA Spring 2026 — Mock Midterm Exam

## Question H

Consider a binary search tree stored in standard array representation. Start from an **empty** tree and **insert** the following keys in order:

$$15, \quad 8, \quad 22, \quad 4, \quad 11, \quad 19, \quad 30, \quad 2, \quad 6, \quad 25$$

1. Draw the constructed BST (after all insertions).
*Image Description: A large empty rectangular box for drawing.*
`[ Large empty box ]`

2. Fill in the array representation **after all insertions** (before any deletion).
*Image Description: A single-row table with 16 columns numbered 0 to 15 above the cells. The cells themselves are empty.*
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` `

3. Fill in the array representation **after deleting key 30**.
*Image Description: Same empty 16-column array format as above.*
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` `

4. Fill in the array representation **after deleting key 8** (from the tree that already had 30 deleted).
*Image Description: Same empty 16-column array format as above.*
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` ` | ` `

5. Draw the **final** BST (after all insertions and both deletions).
*Image Description: A large empty rectangular box for drawing.*
`[ Large empty box ]`

This mock exam has 14 questions. \hfill Page 6 of 9

---

### Page 7

*Image Description:* Header identical to Pages 1, 3, and 5. Question I is about Dynamic Programming and LCS. It has text input boxes and a partially filled DP table. Question J shows an array representation of a tree with numbers and dashes, followed by two input boxes.

Group: `[ BS25 ]` `[ - ]` `[   ]` `[   ]` `[ - ]` `[ 0 ]` `[   ]` Name: `[ Empty text box for Name ]`
Email: `[ 15 empty single-character boxes ]` `@innopolis.university`

## Question I

Answer the following about the **Longest Common Subsequence (LCS)** problem. Given two sequences $X$ and $Y$, we want the length of an LCS and one such subsequence.

1. What is the worst case time and space complexity of computing the LCS length using dynamic programming with *tabulation* (bottom-up), if $|X| = m$ and $|Y| = n$?

**Time:** `[ Empty rectangular box ]`
**Space:** `[ Empty rectangular box ]`

2. Find the LCS **length** for $X = \langle A, B, C, A, B \rangle$ and $Y = \langle B, A, C, B, A \rangle$. Then give one LCS of that length.

**LCS length =** `[ Empty rectangular box ]`
**One LCS (e.g. as sequence):** `[ Empty rectangular box ]`

3. Fill in the DP table $C[i, j]$ (LCS length of $X[1..i]$ and $Y[1..j]$). Row $i = 0$ and column $j = 0$ are filled with 0.

*Image Description: A 7x7 grid table representing the DP array. The top row and leftmost column are headers with sequences. The 0-index row and column are filled with 0s. The rest of the cells are empty.*

| $C$ | $j = 0$ | $j = 1$ (B) | $j = 2$ (A) | $j = 3$ (C) | $j = 4$ (B) | $j = 5$ (A) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **$i = 0$** | 0 | 0 | 0 | 0 | 0 | 0 |
| **$i = 1$ (A)** | 0 | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |
| **$i = 2$ (B)** | 0 | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |
| **$i = 3$ (C)** | 0 | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |
| **$i = 4$ (A)** | 0 | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |
| **$i = 5$ (B)** | 0 | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` | `[ Empty ]` |

## Question J

The **initial** AVL tree is given in array representation. An empty slot is shown as –.

*Image Description: An array representation table with indices 0 to 15 on top. The row below contains the elements of the array.*
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
**7** | **4** | **9** | **1** | **5** | **8** | **10** | **–** | **2** | **–** | **–** | **–** | **–** | **–** | **–** | **–**

Key **3** is inserted using the usual BST insertion (*without* rebalancing).

1. Which rotation(s) are necessary to restore the AVL invariant? For each rotation, give the pair of keys (*parent, child*) where the rotation is performed. List at most two rotations.

**Rotation 1 (parent, child):** `[ Empty rectangular box ]`
**Rotation 2 (parent, child):** `[ Empty rectangular box ]`

This mock exam has 14 questions. \hfill Page 7 of 9

---

### Page 8

*Image Description:* Header. Question K lists three algorithm paradigms for a problem, providing a small box for time complexity and a large empty box for justification for each paradigm. Question L provides two text questions, each paired with a small empty input box.

IU DSA Spring 2026 — Mock Midterm Exam

## Question K

The **maximum subarray** problem: given an array of $n$ numbers, find a contiguous subarray with maximum sum.
For each of the three approaches below, state the worst case **time complexity** in terms of $n$ and give a **brief justification**.

**Time complexity for Brute Force:** `[ Small empty box aligned right ]`
**Brief justification:**
*Image Description: A large empty rectangular box.*
`[ Large empty box ]`

**Time complexity for Divide-and-Conquer:** `[ Small empty box aligned right ]`
**Brief justification:**
*Image Description: A large empty rectangular box.*
`[ Large empty box ]`

**Time complexity for Dynamic Programming:** `[ Small empty box aligned right ]`
**Brief justification:**
*Image Description: A large empty rectangular box.*
`[ Large empty box ]`

## Question L

1. What is the **minimum** number of leaves in a decision tree for *any* comparison-based sorting algorithm on an input array of size 6?
`[ Rectangular empty box aligned right ]`

2. State the **lower bound** on the number of comparisons needed to sort $n$ elements by comparisons. Give the asymptotic bound.
`[ Rectangular empty box aligned right ]`

This mock exam has 14 questions. \hfill Page 8 of 9

---

### Page 9

*Image Description:* Header identical to earlier odd pages. Question M asks for values to be inserted into three boxes and provides a large drawing box. Question N provides instructions and invariants for a tree, followed by a very large drawing box.

Group: `[ BS25 ]` `[ - ]` `[   ]` `[   ]` `[ - ]` `[ 0 ]` `[   ]` Name: `[ Empty text box for Name ]`
Email: `[ 15 empty single-character boxes ]` `@innopolis.university`

## Question M

1. What is the **minimum** number $N(h)$ of (internal) nodes in an AVL tree of height

$h = 4$: \qquad N(4) = `[ Empty rectangular box ]`
$h = 8$: \qquad N(8) = `[ Empty rectangular box ]`
$h = 12$: \quad N(12) = `[ Empty rectangular box ]`

2. Draw a valid AVL tree of **height 4** with the **minimum** number of nodes:
*Image Description: A large empty rectangular box spanning the page width for drawing.*
`[ Large empty box ]`

## Question N

Draw a valid **red-black tree** containing exactly the following keys (inserted in this order):

$$10, \quad 5, \quad 15, \quad 3, \quad 7, \quad 12, \quad 20.$$

Mark each node as red or black. **Red-black tree invariants** (reminder):
1. The root and leaves (empty subtrees) are **black**.
2. If a node is **red**, both its children are **black**.
3. For every node, every path from that node to a leaf has the same number of **black** nodes.

*Image Description: A very large empty rectangular box occupying the bottom half of the page for drawing the red-black tree.*
`[ Large empty box ]`

This mock exam has 14 questions. \hfill Page 9 of 9
