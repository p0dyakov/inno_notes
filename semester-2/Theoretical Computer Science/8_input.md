Here is the complete, carefully formatted transcript of the documents provided. As requested, progressive "animated" slides that build upon each other have been merged into their final version to provide a clean reading experience, and all images have been fully described.

***

# File 1: Theoretical Computer Science - Lab Session 7

## Slide 1
**Theoretical Computer Science**
Lab Session 7

March 19, 2026

*[Image description: The logo for Innopolis University, featuring stylized, modern typography.]*

## Slide 2
**Agenda**

*   **Turing Machine:**
    *   formal definition;
    *   example;
    *   exercises.

## Slide 3
**Turing Machine.**

## Slide 4
**Turing Machine**
### Formal Definition

A Turing Machine (TM) with k-tapes is a tuple

$$T = \langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$$

where
*   $Q$ is a finite set of states;
*   $I$ is the input alphabet;
*   $\Gamma$ is the memory alphabet;
*   $\delta$ is the transition function;
*   $q_0 \in Q$ is the initial state;
*   $Z_0 \in \Gamma$ is the initial memory symbol;
*   $F \subseteq Q$ is the set of final states.

## Slide 5
**Transition Function**

The transition function is defined as
$$\delta : (Q - F) \times (I \cup \{\_\}) \times (\Gamma \cup \{\_\})^k \rightarrow Q \times (\Gamma \cup \{\_\})^k \times \{R, L, S\}^{k+1}$$

where elements of $\{R, L, S\}$ indicate "directions" of the head of the TM:
*   **R** : move the head one position to the right;
*   **L** : move the head one position to the left;
*   **S** : stand still.

**Remarks:**
*   the transition function can be partial;
*   no transition outgoing from the final states;
*   the symbol $\_ \notin \Gamma \cup I$ is a special blank symbol on the tapes.

## Slide 6
**Moves**

Moves are based on
*   one symbol read from the input tape,
*   $k$ symbols, one for each memory tape,
*   state of the control device.

**Actions**
*   Change state.
*   Write a symbol replacing the one read on each memory tape.
*   Move the $k + 1$ heads.

## Slide 7
**Moves: Graphically**

