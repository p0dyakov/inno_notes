Here is the complete transcript of the presentation, beautifully formatted. As requested, slides that build upon each other by adding single bullet points or lines of math have been combined into their final, complete versions to provide a clean and readable transcript. All images, diagrams, and handwritten notes have been thoroughly described.

***

### Slide 1: Title Slide

**Data Structures and Algorithms**
Lecture 7. Probabilistic Analysis and Randomized Algorithms

**Nikolai Kudasov**
Lab of Programming Languages and Compilers

*Image Description:* The slide features the green logo of Innopolis University on the left. On the right, there is a stylized graphic of a tree where the trunk and branches are made of black circuitry/tech lines, and the leaves are a mix of vibrant red and black shapes.

---

### Slide 2: Objectives

**Objectives**

Today you will learn to:
1. recall the basic definitions of probability, probability distributions, and random variables;
2. carry out probabilistic analysis of algorithm running time;
3. design and analyze randomized algorithms;
4. perform probabilistic analysis of randomized quicksort;
5. perform probabilistic analysis of bucket sort;
6. determine the expected height of a randomly built binary search tree.

In addition to today’s lecture, see (Cormen et al. 2022, §B.2–B.3, §5, §7.3–7.4, §8.4).

---

### Slide 3: Outline

**Outline**

* Probability
* Probabilistic Analysis
* Randomized Algorithms
* Randomized Quicksort
* Probabilistic Analysis of Bucket Sort
* Randomly Built Binary Search Tree

---

### Slide 4: Probability

**Probability**
*(Section Header)*

---

### Slides 5-8: Events
*(Note: These slides build upon each other. The combined final text is presented below).*

**Events**

Let $S$ be a **sample space**, that is, the set of (elementary) **outcomes**.
An **event** is a subset of the sample space $S$.

**Coin tossing**
Consider tossing a coin 3 times in a row.
The set of outcomes is the set of all length-3 strings (one symbol per toss):

$$S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\},$$

where H stands for heads and T stands for tails.
The event $P_1 = \{HHT, HTH, THH\}$ corresponds to "exactly one tails".

---

### Slides 9-14: Axioms of Probability
*(Note: Combined from slides 9 through 14).*

**Axioms of Probability**

A probability distribution $\text{Pr} : \mathcal{P}(S) \rightarrow \mathbb{R}$ is a function that maps events to real numbers and satisfies the following axioms:

1. $\text{Pr}\{A\} \geq 0$ for any event $A$.
2. $\text{Pr}\{S\} = 1$.
3. $\text{Pr}\{A \cup B\} = \text{Pr}\{A\} + \text{Pr}\{B\}$ for any two mutually exclusive events $A$ and $B$ (that is, $A \cap B = \emptyset$).
4. $\text{Pr}\{\bigcup_i A_i\} = \sum_i \text{Pr}\{A_i\}$ for any finite (or countably infinite) sequence of pairwise mutually exclusive events $A_1, A_2, \dots$

$\text{Pr}\{A\}$ is called the **probability** of event $A$.

*Image Description:* On slide 14, there is a handwritten red brace "{" grouping axioms 1, 2, and 3 together on the left side.

---

### Slides 15-20: Basic Properties of Probability
*(Note: Slides 15-19 feature extensive handwritten proofs and diagrams that build up to the typed text on Slide 20. The final typed text is shown first, followed by transcriptions of the handwritten material).*

**Basic Properties of Probability**

The following properties follow directly from the axioms of probability and basic set theory:
1. $\text{Pr}\{\emptyset\} = 0$
2. $\text{Pr}\{\overline{A}\} = 1 - \text{Pr}\{A\}$
3. $\text{Pr}\{A \cup B\} = \text{Pr}\{A\} + \text{Pr}\{B\} - \text{Pr}\{A \cap B\} \leq \text{Pr}\{A\} + \text{Pr}\{B\}$

**Coin tossing**
Consider tossing a coin 3 times in a row. The set of outcomes is the set of all length-3 strings (one symbol per toss):
$$S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\},$$
where H stands for heads and T stands for tails.
The event $P_1 = \{HHT, HTH, THH\}$ corresponds to "exactly one tails".
🧩 What is the probability of the event $P_1$, assuming all outcomes are equally likely?

**Handwritten Annotations on these slides:**
*   **Slide 15 (Proof for Property 1):**
    $\text{Pr}\{\emptyset \cup S\} = \text{Pr}\{\emptyset\} + \text{Pr}\{S\}$
    because $\emptyset \cap S = \emptyset$
    $\Downarrow$
    $\text{Pr}\{\emptyset\} = \text{Pr}\{\emptyset \cup S\} - \text{Pr}\{S\}$
    $= \text{Pr}\{S\} - \text{Pr}\{S\} = 0$

