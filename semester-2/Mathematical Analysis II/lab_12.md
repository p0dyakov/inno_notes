Here is the complete, line-by-line transcript of the presentation with beautiful formatting, LaTeX for mathematical formulas, and detailed descriptions of all images. 

***

# Mathematical Analysis (MA) II
## Multiple Integrals
**Ikechi Ndukwe**
Lab 12
(April 8, 2026)

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 1 / 17*

***

### Objectives

*   Recap
*   Triple Integrals
*   Change of Variables in Double and Triple Integrals
*   Homework

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 2 / 17*

***

### Polar Coordinates $(r, \theta)$ (Recap)

> **Image Description:** 
> There are two diagrams on this slide side-by-side explaining polar coordinates.
> *   **Left Diagram:** A 2D Cartesian coordinate system (x and y axes). A red dot represents a point labeled $P = (x,y)$ and $[r,\theta]$. A dashed line drops vertically from the point to the x-axis, forming a right-angled triangle. The hypotenuse represents the distance from the origin, labeled $r$. The vertical side is labeled $y$, and the horizontal base on the x-axis is labeled $x$. The angle between the x-axis and the hypotenuse $r$ is labeled $\theta$.
> *   **Right Diagram:** A polar coordinate grid showing concentric circles intersecting with radial lines emanating from the origin. Several red dots are plotted on the grid with their corresponding polar coordinates indicated, such as $[1, 0]$, $[3, \frac{\pi}{4}]$, $[4, \frac{\pi}{6}]$, $[2, \frac{\pi}{2}]$, $[5, \frac{7\pi}{12}]$, $[4, \pi]$, $[4, \frac{2\pi}{3}]$, and $[3, -\frac{\pi}{4}]$.

**Polar-Cartesian Conversions**

$$x = r \cos \theta, \quad y = r \sin \theta,$$
$$r^2 = x^2 + y^2, \quad \tan \theta = \frac{y}{x}$$

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 3 / 17*

***

### Cylindrical Coordinates $(r, \theta, z)$ (Recap)

> **Image Description:** 
> Two 3D diagrams side-by-side explaining cylindrical coordinates.
> *   **Left Diagram:** A 3D coordinate system (x, y, z axes). A red point $P = (x, y, z) = [r, \theta, z]$ is shown in space. A solid red line represents the distance $d$ from the origin to $P$. A dashed red line drops straight down from $P$ to the xy-plane, indicating the height $z$. On the xy-plane, a dashed line goes from the origin to the projection point, labeled $r$. The angle between the positive x-axis and $r$ is labeled $\theta$. 
> *   **Right Diagram:** A geometric visualization showing how intersecting surfaces define a point in cylindrical coordinates. It shows a blue vertical cylinder labeled "cylinder $r = r_0$", a yellow vertical plane starting from the z-axis labeled "vertical half-plane $\theta = \theta_0$", and a flat pink horizontal plane labeled "plane $z = z_0$". The point where these three surfaces intersect is marked with a black dot, labeled $P = [r_0, \theta_0, z_0]$.

**Cylindrical-Cartesian Conversions**

$$x = r \cos \theta, \quad y = r \sin \theta, \quad z = z,$$
$$r^2 = x^2 + y^2, \quad \tan \theta = \frac{y}{x}$$

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 4 / 17*

***

### Spherical Coordinates $(r, \phi, \theta)$ (Recap)

> **Image Description:** 
> Two 3D diagrams side-by-side explaining spherical coordinates. *(Note: The diagram uses $R$ for the radius, while the text uses $\rho$.)*
> *   **Left Diagram:** A 3D coordinate system (x, y, z axes). A red point $P = (x, y, z) = [R, \phi, \theta]$ is plotted. A solid red line labeled $R$ connects the origin to $P$. The angle between the positive z-axis and $R$ is labeled $\phi$. A dashed line drops vertically from $P$ to the xy-plane (length $z$). A dashed line $r$ connects the origin to the projection on the xy-plane. The angle between the x-axis and $r$ is labeled $\theta$. 
> *   **Right Diagram:** A visualization of intersecting surfaces defining a point in spherical coordinates. It shows a transparent blue sphere labeled "sphere $R = R_0$", a pink cone opening upwards labeled "cone $\phi = \phi_0$", and a yellow vertical half-plane labeled "plane $\theta = \theta_0$". The point where the sphere, cone, and half-plane intersect is marked with a red dot, labeled $P = [R_0, \phi_0, \theta_0]$.