*[Image description: A state diagram showing two circular nodes representing states labeled $q$ and $q'$. An arrow points from $q$ to $q'$ representing a transition. The arrow is labeled with the complex text: $i, \langle A_1, A_2, . . . , A_k \rangle / \langle A'_1, A'_2, . . . , A'_k \rangle, \langle M_0, M_1, . . . , M_k \rangle$]*

*   $q \in Q - F$ and $q' \in Q$
*   $i$ is the input symbol,
*   $A_j$ is the symbol read from the $j^{th}$ memory tape,
*   $A'_j$ is the symbol replacing $A_j$,
*   $M_0$ is the direction of the head of the input tape,
*   $M_j$ is the direction of the head of the $j^{th}$ memory tape.

where $1 \leq j \leq k$

## Slide 8
**Configuration**

A configuration (a snapshot) $c$ of a TM with $k$ memory tapes is the following $(k + 2)$-tuple:

$$c = \langle q, x\uparrow y, \alpha_1\uparrow\beta_1, . . . , \alpha_k\uparrow\beta_k \rangle$$

where
*   $q \in Q$
*   $x \in (I \cup \{\_\})^*$, $y = y' \cdot \_$ with $y' \in I^*$
*   $\alpha_r \in (\Gamma \cup \{\_\})^*$ and $\beta'_r = \beta'_r \cdot \_$ with $\beta'_r \in \Gamma^*$ and $1 \leq r \leq k$
*   $\uparrow \notin I \cup \Gamma$

## Slide 9
**Acceptance Condition**

If $T = \langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$ is a TM and $s \in I^*$, $s$ is accepted by $T$ if
$$c_0 \vdash^* c_F$$

where
1.  $c_0$ is an initial configuration defined as
    $c_0 = \langle q_0, \uparrow s, \uparrow Z_0, . . . , \uparrow Z_0 \rangle$ where
    *   $x = \epsilon$
    *   $y = s\_\,$
    *   $\alpha_r = \epsilon, \beta_r = Z_0$, for any $1 \leq r \leq k$.
2.  $c_F$ is a final configuration defined as
    $c_F = \langle q, s'\uparrow y, \alpha_1\uparrow\beta_1, . . . , \alpha_k\uparrow\beta_k \rangle$ where
    *   $q \in F$
    *   $x = s'$

$L(T) = \{s \in I^* \mid x \text{ is accepted by } T\}$

## Slide 10
**Example: Language $A^nB^nC^n$**

A TM $T$ that recognises the language $A^nB^nC^n = \{a^n b^n c^n \mid n > 0\}$

*[Image description: A state machine diagram containing five states: $q_0$ (start state), $q_1$, $q_2$, $q_3$, and $q_F$ (final state, indicated by a double circle).]*
*   *An arrow labeled "start" points to $q_0$.*
*   *Transition from $q_0$ to $q_1$: `a, Z0/Z0, ⟨S, R⟩`*
*   *Self-loop on $q_1$: `a, _/M, ⟨R, R⟩`*
*   *Transition from $q_1$ to $q_2$: `b, _/_, ⟨S, L⟩`*
*   *Self-loop on $q_2$: `b, M/M, ⟨R, L⟩`*
*   *Transition from $q_2$ to $q_3$: `c, Z0/Z0, ⟨S, R⟩`*
*   *Self-loop on $q_3$: `c, M/M, ⟨R, R⟩`*
*   *Transition from $q_3$ to $q_F$: `_, _/_, ⟨S, S⟩`*

## Slide 11
**Exercises**

Build TMs that recognise the following languages:
*   $L_1 = \{wcw \mid w \in \{a, b\}^+\}$
*   $L_2 = \{wcw^R \mid w \in \{a, b\}^+\}$, where $w^R$ is the reversed string $w$.
*   $L_3 = \{w \mid w \in \{a, b\}^*\}$, where $w$ is a palindrome.
*   $L_4 = \{a^n b^n \mid n \geq 0\} \cup \{a^n b^{2n} \mid n \geq 0\}$

## Slide 12
**Homework**

Build TM that recognise the following language:
*   $L_5 = \{(ab)^n \mid n \geq 0\}$
*   $L_6 = \{a^n b^{2n} c^{3n} \mid n \geq 0\}$

***

# File 2: Theoretical Computer Science - Tutorial Week 9

## Slide 1
**Theoretical Computer Science**
Tutorial Week 9

Munir Makhmutov

*[Image description: Innopolis University logo]*

## Slide 2
**Agenda**

**Turing Machine**
*   Formal definition
*   Examples

## Slide 3
**FSA**

*[Image description: Two images and a diagram are shown. The top-left image is a close-up of a mechanical combination lock or adding machine showing numbered dials. The bottom-left image is the internal rotating dial mechanism of a safe. The right side shows a Finite State Automaton (FSA) state diagram.]*
*   *The diagram has three states: $q_0$ (start state), $q_1$, and $q_2$ (final state, double circle).*
*   *Start arrow points to $q_0$.*
*   *Self-loop on $q_0$ with input `b`.*
*   *Transition from $q_0$ to $q_1$ with input `a`.*
*   *Transition from $q_1$ to $q_0$ with input `b`.*
*   *Transition from $q_1$ to $q_2$ with input `a`.*
*   *Self-loop on $q_2$ with input `a`.*
*   *Transition from $q_2$ to $q_0$ with input `b`.*

## Slide 4
**Pushdown Automata**

*[Image description: Two images and a diagram. The top-left image shows a hand inserting a coin into a vending machine/payment terminal slot. The bottom-left image shows a stacked pile of copper coins. The right side shows a Pushdown Automaton (PDA) state diagram.]*
*   *The diagram has four states: $q_0$ (start state), $q_1$, $q_2$, and $q_3$ (final state, double circle).*
*   *Start arrow points to $q_0$.*
*   *Transition from $q_0$ to $q_1$: `a, Z0/AZ0`*
*   *Self-loop on $q_1$: `a, A/AA`*
*   *Transition from $q_1$ to $q_2$: `b, A/A`*
*   *Self-loop on $q_2$: `a, A/ε`*
*   *Transition from $q_2$ to $q_3$: `ε, Z0/Z0`*

## Slide 5
**Turing Machine**

*[Image description: Black and white portrait photos of Alonzo Church (left) and Alan Turing (right).]*

**Turing thesis (Church–Turing thesis)**
A function on the natural numbers can be calculated by an effective method if and only if it is computable by a Turing machine.

## Slide 6
**Turing Machine**

*[Image description: A photograph of a beautifully constructed physical representation of a Turing machine. It features a continuous white paper tape feeding from a spool on the right, passing through a mechanical read/write head assembly in the center (illuminated by an LED, with visible gears and mechanisms), and rolling onto a spool on the left.]*

## Slide 7
**Turing Machine**

*[Image description: Three distinct images representing the evolution of computing hardware. Top left: A hand-drawn sketch of an intricate, hypothetical mechanical device operating on a long paper tape filled with 1s and 0s. Bottom left: A generic modern sleek desktop computer and monitor. Right: A photograph of an early, massive room-sized electromechanical computer (likely the British Bombe machine), showing its complex back-panel wiring and dials.]*

## Slide 8
**Turing Machine**

*[Image description: The same hand-drawn sketch of an intricate mechanical Turing machine from the previous slide. It shows mechanical gears, a bell, and a paper tape moving through it. The tape has binary digits (1, 0) printed on it.]*

$\leftarrow L \quad S \quad R \rightarrow$

## Slides 9-13 (Animated Build Merged)
**Example of TM**

*[Image description: A Turing Machine state diagram with states $q_0$ (start), $q_1$, $q_2$, and $q_F$ (final, double circle).*
*   *Start arrow to $q_0$.*
*   *Transition $q_0$ to $q_1$: `a, Z0/Z0, ⟨S, R⟩`*
*   *Self-loop on $q_1$: `a, _/M, ⟨R, R⟩`*
*   *Transition $q_1$ to $q_2$: `b, _/_, ⟨S, L⟩`*
*   *Self-loop on $q_2$: `b, M/M, ⟨R, L⟩`*
*   *Transition $q_2$ to $q_F$: `_, Z0/Z0, ⟨S, S⟩`*

*"input str", "tape / tape", ⟨"head str", "head tape"⟩*
*(Note: As the slides progress, different parts of the transition strings are highlighted in red to explain the syntax. The final slide highlights "head tape".)*

## Slide 14
**Agenda**

**Turing Machine**
*   **Formal definition**
*   Examples

## Slide 15
**FSA (Formal Definition)**

**Definition**
A (complete) Finite State Automaton is a tuple $\langle Q, \Sigma, \delta, q_0, F \rangle$, where
*   $Q$ is a finite set of *states*;
*   $\Sigma$ is a finite *input alphabet*;
*   $\delta : Q \times \Sigma \rightarrow Q$ is a (total) *transition* function;
*   $q_0 \in Q$ is the *initial* state;
*   $F \subseteq Q$ is the set of *accepting* states.

## Slide 16
**PDA (Formal Definition)**

**Definition**
A (Deterministic) Pushdown Automaton (PDA) is a tuple $\langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$, where
*   $Q$ is a finite set of states;
*   $I$ is finite input alphabet;
*   <span style="color:red">$\Gamma$ is finite stack alphabet;</span>
*   <span style="color:red">$\delta : Q \times (I \cup \{\epsilon\}) \times \Gamma \rightarrow Q \times \Gamma^*$</span> is the (partial) transition function;
*   $q_0 \in Q$ is the initial state;
*   <span style="color:red">$Z_0 \in \Gamma$ is the initial stack symbol;</span>
*   $F \subseteq Q$ is the set of accepting states.

## Slide 17
**Turing Machine**

**Formal Definition**
A (Deterministic) Turing Machine (TM) (with 1-tape) is a tuple
$$T = \langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$$

where
*   $Q$ is a finite set of states;
*   $I$ is the input alphabet;
*   <span style="color:red">$\Gamma$ is the memory alphabet;</span>
*   <span style="color:red">$\delta : (Q - F) \times (I \cup \{\_\}) \times (\Gamma \cup \{\_\}) \rightarrow Q \times (\Gamma \cup \{\_\}) \times \{R, L, S\}^2$</span> is the transition function;
*   $q_0 \in Q$ is the initial state;
*   <span style="color:red">$Z_0 \in \Gamma$ is the initial memory symbol;</span>
*   $F \subseteq Q$ is the set of final states.

## Slide 18
**Turing Machine**

**Special symbols**
*   **R** : move the head one position to the right
*   **L** : move the head one position to the left
*   **S** : stand still
*   **\_** : a special blank symbol on the tapes

## Slide 19
**Turing Machine**

**Formal Definition**
A (Deterministic) Turing Machine (TM) (with k-tapes) is a tuple
$$T = \langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$$

where
*   $Q$ is a finite set of states;
*   $I$ is the input alphabet;
*   <span style="color:red">$\Gamma$ is the memory alphabet;</span>
*   <span style="color:red">$\delta$ is the transition function;</span>
*   $q_0 \in Q$ is the initial state;
*   <span style="color:red">$Z_0 \in \Gamma$ is the initial memory symbol;</span>
*   $F \subseteq Q$ is the set of final states.

## Slide 20
**Transition Function**

The transition function is defined as
$$\delta : (Q - F) \times (I \cup \{\_\}) \times (\Gamma \cup \{\_\})^k \rightarrow Q \times (\Gamma \cup \{\_\})^k \times \{R, L, S\}^{k+1}$$

**Remarks:**
*   the transition function can be partial;
*   no transition outgoing from the final states;
*   the symbol $\_ \notin \Gamma \cup I$ is a special blank symbol on the tapes.

## Slide 21
**Moves**

Moves are based on
*   state of the control device,
*   one symbol read from the input tape,
*   $k$ symbols, one for each memory tape.

**Actions**
*   Change state,
*   Write a symbol replacing the one read on each memory tape,
*   Move the $k + 1$ heads.

## Slide 22
**Moves: Graphically**

*[Image description: Same state diagram shown in File 1 Slide 7. Node $q$ transitions to node $q'$ via an edge labeled with variables representing inputs, tape reads/writes, and head movements.]*

*   $q \in Q - F$ and $q' \in Q$
*   $i$ is the input symbol,
*   $A_j$ is the symbol read from the $j^{th}$ memory tape,
*   $A'_j$ is the symbol replacing $A_j$,
*   $M_0$ is the direction of the head of the input tape,
*   $M_j$ is the direction of the head of the $j^{th}$ memory tape.

where $1 \leq j \leq k$

## Slide 23
**Configuration**

A configuration (a snapshot) $c$ of a TM with $k$ memory tapes is the following $(k + 2)$-tuple:
$$c = \langle q, x\uparrow y, \alpha_1\uparrow\beta_1, . . . , \alpha_k\uparrow\beta_k \rangle$$

where
*   $q \in Q$
*   $x \in (I \cup \{\_\})^*$, $y = y' \cdot \_$ with $y' \in I^*$
*   $\alpha_r \in (\Gamma \cup \{\_\})^*$ and $\beta_r = \beta'_r \cdot \_$ with $\beta'_r \in \Gamma^*$ and $1 \leq r \leq k$
*   <span style="color:red">$\uparrow \notin I \cup \Gamma$ is the tape symbol</span>

## Slide 24
**Acceptance Condition**

If $T = \langle Q, I, \Gamma, \delta, q_0, Z_0, F \rangle$ is a TM and $s \in I^*$,
$s$ is accepted by $T$, if $c_0 \vdash^* c_F$

where
1.  $c_0 = \langle q_0, \uparrow s, \uparrow Z_0, . . . , \uparrow Z_0 \rangle$ is an <span style="color:red">initial configuration</span>
2.  $c_F = \langle q, x\uparrow y, \alpha_1\uparrow\beta_1, . . . , \alpha_k\uparrow\beta_k \rangle$ is a <span style="color:red">final configuration</span>, if $q \in F$

$L(T) = \{s \in I^* \mid s \text{ is accepted by } T\}$

## Slide 25
**Agenda**

**Turing Machine**
*   Formal definition
*   **Examples**

## Slides 26-33 (Animated Build Merged)
**Example 1: Language $A^nB^n = \{a^nb^n \mid n > 0\}$**

*[Image description: A state machine diagram containing four states: $q_0$ (start state), $q_1$, $q_2$, and $q_F$ (final state, indicated by a double circle).]*
*   *Transition from $q_0$ to $q_1$: `a, Z0/Z0, ⟨S, R⟩`*
*   *Self-loop on $q_1$: `a, _/M, ⟨R, R⟩`*
*   *Transition from $q_1$ to $q_2$: `b, _/_, ⟨S, L⟩`*
*   *Self-loop on $q_2$: `b, M/M, ⟨R, L⟩`*
*   *Transition from $q_2$ to $q_F$: `_, Z0/Z0, ⟨S, S⟩`*

*(The sequence below traces the execution of the machine for input "aabb" across the configurations)*

$\langle q_0, \uparrow aabb, \uparrow Z_0 \rangle \vdash$
$\langle q_1, \uparrow aabb, Z_0\uparrow \rangle \vdash$
$\langle q_1, a\uparrow abb, Z_0M\uparrow \rangle \vdash$
$\langle q_1, aa\uparrow bb, Z_0MM\uparrow \rangle \vdash$
$\langle q_2, aa\uparrow bb, Z_0M\uparrow M \rangle \vdash$
$\langle q_2, aab\uparrow b, Z_0\uparrow MM \rangle \vdash$
$\langle q_2, aabb\uparrow, \uparrow Z_0MM \rangle \vdash$
$\langle q_F, aabb\uparrow, \uparrow Z_0MM \rangle$

$c_0 \vdash c_1 \vdash c_2 \vdash c_3 \vdash c_4 \vdash c_5 \vdash c_6 \vdash c_7 = c_F$
$c_0 \vdash^* c_F$

## Slides 34-43 (Animated Build Merged)
**Example 2: Language $A^nB^nC^n = \{a^nb^nc^n \mid n > 0\}$**

*[Image description: A state machine diagram containing five states: $q_0$ (start state), $q_1$, $q_2$, $q_3$, and $q_F$ (final state, indicated by a double circle).]*
*   *Transition from $q_0$ to $q_1$: `a, Z0/Z0, ⟨S, R⟩`*
*   *Self-loop on $q_1$: `a, _/M, ⟨R, R⟩`*
*   *Transition from $q_1$ to $q_2$: `b, _/_, ⟨S, L⟩`*
*   *Self-loop on $q_2$: `b, M/M, ⟨R, L⟩`*
*   *Transition from $q_2$ to $q_3$: `c, Z0/Z0, ⟨S, R⟩`*
*   *Self-loop on $q_3$: `c, M/M, ⟨R, R⟩`*
*   *Transition from $q_3$ to $q_F$: `_, _/_, ⟨S, S⟩`*

*(The sequence below traces the execution of the machine for input "aabbcc". It shows the progression state by state)*

$\dots \vdash$
$\langle q_2, aa\uparrow bbcc, Z_0M\uparrow M \rangle \vdash$
$\langle q_2, aab\uparrow bcc, Z_0\uparrow MM \rangle \vdash$
$\langle q_2, aabb\uparrow cc, \uparrow Z_0MM \rangle \vdash$
$\langle q_3, aabb\uparrow cc, Z_0\uparrow MM \rangle \vdash$
$\langle q_3, aabbc\uparrow c, Z_0M\uparrow M \rangle \vdash$
$\langle q_3, aabbcc\uparrow, Z_0MM\uparrow \rangle \vdash$
$\langle q_F, aabbcc\uparrow, Z_0MM\uparrow \rangle$

## Slides 44-53 (Animated Build Merged)
**Example 2: Language $A^nB^nC^n = \{a^nb^nc^n \mid n > 0\}$**

*(This is a continuation of the visual trace shown in the previous block. The slides repeatedly show the states turning red to track progress. We will represent the final visible trace on Slide 53).*

$\dots \vdash$
$\langle q_3, aabbcc\uparrow, Z_0MM\uparrow \rangle \vdash$
$\langle q_F, aabbcc\uparrow, Z_0MM\uparrow \rangle$

## Slide 54
**Summary**

**Turing Machine**
*   Formal definition
*   Examples

## Slide 55
**Thank you for your attention!**

***

# File 3: Theoretical Computer Science - Lecture 8 (Manuel Mazzara)

## Slide 1
**Theoretical Computer Science**

**Automata Theory and Models of Computation**
Lecture 8 - Manuel Mazzara

## Slide 2
**Who is him?**

*[Image description: A detailed classical illustration/engraving of the bust of Homer, featuring his curly hair, beard, and characteristic blind gaze.]*

## Slide 3
**Homer**

*   Real character vs. mythological (850 BCE?)
*   *Iliad* and *Odyssey*
*   Believed to be the first and greatest of the epic poets
*   **Author of the first known literature of Europe**
*   Why should we mention him?

## Slide 4
**Automata Theory**

It regards:
*   The study of <span style="color:red">abstract mathematical machines</span> (automata)
*   The <span style="color:red">computational problems</span> that can be solved by them

Automaton (singular), Automata (plural)

Latinization of the Greek αὐτόματον (automaton): *self-moving*
*   something is doing something by itself

**The word automaton was first used by Homer**
*   describing automatic door opening
*   automatic movement of wheeled tripods
*   moving statues...

## Slide 5
**Why studying Automata Theory?**

An automaton is a ***finite*** representation of a formal language that may be ***infinite***

**Theoretical models for computing machines** to be used for proofs about computability

## Slide 6
**Model of computation**

*   **A mathematical model of computation** describes how
    *   a set of **outputs are computed** given a set of inputs
    *   units of computations, memories, and communications are **organized**

*   Theory: **automata theory, computability** and **computational complexity**

*   Practice: **system specification**, compiler construction...

## Slide 7
**Different Models of computation**

*   Sequential
    *   <span style="color:red">Finite state automata</span>
    *   <span style="color:red">Pushdown automata</span>
    *   Turing Machine
*   Functional
    *   Lambda calculus
*   Concurrent
    *   Petri nets
    *   ...
*   **This list is not even close to be exhaustive**

## Slide 8
**Example: FSA**

*   **Simple model of computation**
*   **Limited expressiveness**
    *   Fixed memory
*   Suitable to "brute force" analysis
    *   **Model Checking**

*[Image description: A Finite State Automaton state diagram featuring four states: S1 (start), S2, S3, and S4 (final, double circle).*
*   *Start arrow points to S1.*
*   *S1 to S2 on input 'a'.*
*   *Self-loop on S2 on input 'a'.*
*   *S2 to S1 on input 'b'.*
*   *S2 to S4 on input 'c'.*
*   *S3 to S1 on input 'a'.*
*   *S3 to S4 on input 'b'.*
*   *S4 to S3 on input 'd'.]*

## Slide 9
**Applications**

*   FSA have several applications

*   **Moore/Mealy** machines model computer circuits or electronic devices
    *   Mealy machines are **finite state transducers**
    *   The have both input and output tape

*   Finite State Automata have a major application in compilers construction
    *   **Lexical Analysis**

## Slide 10
**General Structure of a Compiler**

*[Image description: A block diagram detailing the phases of a compiler.*
*   *Source Program enters -> Lexical Analysis -> (tokens) -> Syntax Analysis -> (Parse tree) -> Semantic Analysis -> (Parse tree + data type information) -> Code generation -> Code optimization.*
*   *A large blue arrow labeled "FSA" points up into Lexical Analysis.*
*   *A large blue arrow labeled "NPDA" points down into Syntax Analysis.*
*   *All central blocks interface down with a "Symbol Table" block.]*

<span style="color:red">**You will study this in Compilers course**</span>

## Slide 11
**Theoretical Computer Science**

**FSA for System Design and Verification**
Lecture 8 - Manuel Mazzara

## Slide 12
Finite State Automata can be used for <span style="color:red">analysis and design</span> of systems

*[Image description: Two graphics: one small blue icon of a human head containing three gears, and one large faded grey icon of a human head containing two gears.]*

## Slide 13
**UML state machines**

*   The **Unified Modeling Language** has a notation for describing state machines
*   This notation can be used for **analysis and design** of part of a system

*[Image description: A UML state machine diagram inside a boundary labeled `stm TemperatureController`. There is a solid black circle indicating the starting point leading to an "Idle" state. From "Idle", if it gets "Too cold", it transitions to "Heating". If "OK", it returns to "Idle". From "Idle", if "Too hot", it transitions to "Cooling". If "OK", it returns to "Idle". Both "Heating" and "Cooling" can transition to an "Error" state if an "Error" occurs. The "Error" state transitions back to "Idle" when "Error removed".]*

## Slide 14
**Coin Operated Toilet Turnstiles**

*[Image description: On the left, a photograph of a stainless steel automated turnstile with a coin slot. On the right, a finite state machine diagram showing two states: "Locked" and "Un-locked". A black start dot points to "Locked". Pushing when locked loops back to "Locked" (Push). Inserting a coin transitions to "Un-locked" (Coin). When Un-locked, inserting a coin loops back to "Un-locked" (Coin). Pushing transitions back to "Locked" (Push).]*

## Slide 15
Would you be able to use FSA to design <ins>Innopolis University Turnstile system</ins>?

*[Image description: A blue icon depicting a teacher or presenter pointing at a presentation board.]*

## Slide 16
*[Image description: A 3D architectural render of modern, sleek glass barrier turnstiles (speed gates), typical of modern office buildings or universities.]*

## Slide 17
Is FSA all you need?
Is there anything missing?
What and Why?

*[Image description: A large blue circle icon containing a white question mark.]*

## Slide 18
**FSA and Software Verification**

*   FSAs are also used for Software Verification (in some of their variants)
*   The term **Software Model-Checking** denotes techniques to <span style="color:red">**automatically verify real programs based on finite-state models of them**</span>
*   The work received the <ins>**Turing Award**</ins>

## Slide 19
*[Image description: A screenshot of an ACM Turing Award biography page for Edmund Melson Clarke (United States - 2007). A photo of Clarke, a bearded man with glasses, is on the left. The citation reads: "Together with E. Allen Emerson and Joseph Sifakis, for their role in developing Model-Checking into a highly effective verification technology that is widely adopted in the hardware and software industries." Portions of the text under "Birth and education" are highlighted, indicating his switch from mathematics to computer science and his studies under Robert Constable, a pioneer in mathematical logic and computing.]*

## Slide 20
**The Program Verification Problem**

*   The very nature of universal (Turing-complete) computation entails the <span style="color:red">**impossibility of deciding automatically the program verification problem**</span>
    *   **<ins>Rice's theorem</ins>** (we will see this in detail)

*   <span style="color:red">**The <ins>Program Verification problem</ins> is generally undecidable, but it is decidable over finite state machines**</span>
    *   What does all this mean?

## Slide 21
**Program Verification: limits**

P: a program $\Updownarrow$ TM(P): a Turing machine
S: a specification $\Updownarrow$ F(S): a first-order formula

Does TM(P) $\vDash$ F(S) hold?

<span style="color:red">**UNDECIDABLE**</span>

## Slide 22
**What can be done?**

*   Restricting the expressiveness of:
    *   the computational model
    *   the specification language

*   **The verification problem may become <span style="color:red">decidable</span>**

*   Model Checking operates restricting the expressiveness of the computational model (From TMs to FSAs)

## Slide 23
We will cover these aspects in details in the final part of the course

*[Image description: A blue icon depicting a teacher or presenter pointing at a presentation board.]*

## Slide 24
Today's lecture is about connecting the dots...

*[Image description: A 5-panel comic strip illustration. Panel 1 (Data): Random scattered colored dots. Panel 2 (Information): The dots are now color-coded. Panel 3 (Knowledge): Lines connect the dots into a complex network. Panel 4 (Insight): One specific path through the network is highlighted. Panel 5 (Wisdom): The highlighted path avoids dead ends and successfully navigates through the network.]*

## Slide 25
**Theoretical Computer Science**

**Alan Turing**
Lecture 8 - Manuel Mazzara

## Slide 26
"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human."

*[Image description: Large quote marks surrounding the text]*

## Slide 27
Who Said That?

## Slide 28
*[Image description: On the left, a movie poster for "The Imitation Game" featuring Benedict Cumberbatch. On the right, a diagram illustrating the Turing Test: A computer (A) and a human (B) are behind a partition. A human interrogator (C) communicates with both via typed messages on paper to determine which is the machine.]*

## Slide 29
**Alan Turing**

<ins>23 June 1912 – 7 June 1954</ins>

Major contributions in:
*   **Computability**
*   **Cryptography**
*   **Artificial Intelligence**
*   **Bioinformatics**

*[Image description: A black and white portrait photo of a young Alan Turing smiling.]*

## Slide 30
Turing's home at Wilmslow (UK)

*[Image description: A circular blue historical plaque mounted on a brick wall. Text on plaque: "ALAN TURING 1912 - 1954 Founder of computer science and cryptographer, whose work was key to breaking the wartime Enigma codes, lived and died here."]*

## Slide 31
*[Image description: A map of the United Kingdom and Ireland, with a red location pin dropped on Wilmslow, just south of Manchester.]*

## Slide 32
Turing machine (<ins>Computability</ins>)

*[Image description: A 3D illustration of an abstract Turing machine head processing a looping strip of paper tape divided into squares.]*

## Slide 33
Decision Problem (<ins>Computability</ins>)

*[Image description: A cropped image of the title header of an academic paper. It reads: "ON COMPUTABLE NUMBERS, WITH AN APPLICATION TO THE ENTSCHEIDUNGSPROBLEM By A. M. TURING. [Received 28 May, 1936.—Read 12 November, 1936.]"]*

## Slide 34
Defeat of Enigma (<ins>Cryptography</ins>)

*[Image description: Two images side-by-side. Left: A high-quality photo of a real German Enigma machine with its lid open, showing the keyboard, plugboard, and rotors. Right: A still from the movie "The Imitation Game" showing a replica Enigma machine sitting on a large wooden desk in a war room.]*

## Slide 35
**WWII and Turing**

*   Turing worked for the **Government Code and Cypher School** (GC&CS)
    *   Britain's codebreaking centre

*   He led **Hut 8**, section responsible for German naval **cryptanalysis**
    *   He devised a number of techniques for speeding the breaking of German ciphers

*   **Turing played a pivotal role in cracking intercepted coded messages**

## Slide 36
**The history in a few points**

*   **<ins>Enigma</ins>** was a German enciphering machine used to send messages securely
*   The main focus of Turing was in <ins>**cracking the ‘Enigma’ code**</ins>
*   <ins>**Polish mathematicians**</ins> had worked out how to read Enigma messages and had shared this information with the British
*   The Germans increased its security at the outbreak of war by <ins>**changing the cipher system daily**</ins>
*   **Alan Turing** and **Gordon Welchman** designed a machine (“the Bombe”) so that, from mid-1940, German Air Force signals were being read and the intelligence gained from them was helping the war effort

## Slide 37
**A good reading**

*   <ins>**Dermot Turing**</ins> is Alan’s nephew
*   Behind major achievements there is <ins>**always a team**</ins>
*   For example, this books give credits to the *team* of *polish mathematicians* who worked with Turing

*[Image description: Book cover for "XYZ & Z: THE REAL STORY OF HOW ENIGMA WAS BROKEN" by Dermot Turing. The cover features large letters X, Y, and Z patterned with the flags of France, Britain, and Poland respectively.]*

## Slide 38
Turing test (<ins>AI</ins>)

*[Image description: A blue rectangular graphic containing the text: "A computer would deserve to be called intelligent if it could deceive a human into believing that it was human. - Alan Turing"]*

## Slide 39
Seminal Turing’s article on AI

*[Image description: A scan of the cover and first paragraph of a journal article. Title: "MIND: A QUARTERLY REVIEW OF PSYCHOLOGY AND PHILOSOPHY. VOL. LIX. No. 236. October, 1950. I.—COMPUTING MACHINERY AND INTELLIGENCE. By A. M. TURING." The first section is highlighted, starting with "1. The Imitation Game. I PROPOSE to consider the question, 'Can machines think?'..."]*

## Slide 40
*[Image description: A black background slide. On the left is the standard portrait of Alan Turing. To the right, white text reads: "I propose to consider the question, 'Can machines think?' (Alan Turing)"]*

## Slide 41
*(Note: This slide is a visual duplicate of Slide 28)*

*[Image description: On the left, a movie poster for "The Imitation Game" featuring Benedict Cumberbatch. On the right, a diagram illustrating the Turing Test: A computer (A) and a human (B) are behind a partition. A human interrogator (C) communicates with both via typed messages on paper.]*

## Slide 42
*[Image description: A collage of three elements. Left: An etching of Ada Lovelace next to a graphic showing a human head silhouette overlapping a mechanical/circuit head silhouette, next to a photo of Alan Turing. Below them is the quote: "Let us return for a moment to Lady Lovelace's objection, which stated that the machine can only do what we tell it to do." - Alan Turing. Right: A vintage cover of TIME magazine showing a woman's face made of circuit boards and gears, with the bold red text "Can Machines Think? They already do, say scientists. So what (if anything) is special about the human mind?"]*

## Slide 43
<ins>Bioinformatics</ins> before Bioinformatics

*[Image description: An excerpt of an academic paper. Header: "THE CHEMICAL BASIS OF MORPHOGENESIS. By A. M. TURING, F.R.S. University of Manchester (Received 9 November 1951—Revised 15 March 1952)". The abstract text discusses chemical substances called morphogens and reaction-diffusion systems explaining patterns in biology. A bottom paragraph is highlighted: "The purpose of this paper is to discuss a possible mechanism by which the genes of a zygote may determine the anatomical structure of the resulting organism..."]*

## Slide 44
**Theoretical Computer Science**

**The historical background of Turing Machines**
Lecture 8 - Manuel Mazzara

## Slide 45
Computers *Before* Computers (1930s)
Hierarchy of calculation workers

*[Image description: A black and white historical photograph of a massive room filled with rows of desks. Dozens of women are seated at these desks, operating mechanical calculation machines or typewriters in a factory-like setting.]*

## Slide 46
*[Image description: Another black and white historical photograph from a similar angle. A sign hangs from the ceiling reading "COMPUTING DIVISION COMPUTING SECTION". Rows of women are operating heavy mechanical calculators.]*

## Slide 47
**Human computers**

*   19th and 20th century, until about 1946
    *   <ins>**industrial organization of computational labour**</ins>
    *   <ins>**information as an industrial material**</ins>

*   “*Pen and paper*” industrialization of mathematics
    *   "*computing factories*"
    *   *Hierarchy* based on other forms of industrialization

*   **ENIAC** (Electronic Numerical Integrator and Computer)
    *   the first programmable, electronic, **<ins>general-purpose</ins>** digital computer (1945)
    *   <ins>**digital information as an industrial material**</ins>: the **punch card**

## Slide 48
*[Image description: A famous historical black and white photograph showing two women ("human computers" or programmers) wiring the ENIAC. The machine is a massive wall-to-wall installation of black panels covered in dials, switches, and thick bundles of black cables that the women are plugging in.]*

## Slide 49
**Computation**

*   People did not have computers in the 1930s
    *   Yet they needed them

*   Scientists, engineers, businesses, and government agencies faced growing mountains of tedious, repetitive computations

*   Many inventors worked on the automation of these tasks
    *   Here we will discuss the work of a man that worked on modelling the idea of computations
    *   Why?

## Slide 50
**Turing machine (1)**

*   The Turing machine (TM) is the historical model of “computer”
    *   simple
    *   conceptually important
*   TMs use <ins>**tapes**</ins> as memory
    *   Tapes are <span style="color:red">**not destructive**</span>
    *   They can be read many times

## Slide 51
**Turing Machine (2)**

*   It is intended <ins>**to emulate the human behavior when computing**</ins>
*   Limits of mechanical computation are in common with “*human computation*”
*   Performance is another issue

*[Image description: A clip-art style illustration of a human office worker sitting at a desk, pulling and examining a massive, endlessly long strip of paper tape with printed markings.]*

## Slide 52
**Turing Machine and brains (1)**

*   The fact that Turing devised the machine to emulate human's behaviour in the *specific* computation process <ins>**does not directly imply that we are Turing’s Machine**</ins>
    *   It may ore may not be, no one knows

*[Image description: A cropped title text from an article reading: "THE FUNDAMENTAL DISTINCTION BETWEEN BRAINS AND TURING MACHINES By Andrew Friedman"]*

## Slide 53
**Turing Machine and brains (2)**

*[Image description: A cropped quote from an article reading: "...if there is a single property, even a trivially unimportant one, that we have but Turing Machines do not have, then we can not be simply Turing Machines."]*

## Slide 54
**Debate**

*   The debate is open here, also in relation with **AI and Turing test**
*   Turing’s idea are still debated after 80 years showing the level of his genius

*[Image description: A cropped text block explaining the concept of Aleph numbers in mathematics. Above the text is an illustration of the Hebrew letter Aleph ($\aleph$) with subscripts 0 and 1, visually representing different sizes of infinity.]*

## Slide 55
**The general model**

*[Image description: A diagram of a Multi-tape Turing machine. A central control box contains states 'q' and 'p' connected by an arrow. From this box, read/write heads (arrows) point to multiple horizontal tapes split into cells.
1. "Input tape" has an arrow pointing to cell 'a'.
2. "Output tape" has an arrow pointing to cell 'x'.
3. "Memory tape 1" has an arrow pointing to cell 'A'.
4. "Memory tape 2" has an arrow pointing to cell 'B'.
5. "Memory tape K" has an arrow pointing to cell 'D'.
A red bracket groups the output and memory tapes together.]*

## Slide 56
**Von Neumann Architecture**

*[Image description: A block diagram showing the classic Von Neumann architecture. A large blue box represents the "Central Processing Unit". Inside it are two smaller orange boxes: "Control Unit" and "Arithmetic/Logic Unit". Below them, still inside the main system, is an orange box "Memory Unit", with two-way arrows connecting it to the CPU. An "Input device" green box points into the CPU. An "Output device" green box receives an arrow from the CPU.]*

## Slide 57
What is the key idea behind the Von Neumann Architecture?

## Slide 58
What is a stored-program computer?

*[Image description: A large blue icon of a computer microchip/processor inside a stylized blue brush-stroke circle.]*

## Slide 59
**Stored-program computer**

*   Instructions are in memory and the program can be changed
*   The <ins>**Northrop Loom**</ins> will always run a “loom program”

*[Image description: A black and white historical photograph showing a massive, complex mechanical loom (The Northrop Loom) in a textile factory, operating continuously.]*

## Slide 60
**Von Neumann Machines (VNM)**

*[Image description: A highly similar block diagram to the one shown in Slide 56. Central Processing Unit containing Control Unit and Arithmetic/Logic Unit, connected bidirectionally to a Memory Unit. Input Device arrows in, Output Device arrows out.]*

## Slide 61
It seems a trivial idea these days, but it is very powerful and innovative!

*[Image description: A large blue icon of a lightbulb inside a stylized blue brush-stroke circle.]*

## Slide 62
**Harvard Architecture**

*   <ins>**A computer that stores program instructions in electronic memory**</ins>
*   Not a synonym for von Neumann architecture
    *   **Harvard architecture** is a computer architecture with physically separate storage and signal pathways for instructions and data

*[Image description: A block diagram showing the Harvard Architecture. A central green "Control unit" is connected by bidirectional arrows to four surrounding blocks: a pink "ALU" (top), a light-yellow "Instruction memory" (left), a light-green "Data memory" (right), and a light-blue "I/O" (bottom).]*

## Slide 63
**TM vs Von Neumann Machines**

*   TMs can simulate a Von Neumann machine (VNM)
    *   It is an abstract model of computers
*   TM differs from VNM wrt. memory access
    *   TM: sequential
    *   VNM: direct
*   This difference <ins>does not affect the expressive power</ins> of a machine
    *   It does not change the class of problems solvable with a machine
    *   It may affect the computational complexity

## Slide 64
**Why TMs?**

*   TMs have the **same expressive power** as high-level programming languages
    *   <span style="color:red"><ins>**Church-Turing thesis**</ins></span>

*   TMs are **theoretical models** not really meant for programming but for <ins>**proofs and understanding of properties**</ins>

## Slide 65
**Theoretical Computer Science**

**Turing Machines in their mathematical context**
Lecture 8 - Manuel Mazzara

## Slide 66
**Languages**

*[Image description: An Euler diagram (concentric sets) showing the Chomsky hierarchy of languages.
The innermost circle is "Regular languages" (points to text: "FSA can only count fixed numbers (finite states), no generic n").
The next larger circle is "Languages recognizable with PDAs" and contains the formula $a^n b^n$. (points to text: "In programming languages we need to syntactically check nested structures" and "PDAs are not closed under union: stack needs to be prepared for what we are looking for").
The outermost circle is "Recursively enumerable languages" and contains the formulas $a^n b^n c^n$ and $a^n b^n \cup a^n b^{2n}$. (points to text: "PDAs have a destructive external memory").]*

## Slide 67
**History**

*   The Turing machine was invented in 1936 by Alan Turing, (*a-machine*, automatic machine)
*   It is a mathematical description of a very simple device for <ins>arbitrary computations</ins>
*   <ins>**It is intended to show theoretical results of computability theory**</ins>
*   In his article Turing mentions Gödel’s work

## Slide 68
*[Image description: On the left, a scan of a page from Turing's paper "ON COMPUTABLE NUMBERS...". A paragraph at the bottom is boxed in red. To the right is a large text quote extracted from that box.]*

**«Conclusions are reached which are superficially similar to those of Gödel»**

## Slide 69
Kurt Friedrich Gödel (1906 - 1978)

*[Image description: A black and white portrait photo of Kurt Gödel wearing round glasses.]*

## Slide 70
**A bit of background**

*   <ins>**Principia Mathematica**</ins>
*   Whitehead and Russell (1910– 1913)
    *   Attempt of **axiomatizing mathematical reasoning** (2000 pages)
    *   **Derive mathematical “truths” by following mechanical rules of inference**
    *   Claimed to be **complete** and **consistent**
        *   All true theorems could be derived
        *   No falsehoods could be derived

## Slide 71
Russell and Whitehead

*[Image description: Side-by-side black and white portrait photos of an older Bertrand Russell (left) and Alfred North Whitehead (right).]*

## Slide 72
**Logicism and Principia Mathematica**

*   An attempt to <ins>**ground all of mathematics in pure logic**</ins>
    *   <ins>**Logicism**</ins>: a philosophy of mathematics according to which mathematical concepts and truths are **reducible to, or derivable from, pure, fundamental logical principles**

*   The proof system of *Principia Mathematica* is hard to read, different from the modern and streamlined form
    *   a complex, pioneering framework using **Modus Ponens as the dominant and most frequently used inference rule**, but not the only one!

## Slide 73
*[Image description: A photo of an older Bertrand Russell smoking a pipe on the left. On the right, a scan of a complex page from Principia Mathematica showing highly symbolic, dense logical notation proving that 1 + 1 = 2. A specific sentence in the middle of the proof is highlighted in a blue box: "The above proposition is occasionally useful. It is used at least three times, in *113.66 and *120.123.472."]*

## Slide 74
**All logical systems of any complexity are incomplete**: there are statements that are true that cannot be proven within the system (Gödel , 1931)

## Slide 75
**There are mathematical truths that cannot be determined mechanically**

## Slide 76
**Entscheidungsproblem**

*   David Hilbert (23 January 1862 – 14 February 1943)
*   Was devoted to axiomatizing mathematics as other mathematicians at the time (Russel, Whitehead...)
*   In 1928, proposed *Entscheidungsproblem* (decision problem)

*[Image description: A portrait photo of David Hilbert wearing a white hat, glasses, and a suit.]*

## Slide 77
Entscheidungsproblem - decision problem

## Slide 78
**Hilbert Problems and Decision Problem**

*   *Hilbert Problems (1900)*
    *   23 unsolved problems in mathematics
    *   Important mathematical challenges for the 20th century

*   *Entscheidungsproblem (1928)*
    *   in the original German
    *   David Hilbert and Wilhelm Ackermann

## Slide 79
**The Decision Problem (1)**

*   Hilbert characterised it as ‘*the fundamental problem of mathematical logic*’

*   Find an **algorithm** to determine, given some sentences of first order logic regarded as *premises*, and another sentence, being a desired *conclusion*, **whether that conclusion is provable from the premises** using the rules of proof for first order logic

*   If we think of the premises as the axioms of some mathematical domain, an actual algorithm solving the Entscheidungsproblem would **reduce all mathematics to mechanical calculation**

## Slide 80
**The Decision Problem (2)**

*[Image description: A flowchart showing a block "Input" pointing to an oval "Algorithm". The "Algorithm" branches to two separate boxes: "YES" and "NO".]*

*   Is it possible to find a set of *basic truths (axioms)* from which <ins>all statements</ins> in mathematics can be proven, <ins>without giving any contradictory answers</ins> such as 1=0?
*   Is there an <ins>effective procedure</ins> (*algorithm*) which, given a set of axioms and a mathematical proposition, decides whether it is or is not provable from the axioms?
*   Hilbert was asking whether mathematics was <ins>***complete***</ins>, <ins>***consistent***</ins> and <ins>***decidable***</ins>.

## Slide 81
**Answer to the Decision Problem**

*[Image description: A split image. Left side is the portrait of Alan Turing. Right side is a photo of an older Alonzo Church standing at a chalkboard full of mathematical equations, pointing with his arm.]*

*   In 1936, Alonzo Church and Alan Turing published independently papers showing that <ins>**a general solution to the problem is impossible**</ins>
*   An algorithm to answer the general decision problem <ins>**does not exist**</ins>

## Slide 82
**Alonzo Church**

*[Image description: A portrait photo of Alonzo Church wearing thick black glasses. To the right is a quote graphic.]*

"Never had any mathematical conversations with anybody, because there was nobody else in my field. — *Alonzo Church*"