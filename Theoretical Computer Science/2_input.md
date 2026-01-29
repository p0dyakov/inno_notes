Here is the transcription of the slides from the provided PDF files.

# File 1: Lab Session 1

**Slide 1**
# Theoretical Computer Science
## Lab Session 1

January 29, 2026

**Innopolis University**

1 / 25

---

**Slide 2**
# Agenda

▶ Introduction (rules of the game!)
▶ Preliminaries - Sets
▶ Formal Languages
▶ Operations on Formal Languages

2 / 25

---

**Slide 3**
# Rules of the Game

**Laboratory Exercises:** There are weekly laboratory exercises.
**Assessment (max 105):** Mid-term Exam (30%), Final Exam (30%), 5 Quizzes (40%), Participation (5%).

**Note:** To be admitted to the final exam, in each of the following graded items it is necessary to score at least 40% individually: Quiz 1, Quiz 2, Quiz 3, Quiz 4, Quiz 5, Midterm exam. Otherwise, the grade will be computed according to the collected score **without final exam**.

**Group switching**
Switching lab groups is allowed under the following conditions:
▶ The group size limit is 30 students.
▶ TA approval

3 / 25

---

**Slide 4**
# Preliminaries - Sets

4 / 25

---

**Slide 5**
# Sets

A finite set can be described, at least in principle, by listing its elements: $A = \{1, 2, 4, 8\}$ says that $A$ is the set whose elements are 1, 2, 4, and 8.

For infinite (even for finite sets if they have more than just a few elements) sets ellipses (. . . ) are sometimes used to describe how the elements might be listed: $B = \{0, 3, 6, 9, . . .\}$

A more reliable way is to give the property that characterises their elements (also called set comprehension or predicate). Set $B = \{0, 3, 6, 9, . . .\}$ can be described as

$$B = \{x \mid x \text{ is a non-negative integer multiple of 3}\}$$

It is read: “$B$ is the set of all $x$ such that $x$ is a non-negative integer multiple of 3”

5 / 25

---

**Slide 6**
# Sets (notation)

▶ For any set $A$, the statement that $x$ is an element of $A$ is written $x \in A$.
▶ $A \subseteq B$ means that $A$ is a subset of $B$: every element of $A$ is an element of $B$.
▶ $\emptyset$ denotes the empty set: the set with no elements.

To show that two sets $A$ and $B$ are the same, we must show that $A$ and $B$ have exactly the same elements, i.e. $A \subseteq B$ and $B \subseteq A$.

6 / 25

---

**Slide 7**
# Element vs Subset

**Element of a Set:**
The symbol $\in$ is used to denote "is an element of."
Example: $2 \in \{1, 2, 3\}$
Example: $4 \notin \{1, 2, 3\}$

**Assigning Names to Sets:**
Sets are often represented by capital letters, and elements by lowercase letters.
If $A = \{1, 2, 3\}$, then $2 \in A$ and $a \in A$ where $a$ is an element of $A$.

**Sets Containing Other Sets:**
Sets can contain other sets. Example: $C = \{\{1, 2, 3\}, \{2, 3, 4, 5\}\}$
In this case, $A \in C$ because $A$ is an element of $C$. However, $1 \notin C$.

**Subsets:**
A set $A$ is a subset of $B$ denoted by $A \subseteq B$ if every element of $A$ is also an element of $B$.
Example: $\{1, 2\} \subseteq \{1, 2, 3, 4\}$

7 / 25

---

**Slide 8**
# Sets (operations)

For two sets $A$ and $B$, we can define their union $A \cup B$, their intersection $A \cap B$, and their difference $A \setminus B$ (sometimes denoted as $A - B$), as follows$^1$:

$A \cup B = \{x \mid x \in A \lor x \in B\}$
$A \cap B = \{x \mid x \in A \land x \in B\}$
$A \setminus B = \{x \mid x \in A \land x \notin B\}$

$^1 \lor$ and $\land$ denote the logical ‘or’ and logical ‘and’ respectively.

8 / 25

---

**Slide 9**
# Sets (Union of any number of sets) - Notation

If $A_0, A_1, A_2, . . .$ are sets, the union of these sets can be denoted as

$$\bigcup \{A_i \mid i \ge 0\} = \{x \mid x \in A_i \text{ for at least one } i \text{ with } i \ge 0\}$$

or

$$\bigcup_{i=0}^{\infty} A_i$$

9 / 25

---

**Slide 10**
# Sets (Power Sets)

For a set $A$, the set of all subsets of $A$ is called the power set. Can be denoted as $\mathcal{P}(A)$ or as $2^A$.

Power set of set $\{a, b, c\}$ is
$$\{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}\}$$

For a set $A$, the set $\mathcal{P}(A)$ has exactly $2^n$ elements, where $n$ is the cardinality of $A$.

10 / 25

---

**Slide 11**
# Languages

11 / 25

---

**Slide 12**
# Notation and Terminology

**Alphabet:** a finite set of symbols, e.g. $\{a, b\}$, or $\{0, 1\}$. Normally denoted by $\Sigma$

**String:** a string over an alphabet ($\Sigma$) is a finite sequence of symbols in $\Sigma$.

**length:** for a string $x$, $|x|$ is the number of symbols of $x$.

**empty string:** is the null string over $\Sigma$. It is denoted as $\epsilon$. By definition, $|\epsilon| = 0$

**Set of all strings:** the set of all strings over $\Sigma$ is denoted by $\Sigma^*$, e.g. for the alphabet $A = \{a, b\}$
$A^* = \{\epsilon, a, b, aa, ab, ba, bb, aaa, aab, . . .\}$

**Language:** A language $L$ over an alphabet $A$ is a subset of $A^*$

12 / 25

---

**Slide 13**
# Concatenation of strings

If $x$ and $y$ are two strings over an alphabet, the concatenation $xy$ (sometimes denoted as $x \cdot y$) consists of the symbols of $x$ followed by those of $y$:

$x = ab$
$y = bab$
$xy = abbab$

Concatenation is an associative operation: $(xy)z = x(yz)$ for all possible strings $x$, $y$, and $z$.

13 / 25

---

**Slide 14**
# Constructing new Languages

