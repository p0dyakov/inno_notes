# File 1: Assignments-Solutions

## Page 1
**Assignments-Solutions**

**1 Similar Matrices - Solutions**

**Exercise 1.1.** *To determine if matrices $A$ and $B$ are similar, we need to find an invertible matrix $M$ such that $MA = BM$, or equivalently $M$ satisfies the linear system.*

**(a)** $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}, B = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}$

Let $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $\det(M) \neq 0$.
*Compute MA:*
$$MA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2a & a + 2b \\ 2c & c + 2d \end{pmatrix}$$

*Compute BM:*
$$BM = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 2a & 2b \\ a + 2c & b + 2d \end{pmatrix}$$

*Set MA = BM:*
$$\begin{pmatrix} 2a & a + 2b \\ 2c & c + 2d \end{pmatrix} = \begin{pmatrix} 2a & 2b \\ a + 2c & b + 2d \end{pmatrix}$$

*This gives the system:*
$2a = 2a$ *(always true)*
$a + 2b = 2b \implies a = 0$
$2c = a + 2c \implies a = 0$ *(consistent)*
$c + 2d = b + 2d \implies c = b$

So $M = \begin{pmatrix} 0 & b \\ b & d \end{pmatrix}$ with $\det(M) = -b^2 \neq 0$, so $b \neq 0$ and any $d$ works.
We can choose $b = 1, d = 0$: $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

*Check:* $MA = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 2 & 1 \end{pmatrix}$
$BM = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 2 & 1 \end{pmatrix}$
Since an invertible $M$ exists, $A$ and $B$ are **similar**.

**(b)** $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}, B = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$

Let $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
*Compute MA:*
$$MA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} a & 2a + 3b \\ c & 2c + 3d \end{pmatrix}$$

## Page 2
*Compute BM:*
$$BM = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 3a & 3b \\ c & d \end{pmatrix}$$

*Set MA = BM:*
$$\begin{pmatrix} a & 2a + 3b \\ c & 2c + 3d \end{pmatrix} = \begin{pmatrix} 3a & 3b \\ c & d \end{pmatrix}$$

*This gives:*
$a = 3a \implies 2a = 0 \implies a = 0$
$2a + 3b = 3b \implies 2a = 0$ *(consistent with a = 0)*
$c = c$ *(always true)*
$2c + 3d = d \implies 2c + 2d = 0 \implies c + d = 0 \implies d = -c$

So $M = \begin{pmatrix} 0 & b \\ c & -c \end{pmatrix}$ with $\det(M) = 0 \cdot (-c) - b \cdot c = -bc$
For $M$ to be invertible, $\det(M) = -bc \neq 0$, so we need $b \neq 0$ and $c \neq 0$.
Choose $b = 1, c = 1$: $M = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$

*Check:* $MA = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 0 & 3 \\ 1 & -1 \end{pmatrix}$
$BM = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 3 \\ 1 & -1 \end{pmatrix}$
Since an invertible $M$ exists, $A$ and $B$ are **similar**.

**(c)** $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$

Let $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
*Compute MA:*
$$MA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & a + b \\ c & c + d \end{pmatrix}$$

*Compute BM (B is identity):*
$$BM = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

*Set MA = BM:*
$$\begin{pmatrix} a & a + b \\ c & c + d \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

*This gives:*
$a = a$ *(always true)*
$a + b = b \implies a = 0$
$c = c$ *(always true)*
$c + d = d \implies c = 0$

So $M = \begin{pmatrix} 0 & b \\ 0 & d \end{pmatrix}$.
But $\det(M) = 0 \cdot d - b \cdot 0 = 0$ for any choice of $b$ and $d$.
Thus no invertible matrix $M$ exists satisfying $MA = BM$.
Therefore, $A$ and $B$ are **NOT similar**.

## Page 3
**Summary**
* (a) Similar: $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
* (b) Similar: $M = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$
* (c) Not similar (no invertible $M$ exists)

**Exercise 1.2. Solution:**
(a) $\det(B) = \det(P^{-1}AP) = \det(P^{-1})\det(A)\det(P) = \frac{1}{\det(P)}\det(A)\det(P) = \det(A)$
(b) $\text{tr}(B) = \text{tr}(P^{-1}AP) = \text{tr}(APP^{-1}) = \text{tr}(A)$
(c) Characteristic polynomial: $p_B(\lambda) = \det(B - \lambda I) = \det(P^{-1}AP - \lambda I) = \det(P^{-1}(A - \lambda I)P) = \det(P^{-1})\det(A - \lambda I)\det(P) = \det(A - \lambda I) = p_A(\lambda)$
(d) Since they have the same characteristic polynomial, they have the same eigenvalues with the same algebraic multiplicities.

**Exercise 1.3.** $A = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 2 & 1 \\ -1 & 0 & 1 \end{pmatrix}$
**Solution:** First find eigenvalues by solving $\det(A - \lambda I) = 0$:
$$\det \begin{pmatrix} 2 - \lambda & 0 & 0 \\ 1 & 2 - \lambda & 1 \\ -1 & 0 & 1 - \lambda \end{pmatrix} = (2 - \lambda)[(2 - \lambda)(1 - \lambda) - 0] = (2 - \lambda)^2(1 - \lambda) = 0$$
So $\lambda = 2$ *(multiplicity 2)* and $\lambda = 1$ *(multiplicity 1)*.

For $\lambda = 2$: $(A - 2I)v = 0 \implies \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 1 \\ -1 & 0 & -1 \end{pmatrix} v = 0 \implies v_1 + v_3 = 0$, $v_2$ free. So eigenvectors:
$$v = \begin{pmatrix} -t \\ s \\ t \end{pmatrix} = s \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}$$

For $\lambda = 1$: $(A - I)v = 0 \implies \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ -1 & 0 & 0 \end{pmatrix} v = 0 \implies v_1 = 0, v_2 = -v_3$. So eigenvector: $v = \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix}$

We have 3 linearly independent eigenvectors, so $P = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 1 \end{pmatrix}$ and $D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
This diagonalization is not unique - we can scale eigenvectors or choose different bases for the eigenspaces.

**Exercise 1.4. Solution:** If $B = P^{-1}AP$, then $B^n = (P^{-1}AP)^n = P^{-1}A^nP$, so $A^n$ is similar to $B^n$.
For $A = \begin{pmatrix} 4 & 3 \\ -2 & -1 \end{pmatrix}$:
Find eigenvalues: $\det \begin{pmatrix} 4 - \lambda & 3 \\ -2 & -1 - \lambda \end{pmatrix} = (4 - \lambda)(-1 - \lambda) + 6 = \lambda^2 - 3\lambda + 2 = 0$. So $\lambda = 1, 2$.

For $\lambda = 1$: $\begin{pmatrix} 3 & 3 \\ -2 & -2 \end{pmatrix} v = 0 \implies v_1 = -v_2$, eigenvector $v_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$
For $\lambda = 2$: $\begin{pmatrix} 2 & 3 \\ -2 & -3 \end{pmatrix} v = 0 \implies 2v_1 + 3v_2 = 0$, eigenvector $v_2 = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$

$$P = \begin{pmatrix} 1 & 3 \\ -1 & -2 \end{pmatrix}, \quad P^{-1} = \begin{pmatrix} -2 & -3 \\ 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$$

## Page 4
$$A^{10} = P D^{10} P^{-1} = \begin{pmatrix} 1 & 3 \\ -1 & -2 \end{pmatrix} \begin{pmatrix} 1^{10} & 0 \\ 0 & 2^{10} \end{pmatrix} \begin{pmatrix} -2 & -3 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 3 \cdot 1024 \\ -1 & -2 \cdot 1024 \end{pmatrix} \begin{pmatrix} -2 & -3 \\ 1 & 1 \end{pmatrix}$$
$$= \begin{pmatrix} 1 - 3 \cdot 1024 & -3 + 3 \cdot 1024 \\ 2 - 2 \cdot 1024 & 3 - 2 \cdot 1024 \end{pmatrix} = \begin{pmatrix} 1 - 3072 & -3 + 3072 \\ 2 - 2048 & 3 - 2048 \end{pmatrix} = \begin{pmatrix} -3071 & 3069 \\ -2046 & -2045 \end{pmatrix}$$

**2 Eigenvalues and Eigenvectors - Solutions**

**Exercise 2.1.** 
(a) $A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ $\det(A - \lambda I) = (3 - \lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = 0 \implies \lambda = 4, 2$
For $\lambda = 4$: $\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} v = 0 \implies v_1 = v_2$, eigenvector $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
For $\lambda = 2$: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} v = 0 \implies v_1 = -v_2$, eigenvector $\begin{pmatrix} 1 \\ -1 \end{pmatrix}$

(b) $B = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}$ $\det(B - \lambda I) = (2 - \lambda)^2 + 1 = \lambda^2 - 4\lambda + 5 = 0 \implies \lambda = 2 \pm i$
For $\lambda = 2 + i$: $\begin{pmatrix} -i & -1 \\ 1 & -i \end{pmatrix} v = 0 \implies -i v_1 - v_2 = 0 \implies v_2 = -i v_1$, eigenvector $\begin{pmatrix} 1 \\ -i \end{pmatrix}$
For $\lambda = 2 - i$: $\begin{pmatrix} i & -1 \\ 1 & i \end{pmatrix} v = 0 \implies i v_1 - v_2 = 0 \implies v_2 = i v_1$, eigenvector $\begin{pmatrix} 1 \\ i \end{pmatrix}$

(c) $C = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}$ $\det(C - \lambda I) = (1 - \lambda)(2 - \lambda)(3 - \lambda) = 0 \implies \lambda = 1, 2, 3$
For $\lambda = 1$: Solve $(C - I)v = 0$, eigenvector $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$
For $\lambda = 2$: Solve $(C - 2I)v = 0$, eigenvector $\begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$
For $\lambda = 3$: Solve $(C - 3I)v = 0$, eigenvector $\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

**Exercise 2.2.** 
(a) **False**. Real matrices can have complex eigenvalues (e.g., rotation matrices).
(b) **False**. The sum of eigenvectors is an eigenvector only if they correspond to the same eigenvalue.
(c) **True**. If $Av = \lambda v$, then $A^2v = A(Av) = A(\lambda v) = \lambda Av = \lambda^2 v$.
(d) **True**. $\det(A^T - \lambda I) = \det((A - \lambda I)^T) = \det(A - \lambda I)$, so characteristic polynomials are equal.
(e) **True**. If $Av = \lambda v$ with $\lambda \neq 0$ and $A$ invertible, then $A^{-1}Av = A^{-1}(\lambda v) \implies v = \lambda A^{-1}v \implies A^{-1}v = \frac{1}{\lambda} v$.

