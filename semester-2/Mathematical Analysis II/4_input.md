## Slide 1

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

# Mathematical Analysis II.
### Chapter 4: Integrals and Vector Fields: Line Integrals, Surface Integrals

**Mohammad S. Alkousa**
Assistant Professor in Innopolis University
Lab of High Performance Computing.
Senior Researcher at Laboratory of Modern Adaptive
Computational Methods in Innopolis University.
`m.alkousa@innopolis.ru`

Updated April 22, 2026

M. S. Alkousa | Chapter 4

***

## Slide 2

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Contents

**1. Introduction to Vector Calculus**
* Vector Fields
* Gradients, Curl, and Divergence

**2. Line Integrals**
* Line Integrals of Scalar Functions
* Line Integrals of Vector Fields: Work, Circulation, and Flux
* The Fundamental Theorem of Line Integrals
* Green’s Theorem

**3. Surface Integrals**
* Parametric surfaces and Their Areas
* Surface Integrals of Scalar Functions
* Oriented Surfaces

M. S. Alkousa | Chapter 4

***

## Slide 3

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Vector Fields

Gravitational forces, electric forces, and many other types of fields have both direction and magnitude. These quantities are described by a vector assigned to every point within their domain, which is known as a **vector field**.
More generally, a vector field is a function that maps each point in its domain to a vector. A vector field on a **three-dimensional** domain in space might have a formula like:
$$\mathbf{F}(x, y, z) = M(x, y, z)\hat{i} + N(x, y, z)\hat{j} + P(x, y, z)\hat{k}.$$

*Image Description: Three side-by-side illustrations of vector fields.* 
* *Left: Velocity vectors of fluid flowing around a grey airfoil shape, showing air deflecting around it.* 
* *Middle: Red and blue velocity vectors (streamlines) in a contracting channel. The arrows are longer in the narrower section, indicating that water speeds up as the channel narrows.* 
* *Right: A 3D spherical object surrounded by a gravitational vector field where all colored arrows point directly toward the center of mass.*

**Figure:** Velocity vectors of a flow around an airfoil (left). Streamlines in a contracting channel, note that the water speeds up as the channel narrows, and the velocity vectors increase in length (middle). Vectors in a gravitational field point toward the center of mass (right).

M. S. Alkousa | Chapter 4

***

## Slide 4

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Vector Fields

**Examples.**
1. The tangent vectors $\mathbf{T}$ and normal vectors $\mathbf{N}$ for a curve in space both form vector fields along the curve $\mathbf{r}(t) = f(t)\hat{i} + g(t)\hat{j} + h(t)\hat{k}$.
2. If we attach the gradient vector $\nabla f$ of a scalar function $f(x, y, z)$ to each point of a level surface of the function, we obtain a three-dimensional vector field on the surface.
3. If we attach the velocity vector to each point of a flowing fluid, we obtain a three-dimensional field defined on a region in space.

*Image Description: Four illustrative diagrams.*
* *Top Right: A blue parametric curve in space with distinct points $P_0, P_1, P_2$. At each point, red arrows represent the tangent vector ($\mathbf{T}$) and green arrows represent the normal vector ($\mathbf{N}$).*
* *Bottom Left: A 3D coordinate system showing a vector field pointing directly upwards along the z-axis, represented by the formula $\mathbf{F}(x, y, z) = z\hat{k}$.*
* *Bottom Middle: A 3D vector field within a rectangular volume where vectors flow primarily horizontally, represented by the formula $\mathbf{F}(x, y, z) = y\hat{i} - 2\hat{j} + x\hat{k}$.*
* *Bottom Right: A 3D vector field within a rectangular volume with vectors pointing radially outward and upward, represented by the formula $\mathbf{F}(x, y, z) = \frac{y}{z}\hat{i} - \frac{x}{z}\hat{j} + \frac{z}{4}\hat{k}$.*

M. S. Alkousa | Chapter 4

***

## Slide 5

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Gradient Fields, Conservative Fields

**Definition (Gradient Field)**
We define the **gradient field** of a differentiable function $f(x, y, z)$ (the definition extends naturally to functions of $n$ variables) as the vector field consisting of the gradient vectors:
$$\nabla f = \frac{\partial f}{\partial x}\hat{i} + \frac{\partial f}{\partial y}\hat{j} + \frac{\partial f}{\partial z}\hat{k}.$$
At each point $(x, y, z)$, the gradient field assigns a vector that points in the direction of the greatest increase of $f$, and its magnitude equals the directional derivative of $f$ in that direction.

**Definition (Conservative vector field)**
A vector field $\mathbf{F}$ is called a **conservative vector field** if it is the gradient of some scalar function. That is, if there exists a function $f$ such that $\mathbf{F} = \nabla f$. In this situation, $f$ is called a **potential function** for $\mathbf{F}$.

**Example.** The field $\mathbf{F} = (e^x \cos y + yz)\hat{i} + (xz - e^x \sin y)\hat{j} + (xy + z)\hat{k}$ is conservative over its natural domain, and $f(x, y, z) = e^x \cos y + xyz + \frac{z^2}{2}$ is a potential function for it.
*(Check why. Try to explain how can we calculate $f$).*

M. S. Alkousa | Chapter 4

***

## Slide 6

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Curl of a Vector Field and Conservative Fields

**Definition (Curl)**
If $\mathbf{F} = P\hat{i} + Q\hat{j} + R\hat{k}$ is a vector field on $\mathbb{R}^3$ and the partial derivatives of $M, N$ and $P$ exist, then the curl of $\mathbf{F}$ (or the rotation of $\mathbf{F}$) is the vector field on $\mathbb{R}^3$ defined by
$$\text{curl}(\mathbf{F}) = \nabla \times \mathbf{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ M & N & P \end{vmatrix} = \left(\frac{\partial P}{\partial y} - \frac{\partial N}{\partial z}\right)\hat{i} - \left(\frac{\partial P}{\partial x} - \frac{\partial M}{\partial z}\right)\hat{j} + \left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right)\hat{k}.$$

**Theorem (Curl and Gradient)**
*If $f$ is a function of three variables that has **continuous** second-order partial derivatives, then $\text{curl}(\nabla f) = \mathbf{0}$.*

**Proof.** We have
$$\text{curl}(\nabla f) = \nabla \times (\nabla f) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} & \frac{\partial f}{\partial z} \end{vmatrix}$$
$$= \left(\frac{\partial^2 f}{\partial y \partial z} - \frac{\partial^2 f}{\partial z \partial y}\right)\hat{i} - \left(\frac{\partial^2 f}{\partial x \partial z} - \frac{\partial^2 f}{\partial z \partial x}\right)\hat{j} + \left(\frac{\partial^2 f}{\partial x \partial y} - \frac{\partial^2 f}{\partial y \partial x}\right)\hat{k} = \mathbf{0}. \quad \square$$

M. S. Alkousa | Chapter 4

***

## Slide 7

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Curl of a Vector Field and Conservative Fields

Since a conservative vector field is one for which $\mathbf{F} = \nabla f$, this Theorem can be rewrite as follows: $\color{red}{\text{If } \mathbf{F} \text{ is conservative, then } \text{curl}(\mathbf{F}) = \mathbf{0}.}$ This gives us a way to test whether a given vector field is conservative.

In general, the converse of this theorem **does not** hold (a counterexample will be provided in the next section, following our discussion of line integrals of vector fields). Nevertheless, the following theorem establishes that the converse is true provided $\mathbf{F}$ is defined on the entire domain. $\color{red}{\text{More generally, the converse is true if the domain is simply-connected, that is, “domain without holes”.}}$

**Theorem**
*Let $\mathbf{F}$ be a field on an **open simply connected domain** whose component functions have **continuous** first partial derivatives. Then $\mathbf{F}$ is a conservative if and only if $\text{curl}(\mathbf{F}) = \mathbf{0}$.*

**Proof.** The proof requires Stokes' Theorem, which we will study in the next.

**Example.** The field $\mathbf{F}(x, y, z) = y^2 z^3 \hat{i} + 2xyz^3 \hat{j} + 3xy^2 z^2 \hat{k}$ is a conservative vector field (it is defined on $\mathbb{R}^3$ and $\nabla \times \mathbf{F} = \mathbf{0}$ $\color{red}{\text{(check the answer)}}$), and $f(x, y, z) = xy^2 z^3 + C$ is a potential for this field (where $C \in \mathbb{R}$). $\color{red}{\text{Explain how can we find } f.}$

M. S. Alkousa | Chapter 4

***

## Slide 8

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Divergence of a Vector Field

**Definition (Divergence of a Vector Field)**
If $\mathbf{F} = M\hat{i} + N\hat{j} + P\hat{k}$ is a vector field on $\mathbb{R}^3$, and $\frac{\partial M}{\partial x}, \frac{\partial N}{\partial y}, \frac{\partial P}{\partial z}$ exist, then the **divergence** of $\mathbf{F}$ is the function (scalar field) of three variables defined by
$$\text{div}(\mathbf{F}) = \nabla \cdot \mathbf{F} = \frac{\partial M}{\partial x} + \frac{\partial N}{\partial y} + \frac{\partial P}{\partial z}.$$

**Example.** For the field $\mathbf{F}(x, y, z) = y^2 z^3 \hat{i} + 2xyz^3 \hat{j} + 3xy^2 z^2 \hat{k}$, we have
$$\text{div}(\mathbf{F}) = \frac{\partial}{\partial x}(y^2 z^3) + \frac{\partial}{\partial y}(2xyz^3) + \frac{\partial}{\partial z}(3xy^2 z^2) = 2xz^3 + 6xy^2 z.$$

**Theorem (Divergence and Curl)**
*If $\mathbf{F} = M\hat{i} + N\hat{j} + P\hat{k}$ is a vector field on $\mathbb{R}^3$ and $M, N, P$ have continuous second-order partial derivatives, then $\text{div}(\text{curl}(\mathbf{F})) = 0$.*

**Proof.** $\color{red}{\text{Try to formulate the proof, by calculating } \text{div}(\text{curl}(\mathbf{F})) = \nabla \cdot (\nabla \times \mathbf{F}).}$

**Remark.** Note that $\text{div}(\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2} = \nabla^2 f$, where $\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$ is the **Laplace Operator**, and $\nabla^2 f = 0$ is the **Laplace's Equation**.

M. S. Alkousa | Chapter 4

***

## Slide 9

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Gradients, Curl, and Divergence: Exercises

$\color{red}{\text{Exercise 1.}}$ $\color{red}{\text{Find the curl and the divergence of the vector field.}}$
1. $\mathbf{F} = xy^2 z^2 \hat{i} + yx^2 z^2 \hat{j} + zx^2 y^2 \hat{k}.$
2. $\mathbf{F} = \frac{\sqrt{x}}{1 + z}\hat{i} + \frac{\sqrt{y}}{1 + x}\hat{j} + \frac{\sqrt{z}}{1 + y}\hat{k}.$
3. $\mathbf{F} = \ln(2y + 3z)\hat{i} + \ln(x + 3z)\hat{j} + \ln(x + 2y)\hat{k}.$
4. $\mathbf{F} = \arctan(xy)\hat{i} + \arctan(yz)\hat{j} + \arctan(xz)\hat{k}.$

$\color{red}{\text{Exercise 2.}}$ $\color{red}{\text{Determine whether or not the vector field is conservative. If it is conservative, find a function } f \text{ such that } \mathbf{F} = \nabla f.}$
1. $\mathbf{F}(x, y, z) = xyz^4 \hat{i} + x^2 z^4 \hat{j} + 4x^2 yz^3 \hat{k}.$
2. $\mathbf{F}(x, y, z) = z \cos y \hat{i} + xz \sin y \hat{j} + x \cos y \hat{k}.$
3. $\mathbf{F}(x, y, z) = e^{yz}\hat{i} + xze^{yz}\hat{j} + xye^{yz}\hat{k}.$
4. $\mathbf{F}(x, y, z) = e^x \sin yz \hat{i} + ze^x \cos yz \hat{j} + ye^x \cos yz \hat{k}.$

$\color{red}{\text{Exercise 3.}}$ $\color{red}{\text{Let } f \text{ be a scalar fields, and } \mathbf{F, G} \text{ be vector fields. Prove that}}$
1. $\text{div}(\mathbf{F} + \mathbf{G}) = \text{div}(\mathbf{G}) + \text{div}(\mathbf{G}).$
2. $\text{curl}(\mathbf{F} + \mathbf{G}) = \text{curl}(\mathbf{G}) + \text{curl}(\mathbf{G}).$
3. $\text{div}(f\mathbf{F}) = f\text{div}(\mathbf{F}) + \mathbf{F} \cdot \nabla f.$
4. $\text{curl}(f\mathbf{F}) = \nabla f \times \text{curl}(\mathbf{F}) + f\text{curl}(\mathbf{F}).$

