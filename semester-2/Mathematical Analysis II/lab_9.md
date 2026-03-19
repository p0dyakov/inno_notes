Ниже представлен полный построчный транскрипт презентации, разбитый по слайдам, с сохранением структуры и описанием визуальных элементов.

---

### Slide 1: Title Page

**[Visual Description]**
Верхнюю треть слайда занимает темно-зеленый прямоугольный баннер с закругленными углами и легкой тенью. Внутри баннера центрированный белый текст. Остальная часть слайда — белый фон с черным и серым текстом. В самом низу расположена узкая навигационная панель темно-зеленого цвета.

**[Text Content]**
**Mathematical Analysis (MA) II**
**Functions of Several Variables**

Ikechi Ndukwe

Lab 9
(March 18, 2026)

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 1 / 14

---

### Slide 2: Objectives

**[Visual Description]**
Заголовок слайда на темно-зеленом фоне. Основное содержание представлено в виде маркированного списка. Маркеры — маленькие зеленые сферы с бликом.

**[Text Content]**
**Objectives**

*   Recap
*   Lagrange Multipliers
*   Taylor’s Formula for Multivariable Functions
*   Homework

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 2 / 14

---

### Slide 3: Second Derivative Test for Local Extreme Values (Recap)

**[Visual Description]**
Заголовок на зеленом фоне. Текст на белом фоне. Пункты списка обозначены маленькими зелеными кружками с белыми буквами (a, b, c, d). Математические формулы выделены в отдельные строки.

**[Text Content]**
**Second Derivative Test for Local Extreme Values (Recap)**

Suppose that $f(x, y)$ and its first and second partial derivatives are continuous throughout a disk centered at $(a, b)$ and that $f_x(a, b) = f_y(a, b) = 0$. Then

a. $f$ has a **local maximum** at $(a, b)$ if $f_{xx} < 0$ and $D > 0$ at $(a, b)$.
b. $f$ has a **local minimum** at $(a, b)$ if $f_{xx} > 0$ and $D > 0$ at $(a, b)$.
c. $f$ has a **saddle point** at $(a, b)$ if $D < 0$ at $(a, b)$.
d. The test is **inconclusive** at $(a, b)$ if $D = 0$ at $(a, b)$. In this case, we must find some other way to determine the behavior of $f$ at $(a, b)$.

The expression $D = f_{xx}f_{yy} - f_{xy}^2$ is called the **discriminant** or **Hessian** of $f$. It is sometimes easier to remember it in determinant form,