*   **Slide 16 (Proof for Property 2):**
    $\overline{A} = S \setminus A$
    $\text{Pr}\{A \cup \overline{A}\} = \text{Pr}\{A\} + \text{Pr}\{\overline{A}\} \quad \text{since } A \cap \overline{A} = \emptyset$
    $\text{Pr}\{\overline{A}\} = \text{Pr}\{A \cup \overline{A}\} - \text{Pr}\{A\} = \text{Pr}\{S\} - \text{Pr}\{A\} = 1 - \text{Pr}\{A\}$

*   **Slide 17 (Proof for Property 3 & Venn Diagrams):**
    *Diagram 1:* A Venn diagram showing two intersecting circles, $A$ (green) and $B$ (red). The intersection $A \cap B$ is shaded with blue lines.
    *Diagram 2:* A breakdown of circle $B$, pointing out $A \cap B$ and $B \setminus (A \cap B)$.
    *Mathematical Derivation:*
    $\text{Pr}\{A \cup B\} = \text{Pr}\{A \cup (B \setminus (A \cap B))\}$
    $= \text{Pr}\{A\} + \text{Pr}\{B \setminus (A \cap B)\} = \text{Pr}\{A\} + \text{Pr}\{B\} - \text{Pr}\{A \cap B\}$
    *Side note derivation for the last step:*
    $\text{Pr}\{(A \cap B) \cup (B \setminus (A \cap B))\} = \text{Pr}\{A \cap B\} + \text{Pr}\{B \setminus (A \cap B)\}$
    $\text{Pr}\{B\} \quad \Downarrow$
    $\text{Pr}\{B \setminus (A \cap B)\} = \text{Pr}\{B\} - \text{Pr}\{A \cap B\}$

*   **Slide 20 (Solving the Coin Toss Question):**
    Handwritten fractions appear above the elements of $S$: "$1/8$" above HHH, "$1/8$" above HHT, "$1/8$" above HTH, "$...$", and "$1/8$" above TTT.
    Next to the final question, the handwritten answer is: "$3/8$".

---

### Slides 21-25: Discrete Probability Distributions
*(Note: Combined from slides 21-25).*

**Discrete Probability Distributions**

* A probability distribution is called **discrete** if it is defined on a finite or countably infinite sample space.
* If $S$ is finite and each outcome $s \in S$ has probability $\text{Pr}\{s\} = \frac{1}{|S|}$, then the distribution is called **uniform**. In this case we often say "we pick an element of $S$ uniformly at random".

**Examples of Discrete Distributions**
1. Rolling a fair six-sided die.
2. Rolling two fair six-sided dice and looking at the sum of the faces.
3. Choosing a random student ID from a class of $n$ students.

🧩 Which of these example distributions are uniform?

**Handwritten Annotations (Answers on Slide 25):**
*   Next to Example 1: Handwritten "Yes" and the sample space $\{1, 2, 3, 4, 5, 6\}$.
*   Next to Example 2: Handwritten "No" and the expanded space of sums: $\{1+1, 1+2, 2+1, 1+3, 2+2, 3+1, \dots\}$. A plus sign indicates adding the two die rolls $\{1, 2, 3, 4, 5, 6\} + \{1, 2, 3, 4, 5, 6\}$.
*   Next to Example 3: Handwritten "Yes, by default".

---

### Slide 26: Discrete Random Variable

**Discrete Random Variable**

A **discrete random variable** $X$ is a function that maps a finite or countably infinite sample space $S$ to the set of real numbers.
We define
$$\text{Pr}\{X = x\} = \sum_{s \in S : X(s) = x} \text{Pr}\{s\}.$$
The function $f(x) = \text{Pr}\{X = x\}$ is called the **probability mass function** of the random variable $X$.

**Handwritten Annotations:**
At the top of the slide, the mapping is explicitly written out in purple:
$X : S \rightarrow \mathbb{R}$

---

### Slides 27-28: Expected Value

**Expected Value**

The **expected value** is the average value of a random variable:
$$E[X] = \sum_x x \cdot \text{Pr}\{X = x\}.$$

**Exercise 7.1**
Consider a game in which we toss a pair of coins. For each heads you gain 3 points, and for each tails you lose 2 points. What is the expected value of your score?

**Handwritten Annotations (Solution on Slide 28):**
*Defining the sample space and random variable:*
$S = \{HH, HT, TH, TT\}$
$X(s) = \begin{cases}
+6, & \text{if } s = HH \\
+1, & \text{if } s \in \{HT, TH\} \\
-4, & \text{if } s = TT
\end{cases}$
*Calculating the Expectation:*
$E[X] = (+6) \cdot \frac{1}{4} + (+1) \cdot \frac{1}{2} + (-4) \cdot \frac{1}{4} = 1$

---

### Slides 29-32: Expected Value (Linearity)
*(Note: Combined from slides 29-32).*

**Expected Value (Linearity)**

Expected value is a linear operator$^{1}$:
$$E[X + Y] = E[X] + E[Y]$$