**Cartesian-Cylindrical-Spherical Conversions**

$$x = \rho \sin \phi \cos \theta, \quad y = \rho \sin \phi \sin \theta, \quad z = \rho \cos \phi,$$
$$\rho^2 = x^2 + y^2 + z^2 = r^2 + z^2, \quad r = \sqrt{x^2 + y^2} = \rho \sin \phi$$
$$\tan \phi = \frac{r}{z}, \quad \tan \theta = \frac{y}{x}$$

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 5 / 17*

***

### Reversing the Order of Integration of Double Integrals

**Using Vertical Cross-sections:** To reverse the order of integration such that we integrate first with respect to $y$, and then with respect to $x$, take the following steps:

*   **i** **Sketch** the region of integration and label the bounding curves.
*   **ii** **To find the y-limits of integration:** Imagine a vertical line $L$ cutting through the region in the direction of increasing $y$. Mark the y-values where $L$ enters and leaves. These are the y-limits of integration and are usually functions of $x$.
*   **iii** **To find the x-limits of integration:** Choose x-limits that include all the vertical lines through the region.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 6 / 17*

***

**Using Horizontal Cross-sections:** To reverse the order of integration such that we integrate first with respect to $x$, and then with respect to $y$, take the following steps:

*   **i** **Sketch** the region of integration and label the bounding curves.
*   **ii** **To find the x-limits of integration:** Imagine a horizontal line $L$ cutting through the region in the direction of increasing $x$. Mark the x-values where $L$ enters and leaves. These are the x-limits of integration and are usually functions of $y$.
*   **iii** **To find the y-limits of integration:** Choose y-limits that include all the horizontal lines through the region.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 7 / 17*

***

### Exercises on Triple Integrals

**1** Calculate the following integrals:
*   **a** $\displaystyle \int_{0}^{7} \int_{0}^{2} \int_{0}^{\sqrt{4-y^2}} \frac{y}{1 + z} \,dx \,dy \,dz$
*   **b** $\displaystyle \int_{0}^{4} \int_{0}^{2} \int_{2y}^{4} \frac{4 \cos(x^2)}{2\sqrt{z}} \,dx \,dy \,dz$

**2** Find the volume of the solid region bounded by the planes $z = x$, $x + z = 8$, $z = y$, $y = 8$, and $z = 0$.

**3** Set up and evaluate $\displaystyle \iiint_G (x + y + z) \,dV$, where $G$ is the tetrahedron in the first octant bounded by the plane $x + y + z = 1$.

**4** Let $G$ be the wedge in the first octant that is cut from the cylindrical solid $y^2 + z^2 \leq 1$ by the planes $y = x$ and $x = 0$. Evaluate $\displaystyle \iiint_G z \,dV$.

**5** Let $G$ be the solid bounded above by the plane $z = 4$ and below by the paraboloid $z = x^2 + y^2$, with projection $R$ being the disk $x^2 + y^2 \leq 4$ in the xy-plane. Evaluate $\displaystyle \iiint_G (x^2 + y^2) \,dV$.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 8 / 17*

***

### Change of Variables in Double Integrals

**Jacobian**

The **Jacobian** of the coordinate transformation $x = g(u, v), y = h(u, v)$ is

$$J(u, v) = \left| \frac{\partial(x,y)}{\partial(u,v)} \right| = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial y}{\partial u} \frac{\partial x}{\partial v}$$