**Exercise 2.3.** 
(a) If $Av = \lambda v$, then $A^2v = A(Av) = A(\lambda v) = \lambda Av = \lambda^2 v$. So $v$ is eigenvector of $A^2$ with eigenvalue $\lambda^2$.
(b) By induction, $A^kv = \lambda^k v$.
(c) For polynomial $p(t) = a_kt^k + \dots + a_1t + a_0$, $p(A)v = a_kA^kv + \dots + a_1Av + a_0v = (a_k\lambda^k + \dots + a_1\lambda + a_0)v = p(\lambda)v$.

**Exercise 2.4.** 
(a) $Av_1 = 1 \cdot v_1$, $Av_2 = 2v_2$, $Av_3 = 3v_3$
(b) $A^2v_1 = 1^2v_1 = v_1$
(c) $Au = 2Av_1 - Av_2 + 3Av_3 = 2v_1 - 2v_2 + 9v_3$
(d) Basis $\{v_1, v_2, v_3\}$ diagonalizes $A$ to $D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$

## Page 5
**3 Complex Vectors and Matrices - Solutions**

**Exercise 3.1.** $u = \begin{pmatrix} 1 + i \\ 2 - i \\ 3i \end{pmatrix}, v = \begin{pmatrix} 2 \\ 1 - i \\ 1 + 2i \end{pmatrix}, w = \begin{pmatrix} i \\ 1 \\ -i \end{pmatrix}$
(a) $u + v = \begin{pmatrix} 3 + i \\ 3 - 2i \\ 1 + 5i \end{pmatrix}$, $u - w = \begin{pmatrix} 1 \\ 1 - i \\ 4i \end{pmatrix}$, $2u - 3v = \begin{pmatrix} 2 + 2i - 6 \\ 4 - 2i - 3 + 3i \\ 6i - 3 - 6i \end{pmatrix} = \begin{pmatrix} -4 + 2i \\ 1 + i \\ -3 \end{pmatrix}$
(b) $\langle u, v \rangle = u^H v = \overline{(1 + i)}\cdot 2 + \overline{(2 - i)}\cdot (1 - i) + \overline{(3i)}\cdot (1 + 2i) = (1 - i)(2) + (2 + i)(1 - i) + (-3i)(1 + 2i)$
$= 2 - 2i + (2 + i - 2i - i^2) + (-3i - 6i^2) = 2 - 2i + (2 - i + 1) + (-3i + 6) = 2 - 2i + 3 - i + 6 - 3i = 11 - 6i$
(c) $\langle v, u \rangle = v^H u = \overline{\langle u, v \rangle} = 11 + 6i$. So $\langle v, u \rangle = \overline{\langle u, v \rangle}$.
(d) $\|u\|^2 = \langle u, u \rangle = (1 + i)(1 - i) + (2 - i)(2 + i) + (3i)(-3i) = 2 + 5 + 9 = 16$, so $\|u\| = 4$
$\|v\|^2 = 4 + (1 - i)(1 + i) + (1 + 2i)(1 - 2i) = 4 + 2 + 5 = 11$, so $\|v\| = \sqrt{11}$
$\|w\|^2 = (i)(-i) + 1 \cdot 1 + (-i)(i) = 1 + 1 + 1 = 3$, so $\|w\| = \sqrt{3}$
(e) $|\langle u, v \rangle| = \sqrt{11^2 + 6^2} = \sqrt{121 + 36} = \sqrt{157} \approx 12.53$
$\|u\| \|v\| = 4\sqrt{11} \approx 13.27$, so Cauchy-Schwarz holds: $12.53 \leq 13.27$.

**Exercise 3.2.** 
(a) $A = \begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix}$ $\det(A - \lambda I) = (1 - \lambda)^2 - i(-i) = (1 - \lambda)^2 - 1 = \lambda^2 - 2\lambda = \lambda(\lambda - 2) = 0$, so $\lambda = 0, 2$
For $\lambda = 0$: $\begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix} v = 0 \implies v_1 + iv_2 = 0$, eigenvector $\begin{pmatrix} i \\ -1 \end{pmatrix}$ or $\begin{pmatrix} 1 \\ i \end{pmatrix}$
For $\lambda = 2$: $\begin{pmatrix} -1 & i \\ -i & -1 \end{pmatrix} v = 0 \implies -v_1 + iv_2 = 0$, eigenvector $\begin{pmatrix} i \\ 1 \end{pmatrix}$

(b) $B = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$ $\det(B - \lambda I) = -\lambda^3 + 1 = 0 \implies \lambda^3 = 1$, so $\lambda = 1, e^{2\pi i/3}, e^{4\pi i/3}$
For $\lambda = 1$: $(B - I)v = 0$, eigenvector $\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$
For $\lambda = e^{2\pi i/3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$, eigenvector $\begin{pmatrix} 1 \\ \lambda \\ \lambda^2 \end{pmatrix}$
For $\lambda = e^{4\pi i/3} = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$, eigenvector $\begin{pmatrix} 1 \\ \lambda^2 \\ \lambda \end{pmatrix}$

(c) $C = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$ $\det(C - \lambda I) = (\cos \theta - \lambda)^2 + \sin^2 \theta = \lambda^2 - 2\cos\theta\lambda + 1 = 0$
$\lambda = \cos \theta \pm i \sin \theta = e^{\pm i\theta}$
Eigenvectors: $\begin{pmatrix} 1 \\ \mp i \end{pmatrix}$

**Exercise 3.3.** $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, B = \begin{pmatrix} 1 & i \\ 0 & 1 \end{pmatrix}$
(a) Both have eigenvalue $\lambda = 1$ with algebraic multiplicity 2.
(b) For $A$: $(A - I)v = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} v = 0 \implies v_2 = 0$, so eigenvectors are $\begin{pmatrix} t \\ 0 \end{pmatrix}$ *(only one direction)*
For $B$: $(B - I)v = \begin{pmatrix} 0 & i \\ 0 & 0 \end{pmatrix} v = 0 \implies iv_2 = 0 \implies v_2 = 0$, so eigenvectors are also $\begin{pmatrix} t \\ 0 \end{pmatrix}$
(c) Neither matrix is diagonalizable because each has only one linearly independent eigenvector (geometric multiplicity 1 < algebraic multiplicity 2).

## Page 6
(d) Both matrices are not diagonalizable over either field.

**Exercise 3.4.** 
(a) If $U = [u_1 \dots u_n]$, then $U^H U = I$ means $u_i^H u_j = \delta_{ij}$, so columns are orthonormal.
(b) $\|Ux\|^2 = (Ux)^H(Ux) = x^H U^H U x = x^H x = \|x\|^2$, so $\|Ux\| = \|x\|$.
(c) If $Uv = \lambda v$, then $\|Uv\| = |\lambda|\|v\|$. But $\|Uv\| = \|v\|$, so $|\lambda| = 1$.
(d) $U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$
Check $U^H U = \frac{1}{2} \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 + 1 & i - i \\ i - i & 1 + 1 \end{pmatrix} = I$
Eigenvalues: $\det(U - \lambda I) = 0 \implies (1/\sqrt{2} - \lambda)^2 - (i/\sqrt{2})(-i/\sqrt{2}) = \lambda^2 - \sqrt{2}\lambda + 1 = 0$
$\lambda = \frac{\sqrt{2} \pm i\sqrt{2}}{2} = \frac{1 \pm i}{\sqrt{2}}$, and indeed $|\lambda| = 1$.

**Exercise 3.5.** $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
(a) $A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$, $A^H = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$ *(same since A is real)*
(b) $(A^H)^H = A$ *(property of conjugate transpose)*
(c) $(AB)^H = B^H A^H$ *(property)*
(d) Hermitian matrix example: $\begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix}$

**4 Diagonalizable Matrices - Solutions**

**Exercise 4.1.** 
(a) $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$: Eigenvalues 3 and 2 *(distinct)* $\to$ diagonalizable
$P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$
(b) $B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$: Eigenvalue 2 *(multiplicity 2)* but only one eigenvector $\to$ NOT diagonalizable
(c) $C = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 2 & 0 \\ 1 & 0 & 3 \end{pmatrix}$: Eigenvalues 1, 2, 3 *(distinct)* $\to$ diagonalizable
Eigenvectors: $\lambda = 1 : \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$, $\lambda = 2 : \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$, $\lambda = 3 : \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$? Wait, need to compute carefully.
Actually for $\lambda = 1$: $(C - I)v = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 2 \end{pmatrix} v = 0 \implies v_1 + v_2 = 0, v_1 + 2v_3 = 0$, so $v = \begin{pmatrix} 2 \\ -2 \\ -1 \end{pmatrix}$
For $\lambda = 2$: $(C - 2I)v = \begin{pmatrix} -1 & 0 & 0 \\ 1 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix} v = 0 \implies v_1 = 0, v_3 = 0$, so $v = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$
For $\lambda = 3$: $(C - 3I)v = \begin{pmatrix} -2 & 0 & 0 \\ 1 & -1 & 0 \\ 1 & 0 & 0 \end{pmatrix} v = 0 \implies v_1 = 0, v_2 = 0$, so $v = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$
So $P = \begin{pmatrix} 2 & 0 & 0 \\ -2 & 1 & 0 \\ -1 & 0 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$

## Page 7
(d) $D = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$: Eigenvalue 2 *(multiplicity 3)* but only one eigenvector $\to$ NOT diagonalizable

**Exercise 4.2. Diagonalization Theorem:** An $n \times n$ matrix $A$ is diagonalizable iff it has $n$ linearly independent eigenvectors.
**Proof:** If $A$ has $n$ linearly independent eigenvectors $v_1, \dots, v_n$ with eigenvalues $\lambda_1, \dots, \lambda_n$, then let $P = [v_1 \dots v_n]$. Then $AP =[Av_1 \dots Av_n] = [\lambda_1v_1 \dots \lambda_nv_n] = P D$ where $D = \text{diag}(\lambda_1, \dots, \lambda_n)$. So $P^{-1}AP = D$.
Conversely, if $P^{-1}AP = D$ is diagonal, then the columns of $P$ are eigenvectors of $A$ and are linearly independent.
(a) Distinct eigenvalues guarantee $n$ linearly independent eigenvectors.
(b) Repeated eigenvalues can still have enough eigenvectors (e.g., identity matrix).
(c) Repeated eigenvalues may lead to a shortage of eigenvectors.