M. S. Alkousa | Chapter 4

***

## Slide 10

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions

To compute the total mass of a wire that lies along a curve in space, or to determine the work done by a force moving along that curve, we need a more general concept of integration than the standard definite (single) integral over an interval. Specifically, we need to integrate over a curve $C$, rather than over an interval $[a, b]$. These more general integrals are known as **line integrals**.

Let $f(x, y, z)$ be a real-valued function, and $C$ be a curve lying within the domain of $f$ and parametrized by $\mathbf{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}, a \le t \le b$. The values of $f$ along the curve $C$ are given by the composite function $f(x(t), y(t), z(t))$. To integrate $f$ over $C$, we are going to integrate this composition **with respect to arc length** from $t = a$ to $t = b$. For this, we partition the curve $C$ into a finite number $n$ of subarcs. The typical subarc has length $\Delta s_k$. In each subarc we choose a point $(x_k, y_k, z_k)$ and form the sum

$$S_n = \sum_{k=1}^n f(x_k, y_k, z_k)\Delta s_k,$$

Depending on how we partition the curve $C$ and pick $(x_k, y_k, z_k)$ in the $k$th subarc, we may get different values for $S_n$.

*Image Description: A 3-dimensional coordinate system with axes x, y, and z. A blue curve represented by $\mathbf{r}(t)$ spans from $t=a$ to $t=b$. The curve is partitioned into segments, highlighting one segment as $\Delta s_k$, with a specific point $(x_k, y_k, z_k)$ lying on that subarc.*

M. S. Alkousa | Chapter 4

***

## Slide 11

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions

**Definition (Line Integrals of Scalar Function)**
If $f$ is defined on a curve $C$ given parametrically by $\mathbf{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$, for $a \le t \le b$, then the **line integral of $f$ over (along) $C$ with respect to arc length** is

$$\int_C f(x, y, z)ds = \lim_{n \to \infty} \sum_{k=1}^n f(x_k, y_k, z_k)\Delta s_k, \quad (1)$$

provided this limit exists.

If the curve $C$ is smooth for $a \le t \le b$, so $\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} \neq \mathbf{0}$ is continuous, and the function $f$ is continuous on $C$, then the limit in (1) exists. We can then apply the Fundamental Theorem of Calculus to differentiate the arc length equation,

$$s(t) = \int_{t_0 = a}^t ||\mathbf{v}(\tau)|| d\tau \implies \frac{ds}{dt} = ||\mathbf{v}(t)|| = \left|\left| \frac{d\mathbf{r}}{dt} \right|\right| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}.$$

So we get the following formula for the line integral in (1)

$${\color{blue} \int_C f(x, y, z)ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} dt.} \quad (2)$$

M. S. Alkousa | Chapter 4

***

## Slide 12

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions: Example

The integral on the right side of (2) is just an ordinary definite integral over the interval $[a, b]$, where we are integrating with respect to the parameter $t$. Note that the parameter $t$ defines a direction along $C$. The starting point on $C$ is the position $\mathbf{r}(a)$, and movement along the path is in the direction of increasing $t$.

**Example.** Calculate $\int_C (2 + x^2 y)ds$, where $C$ is the upper half of the unit circle $x^2 + y^2 = 1$.
**Solution.**
The upper half of the unit circle can be parametrized by the equations $x = \cos t, y = \sin t$, with $0 \le t \le \pi$.
Thus,

$$\int_C (2 + x^2 y)ds = \int_0^\pi (2 + \sin t \cos^2 t)\sqrt{(x')^2 + (y')^2} dt$$
$$= \int_0^\pi (2 + \sin t \cos^2 t)\sqrt{\sin^2 t + \cos^2 t} dt$$
$$= \int_0^\pi (2 + \sin t \cos^2 t)dt = \left[ 2t - \frac{1}{3} \cos^3 t \right]_0^\pi = \frac{2}{3} + 2\pi$$

*Image Description: A 2D Cartesian plane showing the upper half of the unit circle (a pink semicircle) defined by $x^2 + y^2 = 1 \ (y \ge 0)$, stretching from $x = -1$ to $x = 1$. The curve is oriented counterclockwise with an arrow indicating the direction.*

M. S. Alkousa | Chapter 4

***

## Slide 13

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions: Example

**Remark.** If the curve $C$ is a **piecewise-smooth**; that is, $C$ is a union of a finite number of smooth curves $C_1, C_2, \dots, C_n$, the initial point of $C_{i+1}$ is the terminal point of $C_i$. Then we define the integral of $f$ along $C$ as:

$$\int_C f ds = \int_{C_1} f ds + \int_{C_2} f ds + \dots + \int_{C_n} f ds.$$

**Example.** Calculate $\int_C (x - 3y^2 + z)ds$, where
1. $C$ is the line segment joining the origin to the point $(1, 1, 1)$
2. $C = C_1 \cup C_2$, where $C_1$ is the line segment joining the origin to the point $(1, 1, 0)$ and $C_2$ is the line segment joining the point $(1, 1, 0)$ to the point $(1, 1, 1)$.

*Image Description: Three separate illustrative figures.*
* *Top Right: A 2D graph demonstrating a generic piecewise-smooth curve $C$ composed of five connected segments: $C_1, C_2, C_3, C_4, C_5$.*
* *Bottom Left: A 3D graph showing a direct straight path (light blue dashed line) labeled $C$ from the origin $(0,0,0)$ to the point $(1, 1, 1)$. A red dashed line projects this point down to $(1,1,0)$ in the xy-plane.*
* *Bottom Right: A 3D graph showing a piecewise path. The first segment $C_1$ goes from the origin $(0,0,0)$ to $(1,1,0)$ on the xy-plane. The second segment $C_2$ goes vertically from $(1,1,0)$ up to $(1,1,1)$.*

M. S. Alkousa | Chapter 4

***

## Slide 14

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions: Example

**Solution.**
1. For $C$, we can take the parameterization $\mathbf{r}(t) = t\hat{i} + t\hat{j} + t\hat{k}$, with $0 \le t \le 1$. Thus, $ds = \sqrt{3}dt$, and
$$\int_C (x - 3y^2 + z)ds = \int_0^1 (t - 3t^2 + t)\sqrt{3}dt = \sqrt{3} \int_0^1 (2t - 3t^2)dt = 0$$

2. For $C_1$ and $C_2$, we can take the parameterization
$C_1: \mathbf{r}(t) = t\hat{i} + t\hat{j}, \quad 0 \le t \le 1 \implies ds = \sqrt{2}dt.$
$C_2: \mathbf{r}(t) = \hat{i} + \hat{j} + t\hat{k}, \quad 0 \le t \le 1 \implies ds = dt.$

Thus, we get
$$\int_{C=C_1 \cup C_2} f(x, y, z) ds = \int_0^1 f(t, t, 0)\sqrt{2} dt + \int_0^1 f(1, 1, t)dt$$
$$= \sqrt{2}\left[\frac{t^2}{2} - t^3\right]_0^1 + \left[\frac{t^2}{2} - 2t\right]_0^1 = -\frac{\sqrt{2} + 3}{2}$$

$\color{red}{\text{\textbf{Note} that the value of a line integral along a path joining two points can change if you change the path between them.}}$

M. S. Alkousa | Chapter 4

***

## Slide 15

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions

