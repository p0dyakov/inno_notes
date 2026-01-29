<!-- Here is the transcribed and formatted text from the provided documents, separated by file and organized by slides/sections.

---

# File 1: Topic 1. Problem Set (Theory)

**Course:** Data Structures and Algorithms (Spring 2025), Innopolis University
**Reference:** [CLRS] Cormen, T.H., Leiserson, C.E., Rivest, R.L. and Stein, C., 2022. *Introduction to algorithms, Fourth Edition*. MIT press.

### Problem 1.1
Compute asymptotic worst case time complexity of the following algorithm (see pseudocode conventions in [CLRS, §2.1]). You **must** use $\Theta$-notation. Provide full justification, including:
*   Execution cost and frequency count for each line in the body of the `secret` procedure.
*   The details for the computation of the running time $T(n)$ for the worst-case scenario.

*Proof for the asymptotic bound is not required for this exercise.*

```text
/* A is a 1-indexed array,
 * n is the number of items in A */
function secret(A, n)
    r := n
    while (2 * r > n)
        k := n - r + 1
        i := r
        for j = k to r
            if (A[j] < A[i])
                i := j
            if (A[j] > A[k])
                k := j
        exchange A[i] with A[r]
        exchange A[k] with A[n - r + 1]
        r := r - 1
```

**Table: Cost and Frequency**

| Line | Execution Cost | Frequency Count |
| :--- | :--- | :--- |
| 1 | — | — |
| 2 | — | — |
| 3 | — | — |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |
| 11 | | |
| 12 | | |
| 13 | | |
| 14 | | |
| 15 | | |

---

### Problem 1.2
The following algorithm manipulates elements in the input array. For example:
**Visual Representation:**
Input Array: `[2, 1, 4, 3, 5, 8, 9]` $\Longrightarrow$ Output Array: `[2, 4, 5, 8, 9, 3, 1]`

```text
/* A is a 1-indexed array,
 * n is the number of items in A */
function reorder(A, n)
    k := 0
    for i = 1 to (n - 1)
        if A[i - k] < A[i + 1]
            exchange A[i - k + 1] with A[i + 1]
        else:
            k := k + 1
```

Let $n > 0$. Is it true that the element at index $(n - k)$ in the output array is always the largest element of the input array? If yes — prove it using a loop invariant. If not — provide a counterexample.

---

### Problem 1.3
For each of the following statements determine whether it is **TRUE** or **FALSE**. Provide full justification (formal proof) using formal definitions [CLRS, §3] and/or known properties of asymptotic notation (it is **mandatory** to explicitly reference or prove all used properties):

1.  Is it true that $n^4 - 20n^2 - 1 = \Theta(n^4)$?
2.  Is it true that $\log_2(\log_3 n) = O(\log_6 n)$?
3.  Is it true that $\min(\log n, \sqrt{n}) = \Omega(\log n + \sqrt{n})$?
4.  Is it true that $n 2^n = o(3^n)$?
5.  Is it true that $(n - 1)! = \Theta(n!)$?

---
---

# File 2: Lecture 1 Presentation

## Section: Introduction & Admin

### Slide 1: Title Slide
**Data Structures and Algorithms**
Lecture 1. Introduction. Algorithms. Algorithm Correctness and Analysis. Asymptotic Notation.

*Nikolai Kudasov*
*Lab of programming languages and compilers*
*Innopolis University*

### Slide 2: Outline
*   About this course
*   Algorithms
*   Algorithm Correctness
*   Algorithm Analysis
*   Formal Asymptotic Notation
*   Properties of Asymptotic Notation
*   Common Functions and Asymptotic Notation
*   Exercises

### Slide 3: About this course
*(Header slide)*

### Slide 4: What is this course about?
This semester you will learn:
1.  to formulate algorithms with pseudocode
2.  to prove correctness of (simple) algorithms
3.  to analyse the trade-offs when selecting algorithms or data structures to solve a practical task
4.  to analyse algorithm time and space complexity (formally)
5.  to apply some classical algorithms and data structures to solve problems
6.  to implement some classical algorithms and data structures using programming languages