**Exercise 4.3.** 
(a) Yes, $A$ is diagonalizable because we have 3 linearly independent eigenvectors for a $3 \times 3$ matrix.
(b) $P = [v_1 v_2 v_3] = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$
(c) $A^5 = P D^5 P^{-1}$. First find $P^{-1}$: $\det(P) = 1(0 \cdot 1 - 1 \cdot 1) - 1(1 \cdot 1 - 1 \cdot 0) + 0 = -1 - 1 = -2$
$P^{-1} = -\frac{1}{2} \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix}^T = -\frac{1}{2} \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix}$
$D^5 = \begin{pmatrix} 32 & 0 & 0 \\ 0 & 32 & 0 \\ 0 & 0 & 243 \end{pmatrix}$
$$A^5 = -\frac{1}{2} \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 32 & 0 & 0 \\ 0 & 32 & 0 \\ 0 & 0 & 243 \end{pmatrix} \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix}$$

**Exercise 4.4.** $A = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}$
(a) $\det(A - \lambda I) = (4 - \lambda)^2 - 4 = \lambda^2 - 8\lambda + 12 = 0 \implies \lambda = 6, 2$
For $\lambda = 6$: $\begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix} v = 0 \implies v_1 = v_2$, eigenvector $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
For $\lambda = 2$: $\begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} v = 0 \implies v_1 = -v_2$, eigenvector $\begin{pmatrix} 1 \\ -1 \end{pmatrix}$
(b) $\begin{pmatrix} 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ -1 \end{pmatrix} = 1 - 1 = 0$, so they are orthogonal.
(c) Normalize eigenvectors: $q_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, q_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$
$Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad Q^T = Q^{-1}, \quad Q^T A Q = \begin{pmatrix} 6 & 0 \\ 0 & 2 \end{pmatrix}$
(d) A matrix must be symmetric ($A^T = A$) to be orthogonally diagonalizable over $\mathbb{R}$. Over $\mathbb{C}$, it must be normal ($AA^H = A^HA$).

**Exercise 4.5.** 
(a) Impossible - distinct eigenvalues guarantee diagonalizability.

## Page 8
(b) Possible: $A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$
(c) Possible: $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$
(d) Possible: Rotation matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $\pm i$, diagonalizable over $\mathbb{C}$.
(e) Impossible - a real matrix with complex eigenvalues is diagonalizable over $\mathbb{C}$, but over $\mathbb{R}$ it's not diagonalizable because eigenvectors would be complex.

**Exercise 4.6.** 
(a) If $A = P D P^{-1}$ with $D$ diagonal, then $p(A) = P p(D) P^{-1}$, and $p(D)$ is diagonal.
(b) Eigenvalues of $p(A)$ are $p(\lambda_1), \dots, p(\lambda_n)$.
(c) For $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, eigenvalues: $\lambda = 2, 3$
$p(2) = 8 - 4 + 1 = 5$, $p(3) = 27 - 6 + 1 = 22$
So $A^3 - 2A + I$ has eigenvalues 5 and 22, and is similar to $\begin{pmatrix} 5 & 0 \\ 0 & 22 \end{pmatrix}$.

**5 Challenge Problems - Solutions**

**Exercise 5.1. Proof:** Since $A$ and $B$ commute and are diagonalizable, they can be simultaneously diagonalized. First diagonalize $A$: $P^{-1}AP = D_A$ diagonal. Then $P^{-1}BP$ commutes with $D_A$, so it must be block diagonal with blocks corresponding to distinct eigenvalues of $A$. Within each block (where $A$ has a single eigenvalue), $B$ is diagonalizable, so we can diagonalize each block. The combination gives a matrix that diagonalizes both.

**Exercise 5.2.** 
(a) Let $w_i$ be the left eigenvectors (rows of $P^{-1}$). Then $A = P D P^{-1} = \sum_{i=1}^n \lambda_i v_i w_i^H$.
(b) $w_i$ are eigenvectors of $A^H$ with eigenvalues $\overline{\lambda_i}$.
(c) For $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$: $\lambda_1 = 3, v_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \lambda_2 = 1, v_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$, and $w_i = v_i$ *(since A is symmetric)*. Then $A = 3 v_1 v_1^T + 1 v_2 v_2^T$.

**Exercise 5.3.** 
(a) For $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$, characteristic polynomial $p(\lambda) = (\lambda - 2)^2 = \lambda^2 - 4\lambda + 4$
$p(A) = A^2 - 4A + 4I = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix} - \begin{pmatrix} 8 & 4 \\ 0 & 8 \end{pmatrix} + \begin{pmatrix} 4 & 0 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$
(b) For $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, characteristic polynomial $p(\lambda) = \lambda^2 - 4\lambda + 3$
$p(A) = 0 \implies A^2 - 4A + 3I = 0 \implies A(A - 4I) = -3I \implies A^{-1} = -\frac{1}{3}(A - 4I) = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$
(c) If $A = P D P^{-1}$, then $p(A) = P p(D) P^{-1}$. Since $p(\lambda_i) = 0$ for each eigenvalue $\lambda_i$, $p(D) = 0$, so $p(A) = 0$.

***

# File 2: Assignments

## Page 1
**Assignments**

**1 Similar Matrices**

**Exercise 1.1.** Determine whether the following pairs of matrices are similar. Justify your answer.
(a) $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}$
(b) $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$
(c) $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$

**Exercise 1.2.** Let $A$ and $B$ be similar matrices, i.e., $B = P^{-1}AP$ for some invertible matrix $P$.
Prove that:
(a) $\det(A) = \det(B)$
(b) $\text{tr}(A) = \text{tr}(B)$
(c) $A$ and $B$ have the same characteristic polynomial
(d) $A$ and $B$ have the same eigenvalues with the same multiplicities

**Exercise 1.3.** Find a matrix $P$ that diagonalizes $A$ and verify that $P^{-1}AP$ is diagonal:
$$A = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 2 & 1 \\ -1 & 0 & 1 \end{pmatrix}$$
Is this diagonalization unique? Explain.

**Exercise 1.4.** Show that if $A$ is similar to $B$, then $A^n$ is similar to $B^n$ for any positive integer $n$.
Use this to compute $A^{10}$ where:
$$A = \begin{pmatrix} 4 & 3 \\ -2 & -1 \end{pmatrix}$$
*(Hint: First show A is similar to a diagonal matrix)*

**2 Eigenvalues and Eigenvectors**

**Exercise 2.1.** Find all eigenvalues and corresponding eigenvectors for the following matrices:
(a) $A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$
(b) $B = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}$

## Page 2
(c) $C = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}$

**Exercise 2.2.** For each of the following statements, determine if it is true or false. If true, provide a proof. If false, give a counterexample.
(a) Every square matrix has at least one real eigenvalue.
(b) The sum of two eigenvectors of a matrix is always an eigenvector.
(c) If $\lambda$ is an eigenvalue of $A$, then $\lambda^2$ is an eigenvalue of $A^2$.
(d) A matrix and its transpose always have the same eigenvalues.
(e) If $A$ is invertible, then the eigenvalues of $A^{-1}$ are the reciprocals of the eigenvalues of $A$.

**Exercise 2.3.** Let $A$ be an $n \times n$ matrix with eigenvalue $\lambda$ and corresponding eigenvector $v$.
(a) Show that $v$ is also an eigenvector of $A^2$ and find its eigenvalue.
(b) Show that $v$ is also an eigenvector of $A^k$ for any positive integer $k$ and find its eigenvalue.
(c) Show that $v$ is also an eigenvector of any polynomial $p(A)$ where $p$ is a polynomial. If $p(\lambda)$ is the eigenvalue of $A$ for eigenvector $v$, what is the eigenvalue of $p(A)$ for the same eigenvector?

**Exercise 2.4.** Given that $A$ is a $3 \times 3$ matrix with eigenvalues $\lambda_1 = 1, \lambda_2 = 2, \lambda_3 = 3$ and corresponding eigenvectors $v_1, v_2, v_3$, solve:
(a) Find $Av_1$, $Av_2$, $Av_3$
(b) Find $A^2v_1$
(c) If $u = 2v_1 - v_2 + 3v_3$, compute $Au$
(d) Find a basis for which $A$ becomes diagonal. What is this diagonal matrix?

**3 Complex Vectors and Matrices**

**Exercise 3.1.** Consider the complex vectors:
$$u = \begin{pmatrix} 1 + i \\ 2 - i \\ 3i \end{pmatrix}, \quad v = \begin{pmatrix} 2 \\ 1 - i \\ 1 + 2i \end{pmatrix}, \quad w = \begin{pmatrix} i \\ 1 \\ -i \end{pmatrix}$$
(a) Compute $u + v$, $u - w$, and $2u - 3v$.
(b) Compute the standard inner product $\langle u, v \rangle = u^H v$ *(where $u^H$ is the conjugate transpose)*.
(c) Compute $\langle v, u \rangle$ and compare with $\langle u, v \rangle$. What do you notice?
(d) Compute the norms $\|u\|$, $\|v\|$, and $\|w\|$.
(e) Verify the Cauchy-Schwarz inequality for $u$ and $v$.

**Exercise 3.2.** For each of the following complex matrices, find all eigenvalues and eigenvectors:
(a) $A = \begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix}$

## Page 3
(b) $B = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$ *(complex entries allowed - find complex eigenvalues)*
(c) $C = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$ *(real matrix - find complex eigenvalues)*

**Exercise 3.3.** Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & i \\ 0 & 1 \end{pmatrix}$.
(a) Find the eigenvalues of $A$ and $B$.
(b) Find all eigenvectors of $A$ and $B$.
(c) Is $A$ diagonalizable? Is $B$ diagonalizable? Explain.
(d) What do you notice about the relationship between diagonalizability and the field (real vs complex)?

**Exercise 3.4.** A matrix $U$ is called unitary if $U^H U = I$, where $U^H$ is the conjugate transpose.
(a) Show that the columns of a unitary matrix form an orthonormal basis in $\mathbb{C}^n$.
(b) Show that if $U$ is unitary, then $\|Ux\| = \|x\|$ for all vectors $x$ *(unitary matrices preserve length)*.
(c) Show that all eigenvalues of a unitary matrix have modulus 1 (i.e., $|\lambda| = 1$).
(d) Verify that $U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ is unitary and find its eigenvalues.