**Remark.** We can integrate $f(x, y, z)$ along the curve $C: \mathbf{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$, where $a \le t \le b$, **with respect to** $x, y$ **and** $z$ (not only with respect to arc length) as follows:
$$\int_C f(x, y, z)dx = \int_a^b f(x(t), y(t), z(t))x'(t) dt;$$
$$\int_C f(x, y, z)dy = \int_a^b f(x(t), y(t), z(t))y'(t) dt;$$
$$\int_C f(x, y, z)dz = \int_a^b f(x(t), y(t), z(t))z'(t) dt.$$

**Example.** Calculate $I = \int_C y dx + z dy + x dz$, where $C$ consists of the line segment $C_1$ from $(2, 0, 0)$ to $(3, 4, 5)$, followed by the line segment $C_2$ from $(3, 4, 5)$ to $(3, 4, 0)$.
**Solution.** For $C_1, C_2$, We have following parameterization $C$
$$C_1 : x = 2 + t, y = 4t, z = 5t, \quad C_2 : x = 3, y = 4, z = 5 - 5t \text{ with } 0 \le t \le 1$$

$$I = \int_{C_1} y dx + z dy + x dz + \int_{C_2} y dx + z dy + x dz$$
$$= \int_0^1 (10 + 29t)dt + \int_0^1 (-15)dt = 24.5 - 15 = 9.5$$

M. S. Alkousa | Chapter 4

***

## Slide 16

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Scalar Functions: Exercises

$\color{red}{\text{Exercise 1.}}$
1. Calculate $\int_C (x - y + z - 2)ds$, where $C$ is the straight-line segment from $(0, 1, 1)$ to $(1, 0, 1)$.
2. Calculate $\int_C \sqrt{x^2 + y^2}ds$ along the curve $C: \mathbf{r}(t) = (4 \cos t)\hat{i} + (4 \sin t)\hat{j} + 3t\hat{k}$, with $-2\pi \le t \le 2\pi$.
3. Integrate the function $f(x, y, z) = x + \sqrt{y} - z^2$ over the path $C_1$ followed by $C_2$ followed by $C_3$ from $(0, 0, 0)$ to $(1, 1, 1)$ given by:
$$C_1: \mathbf{r}(t) = t\hat{k}; \quad C_2: \mathbf{r}(t) = t\hat{j} + \hat{k}; \quad C_3: \mathbf{r}(t) = t\hat{i} + \hat{j} + \hat{k}, \quad 0 \le t \le 1.$$

$\color{red}{\text{Exercise 2.}}$
1. Calculate $\int_C (x + \sqrt{y})ds$, where $C$ is given in the figure as a joining of the parabola and a line segment.
2. Calculate $\int_C \frac{ds}{1 + x^2 + y^2}$, where $C$ is given in the figure as a square.

*Image Description: Two graphs corresponding to Exercise 2.*
* *Left Diagram (for Exercise 2.1): A 2D graph with a path $C$ composed of two parts: moving along the parabola $y = x^2$ from $(0,0)$ to $(1,1)$, then returning straight back to the origin along the line $y = x$. Arrows indicate a counterclockwise loop.*
* *Right Diagram (for Exercise 2.2): A 2D graph with a square path $C$. The path travels from $(0,0)$ to $(1,0)$, then up to $(1,1)$, then left to $(0,1)$, and back down to $(0,0)$, with arrows indicating a counterclockwise direction.*

M. S. Alkousa | Chapter 4

***

## Slide 17

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields

In the previous section, we defined the line integral of a scalar function $f(x, y, z)$ over a path $C$. We will now see the idea of a line integral of a vector field $\mathbf{F}$ along the curve $C$. Such line integrals have important applications in the study of fluid flows, work, and energy, and electrical or gravitational fields.
Assume that the vector field $\mathbf{F} = M(x, y, z)\hat{i} + N(x, y, z)\hat{j} + P(x, y, z)\hat{k}$ has continuous components, and defined along a smooth curve $C$ parametrized by $\mathbf{r}(t) = g(t)\hat{i} + h(t)\hat{j} + k(t)\hat{k}, a \le t \le b$.
The parametrization $\mathbf{r}(t)$ defines a direction (or orientation) along $C$ that we call the **forward direction**. At each point along the path $C$, the tangent vector $\mathbf{T} = \frac{d\mathbf{r}}{ds}$ is a unit vector tangent to the path and pointing in this forward direction.

*Image Description: A parametric curve in 3D space starting at point A ($t=a$) and ending at point B ($t=b$). At a specific point on the curve, two vectors are drawn: a red unit tangent vector $\mathbf{T}$ pointing along the path's direction, and a purple vector $\mathbf{F}$ representing the vector field at that location.*

**Definition (Line Integral of a Vector Field, and Work)**
The **line integral of a continuous vector field $\mathbf{F}$ along a smooth curve** $C$ given by a vector function $\mathbf{r}(t); a \le t \le b$, $\color{blue}{\text{or}}$ the **work** done by the force field $\mathbf{F}$ in moving an object from the point $A = \mathbf{r}(a)$ to the point $B = \mathbf{r}(b)$ along $C$, is the line integral of the scalar component of $\mathbf{F}$ in the direction of the unit tangent vector (i.e., $\mathbf{F} \cdot \mathbf{T} = \mathbf{F} \cdot d\mathbf{r}$) over the smooth curve from $A$ to $B$.

M. S. Alkousa | Chapter 4

***

## Slide 18

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Examples

**Example 1.**
Find the work done by the force field $\mathbf{F} = (y - x^2)\hat{i} + (z - y^2)\hat{j} + (x - z^2)\hat{k}$ in moving an object along the curve $C: \mathbf{r}(t) = t\hat{i} + t^2\hat{j} + t^3\hat{k}, 0 \le t \le 1$, from $(0, 0, 0)$ to $(1, 1, 1)$.

**Solution.** We have $\frac{d\mathbf{r}}{dt} = \hat{i} + 2t\hat{j} + 3t^2\hat{k}$, and the work is
$$W = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt$$
$$= \int_0^1 (-3t^8 - 2t^5 + 2t^4 + 3t^3)dt = \boxed{\frac{29}{60}}$$

*Image Description: A 3D plot showing the space curve $\mathbf{r}(t) = t\hat{i} + t^2\hat{j} + t^3\hat{k}$ drawn as a blue solid line from the origin $(0,0,0)$ to the point $(1,1,1)$. Red dashed lines show the projection to the point $(1,1,0)$ on the xy-plane.*

**Example 2.** Calculate the line integral $\int_C \mathbf{F} \cdot d\mathbf{r}$, where
$\mathbf{F}(x, y, z) = \sin x \hat{i} + \cos y \hat{j} + xz \hat{k}, \quad \mathbf{r}(t) = t^3\hat{i} - t^2\hat{j} + t\hat{k}, 0 \le t \le 1.$
**Solution.**
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt = \int_0^1 \left( 3t^2 \sin(t^3) - 2t \cos(t^2) + t^4 \right) dt$$
$$= \left[ -\cos(t^3) - \sin(t^2) + \frac{t^5}{5} \right]_0^1 = \boxed{-\cos(1) - \sin(1) + \frac{6}{5}}$$

M. S. Alkousa | Chapter 4

***

## Slide 19

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Flow Integrals, Circulation for Velocity Fields

Suppose that $\mathbf{F}$ represents the velocity field of a fluid flowing through a region in space (the turbine chamber of a hydroelectric generator, for example). The integral of $\mathbf{F} \cdot \mathbf{T}$ along a curve in the region gives the **fluid's flow** $\color{red}{\text{along}}$, or **circulation around**, the curve.

*Image Description: Two 2-dimensional vector fields plotted on x-y axes.*
* *Left: Red arrows radiate outward from the origin uniformly in all directions. This is the radial field $\mathbf{F} = x\hat{i} + y\hat{j}$.*
* *Right: Red arrows form a counterclockwise circulating pattern around the origin. The length of the vectors is consistent. This is the "spin" field.*

$\color{green}{\text{Figure:}}$ The radial field $\mathbf{F} = x\hat{i} + y\hat{j}$, this field gives zero circulation around the unit circle (in the left). A "spin" field of rotating unit vectors $\mathbf{F} = -\frac{y}{\sqrt{x^2+y^2}}\hat{i} + \frac{x}{\sqrt{x^2+y^2}}\hat{j}$ in the plane, this field gives a nonzero circulation around the unit circle (in the right).

M. S. Alkousa | Chapter 4

***

## Slide 20

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Flow Integrals, Circulation for Velocity Fields

**Definition (Flow Integral and Circulation for Velocity Fields Around the Curve)**
If $\mathbf{r}(t)$ parametrizes a smooth curve $C$ in the domain of a continuous velocity field $\mathbf{F}$, then the **flow** $\color{red}{\text{along}}$ **the curve** from $A = \mathbf{r}(a)$ to $B = \mathbf{r}(b)$ is: $\color{blue}{\text{Flow } = \int_C \mathbf{F} \cdot \mathbf{T}}$. This integral is called a **flow integral**. If the curve is closed (i.e., starts and ends at the same point), so that $A = B$, the flow is called the **circulation around the curve**.

**Example.** Find the circulation of the field $\mathbf{F} = (x - y)\hat{i} + x\hat{j}$ around the circle $\mathbf{r}(t) = (\cos t)\hat{i} + (\sin t)\hat{j}, \ 0 \le t \le 2\pi$.

**Solution.** On the circle, we have
$\mathbf{F} = (\cos t - \sin t)\hat{i} + (\cos t)\hat{j}$, and
$\mathbf{r}'(t) = (-\sin t)\mathbf{i} + (\cos t)\mathbf{j}$. Then

$$\text{Circulation} = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt$$
$$= \int_0^{2\pi} (1 - \sin t \cos t) dt$$
$$= \left[ t - \frac{\sin^2 t}{2} \right]_0^{2\pi} = \boxed{2\pi}$$

*Image Description: A 2D vector field with red arrows mapped over the Cartesian plane. Overlaid on the vector field is a blue circle centered at the origin, with a counterclockwise directional arrow.*

M. S. Alkousa | Chapter 4

***

## Slide 21

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Flux Across a Simple Closed Plane Curve

A curve in the $xy$-plane is **simple** if it does not cross itself. When a curve starts and ends at the same point, it is a **closed curve** or **loop**.

**Definition (Flux of a Vector Field Across a Simple Closed Plane Curve)**
If $C$ is a smooth, **simple closed curve** in the domain of a continuous vector field $\mathbf{F} = M(x, y)\hat{i} + N(x, y)\hat{j}$ in the plane. The $\color{blue}{\text{flux of } \mathbf{F}}$ $\color{red}{\text{across } C}$ is the line integral over $C$ of the scalar component of the fluid's velocity field in the direction of the curve's outward-pointing unit $\color{red}{\text{normal}}$ vector $\mathbf{n}$,

$$\text{Flux of } F \text{ across } C = \int_C \mathbf{F} \cdot \mathbf{n}. \quad (3)$$

*Image Description: Four drawings illustrating different topological classifications of curves.*
* *Top Left (Blue): A curved line segment that does not cross itself and does not connect ends. Labeled "Simple, not closed".*
* *Top Right (Blue): A deformed circular loop that does not cross itself. Labeled "Simple, closed".*
* *Bottom Left (Red): A curve that crosses over itself forming a loop but doesn't connect ends. Labeled "Not simple, not closed".*
* *Bottom Right (Red): A figure-eight loop that crosses itself at the center. Labeled "Not simple, closed".*

To evaluate the integral for flux in (3), we begin with a smooth parametrization $x = x(t), y = y(t), a \le t \le b$, that traces the curve $C$ exactly once as $t$ increases from $a$ to $b$. We can find the outward unit normal vector $\mathbf{n}$ by taking the cross product of the curve's unit tangent vector $\mathbf{T}$ with the vector $\hat{k}$.
* If the motion is counterclockwise, $\mathbf{T} \times \hat{k}$ points outward, and we can take $\mathbf{n} = \mathbf{T} \times \hat{k}$.
* If the motion is clockwise, $\hat{k} \times \mathbf{T}$ points outward, and we can take $\mathbf{n} = \hat{k} \times \mathbf{T}$.

M. S. Alkousa | Chapter 4

***

## Slide 22

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Flux Across a Simple Closed Plane Curve

*Image Description: Two 3-dimensional coordinate system diagrams showing how to determine the outward normal vector using the cross product for a simple closed curve in the xy-plane.*
* *Left diagram: "For clockwise motion, $\mathbf{k} \times \mathbf{T}$ points outward." The curve C is traced clockwise (yellow arrow indicates direction). Tangent vector $\mathbf{T}$ points along the curve. Vector $\mathbf{k}$ points up along the z-axis. Their cross product $\mathbf{k} \times \mathbf{T}$ (red arrow) points radially outward.*
* *Right diagram: "For counterclockwise motion, $\mathbf{T} \times \mathbf{k}$ points outward." The curve C is traced counterclockwise. Tangent vector $\mathbf{T}$ points along the curve. Vector $\mathbf{k}$ points up. Their cross product $\mathbf{T} \times \mathbf{k}$ (red arrow) points radially outward.*

Therefore, for the counterclockwise motion, we have
$$\mathbf{n} = \mathbf{T} \times \hat{k} = \left(\frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j}\right) \times \hat{k} = \frac{dy}{dt}\hat{i} - \frac{dx}{dt}\hat{j}.$$

If $\mathbf{F} = M(x, y)\hat{i} + N(x, y)\hat{j}$, then
$$\mathbf{F} \cdot \mathbf{n} = M(x(t), y(t))\frac{dy}{dt} - N(x(t), y(t))\frac{dx}{dt}.$$

Hence,
$$\text{Outward flux} = \int_C \mathbf{F} \cdot \mathbf{n} = \color{red}{\oint_C (M \, dy - N \, dx)}.$$

M. S. Alkousa | Chapter 4

***

## Slide 23

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Flux Across a Simple Closed Plane Curve

**Example.** Find the flux of $\mathbf{F} = (x - y)\hat{i} + x\hat{j}$ across the circle $x^2 + y^2 = 1$ in the $xy$-plane.

**Solution.**
The parameterization $\mathbf{r}(t) = (\cos t)\hat{i} + (\sin t)\hat{j}, \ 0 \le t \le 2\pi$, exactly once traces the circle counterclockwise. We have $\mathbf{n} = \mathbf{T} \times \hat{k}$. Thus,
$$M = x - y = \cos t - \sin t, \quad N = x = \cos t, \quad dx = -\sin t \, dt, \quad dy = \cos t \, dt.$$

Therefore,
$$\text{Flux} = \oint_C (M \, dy - N \, dx) = \int_0^{2\pi} (\cos^2 t - \sin t \cos t + \cos t \sin t) dt$$
$$= \int_0^{2\pi} \cos^2 t \, dt = \int_0^{2\pi} \frac{1 + \cos 2t}{2} dt = \left[ \frac{t}{2} + \frac{\sin 2t}{4} \right]_0^{2\pi} = \boxed{\pi}$$

**Remark.** Because the flux of $\mathbf{F}$ is positive, the net flow across the curve is outward ($\mathbf{F}$ and $\mathbf{n}$ point in the same general direction (both pointing out)). If the net flow were inward, the flux would be negative ($\mathbf{F}$ points opposite to $\mathbf{n}$ (pointing in)).

M. S. Alkousa | Chapter 4

***

## Slide 24

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Flux Across a Simple Closed Plane Curve

*Image Description: Two illustrations demonstrating flux across a boundary.*
* *Left image: Labeled "Positive Flux". A red circle bounds a region. The blue vector field arrows start from the inside, point radially outward, and cross the red boundary to the outside. Text below says: "Field points OUT. Net flow is outward".*
* *Right image: Labeled "Negative Flux". A red circle bounds a region. The green vector field arrows point radially inward, crossing from the outside to the inside of the boundary. Text below says: "Field points IN. Net flow is inward".*

$\color{green}{\text{Figure:}}$ Left (Positive Flux): The arrows cross the red boundary from the inside to the outside. This is a "source". Right (Negative Flux): The arrows cross from the outside to the inside. This is a "sink".

M. S. Alkousa | Chapter 4

***

## Slide 25

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Line Integrals of Vector Fields: Exercises

$\color{red}{\text{Exercise 1.}}$ Find the line integrals of fields (that is, the work done by $\mathbf{F}$)
$\mathbf{F} = \sqrt{z}\hat{i} - 2x\hat{j} + \sqrt{y}\hat{k}, \quad \mathbf{F} = (3x^2 - 3x)\hat{i} + 3z\hat{j} + \hat{k}, \quad \mathbf{F} = (y + z)\hat{i} + (z + x)\hat{j} + (x + y)\hat{k}.$
$\color{red}{\text{from } (0, 0, 0) \text{ to } (1, 1, 1) \text{ over each of the following paths}}$
1. The straight-line path $C_1: \mathbf{r}(t) = t\hat{i} + t\hat{j} + t\hat{k}, \quad 0 \le t \le 1.$
2. The curved path $C_2: \mathbf{r}(t) = t\hat{i} + t^2\hat{j} + t^4\hat{k}, \quad 0 \le t \le 1.$
3. The path $C_3 \cup C_4$ consisting of the line segment from $(0, 0, 0)$ to $(1, 1, 0)$ followed by the segment from $(1, 1, 0)$ to $(1, 1, 1)$.

