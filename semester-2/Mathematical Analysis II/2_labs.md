


Вот полный построчный транскрипт предоставленных файлов на английском языке. Весь текст, включая математические формулы, перенесён с сохранением структуры. Так как в файлах отсутствуют графики, фотографии или схемы (контент состоит исключительно из текста и формул), описания картинок не требуются, но визуальные элементы (например, цветные блоки) переданы через соответствующее форматирование.

***

# File 1: Mathematical Analysis (MA) II – Lab 6

## Page 1

**Mathematical Analysis (MA) II**  
**Lab 6 Tasks**

1. Find and sketch the domain for each function:
   (a) $f(x, y) = \sqrt{y - x - 2}$
   (b) $f(x, y) = \ln(x^2 + y^2 - 4)$
   (c) $f(x, y, z) = \sqrt{4 - x^2} + \sqrt{9 - y^2} + \sqrt{1 - z^2}$

2. Sketch the level curve $z = k$ for the specified values of k:
   (a) $z = f(x, y) = x + y - 1, \quad k = -2, -1, 0, 1, 2.$
   (b) $z = f(x, y) = \frac{y}{x}, \quad k = -2, -1, 0, 1, 2.$
   (c) $z = f(x, y) = x^2 - y^2, \quad k = -2, -1, 0, 1, 2.$

3. Find the following limits:
   (a) $\lim_{(x,y) \to (\infty,3)} \frac{2x - 3}{x^3 + 4y^3}$
   (b) $\lim_{(x,y) \to (0,0)} \frac{x - y + 2\sqrt{x} - 2\sqrt{y}}{\sqrt{x} - \sqrt{y}}, \quad x \neq y$
   (c) $\lim_{(x,y) \to (0,0)} \frac{1 - \cos(xy)}{xy}$

4. Show that the following functions have no limit as $(x, y) \to (0, 0)$:
   (a) $f(x, y) = -\frac{x}{\sqrt{x^2 + y^2}}$
   (b) $f(x, y) = \frac{x^4 - y^2}{x^4 + y^2}$

5. Define $f(0, 0)$ in a way that extends $f(x, y) = xy \frac{x^2 - y^2}{x^2 + y^2}$ to be continuous at the origin $(0, 0)$.

*(Page number at the bottom: 1)*

---

## Page 2

**Homework**

1. Find and sketch the domain for each function:
   (a) $f(x, y) = \frac{\sin(xy)}{x^2 + y^2 - 25}$
   (b) $f(x, y, z) = \ln(16 - 4x^2 - 4y^2 - z^2)$

2. Sketch the level curve $z = k$ for the specified values of k:
   (a) $z = f(x, y) = x^2 + y^2, \quad k = 0, 1, 2, 3, 4.$
   (b) $z = f(x, y) = x^2 + 9y^2, \quad k = 0, 1, 2, 3, 4.$

3. Find the following limits:
   (a) $\lim_{(x,y) \to (2,-4)} \frac{y + 4}{x^2y - xy + 4x^2 - 4x}, \quad y \neq -4, \, x \neq x^2$
   (b) $\lim_{(x,y) \to (2,0)} \frac{\sqrt{2x - y - 2}}{2x - y - 4}, \quad 2x - y \neq 4$
   (c) $\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2}$
   (d) $\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^4 + y^2}$

4. Show that the following functions have no limit as $(x, y) \to (0, 0)$:
   (a) $f(x, y) = \frac{xy}{|xy|}$
   (b) $f(x, y) = \frac{x^2 - y}{x - y}$

5. Test the following functions for continuity:
   (a) $f(x, y) = \begin{cases} \frac{x^3 - y^3}{x^2 + y^2}, & \text{when } x \neq 0, y \neq 0 \\ 0, & \text{when } x = 0, y = 0 \end{cases}$
   (b) $f(x, y) = \begin{cases} \frac{xy(x^2 - y^2)}{x^2 + y^2}, & \text{when } x \neq 0, y \neq 0 \\ 0, & \text{when } x = 0, y = 0 \end{cases}$
   (c) $f(x, y) = \begin{cases} \frac{x}{\sqrt{x^2 + y^2}}, & \text{when } x \neq 0, y \neq 0 \\ 2, & \text{when } x = 0, y = 0 \end{cases}$

*(Page number at the bottom: 2)*

***

# File 2: Lab 7 – Functions of Several Variables

## Slide 1
*Header: Limits | Partial Derivatives; Directional Derivatives and Gradients*

**Lab7: Functions of Several Variables**

**Math Analysis (II)**

Innopolis University  
March 04, 2026

*Footer: Math Analysis (II) | Lab 7*

---

## Slide 2
*Header: Limits | Partial Derivatives; Directional Derivatives and Gradients*

**Contents**

1. Limits
2. Partial Derivatives; Directional Derivatives and Gradients

*Footer: Math Analysis (II) | Lab 7*