**Exercise 3.5.** For the matrix $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, find:
(a) $A^H$ (conjugate transpose) and $A^T$ (transpose). Are they the same? Why or why not?
(b) Show that $(A^H)^H = A$
(c) Show that $(AB)^H = B^H A^H$ for any matrices $A, B$ of compatible sizes
(d) A matrix is called Hermitian if $A^H = A$. Give an example of a $2 \times 2$ Hermitian matrix with complex entries.

**4 Diagonalizable Matrices**

**Exercise 4.1.** Determine whether each of the following matrices is diagonalizable. If so, find an invertible matrix $P$ and a diagonal matrix $D$ such that $P^{-1}AP = D$.
(a) $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$
(b) $B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$
(c) $C = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 2 & 0 \\ 1 & 0 & 3 \end{pmatrix}$
(d) $D = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$

## Page 4
**Exercise 4.2.** State and prove the Diagonalization Theorem: An $n \times n$ matrix $A$ is diagonalizable if and only if it has $n$ linearly independent eigenvectors.
Use this theorem to explain why:
(a) A matrix with $n$ distinct eigenvalues is always diagonalizable.
(b) A matrix can have repeated eigenvalues and still be diagonalizable.
(c) A matrix with a repeated eigenvalue may fail to be diagonalizable.

**Exercise 4.3.** Given that $A$ is a $3 \times 3$ matrix with eigenvalues $\lambda = 2, 2, 3$ and eigenvectors:
$$v_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad v_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \quad v_3 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$
(a) Is $A$ diagonalizable? Why or why not?
(b) If diagonalizable, find matrices $P$ and $D$ such that $A = P D P^{-1}$.
(c) Compute $A^5$ using this diagonalization.

**Exercise 4.4.** Let $A = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}$.
(a) Find the eigenvalues and eigenvectors of $A$.
(b) Verify that eigenvectors corresponding to distinct eigenvalues are orthogonal.
(c) Find an orthogonal matrix $Q$ *(i.e., $Q^T = Q^{-1}$)* that diagonalizes $A$.
(d) This is called orthogonal diagonalization. What special property must a matrix have to be orthogonally diagonalizable?

**Exercise 4.5.** For each of the following, find a matrix $A$ with the given properties or explain why it's impossible:
(a) A $2 \times 2$ matrix with eigenvalues 2 and 3 that is not diagonalizable.
(b) A $3 \times 3$ matrix with eigenvalues 1, 1, 2 that is diagonalizable.
(c) A $3 \times 3$ matrix with eigenvalues 1, 1, 2 that is NOT diagonalizable.
(d) A $2 \times 2$ matrix with no real eigenvalues that is diagonalizable over $\mathbb{C}$.
(e) A $2 \times 2$ matrix with no real eigenvalues that is diagonalizable over $\mathbb{R}$.

**Exercise 4.6.** Suppose $A$ is diagonalizable and $p(t)$ is a polynomial.
(a) Show that $p(A)$ is also diagonalizable.
(b) If $A$ has eigenvalues $\lambda_1, \dots, \lambda_n$, what are the eigenvalues of $p(A)$?
(c) Use this to compute $A^3 - 2A + I$ for $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ without directly multiplying matrices.

## Page 5
**5 Challenge Problems**

**Exercise 5.1.** Prove that if $A$ and $B$ are diagonalizable and they commute ($AB = BA$), then they are simultaneously diagonalizable, i.e., there exists an invertible matrix $P$ such that $P^{-1}AP$ and $P^{-1}BP$ are both diagonal.

**Exercise 5.2.** Let $A$ be an $n \times n$ matrix with $n$ linearly independent eigenvectors $v_1, \dots, v_n$ and corresponding eigenvalues $\lambda_1, \dots, \lambda_n$.
(a) Show that $A$ can be written as $A = \sum_{i=1}^n \lambda_i v_i w_i^H$, where $w_i$ are appropriately chosen vectors. *(This is called the spectral decomposition.)*
(b) What are the vectors $w_i$ in terms of the eigenvectors of $A^H$?
(c) Verify this decomposition for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.

**Exercise 5.3.** The Cayley-Hamilton theorem states that every matrix satisfies its own characteristic equation.
(a) Verify the Cayley-Hamilton theorem for $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
(b) Use the Cayley-Hamilton theorem to find $A^{-1}$ as a polynomial in $A$ for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
(c) For a diagonalizable matrix, explain why the Cayley-Hamilton theorem is true.

***

# File 3: Why the Inner Product Over Complex Spaces Requires Conjugation

## Page 1
**Why the Inner Product Over Complex Spaces Requires Conjugation**

The definition of an inner product on a vector space over the complex field $\mathbb{C}$ includes a subtle but crucial modification compared to the real case: **conjugate symmetry** (also called Hermitian symmetry). Instead of the real condition $\langle x, y \rangle = \langle y, x \rangle$, the complex inner product must satisfy:
$$\langle x, y \rangle = \overline{\langle y, x \rangle}$$
where $\overline{z}$ denotes the complex conjugate. This requirement is not arbitrary; it is necessary to preserve the fundamental properties of an inner product, primarily **positive definiteness** and the consistent definition of a **norm**.

**1 Preserving Positive Definiteness**

The most important reason for conjugation is to ensure that the inner product of a vector with itself is always a real, non-negative number. This is the property of **positive definiteness**:
$$\langle x, x \rangle \ge 0 \quad \text{and} \quad \langle x, x \rangle = 0 \iff x = 0.$$

If we attempted to define a complex inner product without conjugation (i.e., using a standard bilinear form over $\mathbb{C}$), we would run into contradictions. Consider the standard complex vector space $\mathbb{C}^n$. A naive bilinear form might be $B(x, y) = \sum_{i=1}^n x_i y_i$. For a non-zero vector like $x = (1, i)$, we would obtain:
$$B(x, x) = 1 \cdot 1 + i \cdot i = 1 + i^2 = 1 - 1 = 0.$$

This yields zero for a non-zero vector, violating the definiteness condition. Worse, the result could even be a complex number, making it impossible to interpret as a "length" or to compare magnitudes.

By introducing conjugation—turning the form into a **sesquilinear** form—we ensure $\langle x, x \rangle$ is always real. Using the standard Hermitian inner product $\langle x, y \rangle = \sum_{i=1}^n x_i \overline{y_i}$, the same vector $x = (1, i)$ gives:
$$\langle x, x \rangle = 1 \cdot \overline{1} + i \cdot \overline{i} = 1 \cdot 1 + i \cdot (-i) = 1 + 1 = 2 > 0,$$
which is exactly the squared Euclidean norm.

## Page 2
**2 Ensuring a Consistent Norm**

A natural geometric requirement is that scaling a vector by a complex scalar $\alpha$ should scale its length (norm) by $|\alpha|$, the modulus of the scalar. If the inner product is to define the norm as $\|x\| = \sqrt{\langle x, x \rangle}$, we need:
$$\|\alpha x\|^2 = \langle \alpha x, \alpha x \rangle = |\alpha|^2 \langle x, x \rangle.$$

This property forces the inner product to be **conjugate linear** in the first argument (if linearity is chosen in the second) or vice-versa. The standard convention in physics and mathematics is to have the inner product linear in the second argument and conjugate-linear in the first (though conventions vary; the key is the presence of conjugation).

**3 Natural Extension of $\mathbb{C}$ as a Module over Itself**

Even in the simplest case—the complex numbers themselves as a one-dimensional vector space over $\mathbb{C}$—the need for conjugation is apparent. We want the "inner product" of a number with itself to give the squared magnitude. The natural choice is:
$$\langle z, w \rangle = z \overline{w}.$$

This yields $\langle z, z \rangle = |z|^2$, which is real and positive for $z \neq 0$. The alternative, $zw$, would give $z^2$, which is not necessarily real and does not represent a length.

**4 Conclusion**

The conjugate in the complex inner product is not a mere formality; it is the essential ingredient that extends the geometric concept of "angle" and "length" from real spaces to complex spaces. It guarantees that:
* $\langle x, x \rangle$ is real and positive for $x \neq 0$.
* The induced norm behaves correctly under scalar multiplication.
* The inner product aligns with the natural modulus on $\mathbb{C}$.

Without conjugation, the structure would be a bilinear form, which is useful in other contexts (e.g., complex bilinear forms in physics), but it would lack the positive-definite metric properties required for a true inner product space.

***

# File 4: Matrices and Vectors over the Complex Field (Presentation Slides)
*(Note: Animated slides building up to the same final content have been consolidated into single slides to avoid redundancy while preserving 100% of the text.)*

## Slide 1 (Page 1)
**Matrices and Vectors over the Complex Field**
Salman Ahmadi-Asl
Innopolis University
March 13, 2026
*(Footer appearing on all subsequent slides: Salman Ahmadi-Asl (Innopolis University) | Complex Matrices and Vectors | March 13, 2026)*

## Slide 2 (Page 2)
**Outline**
1. Introduction and Motivation
2. Complex Vectors ($\mathbb{C}^n$)
3. Complex Matrices ($\mathbb{C}^{m \times n}$)
4. Special Classes of Complex Matrices
5. Matrix Subspaces and Rank
6. Eigenvalues and Diagonalization
7. Summary

## Slide 3 (Pages 3-9 consolidated)
**Why the Complex Field?**
* **Algebraic Closure:** Every polynomial $p(\lambda) = 0$ has $n$ roots in $\mathbb{C}$.
  * Guarantees eigenvalues for *every* matrix.
* **Physics and Engineering:**
  * Quantum Mechanics (wave functions, operators).
  * AC Circuit Analysis (phasors, impedance).
  * Signal Processing (Fourier transforms).
* **Mathematical Elegance:** Spectral Theorem and Unitary Diagonalization are cleaner in $\mathbb{C}^n$.

## Slide 4 (Pages 10-12 consolidated)
**Complex Vectors: Definition and Operations**
**Definition**
A complex vector $\mathbf{v} \in \mathbb{C}^n$ is an ordered $n$-tuple of complex numbers:
$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}, \quad v_i \in \mathbb{C}$$

**Basic Operations:**
* **Addition:** $(v_i) + (w_i) = (v_i + w_i)$
* **Scalar Multiplication:** $\alpha \mathbf{v} = (\alpha v_i), \alpha \in \mathbb{C}$