Languages are sets.
▶ Operations on languages are ways of constructing new languages: for two languages $L_1$ and $L_2$ over the alphabet $\Sigma$, $L_1 \cup L_2$, $L_1 \cap L_2$, and $L_1 \setminus L_2$ are also languages over $\Sigma$.
▶ String operation of concatenation is also used to construct new languages: if $L_1$ and $L_2$ are both languages over $\Sigma$, the concatenation of $L_1$ and $L_2$ is the language

$$L_1L_2 = \{xy \mid x \in L_1, y \in L_2\}$$

Example:
$\{a, aa\}\{\epsilon, b, ab\} = \{a, ab, aab, aa, aab, aaab\}$

Is this statement true?
$L_1L_2 = L_2L_1$

14 / 25

---

**Slide 15**
# Exponential notation

The concatenation of $k$ copies of a single symbol $a$, a single string $s$, or a single language $L$ is defined as:
If $k = 0$, then
$$a^k = \{\epsilon\}$$

If $k > 0$, then
$$a^k = aa . . . a$$
where there are $k$ occurrences of $a$, similarly for $s^k$ and $L^k$. In the case where $L$ is simply the alphabet $\Sigma$,

$$\Sigma^k = \{x \in \Sigma^* \mid |x| = k\}$$

Example:
$\Sigma = \{0, 1\}$
$\Sigma^2 = \{00, 01, 10, 11\}$

15 / 25

---

**Slide 16**
# Operations on Languages

16 / 25

---

**Slide 17**
# Operations on Languages

▶ Union
▶ Intersection
▶ Set difference
▶ Complement: if $L$ is a language over $\Sigma$,
$$\bar{L} = \Sigma^* \setminus L$$
▶ Concatenation: if $L_1$ and $L_2$ are both languages over $\Sigma$,
$$L_1L_2 = \{xy \mid x \in L_1, y \in L_2\}$$
▶ Power of n
$$L^n = \{x_1x_2...x_n \mid x_i \in L \text{ for all } 1 \le i \le n\}$$
▶ Kleene Star
$$L^* = \{x_1x_2...x_n \mid n \in \mathbb{N}, x_1, x_2, ..., x_n \in L\} = \bigcup_{n \in \mathbb{N}} L^n$$

17 / 25

---

**Slide 18**
# Exercises

18 / 25

---

**Slide 19**
# Exercises (0)

What are the sets $D$ and $E$?:
i. $D = \{\{x\} \mid x \text{ is a non-negative integer such that } x \le 4\}$
ii. $E = \{3i + 5j \mid i \text{ and } j \text{ are non-negative integers}\}$

Are the following statements true?
iii. $\{0, 1\} = \{1, 0\}$
iv. $\{0, 1, 2, 1, 0\} = \{1, 1, 1, 1, 0, 2, 2\}$

19 / 25

---

**Slide 20**
# Exercises (1)

Construct the power set for the following sets:
i. $\{a, b\}$
ii. $\{0, 1\} \cup \{1, 2\}$
iii. $\{z\}$
iv. $\{0, 1, 2, 3, 4\} \cap \{1, 3, 5, a\}$
v. $\{0, 1, 2, 3\} \setminus \{1, 3, 5, a\}$
vi. $\emptyset$

Determine the following languages over the alphabet $\Sigma = \{0, 1\}$
vii. $\Sigma^0$
viii. $\Sigma^4$
ix. $\mathcal{P}(\Sigma)$
x. $\mathcal{P}(\Sigma^*)$

20 / 25

---

**Slide 21**
# Exercises (2)

Find a possible alphabet for the following languages$^2$
i. The language $L = \{oh, ouch, ugh\}$
ii. The language $L = \{apple, pear, 4711\}$
iii. The language of all binary strings

Determine what the Kleene star operation produces over the following alphabets:
iv. $\Sigma = \{0, 1\}$
v. $\Sigma = \{a\}$
vi. $\Sigma = \emptyset$ (the empty alphabet)

$^2$A word *foo* should be interpreted as a string of characters $f$, $o$, and $o$.

21 / 25

---

**Slide 22**
# Exercises (3)

State the alphabet $\Sigma$ for the following languages:
i. $L = \Sigma^* = \{\epsilon, 0, 1, 00, 01, 10, 11, 000, . . .\}$
ii. $L = \Sigma^* = \{\epsilon, a, aa, aaa, aaaa, . . .\}$

Assuming that $\Sigma = \{0, 1\}$, construct complement languages for the following:
iii. $\overline{\{010, 101, 11\}}$
iv. $\overline{\Sigma^* \setminus \{110\}}$

State the following languages explicitly
v. $\mathcal{P}(\{a, b\}) \setminus \mathcal{P}(\{a, c\})$
vi. $\{x \mid x, y \in \mathbb{N} \land \exists y : y < 10 \land (y + 2 = x)\}$ ($\mathbb{N}$ is the set of all non-negative integers)

22 / 25

---

**Slide 23**
# Exercises on Operations on Languages

23 / 25

---

**Slide 24**
# Exercises (4)

1. Let $L = \{a^i, i \ge 0\}$ be a language over $\Sigma = \{a, b\}$. Find $\bar{L}$ and $L^*$
2. Let $L_1, L_2$ be languages over $\Sigma = \{a, b\}$. Find $L_1L_2$
a) $L_1 = \{\epsilon, a, aa\}, L_2 = \{aa, aaa\}$
b) $L_1 = \{a, a^2, a^4\}, L_2 = \{b^0, b^2, b^3\}$
3. Let $L = \{0, 01, 001\}$. Find $L^2$.
4. Describe in plain English the following languages over $\Sigma = \{a, b\}$:
a) $L = \{a, b\}^*$
b) $L = \{a\}^* \cup \{b\}^*$
c) $L = \{a\}^* \cap \{b\}^*$
d) $L = \{aa\}^* \setminus \{aaaa\}^*$
5. Write out in full the strings $0^5, 0^31^3, (010)^2, (01)^30, 1^0$

24 / 25

---

**Slide 25**
# Exercises (5)