Let $x = g(u, v)$, $y = h(u, v)$ be a one-to-one transformation from a domain $G$ in the uv-plane onto a domain $R$ in the xy-plane. Suppose that the functions $x$ and $y$, and their first partial derivatives with respect to $u$ and $v$, are continuous in $S$. If $f(x, y)$ is integrable on $R$, and if $f(x, y) = f(g(u, v), h(u, v))$, then $f$ is integrable on $G$ and

**Change of Variables Formula for Double Integrals**

$$\iint_R f(x, y) \,dx \,dy = \iint_G f(g(u, v), h(u, v)) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \,du \,dv.$$

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 9 / 17*

***

### Change of Variables in Triple Integrals

Suppose that a solid region $G$ in uvw-space is transformed one-to-one into the solid region $D$ in xyz-space by differentiable equations of the form

$$x = g(u, v, w), \quad y = h(u, v, w), \quad z = k(u, v, w),$$

Then any function $F(x, y, z)$ defined on $D$ can be thought of as a function

$$F(g(u, v, w), h(u, v, w), k(u, v, w)) = H(u, v, w)$$

defined on $G$. If $g$, $h$, and $k$ have continuous first partial derivatives, then the integral of $F(x, y, z)$ over $D$ is related to the integral of $H(u, v, w)$ over $G$ by the equation

**Change of Variables Formula for Triple Integrals**

$$\iiint_D F(x, y, z) \,dx \,dy \,dz = \iiint_G H(u, v, w) |J(u, v, w)| \,du \,dv \,dw.$$

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 10 / 17*

***

**Jacobian**

$$J(u, v, w) = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{vmatrix} = \frac{\partial(x, y, z)}{\partial(u, v, w)}.$$

The Jacobian measures by how much the volume near a point in $G$ is being expanded or contracted by the transformation from $(u, v, w)$ to $(x, y, z)$ coordinates.

**Note:**
*   Cylindrical and spherical coordinates are standard changes of variables.
*   Linear substitutions are useful for tilted boxes, prisms, and ellipsoids.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 11 / 17*

***

### Exercises

**6** Use the transformation $x = u/v$, $y = uv$ to evaluate $\displaystyle \iint_R xy \,dA$ where $R$ is bounded by $xy = 1$, $xy = 2$, $y = x$, $y = 2x$ in the first quadrant.

**7** Calculate the integral by changing to cylindrical coordinates:
$$\int_{-3}^{3} \int_{0}^{\sqrt{9-x^2}} \int_{0}^{9-x^2-y^2} \sqrt{x^2 + y^2} \,dz \,dy \,dx$$

**8** Use spherical coordinates to find the volume of the solid that lies above the cone $z = \sqrt{x^2 + y^2}$ and below the sphere $x^2 + y^2 + z^2 = z$.

**9** Describe the solid and compute its volume:
$G = \{(x, y, z) : x^2 + y^2 \leq 4, 0 \leq z \leq 5 - x^2 - y^2\}$. Which coordinate system is most natural?

**10** Use a scaling change of variables to find the volume of the ellipsoid
$$\frac{x^2}{4} + y^2 + \frac{z^2}{9} \leq 1.$$

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 12 / 17*

***

### Homework

**1** Calculate the following integrals:
*   **a** $\displaystyle \iiint_G (x + y^2 + z^3) \,dV$ over $G = [0, 1] \times [0, 2] \times [0, 3]$.
*   **b** $\displaystyle \iiint_G xyz \,dV$ where $G = [1, 2] \times [0, 1] \times [0, 4]$.
*   **c** $\displaystyle \iiint_G e^{x+y+z} \,dV$ over $G = [0, 1] \times [0, 1] \times [0, 1]$.
*   **d** $\displaystyle \iiint_G 6x^2yz^2 \,dV$ over $G = [-1, 1] \times [0, 2] \times [1, 3]$.

**2** The solid $G$ is bounded by the planes $z = 0$, $z = 1 - y$, and the parabolic cylinder $x = y^2$, and by the planes $x = 0$ and $y = 1$ (where $x \geq 0$, $y \geq 0$). The projection $R$ onto the xy-plane is the region $0 \leq y \leq 1$, $0 \leq x \leq y^2$. Compute $\displaystyle \iiint_G 2z \,dV$.