**Example**
Let $\mathbf{v} = \begin{bmatrix} 2 + i \\ -3i \end{bmatrix}, \mathbf{w} = \begin{bmatrix} 1 - i \\ 2 \end{bmatrix}, \alpha = 2i$.
$$\mathbf{v} + \mathbf{w} = \begin{bmatrix} (2 + i) + (1 - i) \\ -3i + 2 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 - 3i \end{bmatrix}$$

## Slide 5 (Page 13)
**Example**
$$\alpha \mathbf{v} = \begin{bmatrix} 2i(2 + i) \\ 2i(-3i) \end{bmatrix} = \begin{bmatrix} 4i + 2i^2 \\ -6i^2 \end{bmatrix} = \begin{bmatrix} -2 + 4i \\ 6 \end{bmatrix},$$

## Slide 6 (Pages 14-15 consolidated)
**The Complex Inner Product**
**Definition (Hermitian Inner Product)**
For $\mathbf{x}, \mathbf{y} \in \mathbb{C}^n$, the inner product is:
$$\langle \mathbf{x}, \mathbf{y} \rangle = \sum_{i=1}^n x_i \overline{y_i}$$
**Note:** Conjugation on the second argument is crucial.

**Key Properties**
1. **Conjugate Symmetry:** $\langle \mathbf{x}, \mathbf{y} \rangle = \overline{\langle \mathbf{y}, \mathbf{x} \rangle}$
2. **Linearity in first argument:** $\langle \alpha \mathbf{x}, \mathbf{y} \rangle = \alpha \langle \mathbf{x}, \mathbf{y} \rangle$
3. **Conjugate linearity in second:** $\langle \mathbf{x}, \alpha \mathbf{y} \rangle = \overline{\alpha} \langle \mathbf{x}, \mathbf{y} \rangle$
4. **Positive Definiteness:** $\langle \mathbf{x}, \mathbf{x} \rangle \ge 0$ and equals 0 iff $\mathbf{x} = \mathbf{0}$

## Slide 7 (Pages 16-18 consolidated)
**Norm, Distance, and Orthogonality**
**Definition (Euclidean Norm)**
$$\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle} = \left( \sum_{i=1}^n |v_i|^2 \right)^{1/2}$$

**Example**
For $\mathbf{v} = \begin{bmatrix} 1 + i \\ 2 - i \end{bmatrix}$:
$$\|\mathbf{v}\| = \sqrt{|1 + i|^2 + |2 - i|^2}$$
$$= \sqrt{(1^2 + 1^2) + (2^2 + (-1)^2)}$$
$$= \sqrt{2 + 5} = \sqrt{7}$$

**Definition (Orthogonality)**
$\mathbf{x} \perp \mathbf{y}$ iff $\langle \mathbf{x}, \mathbf{y} \rangle = 0$.

## Slide 8 (Pages 19-22 consolidated)
**Linear Dependence and Basis**
* Linear independence is defined the same as in $\mathbb{R}^n$:
  $\sum \alpha_i \mathbf{v}_i = \mathbf{0} \implies \alpha_i = 0$ for all $i$.
* A set of $n$ linearly independent vectors forms a **basis** for $\mathbb{C}^n$.
* **Gram-Schmidt Process** works in $\mathbb{C}^n$, but uses the complex inner product.

**Important Note**
While $\mathbb{R}^n$ and $\mathbb{C}^n$ share similar vector space properties, the underlying field changes the geometry. Orthonormal bases in $\mathbb{C}^n$ satisfy $\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij}$.

## Slide 9 (Pages 23-24 consolidated)
**Complex Matrices: Basic Definitions**
**Definition**
A complex matrix $A \in \mathbb{C}^{m \times n}$ has entries $a_{ij} \in \mathbb{C}$.

**Example**
$$A = \begin{bmatrix} 2 + i & 0 & 3i \\ 1 & -i & 4 - 2i \end{bmatrix} \in \mathbb{C}^{2 \times 3}$$

**Standard Operations:**
* Addition and Scalar Multiplication (component-wise)
* Matrix Multiplication: $(AB)_{ik} = \sum_{j=1}^n A_{ij}B_{jk}$

## Slide 10 (Pages 25-26 consolidated)
**The Conjugate Transpose (Hermitian Adjoint)**
**Definition**
For $A \in \mathbb{C}^{m \times n}$, the **Hermitian adjoint** $A^* \in \mathbb{C}^{n \times m}$ is:
$$(A^*)_{ij} = \overline{A_{ji}}$$
(Transpose + Complex Conjugate)

**Example**
Let $A = \begin{bmatrix} 1 & i & 2 \\ 1 - i & 0 & 3i \end{bmatrix}_{2 \times 3}.$
$$A^* = \begin{bmatrix} 1 & \overline{1 - i} \\ \overline{i} & \overline{0} \\ \overline{2} & \overline{3i} \end{bmatrix} = \begin{bmatrix} 1 & 1 + i \\ -i & 0 \\ 2 & -3i \end{bmatrix}_{3 \times 2}$$

## Slide 11 (Pages 27-32 consolidated)
**Properties of the Adjoint**
For matrices $A, B$ of appropriate sizes and $\alpha \in \mathbb{C}$:
* $(A^*)^* = A$
* $(A + B)^* = A^* + B^*$
* $(\alpha A)^* = \overline{\alpha}A^*$
* $(AB)^* = B^*A^*$ (Reversal rule)
* If $A$ is invertible, $(A^{-1})^* = (A^*)^{-1}$
* $\langle A\mathbf{x}, \mathbf{y} \rangle = \langle \mathbf{x}, A^* \mathbf{y} \rangle$

## Slide 12 (Pages 33-34 consolidated)
**Hermitian Matrices ($A = A^*$)**
**Definition**
A square matrix $A$ is **Hermitian** if $A = A^*$.

**Example**
$$H = \begin{bmatrix} 1 & 2 + i & 3 \\ 2 - i & 4 & i \\ 3 & -i & 0 \end{bmatrix}$$
Notice: Diagonal entries are real ($\overline{a_{ii}} = a_{ii}$).

**Theorem (Properties of Hermitian Matrices)**
1. All eigenvalues are **real**.
2. Eigenvectors corresponding to distinct eigenvalues are *orthogonal*.
3. $A$ is *unitarily diagonalizable*.

## Slide 13 (Page 35)
**Theorem 1: All Eigenvalues are Real**
**Proof.**
Let $\lambda$ be an eigenvalue of $A$ with corresponding eigenvector $\mathbf{v} \neq \mathbf{0}$:
$$A\mathbf{v} = \lambda\mathbf{v}$$
Consider the inner product $\langle \mathbf{v}, A\mathbf{v} \rangle$ in two ways:
$$\langle \mathbf{v}, A\mathbf{v} \rangle = \langle \mathbf{v}, \lambda\mathbf{v} \rangle = \lambda \langle \mathbf{v}, \mathbf{v} \rangle = \lambda \|\mathbf{v}\|^2$$
$$\langle \mathbf{v}, A\mathbf{v} \rangle = \langle A^*\mathbf{v}, \mathbf{v} \rangle = \langle A\mathbf{v}, \mathbf{v} \rangle \quad \text{(since } A^* = A \text{)}$$
$$= \langle \lambda\mathbf{v}, \mathbf{v} \rangle = \overline{\lambda} \langle \mathbf{v}, \mathbf{v} \rangle = \overline{\lambda} \|\mathbf{v}\|^2$$

Equating both expressions:
$$\lambda \|\mathbf{v}\|^2 = \overline{\lambda} \|\mathbf{v}\|^2$$
Since $\|\mathbf{v}\|^2 \neq 0$, we have $\lambda = \overline{\lambda}$, which means $\lambda \in \mathbb{R}$.

## Slide 14 (Pages 36-37 consolidated)
**Theorem 2: Orthogonal Eigenvectors**
**Proof.**
Let $\lambda$ and $\mu$ be distinct eigenvalues of $A$ with corresponding eigenvectors $\mathbf{v}$ and $\mathbf{w}$:
$$A\mathbf{v} = \lambda\mathbf{v}, \quad A\mathbf{w} = \mu\mathbf{w}, \quad \lambda \neq \mu$$
Consider the inner product $\langle A\mathbf{v}, \mathbf{w} \rangle$:
$$\langle A\mathbf{v}, \mathbf{w} \rangle = \langle \lambda\mathbf{v}, \mathbf{w} \rangle = \overline{\lambda} \langle \mathbf{v}, \mathbf{w} \rangle$$
$$\langle A\mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{v}, A^*\mathbf{w} \rangle = \langle \mathbf{v}, A\mathbf{w} \rangle \quad \text{(since } A^* = A \text{)}$$
$$= \langle \mathbf{v}, \mu\mathbf{w} \rangle = \mu \langle \mathbf{v}, \mathbf{w} \rangle$$

Equating both expressions:
$$\overline{\lambda} \langle \mathbf{v}, \mathbf{w} \rangle = \mu \langle \mathbf{v}, \mathbf{w} \rangle$$
From Theorem 1, $\mu$ is real, so $\overline{\mu} = \mu$. Thus:
$$\lambda \langle \mathbf{v}, \mathbf{w} \rangle = \mu \langle \mathbf{v}, \mathbf{w} \rangle$$
$$(\lambda - \mu)\langle \mathbf{v}, \mathbf{w} \rangle = 0$$
Since $\lambda \neq \mu$, we must have $\langle \mathbf{v}, \mathbf{w} \rangle = 0$, i.e., $\mathbf{v}$ and $\mathbf{w}$ are orthogonal.

## Slide 15 (Page 38)
**Theorem 3: Unitary Diagonalization (Part 1)**
**Theorem**
*Every Hermitian matrix $A \in \mathbb{C}^{n \times n}$ is unitarily diagonalizable. That is, there exists a unitary matrix $U$ ($U^* U = I$) and a real diagonal matrix $\Lambda$ such that:*
$$A = U \Lambda U^*$$

**Proof (by induction on n).**
**Base case:** $n = 1$ is trivially true (a $1 \times 1$ Hermitian matrix is a real number).
**Inductive step:** Assume the theorem holds for all Hermitian matrices of size $(n - 1) \times (n - 1)$. Consider $A \in \mathbb{C}^{n \times n}$ Hermitian.