Perform operations on the languages over $\Sigma = \{0, 1\}$:
$L_1 = \{0, 1, 00, 11, 000, 111, ...\},$
$L_2 = \{0, 1\}^*,$
$L_3 = \{w \mid w \in \Sigma^*, |w| = 1\},$
$L_4 = \{w \mid w \in \Sigma^*, |w| = 2\},$
$L_5 = \{w \mid w \in \Sigma^*, |w| \ge 1\}$

1. $L_1 \cup L_2, \quad L_3 \cup L_4$
2. $L_1 \cap L_2, \quad L_1 \cap L_3, \quad L_1 \cap L_4, \quad L_1 \cap L_5, \quad L_3 \cap L_4$
3. $L_1 \setminus L_2, \quad L_1 \setminus L_3, \quad L_3 \setminus L_4, \quad L_4 \setminus L_5, \quad L_5 \setminus L_4$
4. $\overline{L_1}, \quad \overline{L_2}, \quad \overline{L_3}, \quad \overline{L_5 \setminus L_4}$
5. $L_1L_2, \quad L_3L_4, \quad L_4L_3$
6. $L_2^*, \quad L_3^*, \quad L_4^*$

25 / 25

***

# File 2: Tutorial Week 2

**Slide 1**
# Theoretical Computer Science
## Tutorial Week 2

Munir Makhmutov

**Innopolis University**

1 / 44

---

**Slide 2**
# Agenda

*   Alphabets and Strings
*   Formal Languages
*   Operations

2 / 44

---

**Slide 3**
# Alphabets and Strings

**Definition**
An **alphabet** is a finite set of symbols

**Examples**
$$\{0, 1\}$$
$$\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$$
$$\{a, b, c, d, . . . , x, y, z\}$$

3 / 44

---

**Slide 4**
# Alphabets and Strings

**Definition**
A **string** over an alphabet $\Sigma$ is a finite sequence of symbols in $\Sigma$

**Examples**
For $\Sigma = \{0, 1\}$,
010011
11100011

4 / 44

---

**Slide 5**
# Alphabets and Strings

**Definition**
A **string** over an alphabet $\Sigma$ is a finite sequence of symbols in $\Sigma$

**Examples**
For $\Sigma = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$,
123456
666
2023

5 / 44

---

**Slide 6**
# Alphabets and Strings

**Definition**
A **string** over an alphabet $\Sigma$ is a finite sequence of symbols in $\Sigma$

**Examples**
For $\Sigma = \{a, b, c, d, . . . , x, y, z\}$,
peace
war
dfklgnkjrbgjrbg

6 / 44

---

**Slide 7**
# Alphabets and Strings

**Definition**
The **length** of a string $s$ is the number of symbols of $s$ and denoted as $|s|$

**Examples**
$|peace| = 5$
$|war| = 3$
$|dfklgnkjrbgjrbg| = 15$

7 / 44

---

**Slide 8**
# Alphabets and Strings

**Definition**
$\epsilon$ is the **null** string (empty string) over any alphabet.

**Property**
$|\epsilon| = 0$

8 / 44

---

**Slide 9**
# Alphabets and Strings

**Definition**
For two strings $x$ and $y$, the concatenation $x \cdot y$ is the operation of joining “end-to-end”.

**Examples**
For $x =$“123” and $y =$“987”,
$x \cdot y =$ “123987”

9 / 44

---

**Slide 10**
# Alphabets and Strings

**Definition**
For two strings $x$ and $y$, the concatenation $x \cdot y$ is the operation of joining “end-to-end”.

**Examples**
For $x =$ “back” and $y =$ “end”,

$x \cdot y =$ “backend”

$y \cdot x =$ “endback”

10 / 44 (Duplicate numbering in PDF, distinct slide content)

---

**Slide 11**
# Alphabets and Strings

**Definition**
For two strings $x$ and $y$, the concatenation $x \cdot y$ is the operation of joining “end-to-end”.

**Examples**
For $x =$ “back” and $y =$ “end”,

$x \cdot y =$ “backend”

$y \cdot x =$ “endback”

Non-commutative!

10 / 44 (Duplicate numbering in PDF)

---

**Slide 12**
# Alphabets and Strings

**Property**
$(x \cdot y) \cdot z = x \cdot (y \cdot z)$

**Examples**
For $x =$ “ab”, $y =$ “cd” and $z =$ “ef”,

$(x \cdot y) \cdot z =$ “abcd” $\cdot$ “ef” = “abcdef”

$x \cdot (y \cdot z) =$ “ab” $\cdot$ “cdef” = “abcdef”

11 / 44

---

**Slide 13**
# Alphabets and Strings

**Property**
$(x \cdot y) \cdot z = x \cdot (y \cdot z)$

**Examples**
For $x =$ “ab”, $y =$ “cd” and $z =$ “ef”,

$(x \cdot y) \cdot z =$ “abcd” $\cdot$ “ef” = “abcdef”

$x \cdot (y \cdot z) =$ “ab” $\cdot$ “cdef” = “abcdef”

Associative!

11 / 44 (Duplicate numbering in PDF)

---

**Slide 14**
# Alphabets and Strings

**Property with null**
$\forall x (x \cdot \epsilon = \epsilon \cdot x = x)$

$\epsilon$ is an identity element

12 / 44

---

**Slide 15**
# Agenda

*   Alphabets and Strings
*   **Formal Languages**
*   Operations

13 / 44

---

**Slide 16**
# Formal Languages

**Definition**
The set of all strings over $\Sigma$ is denoted by $\Sigma^*$

**Examples**
For $\Sigma = \{0, 1\}$,
$\Sigma^* = \{\epsilon, 0, 1, 00, 01, 10, 11, 000, 001, 010, . . .\}$

14 / 44

---

**Slide 17**
# Formal Languages

**Definition**
A language $L$ is a **set** of strings over an alphabet $\Sigma$.

**Equivalent definition**
$L \subseteq \Sigma^*$

15 / 44

---

**Slide 18**
# The Naive Set Theory

**Definition of a set**
$A = \{x \in \mathbb{U} \mid P(x)\}$
$A = \{a_1, a_2, . . . , a_n\}$

**Example**
$\{x \in \mathbb{Z} \mid x < 0\}$

$\mathbb{U}$ is a universal set
$\mathbb{Z}$ is a set of all integers

16 / 44

---

**Slide 19**
# Formal Languages