$\color{red}{\text{Exercise 2.}}$ Find the circulation and flux of the fields
$$\mathbf{F}_1 = x\hat{i} + y\hat{j} \quad \text{and} \quad \mathbf{F}_2 = -y\hat{i} + x\hat{j}$$
$\color{red}{\text{around and across each of the following curves.}}$
1. The circle $\mathbf{r}(t) = (\cos t)\hat{i} + (\sin t)\hat{j}, \quad 0 \le t \le 2\pi.$
2. The ellipse $\mathbf{r}(t) = (\cos t)\hat{i} + (4 \sin t)\hat{j}, \quad 0 \le t \le 2\pi.$

$\color{red}{\text{Exercise 3.}}$ Find the flux of the fields
$$\mathbf{F}_1 = 2x\hat{i} - 3y\hat{j} \quad \text{and} \quad \mathbf{F}_2 = 2x\hat{i} + (x - y)\hat{j}$$
$\color{red}{\text{across the circle } \mathbf{r}(t) = (a \cos t)\hat{i} + (a \sin t)\hat{j}, \ 0 \le t \le 2\pi, \ a > 0.}$

M. S. Alkousa | Chapter 4

***

## Slide 26

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### The Fundamental Theorem of Line Integrals: Path Independence

If $A$ and $B$ are two points in an open region $D$ in space, the line integral of $\mathbf{F}$ along $C$ from $A$ to $B$ for a field $\mathbf{F}$ defined on $D$ usually depends on the taken path $C$, as shown in the previous.

**Definition**
Let $\mathbf{F}$ be a continuous vector field with domain $D$. We say that the line integral $\int_C \mathbf{F} \cdot d\mathbf{r}$ is **independent of path** if $\int_{C_1} \mathbf{F} \cdot d\mathbf{r} = \int_{C_2} \mathbf{F} \cdot d\mathbf{r}$ for any $C_1$ and $C_2$ are two piecewise-smooth curves (which are called **paths**) that have the same initial point and the same terminal point in a domain $D$.

**Theorem (Fundamental Theorem of Line Integrals)**
*Let $C$ be a smooth curve joining the point $A$ to the point $B$ and parametrized by $\mathbf{r}(t)$. Let $f$ be a differentiable function with a continuous gradient vector $\mathbf{F} = \nabla f$ on a domain $D$ containing $C$ (i.e., $\mathbf{F}$ is conservative). Then*

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \nabla f \cdot d\mathbf{r} = f(B) - f(A).$$

*$\color{red}{\text{That is, the line integral of the conservative field is independent of the path joining A to B.}}$*

M. S. Alkousa | Chapter 4

***

## Slide 27

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### The Fundamental Theorem of Line Integrals: Path Independence

**Proof.** Suppose $C: \mathbf{r}(t) = g(t)\hat{i} + h(t)\hat{j} + k(t)\hat{k}, a \le t \le b$, is a smooth curve in $D$ joining $A$ to $B$, where $\mathbf{r}(a) = A, \mathbf{r}(b) = B$. We have
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \nabla f \cdot d\mathbf{r} = \int_{t=a}^{t=b} \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt$$
$$= \int_a^b \frac{d}{dt} f(\mathbf{r}(t)) dt = f(\mathbf{r}(b)) - f(\mathbf{r}(a)) = f(B) - f(A).$$
$\color{green}{\square}$

**Remark.** $\color{blue}{\text{Although we have proved the fundamental theorem for smooth curves, it is also true for piecewise smooth curves }} C \color{blue}{\text{. This can be seen by subdividing }} C \color{blue}{\text{ into a finite number of smooth curves and adding the resulting integrals.}}$

**Example.** Calculate the line integral $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $\mathbf{F}(x, y) = (3 + 2xy)\hat{i} + (x^2 - 3y^2)\hat{j}$, and $C$ is the curve given by $\mathbf{r}(t) = e^t \sin t \hat{i} + e^t \cos t \hat{j}, \ 0 \le t \le \pi$.

**Solution.** The field $\mathbf{F}$ is conservative $\color{red}{\text{(Why?)}}$, and $\mathbf{F} = \nabla f(x, y)$, where
$f(x, y) = 3x + x^2 y - y^3 + K$, with $K \in \mathbb{R}$ $\color{red}{\text{(Check!)}}$. We have
$\mathbf{r}(0) = (0, 1), \mathbf{r}(\pi) = (0, e^{-\pi})$, and by the Fundamental Theorem of Line Integrals we get
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \nabla f \cdot d\mathbf{r} = f((0, e^{-\pi})) - f((0, 1)) = \boxed{1 + e^{3\pi}}$$

M. S. Alkousa | Chapter 4

***

## Slide 28

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### The Fundamental Theorem of Line Integrals

**Theorem (Loop Property of Line Integrals)**
*The integral $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of path in $D$ **if and only if** $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every closed path $C$ in $D$.*

**Proof.** Let $\int_C \mathbf{F} \cdot d\mathbf{r}$ be independent of path in $D$ and $C$ is any closed path in $D$, we pick two points $A$ and $B$ on $C$ and use them to break $C$ into two pieces: $C_1$ from $A$ to $B$ followed by $C_2$ from $B$ back to $A$. Then
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} + \int_{C_2} \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} - \int_{-C_2} \mathbf{F} \cdot d\mathbf{r} = 0$$
since $C_1$ and $-C_2$ have the same initial and terminal points.

*Image Description: A diagram visually explaining path addition and subtraction in loops.*
* *Left loop diagram: A closed blue loop with two points A and B. Path $C_1$ goes from A to B (up the right side). Path $C_2$ goes from B to A (down the left side).*
* *Right loop diagram: The same loop. Path $C_1$ goes from A to B. But the path on the left is now $-C_2$ pointing from A to B instead of B to A, showing how reversing $C_2$ creates paths that start and end at the same points.*
* *A light blue arrow indicates the transition between the two concepts.*

Conversely, if it is true that $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ whenever $C$ is a closed path in $D$. Take any two paths $C_1$ and $C_2$ from $A$ to $B$ in $D$ and define $C$ to be the curve consisting of $C_1$ followed by $-C_2$. Then
$$0 = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} + \int_{-C_2} \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} - \int_{C_2} \mathbf{F} \cdot d\mathbf{r} \implies \int_{C_1} \mathbf{F} \cdot d\mathbf{r} = \int_{C_2} \mathbf{F} \cdot d\mathbf{r}.$$

M. S. Alkousa | Chapter 4

***

## Slide 29

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Conservative Fields and Curl

From the Fundamental Theorem of Line Integrals, we know that the line integral of a conservative vector field is path-independent. Therefore, we can reformulate the previous theorem as follows.

**Theorem (Loop Property of Conservative Fields)**
*The following statements are equivalent.*
1. $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$ *around every loop (that is, closed curve $C$) in $D$.*
2. *The field $\mathbf{F}$ is conservative on $D$.*

Furthermore, recall that we have shown that if $\mathbf{F}$ is conservative, then $\text{curl}(\mathbf{F}) = \mathbf{0}$, while also noting that the converse does not hold in general. The following example provides a counterexample to this converse statement.

**Example.** Let
$$\mathbf{F} = \frac{-y}{x^2 + y^2}\hat{i} + \frac{x}{x^2 + y^2}\hat{j} + 0\hat{k}.$$
Show that $\text{curl}(\mathbf{F}) = \mathbf{0}$, and it is not conservative over its natural domain.

**Solution:** With simple calculations, we can show that $\text{curl}(\mathbf{F}) = \mathbf{0}$ $\color{red}{\text{(check!)}}$.

M. S. Alkousa | Chapter 4

***

## Slide 30

**Introduction to Vector Calculus | Line Integrals | Surface Integrals**

### Conservative Fields and Curl

Let us consider the unit circle $C$ in the $xy$-plane (loop), parametrized by
$$\mathbf{r}(t) = (\cos t)\hat{i} + (\sin t)\hat{j}, \quad 0 \le t \le 2\pi.$$

To show that $\mathbf{F}$ is not conservative, we will compute the line integral $\oint_C \mathbf{F} \cdot d\mathbf{r}$ around $C$.

In terms of the parameter $t$, we have
$$\mathbf{F} = \frac{-y}{x^2 + y^2}\hat{i} + \frac{x}{x^2 + y^2}\hat{j} = \frac{-\sin t}{\sin^2 t + \cos^2 t}\hat{i} + \frac{\cos t}{\sin^2 t + \cos^2 t}\hat{j} = (-\sin t)\hat{i} + (\cos t)\hat{j}.$$

Also,
$$\frac{d\mathbf{r}}{dt} = (-\sin t)\hat{i} + (\cos t)\hat{j}.$$

So the line integral becomes
$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} \mathbf{F} \cdot \frac{d\mathbf{r}}{dt} dt = \int_0^{2\pi} (\sin^2 t + \cos^2 t) dt = 2\pi \neq 0.$$

Hence, $\mathbf{F}$ is not conservative.

M. S. Alkousa | Chapter 4

## Slide 31: The Fundamental Theorem of Line Integrals

**Theorem (Conservative Fields are Gradient Fields)**
Suppose $\mathbf{F}$ is a vector field that is continuous on an *open connected region* $D$. If $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of path in $D$, then $\mathbf{F}$ is a conservative vector field on $D$; that is, there exists a function $f$ such that $\nabla f = \mathbf{F}$.

**Remark.** This theorem and the Fundamental Theorem of Line Integral say that $\mathbf{F} = \nabla f$ **if and only if**, for any two points $A$ and $B$ in the region $D$, the value of the line integral $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of the path $C$ joining $A$ to $B$ in $D$.

**Exercises.** Find a function $f$ such that $\mathbf{F} = \nabla f$ and use the answer to evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ along the given curve $C$.
**(1)** $\mathbf{F}(x, y, z) = (y^2 z + 2xz^2)\hat{i} + 2xyz\hat{j} + (xy^2 + 2x^2 z)\hat{k}$, 
$C : x = \sqrt{t}, y = t + 1, z = t^2, \ 0 \leq t \leq 1;$

**(2)** $\mathbf{F}(x, y, z) = yze^{xz}\hat{i} + e^{xz}\hat{j} + xye^{xz}\hat{k}$, 
$C : \mathbf{r}(t) = (t^2 + 1)\hat{i} + (t^2 - 1)\hat{j} + (t^2 - 2t)\hat{k}, \ 0 \leq t \leq 2.$

---

## Slide 32: Green’s Theorem

Green’s Theorem gives the relationship between a line integral around a simple closed curve $C$ (that is, the work or flux integral over a closed curve in the plane, or the circulation of a field around a closed curve in the plane) and a double integral over the plane region $D$ bounded by $C$.

> **Image Description:** 
> Two coordinate plane graphs are shown, demonstrating the orientation of a curve $C$ bounding a region $D$. 
> *   **Left Graph (Positive orientation):** The region $D$ is an irregular, blob-like shape in the $xy$-plane. The boundary curve $C$ has arrows indicating a counterclockwise direction. As the curve is traversed, the region $D$ remains to the left.
> *   **Right Graph (Negative orientation):** The same region $D$ is shown, but the boundary curve $C$ has arrows indicating a clockwise direction. As the curve is traversed, the region $D$ is on the right.

**Figure:** The curve is traversed counterclockwise, and said to be **positively oriented**, if the region it encloses is always to the **left** when moving along the curve. If the curve is traversed clockwise, then the enclosed region is on the **right** when moving along the curve, and the curve is said to be **negatively oriented**.

---

## Slide 33: Green’s Theorem

**Theorem (Green’s Theorem)**
*Let $C$ be a **positively oriented, piecewise-smooth, simple and closed curve** enclosing a region $D$ in the plane. If $M(x, y)$ and $Q(x, y)$ have continuous partial derivatives on an open region that contains $D$, then*
$$ \oint_C M dx + N dy = \int_C M dx + N dy = \iint_D \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA = \int_{\partial D} M dx + N dy. $$

**Proof.** See the proof, for some special simply connected regions, in Thomas2024, page 969.

**Example.** Calculate the integral $I = \oint_C \left( 3y - e^{\sin x} \right) dx + \left( 7x + \sqrt{y^4 + 1} \right) dy$, where $C$ is the circle $x^2 + y^2 = 9$.