## Slide 16 (Page 39)
**Theorem 3: Unitary Diagonalization (Part 2)**
**Proof (continued).**
1. By Theorem 1, $A$ has at least one real eigenvalue $\lambda_1$ with corresponding unit eigenvector $\mathbf{u}_1$ ($\|\mathbf{u}_1\| = 1$).
2. Extend $\{\mathbf{u}_1\}$ to an orthonormal basis $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ of $\mathbb{C}^n$. Let $U_1 =[\mathbf{u}_1 \; \mathbf{u}_2 \; \dots \; \mathbf{u}_n]$ be the unitary matrix with these vectors as columns.
3. Consider $U_1^* A U_1$. Since $U_1$ is unitary, this matrix is Hermitian:
$$(U_1^* A U_1)^* = U_1^* A^* U_1 = U_1^* A U_1$$

## Slide 17 (Page 40)
**Theorem 3: Unitary Diagonalization (Part 3)**
**Proof (continued).**
4. Compute the first column of $U_1^* A U_1$:
$$(U_1^* A U_1)_{j1} = \mathbf{u}_j^* A \mathbf{u}_1 = \mathbf{u}_j^*(\lambda_1 \mathbf{u}_1) = \lambda_1 \mathbf{u}_j^* \mathbf{u}_1$$
$$= \lambda_1 \langle \mathbf{u}_j, \mathbf{u}_1 \rangle = \lambda_1 \delta_{j1}$$

This means:
$$U_1^* A U_1 = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & & & \\ \vdots & & A_{n-1} & \\ 0 & & & \end{pmatrix}$$
where $A_{n-1}$ is an $(n-1) \times (n-1)$ Hermitian matrix.

## Slide 18 (Page 41)
**Theorem 3: Unitary Diagonalization (Part 4)**
**Proof (continued).**
5. By the induction hypothesis, $A_{n-1}$ is unitarily diagonalizable. There exists a unitary matrix $V$ of size $(n-1) \times (n-1)$ such that:
$$V^* A_{n-1} V = \text{diag}(\lambda_2, \dots, \lambda_n)$$
6. Construct the block diagonal matrix:
$$U_2 = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & & & \\ \vdots & & V & \\ 0 & & & \end{pmatrix}$$
which is clearly unitary.

## Slide 19 (Page 42)
**Theorem 3: Unitary Diagonalization (Part 5)**
**Proof (completed).**
7. Let $U = U_1 U_2$. Then $U$ is unitary (product of unitary matrices). Compute:
$$U^* A U = (U_1 U_2)^* A (U_1 U_2)$$
$$= U_2^* (U_1^* A U_1) U_2$$
$$= U_2^* \begin{pmatrix} \lambda_1 & 0 \\ 0 & A_{n-1} \end{pmatrix} U_2$$
$$= \begin{pmatrix} 1 & 0 \\ 0 & V^* \end{pmatrix} \begin{pmatrix} \lambda_1 & 0 \\ 0 & A_{n-1} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & V \end{pmatrix}$$
$$= \begin{pmatrix} \lambda_1 & 0 \\ 0 & V^* A_{n-1} V \end{pmatrix}$$
$$= \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n) = \Lambda$$
Thus $A = U \Lambda U^*$, completing the proof by induction.

## Slide 20 (Pages 43-44 consolidated)
**Unitary Matrices ($U^* = U^{-1}$)**
**Definition**
$U \in \mathbb{C}^{n \times n}$ is **unitary** if $U^* = U^{-1}$, i.e.:
$$U U^* = U^* U = I$$

**Example (A 2x2 Unitary Matrix)**
$$U = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & i \\ i & 1 \end{bmatrix}$$
Check: $U^* = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -i \\ -i & 1 \end{bmatrix}$
$$U U^* = \frac{1}{2} \begin{bmatrix} 1 \cdot 1 + i \cdot (-i) & 1 \cdot (-i) + i \cdot 1 \\ i \cdot 1 + 1 \cdot (-i) & i \cdot (-i) + 1 \cdot 1 \end{bmatrix} = I$$

## Slide 21 (Pages 45-50 consolidated)
**Properties of Unitary Matrices**
* Columns of $U$ form an orthonormal basis in $\mathbb{C}^n$.
* Rows of $U$ also form an orthonormal basis.
* **Preserves inner product:** $\langle U\mathbf{x}, U\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$
* **Preserves norm:** $\|U\mathbf{x}\| = \|\mathbf{x}\|$
* All eigenvalues $|\lambda| = 1$ lie on the unit circle.
* $|\det(U)| = 1$.

## Slide 22 (Page 51)
**Inner Product Preservation**
**Theorem**
*Unitary matrices preserve the inner product. For any $\mathbf{x}, \mathbf{y} \in \mathbb{C}^n$:*
$$\langle U\mathbf{x}, U\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$$

**Proof.**
Using the definition of inner product and properties of conjugate transpose:
$$\langle U\mathbf{x}, U\mathbf{y} \rangle = (U\mathbf{x})^* (U\mathbf{y})$$
$$= \mathbf{x}^* U^* U \mathbf{y}$$
$$= \mathbf{x}^* (U^* U) \mathbf{y}$$
$$= \mathbf{x}^* I \mathbf{y} \quad \text{(since } U \text{ is unitary)}$$
$$= \mathbf{x}^* \mathbf{y} = \langle \mathbf{x}, \mathbf{y} \rangle$$

## Slide 23 (Page 52)
**Norm Preservation**
**Theorem**
*Unitary matrices preserve the Euclidean norm (length). For any $\mathbf{x} \in \mathbb{C}^n$:*
$$\|U\mathbf{x}\| = \|\mathbf{x}\|$$

**Proof.**
This follows directly from inner product preservation:
$$\|U\mathbf{x}\|^2 = \langle U\mathbf{x}, U\mathbf{x} \rangle$$
$$= \langle \mathbf{x}, \mathbf{x} \rangle \quad \text{(by Property 3)}$$
$$= \|\mathbf{x}\|^2$$
Taking square roots (both sides are non-negative real numbers) gives $\|U\mathbf{x}\| = \|\mathbf{x}\|$.

## Slide 24 (Page 53)
**Eigenvalues Lie on Unit Circle**
**Theorem**
*If $\lambda$ is an eigenvalue of a unitary matrix $U$, then $|\lambda| = 1$.*

**Proof.**
Let $\lambda$ be an eigenvalue with corresponding eigenvector $\mathbf{v} \neq \mathbf{0}$:
$$U\mathbf{v} = \lambda\mathbf{v}$$
Take norms of both sides:
$$\|U\mathbf{v}\| = \|\lambda\mathbf{v}\|$$
$$\|\mathbf{v}\| = |\lambda| \|\mathbf{v}\| \quad \text{(by Property 4)}$$
Since $\|\mathbf{v}\| \neq 0$, we can divide both sides by $\|\mathbf{v}\|$ to obtain:
$$1 = |\lambda|$$
Thus $\lambda = e^{i\theta}$ for some $\theta \in \mathbb{R}$, lying on the unit circle in the complex plane.

## Slide 25 (Page 54)
**Determinant Has Unit Modulus**
**Theorem**
*For any unitary matrix $U$, $|\det(U)| = 1$.*

**Proof.**
Using properties of determinants and conjugate transposes:
$$|\det(U)|^2 = \det(U) \cdot \overline{\det(U)}$$
$$= \det(U) \cdot \det(\overline{U})$$
$$= \det(U) \cdot \det(U^T)$$
$$= \det(U) \cdot \det(U^*) \quad \text{(since } U^* = \overline{U}^T \text{)}$$
$$= \det(U U^*)$$
$$= \det(I) \quad \text{(since } U \text{ is unitary)}$$
$$= 1$$
Taking square roots, $|\det(U)| = 1$ (determinant could be any complex number on the unit circle).

## Slide 26 (Pages 55-56 consolidated)
**Four Fundamental Subspaces (Complex Case)**
For $A \in \mathbb{C}^{m \times n}$:
**Row Space:** $\mathcal{R}(A^*) \subset \mathbb{C}^n$
**Nullspace:** $\mathcal{N}(A) \subset \mathbb{C}^n$
**Column Space:** $\mathcal{R}(A) \subset \mathbb{C}^m$
**Left Nullspace:** $\mathcal{N}(A^*) \subset \mathbb{C}^m$

**Theorem (Fundamental Theorem of Linear Algebra)**
* $\mathcal{N}(A) = \mathcal{R}(A^*)^\perp \text{ in } \mathbb{C}^n$
* $\mathcal{N}(A^*) = \mathcal{R}(A)^\perp \text{ in } \mathbb{C}^m$
* $\dim \mathcal{R}(A) = \dim \mathcal{R}(A^*) = \text{rank}(A)$

## Slide 27 (Pages 57-59 consolidated)
**Eigenvalues in $\mathbb{C}$: Always Exist!**
**Definition**
$\lambda \in \mathbb{C}$ is an eigenvalue of $A$ if $\exists \mathbf{v} \neq \mathbf{0}$ such that:
$$A\mathbf{v} = \lambda\mathbf{v}$$

**Key Difference from $\mathbb{R}$**
Over $\mathbb{C}$, the characteristic polynomial $\det(A - \lambda I) = 0$ always has $n$ roots (counting multiplicity) by the Fundamental Theorem of Algebra.
**Every complex matrix has at least one eigenvalue!**

**Example (Rotation matrix has no real eigenvalues)**
$R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ in $\mathbb{R}^2$ has no real eigenvalues, but in $\mathbb{C}^2$:
$$\lambda = i, -i$$

## Slide 28 (Pages 60-62 consolidated)
**Diagonalization**
**Definition**
$A$ is **diagonalizable** if there exists an invertible matrix $P$ such that:
$$P^{-1}AP = \Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$$

**Criteria:**
* $A$ has $n$ linearly independent eigenvectors.
* Algebraic multiplicity = Geometric multiplicity for each eigenvalue.

**Unitary Diagonalization**
If $A$ is **normal**, then we can choose $P$ to be **unitary**:
$$A = U \Lambda U^*$$

## Slide 29 (Pages 63-71 consolidated)
**Applications**
1. **Quantum Mechanics:**
   * States are vectors in $\mathbb{C}^n$ (Hilbert space).
   * Observables are Hermitian operators (real eigenvalues).
   * Evolution is unitary ($U(t) = e^{-iHt/\hbar}$).
2. **Signal Processing:**
   * Fourier matrix is unitary.
   * DFT and FFT algorithms.
3. **Control Theory:**
   * Stability of systems via eigenvalue analysis.

## Slide 30 (Page 72)
**Summary: Real vs Complex**