**3** Evaluate $\displaystyle \iint_R \frac{1}{\sqrt{x^2 + y^2}} \,dA$ over the region inside $x^2 + y^2 = 1$ and above $y = |x|$ using polar coordinates.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 13 / 17*

***

**4** Evaluate $\displaystyle \iint_R e^{x^2+y^2} \,dA$ where $R$ is the upper half of the unit disk using polar coordinates.

**5** Evaluate $\displaystyle \int_{1}^{2} \int_{y/x}^{\sqrt{y}} e^{\sqrt{xy}} \,dx \,dy$ using $u = \sqrt{xy}$, $v = \sqrt{y/x}$.

**6** Use the transformation $u = x + y$, $v = x - y$ to evaluate
$\displaystyle \iint_R e^{x+y} \sin(x - y) \,dA$ where $R$ is the square with vertices $(0, 0)$, $(\pi, 0)$, $(\pi, \pi)$, $(0, \pi)$.

**7** Evaluate $\displaystyle \iint_R (x^2 + y^2) \,dA$ over the region in the first quadrant bounded by $xy = 1$, $xy = 2$, $y = x$, and $y = 2x$ using an appropriate transformation.

**8** Evaluate $\displaystyle \iiint_G z \,dV$, where $G$ is the solid inside the cylinder $x^2 + y^2 \leq 1$ and between the planes $z = 0$ and $z = 2 + y$.

**9** Let $G$ be the solid enclosed by the sphere $x^2 + y^2 + z^2 = 9$ and above the cone $z = \sqrt{x^2 + y^2}$. Compute the volume of $G$.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 14 / 17*

***

**10** Evaluate $\displaystyle \iiint_G (x^2 + y^2) \,dV$, where $G$ is the upper half of the ball $x^2 + y^2 + z^2 \leq 4$ (that is, $z \geq 0$).

**11** A cylindrical sensor covers the region
$G = \{(r, \theta, z) : 0 \leq r \leq 2, 0 \leq \theta \leq 2\pi, 0 \leq z \leq 4 - r\}$. Assume the signal intensity is $I(x, y, z) = z$. Find the accumulated signal
$$S = \iiint_G I(x, y, z) \,dV.$$

**12** Let $G$ be the solid in 3-space defined by the inequalities
$1 - e^x \leq y \leq 3 - e^x$, $1 - y \leq 2z \leq 2 - y$, $y \leq e^x \leq y + 4$.
*   **a** Using the coordinate transformation $u = e^x + y$, $v = y + 2z$, $w = e^x - y$, calculate the Jacobian $\frac{\partial(x,y,z)}{\partial(u,v,w)}$. Express your answer in terms of $u, v, w$.
*   **b** Using a triple integral and the change of variables given in part (a), find the volume of $G$.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 15 / 17*

***

**13** Use the change of variables $x = u + v$, $y = u - v$, $z = w$ to evaluate
$\displaystyle \iiint_G (x - y) \,dV$, where $G$ is the image of the box
$0 \leq u \leq 1$, $0 \leq v \leq 2$, $0 \leq w \leq 3$.

**14** Let $D$ be the solid region in xyz-space defined by the inequalities
$1 \leq x \leq 2$, $0 \leq xy \leq 2$, $0 \leq z \leq 1$. Calculate the integral
$\displaystyle \iiint_D (x^2y + 3xyz) \,dx \,dy \,dz$ by applying the transformation
$u = x$, $v = xy$, $w = 3z$.

**15** Find the average value of $f(x, y, z) = z$ on the solid
$G = \{(x, y, z) : x^2 + y^2 + z^2 \leq 4, z \geq 0\}$.
Recall that $\displaystyle f_{\text{avg}} = \frac{1}{\text{Vol}(G)} \iiint_G f \,dV$.

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 16 / 17*

***

# Thank You

*Footer: Ikechi Ndukwe | MA II | Lab 12 (April 8, 2026) | 17 / 17*