**Solution.** The region $D$ bounded by $C$ is the disk $x^2 + y^2 \leq 9$. By Green’s Theorem, we find:
$$ I = \iint_D \left( \frac{\partial}{\partial x} \left( 7x + \sqrt{y^4 + 1} \right) - \frac{\partial}{\partial y} \left( 3y - e^{\sin x} \right) \right) dA $$
$$ = \int_0^{2\pi} \int_0^3 (7 - 3) r \, dr \, d\theta = 4 \int_0^{2\pi} d\theta \int_0^3 r \, dr = \mathbf{36\pi} $$

---

## Slide 34: Green’s Theorem for Non Simply-Connected Regions

**Remark.** Green’s Theorem can be extended to apply to regions with holes, that is, regions that are **not simply-connected**. Observe that the boundary $C$ of the region $D$ in the inserted figure consists of two simple closed curves $C_1$ and $C_2$. We assume that these boundary curves are oriented so that the region $D$ is always on the left as the curve $C$ is traversed. Thus, the positive direction is counterclockwise for the outer curve $C_1$ but clockwise for the inner curve $C_2$. If we divide $D$ into two regions $D'$ and $D''$ by means of the lines shown in the figure and then apply Green’s Theorem to each of $D'$ and $D''$, we get

> **Image Description:**
> The image displays two stages of a region $D$ with a hole.
> *   **Top diagram:** A larger outer blob bounded by a counterclockwise curve $C_1$ and an inner white "hole" bounded by a clockwise curve $C_2$. The shaded region between them is $D$.
> *   **Bottom diagram:** The region $D$ is split into an upper half $D'$ and a lower half $D''$ by two horizontal line segments. Arrows on the boundary of $D'$ and $D''$ show that along the dividing lines, the integration directions are opposite and will cancel each other out.

$$ \iint_D \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA = \iint_{D'} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA + \iint_{D''} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA $$
$$ = \int_{\partial D'} M dx + N dy + \int_{\partial D''} M dx + N dy. $$

Since the line integrals along the common boundary lines are in opposite directions, they cancel, and we get
$$ \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \int_{C_1} P dx + Q dy + \int_{C_2} P dx + Q dy = \int_C P dx + Q dy, $$
which is Green’s Theorem for the region $D$.

---

## Slide 35: Green’s Theorem

**Example.** Let $\mathbf{F} = -\frac{y}{x^2 + y^2}\hat{i} + \frac{x}{x^2 + y^2}\hat{j}$. Calculate the integral $\int_C \mathbf{F} \cdot d\mathbf{r}$, for any positively oriented simple closed path $C$ that encloses the origin.

> **Image Description:**
> A coordinate plane shows an arbitrarily shaped, positively oriented (counterclockwise) closed curve $C$. Completely inside $C$, there is a smaller, positively oriented circle $C'$ centered at the origin. The region between $C$ and $C'$ is shaded and labeled $D$.

**Solution.** Since $C$ is an arbitrary closed path that encloses the origin, it’s difficult to compute the given integral directly. So let’s consider a counterclockwise-oriented circle $C'$ with center the origin and radius $r$, where $r$ is chosen to be small enough that $C'$ lies inside $C$. Let $D$ be the region bounded by $C$ and $C'$.
Then its positively oriented boundary is $C \cup (-C')$ and so the general version of Green’s Theorem gives

$$ \int_C M dx + N dy + \int_{-C'} M dx + N dy = \int_{C \cup (-C')} \mathbf{F} \cdot d\mathbf{r} $$
$$ = \iint_D \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA = \iint_D \left( \frac{y^2 - x^2}{(x^2 + y^2)^2} - \frac{y^2 - x^2}{(x^2 + y^2)^2} \right) dA = 0. $$

Therefore $\int_C M dx + N dy = \int_{C'} M dx + N dy \implies \color{red}{\int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C'} \mathbf{F} \cdot d\mathbf{r}}.$
Using the parametrization given by $\mathbf{r}(t) = r \cos t \mathbf{i} + r \sin t \mathbf{j}, \ 0 \leq t \leq 2\pi$, we find
$$ \int_{C'} \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt = \int_0^{2\pi} \frac{(-r \sin t)(-r \sin t) + (r \cos t)(r \cos t)}{r^2 \cos^2 t + r^2 \sin^2 t} dt = \mathbf{2\pi} $$

---

## Slide 36: Green’s Theorem: Exercises

**Exercise 1.** Use Green’s Theorem to evaluate the line integral along the given positively oriented curve.
**(1)** $\int_C ye^x dx + 2e^x dy$, where $C$ is the rectangle with vertices $(0, 0), (3, 0), (3, 4)$, and $(0, 4)$;
**(2)** $\int_C (x^2 + y^2) dx + (x^2 - y^2) dy$, where $C$ is the triangle with vertices $(0, 0), (2, 1)$, and $(0, 1)$;
**(3)** $\int_C y^4 dx + 2xy^3 dy$, where $C$ is the ellipse $x^2 + 2y^2 = 2$;
**(4)** $\int_C (1 - y^3) dx + (x^3 + e^{y^2}) dy$, where $C$ is the boundary of the region between the circles $x^2 + y^2 = 4$ and $x^2 + y^2 = 9$.

**Exercise 2.** Find the counterclockwise circulation and outward flux for the field $\mathbf{F}(x, y) = \sqrt{1 + x^2}\hat{i} + \arctan x\hat{j}$, around and across $C$, which is the triangle from $(0, 0)$ to $(1, 1)$ to $(0, 1)$ to $(0, 0)$.

**Exercise 3.** Use Green’s Theorem to find the work done by the force $\mathbf{F}(x, y) = x(x + y)\hat{i} + xy^2\hat{j}$ in moving a particle from the origin along the $x$-axis to $(1, 0)$, then along the line segment to $(0, 1)$, and then back to the origin along the $y$-axis.

---

## Slide 37: Green’s Theorem: Exercises

**Exercise 4.** A particle starts at the origin, moves along the $x$-axis to $(5, 0)$, then along the quarter-circle $x^2 + y^2 = 25, \ x \geq 0, y \geq 0$, to the point $(0, 5)$, and then down the $y$-axis back to the origin. Use Green’s Theorem to find the work done on this particle by the force field $\mathbf{F}(x, y) = \sin x\hat{i} + (\sin y + xy^2 + \frac{1}{3}x^3)\hat{j}$.

**Exercise 5.** (Region with a hole.) Find the integral $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $\mathbf{F}(x, y) = \frac{2xy\hat{i} + (y^2 - x^2)\hat{j}}{(x^2 + y^2)^2}$, and $C$ is any positively oriented simple closed curve that encloses the origin.

**Exercise 6.** Find the counterclockwise circulation and the outward flux of the field $\mathbf{F}(x, y) = (-\sin y)\hat{i} + (x \cos y)\hat{j}$ around and across the boundary of the square $0 \leq x \leq \pi/2, \ 0 \leq y \leq \pi/2$.

**Exercise 7.** Find the outward flux of the field
$$ \mathbf{F}(x, y) = \left( 3xy - \frac{x}{1 + y} \right) \hat{i} + (e^x + \arctan y)\hat{j} $$
across the cardioid $r = a(1 + \cos \theta), \ a > 0$.

**Exercise 8.** Find the counterclockwise circulation of $\mathbf{F}(x, y) = (y + e^x \ln y)\hat{i} + (exy)\hat{j}$ around the boundary of the region that is bounded above by the curve $y = 3 - x^2$ and below by the curve $y = x^4 + 1$.

---

## Slide 38: Parametric surfaces

We have already studied several special classes of surfaces: cylinders, quadric surfaces, graphs of two-variable functions, and level surfaces of three-variable functions. Now we turn to a broader class, called **parametric surfaces**, which are described using vector functions.

We have described curves in the plane in three different ways.
*   Explicit form: $y = f(x)$.
*   Implicit form: $F(x, y) = 0$.
*   Parametric vector form: $\mathbf{r}(t) = x(t)\hat{i} + y(t)\hat{j}, \quad a \leq t \leq b$.

We have analogous descriptions of surfaces in space.
*   Explicit form: $z = f(x, y)$.
*   Implicit form: $F(x, y, z) = 0$.

Suppose that
$$ \mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}, \qquad (4) $$
is a continuous vector-valued function defined on a region $D$ in the $uv$-plane, and is one-to-one on the interior of the $D$. We call the range of $\mathbf{r}$ the **surface** $S$ defined or traced by $\mathbf{r}$. Equation (4) together with the domain $D$ constitutes a **parametrization** of the surface. The variables $u$ and $v$ are the **parameters**, and $D$ is the **parameter domain**.
$\color{red}{\text{The requirement that } \mathbf{r} \text{ be one-to-one on the interior of } D \text{ ensures that } S \text{ does not cross itself.}}$

---

## Slide 39: Parametric surfaces

> **Image Description:**
> The image illustrates the mapping of a parameter domain $D$ in the $uv$-plane to a surface $S$ in the $xyz$-space using a vector function $\mathbf{r}$. 
> *   **Top Pair:** A domain $D$ in the $uv$-plane is mapped via arrow $\mathbf{r}$ to a smooth 3D surface patch $S$ in $xyz$-space. A specific point $(u, v)$ in $D$ is mapped to a position vector $\mathbf{r}(u, v)$ on the surface $S$.
> *   **Bottom Pair:** Highlights grid curves. In the $uv$-plane, a horizontal line $v=v_0$ and a vertical line $u=u_0$ intersect at $(u_0, v_0)$. When mapped via $\mathbf{r}$, the line $v=v_0$ transforms into a curve $C_1$ on the surface $S$, and the line $u=u_0$ transforms into a curve $C_2$ on the surface $S$. Their intersection on the surface is $\mathbf{r}(u_0, v_0)$.

**Figure:** If we keep $u$ constant by putting $u = u_0$, then $\mathbf{r}(u_0, v)$, becomes a vector function of the single parameter $v$ and defines a curve $C_1$ lying on $S$. Similarly, if we keep $v$ constant by putting $v = v_0$, we get a curve $C_2$ given by $\mathbf{r}(u, v_0)$ that lies on $S$.

---

## Slide 40: Parametric surfaces (Plane in the Space)

**Example 1.**
Let $\mathbf{a}$ and $\mathbf{b}$ be two nonparallel vectors. For the vector function that represents the plane that passes through the point $P_0$ with position vector $\mathbf{r}_0$ and contains $\mathbf{a}, \mathbf{b}$. Let $P$ be any point in the plane, so there are scalars $u$ and $v$ such that $\overrightarrow{P_0P} = u \mathbf{a} + v \mathbf{b}$ $\color{red}{\text{(Why?)}}$.

> **Image Description:**
> A parallelogram in 3D space forms a plane. Point $P_0$ is one vertex. A blue vector $u\mathbf{a}$ lies along the bottom edge, and a blue vector $v\mathbf{b}$ lies along the left edge. Their vector sum points from $P_0$ to point $P$ at the opposite vertex. Base vectors $\mathbf{a}$ and $\mathbf{b}$ are drawn in magenta extending from $P_0$.

If $\mathbf{r}$ is the position vector of $P$, then
$$ \mathbf{r}(u, v) = \overrightarrow{OP_0} + \overrightarrow{P_0P} = \mathbf{r}_0 + u\mathbf{a} + v\mathbf{b} \quad \forall u, v \in \mathbb{R}. $$

If we write the vectors $\mathbf{r} = (x, y, z), \mathbf{r}_0 = (x_0, y_0, z_0), \mathbf{a} = (a_1, a_2, a_3)$, and $\mathbf{b} = (b_1, b_2, b_3)$, then we can write the parametric equations of the plane through the point $(x_0, y_0, z_0)$ as follows:
$$ x = x_0 + ua_1 + vb_1, \quad y = y_0 + ua_2 + vb_2, \quad z = z_0 + ua_3 + vb_3, \quad \forall u, v \in \mathbb{R}. $$

---

## Slide 41: Parametric surfaces (Cone)

**Example 2.** For the cone $z = \sqrt{x^2 + y^2}, \ 0 \leq z \leq 1$.
The cylindrical coordinates provide a parametrization as follows. For any point $(x, y, z)$ on the cone, we have
$$ x = r \cos \theta, \ y = r \sin \theta, \ z = \sqrt{x^2 + y^2} = r, $$
with $0 \leq r \leq 1$ and $0 \leq \theta \leq 2\pi$. Taking $u = r$ and $v = \theta$ in (4), we get the following parametrization
$$ \mathbf{r}(r, \theta) = (r \cos \theta)\hat{i} + (r \sin \theta)\hat{j} + r\hat{k}, $$
with $0 \leq r \leq 1, \ 0 \leq \theta \leq 2\pi$.

> **Image Description:**
> An upward-opening cone in an $xyz$-coordinate system. The tip is at the origin and the top is a circular cross section at $z=1$. A point on the cone is defined by a position vector $\mathbf{r}(r, \theta)$. The diagram illustrates the cylindrical coordinates mappings: the distance $r$ from the $z$-axis, the angle $\theta$ from the $x$-axis, and the resulting coordinates $(x, y, z) = (r\cos\theta, r\sin\theta, r)$.

This parametrization is one-to-one on the interior of the domain, though not on the boundary where $r = 0$ (mapped to the tip of the cone) or where $\theta = 0$ or $\theta = 2\pi$ (where the cone glues together along a seam above the $x$-axis). That is,
*   When $r = 0$, we get $\mathbf{r}(0, \theta) = 0\hat{i} + 0\hat{j} + 0\hat{k}$, for any $\theta \in[0, 2\pi]$.
*   When $\theta = 0$ or $\theta = 2\pi$, we get $\mathbf{r}(r, 0) = r\hat{i} + 0\hat{j} + r\hat{k} = \mathbf{r}(r, 2\pi)$, for any $r \in [0, 1]$.
    So the edge $\theta = 0$ and the edge $\theta = 2\pi$ map to the same curve on the cone.

---

## Slide 42: Parametric surfaces (Sphere)

**Example 3.** Spherical coordinates provide a parametrization of the sphere $x^2 + y^2 + z^2 = a^2$, as follows.
The point $(x, y, z)$ on the sphere has the following coordinates
$$ x = a \sin \phi \cos \theta, \ y = a \sin \phi \sin \theta, \ z = a \cos \phi, $$
with $0 \leq \phi \leq \pi$ and $0 \leq \theta \leq 2\pi$.

> **Image Description:**
> A sphere of radius $a$ in $xyz$-coordinates. The radius vector $\mathbf{r}(\phi, \theta)$ points to the surface. The angle $\phi$ is shown measured down from the positive $z$-axis to the vector. The angle $\theta$ is shown in the $xy$-plane measured from the $x$-axis to the vector's projection. The point on the sphere is $(x, y, z) = (a\sin\phi\cos\theta, a\sin\phi\sin\theta, a\cos\phi)$.

Taking $u = \phi$ and $v = \theta$ in (4), for $0 \leq \phi \leq \pi, \ 0 \leq \theta \leq 2\pi$, gives the following parametrization
$$ \mathbf{r}(\phi, \theta) = (a \sin \phi \cos \theta)\hat{i} + (a \sin \phi \sin \theta)\hat{j} + (a \cos \phi)\hat{k}, $$

Again, the parametrization is one-to-one on the interior of the domain, though not on its boundary.

---

## Slides 43 & 44: Smooth Surface and Tangent Plane

*(Note: Slide 44 is entirely composed of the image that illustrates the text on Slide 43. They are combined here for clarity.)*

Let $S$ be a parametric surface traced out by a vector function
$$ \mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}, $$
and $P_0 \in S$ with position vector $\mathbf{r}(u_0, v_0)$. If we keep $u$ constant by putting $u = u_0$, then $\mathbf{r}(u_0, v)$ becomes a vector function of the single parameter $v$ and defines a grid curve $C_1$ lying on $S$. The tangent vector to $C_1$ at $P_0$ is obtained by taking the partial derivative of $\mathbf{r}$ with respect to $v$:
$$ \mathbf{r}_v = \frac{\partial x}{\partial v}(u_0, v_0)\hat{i} + \frac{\partial y}{\partial v}(u_0, v_0)\hat{j} + \frac{\partial z}{\partial v}(u_0, v_0)\hat{k}. $$
Similarly, if $v = v_0$ is a constant, we get a grid curve $C_2$ given by $\mathbf{r}(u, v_0)$ that lies on $S$, and its tangent vector at $P_0$ is
$$ \mathbf{r}_u = \frac{\partial x}{\partial u}(u_0, v_0)\hat{i} + \frac{\partial y}{\partial u}(u_0, v_0)\hat{j} + \frac{\partial z}{\partial u}(u_0, v_0)\hat{k}. $$

