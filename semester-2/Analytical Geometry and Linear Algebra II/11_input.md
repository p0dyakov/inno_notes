# Lab

## Страница 1
**Problem 1**

Find the **eigenvalues**, **eigenvectors** and $e^{At}$ for
$$A = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$$

***

## Страница 2
**Problem 2**

Solve the following differential equation:
$$\frac{du}{dt}(t) = Au$$
$$u(0) = u_0$$

where
$$A = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \quad \text{and} \quad u_0 = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$$

***

## Страница 3
**Problem 3**

Find a matrix $A$ to illustrate each of the stability regions in Figure 1.
<span style="color:green">(a)</span> $\lambda_1 < 0$ and $\lambda_2 > 0$
<span style="color:green">(b)</span> $\lambda_1 > 0$ and $\lambda_2 > 0$
<span style="color:green">(c)</span> Complex $\lambda$'s with real part $a > 0$

> **[Описание изображения]**
> График на координатной плоскости, показывающий области устойчивости динамических систем в зависимости от следа матрицы (ось абсцисс, обозначена как trace $T$) и её определителя (ось ординат, обозначена как determinant $D$).
> * В верхней полуплоскости ($D > 0$) нарисована пунктирная парабола с уравнением $T^2 = 4D$, на которой $\lambda_1 = \lambda_2$.
> * Внутри параболы ($T^2 < 4D$) находится область с надписью **complex eigenvalues**. Слева от оси ординат в этой области написано **both $\text{Re}\lambda < 0$ stable**, а справа — **both $\text{Re}\lambda > 0$ unstable**.
> * Ниже параболы, но выше горизонтальной оси (где дискриминант положителен): слева указано **both $\lambda < 0$ real and stable**, справа — **both $\lambda > 0$ real and unstable**.
> * В нижней полуплоскости ($D < 0$) находится область с текстом: **det $< 0$ gives $\lambda_1 < 0$ and $\lambda_2 > 0$: real and unstable**.

***

## Страница 4
**Problem 4**

From their **trace** and **determinant**, at what time $t$ do the following matrices change **between** stable with real eigenvalues, stable with complex eigenvalues and unstable?

$$A_1 = \begin{pmatrix} 1 & -1 \\ t & -1 \end{pmatrix} \quad \text{and} \quad A_2 = \begin{pmatrix} t & -1 \\ 1 & t \end{pmatrix}$$

***

## Страница 5
**Problem 5**

The matrix $B$ has $B^2 = 0$. Find $e^{Bt}$ from an <mark style="background-color: #fce4c8;">infinite series</mark>. Check that the derivative of $e^{Bt}$ is $Be^{Bt}$.

$$B = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix}$$

***

## Страница 6
**Problem 6**

Find a permutation $P$ of the columns of $F$ that produces $FP = \bar{F}$ ($n$ by $n$). Combine with $F\bar{F} = nI$ to find $F^2$ and $F^4$ for the $n$ by $n$ Fourier matrix.

***

## Страница 7
**Problem 7**

➢ Solve the 4 by 4 system, $F_4 c = y$, if the right-hand sides are $y_0 = 2, \ y_1 = 0, \ y_2 = 2, \ y_3 = 0$.

***
***

# Файл 2 (Презентация: The DFT Matrix and Its Properties) - Lecture

*Примечание: футер присутствует на каждом слайде презентации. Для удобства чтения он вынесен в конец каждого блока.*

## Слайд 1
# The DFT Matrix and Its Properties

**Salman Ahmadi-Asl**

Innopolis University

April 24, 2026

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 1 / 25*

***

## Слайд 2
### Lecture Outline

1. Introduction to Fourier Analysis
2. The Roots of Unity
3. The Fourier Matrix
4. Orthogonality Properties
5. Practice Problems

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 2 / 25*

***

## Слайд 3
### Why Fourier Analysis?

> **The Central Idea**
> Any signal/function can be represented as a sum of complex exponentials (sines and cosines).

**Applications:**
* Audio processing (MP3, noise cancellation)
* Image compression (JPEG)
* MRI and medical imaging
* Telecommunications (WiFi, 5G)
* Solving differential equations
* Quantum mechanics

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 3 / 25*

