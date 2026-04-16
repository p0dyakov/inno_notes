### Slide 1: Title Slide

**Mathematical Analysis (MA) II**
Vector Fields

Ikechi Ndukwe
Lab 13
(April 15, 2026)

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 1 / 15*

***

### Slide 2

**Objectives**

*   Recap
*   Vector Fields
*   Gradient, Curl, and Divergence
*   Homework

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 2 / 15*

***

### Slide 3

**Vector Fields**

A **vector field** is a function that maps each point in its domain to a vector.

**Vector Field Representations**
In 2D, a vector field may be written as:
$$ \mathbf{F}(x, y) = P(x, y)\mathbf{i} + Q(x, y)\mathbf{j} $$

In 3D, a vector field may be written as:
$$ \mathbf{F}(x, y, z) = P(x, y, z)\mathbf{i} + Q(x, y, z)\mathbf{j} + R(x, y, z)\mathbf{k} $$

Some examples of vector fields include: gravitational field, electric field, fluid velocity field, and magnetic field.

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 3 / 15*

***

### Slide 4

**A Rotational Field in the Plane**

Describe the vector field $\mathbf{F}(x, y) = -y\mathbf{i} + x\mathbf{j}$ by sketching some vectors.

*[Image Description: A diagram of a 2D Cartesian coordinate system with an x-axis and a y-axis. Several blue vector arrows are plotted around the origin, demonstrating a counter-clockwise rotational flow. A grey circle is drawn lightly in the background to emphasize the circular path. Specific points are labeled with their corresponding vectors: at the right on the x-axis, the vector is labeled $\mathbf{F}(1, 0)$ and points straight up; at the top on the y-axis, the vector is labeled $\mathbf{F}(0, 3)$ and points straight left; in the upper-right quadrant, a vector is labeled $\mathbf{F}(2, 2)$ pointing up and left. Below the graph, the equation $\mathbf{F}(x, y) = -y\mathbf{i} + x\mathbf{j}$ is written.]*

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 4 / 15*

***

### Slide 5

**A Simple Field in Space**

Sketch the vector field on $\mathbb{R}^3$ given by $\mathbf{F}(x, y, z) = z\mathbf{k}$.

*[Image Description: A diagram of a 3D Cartesian coordinate system with x, y, and z axes meeting at the origin (0). Blue vector arrows are plotted throughout the space, all running parallel to the vertical z-axis. For points above the xy-plane (where z is positive), the arrows point upwards. For points below the xy-plane (where z is negative), the arrows point downwards. The length of the arrows increases as the distance from the xy-plane increases, visually showing that the magnitude of the vector is directly proportional to the value of z.]*

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 5 / 15*

***

### Slide 6

**Exercises**

**1.** Sketch the following vector fields:
**a)** $\mathbf{F}(x, y) = 0.3\mathbf{i} - 0.4\mathbf{j}$
**b)** $\mathbf{F}(x, y) = -\frac{1}{2}\mathbf{i} + (y - x)\mathbf{j}$
**c)** $\mathbf{F}(x, y) = \frac{y\mathbf{i} + x\mathbf{j}}{\sqrt{x^2 + y^2}}$
**d)** $\mathbf{F}(x, y, z) = \mathbf{i}$ in $\mathbb{R}^3$

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 6 / 15*

***

### Slide 7

**Gradient, Curl, and Divergence**

**Gradient**
If $f(x, y, z)$ is a scalar function, its gradient is the vector field given by:
$$ \nabla f = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k} $$

**Divergence**
The **divergence (flux density)** of a vector field $\mathbf{F} = P\mathbf{i} + Q\mathbf{j} + R\mathbf{k}$ at the point $(x, y, z)$ is
$$ \text{div } \mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} $$

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 7 / 15*

***

### Slide 8

**Curl**

The **curl** of a vector field $\mathbf{F} = P\mathbf{i} + Q\mathbf{j} + R\mathbf{k}$ is
$$ \text{curl } \mathbf{F} = \nabla \times \mathbf{F} $$
$$ = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix} $$
$$ = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)\mathbf{i} + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)\mathbf{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\mathbf{k} $$

If $\mathbf{F}$ is conservative, then $\text{curl } \mathbf{F} = 0$

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 8 / 15*

***

### Slide 9

**Examples**

a) Find the gradient vector field of $f(x, y) = x^2y - y^3$.