**Definition (Smooth surface, tangent plane)**
A parametrized surface $\mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}$ is **smooth** (it has no “corners”) if $\mathbf{r}_u = \frac{\partial \mathbf{r}}{\partial u}$ and $\mathbf{r}_v = \frac{\partial \mathbf{r}}{\partial v}$ are continuous and if $\mathbf{r}_u \times \mathbf{r}_v$ is never zero on the interior of the parameter domain. For a smooth surface, the **tangent plane** is the plane that contains the tangent vectors $\mathbf{r}_u$ and $\mathbf{r}_v$, and the vector $\mathbf{r}_u \times \mathbf{r}_v$ is a normal vector to the tangent plane.

> **Image Description (from Slide 44):**
> A visualization of mapping domain $D$ to a surface $S$.
> *   **Left side:** A 2D parameter domain $D$ in the $uv$-plane. Two crossing lines are marked: a horizontal line $v = v_0$ and a vertical line $u = u_0$. They intersect at $(u_0, v_0)$.
> *   **Right side:** The mapped 3D surface patch in the $xyz$-plane. The horizontal line maps to curve $C_1$ and the vertical line maps to curve $C_2$. They intersect at point $P_0$. At $P_0$, two tangent vectors are drawn: $\mathbf{r}_v$ tangent to $C_1$, and $\mathbf{r}_u$ tangent to $C_2$.

---

## Slide 45: Surface Area

Now consider a small rectangle $\Delta A_{uv}$ in $D := \{(u, v) \in [a, b] \times [c, d]\}$ with sides on the lines $u = u_0, u = u_0 + \Delta u, v = v_0$, and $v = v_0 + \Delta v$. Each side of $\Delta A_{uv}$ maps onto a curve on the surface $S$, and together these four curves bound a “curved patch element” $\Delta \sigma_{uv}$.

> **Image Description:**
> Three connected diagrams explaining the geometry of a surface patch.
> *   **Left Diagram:** Shows the parameter domain $D$ in the $uv$-plane with a small rectangular highlighted region $\Delta A_{uv}$ defined by bounds $[u_0, u_0+\Delta u]$ and $[v_0, v_0+\Delta v]$. 
> *   **Middle Diagram:** A red arrow labeled "Parametrization" points from the $uv$-plane to a 3D surface $S$ in $xyz$-space. The small rectangle maps to a curved blue patch element labeled $\Delta \sigma_{uv}$. The bounding curves are $C_1: v=v_0$, $C_2: u=u_0$, $v=v_0+\Delta v$, and $u=u_0+\Delta u$. The bottom-left corner of the patch is $P_0$.
> *   **Right Diagram:** A zoomed-in view of the patch. The base corner is $P_0$. The tangent vectors $\Delta u \mathbf{r}_u$ and $\Delta v \mathbf{r}_v$ define a flat parallelogram approximating the curved patch. A vector normal to this parallelogram is shown pointing upwards as $\mathbf{r}_u \times \mathbf{r}_v$.

**Figure:** The side $v = v_0$ maps to curve $C_1$, the side $u = u_0$ maps onto $C_2$, and their common vertex $(u_0, v_0)$ maps to $P_0$. The partial derivative vector $\mathbf{r}_u(u_0, v_0)$ is tangent to $C_1$ at $P_0$, and $\mathbf{r}_v(u_0, v_0)$ is tangent to $C_2$ at $P_0$. The cross product $\mathbf{r}_u \times \mathbf{r}_v$ is normal to the surface at $P_0$ (recall that we assumed $\mathbf{r}_u \times \mathbf{r}_v \neq \mathbf{0}$).

---

## Slide 46: Surface Area

We next approximate the surface patch element $\Delta \sigma_{uv}$ by the parallelogram on the tangent plane whose sides are determined by the vectors $\Delta u \mathbf{r}_u$ and $\Delta v \mathbf{r}_v$. The area of this parallelogram is
$$ \|\Delta u \mathbf{r}_u \times \Delta v \mathbf{r}_v\| = \|\mathbf{r}_u \times \mathbf{r}_v\| \Delta u \Delta v. $$

A partition of the region $D$ in the $uv$-plane by rectangular regions $\Delta A_{uv}$ induces a partition of the surface $S$ into surface patch elements $\Delta \sigma_{uv}$. We approximate the area of each surface patch element $\Delta \sigma_{uv}$ by the parallelogram area and sum these areas together to obtain an approximation of the surface area of $S$:
$$ \sum_n \|\mathbf{r}_u \times \mathbf{r}_v\| \Delta u \Delta v. $$

As $\Delta u$ and $\Delta v$ approach zero independently, the number of area elements $n$ approaches $\infty$ and the continuity of $\mathbf{r}_u$ and $\mathbf{r}_v$ guarantees that the sum approaches the double integral $\iint_D \|\mathbf{r}_u \times \mathbf{r}_v\| du \, dv$. $\color{red}{\text{Let } d\sigma := \|\mathbf{r}_u \times \mathbf{r}_v\| du \, dv}$ denote the **surface area differential** (it is analogous to the arc length differential $ds$ in line integrals).

**Definition**
The **area** of the smooth surface $\mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}$, is
$$ \color{red}{A = \iint_S d\sigma = \iint_D \|\mathbf{r}_u \times \mathbf{r}_v\| du \, dv.} $$

---

## Slide 47: Surface Area: Examples

**Example 1.**
Find the surface area of the cone $z = \sqrt{x^2 + y^2}$ with $0 \leq z \leq 1$.

**Solution.** For this cone, we found the parametrization
$$ \mathbf{r}(r, \theta) = (r \cos \theta)\hat{i} + (r \sin \theta)\hat{j} + r\hat{k}, \quad 0 \leq r \leq 1, \quad 0 \leq \theta \leq 2\pi. $$
Thus,
$$ \mathbf{r}_r \times \mathbf{r}_\theta = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \cos \theta & \sin \theta & 1 \\ -r \sin \theta & r \cos \theta & 0 \end{vmatrix} = -(r \cos \theta)\hat{i} - (r \sin \theta)\hat{j} + r\hat{k}. $$
Thus,
$$ \|\mathbf{r}_r \times \mathbf{r}_\theta\| = \sqrt{r^2 \cos^2 \theta + r^2 \sin^2 \theta + r^2} = \sqrt{2} r. $$

Therefore, the area of the given cone is
$$ A = \iint_S d\sigma = \int_0^{2\pi} \int_0^1 \|\mathbf{r}_r \times \mathbf{r}_\theta\| \, dr \, d\theta = \int_0^{2\pi} \int_0^1 \sqrt{2} r \, dr \, d\theta = \frac{\sqrt{2}}{2}(2\pi) = \mathbf{\sqrt{2}\pi} $$

---

## Slide 48: Surface Area: Examples

**Example 2.** Find the surface area of a sphere of radius $a$.

**Solution.** For this sphere, we found the parametrization
$$ \mathbf{r}(\phi, \theta) = (a \sin \phi \cos \theta)\hat{i} + (a \sin \phi \sin \theta)\hat{j} + (a \cos \phi)\hat{k}, \quad 0 \leq \phi \leq \pi, \ 0 \leq \theta \leq 2\pi. $$

For $\mathbf{r}_\phi \times \mathbf{r}_\theta$, we get
$$ \mathbf{r}_\phi \times \mathbf{r}_\theta = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a \cos \phi \cos \theta & a \cos \phi \sin \theta & -a \sin \phi \\ -a \sin \phi \sin \theta & a \sin \phi \cos \theta & 0 \end{vmatrix} $$
$$ = (a^2 \sin^2 \phi \cos \theta)\hat{i} + (a^2 \sin^2 \phi \sin \theta)\hat{j} + (a^2 \sin \phi \cos \phi)\hat{k}. $$

Thus,
$$ \|\mathbf{r}_\phi \times \mathbf{r}_\theta\| = \sqrt{a^4 \sin^4 \phi \cos^2 \theta + a^4 \sin^4 \phi \sin^2 \theta + a^4 \sin^2 \phi \cos^2 \phi} = a^2 \sqrt{\sin^2 \phi} = a^2 \sin \phi. $$

Therefore, the area of the given sphere is
$$ A = \int_0^{2\pi} \int_0^\pi a^2 \sin \phi \, d\phi \, d\theta = \int_0^{2\pi} \left[ -a^2 \cos \phi \right]_0^\pi d\theta = \int_0^{2\pi} 2a^2 \, d\theta = \mathbf{4\pi a^2} $$