If $X$ is a random variable, then any function $g(x)$ defines a random variable $g(X)$.
If the expected value exists, then
$$E[g(X)] = \sum_x g(x) \cdot \text{Pr}\{X = x\}$$

🧩 How is it possible for an expected value $E[X]$ to not exist?

*Footnote:*
$^{1}$ Technically, linearity also includes $E[\alpha X] = \alpha E[X]$ for any scalar constant $\alpha$.

---

### Slides 33-35: Independent Random Variables
*(Note: Slide 35 has the final typed text. Slides 34 and 35 have different handwritten examples responding to the prompt).*

**Independent Random Variables**

Random variables $X$ and $Y$ are **independent** if knowing the value of one gives no information about the value of the other.

For discrete random variables, $X$ and $Y$ are independent if and only if
$$\text{Pr}\{X = x \text{ and } Y = y\} = \text{Pr}\{X = x\} \cdot \text{Pr}\{Y = y\}$$
for all values $x$ and $y$.

🧩 Can you give an example of two random variables that are *not* independent?

**Handwritten Annotations:**
*Example 1 (From Slide 34):*
$S = \{HH, HT, TH, TT\}$
$X(s) = \begin{cases} 1, & \text{if } s \in \{HH, HT\} \\ 0, & \text{otherwise} \end{cases}$
$Y(s) = \begin{cases} 1, & \text{if } s \in \{HH, TH\} \\ 0, & \text{otherwise} \end{cases}$
$\text{Pr}\{X=1 \cap Y=1\} = 1/4$
$\text{Pr}\{X=1\} = 1/2 \quad \text{Pr}\{Y=1\} = 1/2$
*(Note: In this specific example $1/4 = 1/2 \times 1/2$, meaning they ARE actually independent. The lecturer might have written this to test the class or corrected it verbally).*

*Example 2 (From Slide 35):*
$S = \{H, T\}$
$X(s) = \begin{cases} 1, & s=H \\ 0, & s=T \end{cases}$
$Y(s) = \begin{cases} 1, & s=T \\ 0, & s=H \end{cases}$
$\text{Pr}\{X=1 \cap Y=1\} = 0$
$\text{Pr}\{X=1\} = 1/2 \quad \text{Pr}\{Y=1\} = 1/2$
*(Since $0 \neq 1/2 \times 1/2$, these ARE dependent).*

---

### Slides 36-38: Expected Value of Independent Variables
*(Note: Combined from slides 36-38).*

**Expected Value of Independent Variables**

Let $X$ and $Y$ be discrete random variables.
* For any (not necessarily independent) $X$ and $Y$,
  $$E[X + Y] = E[X] + E[Y].$$
* If $X$ and $Y$ are **independent**, then
  $$E[XY] = E[X] \cdot E[Y].$$

These properties are heavily used in probabilistic analysis as we will see today.

---

### Slide 39: Probabilistic Analysis

**Probabilistic Analysis**
*(Section Header)*

---

### Slides 40-47: The Hiring Problem
*(Note: Combined from slides 40-47).*

**The Hiring Problem**

Imagine you want to improve a company process by automating it with an AI agent.
1. Currently the process is partially automated with a collection of scripts.
2. You want to replace this collection of scripts with an AI agent that would handle work requests better.
3. Preliminary **evaluation** (interview) of an AI agent takes some time.
4. **"Hiring"** an AI agent (reconfiguring scripts, updating documentation) takes even more time and resources.
5. Each (working) day you can evaluate one AI agent and either replace the current one or skip it.
6. Management is willing to invest in evaluating/replacing $n$ AI agents but wants to understand the total resources needed for the whole process.

How can we estimate the effort required for evaluating/updating $n$ AI agents?

---

### Slide 48: The Hiring Problem (Pseudocode)

**The Hiring Problem (Pseudocode)**

*Image Description:* A beige box containing pseudocode for the algorithm.
**HIRE-ASSISTANT(n)**
1  $best = 0$         **// candidate 0 is a least-qualified dummy candidate**
2  **for** $i = 1$ **to** $n$
3      interview candidate $i$
4      **if** candidate $i$ is better than candidate $best$
5          $best = i$
6          hire candidate $i$

**Figure 1:** Pseudocode for hiring an AI agent (Cormen et al. 2022, §5.1).

---

### Slide 49: The Hiring Problem (Worst- and Best-Case Analysis)

**The Hiring Problem (Worst- and Best-Case Analysis)**

Suppose evaluating an AI agent costs $c_c$, and hiring an AI agent costs $c_h$. In any case, we need to evaluate each candidate for a total cost of $c_c n$.
In the worst case, each next AI agent is better than the previous one. In this case the total cost of replacements is
$$T(n) = c_h n$$

In the best case, the first AI candidate turns out to be the best, and the total replacement cost is
$$T(n) = c_h$$

---

### Slides 50-54: Probabilistic Analysis (Idea)
*(Note: Combined from slides 50-54).*