***

## Слайд 4
### From Continuous to Discrete

**Continuous Fourier Transform:**
$$F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t} dt$$
**Problem:** Computers can't integrate continuously!

**Discrete Fourier Transform (DFT):**
$$y_k = \sum_{n=0}^{N-1} x_n e^{-2\pi ikn/N}$$
where $k = 0, 1, \dots, N - 1$

The DFT takes $N$ samples and produces $N$ frequency components.

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 4 / 25*

***

## Слайд 5
### The DFT as a Matrix Operation

The DFT can be written as:
$$\mathbf{y} = F_N \mathbf{x},$$

where $F_N$ is the $N \times N$ **Fourier matrix**.

$$F_N = \frac{1}{\sqrt{N}} \begin{pmatrix} \omega^0 & \omega^0 & \omega^0 & \dots & \omega^0 \\ \omega^0 & \omega^1 & \omega^2 & \dots & \omega^{(N-1)} \\ \omega^0 & \omega^2 & \omega^4 & \dots & \omega^{2(N-1)} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \omega^0 & \omega^{(N-1)} & \omega^{2(N-1)} & \dots & \omega^{(N-1)^2} \end{pmatrix},$$

where $\omega = e^{-2\pi i/N}$.

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 5 / 25*

***

## Слайд 6
### The DFT as a Matrix Operation

So we have:

> **Definition (Fourier Matrix)**
> The $N \times N$ Fourier matrix $F_N$ has entries:
> $$(F_N)_{jk} = \frac{1}{\sqrt{N}} \omega^{jk}, \quad j, k = 0, 1, \dots, N - 1$$
> where $\omega = e^{-2\pi i/N}$.

Here $\omega = e^{-2\pi i/N}$ is the **primitive N-th root of unity**.

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 6 / 25*

***

## Слайд 7
### The N-th Roots of Unity

> **Definition (Roots of Unity)**
> The N-th roots of unity are the complex numbers satisfying $z^N = 1$.

There are exactly $N$ distinct roots:
$$\omega_N^k = e^{2\pi ik/N} = \cos\left(\frac{2\pi k}{N}\right) + i\sin\left(\frac{2\pi k}{N}\right),$$

for $k = 0, 1, 2, \dots, N - 1$.

**Note:** In FFT literature, $\omega = e^{-2\pi i/N}$ is common (sign convention varies).

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 7 / 25*

***

## Слайд 8
### Visualizing Roots of Unity (N = 8)

> **[Описание изображения]**
> График на комплексной плоскости с осями Re (вещественная, горизонтальная) и Im (мнимая, вертикальная). Изображена окружность единичного радиуса. На ней равномерно расположены 8 синих точек, символизирующих корни 8-й степени из единицы. Они обозначены против часовой стрелки:
> * $\omega_8^0$ (находится на точке 1 оси Re)
> * $\omega_8^1$
> * $\omega_8^2$ (находится на верхней точке оси Im)
> * $\omega_8^3$
> * $\omega_8^4$ (находится на точке -1 оси Re)
> * $\omega_8^5$
> * $\omega_8^6$ (находится на нижней точке оси Im)
> * $\omega_8^7$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 8 / 25*

***

## Слайд 9
### The 2 × 2 Fourier Matrix Explicitly

For $N = 2$, write the Fourier matrix $F_2$ explicitly.

**Solution:**
$$\omega = e^{-2\pi i/2} = e^{-i\pi} = -1.$$
$$F_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} \omega^0 & \omega^0 \\ \omega^0 & \omega^1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$

Verify orthogonality:
$$F_2^* F_2 = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I_2.$$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 9 / 25*

***

## Слайд 10
### The 3 × 3 Fourier Matrix Explicitly

For $N = 3$, $\omega = e^{-2\pi i/3} = \cos(120^\circ) - i \sin(120^\circ) = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$