**Alphabet**
For $\Sigma = \{0, 1\}$,
$\Sigma^* = \{\epsilon, 0, 1, 00, 01, 10, 11, 000, 001, 010, . . .\}$

**Languages**
$L_1 = \{00000000, 00000001, . . . , 11111110, 11111111\} =$
$= \{x \in \{0, 1\}^* \mid |x| = 8\}$

$L_2 = \{0, 00, 01, 000, 001, 010, . . .\} = \{0x \mid x \in \Sigma^*\}$

17 / 44

---

**Slide 20**
# Formal Languages

**Alphabet**
For $\Sigma = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$,
$\Sigma^* = \mathbb{N} \cup \{\epsilon\}$

**Languages**
$L_1 = \{0, 2, 4, 6, 8, 10, . . .\} = \{x \in \Sigma^* \mid x \text{ is even }\}$
$L_2 = \{2, 3, 5, 7, 13, . . .\} = \{x \in \Sigma^* \mid x \text{ is prime }\}$

18 / 44

---

**Slide 21**
# Formal Languages

**Alphabet**
For $\Sigma = \{a, b, c, d, . . . , x, y, z\}$

**Languages**
Russian, English, Italian, Tatar, . . .

19 / 44

---

**Slide 22**
# Formal Languages

**Alphabet**
For $\Sigma = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, =\}$

**Arithmetic**
$\{0 + 0 = 0, 0 - 0 = 0, . . . , 12 + 32 = 44, . . . , 52 - 39 = 13, . . .\}$

20 / 44

---

**Slide 23**
# Agenda

*   Alphabets and Strings
*   Formal Languages
*   **Operations**
    *   Operations from Set Theory
    *   Special operations

21 / 44

---

**Slide 24**
# 1. Complement

**Complement of a set**
$A^c = \overline{A} = \{x \in \mathbb{U} \mid x \notin A\}$

**Example**
If $\mathbb{U} = \{1, 2, 3, 4\}$ and $A = \{1, 3\}$, then
$\overline{A} = \{2, 4\}$

22 / 44

---

**Slide 25**
# Complement

**Complement of a language**
For an alphabet $\Sigma$,
$L^c = \overline{L} = \{x \in \Sigma^* \mid x \notin L\}$

**Example**
For $\Sigma = \{0, 1\}$, if $L = \{0x \mid x \in \Sigma^*\}$, then
$\overline{L} =$

23 / 44

---

**Slide 26**
# Complement

**Complement of a language**
For an alphabet $\Sigma$,
$L^c = \overline{L} = \{x \in \Sigma^* \mid x \notin L\}$

**Example**
For $\Sigma = \{0, 1\}$, if $L = \{0x \mid x \in \Sigma^*\}$, then
$\overline{L} = \{1x \mid x \in \Sigma^*\} \cup \{\epsilon\}$

23 / 44 (Duplicate numbering in PDF)

---

**Slide 27**
# Union

**Union**
$A \cup B = \{x \in \mathbb{U} \mid x \in A \lor x \in B\}$

**Example**
If $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$, then
$A \cup B = \{1, 2, 3, 4\}$

24 / 44

---

**Slide 28**
# Intersection

**Intersection**
$A \cap B = \{x \in \mathbb{U} \mid x \in A \land x \in B\}$

**Example**
If $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$, then
$A \cap B = \{2, 3\}$

25 / 44

---

**Slide 29**
# Difference

**Difference**
$A \setminus B = \{x \in \mathbb{U} \mid x \in A \land x \notin B\}$

**Example**
If $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$, then
$A \setminus B = \{1\}$

26 / 44

---

**Slide 30**
# Formal Languages

**2. Union**
$L_1 \cup L_2 = \{s \in \Sigma^* \mid s \in L_1 \lor L_2\}$

**3. Intersection**
$L_1 \cap L_2 = \{s \in \Sigma^* \mid s \in L_1 \land s \in L_2\}$

**4. Difference**
$L_1 \setminus L_2 = \{s \in \Sigma^* \mid s \in L_1 \land s \notin L_2\}$

27 / 44

---

**Slide 31**
# The Naive Set Theory

**Definition**
$X \times Y = \{(x, y) \mid x \in X \land y \in Y\}$

**Example**
If $A = \{1, 2, 3\}$ and $B = \{a, b\}$, then
$A \times B = \{(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)\}$

28 / 44

---

**Slide 32**
# The Naive Set Theory

**Definition**
$X_1 \times \cdot \cdot \cdot \times X_n = \{(x_1, . . . , x_n) \mid x_1 \in X_1 \land . . . \land x_n \in X_n\}$

**Example**
$\underbrace{X \times \cdot \cdot \cdot \times X}_{n \text{ times}} = X^n$

29 / 44

---

**Slide 33**
# The Naive Set Theory

**Definition**
For a set $A$, the power of $A$ is the set
$2^A = \mathcal{P}(A) = \{B \mid B \subseteq A\}$

**Examples**
1) If $A = \{a\}$ then $\mathcal{P}(A) = \{\emptyset, \{a\}\}$
2) If $A = \{a, b\}$ then $\mathcal{P}(A) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}$

30 / 44

---

**Slide 34**
# The Naive Set Theory

**Definition**
Intuitively, the cardinality of a set $A$, denoted by $|A|$, is the number of elements of $A$.

**Examples**
1. $|\emptyset| = 0$
2. if $A = \{2\}$ then $|A| = 1$
3. if $A = \{1, 2, 3\}$ then $|A| = 3$

31 / 44

---

**Slide 35**
# Relationship

**Question 1**
What is the difference between sets and strings?

**Question 2**
What is the difference between $\emptyset$ and $\epsilon$?

**Question 3**
What is the difference between the cardinality and the length?

32 / 44

---

**Slide 36**
# Agenda

*   Alphabets and Strings
*   Formal Languages
*   **Operations**
    *   Operations from Set Theory
    *   **Special operations**

33 / 44

---

**Slide 37**
# Formal Languages

**Concatenation**
$L_1 \cdot L_2 = \{x \cdot y \mid x \in L_1 \land y \in L_2\}$