| Concept | Real Field ($\mathbb{R}$) | Complex Field ($\mathbb{C}$) |
| :--- | :--- | :--- |
| Vector Space | $\mathbb{R}^n$ | $\mathbb{C}^n$ |
| Inner Product | $\mathbf{x}^T \mathbf{y}$ | $\mathbf{x}^* \mathbf{y} = \sum x_i \overline{y_i}$ |
| Norm | $\sqrt{\sum x_i^2}$ | $\sqrt{\sum |x_i|^2}$ |
| Transpose | $A^T$ | $A^*$ (Conjugate transpose) |
| Symmetric | $A^T = A$ | Hermitian $A^* = A$ |
| Orthogonal | $Q^T = Q^{-1}$ | Unitary $U^* = U^{-1}$ |
| Eigenvalues | May not exist | Always exist |

**Takeaway:** Conjugation is the key to preserving structure!

## Slide 31 (Page 73)
**Further Reading**[1] Gilbert Strang, *Linear Algebra and Its Applications*, 4th ed.
[2] Hoffman and Kunze, *Linear Algebra*, 2nd ed.
[3] Horn and Johnson, *Matrix Analysis*, 2nd ed.

## Slide 32 (Page 74)
**Thank You!**
Questions?

***

# File 5: Matrices and vectors over the Complex Field (Tasks and Solutions)

## Page 1
**Matrices and vectors over the Complex Field**
* Complex vectors
* Complex matrices
* Special classes of complex matrices

## Page 2
**TASK 1**
Add and multiply each pair of complex numbers
(a) $2 + i, 2 - i$
(b) $-1 + i, -1 + i$
(c) $\cos\theta + i\sin\theta, \cos\theta - i\sin\theta$

## Page 3
**SOLUTION**
*The computations are:*
(a) $(2+i)(2-i) = 4 - 2i + 2i - i^2 = 4 - (-1) = 5$
(b) $(-1+i)(-1+i) = 1 - i - i + i^2 = 1 - 2i + (-1) = -2i$
(c) The long way:
$(\cos\theta + i\sin\theta)(\cos\theta - i\sin\theta) = \cos^2\theta - i\cos\theta\sin\theta + i\sin\theta\cos\theta + \sin^2\theta = \cos^2\theta + \sin^2\theta = 1$
The short way:
$e^{i\theta}e^{-i\theta} = e^{i(\theta-\theta)} = e^{i0} = e^0 = 1$

## Page 4
**TASK 2**
(a) The sum $z + \bar{z}$ is always:
(b) The difference $z - \bar{z}$ is always
(c) The product $z \cdot \bar{z}$ is
(d) The ratio $z / \bar{z}$ always ($\bar{z} \neq 0$) has absolute value:

## Page 5
**SOLUTION**
In the following exercises let $z = a + ib$.
(a) $z + \bar{z} = (a+ib) + (a-ib) = 2a = 2\text{Re}(z)$
(b) $z - \bar{z} = (a+ib) - (a-ib) = 2ib = 2i\text{Im}(z)$
(c) $z \bar{z} = (a+ib)(a-ib) = a^2 - iab + iab - i^2b^2 = a^2 - (-1)b^2 = a^2 + b^2 = \|z\|^2$
(d) $\frac{z}{\bar{z}} = \frac{a+ib}{a-ib} = \frac{a+ib}{a-ib} \frac{a+ib}{a+ib} = \frac{z^2}{\|z\|^2}$

## Page 6
**TASK 3**
Find the lengths of $u, v \in \mathbb{C}^3$. Also find $u^H v$ and $v^H u$.
$$u = \begin{pmatrix} 1+i \\ 1-i \\ 1+2i \end{pmatrix} \quad v = \begin{pmatrix} i \\ i \\ i \end{pmatrix}$$

## Page 7
**SOLUTION**
To find the length we recall that:
$\bar{u}^T u = (1-i \quad 1+i \quad 1-2i) \begin{pmatrix} 1+i \\ 1-i \\ 1+2i \end{pmatrix} = 9 = \|u\|^2$
$\bar{v}^T v = (-i \quad -i \quad -i) \begin{pmatrix} i \\ i \\ i \end{pmatrix} = 3 = \|v\|^2$
$u^H v = (1-i \quad 1+i \quad 1-2i) \begin{pmatrix} i \\ i \\ i \end{pmatrix} = 2 + 3i$
$v^H u = (-i \quad -i \quad -i) \begin{pmatrix} 1+i \\ 1-i \\ 1+2i \end{pmatrix} = 2 - 3i$

## Page 8
**TASK 4**
Which classes of matrices does the matrix $P$ belong to? (Hermitian, invertible, unitary?)
$$P = \begin{pmatrix} 0 & i & 0 \\ 0 & 0 & i \\ i & 0 & 0 \end{pmatrix}$$
Compute $P^2$, $P^3$, and $P^{100}$.

## Page 9
**SOLUTION**
Is $P$ Hermitian? **No!** Since $P \neq P^H$:
$\begin{pmatrix} 0 & i & 0 \\ 0 & 0 & i \\ i & 0 & 0 \end{pmatrix} = P \neq P^H = \bar{P}^T = - \begin{pmatrix} 0 & 0 & i \\ i & 0 & 0 \\ 0 & i & 0 \end{pmatrix} = -i \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$

Is $P$ invertible? **Yes!** $P$ has a nonzero determinant, namely, $\det(P) = -i \neq 0$.

Is $P$ unitary? **Yes!** Since $P^H = P^{-1}$:
$P^{-1} = -i \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = \bar{P}^T = P^H$

## Page 10
*(Картинка: Рукописные вычисления матричных степеней)*
**Транскрипт изображения:**
For the computations we have:
$$P^2 = \begin{pmatrix} 0 & i & 0 \\ 0 & 0 & i \\ i & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & i & 0 \\ 0 & 0 & i \\ i & 0 & 0 \end{pmatrix} = - \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$
$$P^3 = - \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & i & 0 \\ 0 & 0 & i \\ i & 0 & 0 \end{pmatrix} = -i I$$
To compute $P^{100}$ we have
$$P^{100} = P^{99} \cdot P = (P^3)^{33} \cdot P = (-i I)^{33} P$$
$$= (-1)^{33} (i)^{33} I P = (-1) i P = -i P$$

## Page 11
**TASK 5**
Diagonalize $B$ to prove that the following formula.
$$B = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} \quad B^k = \begin{pmatrix} 3^k & 3^k - 2^k \\ 0 & 2^k \end{pmatrix}$$

## Page 12
**SOLUTION**
As in our previous computations, we have: $\text{tr}(B) = 5$ and $\det(B) = 6$
$\lambda_{1,2} = \frac{1}{2}(\text{tr}(A) \pm \sqrt{\text{tr}^2(A) - 4\det(A)})$
$\lambda_{1,2} = \frac{1}{2}(5 \pm \sqrt{25 - 6 \cdot 4}) = \frac{1}{2}(5 \pm 1) = 3, 2$

For $\lambda = 2$:
$(A - \lambda I)x = 0 \to (A - 2I)x = 0 \to \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} x = 0 \to x + y = 0$
$(x, y) = (-y, y) = y(-1, 1) \to v = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$

For $\lambda = 3$:
$(A - \lambda I)x = 0 \to (A - 3I)x = 0 \to \begin{pmatrix} 0 & 1 \\ 0 & -1 \end{pmatrix} x = 0 \to 0x + y = 0$
$(x, y) = (x, 0) = x(1, 0) \to v = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

## Page 13
*(Картинка: Рукописные вычисления диагонализации и матричных степеней)*
**Транскрипт изображения:**
Therefore, we have $S = \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}$, $\Lambda = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$, $S^{-1} = -1 \begin{pmatrix} 0 & -1 \\ -1 & -1 \end{pmatrix}$
To compute $A^k$:
$A^k = (S\Lambda S^{-1})^k = \underbrace{(S\Lambda S^{-1})(S\Lambda S^{-1}) \dots (S\Lambda S^{-1})}_{k \text{ times}}$ *(with brackets showing $S^{-1}S$ cancelling to $I$)*
$$= S\Lambda^k S^{-1}$$
$$= \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2^k & 0 \\ 0 & 3^k \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} -2^k & 3^k \\ 2^k & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 3^k & 3^k - 2^k \\ 0 & 2^k \end{pmatrix}$$

## Page 14
**TASK 6**
Choose the second row of $A$ so that $A$ has eigenvalues $4$ and $7$.
$$A = \begin{pmatrix} 1 & 1 \\ \Box & \Box \end{pmatrix}$$

## Page 15
**SOLUTION**
Let $a$ and $b$ be the elements of the second row. The trace and the determinant of $A$ are $1+b$ and $b-a$ respectively. Then on the one hand we have
$$\lambda^2 - \text{tr}(A)\lambda + \det(A) = \lambda^2 - (1+b)\lambda + (b-a)$$
on the other hand we know that
$$(\lambda-4)(\lambda-7) = \lambda^2 - 7\lambda - 4\lambda + 28 = \lambda^2 - 11\lambda + 28$$
so this means $-(1+b) = -11$ and $b-a = 28$. These two equations lead to the values $b=10$ and $a=-18$.

## Page 16
**TASK 7**
Find the matrix $A$ whose eigenvalues are $1$ and $4$ and whose eigenvectors are $(3, 1)^T$ and $(2, 1)^T$, respectively.

## Page 17
**SOLUTION**
We know that diagonalizing a matrix consists in $A = S \Lambda S^{-1}$.
In our case we have:
$$S = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} \quad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix} \quad S^{-1} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}$$
so this is
$$A = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix} \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}$$
$$= \begin{pmatrix} 3 & 8 \\ 1 & 4 \end{pmatrix} \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}$$
$$= \begin{pmatrix} -5 & 18 \\ -3 & 10 \end{pmatrix}$$

## Page 18
**TASK 8**
If $x = r e^{i\theta}$ what are $x^2, x^{-1}$, and $\bar{x}$ in polar coordinates? Where are the complex numbers that have $x^{-1} = \bar{x}$?

## Page 19
*(Картинка: Рукописный текст и чертеж окружности в Декартовой системе координат)*
**Транскрипт изображения:**
$x^2 = r^2 e^{2i\theta}$
$x^{-1} = r^{-1} e^{-i\theta}$
$\bar{x} = r e^{-i\theta}$
(Нарисована декартова система координат с окружностью единичного радиуса с центром в начале координат (0,0). В первой четверти надпись синими чернилами: $x^{-1} = \bar{x}$. Возле оси x стоит отметка 1).