$$F_3 = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & 1 & 1 \\ 1 & \omega & \omega^2 \\ 1 & \omega^2 & \omega^4 \end{pmatrix} = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & 1 & 1 \\ 1 & \omega & \omega^2 \\ 1 & \omega^2 & \omega \end{pmatrix}.$$
(since $\omega^4 = \omega$).

Notice the pattern:
$$F_N = \frac{1}{\sqrt{N}} \begin{pmatrix} 1 & 1 & 1 & \dots & 1 \\ 1 & \omega & \omega^2 & \dots & \omega^{N-1} \\ 1 & \omega^2 & \omega^4 & \dots & \omega^{2(N-1)} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & \omega^{N-1} & \omega^{2(N-1)} & \dots & \omega^{(N-1)^2} \end{pmatrix}.$$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 10 / 25*

***

## Слайд 11
### The 4 × 4 Fourier Matrix Explicitly

For $N = 4$, $\omega = e^{-2\pi i/4} = e^{-i\pi/2} = -i$:

$$\omega^0 = 1, \quad \omega^1 = -i, \quad \omega^2 = -1, \quad \omega^3 = i.$$

$$F_4 = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -i & -1 & i \\ 1 & -1 & 1 & -1 \\ 1 & i & -1 & -i \end{pmatrix}.$$

Check: $(F_4)_{12} = \frac{1}{2}\omega^{1\cdot 2} = \frac{1}{2}\omega^2 = \frac{1}{2}(-1)$.

This matrix transforms 4 time-domain samples to 4 frequency-domain values.

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 11 / 25*

***

## Слайд 12
### Key Properties of $\omega$

> **Fundamental Properties**
> Let $\omega = e^{-2\pi i/N}$. Then:
> 1. **Periodicity:** $\omega^N = 1$.
> 2. **Symmetry:** $\omega^{N/2} = -1$ (if $N$ even).
> 3. **Conjugation:** $\overline{\omega^k} = \omega^{-k} = \omega^{N-k}$.
> 4. **Geometric series:**
> $$\sum_{k=0}^{N-1} \omega^{mk} = \begin{cases} N & \text{if } m \equiv 0 \pmod N \\ 0 & \text{otherwise} \end{cases}$$

<span style="color:red">Property 4 is the key to orthogonality!</span>

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 12 / 25*

***

## Слайд 13
### The Conjugate Fourier Matrix

> **Definition (Conjugate Fourier Matrix)**
> The conjugate Fourier matrix $\overline{F_N}$ has entries:
> $$(\overline{F_N})_{jk} = \frac{1}{\sqrt{N}} \overline{\omega^{jk}} = \frac{1}{\sqrt{N}} \omega^{-jk}.$$

**Important:** $\overline{F_N}$ corresponds to the **inverse DFT** (up to scaling).

For $N = 4$:
$$\overline{F_4} = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{pmatrix}.$$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 13 / 25*

***

## Слайд 14
### The Orthogonality Theorem

> **Theorem (Orthogonality of Fourier Matrix Columns)**
> *The columns of $F_N$ form an **orthonormal basis** of $\mathbb{C}^N$:*
> $$F_N^* F_N = I_N,$$
> *where $F_N^* = \overline{F_N}^T$ is the conjugate transpose.*

Equivalently:
$$(F_N^* F_N)_{mn} = \sum_{k=0}^{N-1} \overline{(F_N)_{km}} (F_N)_{kn} = \delta_{mn}.$$

In other words: $F_N$ is a **unitary matrix**!
$$F_N^{-1} = F_N^*$$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 14 / 25*

***

## Слайд 15
### Proof of Orthogonality

Consider the inner product of columns $m$ and $n$ (0-indexed):

$$(F_N^* F_N)_{mn} = \sum_{k=0}^{N-1} \overline{(F_N)_{km}} (F_N)_{kn}.$$
$$= \sum_{k=0}^{N-1} \left( \frac{1}{\sqrt{N}} \overline{\omega^{km}} \right) \left( \frac{1}{\sqrt{N}} \omega^{kn} \right).$$
$$= \frac{1}{N} \sum_{k=0}^{N-1} \omega^{k(n-m)}.$$