**Example**
If $L_1 = \{1, 2, 3\}$ and $L_2 = \{a, b\}$, then
$L_1 \cdot L_2 = \{1a, 1b, 2a, 2b, 3a, 3b\}$

34 / 44

---

**Slide 38**
# Formal Languages

**Concatenation**
$L_1 \cdot L_2 = \{x \cdot y \mid x \in L_1 \land y \in L_2\}$

**Example**
If $L_1 = \{1, 12\}$ and $L_2 = \{\epsilon, 2\}$, then
$L_1 \cdot L_2 = \{1, 12, 122\}$

35 / 44

---

**Slide 39**
# Formal Languages

**Concatenation**
$L_1 \cdot L_2 = \{x \cdot y \mid x \in L_1 \land y \in L_2\}$

**Example**
If $L_1 = \{\epsilon, a\}$ and $L_2 = \{\epsilon, a, aa, aaa, . . .\}$, then
$L_1 \cdot L_2 =$

36 / 44

---

**Slide 40**
# Formal Languages

**Concatenation**
$L_1 \cdot L_2 = \{x \cdot y \mid x \in L_1 \land y \in L_2\}$

**Example**
If $L_1 = \{\epsilon, a\}$ and $L_2 = \{\epsilon, a, aa, aaa, . . .\}$, then
$L_1 \cdot L_2 = L_2$

$L_1 \times L_2 \neq L_2$ for any nonempty $L_1, L_2$

36 / 44 (Duplicate numbering in PDF)

---

**Slide 41**
# Formal Languages

**Kleene star**
$L^* = \{x_1x_2 . . . x_n \mid n \in \mathbb{N}, x_1, x_2, . . . x_n \in L\}$

**Example**
For $\Sigma = \{a, b\}$, if $L = \{a\}$ then
$L^* = \{\epsilon, a, aa, aaa, . . .\}$

37 / 44

---

**Slide 42**
# Formal Languages

**Kleene star**
$L^* = \{x_1x_2 . . . x_n \mid n \in \mathbb{N}, x_1, x_2, . . . x_n \in L\}$

**Example**
For $\Sigma = \{a, b\}$, if $L = \{ab\}$ then
$L^* = \{\epsilon, ab, abab, ababab, . . .\}$

38 / 44

---

**Slide 43**
# Formal Languages

**Kleene star**
Let $\Sigma$ be an alphabet. Kleene star of $\Sigma$ contains all strings and denotes $\Sigma^*$ (as before).

**Special case**
$\Sigma^+ = \Sigma^* \setminus \{\epsilon\}$ - Kleene plus

39 / 44

---

**Slide 44**
# Formal Languages

**Special cases**
$L^k = \{x_1x_2 . . . x_k \mid x_1, x_2, . . . x_k \in L\}$

**Example**
For $\Sigma = \{a, b\}$, if $L = \{a\}$ then
$L^k = \{\underbrace{aa . . . a}_{k \text{ times}}\}$

40 / 44

---

**Slide 45**
# Formal Languages

**Special cases**
$L^k = \{x_1x_2 . . . x_k \mid x_1, x_2, . . . x_k \in L\}$

**Example**
For $\Sigma = \{a, b\}$,
$\Sigma^2 =$

41 / 44

---

**Slide 46**
# Formal Languages

**Special cases**
$L^k = \{x_1x_2 . . . x_k \mid x_1, x_2, . . . x_k \in L\}$

**Example**
For $\Sigma = \{a, b\}$,
$\Sigma^2 = \{aa, ab, ba, bb\}$

41 / 44 (Duplicate numbering in PDF)

---

**Slide 47**
# Formal Languages

**Special cases**
$a^k = \underbrace{aa . . . a}_{k \text{ times}}$

**Example**
For $\Sigma = \{a, b\}$,
$\Sigma^3 =$

42 / 44

---

**Slide 48**
# Formal Languages

**Special cases**
$a^k = \underbrace{aa . . . a}_{k \text{ times}}$

**Example**
For $\Sigma = \{a, b\}$,
$\Sigma^3 = \{a^3, a^2b, aba, ab^2, ba^2, bab, b^2a, b^3\}$

42 / 44 (Duplicate numbering in PDF)

---

**Slide 49**
# Formal Languages

**Special cases**
$a^k = \underbrace{aa . . . a}_{k \text{ times}}$

**Example**
For $\Sigma = \{a, b\}$,
$\Sigma^3 = \{a^3, a^2b, aba, ab^2, ba^2, bab, b^2a, b^3\}$

OR

$\Sigma^3 = \{aaa, aab, aba, abb, baa, bab, bba, bbb\}$

42 / 44 (Duplicate numbering in PDF)

---

**Slide 50**
# Summary

*   Alphabets and Strings
*   Formal Languages
*   Operations
    *   Operations from Set Theory
    *   Special operations

43 / 44

---

**Slide 51**
# Thank you for your attention!

44 / 44

***

# File 3: Lecture 2

**Slide 1**
# Theoretical Computer Science

**Models of Computation (recap)**
Lecture 2 - Manuel Mazzara

---

**Slide 2**
# Machines and Grammars

1. Computation is elegantly **modeled** through simple mathematical objects
• Finite automata, pushdown automata, Turing machines, ...
2. Methods of **generating languages**: regular expressions, grammars…
3. **Computability** theory

---

**Slide 3**
# Different kind of Automata

• Finite State Automata (**FSA**)
• **no temporary memory, just states are used to memorize**
• Pushdown Automata (**PDA**)
• **stack (destructive memory), need to destroy while reading**
• Turing Machines (**TMs**)
• **equivalent to random (non-sequential) access memory**
• In fact, it is sequential, but does not change the computational power

---

**Slide 4**
# Power of Automata

[Diagram showing the hierarchy of automata power]

**Finite Automata** (Simple problems) < **Pushdown Automata** (More complex problems) < **Turing Machine** (Hardest problems)

**Less power** ————————————————> **More power**
Solve more computational problems

---

**Slide 5**
# A course-long question

• **Turing Machine** is the most powerful computational model known (together with others of equivalent expressiveness)

• Are there computational problems that a Turing Machine cannot solve?

• The Answer is “yes” (unsolvable problems)

• **There are indeed unsolvable problems**, and we will see in detail what it means

---