**Solution**
$$ \nabla f(x, y) = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j}. $$
$$ \frac{\partial f}{\partial x} = 2xy, \quad \frac{\partial f}{\partial y} = x^2 - 3y^2 $$

Thus
$$ \nabla f(x, y) = 2xy\mathbf{i} + (x^2 - 3y^2)\mathbf{j}. $$

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 9 / 15*

***

### Slide 10

b) Let $\mathbf{F}(x, y, z) = xz\mathbf{i} + xyz\mathbf{j} - y^2\mathbf{k}$. Find $\text{curl } \mathbf{F}$ and $\text{div } \mathbf{F}$.

**Solution**
$$ \text{curl } \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ xz & xyz & -y^2 \end{vmatrix} $$

$$ = \left( \frac{\partial(-y^2)}{\partial y} - \frac{\partial(xyz)}{\partial z} \right)\mathbf{i} - \left( \frac{\partial(-y^2)}{\partial x} - \frac{\partial(xz)}{\partial z} \right)\mathbf{j} + \left( \frac{\partial(xyz)}{\partial x} - \frac{\partial(xz)}{\partial y} \right)\mathbf{k} $$

$$ = (-2y - xy)\mathbf{i} - (0 - x)\mathbf{j} + (yz - 0)\mathbf{k} $$

$$ \therefore \text{curl } \mathbf{F} = -y(2 + x)\mathbf{i} + x\mathbf{j} + yz\mathbf{k} $$

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 10 / 15*

***

### Slide 11

*(Continuation of Solution from Slide 10)*

$$ \text{div } \mathbf{F} = \frac{\partial}{\partial x}(xz) + \frac{\partial}{\partial y}(xyz) + \frac{\partial}{\partial z}(-y^2). $$

$$ \frac{\partial}{\partial x}(xz) = z, \quad \frac{\partial}{\partial y}(xyz) = xz, \quad \frac{\partial}{\partial z}(-y^2) = 0. $$

$$ \therefore \text{div } \mathbf{F} = z + xz = z(1 + x). $$

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 11 / 15*

***

### Slide 12

**Exercises**

**2.** Find the gradient vector field of the following functions:
**a)** $f(x, y) = y \sin(xy)$
**b)** $f(x, y, z) = \sqrt{x^2 + y^2 + z^2}$

**3.** Compute the curl of $\mathbf{F}(x, y, z) = yz\mathbf{i} + xz\mathbf{j} + xy\mathbf{k}$

**4.** Compute the divergence of $\mathbf{F}(x, y, z) = yz\mathbf{i} + xz\mathbf{j} + xy\mathbf{k}$ and verify that for any $\mathbf{F}$ with continuous second partials, $\text{div}(\text{curl } \mathbf{F}) = 0$.

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 12 / 15*

***

### Slide 13

**Additional Resources**

Tools to help plot vector fields:
*   Desmos 2D
*   Geogebra 2D
*   Geogebra 3D

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 13 / 15*

***

### Slide 14

**Homework**

**1.** Sketch the vector field $\mathbf{F}(x, y) = \frac{1}{2}x\mathbf{i} + y\mathbf{j}$.
**2.** Use a Computer Algebra System (CAS) to plot the vector field $\mathbf{F}(x, y) = \langle \ln(1 + y^2), \ln(1 + x^2) \rangle$ and describe its appearance.
**3.** Find the gradient vector field of $f(s, t) = \sqrt{2s + 3t}$.
**4.** Compute both the curl and divergence of $\mathbf{F}(x, y, z) = y\mathbf{i} + z\mathbf{j} + x\mathbf{k}$.
**5.** Verify that $\text{div}(\nabla f) = \nabla^2f$ for $f(x, y, z) = x^2y e^{y/z}$.
**6.** Show that $\mathbf{F}(x, y, z) = e^{y+2z}(\mathbf{i} + x\mathbf{j} + 2x\mathbf{k})$ is conservative by computing its curl.
**7.** Explain why the gravitational field $\mathbf{F}(\mathbf{x}) = -\frac{mMG}{|\mathbf{x}|^3}\mathbf{x}$ is conservative.

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 14 / 15*

***

### Slide 15

**Thank You**

*Footer: Ikechi Ndukwe | MA II | Lab 13 (April 15, 2026) | 15 / 15*