---

## Slide 3
*Header: Limits | Partial Derivatives; Directional Derivatives and Gradients*

**Limits**

**Task 1.1** Evaluate  
$$ \lim_{(x,y) \to (0,0)} \sqrt{x^2 + y^2} \ln(x^2 + y^2). $$

**Task 1.2** Evaluate  
$$ \lim_{(x,y) \to (0,0)} \frac{x^2 y^2}{\sqrt{x^2 + y^2}}. $$

**Task 1.3** Study the existence of the limit at $(0, 0, 0)$ of  
$$ f(x, y, z) = \frac{xyz}{x + y + z}. $$

**Task 1.4** Study the existence of the limit at $(2, -2, 0)$ of  
$$ f(x, y, z) = \frac{x + y}{x^2 - y^2 + z^2}. $$

*Footer: Math Analysis (II) | Lab 7*

---

## Slide 4
*Header: Limits | Partial Derivatives; Directional Derivatives and Gradients*

**Partial Derivatives; Directional Derivatives and Gradients**

**Task 2.1** Compute $f_x, f_y, f_{xx}, f_{yy}$ for  
$$ f(x, y) = \ln(x^2 y + 2xy + 5). $$

**Task 2.2** For  
$$ f(x, y) = x^3 e^{-y} + y^3 \sec(\sqrt{x}), \quad x > 0, $$  
compute $f_x, f_y$.

**Task 2.3** For  
$$ f(x, y) = (y^2 \tan x)^{-4/3}, \quad \tan x \neq 0, \, y \neq 0, $$  
compute $f_x, f_y$.

**Task 2.4** Determine whether each function is harmonic:  
(a) $f = x^3 + 3xy^2$, \quad (b) $f = \sin x \cosh y + \cos x \sinh y$, \quad (c) $f = \ln \sqrt{x^2 + y^2}$.

**Task 2.5** If $z = \sin x \sin y, x = \sqrt{t}, y = 1/t$, compute $\frac{dz}{dt}$.

**Task 2.6** If $f(x, y, z) = x e^{2x - y} + yz + e^{xz}$ and  
$$ x(t) = t^2, \quad y(t) = \sin t, \quad z(t) = e^{-t}, $$  
compute $\frac{d}{dt} f(x(t), y(t), z(t))$.

*Footer: Math Analysis (II) | Lab 7*

---

## Slide 5
*Header: Limits | Partial Derivatives; Directional Derivatives and Gradients*

**Partial Derivatives; Directional Derivatives and Gradients**

**Task 2.7** From $x e^y + \sin(xy) + y - \ln 2 = 0$, compute  
$$ \left. \frac{dy}{dx} \right|_{(0, \ln 2)}. $$

**Task 2.8** If $F(x, y, z) = x e^{yz} + y^2 z - 3 = 0$ defines $z(x, y)$, compute $z_x, z_y$.

**Task 2.9** For $f(x, y) = \sqrt{x^2 + 4y^2}$, find the slope at $(1, 2)$ toward $(2, 1)$.

*Footer: Math Analysis (II) | Lab 7*

***

# File 3: Lab 8 – Functions of Several Variables

## Slide 1

**Mathematical Analysis (MA) II**  
**Functions of Several Variables**

Ikechi Ndukwe

Lab 8  
(March 11, 2026)

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 1 / 14*

---

## Slide 2

**Objectives**

*   Recap
*   Find Functions from Partial Derivatives
*   Extreme Values of Multivariable Functions
*   Homework

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 2 / 14*

---

## Slide 3

**Gradients (Recap)**

The **gradient vector (gradient)** of $f(x, y)$ at a point $P_0(x_0, y_0)$ is  
$$ \nabla f = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} $$  
obtained by evaluating the partial derivatives of $f$ at $P_0$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 3 / 14*

---

## Slide 4

**Directional Derivative Is a Dot Product (Recap)**

If $f(x, y)$ is differentiable in an open region containing $P_0(x_0, y_0)$, then  
$$ \left( \frac{df}{ds} \right)_{\mathbf{u}, P_0} = (\nabla f)_{P_0} \cdot \mathbf{u}, $$  
$$ D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} $$  
the dot product of the gradient $\nabla f$ at $P_0$ and $\mathbf{u}$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 4 / 14*

---

## Slide 5

**Exercise**

1. Find the slope at point $(1, 1, 1)$ in the direction of vector $(1, 2, 2)$ on the function $f = x^2 + y^2 + z^2$
2. For $f(x, y) = \cos\left(\frac{x}{y}\right)$, find $D_{\vec{u}} f$ in the direction of $\vec{v} = \langle 3, -4 \rangle$.
3. Find the directional derivative of $f(x, y) = 4x^3 - 3xy^2$ in the direction given by the angle $\theta = \frac{\pi}{3}$. Then, evaluate it at the point $(1, 2)$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 5 / 14*