$$D = f_{xx}f_{yy} - f_{xy}^2 = \begin{vmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{vmatrix}.$$

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 3 / 14

---

### Slide 4: Exercises (Part 1)

**[Visual Description]**
Заголовок на зеленом фоне. Одно упражнение, помеченное зеленым кружком с цифрой 1.

**[Text Content]**
**Exercises**

1. Find and classify the critical points of the following function:
   $f(x, y) = 10xye^{-(x^2+y^2)}$

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 4 / 14

---

### Slide 5: Lagrange Multipliers

**[Visual Description]**
Теоретический слайд. Заголовок на зеленом фоне. Основные условия выделены иконками (зеленые кружки с римскими цифрами i, ii).

**[Text Content]**
**Lagrange Multipliers**

Suppose that $f$ and $g$ have continuous first partial derivatives near the point $P_0 = (x_0, y_0)$ on the curve $C$ with equation $g(x, y) = 0$. Suppose also that, when restricted to points on $C$, the function $f(x, y)$ has a local maximum or minimum value at $P_0$. Finally, suppose that

i. $P_0$ is not an endpoint of $C$, and
ii. $\nabla g(P_0) \neq 0$.

Then there exists a number $\lambda_0$ such that $(x_0, y_0, \lambda_0)$ is a critical point of the **Lagrange function**

$$L(x, y, \lambda) = f(x, y) - \lambda g(x, y).$$

$\lambda$ is called a **Lagrange multiplier**, $f(x, y)$ is called the **objective function**, and $g(x, y)$ is called the **constraint**.

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 5 / 14

---

### Slide 6: Critical points of L

**[Visual Description]**
Белый слайд с математическими уравнениями, выровненными по центру.

**[Text Content]**
At any critical point of $L$ we must have

$$0 = \frac{\partial L}{\partial x} = f_1(x, y) - \lambda g_1(x, y),$$
$$0 = \frac{\partial L}{\partial y} = f_2(x, y) - \lambda g_2(x, y),$$
$$0 = \frac{\partial L}{\partial \lambda} = g(x, y),$$

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 6 / 14

---

### Slide 7: Exercises (Part 2)

**[Visual Description]**
Список упражнений (2-5) с использованием Lagrange Multipliers.

**[Text Content]**
**Exercises**

2. A rectangular box without a lid is to be made from $12 \text{ m}^2$ of cardboard. Find the maximum volume.
3. Find the extreme values of $f(x, y) = x^2 + 2y^2$ on the circle $x^2 + y^2 = 1$.
4. Find the points on the sphere $x^2 + y^2 + z^2 = 4$ closest to and farthest from $(3, 1, -1)$.
5. Find the maximum and minimum of $f(x, y) = xy$ on the circle $x^2 + y^2 = 1$.

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 7 / 14

---

### Slide 8: Taylor’s Formula for Multivariable Functions (Point (a,b))

**[Visual Description]**
Заголовок на зеленом фоне. Подзаголовок в светло-зеленой рамке. Сложная многострочная формула.

**[Text Content]**
**Taylor’s Formula for Multivariable Functions**

**Taylor’s Formula at the Point $(a, b)$**

Suppose $f(x, y)$ and its partial derivatives through order $n + 1$ are continuous throughout an open rectangular region $R$ centered at a point $(a, b)$. Then, throughout $R$,

$$f(a + h, b + k) = f(a, b) + (hf_x + kf_y) \big|_{(a,b)} + \frac{1}{2!}(h^2f_{xx} + 2hkf_{xy} + k^2f_{yy}) \big|_{(a,b)}$$
$$+ \frac{1}{3!}(h^3f_{xxx} + 3h^2kf_{xxy} + 3hk^2f_{xyy} + k^3f_{yyy}) \big|_{(a,b)} + \dots$$
$$+ \frac{1}{n!} \left( h \frac{\partial}{\partial x} + k \frac{\partial}{\partial y} \right)^n f \bigg|_{(a,b)}$$
$$+ \frac{1}{(n + 1)!} \left( h \frac{\partial}{\partial x} + k \frac{\partial}{\partial y} \right)^{n+1} f \bigg|_{(a+ch, b+ck)}$$

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 8 / 14

---

### Slide 9: Second Degree Taylor’s Formula

**[Visual Description]**
Заголовок на зеленом фоне. Формула второго порядка в рамке.

**[Text Content]**
**Taylor’s Formula for Multivariable Functions**

**Second Degree Taylor’s Formula at the Point $(a, b)$**

$$f(x, y) = f(a, b) + ((x - a)f_x + (y - b)f_y) \big|_{(a,b)}$$
$$+ \frac{1}{2!} ((x - a)^2f_{xx} + 2(x - a)(y - b)f_{xy} + (y - b)^2f_{yy}) \big|_{(a,b)}$$

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 9 / 14

---

### Slide 10: Taylor’s Formula at the Origin

**[Visual Description]**
Заголовок на зеленом фоне. Формула разложения в точке (0,0) (ряд Маклорена) в рамке.

**[Text Content]**
**Taylor’s Formula for Multivariable Functions**

**Taylor’s Formula at the Origin**

$$f(x, y) = f(0, 0) + xf_x + yf_y + \frac{1}{2!} (x^2f_{xx} + 2xyf_{xy} + y^2f_{yy})$$
$$+ \frac{1}{3!} (x^3f_{xxx} + 3x^2yf_{xxy} + 3xy^2f_{xyy} + y^3f_{yyy}) + \dots$$
$$+ \frac{1}{n!} \left( x^n \frac{\partial^n f}{\partial x^n} + nx^{n-1}y \frac{\partial^n f}{\partial x^{n-1}\partial y} + \dots + y^n \frac{\partial^n f}{\partial y^n} \right)$$
$$+ \frac{1}{(n + 1)!} \left( x^{n+1} \frac{\partial^{n+1} f}{\partial x^{n+1}} + (n + 1)x^ny \frac{\partial^{n+1} f}{\partial x^n\partial y} + \dots + y^{n+1} \frac{\partial^{n+1} f}{\partial y^{n+1}} \right) \bigg|_{(cx, cy)}$$

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 10 / 14

---

### Slide 11: Exercises (Part 3)

**[Visual Description]**
Список упражнений (6-8) по теме формулы Тейлора.

**[Text Content]**
**Exercises**

6. Find the second degree Taylor polynomial for $f(x, y) = e^x \cos y$ at $(0, 0)$.
7. Find the second degree Taylor polynomial for $f(x, y) = \ln(xy)$ at $(1, 2)$.
8. Use a second degree Taylor polynomial to estimate $f(2.1, 1.8)$ for $f(x, y) = x^y$ near $(2, 2)$.

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 11 / 14

---

### Slide 12: Homework (Part 1)

**[Visual Description]**
Заголовок на зеленом фоне. Список домашних задач (a-g) по методу множителей Лагранжа.

**[Text Content]**
**Homework**

1. Using Lagrange multipliers:
   a. Find the dimensions of a rectangular box of maximum volume with fixed surface area $S$ (open top).
   b. Find the points on the surface $xy^2z^3 = 2$ closest to the origin.
   c. Minimize $f(x, y, z) = x^2 + y^2 + z^2$ subject to $x + y + z = 1$.
   d. Find the maximum and minimum of $f(x, y) = x^2 + y^2$ on the curve $xy = 1$.
   e. A rectangular box (with lid) is to have volume $V$. Find the dimensions that minimize the surface area.
   f. Find the maximum volume of a rectangular box inscribed in the ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$.
   g. Find the points on the sphere $x^2 + y^2 + z^2 = 1$ that are closest to $(2, 1, -1)$.

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 12 / 14

---

### Slide 13: Homework (Part 2)

**[Visual Description]**
Продолжение списка домашних задач (2-8) по многочленам Тейлора.

**[Text Content]**
2. Find the second degree Taylor polynomial for $f(x, y) = \sin(xy)$ at $(0, 0)$.
3. Find the second degree Taylor polynomial for $f(x, y) = e^{x+y}$ at $(0, 0)$.
4. Compute the quadratic approximation of $f(x, y) = \cos(x + y)$ at $(0, 0)$.
5. Use a second degree Taylor polynomial to approximate $f(1.1, 1.9)$ for $f(x, y) = x^2 \ln y$ near $(1, 2)$.
6. Find the second degree Taylor polynomial for $f(x, y) = \sqrt{1 + x + y}$ at $(0, 0)$ and estimate $f(0.1, 0.1)$.
7. Find the second degree Taylor polynomial for $f(x, y) = \ln(1 + x + y)$ at $(0, 0)$ and use it to estimate $f(0.1, 0.2)$. Compare with exact value.
8. Compute the second degree Taylor polynomial for $f(x, y) = e^x \sin y$ at $(0, 0)$ and use it to estimate $f(0.1, 0.2)$.

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 13 / 14

---

### Slide 14: Final Slide

**[Visual Description]**
Центрированная надпись на белом фоне.

**[Text Content]**
**Thank You**

**[Footer]**
Ikechi Ndukwe | MA II | Lab 9 (March 18, 2026) | 14 / 14