---

## Slide 49: Explicit Surfaces: Surface area of the graph of an explicit function

For the special case of a surface $S$ with equation $z = f(x, y)$, where $(x, y)$ lies in $D$ and $f$ has continuous partial derivatives, we take $x$ and $y$ as parameters, and we get the following parametric equations
$$ x = x, \quad y = y, \quad z = f(x, y). $$
So
$$ \mathbf{r}_x = \hat{i} + \left( \frac{\partial f}{\partial x} \right) \hat{k}, \quad \mathbf{r}_y = \hat{j} + \left( \frac{\partial f}{\partial y} \right) \hat{k}. $$
Thus,
$$ \mathbf{r}_x \times \mathbf{r}_y = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 0 & \frac{\partial f}{\partial x} \\ 0 & 1 & \frac{\partial f}{\partial y} \end{vmatrix} = -\frac{\partial f}{\partial x}\hat{i} - \frac{\partial f}{\partial y}\hat{j} + \hat{k}, $$
and
$$ \|\mathbf{r}_x \times \mathbf{r}_y\| = \sqrt{\left( \frac{\partial f}{\partial x} \right)^2 + \left( \frac{\partial f}{\partial y} \right)^2 + 1} = \sqrt{1 + \left( \frac{\partial z}{\partial x} \right)^2 + \left( \frac{\partial z}{\partial y} \right)^2}. $$

Therefore, the surface area formula becomes
$$ A(S) = \iint_D \sqrt{1 + \left( \frac{\partial z}{\partial x} \right)^2 + \left( \frac{\partial z}{\partial y} \right)^2} \, dA $$

---

## Slide 50: Implicit Surfaces: Surface area of the graph of an implicit function

Surfaces are often presented as level sets of a function, described by an equation such as $F(x, y, z) = c$, for some constant $c$. Such a level surface does not come with an explicit parametrization and is called an **implicitly defined surface**. It may be difficult to find explicit formulas for the functions $x(u, v), y(u, v)$, and $z(u, v)$ that describe the surface in the form
$$ \mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}. $$

$\color{blue}{\text{We now show how to compute the surface area differen-}}$
$\color{blue}{\text{tial } d\sigma \text{ for implicit surfaces.}}$

> **Image Description:**
> A 3D diagram showing a surface $S$ labeled "Surface $F(x, y, z) = c$" floating above the $xy$-plane. Below the surface is its vertical projection, a flat blue region labeled $R$, on a coordinate plane. The text "The vertical projection or 'shadow' of $S$ on a coordinate plane" points to $R$. An upward unit vector $\mathbf{p}$ is drawn perpendicular to region $R$.

We have a surface defined by the equation $F(x, y, z) = c$. Let us choose $\mathbf{p}$ to be a unit vector normal to the plane region $R$. We assume that the surface is **smooth** ($F$ is differentiable, $\nabla F$ is nonzero and continuous on $S$) and that $\nabla F \cdot \mathbf{p} \neq 0$.

Assume that the normal vector $\mathbf{p}$ is the unit vector $\mathbf{k}$, so the region $R$ lies in the $xy$-plane. By assumption, we then have $\nabla F \cdot \mathbf{p} = \nabla F \cdot \mathbf{k} = F_z \neq 0$ on $S$.

---

## Slide 51: Implicit Surfaces: Surface area of the graph of an implicit function

The Implicit Function Theorem implies that $S$ is then the graph of a differentiable function $z = h(x, y)$, although the function $h(x, y)$ is **not** explicitly known.
Define the parameters $u$ and $v$ by $u = x$ and $v = y$. Then $z = h(u, v)$, and
$$ \mathbf{r}(u, v) = u\hat{i} + v\hat{j} + h(u, v)\hat{k} $$
gives a parametrization of the surface $S$. Applying the Chain Rule for implicit differentiation, we get
$$ \mathbf{r}_u = \hat{i} + \frac{\partial h}{\partial u}\hat{k} = \hat{i} - \frac{F_x}{F_z}\hat{k} \quad \text{and} \quad \mathbf{r}_v = \hat{j} + \frac{\partial h}{\partial v}\hat{k} = \hat{j} - \frac{F_y}{F_z}\hat{k}. $$

Therefore, we have
$$ \mathbf{r}_u \times \mathbf{r}_v = \frac{F_x}{F_z}\hat{i} + \frac{F_y}{F_z}\hat{j} + \hat{k} = \frac{1}{F_z}(F_x\hat{i} + F_y\hat{j} + F_z\hat{k}) = \frac{\nabla F}{\nabla F \cdot \mathbf{k}} = \frac{\nabla F}{\nabla F \cdot \mathbf{p}}. $$

Therefore, the surface area differential is given by
$$ \color{red}{d\sigma = \|\mathbf{r}_u \times \mathbf{r}_v\| \, du \, dv = \frac{\|\nabla F\|}{|\nabla F \cdot \mathbf{p}|} dx \, dy, \quad u = x \text{ and } v = y.} $$

**Remark.** We obtain similar calculations if instead the vector $\mathbf{p} = \hat{j}$ is normal to the $xz$-plane when $F_y \neq 0$ on $S$, or if $\mathbf{p} = \hat{i}$ is normal to the $yz$-plane when $F_x \neq 0$ on $S$.

---

## Slide 52: Implicit Surfaces: Surface area of the graph of an implicit function

**Definition (Formula for the Surface Area of an Implicit Surface)**
The area of the surface $F(x, y, z) = c$ over a closed and bounded plane region $R$ is
$$ \color{red}{\text{Surface area} = \iint_S d\sigma = \iint_R \frac{\|\nabla F\|}{|\nabla F \cdot \mathbf{p}|} dA,} $$
where $\mathbf{p} = \hat{i}, \hat{j}$, or $\hat{k}$ is normal to $R$ and $\nabla F \cdot \mathbf{p} \neq 0$.

**Example.** For the surface area of the spherical band: $x^2 + y^2 + z^2 = 4$, between the plane $z = -1$, and $z = 3$. We have $F(x, y, z) = x^2 + y^2 + z^2 - 4 = 0$, Thus
$$ \nabla F = (2x, 2y, 2z)^\top \implies \|\nabla F\| = \sqrt{4x^2 + 4y^2 + 4z^2} = 2\sqrt{x^2 + y^2 + z^2} = 4. $$

We project $S$ onto the $xy$-plane (the projection is $R = \{(x, y) | \ 1 \leq x^2 + y^2 \leq 3\}$), so $\mathbf{p} = \hat{k}$, and $\nabla F \cdot \mathbf{p} = 2z$.

$$ \text{Surface area} = \iint_R \frac{\|\nabla F\|}{|\nabla F \cdot \mathbf{p}|} dA = \iint_R \frac{4}{|2z|} dA = \iint_{1 \leq x^2 + y^2 \leq 3} \frac{2}{\sqrt{x^2 + y^2 - 4}} dA $$
$$ = \int_0^{2\pi} \int_1^{\sqrt{3}} \frac{2r}{\sqrt{4 - r^2}} \, dr \, d\theta = 2\pi \int_1^{\sqrt{3}} \frac{2r}{\sqrt{4 - r^2}} \, dr \, d\theta = \mathbf{4\pi \left(1 + \sqrt{3}\right)} $$

---

## Slide 53: Parametric surfaces and Their Areas: Exercises

**Exercise 1.** Determine whether the points $P$ and $Q$ lie on the given surface.
**(1)** $\mathbf{r}(u, v) = (u + v)\hat{i}, (u - 2v)\hat{j} + (3 + u - v)\hat{k}, \quad P(4, -5, 1), \ Q(0, 4, 6);$
**(2)** $\mathbf{r}(u, v) = (1 + u - v)\hat{i}, (u + v^2)\hat{j} + (u^2 - v^2)\hat{k}, \quad P(1, 2, 1), \ Q(2, 3, 3).$

**Exercise 2.** Identify the surface with the given vector equation.
**(1)** $\mathbf{r}(u, v) = (u + v)\hat{i} + (3 - v)\hat{j} + (1 + 4u + 5v)\hat{k};$
**(2)** $\mathbf{r}(u, v) = u^2\hat{i} + u \cos v\hat{j} + u \sin v\hat{k};$
**(3)** $\mathbf{r}(s, t) = 3 \cos t\hat{i} + s\hat{j} + \sin t\hat{k}, \quad -1 \leq s \leq 1.$

**Exercise 3.** Find a parametric representation for the surface.
**(1)** The plane that passes through the point $(0, -1, 5)$ and contains the vectors $(2, 1, 4)$ and $(-3, 2, 5)$.
**(2)** The part of the hyperboloid $4x^2 - 4y^2 - z^2 = 4$ that lies in front of the $yz$-plane.
**(3)** The part of the cylinder $x^2 + z^2 = 9$ that lies above the $xy$-plane and between the planes $y = -4$ and $y = 4$.
**(4)** The part of the sphere $x^2 + y^2 + z^2 = 36$ that lies between the planes $z = 0$ and $z = 3\sqrt{3}$.

**Exercise 4.** Find the area of the surface.
**(1)** The part of the surface $z = 4 - 2x^2 + y$ that lies above the triangle with vertices $(0, 0), (1, 0)$, and $(1, 1)$.
**(2)** The part of the paraboloid $y = x^2 + z^2$ that lies within the cylinder $x^2 + z^2 = 16$.

---

## Slide 54: Surface Integrals of Scalar Functions: Definition

In many physics and engineering problems, we need to integrate a function over a curved surface in space. This leads to the concept of a **surface integral**, which is the two-dimensional version of a line integral (used for curves).
Just like line integrals, surface integrals come in two types. The first type integrates a scalar function over a surface — for example, if a surface has a certain mass density at each point, integrating this density gives the total mass of the surface. The second type integrates a vector field over a surface — for example, to measure the net flow of a fluid through a surface submerged in it (similar to how we earlier measured the flux of a vector field across a curve).

Let $G(x, y, z)$ be a continuous function, and $S$ be a **smooth** surface defined parametrically on a region $R$ in the $uv$-plane,
$$ \mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}, \quad (u, v) \in R. $$

> **Image Description:**
> A small, curved surface patch element $\Delta \sigma_k$ on a 3D surface $S$ is approximated by a flat parallelogram. The corner is the point $P_k$ at coordinates $(x_k, y_k, z_k)$. The sides of the flat parallelogram are formed by the tangent vectors $\Delta u \mathbf{r}_u$ and $\Delta v \mathbf{r}_v$. The area of the curved patch is noted as $\Delta \sigma_k = \Delta \sigma_{uv}$.

The subdivision of $R$ (considered as a rectangle for simplicity) divides the surface $S$ into corresponding curved surface elements, or patches, of area
$$ \color{red}{\Delta \sigma_{uv} \approx \|\mathbf{r}_u \times \mathbf{r}_v\| \, du \, dv = \text{area of the tangent parallelogram determined by } \Delta u\mathbf{r}_u, \Delta v\mathbf{r}_v.} $$

---

## Slide 55: Surface Integrals of Scalar Functions: Definition

We number the surface element patches in some order with their areas given by $\Delta \sigma_1, \Delta \sigma_2, \ldots, \Delta \sigma_n$. We choose a point $(x_k, y_k, z_k)$ in the $k$th patch, multiply the value of the function $G$ at that point by the area $\Delta \sigma_k$, and add together the products, we get a Riemann sum over $S$,
$$ \sum_{k=1}^n G(x_k, y_k, z_k)\Delta \sigma_k. $$

Depending on how we pick $(x_k, y_k, z_k)$ in the $k$th patch, we may get different values for this Riemann sum. Then we take the limit as the number of surface patches increases, their areas shrink to zero, and both $\Delta u \to 0$ and $\Delta v \to 0$. This limit, whenever it exists independent of all choices made, defines the **surface integral of $G$ over the surface $S$** as
$$ \color{red}{\iint_S G(x, y, z) \, d\sigma = \lim_{n \to \infty} \sum_{k=1}^n G(x_k, y_k, z_k)\Delta \sigma_k.} \qquad (5) $$

If $S$ is a **piecewise smooth surface** (that is $S$ is partitioned by smooth curves into a finite number of smooth surfaces $S_1, \ldots, S_n$ with nonoverlapping interiors), and $G$ is continuous over $S$, then the surface integral defined by (5) can be shown to exist, and **the domain additivity property** takes the form
$$ \iint_S G \, d\sigma = \iint_{S_1} G \, d\sigma + \iint_{S_2} G \, d\sigma + \ldots + \iint_{S_n} G \, d\sigma. $$