### Slide 5: What is NOT a part of this course
The following topics relate to the course materials, but are NOT part of the course:
1.  machine learning algorithms
2.  concurrent, distributed, or parallel algorithms (e.g. for GPU)
3.  programming for embedded systems
4.  cryptographic algorithms, data compression algorithms
5.  complexity theory (e.g. $P \overset{?}{=} NP$)
6.  competitive programming
7.  programming languages and programming paradigms

### Slide 6: Course structure
*   **Lectures and Tutorials:**
    *   theoretical material
    *   key examples
    *   solving of sample problems
*   **Labs:**
    *   defense of the homework
    *   technical help from TAs
*   **Books:**
    *   detailed explanations, full proofs
    *   self-study of some sections (for homework and better learning experience)
    *   more exercises and examples

### Slide 7: Books
The course makes use of the following books:
1.  **Thomas H Cormen et al. (2022). Introduction to algorithms. MIT press**
    *   The main book of the course. Please note that we are using the 2022 edition.
2.  **Michael T Goodrich, Roberto Tamassia, and Michael H Goldwasser (2014). Data structures and algorithms in Java. John Wiley & Sons**
    *   Examples in Java and additional data structure variations.

For some topics we may also refer to additional literature.

### Slide 8: Grading
Your final grade for this course will consist of:
1.  **Quizzes (during tutorials) — 5%**
    *   a 10-min quiz based on lecture material
2.  **Homework (weekly)**
    *   **Coding (CodeForces) — 25%**
    *   **Theory (Moodle) — 30%**
    *   a few days to complete, fast preliminary grading
    *   preliminary grade must be **defended** (orally) during the next lab
    *   worst homework in each block is dropped (see Block grading policy)
3.  **Midterm and Final Exams — 20% + 20%**
    *   written **closed-book** exam on theory (approximately 90 minutes)

Grade thresholds: A ($\ge 90\%$), B ($\ge 75\%$), C ($\ge 60\%$), D ($< 60\%$)

### Slide 9: Course Topics
*   **Block 1**
    1.  Elementary Data Structures, Recursion, and Brute Force
    2.  Divide-and-Conquer and Solving Recurrences
    3.  Linear-Time Sorting
    4.  Dynamic Programming
*   **Block 2**
    5.  Maps, Sets, and Binary Search Trees
    6.  Probabilistic Analysis and Randomized Algorithms
    7.  Hash Tables
    8.  Priority Queues and Heaps
*   **Block 3**
    9.  Graph Representations, BFS, DFS, Topological Sorting
    10. Minimum Spanning Tree Algorithms
    11. Shortest Paths Algorithms
    12. Flow Networks
    13. Amortized Analysis

### Slide 10-13: Office Hours
**Where and when:**
*   Normally you can find me in room 408 on Fridays from 13:00 to 15:00.
*   To meet at a different time — contact via Telegram at `fizruk31337`.
*   Also visit your TA office hours!

**Things to talk about during office hours:**
*   Course material (clarifications, hints, etc.)
*   Other computer science/programming topics: advanced data structures, functional programming, computer science, logic, abstract math, etc.
*   Anything else you wish to discuss.

### Slide 14-18: Before we begin Lecture 1...
*   If you do not understand some English:
    *   **Ask for the meaning or a translation!** (although I can only translate into Russian)
*   If you do not quite understand something technical:
    *   **Ask a question!** (chances are, someone else also has that question)
*   If there is a lot that you do not understand:
    *   **Be patient:** work through exercises, use office hours! (study can be hard, but persevering is rewarding!)
*   If you already know a topic we are covering:
    *   **Please, verify me!** (slides may contain unintentional typos or mistakes)
*   If you came to the class:
    *   **Please, be here on time and be respectful to other students!**

---

## Section: Algorithms

### Slide 20: Objectives
Today you will be able to:
1.  explain what does it mean for an algorithm to be correct
2.  prove correctness of simple algorithms using loop invariants
3.  explain what is algorithm complexity analysis
4.  recall formal definitions for asymptotic notation
5.  analyse asymptotic time complexity of simple algorithms
6.  formally prove statements with asymptotic notation
7.  recall properties of asymptotic notation
8.  recall properties of common functions w.r.t. asymptotic notation