**Slide 6**
# Theoretical Computer Science

**About Theoretical Computer Science**
Lecture 2 - Manuel Mazzara

6

---

**Slide 7**
# Edsger Wybe Dijkstra
11 May 1930 – 6 August 2002

[Image: Portrait of Edsger Wybe Dijkstra]

• **Structured Programming**
• Software Engineering
• Concurrent and Distributed Computing
• Semaphores
• Mutual exclusion
• Deadlock

• *Solution of a Problem in Concurrent Programming Control* - E.W. Dijkstra, Communications of the ACM, Vol. 8 , No. 9, p. 569, **1965**

7

---

**Slide 8**
"*The **revolution** in views of programming started by Dijkstra's iconoclasm led to a movement known as **structured programming**, which advocated a **systematic, rational approach to program construction**. Structured programming is **the basis for all that has been done since in programming methodology**, including object-oriented programming.*”
**Bertrand Meyer - Touch of Class (page 188)**

8

---

**Slide 9**
[Image: Diagrams comparing unstructured flowcharts with structured programming constructs (sequence, selection, repetition)]

• **Structured programming** is a programming paradigm aimed at improving the **clarity, quality, development and maintenance time** of a computer program by making use of the **structured control flow constructs** of selection (if/then/else) and repetition (while and for), block structures, and subroutines.

# Structured programming

9

---

**Slide 10**
[Image: Photo of Edsger Dijkstra with a quote next to it]

Computer science is no more about computers than astronomy is about telescopes.
(Edsger Dijkstra)

10

---

**Slide 11**
# Seminal Turing’s article on AI

[Image: Cover of the journal "MIND", A Quarterly Review of Psychology and Philosophy, Vol. LIX. No. 236, October 1950. Article: "I.—COMPUTING MACHINERY AND INTELLIGENCE By A. M. Turing". A highlighted box reads: "1. The Imitation Game. I PROPOSE to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think'. The definitions might be framed so as to reflect so far as possible the normal use of the words, but this attitude is dangerous. If the meaning of the words 'machine' and 'think' are to be found by examining how they are commonly"]

11

---

**Slide 12**
“The question of whether a computer can think is no more interesting than the question of whether a submarine can swim.”
— *Edsger W. Dijkstra*

12

---

**Slide 13**
# Theoretical Computer Science

**Models and Abstractions**
Lecture 2 - Manuel Mazzara

13

---

**Slide 14**
WHAT IS A SCIENTIFIC MODEL?

[Image: Cartoon scientist pointing at a whiteboard]

**scientific model**
a representation of a particular phenomena in the world

14

---

**Slide 15**
[Image: A hand-drawn right-angled triangle labeled with vertices A, B, C and sides a, b, c. Below it is the Pythagorean theorem formula: $c^2 = a^2 + b^2$]

---

**Slide 16**
[Image: The Tube Map (London Underground Map) showing various lines (Bakerloo, Central, Circle, etc.) and stations]

---

**Slide 17**
# Mathematical abstractions

• Representing real systems
• **Abstraction allows you to focus on the important aspects of a problem**

• **Formal reasoning** can improve our ability to design and build systems
• Uncover **design flaws**
• Precisely **define requirements**
• Mathematics allows you to **reason about solutions** to the problem

• Different models have different strengths and weaknesses

---

**Slide 18**
[Image: Photograph of three young lions resting in grass]

---

**Slide 19**
[Image: A sequence of images demonstrating abstraction.
1. Photo of lions (More specific)
2. Cave painting of lions
3. Three lion face icons
4. Tally marks (|||)
5. The number 3
6. The variable *n* (Less specific)]

**Abstraction**

• Remove background from foreground
• Remove differences between each animal
• Remove "animal-ness" (treat lions as generic "lines")
• Remove need to count objects with literal lines
• Remove need to specify a fixed number

---

**Slide 20**
[Image: Diagram titled "The role of theoretical physics".
A vertical curved line separates "Real World" (left) from "Abstract World" (right).
Arrows show a cycle:
1. Observed Phenomenon (Real World) -> Mathematical Model (Abstract World)
2. Mathematical Model -> Explore Consequences (Abstract World)
3. Explore Consequences -> Test Consequences (Real World)
4. Applications (Real World)]

20

---

**Slide 21**
[Image: Diagram titled "The role of theoretical computer science".
Similar structure to previous slide, separating Real World and Abstract World.
1. Computation (Real World) -> Mathematical Model (Abstract World) [Annotated with "Only done recently"]
2. Mathematical Model -> Explore Consequences (Abstract World)
3. Explore Consequences -> Applications (Real World)]

21

---

**Slide 22**
# Our big question

• Is every function computable?
• Can I write an algorithm for any function $\mathbb{N} \to \mathbb{N}$?
• **Halting Problem**

[Diagram:
Arbitrary Program $p_i$ Source Code -> [Oracle] -> Halt or No Halt Decision
Set of Inputs to Program $I_j$ -> [Oracle]
]

22

---

**Slide 23**
# Theoretical Computer Science

**Introduction to Formal Languages**
Lecture 2 - Manuel Mazzara

23

---

**Slide 24**
# Big “existential” question (1)

• Do you know anything in nature with an infinite set of “bricks” which is not determined a-priori?
• Think about chemistry, physics and biology!

• Everything, including life seems to be expressed by **building bricks**, finite in nature and **pre-determined**, that do not change over time, and express complexity trough “*combinatorial explosion*”

• ***Can you falsify this statement?***

24

---

**Slide 25**
[Image: Periodic Table of the Elements showing element groups like Alkali Metal, Alkaline Earth, Transition Metal, etc., with atomic numbers and symbols.]

25

---

**Slide 26**
# Big “existential” question (2)

• Everything, including life seems to be expressed by **building bricks, finite in nature and pre-determined**, that do not change over time, and **express complexity trough combinatorial explosion**

• Is brain functioning any different?

• **Language** is not different!

• **Computation** is not different!

26

---

**Slide 27**
[Image: Photo of Noam Chomsky with a quote]

Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied. Even the interpretation and use of words involves a process of free creation.
(Noam Chomsky)

27

---

**Slide 28**
[Image: Photo of Noam Chomsky with a quote. Speech bubble says "An Alphabet!". Text boxes highlight specific phrases in the quote.]