**Probabilistic Analysis (Idea)**

**Probabilistic analysis** is the analysis of an algorithm or problem using probabilities of various events.
1. We need some knowledge about the distribution of input data.
2. **Expected running time** is computed by averaging the running time over all possible inputs.
3. Assumptions about the input distribution must be justified.
4. Sometimes it is not reasonable to specify an input distribution, in which case probabilistic analysis is not applicable.

---

### Slides 55-60: The Hiring Problem (Idea of Probabilistic Analysis)
*(Note: Combined from slides 55-60).*

**The Hiring Problem (Idea of Probabilistic Analysis)**

1. In theory, all candidates can be ordered by skill from $1$ to $n$.
2. Each order in which we evaluate candidates corresponds to a permutation of the numbers $1$ to $n$.
3. Evaluating candidates in a random order means that each such ordering is equally likely.
4. The worst case corresponds to the permutation $\langle 1, 2, \dots, n \rangle$.
5. The best case corresponds to the permutation $\langle n, n - 1, \dots, 1 \rangle$.

Probabilistic analysis of the hiring problem assumes a **uniform random permutation** (that is, each of the $n!$ permutations is equally likely).

---

### Slides 61-64: Indicator Random Variables
*(Note: Combined from slides 61-64).*

**Indicator Random Variables**

An **indicator random variable** $I\{A\}$ is defined as
$$I\{A\} = \begin{cases} 1 & \text{if event } A \text{ occurs,} \\ 0 & \text{if event } A \text{ does not occur.} \end{cases}$$

1. Indicator variables are defined so that probabilities are easy to compute.
2. Events are chosen so that they are independent.
3. Indicator variables make it easy to move from probabilities to expected values.

**Handwritten Annotations (from Slide 61):**
At the top: $I\{A\} : S \rightarrow \mathbb{R}$
At the bottom, expanding the definition mathematically:
$I\{A\}(s) = \begin{cases} 1, & \text{if } s \in A \\ 0, & \text{otherwise} \end{cases}$

---

### Slides 65-66: Indicator Random Variables (Lemma)

**Indicator Random Variables (Lemma)**

**Lemma (Cormen et al. 2022, Lemma 5.1)**
*Let $S$ be a sample space and $A$ an event in $S$, and let $X_A = I\{A\}$. Then $E[X_A] = \text{Pr}\{A\}$.*

**Proof.**
By the definition of an indicator random variable and the definition of expected value:
$$E[X_A] = E[I\{A\}]$$
$$= 1 \cdot \text{Pr}\{A\} + 0 \cdot \text{Pr}\{\overline{A}\}$$
$$= \text{Pr}\{A\},$$
where $\overline{A} = S - A$ is the complement of $A$. $\square$

**Handwritten Proof (from Slide 65):**
$E[X_A] = E[I\{A\}] = \sum_x x \cdot \text{Pr}\{I\{A\} = x\}$
$= 1 \cdot \text{Pr}\{I\{A\} = 1\} + 0 \cdot \text{Pr}\{I\{A\} = 0\}$
$= \text{Pr}\{A\}$

---

### Slides 67-76: Expected Value and Coin Tosses
*(Note: Combined from slides 67-76. The typed math derivation builds up over 10 slides. Slide 67 also contains a handwritten intuitive example).*

**Expected Value and Coin Tosses**

**Problem**
*When tossing a coin $n$ times, what is the expected number of heads?*

**Solution.**
Let $X_i = I\{\text{the } i\text{-th toss results in heads}\}$. Let $X$ be the random variable equal to the total number of heads in $n$ coin tosses. Then $X = \sum_{i=1}^n X_i$.
We want to compute the expected number of heads:

$$E[X] = E\left[ \sum_{i=1}^n X_i \right] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \frac{1}{2} = \frac{n}{2}$$ $\square$

**Handwritten Intuitive Solution (from Slide 67):**
A sequence is written out: `H H T T H T H`
An indicator sequence $X_i$ is mapped below it: `1 + 1 + 0 + 0 + 1 + 0 + 1 = 4 Heads`
$X_i = I\{\text{i-th coin toss} = H\}$
$E\left[ \sum_{i=1}^n X_i \right] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \text{Pr}\{\text{i-th coin toss} = H\}$
$= \sum_{i=1}^n \frac{1}{2} = \frac{n}{2}$

---

### Slides 77-88: The Hiring Problem (Probabilistic Analysis)
*(Note: Combined from slides 77-88. Slide 77 and 78 contain extensive handwritten work mapping out the probabilities which culminate in the final typed text on slide 88).*

**The Hiring Problem (Probabilistic Analysis)**

**Problem**
*When evaluating $n$ candidates, what is the expected number of replacements (hires) of AI agents?*