---

## Slide 6

**Finding Functions from Partial Derivatives**

To find function $f(x, y)$ from its partial derivatives $(f_x, f_y)$:
*   **i.** Integrate $f_x$ w.r.t $x$
*   **ii.** Add $C(y)$
*   **iii.** Differentiate $f$ obtained from steps i & ii w.r.t $y$, and compare with the given $f_y$ to find $C(y)$.

Alternatively, do the following:
*   **i.** Integrate $f_y$ w.r.t $y$
*   **ii.** Add $C(x)$
*   **iii.** Differentiate $f$ obtained from steps i & ii w.r.t $x$, and compare with the given $f_x$ to find $C(x)$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 6 / 14*

---

## Slide 7

**Exercises**

4. Find $f(x, y)$ for the following partial derivatives:
   **a.** $f_x = 2x + y, \quad f_y = x + 4y$
   **b.** $f_x = 3x^2 y^2 - 2x, \quad f_y = 2x^3 y + 6y$
   **c.** $f_x = xy \cos(xy) + \sin(xy), \quad f_y = x^2 \cos(xy)$

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 7 / 14*

---

## Slide 8

**Extreme Values of Multivariable Functions**

Let $f(x, y)$ be defined on a region $R$ containing the point $(a, b)$. Then
**a.** $f(a, b)$ is a **local maximum** value of $f$ if $f(a, b) \geq f(x, y)$ for all domain points $(x, y)$ in an open disk centered at $(a, b)$.
**b.** $f(a, b)$ is a **local minimum** value of $f$ if $f(a, b) \leq f(x, y)$ for all domain points $(x, y)$ in an open disk centered at $(a, b)$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 8 / 14*

---

## Slide 9

**First Derivative Test for Local Extreme Values**

If $f(x, y)$ has a local maximum or minimum value at an interior point $(a, b)$ of its domain and if the first partial derivatives exist there, then  
$f_x(a, b) = 0$ and $f_y(a, b) = 0$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 9 / 14*

---

## Slide 10

**Definitions**

> **Critical Point**  *(Оформлено на слайде в виде зелёного информационного блока)*
> An interior point of the domain of a function $f(x, y)$ where both $f_x$ and $f_y$ are zero or where one or both of $f_x$ and $f_y$ do not exist is a **critical point** of $f$.

> **Saddle Point**  *(Оформлено на слайде в виде зелёного информационного блока)*
> A differentiable function $f(x, y)$ has a **saddle point** at a critical point $(a, b)$ if in every open disk centered at $(a, b)$ there are domain points $(x, y)$ where $f(x, y) > f(a, b)$ and domain points $(x, y)$ where $f(x, y) < f(a, b)$.

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 10 / 14*

---

## Slide 11

**Second Derivative Test for Local Extreme Values**

Suppose that $f(x, y)$ and its first and second partial derivatives are continuous throughout a disk centered at $(a, b)$ and that  
$f_x(a, b) = f_y(a, b) = 0$. Then
**a.** $f$ has a **local maximum** at $(a, b)$ if $f_{xx} < 0$ and $D > 0$ at $(a, b)$.
**b.** $f$ has a **local minimum** at $(a, b)$ if $f_{xx} > 0$ and $D > 0$ at $(a, b)$.
**c.** $f$ has a **saddle point** at $(a, b)$ if $D < 0$ at $(a, b)$.
**d.** The test is **inconclusive** at $(a, b)$ if $D = 0$ at $(a, b)$. In this case, we must find some other way to determine the behavior of $f$ at $(a, b)$.

The expression $D = f_{xx}f_{yy} - f_{xy}^2$ is called the **discriminant** or **Hessian** of $f$. It is sometimes easier to remember it in determinant form,  
$$ D = f_{xx}f_{yy} - f_{xy}^2 = \begin{vmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{vmatrix}. $$

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 11 / 14*

---

## Slide 12

**Exercises**

5. Find and classify the critical points of the following functions:
   **a.** $f(x, y) = x^3 - 3x + y^3 - 3y$
   **b.** $f(x, y) = 2x^3 + 2y^3 - 9x^2 + 3y^2 - 12y$
   **c.** $f(x, y) = 10xy e^{-(x^2 + y^2)}$

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 12 / 14*

---

## Slide 13

**Homework**

1. Determine $D_{\vec{u}} f(3, -1, 0)$ for $f(x, y, z) = 4x - y^2 e^{3xz}$ in the direction of $\vec{v} = \langle -1, 4, 2 \rangle$.
2. Find and classify the critical points of the following functions:
   **a.** $f(x, y) = x^2 - y^3 - 3xy + 2x$
   **b.** $f(x, y) = x^4 + y^4 - 4xy + 1$

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 13 / 14*

---

## Slide 14

**Thank You**

*Footer: Ikechi Ndukwe | MA II | Lab 8 (March 11, 2026) | 14 / 14*