### Slide 21: What is an Algorithm? (Instructions)
**Algorithm as a sequence of instructions (informal)**
> Informally, an **algorithm** is any well-defined computational procedure that takes some value, or set of values, as **input** and produces some value, or set of values, as **output** in a finite amount of time. An algorithm is thus a sequence of computational steps that transform the input into the output.
> — Cormen et al. 2022, §1.1

### Slide 22: What is an Algorithm? (Problem Solving)
**Algorithm as a solution of a computational problem (informally)**
> You can also view an algorithm as a tool for solving a well-specified **computational problem**. The statement of the problem specifies in general terms the desired input/output relationship for problem instances, typically of arbitrarily large size. The algorithm describes a specific computational procedure for achieving that input/output relationship for all problem instances.
> — Cormen et al. 2022, §1.1

### Slide 23-26: Computational Problems (Examples)
**Exponentiation Problem**
*   **Input:** Numbers $a$ and $n$.
*   **Output:** Number $r$ such that $r = a^n$.

**Prime Factorization Problem**
*   **Input:** Natural number $n > 1$.
*   **Output:** Sequence of numbers $\langle p_1, \dots, p_k \rangle$ such that $p_i$ is a prime for all $1 \le i \le k$ and $\prod_{i=1}^k p_i = n$.

**Search Problem**
*   **Input:** Sequence of $n$ numbers $\langle a_1, a_2, \dots, a_n \rangle$ and a number $x$.
*   **Output:** Either a number (index) $i$ such that $a_i = x$ (if such an index exists), or a special value **NOT FOUND** (otherwise).

**Sorting Problem (Cormen et al. 2022, §1.1)**
*   **Input:** Sequence of $n$ numbers $\langle a_1, a_2, \dots, a_n \rangle$.
*   **Output:** Permutation (rearrangement) $\langle a'_1, a'_2, \dots, a'_n \rangle$ of the input sequence such that $a'_1 \le a'_2 \le \dots \le a'_n$.

---

## Section: Algorithm Correctness

### Slide 28-30: Correct Algorithms
A correct algorithm run on any valid input (defined by the computational problem) must:
1.  terminate in finite time and
2.  produce a correct output (defined by the computational problem).

**Example: Search Algorithm**
A correct search algorithm for any finite input sequence $\langle a_1, a_2, \dots, a_n \rangle$ and a number $x$ terminates in a finite time and produces a correct output: either an index $i$ such that $a_i = x$ if such an index exists, or a special value **NOT FOUND**.

### Slide 31-34: Approaches to Correctness
1.  **Testing** — checking an implementation (or pseudocode) on specific examples.
2.  **Pen-and-paper proof** — mathematical proof of correctness on paper.
3.  **Formal verification** — a computer-checked proof of correctness for a formalized computational problem and an algorithm (or its model), often done using computer proof assistants.

*Note:* We will mostly check correctness on examples, but sometimes also will use semi-formal proofs.

### Slide 35: Correctness of Loops
Most of the algorithms in this course rely on for- and while-loops. How do we prove a loop correct?

**Example Code:**
```text
function exp(a, n)
begin
    k := 0
    b := 1
    while k != n do
    begin
        k := k + 1
        b := b * a
    end
    return b
end
```

### Slide 36: Checking an Algorithm on Examples (Testing)
What does this algorithm compute on the following inputs?
*   $a = 2, n = 3$
*   $a = 3, n = 2$

### Slide 37: Loop Invariant
A loop invariant is a property (usually defined in terms of local state variables) that holds on every iteration of the loop. To prove a loop invariant $P$, it is sufficient to prove:
1.  **Initialization:** $P$ holds prior to the first iteration of the loop.
2.  **Maintenance:** If $P$ holds before an iteration, then it holds after the iteration.
3.  **Termination:** The loop terminates, and when it terminates, $P$ gives us a useful property (that helps show that the algorithm is correct).

### Slide 38-43: Loop Invariant (Example)
**Algorithm:** `exp(a, n)` as defined previously.
**Loop invariant:** $b = a^k$.

