


Here is the complete line-by-line transcript of all provided files, with beautiful formatting, full descriptions for all images, and incremental/duplicate slides merged as requested.

***

# File 1: Theoretical Computer Science, Lab 

## Slide 1
**Theoretical Computer Science**
Lab Session 12
April 23, 2026
Innopolis University

## Slide 2
**Agenda**
▶ Context-Sensitive Grammars
▶ Unrestricted Grammars

## Slide 3
**Context-Sensitive Grammars (type 1)**
The rules of the form $\alpha A\beta \to \alpha\gamma\beta$, where $A$ is a non-terminal and $\alpha$, $\beta$ and $\gamma$ are strings of terminals and non-terminals.
1. $\gamma$ must be non-empty
2. The rule $S \to \epsilon$ is allowed if $S$ does not appear on the right side of any rule

**Example**
Generate language $\{a^n b^n c^n \mid n > 0\}$
1. $S \to aBC$
2. $S \to aSBC$
3. $CB \to CZ$
4. $CZ \to XZ$
5. $XZ \to XC$
6. $XC \to BC$
7. $aB \to ab$
8. $bB \to bb$
9. $bC \to bc$
10. $cC \to cc$

## Slide 4
**Exercises**
Define context-sensitive grammars that produce the following languages:
1. $L_1 = \{a^i b^j c^i d^j \mid i, j \ge 1\}$
2. $L_2 = \{WW \mid W \in \{a, b\}^*\}$