**Solution.**
Let $X_i = I\{\text{the } i\text{-th AI agent replaces the previous one}\}$. Let $X$ be the random variable equal to the total number of AI agent replacements over $n$ evaluations. Then $X = \sum_{i=1}^n X_i$. We also have $E[X_i] = \text{Pr}\{\text{the } i\text{-th AI agent is hired}\}$.
Any of the first $i$ candidates can turn out to be the best. Therefore, the probability that the $i$-th candidate is best is $\frac{1}{i}$.
$$E[X_i] = \frac{1}{i}$$
$$E[X] = E\left[ \sum_{i=1}^n X_i \right] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \frac{1}{i} = \Theta(\log n)$$

**Handwritten Derivations (from Slide 77):**
$X_i = I\{\text{i-th agent is hired}\}$
$E\left[ \sum_{i=1}^n X_i \right] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \text{Pr}\{\text{i-th agent is hired}\}$
$\text{Pr}\{\text{1st agent is hired}\} = 1$
$\text{Pr}\{\text{2nd agent is hired}\} = 1/2$
$\text{Pr}\{\text{3rd agent is hired}\} = 1/3$
$= \sum_{i=1}^n 1/i = \Theta(\log n)$

**Handwritten Scratchpad (from Slide 78):**
*(This slide shows the mathematical reasoning behind why $\text{Pr}\{\text{i-th agent is hired}\} = 1/i$)*
Top formula:
$\text{Pr}\{n\text{-th agent is hired}\} = \frac{(n-1)!}{n!} = \frac{1}{n}$
Underneath, an array is visualized:
$1 \quad 2 \quad 3 \dots n$
$2 \quad 1 \quad 3 \dots n$
$\text{Pr}\{(n-1)\text{-th agent is hired}\} = \frac{(n-2)! + (n-1)!}{n!} = \frac{(n-2)!(1 + (n-1))}{n!} = \frac{n}{n(n-1)} = \frac{1}{n-1}$
Below, permutations for $n=4$ are listed out manually to prove it empirically:
Column 1:
1 2 3 4
2 1 3 4
1 3 2 4
2 3 1 4
3 1 2 4
3 2 1 4
*(Certain numbers are circled in colors red, green, blue indicating if they trigger a "hire").*
Other columns list permutations starting with other numbers (1 2 4 3, 1 4 2 3, 4 1 2 3, etc.).
At the bottom left, the probabilities are tallied:
$Pr_1 = 1$
$Pr_2 = 12/24 = 1/2$
$Pr_3 = 8/24 = 1/3$
$Pr_4 = 6/24 = 1/4$

---

### Slide 89: Randomized Algorithms

**Randomized Algorithms**
*(Section Header)*

*Image Description:* The word "Quiz" is handwritten in large red letters in the center of the slide.

---

### Slides 90-92: Randomized Algorithms (Idea)
*(Note: Combined from slides 90-92).*

**Randomized Algorithms (Idea)**

1. To perform probabilistic analysis, we need information about the distribution of input data.
2. Randomized algorithms **take control** over the distribution of inputs, making probabilistic analysis more widely applicable.
3. In general, an algorithm is called **randomized** if its behavior is determined not only by the input but also by the values returned by a **random-number generator**.

---

### Slides 93-97: Randomized Hiring
*(Note: Combined from slides 93-97).*

**Randomized Hiring**

For the hiring problem (choosing an AI agent):
1. Probabilistic analysis showed that under the assumption of a uniformly random permutation of candidates, on average we need to hire $\Theta(\log n)$ agents.
2. However, in general we cannot assume such a distribution for the input order.
3. We can **impose** a convenient distribution by performing a random permutation of candidates **before** running the main algorithm.
4. With this modification, we can expect $\Theta(\log n)$ hires **for any** input order.

---

### Slide 98: Random Permutation of an Array (In Place)

**Random Permutation of an Array (In Place)**

*Image Description:* A beige box containing pseudocode.
**RANDOMLY-PERMUTE(A, n)**
1  **for** $i = 1$ **to** $n$
2      swap $A[i]$ with $A[\text{RANDOM}(i, n)]$

**Figure 2:** In-place random permutation (Cormen et al. 2022, §5.3).

---

### Slide 99: Randomized Quicksort

**Randomized Quicksort**
*(Section Header)*

---

### Slides 100-108: Quicksort (Recap)
*(Note: Combined from slides 100-108).*

**Quicksort (Recap)**

**Quicksort**:
1. is a "divide-and-conquer" algorithm;
2. runs in $\Theta(n \log n)$ on average but $\Theta(n^2)$ in the worst case;
3. is stable;
4. has an efficient in-place implementation.

The idea of the algorithm:
**Divide** Partition the input array into two parts (elements less than the pivot and elements greater than the pivot).
**Conquer** A single-element array is already sorted (no work needed).
**Combine** Concatenate the sorted subarrays and the pivot.

---

### Slide 109: Random Choice of Pivot

**Random Choice of Pivot**