**Proof:**
1.  **Initialization:** Prior to the first iteration we have $b=1, k=0$, so for any $a$ the invariant holds ($1 = a^0$).
2.  **Maintenance:**
    *   before iteration $i$: $b_i = a^{k_i}$ and $k \ne n$.
    *   after iteration $i$: $b_{i+1} = b_i \cdot a = a^{k_i} \cdot a = a^{k_i + 1} = a^{k_{i+1}}$.
3.  **Termination:** Since initially $k < n$ and it increases by 1 with each iteration, there will be no more than $n-k$ iterations, and when the loop terminates we have $k=n$, so $b = a^n$.

---

## Section: Algorithm Analysis

### Slide 46-50: What is Algorithm Analysis?
Algorithm analysis aims to answer the following question:
*   How **resource requirements** of an algorithm scale with the **size of input data**?

**Which "resources"?**
*   Usually — **execution time** or **size of additional memory**.

**What is "size of input data"?**
*   Usually, one of the following:
    *   number of items in a collection,
    *   length of a string,
    *   number of digits in a number,
    *   power of a polynom,
    *   size of a matrix, etc.

### Slide 51-56: How is Algorithm Analysis Useful?
Algorithm analysis allows us to:
1.  methodically compare different approaches to a problem,
2.  determine if a given algorithm fits resource requirements,
3.  determine optimization opportunities.

*Importantly, all of this is possible **before** investing time/money into a full implementation.*

### Slide 57-58: Empirical Algorithm Analysis
**Empirical approach:**
1.  Implement an algorithm.
2.  Run on inputs of different size (and form!).
3.  Measure the running time.
4.  Plot the results.
5.  Find the best approximating curve.

**Image Description (Figure 1):** A line graph titled "fastRev vs. slowRev". The x-axis represents "Input Size" (0 to 100), and the y-axis represents "Time ($\mu$s)". Two lines are plotted:
*   Red line (fastRev): Remains very close to the x-axis (linear growth).
*   Blue line (slowRev): Curves upwards significantly (quadratic growth).
The caption reads: "AutoBench: comparing the time performance of Haskell programs" (Handley and Hutton 2018).

*Question:* What are the advantages and potential pitfalls of this approach?

### Slide 59: Theoretical Algorithm Analysis
**Analytical approach:**
1.  Describe an algorithm as a pseudocode.
2.  Characterize its running time as $T(n)$.

**Image Description (Figure 2):** Pseudocode for `INSERTION-SORT(A, n)`.
**Image Description (Figure 3):** Equation: $T(n) = an^2 + bn + c = O(n^2)$.

### Slide 60-61: Pseudocode Conventions
Pseudocode is a high-level description of an algorithm in a semi-formal language that represents a simplified "implementation" making analysis easier.
*Important:* we will follow CLRS pseudocode conventions (Cormen et al. 2022, §2.1).

### Slide 62-70: Input Size & Running Time
1.  Normally we will use one parameter for input size, as in $T(n)$.
2.  Sometimes multiple parameters will be used, as in $T(n, k)$.
3.  Input size refers to items in a collection, string length, number of bits, etc.

*Why is it not quite precise to have the running time T(n) as a function of the input size?*

**Example:** Incrementing a number.
*   `8456103473641089382376460123862354289341286512300012` -> update only one digit.
*   `8456103473641089382379999999999999999999999999999999` -> check and update the last 32 digits.
**Conclusion:** Input size (length) is the same, but running time differs considerably!

### Slide 71-74: Choosing Input Data for Analysis
We have to make a choice about the kind of inputs we analyze:
*   **best case** analysis (often useless)
*   **average case** analysis (non-trivial, but can be useful for practical considerations)
*   **worst case** analysis (the default choice)

*Question:* Why is worst case the default (safe) choice?

### Slide 75: Intermediate Summary
Thus, most of the time we will talk about **worst case time complexity analysis**.

### Slide 76: Computing Running Time
To compute running time, we estimate the contribution of each instruction (e.g., `x := x + 1`).
We consider:
*   **execution time/cost** — how much does it cost to run it once.
*   **frequency count** — how many times do we execute this instruction.
We sum up contributions from all instructions to compute $T(n)$.

