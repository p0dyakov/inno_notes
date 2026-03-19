This is a complete, line-by-line transcript of the provided Midterm Exam for "Data Structures and Algorithms — Spring 2026."

---

## **Page 1 of 6**

**Header Section:**
*   **Group:** [BS25] - [ ] [ ] - [ 0 ]
*   **Name:** [___________________________________________________]
*   **Email:** [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] @innopolis.university

---

### **Data Structures and Algorithms — Spring 2026**
### **Midterm Exam**

Dear student, welcome to the Midterm Exam!

Please, read carefully the following information about the exam:

*   **This is a closed book exam:**
    1.  Notes, cheat sheets, or devices (including laptops, tablets, phones, smartwatches, headphones, radios, TV-sets) are **not allowed**.
    2.  Cheating, attempts of cheating, assisting others in cheating, communicating with other students during the exam will result in immediate removal from the exam, without any opportunity of retake.
*   **Do not open** the exam questions before the exam starts!
    Reading questions before the official start will be considered cheating.
*   **Keep your student ID card** on the table next to you for the duration of the exam.
*   **Write your name, group number, and email address** at the top of this page.
*   **When the exam starts, write your name, group number, and email address** at the top of **every** odd page.
*   This exam contains 9 regular questions for 125 points total.
*   Maximum total for the exam is 100 points, so you have some room for mistakes.
*   While you wait for the exam to start, you may draw a doodle in the box below:

**[Image Description: A large, empty rectangular box intended for drawing doodles.]**

---
**Footer:**
For full grade you need to score 100 out of 125 points in this Midterm Exam. | **Page 1 of 6**

---

## **Page 2 of 6**

**Header:** IU DSA Spring 2026 — Midterm Exam

### **Question A, variant 1 (15 points)**

Compute asymptotic worst case time complexity of the **SOLVE** procedure:

1.  Express the running time of the **SOLVE** procedure $T(n)$ as a recurrence relation.
2.  Find the asymptotic complexity of $T(n)$ using the master method. You **must** specify which case of the master theorem is applied and provide complete justification for its use.

```python
1  /* A is a 1-indexed array
2   * n is the number of elements in A */
3  Solve(A, n):
4    return Helper(A, 1, n)
5
6  Helper(A, l, r):
7    if r - l <= 100
8      return l
9    else
10     k := ⌈(r - l + 1) / 6⌉
11     a = Helper(A, l, l + 2 * k) + Helper(A, l + k, l + 3 * k)
12     b = Helper(A, l + 2 * k, l + 4 * k) + Helper(A, l + 3 * k, l + 5 * k)
13     c = Helper(A, l + 4 * k, r)
14     low := l; high := r
15     while low < high:
16       mid := ⌊(low + high) / 2⌋
17       count := 0
18       for i from l to r:
19         if A[i] > A[mid]: count := count + 1
20       if count > (r - l + 1) / 2 then high := mid else low := mid + 1
21     return low
```

**Recurrence relation** $T(n) =$ [___________________________________________________]

**Asymptotic complexity** $T(n) =$ [___________________________________________________]

**Which case of the master theorem applies, if any?** [________________________________]

**Justification**
**[Image Description: A large empty rectangular box for writing the justification.]**

---
**Footer:**
For full grade you need to score 100 out of 125 points in this Midterm Exam. | **Page 2 of 6**

---

## **Page 3 of 6**

**Header Section:**
*   **Group:** [BS25] - [ ] [ ] - [ 0 ]
*   **Name:** [___________________________________________________]
*   **Email:** [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] @innopolis.university

---

### **Question B, variant 1 (16 points)**

Use the **most precise** asymptotic notation ($O$, $\Theta$, $\Omega$) in the relations below.
In case none of the asymptotic notations is applicable, use $\times$.

1.  $2026^n$ = [ ] $((n + 2026)!)$
2.  $(\frac{2026}{2025})^n$ = [ ] $(n^{\frac{2026}{2025}})$
3.  $(\log_2 n)^{2026}$ = [ ] $(\sqrt[2026]{n})$
4.  $n \log_2 n$ = [ ] $(\frac{n^2}{\log_2 n})$
5.  $\log_2(n^n)$ = [ ] $(\log_2(n!))$
6.  $\sqrt{n \log_2 n}$ = [ ] $(\sqrt{n} \cdot \log_2 \sqrt{n})$
7.  $(1 + \frac{1}{n})^n$ = [ ] $(n)$
8.  $2^n + 2^n$ = [ ] $(4^n)$

---

### **Question C, variant 1 (10 points)**

Consider the recurrence relation $T(n) = 8T(n/3) + 5n^2 + 10$. Applying the master theorem, we get:

1.  $T(n) = \Theta(n^2 \log n)$;
2.  $T(n) = \Theta(n^3)$;
3.  the master theorem is not applicable;
4.  none of the above.

**Answer** [____________________]

Justify your answer. If the master theorem is applicable, specify which case and which conditions are satisfied. Otherwise, explain why it is not applicable.

**Justification**
**[Image Description: A large empty rectangular box for writing the justification.]**

---
**Footer:**
For full grade you need to score 100 out of 125 points in this Midterm Exam. | **Page 3 of 6**

---

## **Page 4 of 6**

**Header:** IU DSA Spring 2026 — Midterm Exam

### **Question D, variant 1 (15 points)**

Consider a collection $A$ of $n$ columns. Each column $C_i$ is itself a collection of $n$ elements. Consider extending $A$ with one more column $C_{n+1}$ that consists of the diagonal elements $C_1[1], C_2[2], \dots, C_n[n]$:

**[Image Description: A mathematical representation of the operation. 
Left side: "extend" operating on a 3x3 matrix where the columns are (1 2 3), (4 5 6), and (7 8 9). 
Right side: The resulting 3x4 matrix where the first three columns are identical to the original, and the fourth column is (1 5 9), which are the diagonal elements of the original matrix.]**

(Columns are $C_1 = (1, 2, 3), C_2 = (4, 5, 6), C_3 = (7, 8, 9)$; the new column is the diagonal $C_4 = (1, 5, 9)$.)
Fill in the table below. Write the asymptotic worst case time complexity in each cell.

| Rep. of $A$ / Rep. of $C_i$ | Array List | Singly-Linked (no tail) | Singly-Linked (with tail) |
| :--- | :--- | :--- | :--- |
| **Array List** | | | |
| **Singly-Linked (no tail)** | | | |
| **Singly-Linked (with tail)** | | | |

**Brief justification:**
**[Image Description: An empty rectangular box for the justification.]**

---

### **Question E, variant 1 (15 points)**

Consider sorting a collection of *phrases* using RADIX-SORT, treating each word as a “digit” of a phrase:
*   Each *phrase* is a list of at most $w$ words.
*   Each *word* is a list of at most $s$ symbols.
*   Each *symbol* comes from an alphabet of size $a$.

Assume that comparing symbols is $\Theta(1)$, but comparing words or phrases is not.
What is the **worst case** time complexity for sorting $p$ phrases in terms of $p, w, s,$ and $a$, if

1. words are sorted using INSERTION-SORT [________________________________________]
2. words are sorted using COUNTING-SORT [________________________________________]
3. words are sorted using QUICK-SORT [________________________________________]

---
**Footer:**
For full grade you need to score 100 out of 125 points in this Midterm Exam. | **Page 4 of 6**

---

## **Page 5 of 6**

**Header Section:**
*   **Group:** [BS25] - [ ] [ ] - [ 0 ]
*   **Name:** [___________________________________________________]
*   **Email:** [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] @innopolis.university

---

### **Question F, variant 1 (12 points)**

Apply COUNTING-SORT to the following array. Each column is an element with a numeric *key* (top row) and a letter *data* (bottom row). Sort by key only; preserve the data with each key.

| key | 3 | 1 | 2 | 0 | 2 | 1 | 4 | 0 | 2 | 1 | 0 | 3 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **data** | I | E | D | R | S | A | E | I | H | N | S | N |

1.  Give the auxiliary array $C$ after the cumulative step (ready to place elements).

| $k$ | 0 | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $C[k]$ | | | | | |

2.  Give the output array (keys and data in sorted order).

| key | | | | | | | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **data** | | | | | | | | | | | | |

---

### **Question G, variant 1 (10 points)**

For each statement, write **TRUE** or **FALSE** in the corresponding box.

1.  If $\log(f(n)) = \Theta(\log(g(n)))$ then $f(n) = \Theta(g(n))$. [_____________]
2.  Incrementing a binary counter takes $\Theta(\log k)$ worst case time, where $k$ is the number of digits used in the counter. [_____________]
3.  In ARRAYSTACK, PUSH($x$) has $\Theta(n)$ worst case time complexity. [_____________]
4.  MERGE-SORT has $\Theta(n \log n)$ worst case time complexity. [_____________]
5.  COUNTING-SORT sorts $n$ integers in the range $[0, n^2]$ in $\Theta(n)$ worst case time. [_____________]
6.  If the master theorem does not apply to a recurrence, the algorithm may loop indefinitely on some input. [_____________]
7.  Dynamic Programming is a technique that involves a dynamically-typed programming language (e.g. Python). [_____________]
8.  QUICK-SORT has $\Theta(n \log n)$ worst case time complexity. [_____________]
9.  In a binary search tree, the node with the minimum key cannot have a right child. [_____________]
10. The height of a red-black tree with $n$ internal nodes is $\Theta(\log n)$. [_____________]

---
**Footer:**
For full grade you need to score 100 out of 125 points in this Midterm Exam. | **Page 5 of 6**

---

## **Page 6 of 6**

**Header:** IU DSA Spring 2026 — Midterm Exam

### **Question H, variant 1 (12 points)**

Consider a binary search tree $T$ stored in the following array representation. An empty slot is shown as –.

**[Image Description: An array representing a binary tree. Indices range from 0 to 15.]**
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **8** | **4** | **12** | **2** | **6** | **10** | **–** | **–** | **–** | **–** | **–** | **9** | **11** | **–** | **–** | **–** |

What will the array look like after **inserting** into the initial tree $T$ the keys **20, 5, 17** (in this order)?
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | | | | | | | |

What will the array look like after **deleting** key **10** from the **initial** tree $T$?
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | | | | | | | |

What will the array look like after **deleting** key **8** from the **initial** tree $T$?
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | | | | | | | |

---

### **Question I, variant 1 (20 points)**

Answer the following about the Rod Cutting problem.

1.  What is the worst case time complexity of computing the maximum revenue for a rod of length $n$?
    *   **Dynamic Programming with tabulation:** [____________________________________]
    *   **Dynamic Programming with memoization:** [____________________________________]

2.  Find the maximum revenue for a rod of length 10 with the following price table:

| length $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| price $p_i$ | 1 | 5 | 5 | 8 | 10 | 14 | 20 | 18 | 22 | 25 |

**Maximum revenue =** [____________________________________]
**Rod lengths (pieces) that achieve this revenue:** [____________________________________]

Present in the table the values of the solutions to subproblems used in DP for this problem:
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | | |

---
**Footer:**
For full grade you need to score 100 out of 125 points in this Midterm Exam. | **Page 6 of 6**