*Image Description:* A beige box containing pseudocode.
**RANDOMIZED-PARTITION(A, p, r)**
1  $i = \text{RANDOM}(p, r)$
2  exchange $A[r]$ with $A[i]$
3  **return PARTITION**(A, p, r)

**Figure 3:** Random partition of an array (Cormen et al. 2022, §7.3).

---

### Slide 110: Randomized Quicksort

**Randomized Quicksort**

*Image Description:* A beige box containing pseudocode.
**RANDOMIZED-QUICKSORT(A, p, r)**
1  **if** $p < r$
2      $q = \text{RANDOMIZED-PARTITION}(A, p, r)$
3      **RANDOMIZED-QUICKSORT**(A, p, q - 1)
4      **RANDOMIZED-QUICKSORT**(A, q + 1, r)

**Figure 4:** Randomized quicksort (Cormen et al. 2022, §7.3).

---

### Slides 111-114: Comparisons and Running Time
*(Note: Combined from slides 111-114).*

**Comparisons and Running Time**

**Lemma (Cormen et al. 2022, Lemma 7.1)**
*Let $X$ be the total number of comparisons performed in PARTITION during the execution of QUICKSORT on an $n$-element array. Then the running time of QUICKSORT is $O(n + X)$.*

**Proof.**
Observe that PARTITION is called at most $n$ times, each time doing a fixed amount of work and some number of loop iterations. In each loop iteration, one comparison is performed. $\square$

To analyze the average-case running time of quicksort, we need to estimate $X$.

---

### Slides 115-121: Indicator Variables for Comparisons
*(Note: Combined from slides 115-121).*

**Indicator Variables for Comparisons**

Let
$$X_{ij} = I\{z_i \text{ is compared with } z_j\},$$

then $X = \sum_{i=1}^n \sum_{j=i+1}^n X_{ij}$.
Applying expected value to both sides, we obtain:

$$E[X] = E\left[ \sum_{i=1}^n \sum_{j=i+1}^n X_{ij} \right] = \sum_{i=1}^n \sum_{j=i+1}^n E[X_{ij}] = \sum_{i=1}^n \sum_{j=i+1}^n \text{Pr}\{z_i \text{ is compared with } z_j\}$$

What is the value of $\text{Pr}\{z_i \text{ is compared with } z_j\}$?

---

### Slide 122: Handwritten Scratchpad (Quicksort Pivot logic)

*Image Description:* This slide is entirely handwritten with red ink, demonstrating how a pivot splits an array.
At the top, elements are written: $a_1 \ a_2 \ a_3 \ \boxed{a_4} \dots a_{n-1} \ a_n$
Arrows point down from the boxed $\boxed{a_4}$ (acting as the pivot) splitting the array into left and right subtrees.
Left branch: $a_1 \ \boxed{a_4} \ a_2 \ a_3$ (highlighting $a_4$ again as a boundary). Below that, it splits further to $a_1, a_2$ and $a_3$.
Right branch: $a_2 \ \boxed{a_4} \ a_1, a_3$
The diagram visually explains that elements are only compared to the pivot. If a pivot is chosen *between* two values in sorted order, those two values will be sent to different branches and will *never* be compared to each other.

---

### Slides 123-127: Probability of Comparing Two Elements
*(Note: Combined from slides 123-127. Slide 124 contains a handwritten annotation).*

**Probability of Comparing Two Elements**

$\text{Pr}\{z_i \text{ is compared with } z_j\}$
$= \text{Pr}\{z_i \text{ or } z_j \text{ is the first pivot chosen from } Z_{ij}\}$
$= \text{Pr}\{z_i \text{ is the first pivot from } Z_{ij}\} + \text{Pr}\{z_j \text{ is the first pivot from } Z_{ij}\}$
$= \frac{1}{j - i + 1} + \frac{1}{j - i + 1}$
$= \frac{2}{j - i + 1}$

**Handwritten Annotation (from Slide 124):**
A red handwritten sequence clarifies the set $Z_{ij}$:
$Z_i \ Z_{i+1} \ \boxed{Z_{i+2}} \dots Z_{j-1} \ Z_j$
A brace underlines the entire sequence from $Z_i$ to $Z_j$.

---

### Slides 128-133: Expected Number of Comparisons
*(Note: Combined from slides 128-133 showing the full mathematical derivation).*

**Expected Number of Comparisons**

$$E[X] = E\left[ \sum_{i=1}^n \sum_{j=i+1}^n X_{ij} \right] = \sum_{i=1}^n \sum_{j=i+1}^n E[X_{ij}]$$
$$= \sum_{i=1}^n \sum_{j=i+1}^n \text{Pr}\{z_i \text{ is compared with } z_j\}$$
$$= \sum_{i=1}^n \sum_{j=i+1}^n \frac{2}{j - i + 1} \quad (k = j - i)$$
$$= \sum_{i=1}^n \sum_{k=1}^{n-i} \frac{2}{k + 1} < \sum_{i=1}^n \sum_{k=1}^{n-i} \frac{2}{k}$$
$$= \sum_{i=1}^n O(\log n) = O(n \log n)$$