### Slide 77: Execution Time (RAM model)
For algorithm analysis, the most common is the **RAM (random-access machine)** model:
1.  Instructions execute one after another (no concurrent operations).
2.  Each basic operation ($+, -, \times, \div, :=, \le$) takes 1 unit of time to execute.
3.  Loops and subroutine calls are not basic operations.
4.  Each memory access (read or write) takes 1 unit of time to execute.

### Slide 78: Intermediate Summary
Thus, most of the time we will talk about **worst case time complexity analysis in the RAM model**.

### Slide 79-80: Insertion Sort Analysis
**Image Description (Figure 6):** A table showing the pseudocode lines for `INSERTION-SORT(A, n)` alongside columns for "cost" ($c_1$ to $c_8$) and "times" (frequency counts involving sums like $\sum_{i=2}^n t_i$).

**Image Description (Figure 7):** The resulting polynomial equation for $T(n)$ combining the costs and frequencies:
$T(n) = (\frac{c_5}{2} + \frac{c_6}{2} + \frac{c_7}{2})n^2 + (c_1 + c_2 + c_4 + \frac{c_5}{2} - \frac{c_6}{2} - \frac{c_7}{2} + c_8)n - (c_2 + c_4 + c_5 + c_8)$
This simplifies to $an^2 + bn + c = O(n^2)$.

---

## Section: Asymptotic Notation

### Slide 81-82: Why Asymptotic Notation?
1.  Working with explicit $T(n)$ is difficult (too many details).
2.  We care about **order of growth**, not exact running time.
**Asymptotic notation** is an upper (or lower) bound of the function's order of growth when input size grows to infinity.

### Slide 83-89: Examples of Asymptotic Notation
1.  **Ignore lower-order terms:**
    *   $T(n) = n + 3 = O(n)$
    *   $T(n) = n^2 + 5000n = O(n^2)$
    *   $T(n) = n = o(n^2)$ (intuitively, runs faster than $n^2$ for large $n$)
2.  **Ignore constant factors:**
    *   $T(n) = 6n = O(n)$
    *   $T(n) = 10n^2 + 300 = O(n^2)$

### Slide 90-92: Asymptotic Notation Informally
**Image Description (Figure 8):** Three graphs illustrating asymptotic notation.
1.  **Left Graph ($O$-notation):** Shows a function $f(n)$ bounded above by $cg(n)$ for all $n \ge n_0$. Caption: $f(n) = O(g(n))$.
2.  **Middle Graph ($\Omega$-notation):** Shows a function $f(n)$ bounded below by $cg(n)$ for all $n \ge n_0$. Caption: $f(n) = \Omega(g(n))$.
3.  **Right Graph ($\Theta$-notation):** Shows a function $f(n)$ sandwiched between $c_1g(n)$ and $c_2g(n)$ for all $n \ge n_0$. Caption: $f(n) = \Theta(g(n))$.

*   $T(n) = O(g(n))$ — informally $T(n) \le g(n)$
*   $T(n) = \Theta(g(n))$ — informally $T(n) = g(n)$
*   $T(n) = \Omega(g(n))$ — informally $T(n) \ge g(n)$

### Slide 93: Intermediate Summary
Thus, most of the time we will talk about **asymptotic worst case time complexity analysis in the RAM model**.

---

## Section: Formal Asymptotic Notation

### Slide 97-106: $O$-notation (Big-O)
**Formal Definition:**
Let $g : \mathbb{R}^+ \to \mathbb{R}$. Then $O(g(n))$ is a **set of functions** $f$, such that there exist positive $c$ and $n_0$, such that for any $n \ge n_0$ we have $0 \le f(n) \le cg(n)$:
$$O(g(n)) = \{f(n) \mid \exists c, n_0 > 0. \forall n \ge n_0. 0 \le f(n) \le cg(n) \}$$

*   $cg(n)$ is an **upper bound**.
*   Formally, write $f(n) \in O(g(n))$, but $f(n) = O(g(n))$ is often abused.

### Slide 107-110: $O$-notation Proof Structure
To prove $f(n) = O(g(n))$:
1.  Unfold the formal definition.
2.  Provide/guess values for $n_0$ and $c$.
3.  Prove that for any $n \ge n_0$, $0 \le f(n) \le cg(n)$.