From now on I will consider a language to be a set (finite or infinite) of sentences, **each finite in length** and constructed out of a **finite set of elements**. All natural languages in their spoken or written form are languages in this sense.
— *Noam Chomsky* —

[Blue box text: And so are Programming Languages!]

28

---

**Slide 29**
# What is an alphabet?

29

---

**Slide 30**
# Natural languages alphabets

[Image: World map color-coded by alphabet type used.
Green: Latin Alphabet
Red: Cyrillic alphabet
Blue: Arabic alphabet
Light Blue: Brahmic-derived alphabets
Brown: Mixed: Latin and Cyrillic Alphabet
Cyan: Mixed: Latin and Arabic Alphabet
Black: Mixed: no alphabet and other alphabet
Dark Grey: Other alphabet
Light Grey: No alphabet (Logograms)]

30

---

**Slide 31**
# Elements of languages

• **Alphabet** or vocabulary
– Finite set of **basic symbols**
– Examples:
• Roman alphabet {a, b, ..., z}
• Digits {0, 1, ..., 9}
• Binary alphabet {0, 1}

• **String** over an alphabet **A**
– **Finite sequence of symbols** of the alphabet **A**
– Repetitions are allowed

31

---

**Slide 32**
# Examples

• Roman alphabet **A**={a, b, ..., z}
– **a** is a string on **A**
– **aa** is a string on **A**
– **aba, add, aza**, … are strings on **A**

• Alphabet of digits **D**={0, 1, ..., 9}
– **0, 1, 2, ...,9** are strings over **D**
– **012, 999, 923456**, … are strings over **D**

32

---

**Slide 33**
# Length of a string

• The **length** of a string is the **number of symbols** contained in the string
– We denote the length of a string x as **|x|**

• Examples:
– |a|= 1
– |991346|=6

• The **empty string** is a string that has zero symbols
– We denote it as $\varepsilon$
– |$\varepsilon$|=0

33

---

**Slide 34**
# Comparing strings

• Two strings
– x=$x_1x_2… x_n$
– y=$y_1y_2…y_m$
are **equal** if and only if
– |x|=|y| (n=m) [Label: Same length]
– $x_i=y_i$, $\forall i (1 \le i \le n)$ [Label: Corresponding elements are the same]

• Examples
– aabb and aabba are not equal
– ababs and baasb are not equal

34

---

**Slide 35**
# Concatenation

• Given two strings **x** and **y**, the **concatenation** (or product) of **x** and **y** is a string **xy** (or **x⋅y**), where **x** is followed by **y**

– Example: strings on **A**={a, b, c, d}
•x=abadd
•y=dcc
•xy=abadddcc
•yx=dcc abadd

• Remarks
– A string **x** concatenated with $\varepsilon$ is still **x**
– We abbreviate **xx** as **$x^2$**, **xxx** as **$x^3$**, …
– Concatenation is associative and **non-commutative**

35

---

**Slide 36**
# Substrings

• A string **x** is a **substring** (or a factor) of a string **s** if there exist two strings **y** and **z** such that **s=yxz**
– y or z can be $\varepsilon$
•If y= $\varepsilon$, x is called prefix
•If z= $\varepsilon$, x is called suffix
– If both y and z are $\varepsilon$, x is equal to s

• Example: s=aadabbc
– aad is a prefix of s
– abbc is a suffix of s
– ada is a substring of s

36

---

**Slide 37**
# Kleene Star

• The **Kleene star** is a **unary operator** that applies to *a set of symbols or a set of strings*
– It is denoted as *
– In algebra it is called the **free monoid** on a set

• If **A** is an alphabet, then **A\*** is the **set of all strings over symbols in A**, including the **empty string**.

• Examples:
– If A={a, b, c} then A*={$\varepsilon$, a, b, c, aa, ab, ac, ba, bb, bc, ca, …}
– If B={0, 1} then B*={$\varepsilon$, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100, …}

37

---

**Slide 38**
# Do you remember what is a free monoid in abstract algebra (the study of algebraic structures)?

38

---

**Slide 39**
# Free monoid

• A **monoid** is a set equipped with an **associative binary operation** and an **identity element**
• For example: (N,+) is a commutative monoid whose identity is zero

• The **free monoid** on a set is the monoid whose elements are **all the finite sequences (or strings) of zero or more elements from that set**
• **String concatenation** is the monoid operation
• The unique sequence of zero elements, the empty string (denoted by $\varepsilon$ or $\lambda$) is the **identity element** (it leaves any element of the set unchanged when combined with it)

• The **free monoid** on a set A is usually denoted A*

39

---

**Slide 40**
# Stephen Kleene

• Kleene star is widely used for **regular expressions**

• It was introduced by **Stephen Kleene** in this context

• **Stephen Kleene** (1909-1994)
• American mathematician
• Student of **Alonzo Church**

[Blue box: Lambda calculus, Church-Turing thesis]

[Image: Black and white photo of Stephen Kleene]

40

---

**Slide 41**
# Historical hints

• While the mathematical **concept** (free monoid) existed earlier in algebra (1930-40s), **the notation and computational focus came from Kleene** (1950s)

• As a student of Alonzo Church, Kleene was into the mathematical community. He applied the **properties** of free monoids to solve problems in computing

41

---

**Slide 42**
# What is a language?

42

---

**Slide 43**
[Image: Photo of Noam Chomsky with a quote. Speech bubble says "An Alphabet!". Text boxes highlight specific phrases in the quote.]

From now on I will consider a language to be a set (finite or infinite) of sentences, **each finite in length** and constructed out of a **finite set of elements**. All natural languages in their spoken or written form are languages in this sense.
— *Noam Chomsky* —

[Blue box text: And so are Programming Languages!]

43

---

**Slide 44**
[Image: A colorful world map showing languages spoken in different regions (e.g., French, Danish, Tatar, Russian, Turkic, Cantonese, Mandarin, Spanish, Italian, etc.). A legend shows language families like Indo-European, Afro-Asiatic, Turkic, etc.]

**What map is this?**

44

---

**Slide 45**
# Languages