---

### Slides 134-138: Randomized Quicksort (Summary)
*(Note: Combined from slides 134-138).*

**Randomized Quicksort (Summary)**

**Randomized quicksort**:
1. works similarly to ordinary quicksort;
2. uses a random choice of pivot;
3. has expected running time $\Theta(n \log n)$ (on **any** input);
4. still has worst-case running time $\Theta(n^2)$, but now the worst case depends not only on the input array but also on the random-number generator.

---

### Slide 139: Probabilistic Analysis of Bucket Sort

**Probabilistic Analysis of Bucket Sort**
*(Section Header)*

---

### Slides 140-147: Bucket Sort (Recap)
*(Note: Combined from slides 140-147).*

**Bucket Sort (Recap)**

**Bucket sort**:
1. *Assumption*: the input values are numbers, *uniformly distributed* over some interval (by default the interval $[0, 1)$), and we have a *cheap rounding operation*.
2. Idea of the algorithm:
   2.1 Divide the range of possible values into $n$ equal$^{2}$ subintervals.
   2.2 Put each value into the bucket corresponding to its subinterval (using rounding).
   2.3 Sort the values in each bucket (using insertion sort).
   2.4 Concatenate the sorted buckets.
3. Expected running time is $\Theta(n)$.

*Footnote:*
$^{2}$in probability

---

### Slides 148-152: Probabilistic Analysis of Bucket Sort
*(Note: Combined from slides 148-152).*

**Probabilistic Analysis of Bucket Sort**

The running time of bucket sort is dominated by sorting within the buckets:
$$\sum_{i=0}^{n-1} O(n_i^2)$$

The expected time spent sorting buckets is
$$E\left[ \sum_{i=0}^{n-1} O(n_i^2) \right] = \sum_{i=0}^{n-1} E[O(n_i^2)] = \sum_{i=0}^{n-1} O(E[n_i^2])$$

We will prove that
$$E[n_i^2] = 2 - \frac{1}{n}$$

---

### Slide 153: Probabilistic Analysis of Bucket Sort (Continued)

**Probabilistic Analysis of Bucket Sort (Continued)**

Let
$$X_{ij} = I\{A[j] \text{ falls into bucket } i\},$$

**Handwritten Diagram:**
*   On the left, an array labeled $A$ is drawn vertically, with indices running down. Inside one of the slots is an element $a_j$, pointed to by index $j$.
*   In the middle, an array representing $n$ buckets is drawn vertically. The index $i$ points to one of the buckets.
*   A red arrow flows from $a_j$ in array $A$ into bucket $i$.
*   Coming out of bucket $i$ is a linked list of nodes, containing elements like $\boxed{a_j}$, demonstrating how elements mapped to the same bucket are chained together.

---

### Slides 154-160: Probabilistic Analysis of Bucket Sort (Continued)
*(Note: Combined from slides 154-160. Slide 158 contains handwritten algebraic expansion rules).*

**Probabilistic Analysis of Bucket Sort (Continued)**

Let
$$X_{ij} = I\{A[j] \text{ falls into bucket } i\},$$
then $n_i = \sum_{j=1}^n X_{ij}$. We compute $E[n_i^2]$:

$$E[n_i^2] = E\left[ \left( \sum_{j=1}^n X_{ij} \right)^2 \right] = E\left[ \sum_{j=1}^n \sum_{k=1}^n X_{ij} X_{ik} \right]$$
$$= E\left[ \sum_{j=1}^n X_{ij}^2 + \sum_{1 \leq j \leq n} \sum_{1 \leq k \leq n, k \neq j} X_{ij} X_{ik} \right]$$
$$= \sum_{j=1}^n E[X_{ij}^2] + \sum_{1 \leq j \leq n} \sum_{1 \leq k \leq n, k \neq j} E[X_{ij} X_{ik}]$$

We now compute the two sums separately.

**Handwritten Note (from Slide 158):**
A reminder of how to expand the square of a sum:
$(a+b)^2 = a \cdot a + a \cdot b + b \cdot a + b \cdot b$
$= (a^2 + b^2) + (a \cdot b + b \cdot a)$

---

### Slides 161-167: Probabilistic Analysis of Bucket Sort (Continued)
*(Note: Combined from slides 161-167. Includes handwritten notes from slide 161).*

**Probabilistic Analysis of Bucket Sort (Continued)**

$$E[X_{ij}^2] = 1^2 \cdot \frac{1}{n} + 0^2 \cdot \left(1 - \frac{1}{n}\right) = \frac{1}{n}$$

$$E[X_{ij} X_{ik}] = E[X_{ij}]E[X_{ik}] = \frac{1}{n} \cdot \frac{1}{n} = \frac{1}{n^2}$$

🧩 Why is this step correct? *(Referring to $E[X_{ij} X_{ik}] = E[X_{ij}]E[X_{ik}]$)*

