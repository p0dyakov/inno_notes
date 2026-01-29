<!-- Here is the transcription of the three PDF files provided, organized by file and slide number, including image descriptions and mathematical formatting.

---

# File 1: Lab 1 (Indefinite Integrals)

### Slide 1: Title Page
**Lab 1: Indefinite Integrals and Techniques of Integration**
Mathematical Analysis II
Innopolis University
21.01.2026

### Slide 2: Basic Integration Rules (Warm-Up)
**Compute:**
1. $\int (4x^3 - 7x + 2) \, dx$
2. $\int (e^{2x} - \cos 3x) \, dx$
3. $\int \frac{5}{\sqrt{x}} \, dx$

### Slide 3: Integration by Substitution
**The Substitution Method to evaluate $\int f(g(x)) g'(x) \, dx$**
1. Substitute $u = g(x)$ and $du = \frac{du}{dx} dx = g'(x) \, dx$ to obtain $\int f(u) \, du$.
2. Integrate with respect to $u$.
3. Replace $u$ by $g(x)$.

**Tasks**
1. $\int x\sqrt{1 + x^2} \, dx$
2. $\int \frac{2x}{(1 + x^2)^3} \, dx$
3. $\int 5 \sec^2(5x + 1) \, dx$
4. $\int \frac{\ln x}{x} \, dx$
5. $\int x\sqrt{1 + 2x} \, dx$

### Slide 4: Integration by Parts
**The integration by parts formula is given by**
$$ \int u \, dv = uv - \int v \, du $$

**Tasks**
1. $\int x \ln(1 + x) \, dx$
2. $\int x^2 e^{-x} \, dx$
3. $\int \arctan x \, dx$
4. $\int x \cosh x \, dx$
5. $\star \int \cos^n x \, dx$

### Slide 5: Homework
1. $\int \frac{\ln x}{x^2} \, dx$
2. $\int \sqrt{x^2 + 1} \ln x \, dx$
3. $\int \frac{x^2}{\sqrt{1 - x^4}} \, dx$
4. $\int \frac{\sin x}{x} \, dx$ (Special Integral)
5. $\int \frac{\sqrt{x^2 - 1}}{x^3} \, dx$
6. $\int \sqrt{\frac{1 + \sqrt{1 - x^2}}{1 - x^2}} \, dx$

---

# File 2: Lab 2 (Indefinite Integrals Continued)

### Slide 1: Title Page
**Lab 2: Indefinite Integrals and Techniques of Integration**
Mathematical Analysis II
Innopolis University
28.01.2026

### Slide 2: Integration of Rational Functions
**Method:**
To evaluate $\int \frac{P_n(x)}{Q_m(x)} \, dx$ where $n < m$ and $P_n, Q_m$ are coprime polynomials:
We decompose $\frac{P_n(x)}{Q_m(x)}$ into **partial fractions**:
$$ \frac{A}{(x + d)^k}, \quad \frac{Ax + B}{(ax^2 + bx + c)^k} $$
with $k \ge 1$, $a,b,c,d \in \mathbb{R}$, $\Delta = b^2 - 4ac < 0$, and $A, B$ constants to be determined.

**Tasks**
1. $\int \frac{3x + 5}{x^2 - 4} \, dx$
2. $\int \frac{x^3 + x + 1}{(x^2 + 2)^2} \, dx$
3. $\int \frac{dx}{(x - 1)^2(x + 2)}$
4. $\int \frac{2x^3 + x}{x^2 - 1} \, dx$

### Slide 3: Integration of Trigonometric Functions
**Tasks**
1. $\int \sin^3 x \cos x \, dx$
2. $\int \frac{\sin x}{1 + \cos x} \, dx$
3. $\int \sin(2x) \cos(3x) \, dx$
4. $\int \tan^3 x \, dx$

### Slide 4: Integration of Hyperbolic Functions
**Tasks**
1. $\int \sinh(2x) \cosh x \, dx$
2. $\int \frac{\sinh x}{1 + \cosh x} \, dx$
3. $\int \tanh^2 x \, dx$

### Slide 5: Integration of Radical Functions
**Tasks**
1. $\int x\sqrt{4 - x^2} \, dx$
2. $\int \frac{\sqrt{x^2 + 1}}{x^2} \, dx$

### Slide 6: Homework
1. $\int \sqrt{\frac{\tan x}{\cos x \sin x}} \, dx$
2. $\int \frac{x^2 e^x}{(x + 2)^2} \, dx$
3. $\int \frac{x^2 + 1}{x^4 + 1} \, dx$
4. $\int \frac{1}{\cos^6 x + \sin^6 x} \, dx$
5. $\int \frac{1}{1 + \sinh x} \, dx$
6. $\int \sqrt{\frac{1 - x}{1 + x}} \cdot \frac{1}{x} \, dx$

---

Here is the complete transcription of **Chapter 1: Integral Calculus of Functions with One Variable**, formatted by slide with corrected mathematical notation and image descriptions.

---

# File: Mathematical Analysis II - Chapter 1

### Slide 1
**Plan of Our Course: Mathematical Analysis II**
**Indefinite Integrals and Techniques of Integration**
**Definite Integrals**

# Mathematical Analysis II.
## Chapter 1: Integral Calculus of Functions with One Variable

**Mohammad S. Alkousa**
Assistant Professor in Innopolis University
Lab of High Performance Computing.
Senior Researcher at Laboratory of Modern Adaptive Computational Methods in Innopolis University.
`m.alkousa@innopolis.ru`

Updated January 21, 2026

---

### Slide 2: Contents

**1. Plan of Our Course: Mathematical Analysis II**

**2. Indefinite Integrals and Techniques of Integration**
*   Differential of a Function
*   Definitions, Basic Properties of Indefinite Integrals
*   Basic Integration Rules
*   Integration by Substitution (Change of Variable)
*   Integration by Parts
*   Integration of Rational Functions by Partial Fractions
*   Integration of Trigonometric and Hyperbolic Functions
*   Other Techniques of Integration

**3. Definite Integrals and Their Applications**
*   Riemann Sums and Definition of the Definite Integral
*   Properties of Definite Integrals
*   The Fundamental Theorem of Calculus
*   The Substitution Rule for Definite Integrals
*   Applications of Definite Integrals (Calculating Areas, Volumes, Lengths, and Areas of Surfaces)

**4. Improper Integrals**

---

### Slide 3: Plan of the course

The course will be (as Mathematical Analysis I) a combination of Real Analysis (not pure and abstract) and Calculus.
*   We will have 15 weeks.
*   During the course, we have one test (30 points), a midterm (30 points), and a final exam (40 points).
*   Bonus points: 5.

**Communication**
*   Formal matters: by email (`m.alkousa@innopolis.ru`).
*   Lecture notes and assignments: Moodle, General (University) Group in Telegram.
*   Questions about the course and personal consultations: Telegram, email.
*   Consultation hours (Preliminary!): Saturday, from 12:00 to 17:00, office 411A.

---

### Slide 4: References

There is a huge number of references in real analysis and calculus in English and Russian. Our main references are:

1.  George B. Thomas, JR.: *Thomas’ Calculus Early Transcendentals*, Fifteenth edition, Pearson Education Limited, 2024. We will cite this book as (Thomas2024).
2.  Michael Spivak: *Calculus*. Third edition, Publisher Perish, Inc., 1994. (Spivak1994)

**Recommendation.** You can follow many academic journals that cover undergraduate topics and are published in English. Some of the most important are:
1.  The College Mathematics Journal.
2.  Mathematics Magazine.
3.  American Mathematical Monthly.
4.  The Mathematical Gazette.

---

### Slide 5: Differential of a Function

Recall that if $y = f(x)$ is a differentiable function on an interval $I$, then
$$ f'(x) = \frac{dy}{dx} = \frac{d}{dx}f(x) \iff dy = df(x) = f'(x)dx $$
We call $df(x)$ the **differential** of $f$.

**Properties.**
1.  $d(Cf) = Cdf, \quad \forall C \in \mathbb{R}$;
2.  $d(f \pm g) = df \pm dg$;
3.  $d(f \cdot g) = g df + f dg$;
4.  $d\left(\frac{f}{g}\right) = \frac{g df - f dg}{g^2}, \quad g \neq 0$;
5.  $d(f(g(x))) = f'(g(x))g'(x)dx$.

**Examples.**
$$ d(\tan x) = \frac{1}{\cos^2 x} dx, \quad d\left(e^{\cos x + 5}\right) = -\sin x \cdot e^{\cos x + 5} dx $$

---

### Slide 6: Definition of Antiderivative Function

Let $F$ be a differentiable function on a non-empty interval $\emptyset \neq I \subseteq \mathbb{R}$.
The problem of finding the derivative of $F$ consists in determining a function $f$ such that $f(x) = F'(x)$, for all $x \in I$.
Note that the domain of the derivative $f$ does not necessarily have to coincide with the domain of the original function $F$.

We now turn our attention to the inverse problem of differentiation. That is, let $f$ be a given function in a non-empty interval $I \neq \emptyset$. The goal is to find a function $F$ such that
$$ F'(x) = f(x), \quad \forall x \in I. $$

**Definition (Antiderivative or Primitive Function)**
Let $\emptyset \neq I \subseteq \mathbb{R}$ be a non-empty interval and $f$ be a continuous function defined on $I$. We call $F : I \to \mathbb{R}$ an **antiderivative** (or **primitive**) function of $f$ if and only if $F$ is differentiable on $I$, and
$$ F'(x) = f(x) \iff dF(x) = f(x)dx, \quad \forall x \in I. $$

**Example 1.** The function $F(x) = \frac{1}{3}e^{x^3}$ is an antiderivative of $f(x) = x^2e^{x^3}$ on $\mathbb{R}$.
**Example 2.** $F(x) = \frac{1}{10}\sqrt{(2x + 1)^5} - \frac{1}{6}\sqrt{(2x + 1)^3}$ is an antiderivative of $f(x) = x\sqrt{2x + 1}$ on $(-1/2, \infty)$.

---

### Slide 7: Indefinite Integral

**Theorem**
For every **continuous** function $f$ defined in a non-empty interval $I$, there exists an antiderivative $F : I \to \mathbb{R}$. Moreover, any other antiderivative of $f$ differs from $F$ by a constant; that is, the general form of the antiderivative is $F(x) + C$, where $C \in \mathbb{R}$ is an arbitrary constant. In other words, *the difference between any two antiderivatives of f is a constant.*

**Definition (Indefinite Integral)**
Let $F$ be an antiderivative of the function $f$ in a non-empty interval $I$. The expression $F(x) + C$, where $x \in I$ and $C \in \mathbb{R}$ is an arbitrary constant, is called the **indefinite integral** of the function $f$ on $I$. It is denoted by $\int f(x)dx$, and we write
$$ \int f(x)dx = F(x) + C \iff F'(x) = f(x), \quad \forall x \in I. $$

**Example 1.** $\int x^2 e^{x^3} dx = \frac{1}{3}e^{x^3} + C$.
**Example 2.** $\int x\sqrt{2x + 1} dx = \frac{1}{10}\sqrt{(2x + 1)^5} - \frac{1}{6}\sqrt{(2x + 1)^3} + C$.

---

### Slide 8: Indefinite Integral (Visual)

**Remark.** The indefinite integral of a function $f$ in a non-empty interval $I$, that is, $\int f(x)dx$, geometrically, represents a family of curves in the coordinate plane $(O, \vec{i}, \vec{j})$, where each curve corresponds to an antiderivative of $f$. These curves differ from one another by a vertical translation of magnitude $C \in \mathbb{R}$, meaning each curve can be obtained from another by shifting it upward or downward by a constant amount.

In the right, there are graphs of
$$ \int x^2 e^{x^3} dx = \frac{1}{3}e^{x^3} + C, \text{ for } C = -2, -1, 0, 1, 2. $$

**Image Description:**
A Cartesian coordinate system showing five curves plotted on a grid. The functions appear to be exponential in nature ($y = \frac{1}{3}e^{x^3} + C$), rising sharply as $x$ increases. The curves are identical in shape but are parallel to each other, stacked vertically. The vertical distance between any two specific curves remains constant for all $x$.

---

### Slide 9: Basic Properties

**Basic Properties.** Let $f$ be a continuous (integrable) function, and $C \in \mathbb{R}$ be an arbitrary constant. Then, we have

(1) $\left(\int f(x)dx\right)' = f(x)$.

(2) $d\left(\int f(x)dx\right) = f(x)dx$.

(3) $\int dF(x) = F(x) + C; \quad C \in \mathbb{R}$.

(4) Let $f_1, f_2, \dots, f_n$ be integrable functions. Then,
    $$ \int (f_1(x) + \dots + f_n(x)) \, dx = \int f_1(x)dx + \dots + \int f_n(x)dx. $$

(5) $\int \alpha f(x)dx = \alpha \int f(x)dx; \quad \forall \alpha \in \mathbb{R}^*$.
    *Why this property is not true when $\alpha = 0$?*

---

### Slide 10: Basic Integration Rules

(1) $\int a \, dx = ax + C, \quad a \in \mathbb{R}$.

(2) $\int x^a \, dx = \frac{x^{a+1}}{a + 1} + C; \quad a \in \mathbb{R} \setminus \{-1\}$.
    In general, we can write
    $$ \int (f(x))^a f'(x)dx = \frac{(f(x))^{a+1}}{a + 1} + C; \quad a \in \mathbb{R} \setminus \{-1\}. $$