• A **language is a set of strings over an alphabet**
• Languages:
– Russian, Italian, English, French
– C, Java, Pascal, Eiffel
but also
– Graphical languages
– Music
– Multimedia

45

---

**Slide 46**
# Formally

• A language **L** over an alphabet **A** is a **subset** of **A\***
• Examples
– A={a, b, c}
A*={$\varepsilon$, a, b, c, aa, ab, ac, ba, bb, bc, ca, …}
$L_1$= {$\varepsilon$, a, b, c, bc, ca}
$L_2$= {aa, ab, ac, ba, bb, bc, ca, cb, cc}

46

---

**Slide 47**
# Theoretical Computer Science

**Operations on Languages**
Lecture 2 - Manuel Mazzara

47

---

**Slide 48**
# Operations

• Operations on **sets** apply also to **languages**
– **A language is a set of strings**
• Operations on languages are
– Union
– Intersection
– Difference
– Complement
– Concatenation
– Power of n
– Kleene star/closure

48

---

**Slide 49**
# Set operations (1)

• $L_1 \cup L_2$
– Example:
$L_1$= {$\varepsilon$, a, b, c, **bc, ca**}
$L_2$= {ba, bb, **bc, ca**, cb, cc}
$L_1 \cup L_2$ = {$\varepsilon$, a, b, c, ba, bb, bc, ca, cb, cc}

• $L_1 \cap L_2$
– Example: $L_1 \cap L_2$ = {bc, ca}

49

---

**Slide 50**
# Set operations (2)

• $L_1 \setminus L_2$ (or $L_1 – L_2$)
– Generally used when $L_2 \subseteq L_1$
– Example:
$L_1$= { ba, bb, **bc, ca**, cb, cc }
$L_2$= { **bc, ca** }
$L_1 \setminus L_2$ = {ba, bb, cb, cc}

• $L^c=A^* \setminus L$
– A is the alphabet over which L is defined
– Example: $L_1^c$ = set of all strings on {a,b,c}* except the strings of length 2 that start with a ‘b’ or a ‘c’

50

---

**Slide 51**
# Concatenation

• $L_1 \cdot L_2$ (or $L_1L_2$)={x⋅y | x$ \in L_1$, y$ \in L_2$}
– Remark: ‘⋅’ is **not commutative**
– $L_1 \cdot L_2 \neq L_2 \cdot L_1$

• Example
$L_1$= {$\varepsilon$, a, b, c, bc, ca}
$L_2$= {ba, bb, bc, ca, cb, cc}
$L_1L_2$ = {ba, bb, bc, ca, cb, cc, aba, abb, abc, aca, acb, acc, bba, bbb, bbc, bca, bcb, bcc, cba, cbb, cbc, cca, ccb, ccc, bcba, bcbb, bcbc, bcca, bccb, bccc , caba, cabb, cabc, caca, cacb, cacc}

51

---

**Slide 52**
# Power

• $L^n$ is obtained by concatenating L with itself n times
– $L^0$ = {$\varepsilon$}
– $L^i$ = $L^{i-1} \cdot L$

• Examples:
– $L^2=L \cdot L$
– $L^3=L \cdot L \cdot L$
– $L^4=L \cdot L \cdot L \cdot L$
– …

• Remark: ‘⋅’ is associative

52

---

**Slide 53**
# Associative Law (1)

[Image: Diagram using groups of colored dots to illustrate associativity.
Left side: (Group of 6 blue dots + Group of 3 orange dots) + Group of 4 yellow dots.
Right side: Group of 6 blue dots + (Group of 3 orange dots + Group of 4 yellow dots).]

(6 + 3) + 4 = 6 + (3 + 4)

**Do you remember it?**

53

---

**Slide 54**
# Associative Law (2)

[Image: Diagram using blocks to illustrate associativity.
Left side: A rectangular prism of blocks divided into two groups of 4x3 blocks, labeled (2 x 4) x 3.
Right side: A rectangular prism of blocks divided into three groups of 2x4 blocks, labeled 2 x (4 x 3).]

(2 × 4) × 3 = 2 × (4 × 3)

**Do you remember it?**

54

---

**Slide 55**
# Kleene Star (1)

• Kleene star is a **unary operation**, either *on sets of strings or on sets of symbols*

• The application of the Kleene star to a set A is written as A*

• Defined by Stephen Kleene in the context of regular expressions (will see this later in the course)

55

---

**Slide 56**
# Kleene Star (2)

Given a set V we define:

$V_0 = \{\varepsilon\}$ (the language consisting only of the empty string),
$V_1 = V$
$V_{i+1} = \{ wv : w \in V_i \text{ and } v \in V \}$ for each i>0.

[Blue box: Inductive definition]

**$V^* = \bigcup_{i \in \mathbb{N}} V_i = \{\varepsilon\} \cup V \cup V_2 \cup V_3 \cup V_4 \cup ....$**

56

---

**Slide 57**
# What do formal languages represent?

• A language is a **set of strings**
– $L_1$= {bc, ca}
– $L_2$= {ba, bb, bc, ca, cb, cc}
– $L_3$= {x$\in${a,b}*| (∃ y $\in${a,b}*) x=ay}

• How can sets of strings be applied in computer science?
– Formal languages are not only mere mathematical representations

57

---

**Slide 58**
# Languages in CS

• A language is a way of **representing** or **communicating** information
– Not just meaningless strings
• There are many kinds of languages
– Natural languages
– Programming languages
– Logic languages
– …

58

---

**Slide 59**
# Example (1)

• Consider the following languages:
– $L_1$: set of “Word@Mac” documents
– $L_2$: set of “Word@PC” documents

• Operations:
– $L_1^c$ is set of documents that are not compatible with “Word@Mac”
– $L_1 \cup L_2$ is the set of documents that are compatible with either Mac or PC
– $L_1 \cap L_2$ is the set of documents that are compatible with both Mac and PC

59

---

**Slide 60**
# Example (2)

• Consider the following languages:
– $L_1$: set of e-mail messages
– $L_2$: set of spam messages

• Operations:
– $L_1-L_2$ implements a filter

60

---

**Slide 61**
# Languages in practice

• A language can represent
– **Computations**
– Documents
– Programs
– Multimedia

• **Operations** on languages create new classes of languages

61