## Page 20
**TASK 9**
Write out the matrix $A^H$ and compute $C = A^H A$ if
$$A = \begin{bmatrix} 1 & i & 0 \\ i & 0 & 1 \end{bmatrix}$$
What is the relation between $C$ and $C^H$?

## Page 21
**SOLUTION**
**1. Given matrix $A$**
$$A = \begin{bmatrix} 1 & i & 0 \\ i & 0 & 1 \end{bmatrix}$$
We want $A^H$, which is the conjugate transpose: take transpose, then complex conjugate each entry.
* Transpose of $A$:
$$A^T = \begin{bmatrix} 1 & i \\ i & 0 \\ 0 & 1 \end{bmatrix}$$
* Now conjugate each entry: $\bar{i} = -i$, others real unchanged.
$$A^H = \overline{A^T} = \begin{bmatrix} 1 & -i \\ -i & 0 \\ 0 & 1 \end{bmatrix}$$
So: $A^H = \begin{bmatrix} 1 & -i \\ -i & 0 \\ 0 & 1 \end{bmatrix}$

## Page 22
**2. Compute $C = A^H A$**
We have:
$A^H (3 \times 2), \quad A (2 \times 3) \implies C (3 \times 3)$
$$C = A^H A$$
**First row of $A^H$ times columns of $A$:**
Row 1: $[1, -i]$
* Column 1 of $A$: $\begin{bmatrix} 1 \\ i \end{bmatrix}$
  $1 \cdot 1 + (-i) \cdot i = 1 - i^2 = 1 - (-1) = 2$
* Column 2 of $A$: $\begin{bmatrix} i \\ 0 \end{bmatrix}$
  $1 \cdot i + (-i) \cdot 0 = i$
* Column 3 of $A$: $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$
  $1 \cdot 0 + (-i) \cdot 1 = -i$
So first row of $C$: $[2, i, -i]$

**Second row of $A^H$: $[-i, 0]$**
* Col 1: $(-i) \cdot 1 + 0 \cdot i = -i$
* Col 2: $(-i) \cdot i + 0 \cdot 0 = -i^2 = 1$
* Col 3: $(-i) \cdot 0 + 0 \cdot 1 = 0$
Second row of $C$: $[-i, 1, 0]$

**Third row of $A^H$: $[0, 1]$**
* Col 1: $0 \cdot 1 + 1 \cdot i = i$
* Col 2: $0 \cdot i + 1 \cdot 0 = 0$
* Col 3: $0 \cdot 0 + 1 \cdot 1 = 1$
Third row of $C$: $[i, 0, 1]$

## Page 23
**3. Relation between $C$ and $C^H$**
$C^H =$ conjugate transpose of $C$.
First, note $C$ has:
* Real diagonal: $2, 1, 1$
* Off-diagonal terms: $C_{12} = i$, $C_{13} = -i$, $C_{21} = -i$, $C_{31} = i$, $C_{23} = 0$, $C_{32} = 0$

Take conjugate:
$\bar{i} = -i$
$\overline{-i} = i$
So $\overline{C_{12}} = -i = C_{21}$
$\overline{C_{13}} = i = C_{31}$
$\overline{C_{21}} = i = C_{12}$
$\overline{C_{31}} = -i = C_{13}$

That is: $\overline{C_{ij}} = C_{ji}$ for all $i, j$.
In other words:
$$C^H = C$$
because $C$ is Hermitian.

## Page 24
**TASK 10**
$$A = \begin{bmatrix} 1 & i & 0 \\ i & 0 & 1 \end{bmatrix}$$
a) With the preceding $A$, use elimination to solve $Ax = 0$.
b) Show that the nullspace you just computed is orthogonal to $C(A^H)$ and not the usual row space $C(A^T)$. The four fundamental spaces in the complex case are $N(A)$ and $C(A)$ as before, and then $N(A^H)$ and $C(A^H)$

## Page 25
**SOLUTION**
**1. Problem setup**
Given:
$$A = \begin{bmatrix} 1 & i & 0 \\ i & 0 & 1 \end{bmatrix}$$
We want $Ax = 0$, so:
$$\begin{cases} x_1 + i x_2 = 0 \\ i x_1 + 0 x_2 + x_3 = 0 \end{cases}$$
where $x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$.

## Page 26
**2. Elimination (use complex numbers as scalars)**
Write augmented matrix:
$$\begin{bmatrix} 1 & i & 0 & | & 0 \\ i & 0 & 1 & | & 0 \end{bmatrix}$$
Eliminate below first pivot 1:
Multiply first row by $-i$ and add to second row? Let's check:
First equation: $x_1 + i x_2 = 0 \to x_1 = -i x_2$.
Second equation: $i x_1 + x_3 = 0$. Substitute $x_1 = -i x_2$:
$$i(-i x_2) + x_3 = 0$$
$$-i^2 x_2 + x_3 = -(-1)x_2 + x_3 = x_2 + x_3 = 0$$
Thus $x_3 = -x_2$.
So:
$$x_1 = -i x_2, \quad x_3 = -x_2$$
with $x_2$ free variable.

## Page 27
**Nullspace vector:**
Take $x_2 = 1$, then:
$$x_1 = -i, \quad x_3 = -1$$
$$\mathbf{n} = \begin{bmatrix} -i \\ 1 \\ -1 \end{bmatrix}$$
General solution: $x = t \begin{bmatrix} -i \\ 1 \\ -1 \end{bmatrix}, t \in \mathbb{C}.$

**Nullspace:**
$$N(A) = \left\{ t \begin{bmatrix} -i \\ 1 \\ -1 \end{bmatrix} \mid t \in \mathbb{C} \right\}$$

## Page 28
**3. Part (b) Orthogonality with $C(A^H)$**
Recall $A^H$ is the conjugate transpose of $A$.
From earlier problem:
$$A^H = \begin{bmatrix} 1 & -i \\ -i & 0 \\ 0 & 1 \end{bmatrix}$$
Columns of $A^H$ span $C(A^H)$:
$$C(A^H) = \text{span} \left\{ \begin{bmatrix} 1 \\ -i \\ 0 \end{bmatrix}, \begin{bmatrix} -i \\ 0 \\ 1 \end{bmatrix} \right\}$$
Check orthogonal condition: $N(A) \perp C(A^H)$ means:
$$\mathbf{n}^H \mathbf{c} = 0$$
for any $\mathbf{c} \in C(A^H)$.

## Page 29
Take $\mathbf{n} = \begin{bmatrix} -i \\ 1 \\ -1 \end{bmatrix}$, compute $\mathbf{n}^H$ (conjugate transpose):
$$\mathbf{n}^H = \begin{bmatrix} i & 1 & -1 \end{bmatrix}$$
(Note: $\overline{-i} = i$, $\bar{1} = 1$, $\overline{-1} = -1$).
Dot with $\mathbf{c}_1 = \begin{bmatrix} 1 \\ -i \\ 0 \end{bmatrix}$:
$$\mathbf{n}^H \mathbf{c}_1 = i \cdot 1 + 1 \cdot (-i) + (-1) \cdot 0 = i - i + 0 = 0$$
Dot with $\mathbf{c}_2 = \begin{bmatrix} -i \\ 0 \\ 1 \end{bmatrix}$:
$$\mathbf{n}^H \mathbf{c}_2 = i \cdot (-i) + 1 \cdot 0 + (-1) \cdot 1 = -i^2 - 1 = -(-1) - 1 = 1 - 1 = 0$$
Yes, $\mathbf{n} \perp$ both basis vectors of $C(A^H) \implies N(A) \perp C(A^H)$.

## Page 30
**4. Orthogonal to $C(A^T)$?**
$$A^T = \begin{bmatrix} 1 & i \\ i & 0 \\ 0 & 1 \end{bmatrix}$$
$$C(A^T) = \text{span} \left\{ \begin{bmatrix} 1 \\ i \\ 0 \end{bmatrix}, \begin{bmatrix} i \\ 0 \\ 1 \end{bmatrix} \right\}$$
Check $\mathbf{n}^H$ with $\mathbf{r}_1 = \begin{bmatrix} 1 \\ i \\ 0 \end{bmatrix}$:
$$\mathbf{n}^H \mathbf{r}_1 = i \cdot 1 + 1 \cdot i + (-1) \cdot 0 = i + i = 2i \neq 0$$
So $\mathbf{n}$ is NOT orthogonal to the first basis vector of $C(A^T) \implies$ not orthogonal to $C(A^T)$ in general.
Thus: In complex case, $N(A)$ is orthogonal to $C(A^H)$, not $C(A^T)$.

## Page 31
**TASK 11**
Show that $A$ and $B$ are similar by finding $M$ so that $B = M^{-1}AM$:
a) $A = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$
b) $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$
c) $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & 3 \\ 2 & 1 \end{bmatrix}$.

## Page 32
**SOLUTION**
**1)** $A = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$
Let $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ with $ad - bc \neq 0$. Then
$$AM = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} a & b \\ a & b \end{bmatrix},$$
$$MB = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix}.$$
Equating $AM = MB$:
$$\begin{bmatrix} a & b \\ a & b \end{bmatrix} = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix}$$
gives $b = 0$ and $a = c$.
Choose $a = 1, d = 1$. Then
$$M = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \quad M^{-1} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}.$$
Verification:
$$M^{-1} A M = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = B.$$

## Page 33
**2)** $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$
Let $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. Then
$$AM = \begin{bmatrix} a + c & b + d \\ a + c & b + d \end{bmatrix},$$
$$MB = \begin{bmatrix} a - b & -a + b \\ c - d & -c + d \end{bmatrix}.$$
Equating:
$$\begin{cases} a + c = a - b \\ b + d = -a + b \\ a + c = c - d \\ b + d = -c + d \end{cases}$$

## Page 34
From first: $c = -b$. From second: $d = -a$. The last two are consistent.
Choose $a = 1, b = 0$, then $c = 0, d = -1$. So
$$M = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} = M^{-1}.$$
Verification:
$$M^{-1} A M = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = B.$$

## Page 35
**3)** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 4 & 3 \\ 2 & 1 \end{bmatrix}$
Observe that $B$ is obtained from $A$ by reversing the order of rows and columns, i.e.,
$$B = PAP, \quad \text{where } P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}.$$
Since $P = P^{-1}$, we have $B = P^{-1}AP$. So
$$M = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}.$$
Verification:
$$PA = \begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix}, \quad (PA)P = \begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 4 & 3 \\ 2 & 1 \end{bmatrix} = B.$$