### Slide 111-115: Proof Example 5.1(a)
**Prove:** $4n^2 + 100n + 500 = O(n^2)$.
**Proof:**
We need to find positive $c, n_0$ such that $0 \le 4n^2 + 100n + 500 \le cn^2$ for $n \ge n_0$.
Divide by $n^2$: $0 \le 4 + \frac{100}{n} + \frac{500}{n^2} \le c$.
Let $n_0 = 1$. Then $4 + 100 + 500 = 604$.
Set $c = 604$. The inequality holds.

### Slide 116-118: Proof Example 5.1(b)
**Prove:** $4n^2 + 100n + 500 = O(n^2)$.
**Proof:**
Divide by $n^2$: $0 \le 4 + \frac{100}{n} + \frac{500}{n^2} \le c$.
Let $n_0 = 100$.
$0 \le 4 + \frac{100}{100} + \frac{500}{100^2} \le 4 + 1 + 0.05 = 5.05 < 6$.
Thus, we can set $c = 6$.

### Slide 119-124: $O$-notation Negation
What does $f(n) \neq O(g(n))$ mean?
It is the negation of the definition:
$\neg (\exists c, n_0 > 0. \forall n \ge n_0. 0 \le f(n) \le cg(n))$
$\iff \forall c, n_0 > 0. \neg (\forall n \ge n_0. 0 \le f(n) \le cg(n))$
$\iff \forall c, n_0 > 0. \exists n \ge n_0. (f(n) < 0) \lor (f(n) > cg(n))$

### Slide 125-134: Negation Proof Example 5.2
**Prove:** $n^3 - 100n^2 \neq O(n^2)$.
**Proof:**
It is enough to show that for any positive $c$ and $n_0$ there exists $n \ge n_0$ such that $n^3 - 100n^2 > cn^2$.
Divide by $n^2$: $n - 100 > c$.
Set $n = \max(c + 101, n_0)$. The inequality holds.

### Slide 135-140: $\Omega$-notation (Big-Omega)
**Formal Definition:**
$$\Omega(g(n)) = \{f(n) \mid \exists c, n_0 > 0. \forall n \ge n_0. 0 \le cg(n) \le f(n) \}$$
*   $cg(n)$ is a **lower bound**.

### Slide 141-144: $\Omega$ Proof Example 5.3
**Prove:** $4n^2 + 100n + 500 = \Omega(n^2)$.
**Proof:**
Find $c, n_0$ such that $0 \le cn^2 \le 4n^2 + 100n + 500$.
Divide by $n^2$: $0 \le c \le 4 + \frac{100}{n} + \frac{500}{n^2}$.
Let $c = 4$ and $n_0 = 1$.
$4 \le 4 + 100 + 500$ holds.

### Slide 145-152: $\Omega$ Proof Example 5.4
**Prove:** $\frac{n^2}{100} - 100n - 500 = \Omega(n^2)$.
**Proof:**
Find $c, n_0$ such that $0 \le cn^2 \le \frac{n^2}{100} - 100n - 500$.
Divide by $n^2$: $0 \le c \le \frac{1}{100} - \frac{100}{n} - \frac{500}{n^2}$.
Set $n_0$ large enough to make the RHS positive.
If $n_0 = 500^2$, RHS $> \frac{1}{200}$. Set $c = \frac{1}{200}$.

### Slide 153-158: $\Theta$-notation (Theta)
**Formal Definition:**
$$\Theta(g(n)) = \{f(n) \mid \exists c_1, c_2, n_0 > 0. \forall n \ge n_0. 0 \le c_1g(n) \le f(n) \le c_2g(n) \}$$
*   $c_1g(n)$ is a **lower bound**.
*   $c_2g(n)$ is an **upper bound**.
*   Provides an **exact asymptotic bound**.

### Slide 159-160: Theorem 3.1
$f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ AND $f(n) = \Omega(g(n))$.