Homework:
3. $L_3 = \{W \in \{a, b, c\}^* \mid \#(a) = \#(b) = \#(c) \text{ and } \#(a) \ge 1\}$

## Slide 5
**Unrestricted Grammars (type 0)**
The rules of the form $\alpha \to \beta$, where $\alpha$ and $\beta$ are strings of non-terminals and terminals
1. The grammars without any limitation on production rules.
2. $\alpha$ at least have one non-terminal
3. $\alpha$ cannot be an empty string

## Slide 6
**Unrestricted Grammars (type 0)**
The rules of the form $\alpha \to \beta$, where $\alpha$ and $\beta$ are strings of non-terminals and terminals.

**Example**
Generate language $\{a^n b^n c^n \mid n > 0\}$
1. $S \to aBC$
2. $S \to aSBC$
3. $CB \to BC$
4. $aB \to ab$
5. $bB \to bb$
6. $bC \to bc$
7. $cC \to cc$

## Slide 7
**Exercises**
Generate Unrestricted grammars for below languages:
1. $L_1 = \{W \mid W = a^i \text{ and } i = 2^k \text{ and } k > 0\}$
2. $L_2 = \{a^n b^m c^n d^m \mid n > 0, m > 0\}$

Homework:
3. $L_3 = \{a^n b^{2n} c^{3n} \mid n \ge 1\}$

***

# File 2: Theoretical Computer Science, Tutorial 

## Slide 1
**Theoretical Computer Science**
Tutorial Weeks 14
Munir Makhmutov
Innopolis University

## Slides 2, 4, 11, 19 (Merged Agenda)
**Agenda**
*   **Chomsky Hierarchy**
    *   **Context-Sensitive Grammars (type 1)**
    *   **Unrestricted Grammars (type 0)**
*   **Summary**

## Slide 3
**Grammar: Definition**

**Definition**
A grammar is a tuple $\langle V_N, V_T, P, S \rangle$, where
*   $V_N$ is the non-terminal alphabet;
*   $V_T$ is the terminal alphabet;
*   $P \subseteq (V^* \cdot V_N \cdot V^*) \times V^*$ is the (finite) set of rewriting rules of production, where $V = V_N \cup V_T$;
*   $S \in V_N$ is a particular element called axiom or initial symbol.

## Slide 5
**Context-Sensitive Grammars (type 1)**

**Definition**
A Context-Sensitive grammar is a formal grammar $\langle V_N, V_T, P, S \rangle$ such that all the production rules in $P$ are in the following forms:
$$s_1 A s_2 \to s_1 \gamma s_2$$
where $A \in V_N$, $s_1, s_2, \gamma \in (V_T \cup V_N)^*$ and $\gamma \neq \epsilon$. If rule $S \to \epsilon$ is allowed, then $S$ does not appear on the right side of any rule.

**Note**
The order of production rules application is not predefined as in all other grammar types, but may lead to dead end. However, the latter does not always mean that the set of rules is invalid. Still, it has to be possible with some rule order to generate the words existing for the language. Obviously, non-existent words in the language should not be possible to generate.

## Slides 6-9 (Merged Incremental Derivation)
**Context-Sensitive Grammars (type 1)**

**Rules**
$$s_1 A s_2 \to s_1 \gamma s_2, \gamma \neq \epsilon$$

**Example**
Generate language $\{a^n b^n c^n \mid n > 0\}$
1. $S \to aBC$
2. $S \to aSBC$
3. $CB \to CZ$
4. $CZ \to WZ$
5. $WZ \to WC$
6. $WC \to BC$
7. $aB \to ab$
8. $bB \to bb$
9. $bC \to bc$
10. $cC \to cc$

$S \to aSBC \to aaSBCBC \to aaaBCBCBC \to ... \to aaaBBCBCC$
$(aaaBBCBCC) \to ... \to aaaBBBCCC$ $(aaaBBBCCC) \to$
$aaabBBCCC \to aaabbBCCC \to aaabbbCCC \to$
$\to aaabbbcCC \to aaabbbccC \to aaabbbccc$

## Slide 10
**Context-Sensitive Grammars (type 1)**

**Fact**
Context-Sensitive Grammars = LBA's Languages

**Definition**
A Non-deterministic Turing machine that uses only the tape space occupied by the input is called a linear-bounded automaton (LBA).

*[Image Description: A diagram of a Turing machine tape consisting of discrete cells. The visible cells contain the symbols: `<`, `x1`, `x2`, `...`, `xn`, `>`. Below the cells from `<` to `>`, a curly bracket embraces them with the red label "Working space in tape".]*

## Slide 12
**Unrestricted Grammars (type 0)**

**Definition**
A Unrestricted grammar is a formal grammar $\langle V_N, V_T, P, S \rangle$ such that all the production rules in $P$ are in the following forms:
$$\alpha \to \beta$$
where $\alpha, \beta \in (V_T \cup V_N)^*$, and $\alpha \notin V_T^*$, i.e., $\alpha$ has to contain at least one non-terminal symbol.

**Note**
As for Context-sensitive grammars some order of production rules application may lead to dead end and this does not always mean that the set of rules is invalid. Still, it has to be possible with some rule order to generate the words existing for the language.
Non-existent words in the language should not be generated.

## Slide 13
**Unrestricted Grammars (type 0)**

**Rules**
$$\alpha \to \beta$$
where $\alpha, \beta \in (V_T \cup V_N)^*$, $\alpha$ has to contain at least one non-terminal symbol.

**Example 1**
Generate language $\{a^n b^n c^n \mid n > 0\}$
1. $S \to aBC$
2. $S \to aSBC$
3. $CB \to BC$
4. $aB \to ab$
5. $bB \to bb$
6. $bC \to bc$
7. $cC \to cc$

$S \to aSBC \to aaBCBC \to aaBBCC \to aabBCC \to aabbCC \to aabbcC \to aabbcc$

## Slides 14-15 (Merged Incremental Derivation)
**Unrestricted Grammars (type 0)**

**Example 2**
Generate language $\{a^n b^n c^n d^n \mid n > 0\}$
1. $S \to aBCD$
2. $S \to aSBCD$
3. $CB \to BC$
4. $DB \to BD$
5. $DC \to CD$
6. $aB \to ab$
7. $bB \to bb$
8. $bC \to bc$
9. $cC \to cc$
10. $cD \to cd$
11. $dD \to dd$

$S \to aSBCD \to aaBCDBCD \to aaBCBDCD \to aaBBCDCD \to aaBBCCDD \to aabBCCDD \to aabbCCDD \to aabbcCDD \to aabbccDD \to aabbccdD \to aabbccdd$

## Slide 16
**Unrestricted Grammars (type 0)**

**Fact**
Unrestricted Grammars = Non-deterministic TM's Languages

**Definition**
A language is recognized by a non-deterministic TM is called recursively enumerable (computably enumerable).

## Slide 17
**Deterministic & Non-Deterministic TM**

Deterministic:
$$\delta : (Q - F) \times (I \cup \{\_\}) \times (\Gamma \cup \{\_\})^k \to Q \times (\Gamma \cup \{\_\})^k \times \{R, L, S\}^{k+1}$$

**Definition: Non-Deterministic TM (NTM)**
A NTM is a tuple $\langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$, where $Q, I, \Gamma, q_0, Z_0, F$ are defined as in DTM and the transition function is defined as
$$\delta : (Q - F) \times (I \cup \{\_\}) \times (\Gamma \cup \{\_\})^k \to$$
$$\to \mathbb{P}_F \left( Q \times (\Gamma \cup \{\_\})^k \times \{R, L, S\}^{k+1} \right)$$

## Slide 18
**Unrestricted Grammars (type 0)**

**Fact**
DTM = NTM = Unrestricted Grammars

## Slide 20
**Chomsky Hierarchy**

| | Rules | Comments |
|---|---|---|
| **type 3** | $A \to b$ <br> $A \to bB$ | $b \in V_T \cup \{\epsilon\}$ |
| **type 2** | $A \to \beta$ | $\beta \in (V_T \cup V_N)^*$ |
| **type 1** | $s_1 A s_2 \to s_1 \gamma s_2$ | $s_1, s_2, \gamma \in (V_T \cup V_N)^*$ <br> and $\gamma \neq \epsilon$ |
| **type 0** | $\alpha \to \beta$ | $\alpha, \beta \in (V_T \cup V_N)^*$ <br> and $\alpha \notin V_T^*$ |

$A, B \in V_N$, i.e., they are non-terminal symbols

## Slide 21
**Chomsky Hierarchy**

Classification of grammars by Chomsky: four types according to the form of production rules.
(type 3) Regular grammars
(type 2) Context-Free grammars
(type 1) Context-Sensitive grammars
(type 0) Unrestricted grammars

*[Image Description: An Euler diagram composed of four concentric circles showing the containment of language classes. The outermost circle is labeled "unrestricted". Inside it is "context-sensitive". Inside that is "context-free". The innermost circle is labeled "regular".]*

## Slide 22
**Grammars, Languages and Automata**

| Chomsky hierarchy | Grammars | Languages | Minimal automaton |
|---|---|---|---|
| Type-0 | Unrestricted | Recursively enumerable | Turing machine |
| Type-1 | Context-sensitive | Context-sensitive | LBA |
| Type-2 | Context-free | Context-free | NDPDA |
| Type-3 | Regular | Regular | FSA |

## Slide 23
**Machines**

*[Image Description: A flowchart mapping the equivalence and hierarchical relationship of formal languages, machines, and grammars.
Horizontal bidirectional arrows map equivalences:
- DFSA $\leftrightarrow$ NFSA $\leftrightarrow$ RegExp $\leftrightarrow$ RG
- DPDA $\to$ NPDA $\leftrightarrow$ CFG
- LBA $\leftrightarrow$ CSG
- TM $\leftrightarrow$ NTM $\leftrightarrow$ UG
Vertical arrows denote subset hierarchies pointing downwards:
- DFSA $\to$ DPDA $\to$ LBA $\to$ TM
- RegExp $\to$ CFG $\to$ CSG $\to$ UG
An additional diagonal arrow goes from NPDA to LBA.]*

## Slide 24
Thank you for your attention!

***

# File 3: Theoretical Computer Science, Lecture

## Slide 1
**Theoretical Computer Science**
**Halting Problem**
**(Проблема остановки)**
Lecture 13 - Manuel Mazzara

## Slide 2
**Halting Problem**
*   Given a **program** and an **input to the program**, determine if the given program **will eventually stop** with this particular input

*[Image Description: A flowchart demonstrating the Halting Problem. A block labeled "Input" and another block labeled "Program" both point to a central box titled "Program Example and SampleData". This box has an arrow pointing to a block labeled "SolvesHaltingProblem", which then has an arrow pointing to the output block. The output block gives two possibilities: "Halts" or "Loops". The labels below align "Input" with the first box, "Program" with the middle, and "Output" with the rightmost box.]*

## Slide 3
**Remarks**
*   Whether a **particular program** halts on a **particular input** or not is computable in many cases
*   A test to find this out for **all possible combinations of programs and inputs does not exist**
*   From the formal and intuitive proof, you will see that <span style="color:red">**programs that analyse programs can be made to analyse themselves, leading to the impossibility**</span>
    *[Callout pointing to "analyse themselves"]: Self-reference

## Slide 4
This is <span style="color:red">statical analysis</span> of a <span style="color:red">behavioral property</span> of a program

## Slide 5
**Halting Problem, formally (1)**
*   The "<span style="color:red">**halting problem**</span>":
    *   I build a **program**
    *   I give it some **input** data
    *   I know that in general the program might not terminate its execution ("*run into a loop*")
$\to$ Can I determine **in advance (statically)** if this will occur?
*   This problem can be expressed in terms of TMs:
    *   Given a function:
        $g(y,x) = 1$ **if** $f_y(x) \neq \bot$, $g(y,x) = 0$ **if** $f_y(x) = \bot$
        *[Callout pointing to $\bot$]: Undefined
        *   [Callout pointing to $y$]: Goedel number

$\to$ <span style="color:red">**Is there a TM that computes $g$?**</span>

## Slide 6
**Halting Problem, formally (2)**
There is no TM which can compute the ***total*** function **$g$**:
$\mathbb{N} \times \mathbb{N} \to \{0,1\}$ defined as:

$g(y,x)=$ **if** $f_y(x) \neq \bot$ **then 1**
**else 0**
*   [Callout pointing to the word ***total***]: Total means that the TM will never loop!

*   $f_y(x) \neq \bot$ means that $M_y$ comes to halt in a final state on reading $x$ so that $f_y(x)$ is defined

## Slide 7
**Informally**

<div style="text-align: center; color: red; font-weight: bold;">
No TM can decide, for <u>any</u> TM M and <u>any</u> input x,<br>
whether M halts on input x
</div>

*   No TM can decide whether any TM will halt in a final state for any input value
*   **It is always possible to build a TM that will eventually terminate if and only if it reaches a final state (<u>emulation</u>)**
    *   **This is probably the first "naïve" implementation of the HP you may think of (but it works only for positive answers)**

## Slide 8
**No <span style="color:orange">computer program</span> can decide, for <u>any</u> computer program C and <u>any</u> input x, whether <span style="color:orange">C halts</span> on x**

*   [Callout pointing to the text]: What is valid for TMs is also valid for computer programs (Church-Turing thesis)

## Slide 9
**Formal proof of undecidability of HP (1)**
*   Let us **assume (<u>by contradiction</u>)** that the following function is computable:

    **$g(y,x) =$ if $f_y(x) \neq \bot$ then $1$ else $0$**

*   On top of **$g$** let us define **$h$**:
    *[Callout pointing to $h(x)$ and $g(x,x)$]: Self reference

    **$h(x) =$ if $g(x,x) = 0$ then $1$ else $\bot$**

    *   $g(x,x) = 0$ corresponds to **$f_x(x) = \bot$**

## Slide 10
**Formal proof (2)**

**$g(y,x) =$ if $f_y(x) \neq \bot$ then $1$ else $0$**
**$h(x) =$ if $g(x,x) = 0$ then $1$ else $\bot$**

*   **<u>If $g$ is computable then $h$ is computable too</u>**
*   **<u>$h$ is just "calling/using" $g$, it does not alter computability in any way</u>**
    *   [Callout pointing to the text]: Allow me please the programming terminology

## Slide 11
**Formal proof (3)**

*   If **$h$** is computable then **$h = f_{x_0}$** for some **$x_0$**
    *[Callout pointing to $f_{x_0}$]: Some TM with Gödel number X0
*   Let us compute **$h$** in **$x_0$**
    *[Callout pointing to $h$ in $x_0$]: Diagonalization: TM X0 on input X0

*   [Callout pointing to the two bullets below]: By definition of h there are only two possible cases, 1 and $\bot$, we analyze both
*   **$h(x_0) = \color{red}{f_{x_0}(x_0) = 1}$ if $g(x_0, x_0) = 0$**
*   **$g(x_0, x_0) = 0$ if $\color{red}{f_{x_0}(x_0) = \bot} \to \text{ \color{red}{contradiction}}$**

*   **$h(x_0) = \color{red}{f_{x_0}(x_0) = \bot}$ if $g(x_0, x_0) = 1$**
    *   [Callout pointing to this equation]: By definition of h
*   **$g(x_0, x_0) = 1$ if $\color{red}{f_{x_0}(x_0) \neq \bot} \to \text{ \color{red}{contradiction}}$**
    *   [Callout pointing to this equation]: By definition of g

## Slide 12
**The original assumption on the computability of g has to be false**

*[Image Description: A reproduction of the famous painting "The Scream" by Edvard Munch, showing a distorted, agonizing figure holding its face against a swirling red, orange, and blue sky. The text is overlaid on the painting.]*

## Slide 13
**Decidable vs undecidable**
*   **A TM that computes this $g(y,x)$ does not exist**
    *   That's why a computer (which is a program) <span style="color:red">**cannot warn us that our program will run into an infinite loop on certain data**</span> (while it can easily signal a missing "}")
*   Some example:
    *   Determining if an arithmetic expression is **well parenthesized is a solvable (<span style="color:red">decidable</span>)** problem (PDA)
    *   Determining if any given program will **run into an infinite loop on any given input** is an algorithmically unsolvable (<span style="color:red">**undecidable**</span>) problem (no TM can do)

## Slide 14
**Theoretical Computer Science**
**Halting Problem - intuitively**
Lecture 13 - Manuel Mazzara

## Slide 15
Let us try to build the same proof using programming notation instead of mathematical

*[Image Description: A close-up photograph of a computer screen displaying colorful lines of code (HTML/JavaScript) on a black background. The text snippet "Let us try to build..." is overlaid on the right side of the image.]*

## Slide 16
**Halting problem, intuitively (1)**
*   Suppose we have a program "*halts*" which analyses a program **p** running with input **x**, and **always answers** whether or not the evaluation of **p(x)** will stop

```javascript
halts(p(x)) =
    if magical_analysis(p(x)) then yes
    else no
```

## Slide 17
**Halting problem, intuitively (2)**
*   If "*halts*" covers every possible program and input, we can write another program that answers only about **program-checking programs when they check themselves**

```javascript
halts_on_self(p) =
    if halts(p(p)) then yes
    else no
```
*   [Callout pointing to `p(p)`]: Self reference

## Slide 18
**Halting problem, intuitively (3)**
*   We can easily make a program run forever on purpose, so we can also write one which does that when a program-checking program halts on itself

```javascript
trouble(p) =
    if halts_on_self(p) then loop forever
    else yes
```

## Slide 19
**Halting problem, intuitively (4)**
*   Let us consider "*trouble*" checking itself
*   Two evaluations of *trouble(trouble)* with contradicting results

```javascript
trouble(trouble) =
    if halts_on_self(trouble) then loop forever
    else yes
```
*   [Callout pointing to the code block]: For the definition of trouble(p)

*   It should be *semantically equivalent* to the program:

```javascript
trouble(trouble) =
    if halts(trouble(trouble)) then loop forever
    else yes
```
*[Callout pointing to the code block `trouble(trouble)` definition]: For the definition of halts_on_self(p)
*[Callout pointing to `loop forever` and `yes` being mutually exclusive]: Contradiction!

## Slide 20
**Do you see why magical_analysis cannot exist?**

## Slide 21
**Another take on HP**

*[Image Description: A black-and-white comic panel (in the style of xkcd). Inside a box, it shows pseudo-code:
`DEFINE DOESITHALT(PROGRAM):`
`{`
`    RETURN TRUE;`
`}`
Below the code, the caption reads: "THE BIG PICTURE SOLUTION TO THE HALTING PROBLEM".]*

## Slide 22
**A physical perspective**
*   According to our current understanding of physics, *given enough time, any program will halt due to factors external to the actual program*:
    *   Sooner or later, electricity will give out
    *   The memory containing the program will get corrupted by cosmic rays
    *   Corrosion will eat away the silicon in the CPU
    *   The second law of thermodynamics will lead to the end of universe

## Slide 23
**Computers are physical systems: what they can and cannot do is ultimately dictated by the laws of physics**

## Slide 24
**Theoretical Computer Science**
**Rice's theorem: spoiler!**
Lecture 13 - Manuel Mazzara

## Slide 25
**Rice's Theorem**
Henry Gordon Rice, 1951

## Slide 26
**Theorems whose gist is diagonalization are everywhere in computability and complexity theory**

## Slide 27
**Rice's Theorem**
*   <span style="color:red">**Rice's theorem is the most important impossibility result of Theoretical Computer Science**</span>
*   "*All <u>non-trivial</u>, <u>semantic properties</u> of programs are <u>undecidable</u>*"
*   **Software Verification** is about working around it

## Slide 28
For all (non-trivial), <span style="color:red">**semantic**</span> properties of programs it is impossible to construct an algorithm that always leads to <span style="color:red">**a correct yes-or-no answer**</span> to the question on whether the program satisfies the property or not

## Slide 29
Non-trivial means that the property is true for <span style="color:red">*some*</span> program, but not for all or none

## Slide 30
*[Image Description: A photograph of a bald man in a black suit, leaning forward and resting his forehead completely flat on the keyboard of an open silver laptop on a white desk, conveying deep frustration or exhaustion. There is no text on this slide.]*

## Slide 31
**What to do?**
*   **It is impossible to fully automatize software verification**
*   **Software verification is about engineering workaround to the fundamental problems**
*   **Approximate solutions exist and we can still live our life!**

## Slides 32, 42, 49 (Merged Diagram)
*[Image Description: A multi-layered circular Venn diagram depicting formal languages and complexity classes.
- The innermost gray circle is labeled "FSM (Regular Sets)" with examples "$0^n 1^n$" (Wait, the example inside is crossed out or separated, it shows $0^n 1^n$ is outside regular sets). The text inside FSM actually just says "Regular Sets".
- The next purple dashed layer is "DCFL" and "CFL", containing an example "$0^n 1^n \cup 0^m 1^m$".
- These layers are contained in a larger white circle labeled "DECIDABLE", containing "Recursive Sets" with example "$0^n 1^n 0^n$".
- Outside DECIDABLE is a larger blue circle labeled "Undecidable (Partially Decidable)" representing "Recursively Enumerable" or "Turing Recognizable / Acceptable". Examples here include "Halting Problem" (Answers YES, if Yes. No answer, if No) and "Post Correspondence Problem".
- The outermost red circle is labeled "Not Partially Decidable", "NOT Recursively Enumerable". This area holds "Complement of RE Sets".]*

## Slide 33
**This is our next stop!**

*[Image Description: A black-and-white photograph of a hitchhiker walking away down an empty road. The hitchhiker has a large backpack and a cardboard sign stuck to the back that reads "NOWHERE IN PARTICULAR" with a hand pointing left.]*

## Slide 34
**Theoretical Computer Science**
**Decidability vs. Semidecidability**
Lecture 13 - Manuel Mazzara

## Slide 35
**Decision problem**
*   A <span style="color:red">**decision problem**</span> is a question that has two possible answers
    *   **yes or no**
    *   You should have seen the definition of a "*decision problem*" when you studied NP-complete problems in **Complexity Theory**

**Examples:**
*   Does an algorithm terminate for a specific input?
*   Given a graph G and a set of vertices K, is K a clique?
*   Given a set of axioms, a set of rules, and a formula, is the formula provable under the axioms and rules?

## Slide 36
**Semidecidability**
*   A problem is <span style="color:red">**semidecidable**</span> if there is **<u>an algorithm that says yes if the answer is yes</u>**
    *   **however it may loop infinitely if the answer is no**
*   Let us consider again the example of the halting problem in a TM
    *   It is **semidecidable**!
    *   If the TM stops with that input, we will find out!
*   **Decidable problem**: there exists an algorithm that always halts with a "yes" or "no" answer

## Slide 37
**Remarks**
*   There is a significant number of problems that are **not decidable, but that are semidecidable**
    *   Typical example: <span style="color:red">**runtime errors detection in programs**</span>
    *   We can detect the error if it occurs (by running the program and waiting), but **we cannot decide its absence in finite time for all programs**
*   The semidecidable problem is the presence of the error not its absence!
*   Important implications on verification by testing
    *   Famous statement by Dijkstra: "**testing can prove the presence of errors, not their absence**"
    *   **Need of other verification tools**

## Slide 38
**Recursive sets (1)**
*   Let us focus on the problems stated in such a way that the answer is **binary**
*   Problem = **does x belong to set S? (where $S \subseteq \mathbb{N}$ )**
    *   Computational problems can be (re)phrased in such a way
    *   Does the program (or input) belong to a certain set $S \subseteq \mathbb{N}$?
*   <span style="color:red">**Characteristic function**</span> of a set S:
    <div style="text-align: center; color: red; font-weight: bold;">
    $c_S(x) =$ if $x \in S$ then $1$ else $0$
    </div>

## Slide 39
**Recursive sets (2)**
*   A set S is **<u><span style="color:red">recursive</span></u> (or decidable)** if and only if **its characteristic function is <u>computable</u>**
*   **$c_s$** is in the class of **$\mu$-recursive** functions (see the definition as homework)
*   Computability theory was originally called "recursion theory" (Skolem [1923], Gödel [1931], Kleene [1936], Church [1936])
*   $\mu$-recursive functions were later proved to be the same class as functions computed by TMs (**Church–Turing thesis**) forming the foundation of what was originally called recursion theory

## Slide 40
**Recursively enumerable**
*   S is <span style="color:red">**<u>recursively enumerable</u>**</span> **(RE) (or semidecidable)** if and only if:
    *   **S is the empty set**, or
    *   <span style="color:red">**S is the image of a total, computable function $g_S$**</span>
    <div style="text-align: center; color: red; font-weight: bold;">
    $S = I_{gS} = \{x \mid x=g_S(y), y \in \mathbb{N}\} \implies S = \{g_S(0), g_S(1), g_S(2), ...\}$
    </div>

*   The term "recursively enumerable" comes from this "enumeration" and the term "semidecidable" can be explained intuitively
*   If $x \in S$ then, by **enumerating the elements of S, sooner or later one finds x and is able to get a correct (yes) answer** to the question; but what if $x \notin S$?

## Slide 41
**Recursive sets**

## Slides 43, 53 (Merged Diagram)
**Recursively enumerable sets in context**

*[Image Description: An Euler diagram of language classes with text mapping formalisms to them.
- Innermost circle: Regular languages (FA: finite state automaton, RE: regular expression, RG: regular grammar).
- Second circle: Context-free languages (PDA: pushdown automaton, CFG: context-free grammar).
- Third circle: Context-sensitive languages (LBA: linear-bounded automaton, CSG: context-sensitive grammar).
- Fourth circle: Decidable languages (recursive languages) mapped to "TM that halts".
- Fifth circle: Turing recognizable languages (recursively enumerable languages) mapped to "TM: Turing machine". On Slide 53, this specific label is highlighted with a red box and a red question mark "?".
- Outermost space: Non-Turing recognizable languages (non-recursively enumerable languages).]*

## Slide 44
**Basic results about recursive sets**
*   **<u>Theorem 1:</u> If S is recursive, then it is also RE (see the diagram)**
    *   <span style="color:red">**Decidable is more demanding than semidecidable**</span>
    *   **See the diagram: strict inclusion**
*   **<u>Theorem 2:</u> S is recursive if and only if both S itself and its complement $S^{\wedge} = \mathbb{N}-S$ are RE**
    *   Two "*semidecidabilities*" make a "*decidability*"
    *   Here, answering NO to a problem is equivalent to (i.e., it is as difficult as) answering YES to its complement
    *   <span style="color:red">**<u>Corollary: the class of decidable sets is closed under complement</u>**</span>

## Slide 45
Answering NO to a problem is equivalent to answering YES to its complement. This is true for "limited" computational models. Do you remember the attention we put on closure over complement?

## Slide 46
**Proof of <u>Theorem 1</u>**
<span style="color:red">**Recursive -> RE**</span>
*   If S is empty, it is RE by definition
*   If $S \neq \emptyset$, let **$c_S$** be its **characteristic function**
    *   since $S \neq \emptyset$, $\exists\ k \in S$, that is **$c_S(k) = 1$**
    Let us define the generating function $g_S$ as follows:
    <div style="text-align: center; font-weight: bold;">
    $g_S(x) =$ if $c_S(x) = 1$ then $x$ else $k$
    </div>
    **$g_S$ is total and computable, and $I_{gS} = S$**
    $\to$ **S is RE**
    *[Callout pointing to $c_S$ being the characteristic function]: Being the set recursive, the characteristic function is computable
    *   [Callout pointing to $g_S$]: Given the characteristic function we can define the generating function
*   This is a **non-constructive proof**:
    *   We do not know if $S \neq \emptyset$
    *   We do not require an algorithm to find a proper $k$
    *   We just know that $g_S$ exists if $S \neq \emptyset$: this is enough for us!

## Slide 47
**Proof of <u>Theorem 2</u> (1)**
<span style="color:red">**(1) S recursive $\to$ both S and S^ RE and**</span>
<span style="color:red">**(2) both S and S^ RE $\to$ S recursive**</span>

(1.1) S recursive $\to$ S RE (from Theorem 1)
*[Callout pointing to S recursive $\to$ S RE]: Being the set recursive, the characteristic function is computable

(1.2) S recursive $\to$
**$c_S(x)$ ($= 1$ if $x \in S$, $c_S(x) = 0$ if $x \notin S$)** computable $\to$
**$c_{S^{\wedge}}(x)$ ($= 0$ if $x \in S$, $c_S(x) = 1$ if $x \notin S$)** computable $\to$
S^ recursive $\to$
S^ RE
*[Callout pointing to $c_{S^{\wedge}}(x)$ computable]: Just swapping 1s and 0s, and we get the characteristic function of the complement

## Slide 48
**Proof of <u>Theorem 2</u> (2)**
<span style="color:red">**S and S^ RE $\to$ S recursive**</span>

S RE $\to$ construct the enumeration **$S=\{g_S(0), g_S(1), g_S(2), ...\}$**
S^ RE $\to$ construct **$S^{\wedge}=\{g_{S^{\wedge}}(0), g_{S^{\wedge}}(1), g_{S^{\wedge}}(2), ...\}$**
*   [Callout pointing to the enumerations]: Two enumerations for S and its complement

$S \cup S^{\wedge} = \mathbb{N}$, $S \cap S^{\wedge} = \emptyset$ (<span style="color:red">**partition of $\mathbb{N}$**</span>) $\to$
**$\forall x \in \mathbb{N}, \exists y \mid x=g_{S^{\wedge}}(y) \lor x=g_S(y) \land \sim (\exists z \mid x=g_{S^{\wedge}}(z) \land x=g_S(z))$**
*   [Callout pointing to the logical statement]: The two enumerations have no overlap

*   <span style="color:red">**x belongs to one and only one of the two enumerations $\to$**</span>

The enumeration **$\{g_S(0), g_{S^{\wedge}}(0), g_S(1), g_{S^{\wedge}}(1), g_S(2), g_{S^{\wedge}}(2), ...\}$** certainly contains any x:
*   if x is at an odd position, then $x \in S$,
*   if it is at an even position then $x \in S^{\wedge}$.
*   <u>**$c_s$** can be computed</u>

## Slide 50
**With great power comes great...**

## Slide 51
**With Great Power Comes Great Uncomputability!**
*   Turing machines and equivalent models of computation are **<u>more powerful</u>** than FSA and PDA
*   This power is gained via **<u>features that can cause programs to loop infinitely</u>**
*   If we want the power, **<u>we must accept the looping</u>**

## Slide 52
**Recursively enumerable sets**

## Slide 54
**Theorem**
*   Consider the set S with the following features:
    *   $i \in S \to f_i$ total (i.e., **S contains only indexes of total computable functions**)
    *   $f$ total and computable $\to \exists\ i \in S \mid f_i = f$ (i.e., **S contains all of them**)

    *   <span style="color:red">**S is the set of all and only total computable functions**</span>
    *   <span style="color:red">**S is not RE**</span>
    *   Provable by diagonalization (homework)

## Slide 55
**Implications (1)**
*   <span style="color:red">**There is no RE formalism (Automata, grammars, TMs ...) that can define all computable total functions, and only them**</span>
*   FSA define total computable functions, but <u>not all of them</u>
    *   Model with predetermined fixed memory is less powerful than typical programming languages
*   TMs define all computable functions, but <u>including also the non-total ones</u>
    *   **Non termination as a features of programming languages**

## Slide 56
**Implications (2)**
*   C programming language allows coding any algorithm, including the non-terminating ones (Turing-powerful)
*   **<u>There is no subset of C that defines exactly *all and only* the terminating programs</u>**
*   The set of C programs in which **loops comply with given constraints guaranteeing termination** includes terminating programs only, but necessarily **<u>not all terminating programs</u>**

## Slide 57
**There is no RE formalism (Automata, grammars, TMs ...) that can define all computable total functions, and only them**

*[Image Description: A large slide layout. On the left side is a solid light-blue checkmark. On the right side, in the background, is a massive, faint light-blue "X" cross. The text is centered between them.]*