Case 1: $m = n \implies \sum_{k=0}^{N-1} \omega^0 = N \implies \frac{1}{N} \cdot N = 1.$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 15 / 25*

***

## Слайд 16
### Proof of Orthogonality

Case 2: $m \neq n \implies \sum_{k=0}^{N-1} \omega^{k(n-m)} = \frac{1 - \omega^{N(n-m)}}{1 - \omega^{n-m}} = 0 \text{ (since } \omega^N = 1).$

Therefore $(F_N^* F_N)_{mn} = \delta_{mn}.$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 16 / 25*

***

## Слайд 17
### The Inverse Fourier Matrix

Since $F_N$ is unitary:
$$F_N^{-1} = F_N^*.$$

Therefore:
$$\mathbf{x} = F_N^{-1} \mathbf{X} = F_N^* \mathbf{X}.$$

Component-wise:
$$x_n = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} X_k \omega^{-nk}.$$

This is the **inverse DFT** (up to normalization convention).

Some conventions use $F_N$ without the $1/\sqrt{N}$ factor, then:
$$F_N^{-1} = \frac{1}{N} \overline{F_N}^T.$$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 17 / 25*

***

## Слайд 18
### Orthogonality: Row Version

The **rows** of $F_N$ are also orthonormal!

$$F_N F_N^* = I_N.$$

This follows from the same property because $F_N^* F_N = I_N$ implies $F_N$ is invertible with $F_N^{-1} = F_N^*$, so $F_N F_N^* = I_N$ as well.

> **Important**
> The Fourier matrix is **symmetric** ($F_N^T = F_N$) but NOT Hermitian ($F_N^* \neq F_N$ except for small cases).

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 18 / 25*

***

## Слайд 19
### Summary of Orthogonality Properties

| **Property** | **Formula** |
| :--- | :--- |
| Unitarity | $F_N^* F_N = I_N.$ |
| Inverse | $F_N^{-1} = F_N^*.$ |
| Column orthonormality | $\sum_{k=0}^{N-1} \overline{\omega^{km}} \omega^{kn} = N\delta_{mn}.$ |
| Row orthonormality | $\sum_{k=0}^{N-1} \overline{\omega^{mk}} \omega^{nk} = N\delta_{mn}.$ |
| Determinant | $|\det(F_N)| = 1.$ |
| Eigenvalues | $\pm 1, \pm i$ (for powers of 2). |

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 19 / 25*

***

## Слайд 20
### Practice Problem 1

Compute the DFT of $\mathbf{x} = (1, 0, 1, 0)^T$ using $F_4$.

$$F_4 = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -i & -1 & i \\ 1 & -1 & 1 & -1 \\ 1 & i & -1 & -i \end{pmatrix}.$$

$$\mathbf{y} = F_4 \mathbf{x} = \frac{1}{2} \begin{pmatrix} 2 \\ 0 \\ 2 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}.$$

So the DFT of $(1, 0, 1, 0)$ is itself!

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 20 / 25*

***

## Слайд 21
### Practice Problem 2

Show that $F_N^2$ is a permutation matrix for $N = 4$.

$$F_4 = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -i & -1 & i \\ 1 & -1 & 1 & -1 \\ 1 & i & -1 & -i \end{pmatrix}.$$

Compute $F_4^2$:
$$F_4^2 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}.$$

This is a permutation matrix (reverses order of indices 1,2,3).

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 21 / 25*

***

## Слайд 22
### Practice Problem 3

Show that the columns of $F_3$ are orthogonal.

$$F_3 = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & 1 & 1 \\ 1 & \omega & \omega^2 \\ 1 & \omega^2 & \omega \end{pmatrix}, \quad \omega = e^{-2\pi i/3}.$$

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 22 / 25*

***

## Слайд 23
### Further Reading

> **Recommended Resource**
> * **Strang** - Linear Algebra and Its Applications (FFT chapter)

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 23 / 25*

***

## Слайд 24
### Thank You!

Questions?

*Footer: Salman Ahmadi-Asl (Innopolis University) | The DFT Matrix and Its Properties | April 24, 2026 | 24 / 25*