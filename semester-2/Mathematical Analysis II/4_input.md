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