### Slide 161-177: Proper usage of Asymptotic Notation
*   "The worst case running time of insertion sort is $O(n^2)$" — **True** (Upper bound).
*   "The worst case running time of insertion sort is $\Omega(n^2)$" — **True** (Lower bound).
*   "The worst case running time of insertion sort is $\Theta(n^2)$" — **True** (Exact bound).
*   "The running time of insertion sort is $\Theta(n^2)$" — **FALSE** (Must specify worst/best case).
*   "This algorithm runs in at least $O(n^2)$" — **Bad terminology** ("at least" implies lower bound, $O$ is upper). Should use "at least $\Omega(n^2)$".

### Slide 178-191: Notation in Formulas and Equations
*   $2n^2 + 3n + 1 = 2n^2 + \Theta(n)$.
*   Asymptotic notation in a formula is a placeholder for an anonymous function.
*   $\sum_{i=1}^n O(i)$ expands to $\sum f(i)$ where $f(n)=O(n)$.
*   Chains of equations: Each is interpreted separately.

### Slide 192-195: $o$-notation (Little-o)
**Formal Definition:**
$$o(g(n)) = \{f(n) \mid \forall c > 0. \exists n_0 > 0. \forall n \ge n_0. 0 \le f(n) < cg(n) \}$$
*   Strict upper bound.
*   $\lim_{n\to\infty} \frac{f(n)}{g(n)} = 0$.

### Slide 196-199: $\omega$-notation (Little-omega)
**Formal Definition:**
$$\omega(g(n)) = \{f(n) \mid \forall c > 0. \exists n_0 > 0. \forall n \ge n_0. 0 \le cg(n) < f(n) \}$$
*   Strict lower bound.
*   $\lim_{n\to\infty} \frac{f(n)}{g(n)} = \infty$.

---

## Section: Properties of Asymptotic Notation

### Slide 201: Reflexivity
$f(n) = \Theta(f(n))$, $f(n) = O(f(n))$, $f(n) = \Omega(f(n))$.

### Slide 202: Transitivity
If $f(n) = \Theta(g(n))$ and $g(n) = \Theta(h(n))$, then $f(n) = \Theta(h(n))$. (Applies to all notations).

### Slide 203: Symmetry
$f(n) = \Theta(g(n))$ iff $g(n) = \Theta(f(n))$.

### Slide 204: Permutation Symmetry
$f(n) = O(g(n))$ iff $g(n) = \Omega(f(n))$.
$f(n) = o(g(n))$ iff $g(n) = \omega(f(n))$.

### Slide 205: No Trichotomy
Unlike real numbers ($a<b, a=b, a>b$), for functions $f$ and $g$, it is possible that **none** of $f=o(g), f=\Theta(g), f=\omega(g)$ are true (e.g., oscillating functions).

---

## Section: Common Functions

### Slide 207-210: Polynomials
A polynomial of degree $d$ is $p(n) = \Theta(n^d)$.
$p(n) = O(n^d)$.

### Slide 211-212: Exponentials
Exponentials outgrow polynomials: $n^b = o(a^n)$ for $a > 1$.

### Slide 213-215: Logarithms
Polylogarithmic functions grow slower than polynomials: $\log^b n = o(n^a)$ for $a > 0$.

### Slide 216-218: Factorials
$n! \le n^n$.
**Stirling's formula:** $n! = \sqrt{2\pi n} (\frac{n}{e})^n (1 + \Theta(\frac{1}{n}))$.
$n! = o(n^n)$.
$n! = \omega(2^n)$.
$\log(n!) = \Theta(n \log n)$.

---

## Section: Exercises

### Slide 220-222: Exercises 5.1-5.6
1.  Is $2^{n+1} = O(2^n)$?
2.  Is $2^{2n} = O(2^n)$?
3.  Prove $\max(f(n), g(n)) = \Theta(f(n) + g(n))$.
4.  Prove $(n+a)^b = \Theta(n^b)$.
5.  Prove if $f(n)=O(n^2)$ and $g(n)=O(\log n)$, then $f(n)g(n) = O(n^2 \log n)$.
6.  Prove if $k \ln k = \Theta(n)$, then $k = \Theta(\frac{n}{\ln n})$.

### Slide 223: References
*(Bibliography as seen in slides 7 and 1)* -->