---

## Slide 56: Formulas for a Surface Integral of a Scalar Function

**(1)** For a smooth surface $S$ defined **parametrically** as
$$ \mathbf{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k}, \quad (u, v) \in R, $$
and a continuous function $G(x, y, z)$ defined on $S$, the surface integral of $G$ over $S$ is given by the double integral over $R$ in $uv$-plane,
$$ \color{red}{\iint_S G(x, y, z) \, d\sigma = \iint_R G(f(u, v), g(u, v), h(u, v)) \|\mathbf{r}_u \times \mathbf{r}_v\| \, du \, dv.} $$

**(2)** Let $S$ be a surface given **implicitly** by $F(x, y, z) = c$, with $F$ continuously differentiable. If $S$ projects onto a closed, bounded region $R$ in a coordinate plane, then for any continuous function $G$ on $S$, the surface integral over $S$ equals the following double integral over $R$:
$$ \color{red}{\iint_S G(x, y, z) \, d\sigma = \iint_R G(x, y, z) \frac{\|\nabla F\|}{|\nabla F \cdot \mathbf{p}|} \, dA,} $$
where $\mathbf{p}$ is a unit vector normal to $R$ and $\nabla F \cdot \mathbf{p} \neq 0$ (note $\mathbf{p} \in \{\hat{i}, \hat{j}, \hat{k}\}$).

**(3)** **Special case from 2.** For a surface $S$ given **explicitly** as the graph of $z = f(x, y)$, where $f$ is a continuously differentiable function over a region $R$ in the $xy$-plane, so $F(x, y, z) = z - f(x, y)$ and $\mathbf{p} = \hat{k}$. The the surface integral of $G$ over $S$ is
$$ \color{red}{\iint_S G(x, y, z) \, d\sigma = \iint_R G(x, y, f(x, y)) \sqrt{f_x^2 + f_y^2 + 1} \, dx \, dy.} $$

---

## Slide 57: Surface Integrals of Scalar Functions: Examples

**Example 1.** Integrate $G(x, y, z) = x^2$ over the cone $z = \sqrt{x^2 + y^2}, \ 0 \leq z \leq 1$.
**Solution.** We have $z = \sqrt{x^2 + y^2} := f(x, y)$, and
$$ \iint_S x^2 \, d\sigma = \iint_{R: x^2 + y^2 \leq 1} x^2 \sqrt{1 + f_x^2 + f_y^2} \, dx \, dy = \iint_{x^2 + y^2 \leq 1} \sqrt{2} x^2 \, dx \, dy $$
$$ = \sqrt{2} \int_0^{2\pi} \int_0^1 r^3 \cos^2 \theta \, dr \, d\theta = \mathbf{\frac{\pi\sqrt{2}}{4}} $$

**Example 2.** Evaluate $\iint_S z \, d\sigma$, where $S$ is the surface whose sides $S_1$ are given by the cylinder $x^2 + y^2 = 1$, whose bottom $S_2$ is the disk $x^2 + y^2 \leq 1$ in the plane $z = 0$, and whose top $S_3$ is the part of the plane $z = 1 + x$ that lies above $S_2$.

> **Image Description:**
> A 3D illustration of a cylindrical solid that has been sliced at a slant on top. 
> *   $S_1$ is the curved vertical wall of the cylinder given by $x^2 + y^2 = 1$.
> *   $S_2$ is the flat circular base on the $xy$-plane ($z=0$).
> *   $S_3$ is the slanted elliptical top surface defined by the plane $z = 1 + x$.

**Solution.** We have $S = S_1 \cup S_2 \cup S_3$.
For $S_1$ we use $\theta$ and $z$ as parameters and write its parametric equations as $x = \cos \theta, \ y = \sin \theta, \ z = z$, where
$$ 0 \leq \theta \leq 2\pi \quad \text{and} \quad 0 \leq z \leq 1 + x = 1 + \cos \theta. $$

---

## Slide 58: Surface Integrals of Scalar Functions

Therefore,
$$ \mathbf{r}_\theta \times \mathbf{r}_z = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -\sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{vmatrix} = \cos \theta \hat{i} + \sin \theta \hat{j}, $$
and
$$ \|\mathbf{r}_\theta \times \mathbf{r}_z\| = \sqrt{\cos^2 \theta + \sin^2 \theta} = 1. $$

Thus the surface integral over $S_1$ is
$$ \iint_{S_1} z \, dS = \iint_R z \|\mathbf{r}_\theta \times \mathbf{r}_z\| \, dA = \int_0^{2\pi} \int_0^{1+\cos\theta} z \, dz \, d\theta = \int_0^{2\pi} \frac{1}{2}(1 + \cos \theta)^2 \, d\theta $$
$$ = \frac{1}{2} \int_0^{2\pi} \left[ 1 + 2\cos \theta + \frac{1}{2}(1 + \cos 2\theta) \right] d\theta = \mathbf{\frac{3\pi}{2}} $$

Since $S_2$ lies in the plane $z = 0$, we have
$$ \iint_{S_2} z \, dS = \iint_{S_2} 0 \, dS = \mathbf{0} $$

---

## Slide 59: Surface Integrals of Scalar Functions

The top surface $S_3$ lies above the unit disk $R = \{(x, y)| \ x^2 + y^2 \leq 1\}$ and is part of the plane $z = 1 + x = f(x, y)$. So, we get
$$ \iint_{S_3} z \, d\sigma = \iint_R (1 + x)\sqrt{1 + \left( \frac{\partial z}{\partial x} \right)^2 + \left( \frac{\partial z}{\partial y} \right)^2} \, dA $$
$$ = \iint_{x^2 + y^2 \leq 1} (1 + x)\sqrt{1 + 1 + 0} \, dA $$
$$ = \sqrt{2} \int_0^{2\pi} \int_0^1 (1 + r \cos \theta)r \, dr \, d\theta $$
$$ = \sqrt{2} \int_0^{2\pi} \left( \frac{1}{2} + \frac{1}{3}\cos \theta \right) d\theta = \mathbf{\sqrt{2}\pi} $$

Therefore,
$$ \iint_S z \, dS = \iint_{S_1} z \, dS + \iint_{S_2} z \, dS + \iint_{S_3} z \, dS = \mathbf{\left( \frac{3}{2} + \sqrt{2} \right)\pi} $$

---

## Slide 60: Surface Integrals of Scalar Functions: Exercises

**Exercise 1.** Evaluate
$$ \iint_S \sqrt{x(1 + 2z)} \, d\sigma, $$
on the portion of the cylinder $z = y^2/2$ over the triangular region $R : x \geq 0, y \geq 0, x + y \leq 1$, in the $xy$-plane.

**Exercise 2.** Integrate $G(x, y, z) = xyz$ over the surface of the cube cut from the first octant by the planes $x = 1, \ y = 1$, and $z = 1$.

**Exercise 3.**
In the following exercises, integrate the given function $G$ over the given surface.
**(1)** $G(x, y, z) = x$, over the parabolic cylinder $y = x^2, \ 0 \leq x \leq 2, \ 0 \leq z \leq 3$;
**(2)** $G(x, y, z) = z$, over the cylindrical surface $y^2 + z^2 = 4, \ z \geq 0, \ 1 \leq x \leq 4$;
**(3)** $G(x, y, z) = x^2$, over the unit sphere $x^2 + y^2 + z^2 = 1$;
**(4)** $G(x, y, z) = x + y + z$ over the portion of the plane $2x + 2y + z = 2$ that lies in the first octant;
**(5)** $G(x, y, z) = yz$, over the part of the sphere $x^2 + y^2 + z^2 = 4$ that lies above the cone $z = \sqrt{x^2 + y^2}$.

---

## Slide 61: Oriented Surfaces

Recall that a curve $C$ with a parametrization $\mathbf{r}(t)$ has a natural orientation, or direction, given by increasing $t$. The unit tangent vector $\mathbf{T}$ along $C$ points in this forward direction at each point on the curve.
Similarly, to specify an orientation on a surface $S$ in space, we assign a normal vector at each point on the surface. A parametrization $\mathbf{r}(u, v)$ of the surface yields a vector $\mathbf{r}_u \times \mathbf{r}_v$ (or $\mathbf{r}_v \times \mathbf{r}_u$) that is normal to the surface, thereby providing an orientation wherever the parametrization is defined.
If we can choose a continuous field of unit normal vectors $\mathbf{n}$ on a smooth surface $S$, then $S$ is called **orientable (or two-sided)**. Spheres and other smooth surfaces that form the boundaries of solid regions in space are orientable, since we can select an outward-pointing unit normal vector $\mathbf{n}$ (and inward-pointing vector $-\mathbf{n}$) at each point to define an orientation.

> **Image Description:**
> Two 3D illustrations showing orientable surfaces and their normal vectors.
> *   **Left Image:** A blue saddle-like surface defined on axes $x, y, z$. A normal vector $\mathbf{n}_1$ points up and slightly right from the top edge, and a normal vector $\mathbf{n}_2$ points left from the front edge.
> *   **Right Image:** Shows a continuous closed blob-like surface. On its top surface, magenta arrows representing normal vectors $\mathbf{n}$ point outward ("An outward-pointing vector field"). On the bottom right segment of the identical blob, magenta arrows point inward ("an inward-pointing vector field"). The caption says "An outward-pointing vector field and an inward-pointing vector field give the two possible orientations".

---

## Slide 62: Oriented Surfaces

A surface together with its normal field $\mathbf{n}$, or, equivalently, a surface with a consistent choice of sides, is called an **oriented surface**.

Not all surfaces can be oriented. The **Möbius band**$^1$ **(or strip)** is an example of a surface that is **not orientable**. **It has only one side**, and no choice of a vectors can give a continuous normal vector field on the Möbius band.

> **Image Description:**
> A three-part illustration demonstrating the construction and non-orientability of a Möbius band.
> *   **Top Diagram:** A rectangular flat strip with corners labeled $B, C$ on top and $A, D$ on the bottom.
> *   **Left Diagram:** The strip is twisted and joined. It shows a dashed track with a bug starting at "Start" with a "Finish" arrow showing that traversing the center line brings it to the exact opposite orientation of the surface, proving it is a single-sided surface. 
> *   **Center Diagram:** A Möbius band with magenta normal vectors pointing perpendicularly. The arrows clearly show that trying to define a continuous normal vector leads to conflicting (opposite) directions when tracing along the surface.
> *   **Right Diagram:** Shows how the edges align. Edge $AB$ is twisted and glued to edge $CD$ with opposing direction arrows, completing the Möbius loop.

**Figure:** The Möbius band is a nonorientable, or one-sided, surface.
___
$^1$It is named after the German geometer August Möbius (1790–1868). See Möbius strip on Wikipedia.

---

## Slide 63: Oriented Surfaces

If $S$ is a smooth orientable surface given in parametric form by a vector function $\mathbf{r}(u, v)$, then it is automatically supplied with the orientation of the unit normal vector
$$ \color{red}{\mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{\|\mathbf{r}_u \times \mathbf{r}_v\|}}, $$
and the opposite orientation is given by $-\mathbf{n}$.
For a surface $z = f(x, y)$, thus $F(x, y, z) := z - f(x, y)$, given as the graph of $f$, a natural orientation given by the unit normal vector
$$ \color{red}{\mathbf{n} = \frac{\nabla F}{\|\nabla F\|} = \frac{-\frac{\partial f}{\partial x}\hat{i} - \frac{\partial f}{\partial y}\hat{j} + \hat{k}}{\sqrt{1 + \left( \frac{\partial f}{\partial x} \right)^2 + \left( \frac{\partial f}{\partial y} \right)^2}}.} $$
Since the $\mathbf{k}$-component is positive, this gives the **upward** orientation of the surface.
For a **closed surface**, that is, a surface that is the boundary of a solid region $E$, the convention is that the **positive orientation** is the one for which the normal vectors point outward from $E$, and inward-pointing normals give the negative orientation.

> **Image Description:**
> Two spheres demonstrating surface orientation on a 3D coordinate plane.
> *   **Left Sphere ("Positive orientation"):** A blue sphere centered at the origin with magenta normal vectors pointing outward from its surface in all directions.
> *   **Right Sphere ("Negative orientation"):** A blue sphere centered at the origin with magenta normal vectors pointing inward toward the center of the sphere from its surface.

---

## Slide 64: Thank You for Your Attention!

Thank You for Your Attention!