**Handwritten Derivation (from Slide 161):**
Explaining expected value of a squared indicator:
$E[X_{ij}^2] = \sum_{k=0,1} k^2 \cdot \text{Pr}\{X_{ij} = k\}$
(This justifies the formula for $E[X_{ij}^2]$ above, showing that squaring $1$ gives $1$, and squaring $0$ gives $0$).

---

### Slides 168-173: Probabilistic Analysis of Bucket Sort (Continued)
*(Note: Combined from slides 168-173).*

**Probabilistic Analysis of Bucket Sort (Continued)**

$$E[n_i^2] = \dots$$
$$= \sum_{j=1}^n E[X_{ij}^2] + \sum_{1 \leq j \leq n} \sum_{1 \leq k \leq n, k \neq j} E[X_{ij} X_{ik}]$$
$$= \sum_{j=1}^n \frac{1}{n} + \sum_{1 \leq j \leq n} \sum_{1 \leq k \leq n, k \neq j} \frac{1}{n^2}$$
$$= n \cdot \frac{1}{n} + n(n - 1) \cdot \frac{1}{n^2}$$
$$= 1 + \frac{n - 1}{n} = 2 - \frac{1}{n}$$

The expected running time of bucket sort is $n \cdot O(2 - 1/n) = \Theta(n)$.

---

### Slide 174: Randomly Built Binary Search Tree

**Randomly Built Binary Search Tree**
*(Section Header)*

---

### Slide 175: Binary Search Tree

**Binary Search Tree**

A **binary search tree** is a binary tree that satisfies the binary-search-tree property:
* For every node $x$ in the tree:
  * if $y$ is a node in the left subtree of $x$, then $y.\text{key} \leq x.\text{key}$;
  * if $z$ is a node in the right subtree of $x$, then $x.\text{key} \leq z.\text{key}$.

*Image Description:* A diagram of a binary search tree.
Root node: 5
Left child of 5: 1
Right child of 5: 7
Left child of 1: 0
Right child of 1: 3
Left child of 3: 2
Right child of 3: 4
Left child of 7: 6
Right child of 7: 8
Right child of 8: 9
**Figure 5:** Example of a binary search tree.

---

### Slides 176-177: Randomly Chosen Binary Search Tree

**Randomly Chosen Binary Search Tree**

**Exercise 7.2**
What is the expected height of a **randomly chosen** binary search tree
1. with 5 nodes?
2. with $n$ nodes?

**Handwritten Annotations and Diagrams (Across Slide 176 & 177):**
*(The lecturer is manually drawing different shapes of binary search trees to count permutations and heights).*
Slide 176 is filled with various handwritten skeletal trees (nodes represented by numbers 1 through 5, connected by lines) to exhaustively list shapes of BSTs.
Bracketed groupings show counts of trees with specific structures.
At the bottom, a sum is written:
$14 + 5 + 4 + 5 + 14 = 42$

*Slide 177 (Blank slide used for scratchpad calculations):*
Listing tree counts ($n$) vs total permutations:
$n=1 \rightarrow 1$
$n=2 \rightarrow 2$
$n=3 \rightarrow 5$
(Accompanied by drawings of the 2 trees for $n=2$, and the 5 trees for $n=3$).
$n=4 \rightarrow 5 + 2 + 2 + 5 = 14$
$n=5 \rightarrow 14 + 5 + 2 \cdot 2 + 5 + 14 = 42$
$n=6 \rightarrow 42 + 14 + 2 \cdot 5 + 25 + 14 + 42 = 122$
*(This is calculating the Catalan numbers, which represent the number of unique binary search tree shapes).*

---

### Slide 178: Randomly Built Binary Search Tree

**Randomly Built Binary Search Tree**

**Exercise 7.3**
What is the expected height of a **randomly built** binary search tree obtained by inserting keys one by one into an initially empty tree
1. 5 keys?
2. $n$ keys?

**Handwritten Annotations:**
A large equation written in red:
$$E[h] = 2 \cdot \frac{16}{24} + 3 \cdot \frac{8}{24} = \frac{4}{3} + \frac{3}{3} = 2 \frac{1}{3}$$
*(Note: 'h' is written above "expected height" in the prompt).*

Below this, for $n=4$, the permutations of `{1, 2, 3, 4}` are listed out and grouped. Next to each group, a small tree skeleton is drawn in green with orange highlighting to show what shape the tree takes when the numbers are inserted in that specific order.
Examples of the lists:
`1 2 3 4` $\rightarrow$ results in a straight right-leaning line tree (height 3).
`1 2 4 3` $\rightarrow$ results in a tree of height 3.
Groups of permutations are tallied up to calculate the probabilities of achieving specific tree heights, tying back into the $E[h]$ formula above.

---

### Slide 179: References

**References i**

Cormen, Thomas H et al. (2022). *Introduction to algorithms, Fourth Edition*. MIT press.