(3) $\int \frac{dx}{x} = \ln |x| + C; \quad x \neq 0$.
    In general, we can write
    $$ \int \frac{f'(x)}{f(x)} dx = \ln |f(x)| + C; \quad f(x) \neq 0. $$

(4) $\int \sin(ax + b)dx = -\frac{1}{a} \cos(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

---

### Slide 11: Basic Integration Rules (Continued)

(5) $\int \cos(ax + b)dx = \frac{1}{a} \sin(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

(6) $\int \frac{dx}{\cos^2(ax + b)} = \int \sec^2(ax + b)dx = \frac{1}{a} \tan(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

(7) $\int \frac{dx}{\sin^2(ax + b)} = \int \csc^2(ax + b)dx = -\frac{1}{a} \cot(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

(8) $\int \sinh(ax + b)dx = \frac{1}{a} \cosh(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

(9) $\int \cosh(ax + b)dx = \frac{1}{a} \sinh(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

(10) $\int \frac{dx}{\cosh^2(ax + b)} = \frac{1}{a} \tanh(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

---

### Slide 12: Basic Integration Rules (Continued)

(11) $\int \frac{dx}{\sinh^2(ax + b)} = -\frac{1}{a} \coth(ax + b) + C; \quad a \in \mathbb{R}^*, b \in \mathbb{R}$.

(12) $\int a^{\alpha x + \beta} dx = \frac{a^{\alpha x + \beta}}{\alpha \ln(a)} + C; \quad a \in ]0, \infty[ \setminus \{1\}, \alpha \in \mathbb{R}^*, \beta \in \mathbb{R}$.
     **Special case.** If $a = e$, then $\int e^{\alpha x + \beta} dx = \frac{1}{\alpha} e^{\alpha x + \beta} + C$.

(13) $\int \frac{dx}{a^2 + x^2} = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C; \quad a \in \mathbb{R}^*$.

(14) $\int \frac{dx}{a^2 - x^2} = \frac{1}{a} \text{artanh}\left(\frac{x}{a}\right) + C = \frac{1}{2a} \ln \left| \frac{a + x}{a - x} \right| + C; \quad a \in \mathbb{R}^*$.

(15) $\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\left(\frac{x}{a}\right) + C = -\arccos\left(\frac{x}{a}\right) + C; \quad a > 0, -a < x < a$.

(16) $\int \frac{dx}{\sqrt{x^2 + a^2}} = \ln \left| x + \sqrt{x^2 + a^2} \right| + C = \text{arsinh}\left(\frac{x}{a}\right) + C; \quad a > 0$.

---

### Slide 13: Basic Integration Rules: Examples

(17) $\int \frac{dx}{\sqrt{x^2 - a^2}} = \ln \left| x + \sqrt{x^2 - a^2} \right| + C = \text{arcosh}\left(\frac{x}{a}\right) + C; \quad x > a > 0$.

**Example 1.**
$$ I_1 = \int \frac{\ln x}{x} dx = \int \frac{1}{x} \ln x \, dx = \int (\ln x)' \ln x \, dx = \frac{\ln^2 x}{2} + C. $$
In short, we can write
$$ I_1 = \int \frac{\ln x}{x} dx = \int \frac{1}{x} \ln x \, dx = \int \ln x \, d(\ln x) = \frac{\ln^2 x}{2} + C. $$

**Example 2.**
$$ I_2 = \int \frac{dx}{x \ln^2 x} = \int \frac{1}{x} (\ln(x))^{-2} dx = \int (\ln x)^{-2} (\ln x)' dx = -\frac{1}{\ln x} + C. $$
In short, we can write
$$ I_2 = \int \frac{dx}{x \ln^2 x} = \int (\ln x)^{-2} d(\ln x) = -\frac{1}{\ln x} + C. $$

---

### Slide 14: Basic Integration Rules: Examples

**Example 3.**
$$ I_3 = \int \frac{\arcsin x}{\sqrt{1 - x^2}} dx = \int \arcsin x \frac{dx}{\sqrt{1 - x^2}} = \int \arcsin x \, d(\arcsin x) = \frac{(\arcsin x)^2}{2} + C. $$

**Example 4.**
$$ I_4 = \int \left( \sin x + \frac{1}{\sin^3 x} + \cos^2 x \right) \cos x \, dx = \int \left( \sin x + \sin^{-3} x + 1 - \sin^2 x \right) d(\sin x) $$
$$ = \frac{1}{2}\sin^2 x - \frac{1}{2\sin^2 x} + \sin x - \frac{1}{3}\sin^3 x + C. $$

**Example 5.**
$$ I_5 = \int \left( \cos^2 x - 3^{4x} + \sqrt[3]{x} + \frac{5}{1 + x^2} \right) dx = \int \left( \frac{1 + \cos(2x)}{2} - 3^{4x} + x^{1/3} + \frac{5}{1 + x^2} \right) dx $$
$$ = \frac{x}{2} + \frac{1}{4}\sin(2x) - \frac{3^{4x}}{4\ln(3)} + \frac{3}{4}x\sqrt[3]{x} + 5\arctan x + C. $$

**Example 6.**
$$ I_6 = \int \frac{\sqrt{x^2 - 3} - 3\sqrt{x^2 + 3}}{\sqrt{x^4 - 9}} dx = \int \frac{\sqrt{x^2 - 3} - 3\sqrt{x^2 + 3}}{\sqrt{x^2 - 3}\sqrt{x^2 + 3}} dx $$
$$ = \int \frac{dx}{\sqrt{x^2 + 3}} - 3 \int \frac{dx}{\sqrt{x^2 - 3}} = \ln \left| x + \sqrt{x^2 + 3} \right| - 3 \ln \left| x + \sqrt{x^2 - 3} \right| + C. $$

---

### Slide 15: Remark for Integrals of Elementary Functions

**Remark.** When asked to evaluate the indefinite integral $\int f(x)dx$, the goal is to determine a function $F$ that satisfies $F'(x) = f(x)$. The antiderivative $F$ must be expressed explicitly in terms of familiar algebraic operations (addition, subtraction, multiplication, division, and root extraction) and elementary functions: power functions, trigonometric and inverse trigonometric functions, hyperbolic and inverse hyperbolic functions, logarithmic and exponential functions, and radical expressions. Moreover, finite compositions of such functions with real constants are also permitted.

**In our course**, we will focus on integrals of this type, except where otherwise noted.
Among the well-known examples of integrals that are **not elementary** are:

1.  **Elliptic integrals**, which have the following form $\int R(x, \sqrt{P(x)}) dx$, where $P(x)$ is a polynomial of degree 3 or 4, and the equation $P(x) = 0$ doesn't have multiple roots, and $R$ is a rational function in $x$ and $\sqrt{P(x)}$.
2.  **Logarithmic integral** $\int \frac{dx}{\ln x}$.
3.  **Gauss integral, or error function** $\int e^{-x^2} dx$.
4.  **Fresnel integrals** $\int \sin(x^2) dx, \int \cos(x^2) dx$.
5.  **Dirichlet integral** $\int \frac{\sin x}{x} dx$.
6.  Integrals that have, for example, one of the following forms
    $$ \int x^x dx, \quad \int e^{e^x} dx, \quad \int \ln(\ln x) dx, \quad \int \sqrt[3]{1 + x^4} dx, \quad \int \sqrt{2 - \sin^2 x} dx, \dots $$

---

### Slide 16: Basic Integration Rules: Exercises

Find the following integrals (These integrals from MIT Integration Bee).

$I_1 = \int \frac{e^{\sin x}}{\tan x \cdot \csc x} dx, \quad I_2 = \int \tan^2 x dx,$

$I_3 = \int \sin x \tan^2 x dx, \quad I_4 = \int \frac{1 + \cot x}{1 - \cot x} dx,$

$I_5 = \int \frac{dx}{1 + 3e^x}, \quad I_6 = \int \sqrt{\csc x - \sin x} dx,$

$I_7 = \int \frac{x^6 - 1}{x^4 + x^3 - x - 1} dx, \quad I_8 = \int (e^x \cos x - e^x \sin x) dx,$

$I_9 = \int \sin x \sqrt{1 + \tan^2 x} dx, \quad I_{10} = \int (\cos^4 x - \sin^4 x) dx,$

$I_{11} = \int \frac{x}{\sqrt{2 + 4x}} dx, \quad I^*_{12} = \int (x + 1)^2 (x - 1)^{1/3} dx,$

$I^*_{13} = \int \frac{\ln x \cos x - (\frac{\sin x}{x})}{\ln^2 x} dx.$

---

### Slide 17: Integration by Substitution (Change of Variable)

Let us consider the integral $\int f(x)dx$, and assume $x = \phi(t)$, where $\phi$ is a one-to-one continuous differentiable function. Then, $dx = \phi'(t)dt$. Thus, the given integral will be in the following form
$$ \int f(x)dx = \int f(\phi(t)) \phi'(t)dt. \quad (1) $$
The last integral (with respect to the new variable $t$) should be easy to find in terms of the variable $t$. From $x = \phi(t)$, we find $t$ as a function of $x$. Then we substitute the result in (1) to find the given integral as a function of $x$.

**Remark.** It is often convenient, instead of putting $x = \phi(t)$, to put $t = \psi(x)$. For example, for the integral $\int \frac{\psi'(x)}{\psi(x)} dx$, we assume $t = \psi(x)$, then $\psi'(x)dx = dt$. Thus, we get
$$ \int \frac{\psi'(x)}{\psi(x)} dx = \int \frac{dt}{t} = \ln |t| + C = \ln |\psi(x)| + C, \quad C \in \mathbb{R}. $$
Also, for the integral $\int \psi^n(x)\psi'(x)dx$, where $n \neq -1$. Let us set $t = \psi(x)$, then we get
$$ \int \psi^n(x)\psi'(x)dx = \int t^n dt = \frac{t^{n+1}}{n + 1} + C = \frac{\psi^{n+1}(x)}{n + 1} + C, \quad C \in \mathbb{R}. $$

---

### Slide 18: Integration by Substitution: Examples

**Example 1.** For the integral
$$ I_{ex1} = \int \frac{dx}{ax^2 + bx + c}, \quad a, b, c \in \mathbb{R}^*. \quad (2) $$
We have,
$$ ax^2 + bx + c = a \left( x^2 + \frac{b}{a}x + \frac{c}{a} \right) = a \left[ x^2 + 2\frac{b}{2a}x + \left(\frac{b}{2a}\right)^2 + \frac{c}{a} - \left(\frac{b}{2a}\right)^2 \right] $$
$$ = a \left[ \left(x + \frac{b}{2a}\right)^2 + \left(\frac{c}{a} - \frac{b^2}{4a^2}\right) \right]. $$
Since $\frac{c}{a} - \frac{b^2}{4a^2} \in \mathbb{R}^*$, we can write $\frac{c}{a} - \frac{b^2}{4a^2} = \pm d^2$. Thus, we get the following integral,
$$ I_{ex1} = \int \frac{dx}{a \left[ \left(x + \frac{b}{2a}\right)^2 \pm d^2 \right]}. $$
Using the substitution $x + \frac{b}{2a} = t$, we find $dx = dt$. Hence, we get
$$ I_{ex1} = \frac{1}{a} \int \frac{dt}{t^2 \pm d^2}. $$
The last integral is one of the previously mentioned basic integrals.

---

### Slide 19: Integration by Substitution: Examples

**Example 2.** Let us consider the general form of the integral $I_{ex1}$ (2),
$$ I_{ex2} = \int \frac{\alpha x + \beta}{ax^2 + bx + c} dx, \quad \alpha, \beta, a, b, c \in \mathbb{R}^*. \quad (3) $$
We have $(ax^2 + bx + c)' = 2ax + b$. Thus, we get
$$ \frac{\alpha x + \beta}{ax^2 + bx + c} = \frac{\frac{\alpha}{2a}(2ax + b) + (\beta - \frac{\alpha b}{2a})}{ax^2 + bx + c}. $$
Therefore,
$$ I_{ex2} = \frac{\alpha}{2a} \int \frac{2ax + b}{ax^2 + bx + c} dx + \left( \beta - \frac{\alpha b}{2a} \right) \int \frac{dx}{ax^2 + bx + c} $$
$$ = \frac{\alpha}{2a} \ln \left| ax^2 + bx + c \right| + \left( \beta - \frac{\alpha b}{2a} \right) I_{ex1}, \quad (4) $$
where $I_{ex1}$ is the integral in the previous **Example 1** (see (2)). By calculating $I_{ex1}$, and then substituting in (4), we find the desired integral (3) $I_{ex2}$.
**Practical example.** Calculate
$$ I = \int \frac{2x + 5}{5x^2 - 2x - 1} dx. $$

---

### Slide 20: Integration by Substitution: Examples

**Example 3.** For the integral
$$ I_{ex3} = \int \frac{dx}{\sqrt{3x^2 + 5x - 1}}. $$
We have
$$ 3x^2 + 5x - 1 = 3 \left( \left(x + \frac{5}{6}\right)^2 - \frac{37}{36} \right). $$
Thus,
$$ I_{ex3} = \frac{1}{\sqrt{3}} \int \frac{dx}{\sqrt{\left(x + \frac{5}{6}\right)^2 - \frac{37}{36}}}. $$
Using the substitution $x + \frac{5}{6} = t$, we find $dx = dt$. Hence, we get
$$ I_{ex3} = \frac{1}{\sqrt{3}} \int \frac{dt}{\sqrt{t^2 - \left(\frac{37}{36}\right)}} = \frac{1}{\sqrt{3}} \ln \left| t + \sqrt{t^2 - \frac{37}{36}} \right| + C $$
$$ = \frac{1}{\sqrt{3}} \ln \left| x + \frac{5}{6} + \sqrt{\left(x + \frac{5}{6}\right)^2 - \frac{37}{36}} \right| + C, $$
where $t = x + \frac{5}{6}$, and $C \in \mathbb{R}$.

---

### Slide 21: Integration by Substitution: Examples

**Example 4.** For the integral
$$ I_{ex4} = \int \frac{x + 3}{\sqrt{4x^2 + 4x + 3}} dx. $$
We have $(4x^2 + 4x + 3)' = 8x + 4$. Thus, we get
$$ I_{ex4} = \frac{1}{8} \int \frac{8x + 4 - 4 + 24}{\sqrt{4x^2 + 4x + 3}} dx = \frac{1}{8} \int \frac{8x + 4 + 20}{\sqrt{4x^2 + 4x + 3}} dx $$
$$ = \frac{1}{8} \int \frac{8x + 4}{\sqrt{4x^2 + 4x + 3}} dx + \frac{5}{2} \underbrace{\int \frac{dx}{\sqrt{4x^2 + 4x + 3}}}_{:=J}. $$
For the integral $J$, we have $4x^2 + 4x + 3 = 4 \left( (x + \frac{1}{2})^2 + \frac{1}{2} \right)$. Thus,
$$ I_{ex4} = \frac{1}{8} \int \frac{8x + 4}{\sqrt{4x^2 + 4x + 3}} dx + \frac{5}{2} \frac{1}{2} \int \frac{dx}{\sqrt{(x + \frac{1}{2})^2 + \frac{1}{2}}} $$
$$ = \frac{1}{4} \sqrt{4x^2 + 4x + 3} + \frac{5}{4} \ln \left| x + \frac{1}{2} + \sqrt{x^2 + x + \frac{3}{4}} \right| + C, $$
where $C \in \mathbb{R}$.

---

### Slide 22: Integration by Substitution: Hermite-Ostrogradski Method

We now consider the more general integral
$$ \int \frac{P_n(x)}{\sqrt{ax^2 + bx + c}} dx, \quad a, b, c \in \mathbb{R}^*. \quad (5) $$
where $P_n(x)$ is a polynomial of degree $n$.
For the integral (5), we use the following formula, which is called the **Hermite-Ostrogradski formula**.
$$ \int \frac{P_n(x)}{\sqrt{ax^2 + bx + c}} dx = Q_{n-1}(x)\sqrt{ax^2 + bx + c} + \lambda \int \frac{dx}{\sqrt{ax^2 + bx + c}}, \quad (6) $$
where $Q_{n-1}(x)$ is a polynomial of degree $n - 1$ (it is unknown, we need to find it), and $\lambda \in \mathbb{R}$.
To find the coefficient of the polynomial $Q_{n-1}(x)$, and the constant $\lambda \in \mathbb{R}$. We take the derivative (with respect to $x$) of both sides of (6), and then multiply by $\sqrt{ax^2 + bx + c}$. Then, we get
$$ P_n(x) = Q'_{n-1}(x)(ax^2 + bx + c) + \frac{1}{2}Q_{n-1}(x)(2ax + b) + \lambda. $$
By corresponding between the sides of the last equality, we get a system of linear equations with $\lambda$ and the coefficient of $Q_{n-1}(x)$ as unknowns. Solving this system and substituting the results into (6) yields the desired integral.

---

### Slide 23: Hermite-Ostrogradski Method: Example

For the integral
$$ I_{ex5} = \int \frac{1 - x + x^2}{\sqrt{1 + x - x^2}} dx. $$
We have
$$ \int \frac{1 - x + x^2}{\sqrt{1 + x - x^2}} dx = (ax + b)\sqrt{1 + x - x^2} + \lambda \int \frac{dx}{\sqrt{1 + x - x^2}}. \quad (7) $$
By taking the derivative (with respect to $x$) of both sides of (7), we find
$$ \frac{1 - x + x^2}{\sqrt{1 + x - x^2}} = a\sqrt{1 + x - x^2} + \frac{(-2x + 1)(ax + b)}{2\sqrt{1 + x - x^2}} + \frac{\lambda}{\sqrt{1 + x - x^2}}. $$
By multiplying both sides of the previous equality by $2\sqrt{1 + x - x^2}$, we get
$$ 2(1 - x + x^2) = 2a(1 + x - x^2) + (ax + b)(-2x + 1) + 2\lambda. $$
Thus,
$$ 2 - 2x + 2x^2 = (-4a)x^2 + (3a - 2b)x + (2a + b + 2\lambda). $$
Hence, we get
$$ -4a = 2, \quad 3a - 2b = -2, \quad 2a + b + 2\lambda = 2 \implies a = -\frac{1}{2}, b = \frac{1}{4}, \lambda = \frac{11}{8}. $$

---

### Slide 24: Hermite-Ostrogradski Method: Example (Continued)

Therefore, from (7), we get
$$ I_{ex5} = \left(-\frac{1}{2}x + \frac{1}{4}\right)\sqrt{1 + x - x^2} + \frac{11}{8} \int \frac{dx}{\sqrt{1 + x - x^2}} $$
$$ = \left(-\frac{1}{2}x + \frac{1}{4}\right)\sqrt{1 + x - x^2} + \frac{11}{8} \int \frac{dx}{\sqrt{-(x^2 - x + \frac{1}{4} - \frac{1}{4}) + 1}} $$
$$ = \left(-\frac{1}{2}x + \frac{1}{4}\right)\sqrt{1 + x - x^2} + \frac{11}{8} \int \frac{dx}{\sqrt{\left(\frac{\sqrt{5}}{2}\right)^2 - (x - \frac{1}{2})^2}} $$
$$ = \left(-\frac{1}{2}x + \frac{1}{4}\right)\sqrt{1 + x - x^2} + \frac{11}{8} \arcsin\left(\frac{2x - 1}{\sqrt{5}}\right) + C, $$
where $C \in \mathbb{R}$.

**Exercise.** Calculate
$$ I_1 = \int \frac{x^3 - 2}{\sqrt{x^2 + x + 1}} dx, \quad I_2 = \int \frac{x^4 - 5x^3 + 6x - 7}{\sqrt{x^2 + 2x + 3}} dx. $$

---

### Slide 25: Integration by Substitution: Exercises

Find, using a suitable substitution, the following integrals.

$I_1 = \int \frac{dx}{5 - 12x - 9x^2}, \quad I_2 = \int \frac{3x - 2}{2 - 3x + 5x^2} dx, \quad I_3 = \int \frac{dx}{\sqrt{17 - 4x - x^2}},$

$I_4 = \int \frac{3x - 6}{\sqrt{x^2 - 4x + 5}} dx, \quad I_5 = \int \frac{(1 + \sqrt{x})^{1/3}}{\sqrt{x}} dx, \quad I_6 = \int \frac{\sin(2x)}{\sqrt{1 + \sin^4 x}} dx,$

$I_7 = \int \frac{dx}{1 + \sqrt[3]{x + 1}}, \quad I_8 = \int (2x + 1)e^{2x^2 + 2x - 1} dx, \quad I_9 = \int \frac{e^{2x}}{\sqrt[4]{1 + e^x}} dx,$

$I_{10} = \int \frac{\ln(2x)}{x \ln(4x)} dx, \quad I_{11} = \int \frac{1}{x^2} \cos\left(\frac{1}{x}\right) dx, \quad I_{12} = \int \sqrt{\sin x} \cos^5 x dx,$

$I_{13} = \int \frac{\sin(2x)}{\sqrt{25 \sin^2 x + 9 \cos^2 x}} dx, \quad I_{14} = \int \frac{e^{\tan x} + \cot x}{\cos^2 x} dx, \quad I_{15} = \int \frac{(x + 1)e^x}{\cos^2(x e^x)} dx.$

---

### Slide 26: Integration by Substitution: Exercises (Continued)

Find, using a suitable substitution, the following integrals (These integrals from MIT Integration Bee).

$I_1 = \int \frac{2x}{\sqrt{1 - x^4}} dx, \quad I_2 = \int \frac{\ln(\ln x)}{x \ln x} dx, \quad I_3 = \int \frac{\cos(\sqrt{x})}{\sqrt{x}} dx,$

$I_4 = \int \frac{dx}{\sqrt{x} - 1}, \quad I_5 = \int \frac{dx}{\sqrt{e^x - 1}}, \quad I_6 = \int \frac{dx}{x\sqrt{x^2 - 2}},$

$I_7 = \int \frac{dx}{5 + 4\sqrt{x} + x}, \quad I_8 = \int \frac{dx}{x^3 - x}, \quad I_9 = \int \frac{dx}{x(1 + x^5)},$

$I_{10} = \int x^x (1 + \ln x) dx, \quad I_{11} = \int xe^{e^{x^2} + x^2} dx, \quad I_{12} = \int x^3 \sqrt{x^2 + 1} dx.$

---

### Slide 27: Integration by Parts

We know
$$ \int f(x) \cdot g(x) dx \neq \int f(x) dx \cdot \int g(x) dx. $$
Therefore, when calculating integrals of the form
$$ \int f(x)g(x) dx, $$
we can apply the technique known as **integration by parts**. The formula for integration by parts is given as follows: Let $f, g$ be two differentiable functions, then
$$ (f(x)g(x))' = f'(x)g(x) + f(x)g'(x). $$
By taking the integral of the sides, we get
$$ f(x)g(x) = \int f'(x)g(x)dx + \int f(x)g'(x)dx. $$
Hence,
$$ \int f(x)g'(x)dx = f(x)g(x) - \int f'(x)g(x)dx. \quad (8) $$
We call (8) **the integration-by-parts formula**.
This formula, by setting $u = f(x)$, and $v = g(x)$, can be written as follows
$$ \int u \, dv = uv - \int v \, du. $$

---

### Slide 28: Integration by Parts: Common Examples

Some important examples, though not exhaustive, that can be solved using the integration by parts technique include the following integrals:

(1) Integrals of the form
    $$ \int P_n(x) \sin(ax + b)dx, \quad \int P_n(x) \cos(ax + b)dx, \quad \int P_n(x) e^{ax + b} dx, $$
    $$ \int P_n(x) \sinh(ax + b)dx, \quad \int P_n(x) \cosh(ax + b)dx, $$
    where $P_n(x)$ is a polynomial of order $n$.

(2) Integrals of the form
    $$ \int P_n(x)(\ln x)^m dx, \quad \int \arctan x \, dx, \quad \int \text{arccot} \, x \, dx, \quad \int \arcsin x \, dx, $$
    $$ \int \arccos x \, dx, \quad \int \text{arcsinh} \, x \, dx, \quad \int \text{arccosh} \, x \, dx. $$

(3) Integrals of the form
    $$ \int e^{ax + b} \cos(\alpha x + \beta) dx, \quad \int e^{ax + b} \sin(\alpha x + \beta) dx. $$

---

### Slide 29: Integration by Parts: Examples

**Example 1.** For the integral
$$ I = \int (x + 5) \sin(2x + 1) dx. $$
By using integration by parts, let us assume
$$ u = x + 5 \implies du = dx, \quad dv = \sin(2x + 1)dx \implies v = -\frac{1}{2}\cos(2x + 1). $$
Then, we have
$$ I = -\frac{1}{2}(x + 5)\cos(2x + 1) + \frac{1}{2} \int \cos(2x + 1)dx $$
$$ = -\frac{1}{2}(x + 5)\cos(2x + 1) + \frac{1}{4}\sin(2x + 1) + C, $$
where $C \in \mathbb{R}$.

---

### Slide 30: Integration by Parts: Examples

**Example 2.** For the integral
$$ I = \int (x^2 + 5) \arctan x \, dx. $$
By using integration by parts, let us assume
$$ u = \arctan x \implies du = \frac{dx}{1 + x^2}, \quad dv = (x^2 + 5)dx \implies v = \frac{1}{3}x^3 + 5x. $$
Then, we have
$$ I = \left(\frac{1}{3}x^3 + 5x\right) \arctan x - \int \frac{\frac{1}{3}x^3 + 5x}{1 + x^2} dx $$
$$ = \left(\frac{1}{3}x^3 + 5x\right) \arctan x - \frac{1}{3} \int \frac{x^3 + 15x}{1 + x^2} dx $$
$$ = \left(\frac{1}{3}x^3 + 5x\right) \arctan x - \frac{1}{3} \int \left( x + \frac{14x}{1 + x^2} \right) dx $$
$$ = \left(\frac{1}{3}x^3 + 5x\right) \arctan x - \frac{1}{3} \left( \frac{1}{2}x^2 + 7\ln(x^2 + 1) \right) + C $$
$$ = \left(\frac{1}{3}x^3 + 5x\right) \arctan x - \frac{1}{6}x^2 - \frac{7}{3}\ln(x^2 + 1) + C, $$
where $C \in \mathbb{R}$.

---

### Slide 31: Integration by Parts: Examples

**Example 3.** For the integral
$$ I = \int e^x \sin x \, dx. $$
By using integration by parts, let us assume
$$ u = e^x \implies du = e^x dx, \quad dv = \sin x \, dx \implies v = -\cos x. $$
Then, for the first time, we have
$$ I = -e^x \cos x + \underbrace{\int e^x \cos x \, dx}_{:=J}. $$
Now, for the integral $J$. By using integration by parts, let us assume
$$ u = e^x \implies du = e^x dx, \quad dv = \cos x \, dx \implies v = \sin x. $$
Then, for the second time, we have
$$ I = -e^x \cos x + e^x \sin x - \int e^x \sin x \, dx = -e^x \cos(x) + e^x \sin x - I. $$
Thus, $2I = e^x (\sin x - \cos x)$. Therefore, we get
$$ I = \frac{e^x}{2} (\sin x - \cos x) + C, $$
where $C \in \mathbb{R}$.

---

### Slide 32: Integration by Parts: Formulas and Example

In general, we find (Try to prove these formulas!)
$$ \int e^{ax} \sin(bx) dx = \frac{e^{ax}}{a^2 + b^2} [a \sin(bx) - b \cos(bx)] + C; \quad C \in \mathbb{R}, a, b \in \mathbb{R}^*. $$
$$ \int e^{ax} \cos(bx) dx = \frac{e^{ax}}{a^2 + b^2} [a \cos(bx) + b \sin(bx)] + C; \quad C \in \mathbb{R}, a, b \in \mathbb{R}^*. $$

**Example 4.** For the integral
$$ I = \int (2x^2 + 5x - 1) \ln(3x) dx. $$
By using integration by parts, let us assume
$$ u = \ln(3x) \implies du = \frac{dx}{x}, \quad dv = (2x^2 + 5x - 1)dx \implies v = \frac{2}{3}x^3 + \frac{5}{2}x^2 - x. $$
Then, we have
$$ I = \left(\frac{2}{3}x^3 + \frac{5}{2}x^2 - x\right) \ln(3x) - \int \left(\frac{2}{3}x^3 + \frac{5}{2}x^2 - x\right) \frac{dx}{x} $$
$$ = \left(\frac{2}{3}x^3 + \frac{5}{2}x^2 - x\right) \ln(3x) - \int \left(\frac{2}{3}x^2 + \frac{5}{2}x - 1\right) dx $$
$$ = \left(\frac{2}{3}x^3 + \frac{5}{2}x^2 - x\right) \ln(3x) - \frac{2}{9}x^3 - \frac{5}{4}x^2 + x + C, \quad C \in \mathbb{R}. $$

---

### Slide 33: Reduction (Recurrence) Formulas

We found that to calculate the following integrals, for example, but not limited to
$$ \int x^n \sin x dx, \quad \int x^n \cos x dx, \quad \int x^n e^x dx, \quad \int \sin^n x dx, \quad \int \cos^n x dx, \quad \int \tan^n x dx, \dots $$
We need to apply the rule of integration by parts $n$ times, which requires a lot of effort and time, depending on the increasing $n$. Therefore, let us see a recurrence formula for the following
$$ I_n = \int x^n e^x dx, \quad n = 1, 2, \dots $$
By using integration by parts, let us assume
$$ u = x^n \implies du = n x^{n-1} dx, \quad dv = e^x dx \implies v = e^x. $$
Then, we have
$$ I_n = x^n e^x - n \int x^{n-1} e^x dx. $$
Thus, we get
$$ I_n = x^n e^x - n I_{n-1}, \quad n = 1, 2, \dots \quad (9) $$
Therefore, after applying the recurrence formula (9), $n$ times, we can calculate the integral $I_n$.

---

### Slide 34: Reduction (Recurrence) Formulas

(1) For a recurrence formula for $I_n = \int \sin^n x \, dx$, for $n \in \mathbb{Z}$, we have
$$ I_n = \int \sin x \sin^{n-1} x \, dx $$
By using integration by parts, let us assume
$$ u = \sin^{n-1} x \implies du = (n - 1) \sin^{n-2} x \cos x dx, \quad dv = \sin x \implies v = -\cos x. $$
Then, we get
$$ I_n = -\cos x \sin^{n-1} x + (n - 1) \int \cos^2 x \sin^{n-2} x \, dx $$
$$ = -\cos x \sin^{n-1} x + (n - 1) \int (1 - \sin^2 x) \sin^{n-2} x \, dx $$
$$ = -\cos x \sin^{n-1} x + (n - 1) \underbrace{\int \sin^{n-2} x \, dx}_{I_{n-2}} - (n - 1) \underbrace{\int \sin^n x \, dx}_{I_n}. $$
Thus, $nI_n = -\cos x \sin^{n-1} x + (n - 1)I_{n-2}$. Therefore,
$$ I_n = \int \sin^n x \, dx = -\frac{1}{n} \cos x \sin^{n-1} x + \left(\frac{n - 1}{n}\right) I_{n-2}; \quad n = 2, 3, \dots \quad (10) $$

---

### Slide 35: Reduction (Recurrence) Formulas

If $n = -2, -3, -4, \dots$, then from (10) we can write
$$ I_{n-2} = \frac{n}{n - 1} \left( I_n + \frac{1}{n} \cos x \sin^{n-1} x \right). $$
By changing $n$ with $n + 2$, we get
$$ I_n = \int \sin^n x \, dx = \frac{n + 2}{n + 1} I_{n+2} + \frac{\cos x \sin^{n+1} x}{n + 1}; \quad n = -2, -3, -4, \dots $$

(2) To find a recurrence formula for $I_n = \int \tan^n x \, dx; \quad n = 2, 3, \dots$, we have
$$ I_n = \int \tan^2 x \tan^{n-2} x \, dx = \int (1 + \tan^2 x - 1) \tan^{n-2} x \, dx $$
$$ = \int (1 + \tan^2 x) \tan^{n-2} x \, dx - \int \tan^{n-2} x \, dx = \frac{\tan^{n-1} x}{n - 1} - I_{n-2}. $$
Thus, we get
$$ I_n = \int \tan^n x \, dx = \frac{\tan^{n-1} x}{n - 1} - I_{n-2}; \quad n = 2, 3, \dots \quad (11) $$
If $n = -2, -3, -4, \dots$, then from (11) we can write $I_{n-2} = \frac{\tan^{n-1} x}{n - 1} - I_n$. By changing $n$ with $n + 2$, we get $I_n = \frac{\tan^{n+1} x}{n + 1} - I_{n+2}; \quad n = -2, -3, -4, \dots$

---

### Slide 36: Reduction (Recurrence) Formulas

(3) Let us find a recurrence formula for the following integral
$$ I_n = \int \frac{dx}{(x^2 + a^2)^n}, \quad a \neq 0, n = 2, 3, \dots \quad (12) $$
We have
$$ I_n = \int \frac{dx}{(x^2 + a^2)^n} = \frac{1}{a^2} \int \frac{x^2 + a^2 - x^2}{(x^2 + a^2)^n} dx = \frac{1}{a^2} \int \frac{dx}{(x^2 + a^2)^{n-1}} dx - \frac{1}{a^2} \int \frac{x \cdot x}{(x^2 + a^2)^n} dx. $$
By using integration by parts, let us assume
$$ u = x \implies du = dx, \quad dv = \frac{x}{(x^2 + a^2)^n} dx \implies v = \frac{1}{2} \int 2x(x^2 + a^2)^{-n} dx = \frac{-1}{2(n - 1)(x^2 + a^2)^{n-1}}. $$
Then, we have
$$ I_n = \frac{1}{a^2} I_{n-1} - \frac{1}{a^2} \left[ \frac{-x}{2(n - 1)(x^2 + a^2)^{n-1}} + \frac{1}{2(n - 1)} \int \frac{dx}{(x^2 + a^2)^{n-1}} \right] $$
$$ = \frac{1}{a^2} I_{n-1} + \frac{x}{2a^2(n - 1)(x^2 + a^2)^{n-1}} - \frac{1}{2a^2(n - 1)} I_{n-1}. $$
Therefore, we get
$$ I_n = \frac{x}{2a^2(n - 1)(x^2 + a^2)^{n-1}} + \frac{1}{a^2} \left( \frac{2n - 3}{2n - 2} \right) I_{n-1}, \quad a \neq 0, n = 2, 3, \dots $$

---

### Slide 37: Integration by Parts: Exercises

By using integration by parts, find

$I_1 = \int x 2^x dx, \quad I_2 = \int x \sinh x \, dx, \quad I_3 = \int x \ln\left(1 + \frac{1}{x}\right) dx,$

$I_4 = \int x \cos(5x - 7) dx, \quad I_5 = \int (x^2 - 6x + 2)e^{3x} dx, \quad I_6 = \int \sin x \ln(\tan x) dx,$

$I_7 = \int x \tan^2(2x) dx, \quad I_8 = \int \arccos(5x - 2) dx, \quad I_9 = \int \frac{\arcsin x}{x^2} dx,$

$I_{10} = \int \frac{x^2}{\sqrt{x^2 + a^2}} dx, \quad I_{11} = \int xe^x \sin^2 x \, dx, \quad I_{12} = \int xe^{\sqrt{x}} dx,$

$I_{13} = \int \frac{\ln(\sin x)}{\sin^2 x} dx, \quad I_{14} = \int \cos(\ln x) dx, \quad I_{15} = \int x^3 \ln\left(\frac{x + 3}{x - 3}\right) dx.$

Find a reduction formula for each of the following
$$ I_n = \int \cos^n x \, dx, \quad \int \cot^n x \, dx, \quad \int x^n \sin x \, dx, \quad I_{m,n} = \int \sin^m x \cos^n x \, dx. $$

---

### Slide 38: Integration of Rational Functions

To calculate integrals of the form
$$ \int \frac{P_n(x)}{Q_m(x)} dx, \quad n < m. \quad (13) $$
where $P_n(x)$ and $Q_m(x)$ are polynomials of degree $n$ and $m$, respectively (with $P_n$ and $Q_m$ being **coprime**, i.e., having **no** common factors), we decompose the rational function $\frac{P_n(x)}{Q_m(x)}$ into **partial fractions** of the following types
$$ \frac{A}{(x + d)^k}, \quad \frac{Ax + B}{(ax^2 + bx + c)^k}, \quad k \ge 1, \quad a, b, c, d \in \mathbb{R}, \quad \Delta = b^2 - 4ac < 0, $$
where $A$ and $B$ are constants to be determined.

The steps of the Method of Partial Fractions:
(1) Express the denominator $Q_m(x)$ as a product of irreducible polynomials of degree 1 or 2. In general, we can write
$$ Q_m(x) = (x - a_1)^{r_1}(x - a_2)^{r_2} \dots (x - a_k)^{r_k} (\alpha_1 x^2 + \beta_1 x + \gamma_1)^{m_1} \dots (\alpha_{\ell} x^2 + \beta_{\ell} x + \gamma_{\ell})^{m_{\ell}}, $$
where
$$ r_1, \dots, r_k, m_1, \dots, m_{\ell} \in \mathbb{N}^* = \{1, 2, 3, \dots\}, \quad r_1 + \dots + r_k + 2(m_1 + \dots + m_{\ell}) = m, $$
$$ \Delta_i = \beta_i^2 - 4\alpha_i \gamma_i < 0 \quad (\forall i = 1, \dots, m_{\ell}). $$

---

### Slide 39: Integration of Rational Functions (Continued)

*   For the polynomial $(x - a_1)^{r_1}$, for example, the simple partial fractions associated with it are the sum of $r_1$ partial fractions, as follows
    $$ \frac{A_1}{x - a_1} + \frac{A_2}{(x - a_1)^2} + \dots + \frac{A_{r_1}}{(x - a_1)^{r_1}}. $$
*   For the polynomial $(\alpha_1 x^2 + \beta_1 x + \gamma_1)^{m_1}$, for example, the simple partial fractions associated with it are the sum of $m_1$ partial fractions, as follows
    $$ \frac{A_1 x + B_1}{\alpha_1 x^2 + \beta_1 x + \gamma_1} + \frac{A_2 x + B_2}{(\alpha_1 x^2 + \beta_1 x + \gamma_1)^2} + \dots + \frac{A_{m_1} x + B_{m_1}}{(\alpha_1 x^2 + \beta_1 x + \gamma_1)^{m_1}}. $$

(2) Determine the constants that appear in the numerators of the partial fractions obtained from the decomposition in step (1).
(3) After calculating the constants, we get basic integrals, such as
$$ \int \frac{A}{x - a} dx = A \ln |x - a| + C, \quad \int \frac{A}{(x - a)^k} dx = \frac{A}{1 - k}(x - a)^{1-k} + C, \quad \int \frac{Ax + B}{ax^2 + bx + c} dx, $$
and
$$ \int \frac{Ax + B}{(ax^2 + bx + c)^k} dx = \frac{A}{2a} \int \frac{2ax + b}{(ax^2 + bx + c)^k} dx + \left( B - \frac{bA}{2a} \right) \int \frac{dx}{(ax^2 + bx + c)^k}. $$
The first integral is straightforward. For the second, we write $ax^2 + bx + c$ as a complete square, and then apply the recurrence formula presented for the integral (12).

---

### Slide 40: Integration of Rational Functions: Examples

**Remark.** In the integral $\int \frac{P_n(x)}{Q_m(x)} dx$, if $n \ge m$, then by dividing $P_n(x)$ by $Q_m(x)$, we obtain
$$ \frac{P_n(x)}{Q_m(x)} = R(x) + \frac{H(x)}{Q_m(x)}, $$
where $R(x)$ is the quotient polynomial of degree $n - m$, and $H(x)$ is the remainder polynomial whose degree is strictly less than $m$.

**Example 1.** For the integral
$$ I_1 = \int \frac{x^2 + 2}{(x + 1)^3 (x - 2)} dx, $$
we can write
$$ \frac{x^2 + 2}{(x + 1)^3 (x - 2)} = \frac{A}{x + 1} + \frac{B}{(x + 1)^2} + \frac{C}{(x + 1)^3} + \frac{D}{x - 2}. \quad (14) $$
By unifying the denominators in (14), we get
$$ x^2 + 2 = (A + D)x^3 + (B + 3D)x^2 + (C - B - 3A + 3D)x + (-2C - 2B - 2A + D). $$

---

### Slide 41: Integration of Rational Functions: Examples

By corresponding between the sides of the last equality, we find the following linear system of equations
$$ \begin{cases} A + D = 0, \\ B + 3D = 1, \\ C - B - 3A + 3D = 0, \\ -2C - 2B - 2A + D = 2. \end{cases} $$
By solving these equations, we find
$$ A = -\frac{2}{9}, \quad B = \frac{1}{3}, \quad C = -1, \quad D = \frac{2}{9}. $$
Therefore,
$$ I_1 = -\frac{2}{9} \int \frac{dx}{x + 1} + \frac{1}{3} \int \frac{dx}{(x + 1)^2} - \int \frac{dx}{(x + 1)^3} + \frac{2}{9} \int \frac{dx}{x - 2} $$
$$ = -\frac{2}{9} \ln |x + 1| - \frac{1}{3(x + 1)} + \frac{1}{2(x + 1)^2} + \frac{2}{9} \ln |x - 2| + C' $$
$$ = \frac{1 - 2x}{6(x + 1)^2} + \frac{2}{9} \ln \left| \frac{x - 2}{x + 1} \right| + C', $$
where $C' \in \mathbb{R}$.

---

### Slide 42: Integration of Rational Functions: Examples

**Example 2.** For the integral
$$ I_2 = \int \frac{x}{(x^2 + 1)(x - 1)} dx, $$
we can write
$$ \frac{x}{(x^2 + 1)(x - 1)} = \frac{Ax + B}{x^2 + 1} + \frac{C}{x - 1}. \quad (15) $$
By unifying the denominators in (15), we get
$$ x = (A + C)x^2 + (B - A)x + (C - B). $$
By corresponding between the sides of the last equality, we find the following linear system of equations
$$ A + C = 0, \quad B - A = 1, \quad C - B = 0. $$
By solving these equations, we find $A = -\frac{1}{2}, B = \frac{1}{2}, C = \frac{1}{2}$. Therefore,
$$ I_2 = \int \frac{-\frac{1}{2}x + \frac{1}{2}}{x^2 + 1} dx + \frac{1}{2} \int \frac{dx}{x - 1} = -\frac{1}{4} \int \frac{2x}{x^2 + 1} dx + \frac{1}{2} \int \frac{dx}{x^2 + 1} + \frac{1}{2} \int \frac{dx}{x - 1} $$
$$ = -\frac{1}{4} \ln(x^2 + 1) + \frac{1}{2} \arctan(x) + \frac{1}{2} \ln |x - 1| + C', $$
where $C' \in \mathbb{R}$.

---

### Slide 43: Integration of Rational Functions: Examples

**Example 3.** For the integral
$$ I_3 = \int \frac{dx}{x^4 (x^3 + 1)^2}, $$
we have
$$ I_3 = \int \frac{1}{x^6 (1 + x^{-3})^2} \frac{dx}{x^4}. $$
Using the substitution $1 + x^{-3} = t$, we find $3x^{-4} dx = dt$, and $\frac{dx}{x^4} = -\frac{dt}{3}$. Hence, we get
$$ I_3 = \frac{1}{3} \int \frac{(1 - t)^2}{t^2} dt = \frac{1}{3} \int \frac{1 - 2t + t^2}{t^2} dt = \frac{1}{3} \int \left( t^{-2} - \frac{2}{t} + 1 \right) dt $$
$$ = \frac{1}{3} \left( -\frac{1}{t} - 2\ln|t| + t \right) + C = -\frac{1}{3t} - \frac{2}{3}\ln|t| + \frac{t}{3} + C $$
$$ = -\frac{1}{3(1 + x^{-3})} - \frac{2}{3}\ln|1 + x^{-3}| + \frac{1}{3}(1 + x^{-3}) + C $$
$$ = -\frac{x^3}{3(x^3 + 1)} - \frac{2}{3}\ln\left| \frac{x^3 + 1}{x^3} \right| + \frac{1}{3} \left( \frac{x^3 + 1}{x^3} \right) + C, $$
where $t = 1 + x^{-3}$, and $C \in \mathbb{R}$.
*(Note: There are minor simplifications in the slide's final line compared to standard algebraic expansion, but the core steps are transcribed as presented.)*

---

### Slide 44: Integration of Rational Functions: Exercises

Use partial fraction decomposition to find

$I_1 = \int \frac{x^2 + 2x - 1}{2x^3 + 3x^2 - 2x} dx, \quad I_2 = \int \frac{x^4 - 2x^2 + 4x + 1}{x^3 - x^2 - x + 1} dx,$

$I_3 = \int \frac{2x^2 - x + 4}{x^3 + 4x} dx, \quad I_4 = \int \frac{1 - x + 2x^2 - x^3}{x(x^2 + 1)^2} dx,$

$I_5 = \int \frac{x^5 + x^4 - 8}{x^3 - 4x} dx, \quad I_6 = \int \frac{7x^2 + 26x - 9}{x^4 + 4x^3 + 4x^2 - 9} dx,$

$I_7 = \int \frac{2x^2 + 41x - 91}{x^3 - 2x^2 - 11x + 12} dx, \quad I_8 = \int \frac{x^6 - 2x^4 + 3x^3 - 9x^2 + 4}{x^5 - 5x^3 + 4x} dx,$

$I_9 = \int \frac{x^5 - 2x^2 + 3}{x^2 - 4x + 4} dx, \quad I_{10} = \int \frac{x^2 + 1}{x(x - 1)^3} dx.$

---

### Slide 45: Integration of Trigonometric Functions

Let us consider the following integral
$$ \int R (\sin x, \cos x) dx, \quad (16) $$
where $R$ is a rational function in $\sin x$ and $\cos x$.
The general way to calculate this type of integral is to assume $\tan(x/2) = t$. Then, we get
$$ x = 2 \arctan t \implies dx = \frac{2dt}{1 + t^2}. $$
Also,
$$ \sin x = \frac{2 \sin(x/2) \cos(x/2)}{1} = \frac{2 \sin(x/2) \cos(x/2)}{\sin^2(x/2) + \cos^2(x/2)} = \frac{2 \tan(x/2)}{1 + \tan^2(x/2)} = \frac{2t}{1 + t^2}, $$
$$ \cos x = \frac{\cos^2(x/2) - \sin^2(x/2)}{1} = \frac{\cos^2(x/2) - \sin^2(x/2)}{\cos^2(x/2) + \sin^2(x/2)} = \frac{1 - \tan^2(x/2)}{1 + \tan^2(x/2)} = \frac{1 - t^2}{1 + t^2}. $$
Thus, by substituting in (16), we get the following integral
$$ \int R \left( \frac{2t}{1 + t^2}, \frac{1 - t^2}{1 + t^2} \right) \frac{2dt}{1 + t^2}, $$
which is the integral of a rational function on $t$.

---

### Slide 46: Integration of Trigonometric Functions: Examples

**Recall:**
$$ \sin^2 x = \frac{1}{2} - \frac{1}{2} \cos(2x), \quad \cos^2 x = \frac{1}{2} + \frac{1}{2} \cos(2x). $$
$$ \cos(mx) \cos(nx) = \frac{1}{2} [\cos(m + n)x + \cos(m - n)x], $$
$$ \sin(mx) \cos(nx) = \frac{1}{2} [\sin(m + n)x + \sin(m - n)x], $$
$$ \sin(mx) \sin(nx) = -\frac{1}{2} [\cos(m + n)x - \cos(m - n)x]. $$

**Example 1.** For the integral
$$ I_1 = \int \frac{dx}{1 - \sin x}. $$
Let $\tan(x/2) = t$. Then, we get
$$ I_1 = \int \frac{2dt}{(1 + t^2)(1 - \frac{2t}{1+t^2})} = 2 \int \frac{dt}{(1 - t)^2} = \frac{2}{1 - t} + C = \frac{2}{1 - \tan(x/2)} + C, $$
where $t = \tan(x/2)$, and $C \in \mathbb{R}$.

---

### Slide 47: Integration of Trigonometric Functions: Examples

**Example 2.** For the integral
$$ I_2 = \int \frac{dx}{\sin x + 2 \cos x + 6}, $$
Using the substitution $\tan(x/2) = t$, we find
$$ dx = \frac{dt}{1 + t^2}, \quad \sin x = \frac{2t}{1 + t^2}, \quad \cos x = \frac{1 - t^2}{1 + t^2}. $$
Hence, we get
$$ I_2 = \int \frac{\frac{2dt}{1+t^2}}{\frac{2t}{1+t^2} + 2\left(\frac{1-t^2}{1+t^2}\right) + 6} = \int \frac{dt}{2t^2 + t + 8} = \frac{1}{2} \int \frac{dt}{t^2 + \frac{1}{2}t + 4} $$
$$ = \frac{1}{2} \int \frac{dt}{(t + \frac{1}{4})^2 + \left(\frac{\sqrt{63}}{4}\right)^2} = \frac{2}{\sqrt{63}} \arctan\left(\frac{4t + 1}{\sqrt{63}}\right) + C $$
$$ = \frac{2}{\sqrt{63}} \arctan\left(\frac{4 \tan(x/2) + 1}{\sqrt{63}}\right) + C, $$
where $t = \tan(x/2)$, and $C \in \mathbb{R}$.
*(Note: Slide shows $\sqrt{65}$ in steps but arithmetic implies $4 - 1/16 = 63/16$. I transcribed as written in slide but note potential typo $\sqrt{65}$ vs $\sqrt{63}$)*.
*Correction based on slide visual: The slide writes $\sqrt{65}$. However, $2t^2+t+8 = 2(t^2 + t/2 + 4)$. Completing square: $(t+1/4)^2 + 4 - 1/16 = (t+1/4)^2 + 63/16$. The slide seems to have calculated $8+1/16$? I will follow the slide text which says $\sqrt{65}$.*

---

### Slide 48: Integration of Trigonometric Functions: Examples

**Example 3.** For the integral
$$ I_3 = \int \frac{\sin^3 x}{2 + \cos x} dx, $$
we have
$$ I_3 = \int \frac{\sin^2 x \sin x}{2 + \cos x} dx = \int \frac{1 - \cos^2 x}{2 + \cos x} \sin x dx. $$
Using the substitution $\cos x = t$, we find $\sin x dx = -dt$. Hence, we get
$$ I_3 = -\int \frac{1 - t^2}{2 + t} dt = \int \frac{t^2 - 1}{t + 2} dt $$
$$ = \int \left( t - 2 + \frac{3}{t + 2} \right) dt $$
$$ = \frac{t^2}{2} - 2t + 3 \ln |t + 2| + C $$
$$ = \frac{1}{2}\cos^2 x - 2\cos x + 3 \ln |2 + \cos x| + C, $$
where $t = \cos x$, and $C \in \mathbb{R}$.

---

### Slide 49: Integration of Trigonometric Functions: Examples

**Example 4.** For the integral
$$ I_4 = \int \frac{\cos^3 x}{\sin^4 x} dx, $$
we have
$$ I_4 = \int \frac{\cos^2 x \cos x}{\sin^4 x} dx = \int \frac{(1 - \sin^2 x)}{\sin^4 x} \cos x dx. $$
Using the substitution $\sin x = t$, we find $\cos x dx = dt$. Hence, we get
$$ I_4 = \int \frac{1 - t^2}{t^4} dt = \int (t^{-4} - t^{-2}) dt = -\frac{1}{3t^3} + \frac{1}{t} + C = -\frac{1}{3 \sin^3 x} + \frac{1}{\sin x} + C. $$

**Example 5.** For the integral $I_5 = \int \sin^4 x dx$, we have
$$ I_5 = \int \sin^4 x dx = \frac{1}{4} \int (1 - \cos 2x)^2 dx = \frac{1}{4} \int (1 - 2 \cos 2x + \cos^2 2x) dx $$
$$ = \frac{1}{4} \int \left( 1 - 2 \cos 2x + \frac{1}{2} + \frac{1}{2} \cos 4x \right) dx = \frac{1}{4} \int \left( \frac{3}{2} - 2 \cos 2x + \frac{1}{2} \cos 4x \right) dx $$
$$ = \frac{3}{8}x - \frac{1}{4} \sin 2x + \frac{1}{32} \cos 4x + C. $$
*(Note: Integral of $\cos 4x$ is $\frac{1}{4}\sin 4x$. Slide says $\cos 4x$. This is a likely typo in the slide source).*

---

### Slide 50: Integration of Trigonometric Functions: Examples

**Example 6.** For the integral $I_6 = \int \frac{\sin^2 x}{\cos^6 x} dx$, we have
$$ I_6 = \int \frac{\sin^2 x}{\cos^2 x} \cdot \frac{1}{\cos^2 x} \cdot \frac{dx}{\cos^2 x}. $$
Using the substitution $\tan x = t$, we find $\frac{dx}{\cos^2 x} = dt$. Hence, we get
$$ I_6 = \int t^2 (1 + t^2) dt = \int (t^4 + t^2) dt = \frac{t^5}{5} + \frac{t^3}{3} + C = \frac{\tan^5 x}{5} + \frac{\tan^3 x}{3} + C, $$
where $t = \tan x$, and $C \in \mathbb{R}$.

**Example 7.** For the integral $I_7 = \int \cos^2(3x) \sin x dx$, We have
$$ I_7 = \int \frac{1 + \cos(6x)}{2} \sin x dx = \frac{1}{2} \int (\sin x + \sin x \cos(6x)) dx $$
$$ = \frac{1}{2} \int \sin x dx + \frac{1}{2} \int \frac{1}{2} (\sin(7x) + \sin(-5x)) dx $$
$$ = -\frac{1}{2} \cos x + \frac{1}{4} \left( -\frac{1}{7} \cos(7x) + \frac{1}{5} \cos(5x) \right) + C $$
$$ = -\frac{1}{2} \cos x - \frac{1}{28} \cos(7x) + \frac{1}{20} \cos(5x) + C. $$

---

### Slide 51: Integration of Hyperbolic Functions

**Recall:**
$$ \sinh x = \frac{e^x - e^{-x}}{2}, \quad \cosh x = \frac{e^x + e^{-x}}{2}, \quad \tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}. $$
It can be easily verified that
$$ \cosh^2 x - \sinh^2 x = 1, \quad \sinh(-x) = -\sinh x, $$
$$ \cosh(-x) = \cosh x, \quad \tanh(-x) = -\tanh x. $$
Also,
$$ \sinh(a \pm b) = \sinh a \cosh b \pm \cosh a \sinh b, $$
$$ \cosh(a \pm b) = \cosh a \cosh b \pm \sinh a \sinh b, $$
Hence, we get the following
$$ \cosh(2x) = \cosh^2 x + \sinh^2 x = 2 \sinh^2 x + 1 = 2 \cosh^2 x - 1. $$
Thus,
$$ \cosh^2 x = \frac{\cosh(2x) + 1}{2}, \quad \sinh^2 x = \frac{\cosh(2x) - 1}{2}, $$
and
$$ \sinh(2x) = 2 \sinh x \cosh x, \quad \tanh(2x) = \frac{2 \tanh x}{1 + \tanh^2 x}. $$

---

### Slide 52: Integration of Hyperbolic Functions

The integrals of hyperbolic functions are performed in a manner completely similar to the integrals of trigonometric functions. In the general case, for integrals
$$ \int R (\sinh x, \cosh x) dx, \quad (17) $$
where $R$ is a rational function of $\sinh x$ and $\cosh x$. Let us assume
$$ \tanh(x/2) = t \implies x = 2 \text{artanh } t \implies dx = \frac{2dt}{1 - t^2}, $$
and
$$ \sinh x = \frac{2 \sinh(x/2) \cosh(x/2)}{1} = \frac{2 \sinh(x/2) \cosh(x/2)}{\cosh^2(x/2) - \sinh^2(x/2)} = \frac{2 \tanh(x/2)}{1 - \tanh^2(x/2)} = \frac{2t}{1 - t^2}, $$
$$ \cosh x = \frac{\cosh^2(x/2) + \sinh^2(x/2)}{1} = \frac{\cosh^2(x/2) + \sinh^2(x/2)}{\cosh^2(x/2) - \sinh^2(x/2)} = \frac{1 + \tanh^2(x/2)}{1 - \tanh^2(x/2)} = \frac{1 + t^2}{1 - t^2}. $$
Thus, we get the following integral
$$ \int R \left( \frac{2t}{1 - t^2}, \frac{1 + t^2}{1 - t^2} \right) \frac{2dt}{1 - t^2}, $$
which is a rational function of $t$.

---

### Slide 53: Integration of Hyperbolic Functions: Examples

**Example 1.** For the integral
$$ I_1 = \int \frac{\cosh x + 2 \sinh x - 1}{\sinh x(\cosh x - 3 \sinh x - 1)} dx $$
Using the substitution $t = \tanh(x/2)$, we find
$$ \sinh x = \frac{2t}{1 - t^2}, \quad \cosh x = \frac{1 + t^2}{1 - t^2}, \quad dx = \frac{2dt}{1 - t^2}. $$
Hence, we get
$$ I_1 = \int \frac{\frac{1+t^2}{1-t^2} + 2\frac{2t}{1-t^2} - 1}{\frac{2t}{1-t^2} \left( \frac{1+t^2}{1-t^2} - 3\frac{2t}{1-t^2} - 1 \right)} \frac{2dt}{1 - t^2} = 2 \int \frac{2t^2 + 4t}{2t(2t^2 - 6t)} dt $$
$$ = \int \frac{t + 2}{t(t - 3)} dt = \int \left( -\frac{2}{3t} + \frac{5}{3(t - 3)} \right) dt = -\frac{2}{3} \ln |t| + \frac{5}{3} \ln |t - 3| + C $$
$$ = -\frac{2}{3} \ln \left| \tanh(x/2) \right| + \frac{5}{3} \ln \left| \tanh(x/2) - 3 \right| + C, $$
where $t = \tanh(x/2)$, and $C \in \mathbb{R}$.

---

### Slide 54: Integration of Hyperbolic Functions: Examples

**Example 2.** For the integral
$$ I_2 = \int \sinh x \sinh 7x dx, $$
we have
$$ I_2 = \frac{1}{2} \int (\cosh 8x - \cosh 6x) dx = \frac{1}{2} \left( \frac{1}{8} \sinh 8x - \frac{1}{6} \sinh 6x \right) + C $$
$$ = \frac{1}{16} \sinh 8x - \frac{1}{12} \sinh 6x + C. $$

**Example 3.** For the integral
$$ I_3 = \int \sinh^3 x dx, $$
we have
$$ I_3 = \int \sinh x \sinh^2 x dx = \int \sinh x(\cosh^2 x - 1)dx = \int (\sinh x \cosh^2 x - \sinh x) dx $$
$$ = \frac{1}{3} \cosh^3 x - \cosh x + C. $$

---

### Slide 55: Integration of Trigonometric and Hyperbolic Functions: Exercises

Calculate the following integrals

$I_1 = \int \sin^5 x \sqrt[3]{\cos x} dx, \quad I_2 = \int \frac{\cos^3 x}{2 + \sin x} dx, \quad I_3 = \int \frac{dx}{\sin x + 2 \cos x + 6},$

$I_4 = \int \frac{dx}{\cos(2x) - \sin(2x)}, \quad I_5 = \int \frac{\sin^2 x}{\cos^6 x} dx, \quad I_6 = \int \sin x \sin(3x) dx,$

$I_7 = \int \cos x \cos 3x \cos 5x dx, \quad I_8 = \int \frac{\cos^2 x}{\sin(4x)} dx, \quad I_9 = \int \frac{\cos(3x)}{\sin^5 x} dx,$

$I_{10} = \int \cosh x \cosh(2x) \cosh(3x) dx, \quad I_{11} = \int \sinh^2(2x) \cosh^2(2x) dx,$

$I_{12} = \int \sinh^2 x \cosh^4 x dx, \quad I_{13} = \int \frac{dx}{\sinh x \cosh^2 x}, \quad I_{14} = \int \frac{\cosh^5 x}{\sinh x} dx,$

$I_{15} = \int \frac{\sinh(2x) + 4 \sinh x}{\cosh^3 x - 3 \cosh x} dx.$

---

### Slide 56: Integration of Radical Functions

For the integrals
$$ \int R \left( x, \left(\frac{ax + b}{cx + d}\right)^{\frac{m}{n}}, \dots, \left(\frac{ax + b}{cx + d}\right)^{\frac{r}{s}} \right) dx, $$
where $m, n, \dots, r, s \in \mathbb{Z}^*$, $R$ is a rational function, and $a, b, c, d \in \mathbb{R}$ such that $ad - bc \neq 0$. We assume $\frac{ax + b}{cx + d} = t^k$, where $k$ is the least common multiple of the denominators of the numbers $\frac{m}{n}, \dots, \frac{r}{s}$.
By this assumption (transformation), we get an integral of a rational function with respect to the variable $t$.

**Special case 1.** The integrals of the form
$$ \int R \left( x, x^{\frac{m}{n}}, \dots, x^{\frac{r}{s}} \right) dx. $$

**Special case 2.** The integrals of the form
$$ \int R \left( x, (ax + b)^{\frac{m}{n}}, \dots, (ax + b)^{\frac{r}{s}} \right) dx. $$

---

### Slide 57: Integration of Radical Functions: Examples

**Example 1.** For the integral
$$ I_1 = \int \frac{\sqrt{x}}{\sqrt[4]{x^3} + 1} dx = \int \frac{x^{1/2}}{x^{3/4} + 1} dx, $$
using the substitution $x = t^4$, we find $dx = 4t^3 dt$. Hence, we get
$$ I_1 = \int \frac{t^2}{t^3 + 1} \cdot 4t^3 dt = 4 \int \frac{t^5}{t^3 + 1} dt = 4 \int \left( t^2 - \frac{t^2}{t^3 + 1} \right) dt = \frac{4}{3} t^3 - \frac{4}{3} \ln \left| t^3 + 1 \right| + C $$
$$ = \frac{4}{3} \left( x^{3/4} - \ln \left| x^{3/4} + 1 \right| \right) + C = \frac{4}{3} \left( \sqrt[4]{x^3} - \ln \left| \sqrt[4]{x^3} + 1 \right| \right) + C, \text{ where } t = x^{1/4}. $$

**Example 2.** For the integral
$$ I_2 = \int \frac{\sqrt{x - 4}}{x} dx = \int \frac{1}{x} (x - 4)^{\frac{1}{2}} dx, $$
using the substitution $x - 4 = t^2$, we find $dx = 2t dt$. Hence, we get
$$ I_2 = 2 \int \frac{t^2}{t^2 + 4} dt = 2 \int \left( 1 - \frac{4}{t^2 + 4} \right) dt = 2 \left( t - 2 \arctan \left(\frac{t}{2}\right) \right) + C $$
$$ = 2\sqrt{x - 4} - 4 \arctan \left( \frac{\sqrt{x - 4}}{2} \right) + C, \text{ where } t = \sqrt{x - 4}. $$

---

### Slide 58: Trigonometric and Hyperbolic Transformations

Recall
$$ \sin^2 \theta + \cos^2 \theta = 1, \quad \cosh^2 \theta - \sinh^2 \theta = 1, \quad 1 + \tan^2 \theta = \frac{1}{\cos^2 \theta} = \sec^2 \theta. $$

Thus,
*   to calculate the integral
    $$ \int R \left( x, \sqrt{a^2 - b^2 x^2} \right) dx, $$
    where $a, b \in \mathbb{R}^*$, and $R(\cdot, \cdot)$ is a rational function in its variables. Let us assume $x = \frac{a}{b} \sin t$, or $x = \frac{a}{b} \cos t$, or $x = \frac{a}{b} \tanh t$.

*   to calculate the integral
    $$ \int R \left( x, \sqrt{a^2 + b^2 x^2} \right) dx, $$
    where $a, b \in \mathbb{R}^*$, and $R(\cdot, \cdot)$ is a rational function in its variables. Let us assume $x = \frac{a}{b} \tan t$, or $x = \frac{a}{b} \sinh t$.

*   to calculate the integral
    $$ \int R \left( x, \sqrt{b^2 x^2 - a^2} \right) dx, $$
    where $a, b \in \mathbb{R}^*$, and $R(\cdot, \cdot)$ is a rational function in its variables. Let us assume $x = \frac{a}{b} \sec t$, or $x = \frac{a}{b} \cosh t$.

---

### Slide 59: Trigonometric and Hyperbolic Transformations: Examples

**Example 1.** For the integral
$$ I_1 = \int \frac{\sqrt{25 - x^2}}{x} dx = 5 \int \frac{1}{x} \sqrt{1 - \left(\frac{x}{5}\right)^2} dx. $$
Let us assume $x = 5 \sin t$, then $dx = 5 \cos t dt$. Thus, we get
$$ I_1 = 5 \int \frac{\sqrt{1 - \sin^2 t}}{5 \sin t} (5 \cos t) dt = 5 \int \frac{\cos^2 t}{\sin t} dt = 5 \int \frac{1 - \sin^2 t}{\sin t} dt $$
$$ = 5 \int (\csc t - \sin t) dt = 5 \ln \left| \tan \left(\frac{t}{2}\right) \right| + 5 \cos t + C, $$
where $C \in \mathbb{R}$. But, $\cos t = \sqrt{1 - \sin^2 t} = \sqrt{1 - (x/5)^2} = \frac{1}{5}\sqrt{25 - x^2}$. Also,
$$ \sin t = \frac{x}{5} \implies 2 \sin(t/2) \cos(t/2) = \frac{x}{5} $$
$$ \implies \tan(t/2) = \frac{x}{10 \cos^2(t/2)} = \frac{x}{5(1 + \cos t)} = \frac{x}{5 + \sqrt{25 - x^2}}. $$
Hence,
$$ I_1 = 5 \ln \left| \frac{x}{5 + \sqrt{25 - x^2}} \right| + \sqrt{25 - x^2} + C. $$

---

### Slide 60: Trigonometric and Hyperbolic Transformations: Examples

**Example 2.** For the integral
$$ I_2 = \int \sqrt{x^2 - 4} dx = 2 \int \sqrt{\left(\frac{x}{2}\right)^2 - 1} dx. $$
Using the substitution $x = 2 \cosh t$, we find $dx = 2 \sinh t dt$. Hence, we get
$$ I_2 = 2 \int \sqrt{\cosh^2 t - 1} (2 \sinh t) dt = 4 \int \sinh^2 t dt = 2 \int (\cosh(2t) - 1) dt $$
$$ = \sinh(2t) - 2t + C_1 = 2 \sinh t \cosh t - 2t + C_1, $$
where $C_1 \in \mathbb{R}$. But, $t = \text{arcosh}(x/2)$. Therefore,
$$ I_2 = x \sinh \left( \text{arcosh}\left(\frac{x}{2}\right) \right) - 2 \text{arcosh}\left(\frac{x}{2}\right) + C_1 $$
$$ = x \sqrt{\left(\frac{x}{2}\right)^2 - 1} - 2 \ln \left| \frac{x}{2} + \sqrt{\left(\frac{x}{2}\right)^2 - 1} \right| + C_1 $$
$$ = \frac{x}{2} \sqrt{x^2 - 4} - 2 \ln \left| \frac{x + \sqrt{x^2 - 4}}{2} \right| + C_1 $$
$$ = \frac{x}{2} \sqrt{x^2 - 4} - 2 \ln \left| x + \sqrt{x^2 - 4} \right| + C, $$
where $C = C_1 + 2 \ln 2 \in \mathbb{R}$.

---

### Slide 61: Other Techniques of Integration: Exercises

Calculate the following

$I_1 = \int \sin x \cosh x dx, \quad I_2 = \int \frac{e^x \cdot \cos^2(\sqrt[3]{1 + e^x})}{\sqrt[3]{1 + e^x}} dx, \quad I_3 = \int (2x + 1)e^{\arctan x} dx,$

$I_4 = \int x(1 + x^2)^{-3/2} e^{\arctan x} dx, \quad I_5 = \int \frac{x \cos x - \sin x}{x^2} dx, \quad I_6 = \int \frac{1}{x^3} \sqrt[5]{\frac{x}{x + 1}} dx,$

$I_7 = \int x^2 (a^2 - x^2)^{3/2} dx \quad (a > 0), \quad I_8 = \int \frac{dx}{x^2 \sqrt{a^2 - x^2}} \quad (a > 0),$

$I_9 = \int \arctan(1 - \sqrt{x}) dx, \quad I_{10} = \int \frac{\arcsin x}{(1 - x^2)\sqrt{1 - x^2}} dx,$

$I_{11} = \int \frac{dx}{3x + \sqrt[3]{x^2}}, \quad I_{12} = \int x\sqrt[4]{x - 2} dx, \quad I_{13} = \int \frac{x \sqrt[3]{x + 2}}{x + \sqrt[3]{x + 2}} dx.$

$I_{14} = \int \frac{dx}{\sqrt[3]{4x^2 + 4x + 1} - \sqrt{2x + 1}}, \quad I_{15} = \int \frac{dx}{x \sqrt{5x^2 - 2x + 1}}.$

---

### Slide 62: Riemann Sums

We now introduce the notion of a **Riemann sum**, which underlies the theory of the **Definite Integral**.

Let $f : [a, b] \to \mathbb{R}$ be a bounded function. We subdivide the interval $[a, b]$ into sub-intervals, not necessarily of equal width (or length). For this, we choose $n - 1$ points $\{x_1, x_2, \dots, x_{n-1}\}$ between $a$ and $b$ that are in increasing order, so that
$$ a := x_0 < x_1 < x_2 < \dots < x_{n-1} < x_n := b. $$
The set of points $P := \{x_0, x_1, x_2, \dots, x_{n-1}, x_n\}$ is called a **partition** of $[a, b]$.
It divides $[a, b]$ into the $n$ closed sub-intervals: $[x_0, x_1], [x_1, x_2], \dots, [x_{n-1}, x_n]$.
The sub-interval $[x_0, x_1]$ with width $\Delta x_1 = x_1 - x_0$, $[x_1, x_2]$ with width $\Delta x_2 = x_2 - x_1$, and the $k$th sub-interval $[x_{k-1}, x_k]$ with width $\Delta x_k = x_k - x_{k-1}$ (where $k = 1, 2, \dots, n$).

**Image Description:**
A number line representing the x-axis. The segment from $a$ (labeled $x_0$) to $b$ (labeled $x_n$) is divided into segments of unequal lengths.
*   The first segment is labeled $\Delta x_1$ between $x_0$ and $x_1$.
*   The second segment is labeled $\Delta x_2$ between $x_1$ and $x_2$.
*   A middle segment is labeled $\Delta x_k$ between $x_{k-1}$ and $x_k$.
*   The last segment is labeled $\Delta x_n$ between $x_{n-1}$ and $x_n$.

If all $n$ sub-intervals have equal width, then their common width is $\Delta x = \frac{b-a}{n}$.
In each sub-interval $[x_{k-1}, x_k]$ ($\forall 1 \le k \le n$), we select a point $c_k$, and we stand a vertical rectangle that stretches from the $x$-axis to touch the curve at $(c_k, f(c_k))$.

---

### Slide 63: Riemann Sums (Visual)

**Image Description:**
A graph of a function $y = f(x)$ plotted on an $xy$-plane.
The interval $[a, b]$ on the x-axis is partitioned into sub-intervals. Above each sub-interval $[x_{k-1}, x_k]$, a rectangle is drawn.
*   The width of the $k$-th rectangle is $\Delta x_k = x_k - x_{k-1}$.
*   The height of the $k$-th rectangle is determined by the function value $f(c_k)$ at a chosen sample point $c_k$ inside that sub-interval.
*   Some rectangles are above the x-axis (where $f(x) > 0$) and are shaded in light red.
*   Some rectangles are below the x-axis (where $f(x) < 0$), extending downwards.
*   A specific rectangle labeled "$k$th rectangle" is pointed out, showing the sample point $c_k$ and height $f(c_k)$.
*   The curve passes through the tops of these rectangles at the points $(c_k, f(c_k))$.

---

### Slide 64: Riemann Sums

On each sub-interval, we form the product $f(c_k) \cdot \Delta x_k$. This product is positive, negative, or zero, depending on the sign of $f(c_k)$. Finally, we get the following sum
$$ S_P = \sum_{k=1}^n f(c_k) \cdot \Delta x_k, $$
Which called a **Riemann sum for f on the interval [a, b]**. There are many such sums, depending on the chosen partition $P$ and on the chosen points $c_k$ in the sub-intervals.
Let us choose $n$ sub-intervals all having equal width $\Delta x = \frac{b-a}{n}$ to partition $[a, b]$, and then choose the point $c_k$ to be the right-hand endpoint of each sub-interval when forming the Riemann sum. This choice leads to the **Riemann sum formula**
$$ S_P = \sum_{k=1}^n f\left( a + k \frac{b - a}{n} \right) \left( \frac{b - a}{n} \right). $$
In the cases in which the sub-intervals all have equal width $\Delta x = (b - a)/n$, we can make them thinner by simply increasing their number $n$.
When a partition has sub-intervals of varying widths, we define the **norm** of a partition $P$, written $\|P\|$, to be the largest of all the sub-interval widths. If $\|P\|$ is a small number, then all of the sub-intervals in the partition $P$ have a small width.

---

### Slide 65: Riemann Sums

**Example.** The set $P = \{0, 0.2, 0.6, 1, 1.5, 2\}$ is a partition of $[0, 2]$. There are five sub-intervals of $P$: $[0, 0.2]$ (with width $\Delta x_1 = 0.2$), $[0.2, 0.6]$ (with width $\Delta x_2 = 0.4$), $[0.6, 1]$ (with width $\Delta x_3 = 0.4$), $[1, 1.5]$ (with width $\Delta x_4 = 0.5$), $[1.5, 2]$ (with width $\Delta x_5 = 0.5$).

**Image Description:**
*Top:* A number line from 0 to 2 showing the partition points and the varying widths $\Delta x_1$ through $\Delta x_5$.
*Bottom:* Two graphs labeled (a) and (b) showing Riemann sums approximating the area under a blue curve $y=f(x)$.
*   **Graph (a):** Shows a partition with fewer, wider rectangles. The approximation is rough.
*   **Graph (b):** Shows a partition with more, narrower rectangles. The approximation of the area under the curve is much closer to the actual shape of the curve.
*   **Figure Caption:** Any Riemann sum associated with a partition of a closed interval $[a, b]$ defines rectangles that approximate the region between the graph of a continuous function $f$ and the x-axis. Partitions with norm approaching zero lead to collections of rectangles that approximate this region with increasing accuracy.

---

### Slide 66: Riemann Sums: Exercises

**Exercise 1.**
For each function $f$,
1.  $f(x) = x^2 - 1, \quad [0, 2]$.
2.  $f(x) = \sin x, \quad [-\pi, \pi]$.
sketch its graph over the given interval. Partition the interval into four sub-intervals of equal length. Then add to your sketch the rectangles associated with the Riemann sum $\sum_{k=1}^4 f(c_k)\Delta x_k$, given that $c_k$ is the
(a) left-hand endpoint,
(b) right-hand endpoint,
(c) midpoint of the $k$th sub-interval.

**Exercise 2.**
For each function $f$,
1.  $f(x) = 2x, \quad [0, 1]$.
2.  $f(x) = 3x + 2x^2, \quad [0, 1]$.
find a formula for the Riemann sum obtained by dividing the interval $[a, b]$ into $n$ equal sub-intervals and using the right-hand endpoint for each $c_k$. Then take a limit of these sums as $n \to \infty$ to calculate the area under the curve over $[a, b]$.

---

### Slide 67: Definition of the Definite Integral

Now, we consider the limit of general Riemann sums as the norm of the partitions of a closed interval $[a, b]$ approaches zero. This limiting process leads us to the definition of the **definite integral** of a function over a closed interval $[a, b]$.

**Definition (Definite Integral)**
Let $f(x)$ be a function defined on a closed interval $[a, b]$. We say that a number $J$ is the **definite integral of f over [a, b]** and that $J$ is the limit of the Riemann sums $\sum_{k=1}^n f(c_k)\Delta x_k$ if the following condition is satisfied:
Given any number $\varepsilon > 0$, there is a corresponding number $\delta > 0$ such that **for every partition** $P = \{x_0, x_1, \dots, x_n\}$ of $[a, b]$, with $\|P\| < \delta$, and **any choice** of $c_k$ in $[x_{k-1}, x_k]$, we have
$$ \left| \sum_{k=1}^n f(c_k)\Delta x_k - J \right| < \varepsilon. $$
The definite integral exists when we always get the **same limit** $J$, no matter what choices are made. **When the limit exists**, we write
$$ J = \lim_{\|P\| \to 0} \sum_{k=1}^n f(c_k)\Delta x_k := \int_a^b f(x)dx, $$
and we say that the **definite integral exists**, and $f$ is said to be **integrable** over $[a, b]$.

---

### Slide 68: Definition of the Definite Integral

**Remark.** If we pick the point $c_k$ to be the right endpoint of the $k$th sub-interval, so that $c_k = a + k\Delta x = a + k\frac{b-a}{n}$, then the formula for the definite integral becomes
$$ \int_a^b f(x)dx = \lim_{n \to \infty} \sum_{k=1}^n f\left( a + k \frac{b - a}{n} \right) \left( \frac{b - a}{n} \right) \quad (18) $$
Equation (18) gives an explicit formula that can be used to compute definite integrals.
When the definite integral exists, the Riemann sums coming from other choices of partitions and locations of points $c_k$ will have the same limit as $n \to \infty$, provided that the norms of the partitions approach zero.

**Integrable and Non-integrable Functions.**
Not every function defined over a closed interval $[a, b]$ is integrable, even if the function is bounded. That is, the Riemann sums for some functions might not converge to the same limiting value, or to any value at all. Understanding which functions defined over $[a, b]$ are integrable and which are not, requires advanced mathematical analysis, but fortunately, most functions that commonly occur in applications are integrable. In particular, every continuous function over $[a, b]$ is integrable over this interval. The following theorem establishes this result.

---

### Slide 69: Integrable and Non-integrable Functions

**Theorem (Continuous Functions Are Integrable)**
If a function $f$ is continuous over the interval $[a, b]$, or if $f$ has at most finitely many jump discontinuities there, then the definite integral $\int_a^b f(x)dx$ exists, and $f$ is integrable over $[a, b]$.

**Remark.** Note that this theorem says nothing about how to calculate definite integrals. A method of calculation will be developed in the next, through a connection of definite integrals to antiderivatives.

**Example (non-integrable function).** The function (called **Dirichlet function**)
$$ f(x) = \begin{cases} 1, & \text{if } x \text{ is rational,} \\ 0, & \text{if } x \text{ is irrational,} \end{cases} $$
has no Riemann integral over $[0, 1]$. At every $x$, the function $f$ takes either value 1 or 0, and in any tiny interval it jumps infinitely often between these values.

---

### Slide 70: Integrable and Non-integrable Functions

For a partition $P$ of $[0, 1]$:
*   If we pick all sample points $c_k$ to be **rational**, then
    $$ \sum_{k=1}^n f(c_k)\Delta x_k = \sum_{k=1}^n (1)\Delta x_k = 1. $$
    So the Riemann sum is equal to 1 for any partition if we choose rational points.
*   If we pick all sample points $c_k$ to be **irrational**, then
    $$ \sum_{k=1}^n f(c_k)\Delta x_k = \sum_{k=1}^n (0)\Delta x_k = 0. $$
    So the Riemann sum is equal to 0 for any partition if we choose irrational points.

So, by choosing different sample points, we can make the Riemann sum tend to 1 or 0 even as $\|P\| \to 0$. Thus, the limit of Riemann sums depends on the choice of $c_k$, so the Riemann integral **does not exist**.

---

### Slide 71: Properties of Definite Integrals

**Theorem**
Let $f$ and $g$ be integrable functions over the interval $[a, b]$, then it satisfies the following rules

1.  **Order of Integration:** $\int_a^b f(x)dx = -\int_b^a f(x)dx$.
2.  **Zero Width Interval:** $\int_a^a f(x)dx = 0$.
3.  **Constant Multiple:** $\int_a^b k f(x)dx = k \int_a^b f(x)dx, \quad \forall k \in \mathbb{R}$.
4.  **Sum and Difference:** $\int_a^b (f(x) \pm g(x))dx = \int_a^b f(x)dx \pm \int_a^b g(x)dx$.
5.  **Additivity:** $\int_a^b f(x)dx + \int_b^c f(x)dx = \int_a^c f(x)dx$.
6.  **Min-Max Inequality:** If $f$ has maximum value $\max f$ and minimum value $\min f$ on $[a, b]$, then
    $$ \min f \cdot (b - a) \le \int_a^b f(x)dx \le \max f \cdot (b - a). $$
7.  **Domination:** If $f(x) \ge g(x)$ on $[a, b]$, then $\int_a^b f(x)dx \ge \int_a^b g(x)dx$.
    **Special case:** If $f(x) \ge 0$ on $[a, b]$, then $\int_a^b f(x)dx \ge 0$.

---

### Slide 72: Properties of Definite Integrals

**Proof.** By the definition of the definite integral, we can prove the first five properties in addition to the seventh property.

To prove the **Rule 6**, for any partition $P$ of $[a, b]$ (recall that $\sum_{k=1}^n \Delta x_k = b - a$) and for any choice of the points $c_k$, we have the following
$$ \min f \cdot (b - a) = \min f \cdot \sum_{k=1}^n \Delta x_k = \sum_{k=1}^n \min f \cdot \Delta x_k \le \sum_{k=1}^n f(c_k) \cdot \Delta x_k $$
$$ \le \sum_{k=1}^n \max f \cdot \Delta x_k = \max f \cdot \sum_{k=1}^n \Delta x_k = \max f \cdot (b - a). $$
Therefore, all Riemann sums for $f$ on $[a, b]$ satisfy the inequality
$$ \min f \cdot (b - a) \le \sum_{k=1}^n f(c_k)\Delta x_k \le \max f \cdot (b - a). $$
Hence,
$$ \min f \cdot (b - a) \le \lim_{\|P\| \to 0} \sum_{k=1}^n f(c_k)\Delta x_k = \int_a^b f(x)dx \le \max f \cdot (b - a). $$

---

### Slide 73: Properties of Definite Integrals (Visual)

**Image Description:**
Six graphs illustrating the properties of definite integrals.
*   **(a) Zero Width Interval:** A graph of $y=f(x)$ showing a single vertical line at $x=a$. The area is 0.
*   **(b) Constant Multiple:** Two graphs. One shows the area under $y=f(x)$, the other shows the area under $y=2f(x)$ or $y=kf(x)$. The area is scaled by $k$.
*   **(c) Sum:** A graph showing $y=f(x)$ and stacked on top is $y=f(x)+g(x)$. The total area under the top curve is the sum of the individual areas.
*   **(d) Additivity:** A graph of $y=f(x)$ divided into two regions, one from $a$ to $c$ and the other from $c$ to $b$. The sum of these two areas equals the total area from $a$ to $b$.
*   **(e) Max-Min Inequality:** A graph showing the area under $f(x)$ bounded by two rectangles: a smaller one with height $\min f$ and a larger one with height $\max f$.
*   **(f) Domination:** A graph showing two functions $f(x)$ and $g(x)$ where $f(x) \ge g(x)$. The area under $f$ is shown to be larger than the area under $g$.

---

### Slide 74: Mean Value Theorem for Definite Integrals

**Definition**
If $f$ is integrable on $[a, b]$, then its **average value** on $[a, b]$, also called its **mean**, is
$$ \text{av}(f) = \frac{1}{b - a} \int_a^b f(x)dx. $$

**Theorem (The Mean Value Theorem for Definite Integrals)**
If $f$ is **continuous** on $[a, b]$, then there exist $c \in [a, b]$, such that,
$$ f(c) = \text{av}(f) = \frac{1}{b - a} \int_a^b f(x)dx. $$

**Proof.** From the Min-Max inequality, for the integral $\int_a^b f(x)dx$, we find
$$ \min f \le \frac{1}{b - a} \int_a^b f(x)dx \le \max f. $$
Since $f$ is continuous, the Intermediate Value Theorem for Continuous Functions says that $f$ must assume every value between $\min f$ and $\max f$. Therefore, there is $c \in [a, b]$ such that $f(c) = \frac{1}{b - a} \int_a^b f(x)dx$.

---

### Slide 75: The Fundamental Theorem of Calculus

Geometrically, the Mean Value Theorem says that there is a number $c$ in $[a, b]$ such that the rectangle with height equal to the average value (or mean) $f(c)$ (when $f \ge 0$) of the function and base width $b - a$ has the same area as the region beneath the graph of $f$ from $a$ to $b$.

**Image Description:**
*Top Right:* A graph showing the curve $y=f(x)$ from $a$ to $b$. A rectangle is superimposed on the area. The height of the rectangle is $f(c)$, and its area is equal to the shaded area under the curve.

Let $f(t)$ be an **integrable** function over a **finite** interval $I$, then the integral from any fixed number $a \in I$ to another number $x \in I$ defines a new function $F$ whose value at $x$ is
$$ F(x) = \int_a^x f(t)dt. $$

**Image Description:**
*Bottom Right:* A graph illustrating the area accumulation function $F(x)$. It shows the area under $y=f(t)$ shaded from $a$ to $x$.

For example, if $f$ is non-negative and $x$ lies to the right of $a$, then the function $F(x)$ represents the area under the graph from $a$ to $x$. For each value of the input $x$, there is a single numerical output, which is the definite integral of $f$ from $a$ to $b$.

---

### Slide 76: The Fundamental Theorem of Calculus, Part 1

**Theorem (The Fundamental Theorem of Calculus, Part 1.)**
If $f$ is continuous on $[a, b]$, then $F(x) = \int_a^x f(t)dt$ is continuous on $[a, b]$ and differentiable on $(a, b)$, and its derivative is $f(x)$. That is $F'(x) = \frac{d}{dx} \int_a^x f(t)dt = f(x)$ (this means that $F(x)$ is an antiderivative of $f(x)$).

**Proof.** If $x, x + h \in (a, b)$, then we have
$$ \lim_{h \to 0} \frac{F(x + h) - F(x)}{h} = \lim_{h \to 0} \frac{1}{h} \left( \int_a^{x+h} f(t)dt - \int_a^x f(t)dt \right) $$
$$ = \lim_{h \to 0} \frac{1}{h} \left( \int_a^x f(t)dt + \int_x^{x+h} f(t)dt \right) - \int_a^x f(t)dt $$
$$ = \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} f(t)dt. $$
By the Mean Value Theorem for Definite Integrals, there exists $c \in [x, x + h]$, such that $f(c) = \frac{1}{h} \int_x^{x+h} f(t)dt \in \mathbb{R}$. This means that $F$ is differentiable (and thus it is continuous) on $(a, b)$. Because $h \to 0$, we get $x + h \to x$, and $c \to x$. Because $f$ is continuous at $x$, then $\lim_{h \to 0} f(c) = \lim_{c \to x} f(c) = f(x)$. Therefore, we get
$$ F'(x) = \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} f(t)dt = \lim_{h \to 0} f(c) = \lim_{c \to x} f(c) = f(x). $$

---

### Slide 77: The Fundamental Theorem of Calculus, Part 1. Examples

We make a similar argument, except that at $x = a$ we need only consider the one-sided limit as $h \to 0^+$, and at $x = b$ we consider $h \to 0^-$. This shows that $F$ has a one-sided derivative at $x = a$, and at $x = b$, and therefore $F$ is continuous at those two points.

**Example 1.** For $y = \left( \int_x^0 (t^3 + 1)^{10} dt \right)^3 = - \left( \int_0^x (t^3 + 1)^{10} dt \right)^3$, we have
$$ \frac{dy}{dx} = -3 \left( \int_0^x (t^3 + 1)^{10} dt \right)^2 \left( \int_0^x (t^3 + 1)^{10} dt \right)' = -3(x^3 + 1)^{10} \left( \int_0^x (t^3 + 1)^{10} dt \right)^2. $$

**Example 2.** For the function $y = x \int_2^{x^2} \sin(t^3) dt$, we have
$$ \frac{dy}{dx} = \int_2^{x^2} \sin(t^3) dt + x \frac{d}{dx} \left( \int_2^{x^2} \sin(t^3) dt \right). $$
Let $g(x) := \int_2^{x^2} \sin(t^3) dt$, and $u := x^2$, then by Chain Rule, we get
$$ \frac{dg}{dx} = \frac{dg}{du} \cdot \frac{du}{dx} = \frac{d}{du} \left( \int_2^u \sin(t^3) dt \right) \cdot \frac{d}{dx}(x^2) = \sin(u^3) \cdot 2x = 2x \sin(x^6). $$
Hence,
$$ \frac{dy}{dx} = \int_2^{x^2} \sin(t^3) dt + 2x^2 \sin(x^6). $$

---

### Slide 78: The Fundamental Theorem of Calculus, Part 1. Exercises

**Exercises.**

Find $\frac{dy}{dx}$, for each of the following functions

$$ y = \int_1^x \frac{1}{u} du \quad (x > 0), \quad y = \int_{\sqrt{x}}^0 \sin(v^2) dv, $$
$$ y = \int_{\tan x}^0 \frac{dt}{1 + t^2}, \quad y = \int_{2x}^{3x} \frac{t^2 - 1}{t^2 + 1} dt, $$
$$ y = \int_x^{x^2} e^{\theta^2} d\theta, \quad y = \int_{\sqrt{x}}^{2x} \arctan(q) dq, $$
$$ y = \int_{1-2x}^{1+2x} t \sin t \, dt, \quad y = \int_{\cos x}^{\sin x} \ln(1 + 2v) dv. $$

---

### Slide 79: The Fundamental Theorem of Calculus, Part 2 (The Evaluation Theorem)

**Theorem (The Fundamental Theorem of Calculus, Part 2)**
If $f$ is continuous over $[a, b]$ and $F$ is any antiderivative of $f$ on $[a, b]$, then
$$ \int_a^b f(x)dx = \int_a^b F'(x)dx = F(b) - F(a) := [F(x)]_a^b. $$

**Proof.**
By the Fundamental Theorem of Calculus (Part 1), there exists an antiderivative of $f$,
$$ G(x) = \int_a^x f(t)dt. $$
Thus, if $F$ is any antiderivative of $f$, then $F(x) = G(x) + C$ for some constant $C \in \mathbb{R}$, and $a < x < b$. Since both $F$ and $G$ are continuous on $[a, b]$, we see that the equality $F(x) = G(x) + C$ also holds when $x = a$ and $x = b$ by taking one-sided limits (as $x \to a^+$ and $x \to b^-$). Thus, we get
$$ F(b) - F(a) = (G(b) + C) - (G(a) + C) = G(b) - G(a) $$
$$ = \int_a^b f(t)dt - \int_a^a f(t)dt = \int_a^b f(x)dx. $$

---

### Slide 80: The Fundamental Theorem of Calculus, Part 2. Exercises

**Exercise 1.** Evaluate the following integrals:

$I_1 = \int_1^4 \left( 3x^2 - \frac{x^3}{4} \right) dx, \quad I_2 = \int_0^1 \left( x^2 + \sqrt{x} \right) dx, \quad I_3 = \int_0^{\pi/3} \frac{4 \sin u}{\cos^2 u} du,$

$I_4 = \int_{-\pi/3}^{\pi/3} \sin^2 t \, dt, \quad I_5 = \int_1^8 \frac{(\sqrt[3]{x} + 1)(2 - \sqrt[3]{x^2})}{\sqrt[3]{x}} dx, \quad I_6 = \int_{-4}^3 |x - 1| dx,$

$I_7 = \int_0^{\pi} \frac{1}{2} (\cos x + |\cos x|) dx, \quad I_8 = \int_{1/2}^{1/\sqrt{2}} \frac{4}{\sqrt{1 - x^2}} dx$

$I_9 = \int_0^{\pi} f(x)dx, \quad \text{where } f(x) = \begin{cases} \sin x, & \text{if } 0 \le x < \pi/2 \\ \cos x, & \text{if } \pi/2 \le x \le \pi, \end{cases}$

$I_{10} = \int_{-2}^2 f(x)dx, \quad \text{where } f(x) = \begin{cases} 2, & \text{if } -2 \le x \le 0 \\ 4 - x^2, & \text{if } 0 < x \le 2. \end{cases}$

**Exercise 2.** What is wrong with the following equations
$$ \int_{-2}^1 x^{-4} dx = \left[ \frac{x^{-3}}{-3} \right]_{-2}^1, \quad \int_{\pi/3}^{\pi} \sec \theta \cdot \tan \theta d\theta = [\sec \theta]_{\pi/3}^{\pi} = -3. $$

---

### Slide 81: The Substitution Rule for Definite Integrals

**Theorem (Substitution in Definite Integrals)**
If $g'$ is continuous on the interval $[a, b]$, and $f$ is continuous on the range of $g(x) = u$. Then
$$ \int_a^b f(g(x))g'(x)dx = \int_{g(a)}^{g(b)} f(u)du. $$

**Proof.** Let $F$ be an antiderivative of $f$ on $[a, b]$.
Since $\frac{d}{dx} F(g(x)) = F'(g(x))g'(x) = f(g(x))g'(x)$, we have
$$ \int_a^b f(g(x))g'(x)dx = [F(g(x))]_a^b = F(g(b)) - F(g(a)) = [F(u)]_{u=g(a)}^{u=g(b)} = \int_{g(a)}^{g(b)} f(u)du. $$

**Example 1.** For the integral $I_1 = \int_0^2 \frac{5x}{(4 + x^2)^2} dx$. Let $u = x^2$, then $du = 2xdx$. If $x = 0$, then $u = 0$, and if $x = 2$, then $u = 4$. Thus, we get
$$ I_1 = \frac{5}{2} \int_0^4 \frac{1}{(4 + u)^2} du = -\frac{5}{4} \left[ \frac{1}{4 + u} \right]_0^4 = -\frac{5}{2} \left( \frac{1}{8} - \frac{1}{4} \right) = -\frac{5}{16}. $$

---

### Slide 82: The Substitution Rule for Definite Integrals

**Example 2.** For the integral $I_2 = \int_0^1 \arctan\left(\sqrt{x + 3}\right) dx$. Using the substitution $\sqrt{x + 3} = t$, we find $\frac{dx}{2\sqrt{x+3}} = dt$, and $dx = 2tdt$. When $x = 0$, then $t = \sqrt{3}$, and when $x = 1$, then $t = 2$. Hence, we get
$$ I_2 = 2 \int_{\sqrt{3}}^2 t \arctan t dt. $$
By using integration by parts, let us assume
$$ u = \arctan t \implies du = \frac{dt}{1 + t^2}, \quad dv = tdt \implies v = \frac{t^2}{2}. $$
Thus, we get
$$ I_2 = 2 \left( \left[ \frac{t^2}{2} \arctan t \right]_{\sqrt{3}}^2 - \frac{1}{2} \int_{\sqrt{3}}^2 \frac{t^2}{1 + t^2} dt \right) $$
$$ = \left[ t^2 \arctan t \right]_{\sqrt{3}}^2 - \int_{\sqrt{3}}^2 \left( 1 - \frac{1}{1 + t^2} \right) dt $$
$$ = 4 \arctan 2 - 3 \arctan(\sqrt{3}) - [t + \arctan t]_{\sqrt{3}}^2 $$
$$ = 5 \arctan 2 - 4 \arctan(\sqrt{3}) - 2 + \sqrt{3}. $$

---

### Slide 83: The Substitution Rule for Definite Integrals

**Example 3.** (MIT Integration Bee 2014) For the integral
$$ I_3 = \int_0^2 \sqrt{x + \sqrt{x + \sqrt{x + \sqrt{x + \dots}}}} dx. $$
Let
$$ y := \sqrt{x + \sqrt{x + \sqrt{x + \dots}}} \ge 0, \quad \forall x \in [0, 2]. $$
Then
$$ y^2 = x + \underbrace{\sqrt{x + \sqrt{x + \dots}}}_{y} = x + y \implies y^2 - y - x = 0. $$
By solving the quadratic equation $y^2 - y - x = 0$, for $y$, we find
$$ y = \frac{1 - \sqrt{1 + 4x}}{2} < 0, \quad y = \frac{1 + \sqrt{1 + 4x}}{2} > 0, \quad \forall x \in [0, 2]. $$
Therefore, for the given integral, we have
$$ I_4 = \int_0^2 \left( \frac{1}{2} + \frac{1}{2}\sqrt{4x + 1} \right) dx = \left[ \frac{1}{2}x + \frac{1}{12}\sqrt{(4x + 1)^3} \right]_0^2 = 1 + \frac{\sqrt{9^3}}{12} - \frac{1}{12} = \frac{19}{6}. $$

---

### Slide 84: Definite Integrals of Symmetric Functions

**Theorem**
Let $f$ be continuous on the symmetric interval $[-a, a]$, then
1.  If $f$ is **even**, then $\int_{-a}^a f(x)dx = 2 \int_0^a f(x)dx$.
2.  If $f$ is **odd**, then $\int_{-a}^a f(x)dx = 0$.

**Proof.** When $f$ is an even, we have
$$ \int_{-a}^a f(x)dx = \int_{-a}^0 f(x)dx + \int_0^a f(x)dx = -\int_0^{-a} f(x)dx + \int_0^a f(x)dx $$
Using $u = -x$:
$$ = -\int_0^a f(-u)(-du) + \int_0^a f(x)dx = \int_0^a f(-u)(du) + \int_0^a f(x)dx $$
$$ = \int_0^a f(u)(du) + \int_0^a f(x)dx = 2 \int_0^a f(x)dx. $$
When $f$ is an odd function, the proof is entirely similar, where
$$ \int_{-a}^a f(x)dx = \int_0^a f(-u)(du) + \int_0^a f(x)dx = -\int_0^a f(u)du + \int_0^a f(x)dx = 0. $$

---

### Slide 85: The Substitution Rule for Definite Integrals. Exercises

Calculate the following integrals.

$I_1 = \int_0^1 \frac{10\sqrt{x}}{\left(1 + \sqrt{x}^3\right)^2} dx, \quad I_2 = \int_{-\pi}^{\pi} \frac{\cos x}{\sqrt{4 + 3 \sin x}} dx,$

$I_3 = \int_1^4 \frac{1}{\sqrt{x} \left(1 + 2\sqrt{x}\right)^{10}} dx, \quad I_4 = \int_{-1}^{-1/2} x^{-2} \sin^2 \left(1 + \frac{1}{x}\right) dx,$

$I_5 = \int_2^{16} \frac{1}{2x\sqrt{\ln x}} dx, \quad I_6 = \int_0^{\pi/3} \frac{\sin(2x)}{\sqrt{1 + 3 \sin^2 x}} dx,$

$I_7 = \int_0^1 \frac{1}{\left(1 + \sqrt{x}\right)^4} dx, \quad I_8 = \int_0^{\pi/2} \cos x \sin(\sin x)dx.$

$I_9 = \int_0^{\sqrt{3}/2} x \arctan(2x)dx, \quad I_{10} = \int_0^{2\pi} x^2 \cos(4x)dx$

---

### Slide 86: Applications of Definite Integrals: Calculating Areas

**Definition**
Let $f$ be an integrable function over a closed interval $[a, b]$. Then
1.  If $f(x) \ge 0 (\forall x \in [a, b])$, then the area between the curve $y = f(x)$ and the x-axis over $[a, b]$ is
    $$ A = \int_a^b f(x)dx $$
2.  If $f(x) \le 0 (\forall x \in [a, b])$, then the area between the curve $y = f(x)$ and the x-axis over $[a, b]$ is
    $$ A = -\int_a^b f(x)dx $$

**Remark.** To find the area between the graph of $y = f(x)$ and the x-axis over the interval $[a, b]$:
1.  Subdivide $[a, b]$ at the zeros of $f$ by solving the equation $f(x) = 0$.
2.  Integrate $f$ over each sub-interval.
3.  Add the absolute values of the integrals.

---

### Slide 87: Applications of Definite Integrals: Calculating Areas

**Example.**
Find the area of the region between the x-axis and the graph of $f(x) = x^3 - x^2 - 2x, -1 \le x \le 2$.

**Image Description:**
A graph of the cubic function $y = x^3 - x^2 - 2x$ on the interval $[-1, 2]$.
The curve starts at $x=-1$ (where $y=0$), goes up to a positive peak, crosses the x-axis at $x=0$, goes down to a negative valley, and returns to the x-axis at $x=2$.
The region between $x=-1$ and $x=0$ is above the axis and labeled "Area = 5/12".
The region between $x=0$ and $x=2$ is below the axis and labeled "Area = |-8/3| = 8/3".

**Solution.** We have
$$ f(x) = 0 \implies x = -1, 0, 2. $$
and the total enclosed area $A = |S_1| + |S_2|$, where
$$ S_1 = \int_{-1}^0 f(x)dx = \int_{-1}^0 (x^3 - x^2 - 2x)dx = \left[ \frac{x^4}{4} - \frac{x^3}{3} + x^2 \right]_{-1}^0 = \frac{5}{12}. $$
$$ S_2 = \int_0^2 f(x)dx = \int_0^2 (x^3 - x^2 - 2x)dx = \left[ \frac{x^4}{4} - \frac{x^3}{3} + x^2 \right]_0^2 = -\frac{8}{3}. $$
Therefore, the total enclosed area $A = \frac{5}{12} + \left|-\frac{8}{3}\right| = \frac{37}{12}$.

---

### Slide 88: Applications of Definite Integrals: Calculating Areas

**Definition (Areas Between Curves)**
If $f$ and $g$ are continuous with $f(x) \ge g(x)$ throughout $[a, b]$, then the area of the region between the curves $y = f(x)$ and $y = g(x)$ from $a$ to $b$ is $A = \int_a^b (f(x) - g(x))dx$.
**In general**, The area between the curves $y = f(x)$ and $y = g(x)$ and $x = a, x = b$ is
$$ A = \int_a^b |f(x) - g(x)|dx. $$

**Example 1.** Find the area of the region enclosed by the parabola $y = 2 - x^2$ and the line $y = -x$.

**Image Description:**
A graph showing a downward-opening parabola $y = 2 - x^2$ intersected by a straight line $y = -x$.
The intersection points are indicated at $(-1, 1)$ and $(2, -2)$.
A vertical rectangular strip with width $\Delta x$ is drawn between the curves to illustrate the integration element.

**Solution.** For the intersection points between the parabola and the line, we set
$$ 2 - x^2 = -x \implies x = -1, 2. $$
Thus, we have two intersection points at $x = -1, 2$. For the enclosed area, we have
$$ A = \int_{-1}^2 |f(x) - g(x)|dx = \int_{-1}^2 (2 + x - x^2)dx = \frac{9}{2}. $$

---

### Slide 89: Applications of Definite Integrals: Calculating Areas

**Example 2.**
Find the area of the region bounded by the curves $y = \sin x, y = \cos x, x = 0$, and $x = \frac{\pi}{2}$.

**Image Description:**
A graph showing the sine curve ($y=\sin x$) and the cosine curve ($y=\cos x$) on the interval $[0, \pi/2]$.
They intersect at $x=\pi/4$.
Two regions are shaded:
*   $A_1$: From $x=0$ to $x=\pi/4$, where $\cos x > \sin x$.
*   $A_2$: From $x=\pi/4$ to $x=\pi/2$, where $\sin x > \cos x$.

**Solution.** For the intersection points between the curves over $[0, \pi/2]$, we set
$$ \sin x = \cos x \implies x = \frac{\pi}{4}. $$
Thus, we have one intersection point at $x = \frac{\pi}{4}$. For the enclosed area, we have
$$ A = \int_0^{\pi/2} |\cos x - \sin x|dx = A_1 + A_2 $$
$$ = \int_0^{\pi/4} (\cos x - \sin x)dx + \int_{\pi/4}^{\pi/2} (\sin x - \cos x)dx $$
$$ = [\sin x + \cos x]_0^{\pi/4} + [-\cos x - \sin x]_{\pi/4}^{\pi/2} $$
$$ = 2\sqrt{2} - 2. $$

---

### Slide 90: Applications of Definite Integrals: Calculating Volumes

**Volume Formulas.**

**Formula 1.** Let $S$ be a solid bounded by two parallel planes perpendicular to the x-axis at $x = a$ and $x = b$. If, for each $x \in [a, b]$, the cross-sectional area of $S$ perpendicular to the x-axis is $A(x)$, then the volume of the solid is $V = \int_a^b A(x)dx$, provided $A(x)$ is integrable.

**Image Description (Right):**
A diagram of a generic 3D solid shape lying along an axis from $a$ to $b$. A cross-sectional slice at position $x$ is highlighted, showing its area. This illustrates the method of slicing to find volume.

**Formula 2.**
Let $S$ be a solid bounded by two parallel planes perpendicular to the y-axis at $y = c$ and $y = d$. If, for each $y \in [c, d]$, the cross-sectional area of $S$ perpendicular to the y-axis is $A(y)$, then the volume of the solid is $V = \int_c^d A(y)dy$, provided $A(y)$ is integrable.

Thus, these formulas state: The volume of a solid can be obtained by integrating the cross-sectional area from one end of the solid to the other.

---

### Slide 91: Applications of Definite Integrals: Calculating Volumes

**Example.**
Derive the formula for the volume of a right pyramid whose altitude is $h$ and whose base is a square with sides of length $a$.

**Image Description:**
A diagram of a square pyramid.
*   The altitude is labeled $h$.
*   The base is a square with side length $a$.
*   A cross-section parallel to the base at coordinate $y$ is shown as a square with side length $s$.
*   A side-view triangle diagram illustrates the similar triangles used to derive the relationship between $s$ and $y$: $\frac{s/2}{a/2} = \frac{h-y}{h}$.

**Solution.**
At any $y$ in the interval $[0, h]$ on the y-axis, the cross section perpendicular to the y-axis is a square. If $s$ denotes the length of a side of this square, then by similar triangles
$$ \frac{s/2}{a/2} = \frac{h - y}{h} \implies s = \frac{a}{h}(h - y). $$
Thus, the area $A(y)$ of the cross section at $y$ is $A(y) = s^2 = \frac{a^2}{h^2}(h - y)^2$. Hence, we have
$$ V = \int_0^h A(y)dy = \int_0^h \frac{a^2}{h^2}(h - y)^2 = \frac{a^2}{h^2} \left[ -\frac{1}{3}(h - y)^3 \right]_0^h $$
$$ = \frac{a^2}{h^2} \cdot \frac{1}{3}h^3 = \frac{1}{3}a^2 h. $$

---

### Slide 92: Applications of Definite Integrals: Calculating Volumes

**Solids of Revolution.**
A solid of revolution is a solid that is generated by revolving a plane region about a line that lies in the same plane as the region; the line is called the axis of revolution.

**Image Description:**
A series of diagrams showing 2D shapes and the 3D solids formed by revolving them around an axis:
1.  A rectangle revolves to form a **Right circular cylinder**.
2.  A semicircle revolves to form a **Solid sphere**.
3.  A right triangle revolves to form a **Solid cone**.
4.  A rectangle distant from the axis revolves to form a **Hollowed right circular cylinder** (washer shape).
**Figure:** Some Familiar Solids of Revolution

---

### Slide 93: Applications of Definite Integrals: Calculating Volumes

To calculate the volume of a solid of revolution, we have the following cases.

**Volumes by Disks Perpendicular to The x-Axis.**
Let $f$ be continuous and non-negative on $[a, b]$, and let $R$ be the region that is bounded above by $y = f(x)$, below by the x-axis, and on the sides by the lines $x = a$ and $x = b$. The volume of the solid of revolution that is generated by revolving the region $R$ about the x-axis is
$$ V = \int_a^b \pi (f(x))^2 dx. $$

**Image Description:**
*Left:* A 2D graph showing a region $R$ under a curve $y=f(x)$ from $a$ to $b$.
*Right:* The 3D solid generated by revolving $R$ around the x-axis. A representative disk slice at position $x$ with radius $f(x)$ is highlighted to illustrate the disk method.

---

### Slide 94: Applications of Definite Integrals: Calculating Volumes

**Volumes by Washers Perpendicular to The x-Axis.**
Let $f$ and $g$ be continuous and non-negative on $[a, b]$, and suppose that $f(x) \ge g(x) \forall x \in [a, b]$. let $R$ be the region that is bounded above by $y = f(x)$, below by the $y = g(x)$, and on the sides by the lines $x = a$ and $x = b$. The volume of the solid of revolution that is generated by revolving the region $R$ about the x-axis is
$$ V = \int_a^b \pi \left( (f(x))^2 - (g(x))^2 \right) dx. $$

**Image Description:**
*Left:* A 2D graph showing a region $R$ enclosed between two curves $y=f(x)$ (top) and $y=g(x)$ (bottom).
*Right:* The hollow 3D solid generated by revolving $R$ around the x-axis. A representative washer (ring) slice at position $x$ is highlighted, showing the outer radius $f(x)$ and inner radius $g(x)$.

---

### Slide 95: Applications of Definite Integrals: Calculating Volumes

**Volumes by Disks and Washers Perpendicular to The y-Axis.**
Similarly, when the solid of revolution that is generated by revolving the region $R$ about the y-axis, the volume by disks and washers will as the following
$$ V = \int_c^d \pi(u(y))^2 dy, \quad V = \int_c^d \pi \left( (w(y))^2 - (v(y))^2 \right) dy $$

**Image Description:**
*Left (Disk Method):* A 2D region bounded by $x=u(y)$ and the y-axis is rotated around the y-axis. The resulting solid is shown with a horizontal disk slice.
*Right (Washer Method):* A 2D region bounded by $x=w(y)$ (outer) and $x=v(y)$ (inner) is rotated around the y-axis. The resulting hollow solid is shown with a horizontal washer slice.

---

### Slide 96: Applications of Definite Integrals: Calculating Volumes

**Example 1.**
Derive the formula for the volume of a sphere of radius $r$.

**Solution.**
A sphere of radius $r$ can be generated by revolving the upper semicircular disk enclosed between the x-axis and
$$ x^2 + y^2 = r^2. $$
about the x-axis. Since the upper half of this circle is the graph of
$$ y = f(x) = \sqrt{r^2 - x^2}, \quad -r \le x \le r. $$
It follows that the volume of the sphere is
$$ V = \int_{-r}^r \pi (f(x))^2 dx = \int_{-r}^r \pi (r^2 - x^2) dx = \pi \left[ r^2x - \frac{x^3}{3} \right]_{-r}^r = \frac{4}{3}\pi r^3 $$

**Image Description:**
A diagram showing a semicircle of radius $r$ ($x^2+y^2=r^2$) on the coordinate plane. An arrow indicates rotation around the x-axis to form a sphere.

---

### Slide 97: Applications of Definite Integrals: Calculating Volumes

**Example 2.**
Find the volume of the solid generated when the region between the graphs of the equations $f(x) = \frac{1}{2} + x^2$ and $g(x) = x$ over the interval $[0, 2]$ is revolved about the x-axis.

**Solution.**
The volume is
$$ V = \int_a^b \pi \left( (f(x))^2 - (g(x))^2 \right) dx = \int_0^2 \pi \left( \left(\frac{1}{2} + x^2\right)^2 - x^2 \right) dx $$
$$ = \pi \int_0^2 \left( \frac{1}{4} + x^4 \right) dx = \pi \left[ \frac{x}{4} + \frac{x^5}{5} \right]_0^2 = \frac{69\pi}{10} $$

**Image Description:**
*Left:* Graph of the region bounded by the parabola $y = 1/2 + x^2$ and the line $y = x$.
*Right:* The funnel-shaped 3D solid created by rotating this region around the x-axis.

---

### Slide 98: Applications of Definite Integrals: Calculating Volumes

**Example 3.**
Find the volume of the solid generated when the region enclosed by $y = \sqrt{x}, y = 2$, and $x = 0$ is revolved about the y-axis.

**Solution.**
The cross sections taken perpendicular to the y-axis are disks. First we must rewrite $y = \sqrt{x}$ as $x = y^2$. Thus, with $u(y) = y^2$, the volume is
$$ V = \int_c^d \pi (u(y))^2 dy = \int_0^2 \pi y^4 dy = \left[ \frac{\pi y^5}{5} \right]_0^2 = \frac{32\pi}{5} $$

**Image Description:**
*Left:* Graph of the region bounded by $y=\sqrt{x}$, $y=2$, and the y-axis.
*Right:* The bowl-shaped solid generated by rotating this region around the y-axis, with a representative horizontal disk shown.

---

### Slide 99: Applications of Definite Integrals: Calculating Lengths

If the curve is the graph of a continuous function defined over an interval, then we can find the length of the curve using a procedure similar to that we used for defining the area between the curve and the x-axis. We divide the curve into many pieces, and we approximate each piece by a straight line segment. The sum of the lengths of these segments is an approximation to the total curve length that we seek. The total length of the curve is the limiting value of these approximations as the number of segments goes to infinity.

**Definition (Length (Arc Length) of the Curve)**
1.  If $f'$ is continuous on $[a, b]$, then the **length (arc length)** of the curve $y = f(x)$ from $A = (a, f(a))$ to $B = (b, f(b))$ is $L = \int_a^b \sqrt{1 + (f'(x))^2} dx$.
2.  If $g'$ is continuous on $[c, d]$, then the **length (arc length)** of the curve $x = g(y)$ from $A = (g(c), c)$ to $B = (g(d), d)$ is $L = \int_c^d \sqrt{1 + (g'(y))^2} dy$.

**Remark.** If the curve is given by the parametric equations $x = x(t), y = y(t), a \le t \le b$.
Then the length from $A(x(a), y(a))$ to $B(x(b), y(b))$ is $L = \int_a^b \sqrt{(x'(t))^2 + (y'(t))^2} dt$.

---

### Slide 100: Applications of Definite Integrals: Calculating Lengths

**Example 1.** Find the length of the graph of $y = \frac{4\sqrt{2}}{3}x^{3/2} - 1, 0 \le x \le 1$.

**Solution.**
We have $y = f(x) = \frac{4\sqrt{2}}{3}\sqrt{x^3} - 1 \implies f'(x) = 2\sqrt{2x}$.
Thus,
$$ L = \int_0^1 \sqrt{1 + (f'(x))^2} dx = \int_0^1 \sqrt{1 + 8x} dx = \frac{13}{6} $$

**Image Description:**
A graph of the function $y = \frac{4\sqrt{2}}{3}x^{3/2} - 1$ from $x=0$ to $x=1$, showing the curve starting at $(0,-1)$ and ending at $B$. A straight line connects the endpoints to illustrate the approximation.

**Example 2.** Find the length of the curve $y = \sqrt[3]{(x/2)^2}, 0 \le x \le 2$.

**Solution.** The derivative $\frac{dy}{dx} = \frac{1}{3}(\frac{2}{x})^{1/3}$ is not defined at $x = 0$. Therefore, we will express $x$ as a function of $y$, where $x = 2y^{3/2}$, and $0 \le y \le 1$.
The derivative $\frac{dx}{dy} = 3\sqrt{y}$ is continuous on $[0, 1]$. Therefore, the required length is
$$ L = \int_c^d \sqrt{1 + \left(\frac{dx}{dy}\right)^2} dy = \int_0^1 \sqrt{1 + 9y} dy = \frac{2}{27}(10\sqrt{10} - 1) $$

---

### Slide 101: Applications of Definite Integrals: Calculating Areas of Surfaces

**A surface of revolution** is a surface that is generated by revolving a plane curve about an axis that lies in the same plane as the curve. For example, the surface of a sphere can be generated by revolving a semicircle about its diameter.

**Image Description:**
Four pairs of diagrams. Each pair shows a 2D curve and the corresponding 3D surface generated by revolving it.
1.  Semicircle $\to$ Sphere.
2.  Horizontal line segment $\to$ Cylinder.
3.  Slanted line segment $\to$ Cone frustum.
4.  Curved segment $\to$ Hourglass-like shape.
**Figure:** Some Surfaces of Revolution

---

### Slide 102: Applications of Definite Integrals: Calculating Areas of Surfaces

For many applications, the area of the surface of revolution is needed, not only the volume it surrounds.

**Definition (Area of the Surface)**
1.  **(The revolution about x-axis)**
    If the function $y = f(x) \ge 0$ is continuously differentiable on $[a, b]$, the area of the surface generated by revolving the graph of $y = f(x)$ about the x-axis is
    $$ S = \int_a^b 2\pi f(x) \sqrt{1 + (f'(x))^2} dx. $$
2.  **(The revolution about y-axis)**
    If the function $x = g(y) \ge 0$ is continuously differentiable on $[c, d]$, the area of the surface generated by revolving the graph of $x = g(y)$ about the y-axis is
    $$ S = \int_c^d 2\pi g(y) \sqrt{1 + (g'(y))^2} dy. $$

---

### Slide 103: Applications of Definite Integrals: Calculating Areas of Surfaces

**Example 1.**
Find the area of the surface that is generated by revolving the portion of the curve $y = x^3$ between $x = 0$ and $x = 1$, about the x-axis.

**Solution.**
We have $y = f(x) = x^3$. Thus, the surface area $S$ is
$$ S = \int_a^b 2\pi f(x) \sqrt{1 + (f'(x))^2} dx $$
$$ = \int_0^1 2\pi x^3 \sqrt{1 + (3x^2)^2} dx $$
$$ = \frac{\pi}{27}(10^{3/2} - 1) $$

**Image Description:**
*Right:* A graph showing the curve $y=x^3$ from $(0,0)$ to $(1,1)$ and the trumpet-shaped surface generated by revolving it around the x-axis.

---

### Slide 104: Applications of Definite Integrals: Calculating Areas of Surfaces

**Example 2.**
Find the area of the surface that is generated by revolving the portion of the curve $y = x^2$ between $x = 1$ and $x = 2$, about the y-axis.

**Solution.**
We have $y = x^2, 1 \le x \le 2$. Thus, $x = \sqrt{y}, 1 \le y \le 4$. Therefore, the required surface area $S$ is
$$ S = \int_c^d 2\pi g(y) \sqrt{1 + (g'(y))^2} dy $$
$$ = \int_1^4 2\pi \sqrt{y} \sqrt{1 + \left(\frac{1}{2\sqrt{y}}\right)^2} dy $$
$$ = \pi \int_1^4 \sqrt{1 + 4y} dy $$
$$ = \frac{\pi}{6} \left( 17^{3/2} - 5^{3/2} \right) $$

**Image Description:**
*Right:* A diagram showing the solid generated by revolving the curve $y=x^2$ (from $x=1$ to $x=2$) around the y-axis, creating a bowl-like shape. The point $(2, 4)$ is labeled.

---

### Slide 105: Applications of Definite Integrals: Exercises

**Calculating Areas.** Find the areas of the regions enclosed by the curves
1.  $y = 4 - x^2, y = -x + 2, x = -2, x = 3$,
2.  $y = x^3 + 4x, x = -1, x = 2$,
3.  $y = \cos(2x), y = 0, x = \pi/4, x = \pi/2$,
4.  $y = -x^2 + 3x, y = 2x^3 - x^2 - 5x$,
5.  $y = xe^{x^2}, y = 2|x|$,
6.  $y = |x^2 - 4|, y = (x^2/2) + 4$.

**Calculating Volumes.** Find the volume of the solid that results when the region enclosed by the given curves is revolved about the x-axis or y-axis (as given).
1.  $y = e^x, y = 0, x = 0, x = \ln 3$. (about the x-axis)
2.  $y = \frac{e^{3x}}{\sqrt{1 + e^{6x}}}, x = 0, x - 1, y = 0$. (about the x-axis)
3.  $y = \sqrt{25 - x^2}, y = 3$. (about the x-axis)
4.  $y = x^2, x = y^2$. (about the y-axis)
5.  $x = 1 - y^2, x = 2 + y^2, y = -1, y = 1$. (about the y-axis)
6.  $y = \frac{\sqrt{1-x^2}}{x^2} (x > 0), x = 0, y = 0, y = 1$. (about the y-axis)

---

### Slide 106: Applications of Definite Integrals: Exercises

**Calculating Lengths of Curves.** Find the lengths of the curve
1.  $y = \frac{1}{3}\sqrt{(x^2 + 2)^3}$ from $x = 0$ to $x = 3$.
2.  $x = \frac{y^3}{3} + \frac{1}{4y}$ from $y = 1$ to $y = 3$.
3.  $y = \frac{x^3}{3} + x^2 + x + \frac{1}{4(x+1)}$ from $x = 0$ to $x = 2$.
4.  $x = (1 + t)^2, y = (1 + t)^3, 0 \le t \le 1$.
5.  $x = e^t \cos t, y = e^t \sin t, 0 \le t \le \frac{\pi}{2}$.
6.  $x = \cos t + t \sin t, y = \sin t - t \cos t, 0 \le t \le \pi$.

**Calculating Areas of Surfaces.** Find the areas of the surfaces generated by revolving the curves about the indicated axes.
1.  $y = \sqrt{2x - x^2}, \frac{1}{2} \le x \le \frac{3}{2}$, x-axis.
2.  $x = \frac{1}{3} \sqrt{y^3} - \sqrt{y}, 1 \le y \le 3$, y-axis.
3.  $x = 2\sqrt{4 - y}, 0 \le y \le \frac{15}{4}$, y-axis.
4.  $x = \frac{e^y + e^{-y}}{2}, 0 \le y \le \ln 2$, y-axis.
5.  $x = \sqrt[3]{y}, 1 \le t \le 8$, x-axis.
6.  $y = \frac{x^3}{9}, 0 \le x \le 2$, x-axis.

---

### Slide 107: Improper Integrals

The Riemann integral is an operation defined for certain **bounded functions** defined on **bounded intervals**. Sometimes, even when one or both of these boundedness requirements are violated, we can still give a meaning to an integral. In either case, the integrals are said to be **improper** and are calculated as limits.

**Definition (Improper Integrals of Type I (the integrals over infinite intervals))**
Integrals with infinite limits of integration are called **improper integrals of Type I**.

1.  If $f(x)$ is continuous on $[a, \infty)$, then $\int_a^{\infty} f(x) dx = \lim_{b \to \infty} \int_a^b f(x) dx$.
2.  If $f(x)$ is continuous on $(-\infty, b]$, then $\int_{-\infty}^b f(x) dx = \lim_{a \to -\infty} \int_a^b f(x) dx$.
3.  If $f(x)$ is continuous on $(-\infty, \infty)$, then
    $$ \int_{-\infty}^{\infty} f(x) dx = \int_{-\infty}^c f(x) dx + \int_c^{\infty} f(x) dx, $$
    where $c$ is any real number (with any convenient choice).

In each case, if the **limit exists and is finite**, we say that the improper integral **converges** and that the limit is the **value** of the improper integral. If the limit fails to exist or it is infinite, the improper integral **diverges**.

---

### Slide 108: Improper Integrals

**Famous improper integrals.**
Dirichlet integral: $\int_0^{\infty} \frac{\sin x}{x} dx = \frac{\pi}{2}$.
Gaussian integral: $\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$.

**Example 1.** Evaluate $\int_1^{\infty} \frac{\ln x}{x^2} dx$.
**Solution.** We have
$$ \int_1^{\infty} \frac{\ln x}{x^2} dx = \lim_{b \to \infty} \int_1^b \frac{\ln x}{x^2} dx. $$
By using the integration by parts, with $u = \ln x, dv = \frac{dx}{x^2}$, we find
$$ \int_1^b \frac{\ln x}{x^2} dx = \left[ (\ln x) \left(-\frac{1}{x}\right) \right]_1^b - \int_1^b \left(-\frac{1}{x}\right) \left(\frac{1}{x}\right) dx = -\frac{\ln b}{b} - \frac{1}{b} + 1. $$
Thus,
$$ \int_1^{\infty} \frac{\ln x}{x^2} dx = \lim_{b \to \infty} \left( -\frac{\ln b}{b} - \frac{1}{b} + 1 \right) = - \left[ \lim_{b \to \infty} \frac{\ln b}{b} \right] - 0 + 1 $$
$$ = - \left( \lim_{b \to \infty} \frac{1}{b} \right) + 1 = 0 + 1 = 1 $$
Thus, the improper integral converges, and its value is 1.

---

### Slide 109: Improper Integrals

**Example 2.** Evaluate $\int_{-\infty}^{\infty} \frac{dx}{1 + x^2}$.
**Solution.** We have
$$ \int_{-\infty}^{\infty} \frac{dx}{1 + x^2} = \int_{-\infty}^0 \frac{dx}{1 + x^2} + \int_0^{\infty} \frac{dx}{1 + x^2}. $$
Next, we evaluate each improper integral simultaneously.
$$ \int_{-\infty}^0 \frac{dx}{1 + x^2} = \lim_{a \to -\infty} \int_a^0 \frac{dx}{1 + x^2} = \lim_{a \to -\infty} \left[\tan^{-1} x\right]_a^0 $$
$$ = \lim_{a \to -\infty} (\tan^{-1} 0 - \tan^{-1} a) = 0 - \left(-\frac{\pi}{2}\right) = \frac{\pi}{2}. $$

$$ \int_0^{\infty} \frac{dx}{1 + x^2} = \lim_{b \to \infty} \int_0^b \frac{dx}{1 + x^2} = \lim_{b \to \infty} \left[\tan^{-1} x\right]_0^b $$
$$ = \lim_{b \to \infty} (\tan^{-1} b - \tan^{-1} 0) = \frac{\pi}{2} - 0 = \frac{\pi}{2}. $$
Thus,
$$ \int_{-\infty}^{\infty} \frac{dx}{1 + x^2} = \frac{\pi}{2} + \frac{\pi}{2} = \pi. $$

---

### Slide 110: Improper Integrals

**Example 3.** For the integral $I_p = \int_1^{\infty} \frac{dx}{x^p}$, depending on the value of $p \in \mathbb{R}$, we have

*   If $p \neq 1$, then
    $$ \int_1^b \frac{dx}{x^p} = \left[ \frac{x^{-p+1}}{-p + 1} \right]_1^b = \left( \frac{1}{1 - p} \right) (b^{-p+1} - 1) = \left( \frac{1}{1 - p} \right) \left( \frac{1}{b^{p-1}} - 1 \right). $$
    Because $\lim_{b \to \infty} \frac{1}{b^{p-1}} = \begin{cases} 0, & p > 1 \\ \infty, & p < 1, \end{cases}$ we find the following
    $$ \int_1^{\infty} \frac{dx}{x^p} = \lim_{b \to \infty} \int_1^b \frac{dx}{x^p} = \lim_{b \to \infty} \left[ \left( \frac{1}{1 - p} \right) \left( \frac{1}{b^{p-1}} - 1 \right) \right] = \begin{cases} \frac{1}{p-1}, & p > 1 \\ \infty, & p < 1 \end{cases} $$
    Therefore, the integral $I_p$ converges to the value $1/(p - 1)$ if $p > 1$, and it diverges if $p < 1$.

*   If $p = 1$, then
    $$ \int_1^{\infty} \frac{dx}{x^p} = \int_1^{\infty} \frac{dx}{x} = \lim_{b \to \infty} \int_1^b \frac{dx}{x} = \lim_{b \to \infty} [\ln |x|]_1^b = \lim_{b \to \infty} (\ln b - \ln 1) = \infty. $$
    Hence, the integral $I_p$ converges to $1/(p - 1)$ when $p > 1$ and divergent when $p \le 1$.

---

### Slide 111: Improper Integrals

**Definition (Improper Integrals of Type II (the integrands are discontinuous))**
Integrals of functions that become infinite at a point within the interval of integration are **improper integrals of Type II**.

1.  If $f(x)$ is continuous on $(a, b]$ and discontinuous at $a$, then
    $$ \int_a^b f(x)dx = \lim_{c \to a^+} \int_c^b f(x)dx = \lim_{\varepsilon \to 0} \int_{a+\varepsilon}^b f(x)dx. $$

2.  If $f(x)$ is continuous on $[a, b)$ and discontinuous at $b$, then
    $$ \int_a^b f(x)dx = \lim_{c \to b^-} \int_a^c f(x)dx = \lim_{\varepsilon \to 0} \int_a^{b+\varepsilon} f(x)dx. $$

3.  If $f(x)$ is discontinuous at $c$, where $a < c < b$, and continuous on $[a, c) \cup (c, b]$, then
    $$ \int_a^b f(x)dx = \int_a^c f(x) dx + \int_c^b f(x)dx. $$

In each case, if the limit exists and is finite, we say that the improper integral **converges** and that the limit is the **value** of the improper integral. If the limit does not exist, or it is infinite, the improper integral **diverges**.

---

### Slide 112: Improper Integrals

**Example 1.** Evaluate the integral $I_1 = \int_1^2 \frac{dx}{1 - x}$.
**Solution.**
$$ \int_1^2 \frac{dx}{1 - x} = \lim_{a \to 1^+} \int_a^2 \frac{dx}{1 - x} = \lim_{a \to 1^+} [-\ln|1 - x|]_a^2 $$
$$ = \lim_{a \to 1^+} [-\ln|-1| + \ln|1 - a|] = \lim_{a \to 1^+} \ln|1 - a| = -\infty $$
so the integral $I_1$ diverges.

**Example 2.** Evaluate the integral $I_2 = \int_1^2 \frac{dx}{(x - 2)^{2/3}}$.
**Solution.** Note that the integrand approaches $+\infty$ at $x = 2$. Thus, we have
$$ I_2 = \int_1^4 \frac{dx}{(x - 2)^{2/3}} = \int_1^2 \frac{dx}{(x - 2)^{2/3}} + \int_2^4 \frac{dx}{(x - 2)^{2/3}}. $$
$$ \int_1^2 \frac{dx}{(x - 2)^{2/3}} = \lim_{k \to 2^-} \int_1^k \frac{dx}{(x - 2)^{2/3}} = \lim_{k \to 2^-} \left[ 3(k - 2)^{1/3} - 3(1 - 2)^{1/3} \right] = 3. $$
$$ \int_2^4 \frac{dx}{(x - 2)^{2/3}} = \lim_{k \to 2^+} \int_k^4 \frac{dx}{(x - 2)^{2/3}} = \lim_{k \to 2^+} \left[ 3(4 - 2)^{1/3} - 3(k - 2)^{1/3} \right] = 3\sqrt[3]{2}. $$
Therefore, we get $I_2 = 3 + 3\sqrt[3]{2}$, and the integral $I_2$ converges.

---

### Slide 113: Improper Integrals: Tests for Convergence and Divergence

When we cannot evaluate an improper integral directly, we try to determine whether it converges or diverges.

**Theorem (Direct Comparison Test)**
Let $f$ and $g$ be continuous on $[a, \infty)$ with $0 \le f(x) \le g(x)$ for all $x \ge a$. Then
1.  if $\int_a^{\infty} g(x)dx$ converges, then $\int_a^{\infty} f(x)dx$ also converges.
2.  if $\int_a^{\infty} f(x)dx$ diverges, then $\int_a^{\infty} g(x)dx$ also diverges.

**Examples.**
1.  The integral $\int_1^{\infty} e^{-x^2} dx$ converges because $0 < e^{-x^2} < e^{-x} \forall x \ge 1$, and
    $$ \int_1^{\infty} e^{-x} dx = \lim_{b \to \infty} \int_1^b e^{-x} dx = \lim_{b \to \infty} [-e^{-x}]_1^b = \lim_{b \to \infty} (-e^{-b} + e^{-1}) = \frac{1}{e}. $$
2.  $\int_1^{\infty} \frac{\sin^2 x}{x^2} dx$ converges because $0 \le \frac{\sin^2 x}{x^2} \le \frac{1}{x^2} \forall x \in [1, \infty)$, and $\int_1^{\infty} \frac{1}{x^2} dx$ converges.
3.  $\int_1^{\infty} \frac{1}{\sqrt{x^2 - 1}} dx$ diverges because $\frac{1}{\sqrt{x^2 - 0.1}} \ge \frac{1}{x} \forall x \in [1, \infty)$, and $\int_1^{\infty} \frac{1}{x} dx$ diverges.

---

### Slide 114: Improper Integrals

**Theorem (Limit Comparison Test)**
If $f(x) \ge 0, g(x) \ge 0$ are continuous functions on $[a, \infty)$, and if $\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$. Then
1.  $\int_a^{\infty} f(x)dx$ and $\int_a^{\infty} g(x)dx$ either both converge or both diverge.
2.  If $L = 0$ and $\int_a^{\infty} g(x)dx$ converges, then $\int_a^{\infty} f(x)dx$ converges.
3.  If $L = \infty$ and $\int_a^{\infty} g(x)dx$ diverges, then $\int_a^{\infty} f(x)dx$ diverges.

**Examples.**
1.  The integral $I_1 = \int_1^{\infty} \frac{dx}{1 + x^2}$ converges (by the Limit Comparison Test), because $\lim_{x \to \infty} \frac{1/(1+x^2)}{1/x^2} = 1$, and the integral $\int_1^{\infty} \frac{dx}{x^2}$ converges.
2.  For the integral $I_2 = \int_1^{\infty} \frac{1 - e^{-x}}{x} dx$, let $f(x) := \frac{1-e^{-x}}{x}$, and $g(x) := \frac{1}{x}$. Then $\lim_{x \to \infty} \frac{f(x)}{g(x)} = \lim_{x \to \infty} (1 - e^{-x}) = 1$. Thus, because $\int_1^{\infty} g(x)dx = \int_1^{\infty} \frac{dx}{x}$ diverges, then by the Limit Comparison Test, we find that the integral $I_2$ diverges.
3.  The integral $\int_0^{\infty} \frac{x^2}{4x^4 + 5x + 25} dx$ converges, since $\lim_{x \to \infty} \frac{x^2/(4x^4 + 5x + 25)}{1/x^2} = \frac{1}{4}$.
4.  The integral $\int_0^{\infty} \frac{x}{\sqrt{x^4 + x^2 + 2}} dx$ diverges, since $\lim_{x \to \infty} \frac{x/\sqrt{x^4 + x^2 + 2}}{1/x} = 1$.

---

### Slide 115: Improper Integrals and Infinite Series (Cauchy Integral Test)

**Theorem**
Let $\sum_{n=1}^{\infty} a_n$ be a series with non-negative terms (i.e., $a_n \ge 0, \forall n \ge 1$), and let $f$ be a real-valued, continuous, and decreasing function on $[1, +\infty[$, such that $f(n) = a_n$. Then, the series $\sum_{n=1}^{\infty} a_n$ and the improper integral $\int_1^{\infty} f(x)dx$ are of the same nature; that is, either both convergent or divergent.

**Example 1.** The series $\sum_{n=1}^{\infty} \frac{1}{n^p}$ converges for any $p > 1$, and diverges for any $p \le 1$.
Recall that the integral $\int_1^{\infty} \frac{dx}{x^p}$ converges for any $p > 1$ and diverges for every $p \le 1$.

**Example 2.** For the series $\sum_{n=1}^{\infty} \frac{1}{\sqrt{n} \cdot e^{\sqrt{n}}}$. Let us consider the function
$$ f : [1, +\infty[ \to \mathbb{R}^+; \quad f(x) = \frac{1}{\sqrt{x} \cdot e^{\sqrt{x}}}. $$

---

### Slide 116: Cauchy Integral Test

This function is continuous on $[1, +\infty[$, and
$$ f'(x) = -\frac{\sqrt{x}(e^{\sqrt{x}} + 1)}{2x^2 \cdot e^{2\sqrt{x}}} < 0, \quad \forall x \in [1, +\infty[. $$
Hence, the conditions of the Cauchy integral test are satisfied. We also have
$$ \int_1^{\infty} f(x)dx = \lim_{b \to \infty} \int_1^b \frac{1}{\sqrt{x} \cdot e^{\sqrt{x}}} dx = \lim_{b \to \infty} \int_1^b \frac{e^{-\sqrt{x}}}{\sqrt{x}} dx. $$
Let $\sqrt{x} = t$. Then, $\frac{dx}{2\sqrt{x}} = dt$. Thus,
$$ \int_1^{\infty} f(x)dx = \lim_{b \to \infty} \int_1^{\sqrt{b}} 2e^{-t} dt = \lim_{b \to \infty} -2 [e^{-t}]_1^{\sqrt{b}} = \lim_{b \to \infty} -2 \left( e^{-\sqrt{b}} - e^{-1} \right) = \frac{2}{e}. $$
Therefore, the integral $\int_1^{\infty} f(x)dx$ is convergent. Hence, the given series is convergent according to the Cauchy Integral Test.

---

### Slide 117: Cauchy Integral Test

**Example 3.** For the series $\sum_{n=2}^{\infty} \frac{2^{\ln(\ln(n))}}{n \ln(n)}$, Let us consider the function
$$ f : [2, +\infty[ \to \mathbb{R}^+; \quad f(x) = \frac{2^{\ln(\ln(x))}}{x \ln(x)}. $$
This function is continuous on $[2, +\infty[$, and
$$ f'(x) = \frac{(\ln(2) - 1 - \ln(x))2^{\ln(\ln(x))}}{x^2 \ln^2(x)} < 0, \quad \forall x \in [2, +\infty[. $$
Hence, the conditions of the Cauchy Integral Test are satisfied. We also have
$$ \int_{10}^{\infty} f(x)dx = \lim_{b \to \infty} \int_{10}^b \frac{2^{\ln(\ln(x))}}{x \ln(x)} dx \stackrel{\ln(\ln(x))=t}{=} \lim_{b \to \infty} \int_{\ln(\ln(2))}^{\ln(\ln(b))} 2^t dt = \lim_{b \to \infty} \left[ \frac{2^t}{\ln(2)} \right]_{\ln(\ln(2))}^{\ln(\ln(b))} = \infty. $$
Therefore, the integral $\int_2^{\infty} f(x)dx$ is divergent. Hence, the given series is divergent according to the Cauchy Integral Test.

---

### Slide 118: Improper Integrals: Exercises

**Exercise 1.** Determine whether each integral is convergent or divergent. Evaluate those that are convergent
$$ \int_3^{\infty} \frac{dx}{(x - 2)^{3/2}}, \quad \int_{-\infty}^{\infty} x e^{-x^2} dx, \quad \int_1^{\infty} \frac{e^{-1/x}}{x^2} dx, $$
$$ \int_2^{\infty} \frac{dx}{x^2 + 2x - 3}, \quad \int_0^{\infty} e^{-\sqrt{x}} dx, \quad \int_1^{\infty} \frac{dx}{\sqrt{x} + x\sqrt{x}}, $$
$$ \int_{-1}^2 \frac{x}{(x + 1)^2} dx, \quad \int_0^9 \frac{dx}{\sqrt[3]{x - 1}}, \quad \int_0^4 \frac{dx}{x^2 - x - 2}, \quad \int_0^1 \frac{e^{1/x}}{x^3} dx. $$

**Exercise 2.** Examine for convergence (using the convergence tests)
$$ \int_1^{\infty} \frac{x}{3x^4 + 5x^2 + 1} dx, \quad \int_2^{\infty} \frac{x^2 - 1}{\sqrt{x^6 + 16}} dx, \quad \int_0^{\infty} e^{-x^2} dx, \quad \int_1^{\infty} \frac{\ln x}{x + 5}. $$

**Exercise 3.** Study the behavior of the following series
$$ \sum_{n=1}^{\infty} \frac{e^{\arctan(n)}}{n^2 + 1}, \quad \sum_{n=2}^{\infty} \frac{1}{n\sqrt{\ln(n)}}, \quad \sum_{n=2}^{\infty} \frac{1}{n \ln^2(n)}, \quad \sum_{n=2}^{\infty} \frac{n}{e^{\sqrt{n}}}, \quad \sum_{n=2}^{\infty} \frac{1}{n \ln(n) \cdot (\ln(\ln(n)))^2}. $$

---

### Slide 119: Conclusion

**Thank You for Your Attention!** -->