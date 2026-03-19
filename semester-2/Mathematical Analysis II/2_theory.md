


Here is the complete line-by-line transcription of the first 45 slides with beautiful formatting, proper mathematical notation, and detailed descriptions of all images.

***

### Slide 1

**Mathematical Analysis II.**
**Chapter 2: Functions of Several Variables**

**Mohammad S. Alkousa**
Assistant Professor in Innopolis University
Lab of High Performance Computing.
Senior Researcher at Laboratory of Modern Adaptive Computational Methods in Innopolis University.
`m.alkousa@innopolis.ru`

Updated March 11, 2026

*Footer: Functions of Several Variables | Limits and Continuity for Functions of Several Variables | Partial Derivatives | Directional Derivatives and Gradients | Extr... | M.S. Alkousa | Chapter 2*

---

### Slide 2

**Contents**

1. **Functions of Several Variables**
   * Functions of Several Variables: Domains, Ranges and Graphs
   * Level Sets: Level Curves (Contours), Level Surfaces and Level Hypersurfaces.
2. **Limits and Continuity for Functions of Several Variables**
3. **Partial Derivatives**
4. **Directional Derivatives and Gradients**
5. **Extreme Values for Functions of Several Variables and Saddle Points**
   * Extreme Values and Saddle Points
   * Minimization Problem: Gradient Descent Method
   * Constrained Maxima and Minima and Lagrange Multipliers
6. **Taylor’s Formula for Functions with Several Variables**

---

### Slide 3

**Functions of Several Variables: Domains and Ranges**

**Definition**
* Let $D$ be a set of $n$-tuples of real numbers $(x_1, x_2, \dots, x_n)$. A real-valued function $f$, of the $n$ **independent variables** $x_1, x_2, \dots, x_n$, on $D$ is a rule that assigns a real number $w = f(x_1, x_2, \dots, x_n)$ to each element in $D$. The set $D$ is the **domain** of $f$. The set of $w$-values (which is a **dependent variable** of $f$) is the function's **range**.
* The **domain** of a function is assumed to be the largest set for which the defining rule generates real numbers.
* The **range** consists of the set of output values for the dependent variables.

> 🖼️ **Image Description:** A mathematical diagram illustrating the mapping of a function. On the left is a 2D coordinate system (with $x$ and $y$ axes) containing a shaded region $D$ representing the domain. Inside $D$, two points are plotted: $(x, y)$ and $(a, b)$. Red arrows labeled $f$ extend from these points, mapping them onto a 1-dimensional horizontal axis on the right, which represents the range. The point $(x, y)$ maps to a value $f(x, y)$, and the point $(a, b)$ maps to a value $f(a, b)$. The figure caption reads: "Figure: $z = f(x, y)$, a function of two independent variables $x, y$."

---

### Slide 4

**Functions of Several Variables: Domains, Ranges and Graphs**

**Examples.**
1. For the function $f(x, y) = \frac{\sqrt{x+y+1}}{x-1}$, the domain is $D_f = \{(x, y) \mid x + y + 1 \ge 1, x \neq 1\}$. <span style="color:red">(Sketch $D_f$!)</span>
2. For the function $g(x, y) = x \ln(y^2 - x)$, the domain is $D_g = \{(x, y) \mid x < y^2\}$. <span style="color:red">(Sketch $D_g$!)</span>
3. For the function $h(x, y) = \sqrt{y} - \ln(1 - x)$, the domain is $D_h = \{(x, y) \mid x < 1, y \ge 0\} = (-\infty, 1) \times[0, \infty)$. <span style="color:red">(Sketch $D_h$!)</span>
4. For the function $\varphi(x, y) = \frac{\sqrt{1-y^2}}{\ln(x^2+1)}$, the domain is $D_\varphi = \{(x, y) \mid x \neq 0, -1 \le y \le 1\} = \mathbb{R}^* \times [-1, 1]$. <span style="color:red">(Sketch $D_\varphi$!)</span>

**Definition (Graph of a function)**
If $f$ is a function of two variables with domain $D$, then the **graph** of $f$ is the set of all points $(x, y, z) \in \mathbb{R}^3$ such that $z = f(x, y)$ and $(x, y) \in D$. So the graph of a function $f$ of two variables is a surface $S$ with equation $z = f(x, y)$.

> 🖼️ **Image Description:** A 3D Cartesian coordinate diagram (with $x$, $y$, and $z$ axes) illustrating the graph of a function. An orange planar region $D$ is shown in the $xy$-plane. Directly above it is a blue 3D surface $S$. A dashed line projects from a point $(x, y, 0)$ in domain $D$ straight up to a point $(x, y, f(x, y))$ on the surface $S$. The vertical height is labeled $f(x,y)$.

---

### Slide 5

**Interior Point, Boundary Point, Bounded and Unbounded Regions**

**Definition**
Let $P_0$ be a point in a region (set) $R$ in $\mathbb{R}^n$.
* $P_0$ is an **interior point** if it is a center of a ball (it is a disk in $\mathbb{R}^2$, and a solid ball in $\mathbb{R}^3$) of positive radius that lies entirely in $R$. <span style="color:blue">The set of interior points of a region, make up the **interior** of the region.</span> <span style="color:red">A region is **open** if it consists entirely of interior points.</span>
* $P_0$ is a **boundary point** of $R$ if every ball centered at $P_0$ contains points that lie outside of $R$ as well as points that lie in $R$. (The boundary point itself need not belong to $R$). <span style="color:blue">The region's boundary points make up its **boundary**.</span> <span style="color:red">A region is **closed** if it contains all its boundary points.</span>
* A region in $\mathbb{R}^n$ is **bounded** if it lies inside a ball of finite radius. A region is **unbounded** if it is not bounded.

> 🖼️ **Image Description:** Four visualizations are displayed side-by-side to illustrate mathematical region definitions:
> 1.  **Interior point (2D):** An amoeba-like 2D shape $R$. A point $(x_0, y_0)$ is inside, surrounded by a red dashed circular neighborhood that fits completely within $R$.
> 2.  **Boundary point (2D):** A similar 2D shape $R$. A point $(x_0, y_0)$ lies exactly on the edge. Its red dashed circular neighborhood contains space both inside and outside $R$.
> 3.  **Interior point (3D):** A blob-like 3D volume. A point $(x_0, y_0, z_0)$ is embedded inside it, with a green spherical neighborhood entirely contained within the volume.
> 4.  **Boundary point (3D):** The same 3D volume. A point $(x_0, y_0, z_0)$ sits on its surface, and its green spherical neighborhood contains space both inside and outside the volume.

---

### Slide 6

**Level Sets**

**Definition**
The set of points $(x_1, \dots, x_n)$ in $\mathbb{R}^n$ where a function of $n$ independent variables has a constant value $f(x_1, \dots, x_n) = c$ ($c \in \mathbb{R}$ is a constant) is called a **level set** of $f$. That is $\mathcal{L}_c(f) = \{(x_1, \dots, x_n) \mid f(x_1, \dots, x_n) = c\}$.
* When the number of independent variables is two (i.e., $n = 2$), a level set is called a **level curve**, also known as **contour line**.
* When $n = 3$, a level set is called a **level surface**.
* When $n > 3$, the level set is called a **level hypersurface**.

> 🖼️ **Image Description:** Two mathematical diagrams.
> *   **Left diagram:** A 3D plot showing an inverted paraboloid-like surface defined by $z = f(x, y) = 100 - x^2 - y^2$. A horizontal plane intersects the surface at $z = 75$, forming a green circle. This circle is projected straight down onto the $xy$-plane to show the level curve $f(x, y) = 75$. A larger red circle on the $xy$-plane represents the level curve $f(x, y) = 51$.
> *   **Right diagram:** A 3D cutaway showing nested, concentric spheres colored blue, green, yellow, and purple. These represent the level surfaces of the equation $x^2 + y^2 + z^2 = c$ for values $c=9, c=4, c=1$.

---

### Slide 7

**Level Curves (Contours)**

> 🖼️ **Image Description:** Two sets of 3D surfaces and their corresponding 2D contour maps.
> *   **Left:** The top shows a continuous undulating 3D surface with multiple peaks and valleys (colored like a rainbow). Below it on the $xy$-plane is its red contour map, displaying a pattern of closed loops (peaks/valleys) and saddle shapes.
> *   **Right:** The top shows a 3D surface featuring two sharp peaks side-by-side on a flat plane. Below it is its red contour map, displaying two distinct sets of concentric circles corresponding to the peaks.

Figure: Level curves of a function $z = \sin x + 2 \sin y$ (left), and $z = (4x^2 + t^2)e^{-x^2-y^2}$ (right).

See `https://www.wikiwand.com/en/articles/Contour_line`

---

### Slide 8

**Functions of Several Variables: Exercises**

**Exercise 1.** Find and sketch the domain for each function
1. $f(x, y) = \sqrt{y - x - 2}$;
2. $f(x, y) = \ln(x^2 + y^2 - 4)$;
3. $f(x, y) = \frac{\sin(xy)}{x^2+y^2-25}$;
4. $f(x, y, z) = \sqrt{4 - x^2} + \sqrt{9 - y^2} + \sqrt{1 - z^2}$;
5. $f(x, y, z) = \ln(16 - 4x^2 - 4y^2 - z^2)$.

**Exercise 2.** Sketch the level curve $z = k$ for the specified values of $k$.
1. $z = f(x, y) = x + y - 1, \quad k = -2, -1, 0, 1, 2$;
2. $z = f(x, y) = x^2 + y^2, \quad k = 0, 1, 2, 3, 4$;
3. $z = f(x, y) = \frac{y}{x}, \quad k = -2, -1, 0, 1, 2$;
4. $z = f(x, y) = x^2 + 9y^2, \quad k = 0, 1, 2, 3, 4$;
5. $z = f(x, y) = x^2 - y^2, \quad k = -2, -1, 0, 1, 2$.

---

### Slide 9

**Limits for Functions of Several Variables**

**Definition**
Let $f$ be a function defined on a subset $D$ of $\mathbb{R}^n$, and assume that $f$ is defined at all points of some open ball (contained in $D$) centered at the point $a \in \mathbb{R}^n$, except possibly at $a$. Then, $\lim_{x \to a} f(x) = L$ means that for every number $\varepsilon > 0$ there is a corresponding number $\delta > 0$ such that
$$\text{If } x \in D \text{ and } 0 < ||x - a|| < \delta \text{ then } |f(x) - L| < \varepsilon.$$

**Remark.** In this definition, we will take the Euclidean norm, that is
$||x|| = ||x||_2 = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$, for any $x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n$.

> 🖼️ **Image Description:** A visual representation of the formal $(\varepsilon, \delta)$ definition of a limit. On the left, a 2D domain $D$ is shown with a central point $(x_0, y_0)$ in blue. A dashed red circle of radius $\delta$ surrounds it. Another point $(x,y)$ lies inside this circle. A red arrow labeled $f$ maps the point $(x,y)$ to a 1D number line on the right. The mapped point lands near the limit value $L$ (black dot) and falls strictly within a red bracketed interval of radius $\varepsilon$ (ranging from $L-\varepsilon$ to $L+\varepsilon$).

---

### Slide 10

**Limits for Functions of Several Variables: Properties**

**Theorem (Properties of Limits of Functions of Several Variables)**
Let $\lim_{x \to a} f(x) = L$, and $\lim_{x \to a} f(x) = M$. Then
1. **Sum Rule:** $\lim_{x \to a} (f(x) + g(x)) = L + M$.
2. **Difference Rule:** $\lim_{x \to a} (f(x) - g(x)) = L - M$.
3. **Constant Multiple Rule:** $\lim_{x \to a} kf(x) = kL$, for any $k \in \mathbb{R}$.
4. **Product Rule:** $\lim_{x \to a} (f(x) \cdot g(x)) = L \cdot M$.
5. **Quotient Rule:** $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}, \quad M \neq 0$.
6. **Power Rule:** $\lim_{x \to a} (f(x))^m = L^m, \quad \forall m \in \mathbb{N}$.
7. **Root Rule:** $\lim_{x \to a} \sqrt[m]{f(x)} = \sqrt[m]{L}$, where $m \in \mathbb{N}$, and $L > 0$ if $m$ is even.
8. **Composition Rule:** If $h(z)$ is continuous at $z = L$, then $\lim_{x \to a} h(f(x)) = h(L)$.

**Example 1.**
$$ \lim_{(x,y) \to (0,0)} \cos\left( \frac{x^2 + y^3}{x + y + 1} \right) = \cos\left( \lim_{(x,y) \to (0,0)} \frac{x^2 + y^3}{x + y + 1} \right) = \boxed{1} $$

---

### Slide 11

**Limits for Functions of Several Variables: Examples**

**Example 2.**
$$ \lim_{(x,y) \to (0,0)} \frac{e^y \sin x}{x} = \lim_{(x,y) \to (0,0)} e^y \cdot \lim_{(x,y) \to (0,0)} \frac{\sin x}{x} = \boxed{1} $$

**Example 3.**
$$ \lim_{(x,y,z) \to (1,0,-1)} \frac{2e^{x+2y-3z}}{x^2 + 2\cos(\sqrt{xy})} = \frac{2e^4}{1 + 2\cos(0)} = \boxed{\frac{2e^4}{3}} $$

**Example 4.**
$$ \lim_{\substack{(x,y) \to (1,1) \\ x \neq 1}} \frac{xy - y - 2x + 2}{x - 1} = \lim_{\substack{(x,y) \to (1,1) \\ x \neq 1}} \frac{y(x - 1) - 2(x - 1)}{x - 1} = \lim_{\substack{(x,y) \to (1,1) \\ x \neq 1}} (y - 1) = \boxed{-1} $$

**Example 5.**
$$ \lim_{\substack{(x,y) \to (4,3) \\ x \neq y+1}} \frac{\sqrt{x} - \sqrt{y+1}}{x - y - 1} = \lim_{\substack{(x,y) \to (4,3) \\ x \neq y+1}} \frac{(\sqrt{x} - \sqrt{y+1})(\sqrt{x} + \sqrt{y+1})}{(x - y - 1)(\sqrt{x} + \sqrt{y+1})} $$
$$ = \lim_{\substack{(x,y) \to (4,3) \\ x \neq y+1}} \frac{x - (y + 1)}{(x - y - 1)(\sqrt{x} + \sqrt{y+1})} $$
$$ = \lim_{\substack{(x,y) \to (4,3) \\ x \neq y+1}} \frac{1}{\sqrt{x} + \sqrt{y+1}} = \boxed{\frac{1}{4}} $$

---

### Slide 12

**Limits for Functions of Several Variables: Examples**

**Remark.** <span style="color:red">Two-Path Test for Non-existence of a Limit.</span>
If a function $f(x, y)$ has different limits along two different paths in the domain of $f$ as $(x, y)$ approaches $(x_0, y_0)$, then $\lim_{(x,y) \to (x_0,y_0)} f(x, y)$ does not exist.
This is true for any function of several variables (not only two).

**Example 6.** Does the limit $\lim_{(x,y) \to (0,0)} \frac{y}{x}$ exist?
The domain of $f(x, y) = \frac{y}{x}$ does not include the $y$-axis, so we do not consider any points $(x, y)$ where $x = 0$ in the approach toward the origin $(0, 0)$.
* Along the $x$-axis ($y = 0$), we have $f(x, 0) = 0$ for all $x \neq 0$. So if the limit does exist as $(x, y) \to (0, 0)$, the value of the limit must be $L = 0$.
* Along the line $y = x$, we have $f(x, y) = f(x, x) = \frac{x}{x} = 1$ for all $x \neq 0$. That is, the function $f$ approaches the value 1 along the line $y = x$.

This means that for every disk of radius $\delta > 0$ centered at $(0, 0)$, the disk will contain points $(x, 0)$ on the $x$-axis where the value of the function is $0$, and also points $(x, y)$ along the line $y = x$ where the value of the function is $1$. <span style="color:blue">Therefore, the limit does not exist because we have different limiting values along different paths approaching the point $(0, 0)$.</span>

---

### Slide 13

**Limits for Functions of Several Variables: Examples**

**Example 7.**
Show that the function $f(x, y) = \frac{2x^2y}{x^4 + y^2}$ has no limit as $(x, y)$ approaches $(0, 0)$.

**Solution** Since $(x, y) \to (0, 0)$ we have indeterminate form $\frac{0}{0}$.
Along the curve $y = kx^2$, $x \neq 0$, the function has the constant value
$$ f(x, y) \bigg|_{y=kx^2} = \frac{2x^2y}{x^4 + y^2} \bigg|_{y=kx^2} = \frac{2x^2(kx^2)}{x^4 + (kx^2)^2} = \frac{2kx^4}{x^4 + k^2x^4} = \frac{2k}{1 + k^2}. $$
Therefore,
$$ \lim_{(x,y) \to (0,0)} f(x, y) = \lim_{(x,y) \to (0,0)} [f(x, y)]_{y=kx^2} = \frac{2k}{1 + k^2}. $$
Hence,
* If $(x, y)$ approaches $(0, 0)$ along the parabola $y = x^2$, that is $k = 1$, then the limit is $1$.
* If $(x, y)$ approaches $(0, 0)$ along the $x$-axis ($y = 0$), that is $k = 0$, then the limit is $0$.

As a result, we find that $f$ has no limit as $(x, y)$ approaches $(0, 0)$.

---

### Slide 14

**Continuity for Functions of Several Variables**

**Definition**
Suppose that every open ball centered at $a \in \mathbb{R}^n$ contains a point in the domain of $f$ other than $a$ itself. Then a function $f$ is **continuous at the point** $a$ if $f$ is defined at the point $a$ and
$$ \lim_{x \to a} f(x) = f(a). $$
A function is **continuous** if it is continuous at every point of its domain.

**Example.** The function $f(x) = \begin{cases} \frac{2xy}{x^2+y^2}, & (x, y) \neq (0, 0) \\ 0, & (x, y) = (0, 0). \end{cases}$ is continuous at every point except the origin $(0, 0)$.
* At any point $(\alpha, \beta) \neq (0, 0)$, we have $\lim_{(x,y) \to (\alpha,\beta)} f(x, y) = \frac{2\alpha\beta}{\alpha^2+\beta^2} = f(\alpha, \beta)$. Thus the function $f$ is continuous at $(\alpha, \beta)$.
* At the origin, note that the limit $\lim_{(x,y) \to (0,0)} f(x, y)$ does not exist. Take the limit along the punctured line $y = mx, x \neq 0$ for different values of $m \in \mathbb{R}$. This limit **changes** with each value of the slope $m$.

**Continuity of Compositions.** If $f$ is continuous at $a \in \mathbb{R}^n$ and $g$ is a single-variable function continuous at $f(a)$, then the composition $h = g \circ f$ defined by $h(x) = g(f(x))$ is also continuous at $a$. For example $e^{x^2+y^2-1}$, $\cos(xy/(z^2 + 1))$, $\ln(1 + x^2y^2)$ are continuous.

---

### Slide 15

**Limits and Continuity for Functions of Several Variables: Exercises**

**Exercise 1.** Find the limits

$$ \lim_{\substack{(x,y) \to (2,-4) \\ y \neq -4, x \neq x^2}} \frac{y + 4}{x^2y - xy + 4x^2 - 4x}, \qquad \lim_{\substack{(x,y) \to (2,0) \\ 2x-y \neq 4}} \frac{\sqrt{2x - y} - 2}{2x - y - 4}, $$

$$ \lim_{\substack{(x,y) \to (0,0) \\ x \neq y}} \frac{x - y + 2\sqrt{x} - 2\sqrt{y}}{\sqrt{x} - \sqrt{y}}, \qquad \lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2}, \qquad \lim_{(x,y) \to (0,0)} \frac{1 - \cos(xy)}{xy}. $$

**Exercise 2.** Show that the following functions have no limit as $(x, y) \to (0, 0)$.

$$ f(x, y) = -\frac{x}{\sqrt{x^2 + y^2}}, \qquad f(x, y) = \frac{x^4 - y^2}{x^4 + y^2}, $$

$$ f(x, y) = \frac{xy}{|xy|}, \qquad f(x, y) = \frac{x^2 - y}{x - y}. $$

**Exercise 3.** Define $f(0, 0)$ in a way that extends $f(x, y) = xy \frac{x^2 - y^2}{x^2 + y^2}$ to be continuous at the origin $(0, 0)$.

---

### Slide 16

**Partial Derivatives**

If $(x_0, y_0)$ is a point in the domain of a function $f(x, y)$, the vertical plane $y = y_0$ will cut the surface $z = f(x, y)$ in the curve $z = f(x, y_0)$. This curve is the graph of the function $z = f(x, y_0)$ in the plane $y = y_0$. The horizontal coordinate in this plane is $x$; the vertical coordinate is $z$. The $y$-value is a constant at $y_0$, so $y$ is not a variable. We define the partial derivative of $f$ with respect to $x$ at the point $(x_0, y_0)$ as the ordinary derivative of $f(x, y_0)$ with respect to $x$ at the point $x = x_0$.

> 🖼️ **Image Description:** A 3D graph explaining the concept of a partial derivative with respect to $x$. A translucent grey surface $z = f(x, y)$ is shown. A vertical blue plane is positioned at a constant $y = y_0$. The intersection of this plane and the surface forms a blue curve labeled "The curve $z = f(x, y_0)$ in the plane $y = y_0$". A specific point $P(x_0, y_0, f(x_0, y_0))$ on this curve is highlighted, and a red tangent line is drawn through it. The slope of this red tangent line represents the partial derivative $\frac{\partial f}{\partial x}$.

**Definition**
The **partial derivative of $f(x, y)$ with respect to $x$** at the point $(x_0, y_0)$ is
$$ \frac{\partial f}{\partial x} \bigg|_{(x_0, y_0)} = f'_x(x_0, y_0) = f_x(x_0, y_0) = \frac{d}{dx} f(x, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}. $$

---

### Slide 17

**Partial Derivatives**

**Definition**
The **partial derivative of $f(x, y)$ with respect to $y$** at the point $(x_0, y_0)$ is
$$ \frac{\partial f}{\partial y} \bigg|_{(x_0, y_0)} = f'_y(x_0, y_0) = f_y(x_0, y_0) = \frac{d}{dy} f(x_0, y) $$
$$ = \lim_{h \to 0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}, $$
provided the limit exists.

**In general,** if $f(x_1, \dots, x_n)$ is a function of $n$ variables, its partial derivative with respect to the $i$th variable $x_i$ at the point $P(p_1, \dots, p_n) \in \mathbb{R}^n$ is
$$ \frac{\partial f}{\partial x_i} \bigg|_{P} = f'_{x_i} \bigg|_{P} = f_{x_i} \bigg|_{P} $$
$$ = \lim_{h \to 0} \frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(x_1, \dots, x_i, \dots, x_n)}{h}, $$
provided the limit exists.

> 🖼️ **Image Description:** Similar to the previous slide's 3D graph, but illustrating the partial derivative with respect to $y$. This time, a vertical plane is held constant at $x = x_0$. The intersection forms a blue curve "The curve $z = f(x_0, y)$ in the plane $x = x_0$". A point $P(x_0, y_0, f(x_0, y_0))$ is selected, and a red tangent line is drawn at that point. The slope of this tangent line represents the partial derivative $\frac{\partial f}{\partial y}$.

---

### Slide 18

**Partial Derivatives: Examples**

**Example 1.** For the function $f(x, y) = 2x^2 - xy^2 + x^3y + y^2$, we have
$$ \frac{\partial f}{\partial x} = 4x - y^2 + 3x^2y, \qquad \frac{\partial f}{\partial y} = -2xy + x^3 + 2y. \quad \text{\color{red}{(Check by the definition!)}} $$

**Example 2.** For the function $f(x, y) = \sqrt{x^2 + y^2}$, we have
$$ \frac{\partial f}{\partial x} = \frac{x}{\sqrt{x^2 + y^2}}, \qquad \frac{\partial f}{\partial y} = \frac{y}{\sqrt{x^2 + y^2}}. \quad \text{\color{red}{(Check by the definition!)}} $$

**Example 3.** For the function $f(x, y) = e^{-x^2} \sin(x + 5y)$, we have
$$ \frac{\partial f}{\partial x} = e^{-x^2} (-2x \sin(x + 5y) + \cos(x + 5y)), \qquad \frac{\partial f}{\partial y} = 5e^{-x^2} \cos(x + 5y). $$

**Example 4.** For the function $f(x, y, z) = \arcsin(xy^2z^3)$, we have
$$ \frac{\partial f}{\partial x} = \frac{y^2z^3}{\sqrt{1 - x^2y^4z^6}}, \qquad \frac{\partial f}{\partial y} = \frac{2xyz^3}{\sqrt{1 - x^2y^4z^6}}, \qquad \frac{\partial f}{\partial z} = \frac{3xy^2z^2}{\sqrt{1 - x^2y^4z^6}}. $$

**Example 5.** For the function $f(x_1, x_2, x_3) = x_1 - \sqrt{x_2^2 + 5x_3^2}$, we have
$$ \frac{\partial f}{\partial x_1} = 1, \qquad \frac{\partial f}{\partial x_2} = -\frac{x_2}{\sqrt{x_2^2 + 5x_3^2}}, \qquad \frac{\partial f}{\partial x_3} = -\frac{5x_3}{\sqrt{x_2^2 + 5x_3^2}}. $$

---

### Slide 19

**Second and Higher Order Partial Derivatives**

**Second Order Partial Derivatives.** When we differentiate $f(x, y)$ twice, where the first partial derivatives exist, we produce its second-order derivatives. These derivatives are usually denoted by
1. $\frac{\partial^2 f}{\partial x^2} = f''_{xx} = f_{xx} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial x} \right),$
2. $\frac{\partial^2 f}{\partial y^2} = f''_{yy} = f_{yy} = \frac{\partial}{\partial y} \left( \frac{\partial f}{\partial y} \right),$
3. $\frac{\partial^2 f}{\partial x \partial y} = f''_{yx} = f_{yx} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial y} \right),$
4. $\frac{\partial^2 f}{\partial y \partial x} = f''_{xy} = f_{xy} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial y} \right).$

**Theorem (The Mixed Derivative Theorem or Clairaut's (or Schwarz's) Theorem)**
If $f(x, y)$ and its partial derivatives $f'_x, f'_y, f''_{xy}, f''_{yx}$ are defined throughout an open region containing a point $(a, b)$ and are all **continuous** at $(a, b)$, then $\text{\color{blue}{f''_{xy}(a, b) = f''_{yx}(a, b).}}$

**Higher Order Partial Derivatives.**
$$ \frac{\partial^3 f}{\partial x \partial y^2} = f'''_{yyx} = f_{yyx}, \qquad \frac{\partial^4 f}{\partial x^2 \partial y^2} = f^{(4)}_{yyxx} = f_{yyxx}, \qquad \frac{\partial^4 f}{\partial x \partial z \partial y \partial z} = f^{(4)}_{zyzx} = f_{zyzx}, \quad \dots $$

---

### Slide 20

**Partial Derivatives: Exercises**

**Definition (Harmonic Function)**
Let $f(x_1, \dots, x_n)$ has second order partial derivatives with respect to $x_i$, for $i = 1, \dots, n$. We say that $f$ is **harmonic**, if $\frac{\partial^2 f}{\partial x_1^2} + \frac{\partial^2 f}{\partial x_2^2} + \dots + \frac{\partial^2 f}{\partial x_n^2} = 0$. This equation called **$n$-dimensional Laplace equation**.

**<span style="color:red">Exercise 1.</span>** Find the first and second partial derivatives of the function
$$ f(x, y) = \ln(x^2y + 2xy + 5), \qquad f(x, y, z, t) = x^2y \cos\left(\frac{z}{t}\right), \qquad f(x, y, z) = xy^2e^{-xz}. $$

**<span style="color:red">Exercise 2.</span>** Find a function $z = f(x, y)$ whose partial derivatives are as given
1. $\frac{\partial f}{\partial x} = 3x^2y^2 - 2x, \qquad \frac{\partial f}{\partial y} = 2x^3y + 6y.$
2. $\frac{\partial f}{\partial x} = xy \cos(xy) + \sin(xy), \qquad \frac{\partial f}{\partial y} = x^2 \cos(xy).$

**<span style="color:red">Exercise 3.</span>** Determine whether each of the following functions is a solution of Laplace's equation
$$ f(x, y) = x^3 + 3xy^2, \qquad f(x, y) = \sin x \cosh y + \cos x \sinh y, \qquad f(x, y) = \ln(\sqrt{x^2 + y^2}). $$

---

### Slide 21

**Partial Derivatives: Differentiability**

Recall that if the function of a single variable $y = f(x)$ is differentiable at $x = x_0$, then
$$ f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} \stackrel{\Delta x \neq 0}{\implies} f'(x_0) \approx \frac{\Delta y}{\Delta x} \implies \frac{\Delta y}{\Delta x} = f'(x_0) + \varepsilon, $$
where $\varepsilon$ is some number that depends on $\Delta x$, and as $\Delta x \to 0$, $\varepsilon \to 0$. Thus, the change in the value of $f$ that results from changing $x$ from $x_0$ to $x_0 + \Delta x$ is given by the equation
$$ \Delta y = f'(x_0)\Delta x + \varepsilon\Delta x, $$
For functions of two variables (and more), the analogous property becomes the definition of differentiability.

**Definition (Differentiable Function of Two Variables)**
A function $z = f(x, y)$ is **differentiable at** $(x_0, y_0)$ if both $f'_x(x_0, y_0)$ and $f'_y(x_0, y_0)$ **exist** and if $\Delta z = f(x, y) - f(x_0, y_0)$ satisfies
$$ \Delta z = f'_x(x_0, y_0)\Delta x + f'_y(x_0, y_0)\Delta y + \varepsilon_1\Delta x + \varepsilon_2\Delta y, $$
where $\Delta x = x - x_0$, $\Delta y = y - y_0$, and both $\varepsilon_1 \to 0$ and $\varepsilon_2 \to 0$ as $(x, y) \to (x_0, y_0)$.
We call the function $f$ **differentiable** if it is differentiable at every point in its domain, and we then say that its graph is a **smooth surface**.

---

### Slide 22

**Partial Derivatives: linearization and tangent plane**

For the class of differentiable functions with several variables and their connection with continuity, we have the following theorem.

**Theorem**
*If the partial derivatives $f'_x$ and $f'_y$ **exist** near a point $(a, b)$, and are **continuous** at $(a, b)$, then $f$ is differentiable at $(a, b)$.*

**Corollary.** If the partial derivatives $f'_x$ and $f'_y$ of a function $f(x, y)$ are continuous throughout an open region $R$, then $f$ is differentiable at every point of $R$.

**Example 1.** The function $f(x, y) = x^2 + y^2$ is differentiable at any point in $\mathbb{R}^2$, since $f'_x(x, y) = 2x, \ f'_y(x, y) = 2y$ are continuous functions at all points in $\mathbb{R}^2$.

The **linearization** of a differentiable function $f$ at $(x_0, y_0)$ is
$$ \mathcal{L}(x, y) = f(x_0, y_0) + f'_x(x_0, y_0)(x - x_0) + f'_y(x_0, y_0)(y - y_0). $$
The graph of this linear function is the **tangent plane** to the surface $S = \{(x, y) \mid z = f(x, y)\}$ at the point $(x_0, y_0, f(x_0, y_0))$.

---

### Slide 23

**Partial Derivatives: linearization and tangent plane**

For example, near the point $(1, 3)$, for the function $f(x, y) = x^2 + y^2$, we have the linearization
$$ \mathcal{L}(x, y) = 2x + 6y - 10 \approx f(x, y) = x^2 + y^2, \quad \text{near } (1, 3). $$
Thus, for the value $f(1.1, 2.8)$ (as an example only), we can write
$$ 9.05 = f(1.1, 2.8) \approx \mathcal{L}(1.1, 2.8) = 9. $$
The approximation $f(x, y) \approx \mathcal{L}(x, y)$ at the point $(x_0, y_0)$ is called **linear approximation** or the **tangent plane approximation** of $f$ at $(x_0, y_0)$.

> 🖼️ **Image Description:** Three 3D plots showing a sequence of zoom-ins.
> *   **Left:** A red paraboloid surface $z = x^2 + y^2$ is shown alongside a blue tangent plane that touches it at a specific point.
> *   **Middle:** A closer view of the intersection between the red paraboloid and the blue tangent plane.
> *   **Right:** An even closer view, showing how the blue tangent plane closely approximates the curved red surface near the point of tangency (marked with a green dot).

---

### Slide 24

**Partial Derivatives: linearization and tangent plane**

**Example 2.** The function $f(x, y) = xe^{xy}$ is differentiable at any point $(\alpha, \beta) \in \mathbb{R}^2$, since
$$ f'_x(x, y) = (1 + xy)e^{xy}, \quad f'_y(x, y) = x^2 e^{xy} $$
are continuous functions at all points in $\mathbb{R}^2$. Near the point $(1, 0)$, we have the linearization
$$ \mathcal{L}(x, y) = x + y \approx f(x, y) = xe^{xy}. $$
Thus, for example, for the value for $f$ at the point $(1.1, -0.1)$, we can write
$$ 1.1, -0.1 = 1 \approx f(1.1, -0.1) = 1.1e^{-0.11} \approx 0.98542. $$

> 🖼️ **Image Description:** Two 3D plots illustrating a tangent plane on a complex surface.
> *   **Left:** A red saddle-like surface representing the function $f(x,y) = x e^{xy}$. A blue dot is placed on the surface.
> *   **Right:** A green plane intersects the red surface at the blue dot. This green plane is the tangent plane, linearly approximating the saddle surface around the given point $(1,0)$.

---

### Slide 25

**Partial Derivatives: Differentiability**

If $z = f(x, y)$ is differentiable, then the definition of differentiability ensures that $\Delta z = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)$ approaches $0$ as $\Delta x$ and $\Delta y$ approach $0$. This tells us that a function of two variables (and analogously of several variables) is continuous at every point where it is differentiable.

**Theorem (Differentiability Implies Continuity)**
*If a function $f(x, y)$ is differentiable at $(x_0, y_0)$, then $f$ is continuous at $(x_0, y_0)$.*

**Remark.** Existence alone of the partial derivatives at that point is **not enough**, but continuity of the partial derivatives guarantees differentiability.

**Example.** The function $f(x, y) = \begin{cases} 0, & xy \neq 0 \\ 1, & xy = 0 \end{cases}$, its graph consists of the lines $L_1$ and $L_2$ (lying $1$ unit above the $xy$-plane) and the four open quadrants of the $xy$-plane. Since $f(x, y) = 0$ along $y = x$ (except at $(0, 0)$), the limit of $f$ as $(x, y) \to (0, 0)$ along $y = x$ is $0$. So $f$ is not continuous at $(0, 0)$, since $f(0, 0) = 1$. To find $\partial f/\partial x$ at $(0, 0)$, we hold $y$ fixed at $y = 0$. Then $f(x, y) = 1$ for all $x$, and the graph of $f$ is the line $L_1$, with slope $\partial f/\partial x = 0$. Similarly, $\partial f/\partial y$ is the slope of line $L_2$ at any $y$, so $\partial f/\partial y = 0$.

> 🖼️ **Image Description:** A 3D graph representing the piecewise function defined in the text. The graph shows a blue plane at $z=0$ for all points where $x$ and $y$ are non-zero. Along the $x$-axis and $y$-axis (where $xy=0$), the value of the function jumps to $z=1$, forming a cross shape (represented by blue lines $L_1$ and $L_2$) elevated 1 unit above the $xy$-plane.

---

### Slide 26

**Partial Derivatives: Chain Rule**

**Theorem (The Chain Rule)**
**Case 1.** *If $z = f(x, y)$ is differentiable and if $x = x(t), y = y(t)$ are differentiable functions of $t$, then the composition $z = f(x(t), y(t))$ is a differentiable function of $t$ and*
$$ \text{\color{red}{\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}.}} $$

**Case 2.** *Suppose that $z = f(x, y), x = g(s, t)$, and $y = h(s, t)$. If all theses functions are differentiable, then $z$ has partial derivatives with respect to $s$ and $t$, given by the formulas*
$$ \text{\color{red}{\frac{\partial z}{\partial s} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial s}, \qquad \frac{\partial z}{\partial t} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial t}.}} $$

**Remark (General Version of Chain Rule).** In general, suppose that $w = f(x_1, x_2, \dots, x_n)$ is a differentiable function of the intermediate variables $x_1, x_2, \dots, x_n$ (a finite set) and that $x_1, x_2, \dots, x_n$ are differentiable functions of the independent variables $t_1, t_2, \dots, t_m$ (another finite set). Then $w$ is a differentiable function of the variables $t_1, t_2, \dots, t_m$, and the partial derivatives of $w$ with respect to these variables are given by equations
$$ \frac{\partial w}{\partial t_i} = \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial t_i} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial t_i} + \dots + \frac{\partial w}{\partial x_n}\frac{\partial x_n}{\partial t_i}; \quad \text{for } i = 1, 2, \dots, m. $$

---

### Slide 27

**Partial Derivatives: Implicit Differentiation**

The Chain Rule can be used to give a more complete description of the process of implicit differentiation.
Suppose that an equation of the form $F(x, y) = 0$ defines $y$ implicitly as a differentiable function of $x$, that is, $y = f(x)$, where $F(x, f(x)) = 0$ for all $x$ in the domain of $f$. If $F$ is differentiable, we can apply **Case 1** of the Chain Rule to differentiate both sides of the equation $F(x, y) = 0$ with respect to $x$. Since both $x$ and $y$ are functions of $x$, we obtain
$$ \frac{\partial F}{\partial x}\frac{dx}{dx} + \frac{\partial F}{\partial y}\frac{dy}{dx} = 0 \implies F'_x + F'_y \frac{dy}{dx} = 0 \implies \boxed{\frac{dy}{dx} = f' = -\frac{F'_x}{F'_y}} \quad (1) $$

The **Implicit Function Theorem**, proved in advanced calculus states that:
If $F$ is defined on a disk containing $(a, b)$, where $F(a, b) = 0$, $F'_y(a, b) \neq 0$, and $F'_x$ and $F'_y$ are continuous on the disk, then the equation $F(x, y) = 0$ defines $y$ as a function of $x$ near the point $(a, d)$ and the derivative of this function is given by Equation (1).

Similarly, if we have an equation $F(x, y, z) = 0$ that defines $z$ implicitly as a function $z = f(x, y)$. Then, for all $(x, y)$ in the domain of $f$, we have $F(x, y, f(x, y)) = 0$.
Assuming that $F$ and $f$ are differentiable functions and $F'_z \neq 0$, then we have
$$ \boxed{\frac{\partial z}{\partial x} = -\frac{F'_x}{F'_z}, \quad \text{and} \quad \frac{\partial z}{\partial y} = -\frac{F'_y}{F'_z}} $$

---

### Slide 28

**Chain Rule and Implicit Differentiation: Examples**

**Example 1.** Assuming that $y \cos x = x^2 + y^2$ defines $y$ as a differentiable function of $x$, then we have $F(x, y) := x^2 + y^2 - y \cos x = 0$, and
$$ \frac{dy}{dx} = -\frac{F'_x}{F'_y} = -\frac{2x + y \sin x}{2y - \cos x}. $$

**Example 2.** Assuming that $F(x, y, z) := e^z - xyz = 0$ defines $z$ as a differentiable function of $x$ and $y$. Then
$$ \frac{\partial z}{\partial x} = -\frac{F'_x}{F'_z} = \frac{yz}{e^z - xy}, \qquad \frac{\partial z}{\partial y} = -\frac{F'_y}{F'_z} = \frac{xz}{e^z - xy}. $$

**Example 3.** For the function $z = xy^3 - x^2y$, with $x = t^2 + 1$, $y = t^2 - 1$, we have
$$ \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} = 2t \left[ (y^3 - 2xy) + (3xy^2 - x^2) \right]_{x=t^2+1,\ y=t^2-1} $$
$$ = 2t \left( (t^2 - 1)^3 - 2(t^4 - 1) + 3(t^2 + 1)(t^2 - 1)^2 - (t^2 + 1)^2 \right) $$
$$ = 8t^7 - 18t^5 - 4t^3 + 6t. $$

---

### Slide 29

**Example 4.** For the function $z = \arctan(x^2 + y^2)$, with $x = s \ln t$ and $y = t e^s$, we have
$$ \frac{\partial z}{\partial x} = \frac{2x}{1 + (x^2 + y^2)^2}, \qquad \frac{\partial z}{\partial y} = \frac{2y}{1 + (x^2 + y^2)^2}, $$
and
$$ \frac{\partial x}{\partial t} = \frac{s}{t}, \qquad \frac{\partial x}{\partial s} = \ln t, \qquad \frac{\partial y}{\partial t} = e^s, \qquad \frac{\partial y}{\partial s} = t e^s. $$
Therefore,
$$ \frac{\partial z}{\partial t} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial t} $$
$$ = \frac{s}{t} \left[ \frac{2x}{1 + (x^2 + y^2)^2} \right]_{x=s \ln t,\ y=te^s} + e^s \left[ \frac{2y}{1 + (x^2 + y^2)^2} \right]_{x=s \ln t,\ y=te^s} $$
$$ = \frac{2(s^2 \ln^2 t + t^2 e^{2s})}{t + t(s^2 \ln^2 t + t^2 e^{2s})^2}. $$

Similarly, we find
$$ \frac{\partial z}{\partial s} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial s} = \frac{2(s \ln^2 t + t^2 e^{2s})}{1 + (s^2 \ln^2 t + t^2 e^{2s})^2}. $$

---

### Slide 30

**Chain Rule and Implicit Differentiation: Exercises**

**<span style="color:red">Exercise 1.</span>** Find $\frac{dz}{dt}$ for each of the following
1. $z = \sin x \sin y$, with $x = \sqrt{t}, y = \frac{1}{t}$;
2. $z = \ln(x^2 + y^2 + w^2)$, with $x = se^t \sin s, y = \arctan t$.

**<span style="color:red">Exercise 2.</span>** Find $\frac{\partial z}{\partial s}$ and $\frac{\partial z}{\partial t}$ for each of the following
1. $z = \sin x \sin y$, with $x = \sqrt{t}, y = \frac{1}{t}$;
2. $z = \ln(2p^3 + 3q^2 + 2r^4)$, with $p = se^t \sin s, q = se^t \cos s, r = se^t$.

**<span style="color:red">Exercise 3.</span>** Assuming that the following equations define $y$ as a differentiable function of $x$, find $\frac{dy}{dx}$ at the given point.
1. $xe^y + \sin(xy) + y - \ln 2 = 0, \quad (0, \ln 2)$;
2. $xe^{x^2y} - ye^x = x + y - 2, \quad (1, 1)$.

**<span style="color:red">Exercise 4.</span>** Assuming that the following equations define $z$ as a differentiable function of $x$ and $y$, find $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$ at the given point.
1. $z^3 - xy + yz - y^3 - 2 = 0, \quad (1, 1, 1)$;
2. $xe^y + ye^z + 2 \ln x - 2 - 3 \ln 2 = 0, \quad (1, \ln 2, \ln 3)$.

---

### Slide 31

**Directional Derivative**

Suppose that the function $f(x, y)$ is defined throughout a region $R$ in the $xy$-plane, that $P_0(x_0, y_0)$ is a point in $R$, and that $\mathbf{u} = u_1\hat{\mathbf{i}} + u_2\hat{\mathbf{j}}$ is a unit vector (i.e., $||\mathbf{u}||_2 = \sqrt{u_1^2 + u_2^2} = 1$). Then the equations
$$ x = x_0 + u_1 s, \qquad y = y_0 + u_2 s, \qquad \forall s \in \mathbb{R}, $$
parametrize the line through $P_0$ parallel to $\mathbf{u}$. If the parameter $s$ measures arc length from $P_0$ in the direction of $\mathbf{u}$, we find the rate of change of $f$ at $P_0$ in the direction of $\mathbf{u}$ by calculating $\frac{df}{ds}$ at $P_0$.

**Definition (The directional derivative)**
The **directional derivative of $f$ at $P_0(x_0, y_0)$ in the direction of a unit vector** $\mathbf{u} = u_1\hat{\mathbf{i}} + u_2\hat{\mathbf{j}}$ is the number
$$ D_{\mathbf{u}} f(x_0, y_0) = \left( \frac{df}{ds} \right)_{\mathbf{u}, P_0} = \lim_{s \to 0} \frac{f(x_0 + u_1s, y_0 + u_2s) - f(x_0, y_0)}{s}. $$

**In general in** $\mathbb{R}^n$, the directional derivative of $f$, with $n$ several variables, at a point $P_0$ in the direction of a unit vector $\mathbf{u}$ is the number $D_{\mathbf{u}} f(P_0) = \text{\color{red}{\lim_{s \to 0} \frac{f(P_0 + s\mathbf{u}) - f(P_0)}{s}}}$.

---

### Slide 32

**Directional Derivative**

**Example.** The directional derivative of the function $f(x, y) = x^2 + xy$ at $P_0(1, 2)$ in the direction of $\mathbf{u} = (1/\sqrt{2})\hat{\mathbf{i}} + (1/\sqrt{2})\hat{\mathbf{j}}$ is
$$ D_{\mathbf{u}} f(P_0) = \lim_{s \to 0} \frac{f(x_0 + u_1s, y_0 + u_2s) - f(x_0, y_0)}{s} $$
$$ = \lim_{s \to 0} \frac{f\left(1 + (s/\sqrt{2}), 2 + (s/\sqrt{2})\right) - f(1, 2)}{s} = \lim_{s \to 0} \frac{(5s/\sqrt{2}) + s^2}{s} = \frac{5}{\sqrt{2}}. $$

**Interpretation of the Directional Derivative.**
The equation $z = f(x, y)$ represents a surface $S$ in space. If $z_0 = f(x_0, y_0)$, then the point $P(x_0, y_0, z_0)$ lies on $S$. The vertical plane that passes through $P$ and $P_0(x_0, y_0)$ parallel to $\mathbf{u}$ intersects $S$ in a curve $C$. The rate of change of $f$ in the direction of $\mathbf{u}$ is the slope of the tangent to $C$ at $P$ in the right-handed system formed by the vectors $\mathbf{u}$ and $\hat{\mathbf{k}}$. When $\mathbf{u} = \hat{\mathbf{i}}$, the directional derivative at $P$ is $f'_x(x_0, y_0)$. When $\mathbf{u} = \hat{\mathbf{j}}$, the directional derivative at $P$ is $f'_y(x_0, y_0)$. <span style="color:red">So the directional derivative generalizes the partial derivatives, thus we can now ask for the rate of change of $f$ in any direction $\mathbf{u}$, not just in the directions $\hat{\mathbf{i}}$ and $\hat{\mathbf{j}}$.</span>

> 🖼️ **Image Description:** A 3D graph showing a light blue surface $S$ defined by $z=f(x,y)$. A vertical plane passes through the surface, positioned parallel to a vector $\mathbf{u}$ on the $xy$-plane. The intersection of this plane and the surface forms a curved line $C$. A point $P(x_0, y_0, z_0)$ is marked on this curve. A red tangent line labeled $Q$ touches the curve $C$ at point $P$. The slope of this tangent line represents the directional derivative $D_{\mathbf{u}} f$. On the $xy$-plane, the vector $\mathbf{u} = u_1\mathbf{i} + u_2\mathbf{j}$ originates from $P_0(x_0,y_0)$.

---

### Slide 33

**Directional Derivative and Gradient**

**Definition**
The gradient of the function $f(x_1, x_2, \dots, x_n)$ at the point $P_0$ is the vector
$$ \nabla f \bigg|_{P_0} = \nabla f(P_0) = \begin{pmatrix} \frac{\partial f}{\partial x_1}(P_0) & \frac{\partial f}{\partial x_2}(P_0) & \dots & \frac{\partial f}{\partial x_n}(P_0) \end{pmatrix}^\top. $$

**Theorem (Directional Derivative and Gradient)**
*If $f(x_1, x_2, \dots, x_n)$ is differentiable in an open region containing the point $P_0$, then*
$$ D_{\mathbf{u}} f(P_0) = \nabla f(P_0) \cdot \mathbf{u}. $$
*That is, the dot product of the gradient $\nabla f$ at $P_0$ with the unit vector $\mathbf{u}$. In brief, $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$.*

**Proof.** Let us prove the theorem for functions with two variables.
Let $P_0(x_0, y_0)$, and $\mathbf{u} = u_1\hat{\mathbf{i}} + u_2\hat{\mathbf{j}}$. The equations $x = x_0 + u_1s$, and $y = y_0 + u_2s$ ($s \in \mathbb{R}$) parametrize the line through $P_0$ and parallel to $\mathbf{u}$. Then by the Chain Rule, we find
$$ \left( \frac{df}{ds} \right)_{\mathbf{u}, P_0} = \left( \frac{\partial f}{\partial x} \right)_{P_0} \frac{dx}{ds} + \left( \frac{\partial f}{\partial y} \right)_{P_0} \frac{dy}{ds} = \left( \frac{\partial f}{\partial x} \right)_{P_0} u_1 + \left( \frac{\partial f}{\partial y} \right)_{P_0} u_2 = \nabla f(P_0) \cdot \mathbf{u}. \quad \square $$

---

### Slide 34

**Directional Derivative and Gradient**

**Example.** Find the derivative of $f(x, y) = \arctan(y/x) + \sqrt{3} \arcsin(xy/2)$, at the point $P_0(1, 1)$, in the direction of $\mathbf{v} = 3\hat{\mathbf{i}} - 2\hat{\mathbf{j}}$.

**Solution.** The unit vector $\mathbf{u}$ parallel to $\mathbf{v}$ is $\mathbf{u} = \frac{\mathbf{v}}{||\mathbf{v}||_2} = \frac{3}{\sqrt{13}}\hat{\mathbf{i}} - \frac{2}{\sqrt{13}}\hat{\mathbf{j}}$. We have
$$ f'_x \bigg|_{P_0} = \left. \frac{-y/x^2}{1 + (y/x)^2} + \frac{\sqrt{3}y/2}{\sqrt{1 - (xy/2)^2}} \right|_{P_0} = \frac{1}{2}, \quad f'_y \bigg|_{P_0} = \left. \frac{1/x}{1 + (y/x)^2} + \frac{\sqrt{3}x/2}{\sqrt{1 - (xy/2)^2}} \right|_{P_0} = \frac{3}{2}. $$

$$ D_{\mathbf{u}} f(P_0) = \nabla f(P_0) \cdot \mathbf{u} = \begin{pmatrix} \frac{1}{2} \\ \frac{3}{2} \end{pmatrix} \begin{pmatrix} \frac{3}{\sqrt{13}} \\ -\frac{2}{\sqrt{13}} \end{pmatrix} = \boxed{ -\frac{3}{2\sqrt{13}} } $$

**Remark.** From the formula of the directional derivative, we have
$$ D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = ||\nabla f||_2 \cdot ||\mathbf{u}||_2 \cos(\theta) = ||\nabla f||_2 \cos(\theta), $$
where $\theta$ is the angle between the vectors $\mathbf{u}$ and $\nabla f$. Therefore, we get the following:
1. The function $f$ increases most rapidly when $\cos(\theta) = 1$, which means that $\theta = 0$, and $\mathbf{u}$ is the direction of $\nabla f$. That is, at each point $P$ in its domain, <span style="color:red"> $f$ increases most rapidly in the direction of the gradient vector $\nabla f$ at $P$.</span> The derivative in this direction is $D_{\mathbf{u}} f = ||\nabla f||_2 \cos(0) = ||\nabla f||_2$.
2. Similarly, <span style="color:red"> $f$ decreases most rapidly in the direction of $-\nabla f$.</span> The derivative in this direction is $D_{\mathbf{u}} f = ||\nabla f||_2 \cos(\pi) = -||\nabla f||_2$.

---

### Slide 35

**Gradients and Tangents to Level Curves**

If a differentiable function $f(x, y)$ has a constant value $c$ along a smooth curve $\mathbf{r} = g(t)\hat{\mathbf{i}} + h(t)\hat{\mathbf{j}}$ (making the curve part of a level curve of $f$), then $f(g(t), h(t)) = c$.
Differentiating both sides of this equation with respect to $t$ leads to the equations
$$ \frac{df}{dt} = \frac{d}{dt}(c) = 0 \implies \frac{\partial f}{\partial x}\frac{dg}{dt} + \frac{\partial f}{\partial y}\frac{dh}{dt} = 0 \implies \left( \frac{\partial f}{\partial x}\hat{\mathbf{i}} + \frac{\partial f}{\partial y}\hat{\mathbf{j}} \right) \cdot \left( \frac{dg}{dt}\hat{\mathbf{i}} + \frac{dh}{dt}\hat{\mathbf{j}} \right) = 0. $$

Thus, assuming the gradient of $f$ is a nonzero vector, we find that $\nabla f$ is **normal to the tangent vector $\frac{d\mathbf{r}}{dt}$**, so it is **normal to the curve**.
Therefore, we get the following result

<span style="color:red">At every point $P_0$ (in $\mathbb{R}^n$) in the domain of a differentiable function $f(x_1, \dots, x_n)$, where the gradient $\nabla f$ is a nonzero vector, this vector is normal to the level curve through $P_0$.</span>

> 🖼️ **Image Description:** A 3D illustration demonstrating gradients on a level curve. A light green plane shows a set of red contour lines (level curves) representing the function $f(x, y) = f(x_0, y_0)$. A specific point $(x_0, y_0)$ lies on one of the red curves. At this point, a blue arrow points perpendicularly outward from the red curve. This blue arrow is labeled $\nabla f(x_0, y_0)$, indicating that the gradient vector is orthogonal to the level curve at that point.

---

### Slide 36

**Directional Derivative and Gradient: Exercises**

**<span style="color:red">Exercise 1.</span>** Find the gradient of the function at the given point
1. $f(x, y) = \arctan\left(\frac{\sqrt{x}}{y}\right), \quad (4, -2)$;
2. $f(x, y, z) = (x^2 + y^2 + z^2)^{-1/2} + \ln(xyz), \quad (-1, 2, -2)$;
3. $f(x, y, z) = e^{x+y}\cos z + (y + 1)\arcsin x, \quad (0, 0, \pi/6)$.

**<span style="color:red">Exercise 2.</span>** Find the derivative of the function at the point $P_0$ in the direction of $\mathbf{u}$.
1. $f(x, y) = \frac{x-y}{xy+2}, \quad P_0(1, -1), \quad \mathbf{u} = 12\hat{\mathbf{i}} + 5\hat{\mathbf{j}}$;
2. $f(x, y, z) = x^2 + 2y^2 - 3z^2, \quad P_0(1, 1, 1), \quad \mathbf{u} = 2\hat{\mathbf{i}} + \hat{\mathbf{j}} - 2\hat{\mathbf{k}}$;
3. $f(x, y, z) = \cos(yz) + e^{yz} + \ln(xz), \quad P_0(1, 0, 1/2), \quad \mathbf{u} = \hat{\mathbf{i}} + 2\hat{\mathbf{j}} + 2\hat{\mathbf{k}}$.

**<span style="color:red">Exercise 3.</span>** Find the directions in which the functions increase most rapidly, and the directions in which they decrease most rapidly, at $P_0$. Then find the derivatives of the functions in these directions.
1. $f(x, y) = x^2y + e^{xy}\sin y, \quad P_0(1, 0)$;
2. $f(x, y, z) = xe^y + z^2, \quad P_0(1, \ln 2, 1/2)$;
3. $f(x, y, z) = \ln(x^2 + y^2 - 1) + y + 6z, \quad P_0(1, 1, 0)$.

---

### Slide 37

**Extreme Values for Functions of Several Variables**

**Definition (Extreme Values)**
Let $f(x_1, \dots, x_n)$ be a function defined on a region $R \subseteq \mathbb{R}^n$ containing the point $x_0$. Then
1. $f(x_0)$ is a **local maximum** value of $f$ if $f(x_0) \ge f(x)$ for all domain points $x$ in an open ball centered at $x_0$.
   $f(x_0)$ is an **absolute (global) maximum** value of $f$ on $R$ if $f(x_0) \ge f(x) \ \forall x \in R$.
2. $f(x_0)$ is a **local minimum** value of $f$ if $f(x_0) \le f(x)$ for all domain points $x$ in an open ball centered at $x_0$.
   $f(x_0)$ is an **absolute (global) minimum** value of $f$ on $R$ if $f(x_0) \le f(x) \ \forall x \in R$.

> 🖼️ **Image Description:** A 3D topographical surface plot representing a function of two variables. It clearly marks four distinct points:
> 1.  The highest peak of the entire surface is labeled "Absolute maximum. No greater value of $f$ anywhere. Also a local maximum."
> 2.  The lowest valley of the entire surface is labeled "Absolute minimum. No smaller value of $f$ anywhere. Also a local minimum."
> 3.  A secondary, smaller peak is labeled "Local maximum. No greater value of $f$ nearby." The neighborhood is represented by a small red dashed ellipse on the peak.
> 4.  A secondary, shallower valley is labeled "Local minimum. No smaller value of $f$ nearby." The neighborhood is represented by a small red dashed ellipse inside the valley.

---

### Slide 38

**Extreme Values for Functions of Several Variables**

**Definition (Critical Point)**
An interior point $P_0 \in \mathbb{R}^n$ of the domain of a function $f(x_1, \dots x_n)$ where $f'_{x_1} = f'_{x_2} = \dots = f'_{x_n} = 0$ (i.e., $\nabla f(P_0) = \mathbf{0}$) or where one or more of $f'_{x_1}, \dots f'_{x_n}$ do not exist is a **critical point** of $f$.

**Theorem (First Derivative Theorem for Local Extreme Values)**
*If $f(x)$, where $x \in \mathbb{R}^n$, has a local maximum or minimum value at an interior point $x_0$ of its domain and if the first partial derivatives exist there, then $\nabla f(x_0) = \mathbf{0} \in \mathbb{R}^n$.*

**Proof.** Let us prove this theorem for functions with two variables; the same proof will work for functions with several variables.
If $f$ has a local extremum at $(a, b)$, then the function $g(x) = f(x, b)$ has a local extremum at $x = a$. Therefore, $g'(a) = 0$. But $g'(a) = f'_x(a, b)$, so $f'_x(a, b) = 0$. A similar argument with the function $h(y) = f(a, y)$ shows that $f'_y(a, b) = 0$. $\square$

> 🖼️ **Image Description:** A 3D graph showing a light blue surface forming a hill-shaped local maximum. A point $(a, b, 0)$ on the $xy$-plane corresponds to the top of the peak on the surface. At the peak, two red tangent lines are drawn. One is parallel to the $x$-axis, where $\frac{\partial f}{\partial x} = 0$. The other is parallel to the $y$-axis, where $\frac{\partial f}{\partial y} = 0$. This visualizes that the tangent plane is completely horizontal at the local maximum.

---

### Slide 39

**Extreme Values for Functions of Several Variables**

**Definition (Saddle Point)**
A differentiable function $f(x)$ (where $x \in \mathbb{R}^n$) has a **saddle point** at a critical point $P_0$ if in every open ball centered at $P_0$ there are domain points $x$ where $f(x) > f(P_0)$ and domain points $x$ where $f(x) < f(P_0)$. The corresponding point $(x, f(P_0)) \in \mathbb{R}^{n+1}$ on the hypersurface $w = f(x)$ is called a saddle point of the hypersurface.

**Example.** The function of two variables $f(x, y) = 2x^3 - 3x^2 - 2y^3 + 3y^2$ is defined on the entire plane $\mathbb{R}^2$, so there are no boundary points, and the partial derivatives $f'_x = 6x^2 - 6x$ and $f'_y = -6y^2 + 6y$ exist everywhere. Therefore, local extreme values can occur only where
$$ f'_x = 6x^2 - 6x = 0, \quad \text{and} \quad f'_y = -6y^2 + 6y = 0. $$
Thus, the critical points (local extrema or saddle) are $(0, 0), (1, 0), (0, 1), (1, 1)$.

**Remarks.**
* Note that $f'_x(a, b) = f'_y(a, b) = 0$ at an interior point $(a, b)$ of $R$ does not guarantee that $f$ has a local extreme value there (the same argument for functions with more than two variables).
* If $f$ and its first and second partial derivatives are continuous on $R$, however, we may be able to learn more about the classification of critical points from the following theorem.

---

### Slide 40

**Extreme Values for Functions of Several Variables**

**Theorem (Second Derivative Test for Local Extreme Values)**
*Suppose that $f(x, y)$ and its first and second partial derivatives are continuous throughout a disk centered at $(a, b)$ and that $f'_x(a, b) = f'_y(a, b) = 0$. Then*
1. *$f$ has a **local maximum** at $(a, b)$ if $f''_{xx}f''_{yy} - f''^2_{xy} > 0$ and $f''_{xx} < 0$ at $(a, b)$.*
2. *$f$ has a **local minimum** at $(a, b)$ if $f''_{xx}f''_{yy} - f''^2_{xy} > 0$ and $f''_{xx} > 0$ at $(a, b)$.*
3. *$f$ has a **saddle point** at $(a, b)$ if $f''_{xx}f''_{yy} - f''^2_{xy} < 0$ at $(a, b)$.*
4. ***The test is inconclusive** at $(a, b)$ if $f''_{xx}f''_{yy} - f''^2_{xy} = 0$ at $(a, b)$.*
   *\color{blue}{In this case, we must find some other way to determine the behavior of $f$ at $(a, b)$.}*

**Remark.** The expression $\Delta(x, y) := f''_{xx}f''_{yy} - f''^2_{xy} > 0$ is called the **discriminant** or **Hessian** of $f$. The Hessian matrix is $H = \begin{pmatrix} f''_{xx} & f''_{xy} \\ f''_{yx} & f''_{yy} \end{pmatrix}$ and $\Delta(x, y) = \det(H) = \begin{vmatrix} f''_{xx} & f''_{xy} \\ f''_{yx} & f''_{yy} \end{vmatrix}$.

**Example 1.** In the previous slide, it was shown that the critical points of the function $f(x, y) = 2x^3 - 3x^2 - 2y^3 + 3y^2$ are $(0, 0), (1, 1), (1, 0)$ and $(0, 1)$. By the Second Derivative Test, we can classify these points and find that $f$ has a local maximum at $(0, 1)$, local minimum at $(1, 0)$, and two saddle points at $(0, 0), (1, 1)$. See the figure in the next slide.

---

### Slide 41

**Extreme Values for Functions of Several Variables**

> 🖼️ **Image Description:** A 3D plot of the function $f(x, y) = 2x^3 - 3x^2 - 2y^3 + 3y^2$ (a red continuous surface). The surface has peaks, valleys, and saddle passes. Four critical points are marked with colored dots, and a legend on the left correlates them to their coordinates:
> *   Red dot: Top of a peak representing $(0, 1, f(0, 1))$, a local maximum.
> *   Blue dot: A saddle point at $(0, 0, f(0, 0))$.
> *   Green dot: Another saddle point at $(1, 1, f(1, 1))$.
> *   Orange dot: Bottom of a valley representing $(1, 0, f(1, 0))$, a local minimum.

**<span style="color:red">Exercise.</span>** <span style="color:red">Find and classify the critical points of the functions.</span>
1. <span style="color:green">$f(x, y) = x^2 - y^3 - 3xy + 2x;$</span>
2. <span style="color:green">$f(x, y) = 2x^3 + 2y^3 - 9x^2 + 3y^2 - 12y;$</span>
3. <span style="color:green">$f(x, y) = 10xye^{-(x^2+y^2)}.$</span>

---

### Slide 42

**Minimization Problem: Gradient Descent Method.**

In mathematics and machine learning, we often want to minimize a **cost function**, which is a function that tells us how "bad" our current model is.
Let us consider the following (unconstrained) optimization problem
$$ \min_{x \in \mathbb{R}^n} f(x), \quad \text{where } f : \mathbb{R}^n \to \mathbb{R} \text{ is a differentiable function.} \quad (2) $$

In general, to solve such a problem, there are many challenges: the dimension $n$ is very big, the structure of the objective function $f$ is complicated (non-convex, for example, thus there are many extrema). In most cases, the problem cannot be solved analytically. Therefore, we use numerical algorithms to find an approximate solution with the required accuracy. The **gradient descent method (GD)** is one of main algorithms used to solve such problems. <span style="color:red">You will take an entire course dedicated to optimization methods.</span>
The iteration process of this algorithm is simple and has the following form
$$ x^{k+1} = x^k - \alpha \nabla f(x^k), \quad k = 0, 1, 2, \dots $$
with $x^0$ is a chosen initial point.
* The parameter $\alpha \in \mathbb{R}$ called **Learning Rate** or **Step Size**. When it is too large, then the algorithm may diverge. If it is too small, then the algorithm will slowly converge. There are adaptive methods that adjust $\alpha$ dynamically.
* **Stopping Criteria:** $||\nabla f(x^k)||_2 \le \varepsilon$ (Gradient magnitude small), $||x^{k+1} - x^k||_2 \le \varepsilon$ (Change in $x$ small), max iterations reached. There are also many other criteria.

---

### Slide 43

**Minimization Problem: Gradient Descent Method.**

**Example: Quadratic Function.**
Let us consider a **convex** quadratic function $f(x) = \frac{1}{2} x^\top Ax - b^\top x$, where $A \in \mathbb{R}^{n \times n}$ is a symmetric positive definite matrix, $b \in \mathbb{R}^n$ is a vector.
For this function we have $\nabla f(x) = Ax - b$. By setting $\nabla f(x) = \mathbf{0}$, we find that the minimum occurs at: $x_* = A^{-1}b$ (that is a solution of a system of $n$ linear equations), that is we solved the problem analytically!

**Example in 2D.** Let $A = \begin{pmatrix} 4 & 1 \\ 1 & 3 \end{pmatrix}, b = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$. Then, we get the function
$$ f(x_1, x_2) = \frac{1}{2} \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} 4 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} - \begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 2x_1^2 + x_1x_2 + \frac{3}{2}x_2^2 - x_1 - 2x_2. $$

For this function, we have
$$ x_* = A^{-1}b = \frac{1}{11} \begin{pmatrix} 1 \\ 7 \end{pmatrix} \approx \begin{pmatrix} 0.0909 \\ 0.6364 \end{pmatrix}, \quad f(x_*) = -\frac{15}{22} \approx -0.6818. $$

To find $x_*$, by using the Gradient Descent Method, we have the following results.

---

### Slide 44

**The Results of Gradient Descent Method for 2D Example (1/2)**

> 🖼️ **Image Description:** Two side-by-side line graphs showing the convergence of Gradient Descent.
> *   **Left Graph:** Titled "Function Value with step size = 0.1". The x-axis is "Iteration $k$" (0 to 50) and the y-axis is $f(x^k)$ (from 0.0 down to -0.7). The solid blue curve drops steeply from 0.0 and flattens out. A red dashed horizontal line marks the true minimum "Min = -0.6818". The blue curve perfectly converges to this red dashed line by roughly iteration 10.
> *   **Right Graph:** Titled "Norm gradient with step size = 0.1". The x-axis is "Iteration $k$" (0 to 50) and the y-axis is $||\nabla f(x^k)||_2$ (from 2.0 down to 0.0). A solid green curve starts high and decays exponentially to 0, indicating the gradient magnitude approaches zero as the minimum is reached.

<span style="color:green">Figure:</span> The Results of the Gradient Descent Method for the previously mentioned 2D Example.

---

### Slide 45

**The Results of Gradient Descent Method for 2D Example (2/2)**

> 🖼️ **Image Description:** Two side-by-side line graphs comparing the performance of Gradient Descent across multiple learning rates ($\alpha$ values: 0.01, 0.05, 0.1, 0.15, 0.2).
> *   **Left Graph:** "Function Value with different step sizes". The x-axis is "Iteration $k$" (0 to 50) and the y-axis is $f(x^k)$. The plot contains five colored curves. The red curve ($\alpha=0.01$) converges very slowly, barely reaching -0.65 by iteration 50. The blue curve ($\alpha=0.05$) is faster. The green ($\alpha=0.1$), orange ($\alpha=0.15$), and cyan ($\alpha=0.2$) curves drop very sharply, practically hitting the minimum by iteration 10-15.
> *   **Right Graph:** "Norm gradient Value with different step sizes". Similar behavior is shown for the gradient norm $||\nabla f(x^k)||_2$ decaying to 0. The red line decreases slowest, while the cyan line plummets the fastest.

<span style="color:green">Figure:</span> The Results of the Gradient Descent Method for the previously mentioned 2D Example.




Here is the complete line-by-line transcription for the remaining slides (Slide 46 to 74), continuing with the same formatting, mathematical notation, and detailed image descriptions.

***

### Slide 46

**Minimization Problem: Gradient Descent Method.**

**Example in 4D.**
Let $A = \begin{pmatrix} 5 & 1 & 0 & 0 \\ 1 & 4 & 1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 \end{pmatrix}, \ b = \begin{pmatrix} 1 \\ 0 \\ -1 \\ 2 \end{pmatrix}$. Then, we get the function
$$ f(x_1, x_2, x_3, x_4) = \frac{1}{2} \begin{pmatrix} x_1 & x_2 & x_3 & x_4 \end{pmatrix} \begin{pmatrix} 5 & 1 & 0 & 0 \\ 1 & 4 & 1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} - \begin{pmatrix} 1 \\ 0 \\ -1 \\ 2 \end{pmatrix}^\top \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} $$

For this function, we have
$$ \nabla f(x) = Ax - b = \mathbf{0} \implies \begin{cases} 5x_1 + x_2 = 1, \\ x_1 + 4x_2 + x_3 = 0, \\ x_2 + 3x_3 + x_4 = -1, \\ x_3 + 2x_4 = 2. \end{cases} \implies x_* \approx \begin{pmatrix} 0.16470588 \\ 0.17647059 \\ -0.87058824 \\ 1.43529412 \end{pmatrix}. $$

Also, $f(x_*) \approx -1.9529$.
To find $x_*$, by using the Gradient Descent Method, we have the following results.

---

### Slide 47

**The Results of Gradient Descent Method for 4D Example (1/2)**

> 🖼️ **Image Description:** Two side-by-side line graphs showing the convergence of the Gradient Descent method for a step size of 0.05.
> *   **Left Graph:** "Function Value with step size = 0.05". The x-axis is "Iteration $k$" (0 to 100) and the y-axis is $f(x^k)$ (from 0.00 down to -2.00). A solid blue line drops steeply from 0.00 and asymptotically flattens out around iteration 40. A red dashed horizontal line denotes the true minimum at "Min = -1.9529". The blue line converges exactly onto the red dashed line.
> *   **Right Graph:** "Norm gradient with step size = 0.05". The x-axis is "Iteration $k$" (0 to 100) and the y-axis is $||\nabla f(x^k)||_2$ (from 2.5 down to 0.0). A green solid curve starts high and decays exponentially to 0, showing that the gradient approaches zero as the algorithm finds the minimum.

<span style="color:green">Figure:</span> The Results of the Gradient Descent Method for the previously mentioned 4D Example.

---

### Slide 48

**The Results of Gradient Descent Method for 4D Example (2/2)**

> 🖼️ **Image Description:** Two side-by-side line graphs comparing the performance of Gradient Descent across multiple learning rates ($\alpha$ values: 0.01, 0.05, 0.1, 0.15, 0.2) over 100 iterations.
> *   **Left Graph:** "Function Value with different step sizes". The red curve ($\alpha=0.01$) converges very slowly and hasn't reached the minimum by iteration 100. The blue curve ($\alpha=0.05$) reaches the minimum around iteration 40. The green, orange, and cyan curves ($\alpha=0.1, 0.15, 0.2$ respectively) drop incredibly fast, reaching the minimum in less than 20 iterations.
> *   **Right Graph:** "Norm gradient Value with different step sizes". The gradient norm exponentially decays to zero for all step sizes, with $\alpha=0.01$ (red) being the slowest to decay and $\alpha=0.2$ (cyan) decaying to zero almost immediately.

<span style="color:green">Figure:</span> The Results of the Gradient Descent Method for the previously mentioned 4D Example.

---

### Slide 49

**Minimization Problem: Gradient Descent Method.**

**Remark.** <span style="color:red">In the non-convex case, the convergence of the Gradient Descent Method cannot be guaranteed even to a local minimum.</span> Let us consider the following function
$$ f(x) = f(x_1, x_2) = \frac{1}{2}x_1^2 + \frac{1}{4}x_2^4 - \frac{1}{2}x_2^2. \qquad (3) $$

For this function, there are three critical points: $(0, 0), (0, -1), (0, 1)$.

The points $(0, -1)$ and $(0, 1)$ are local minima, and $(0, 0)$ is a saddle point. Consider the trajectory of the gradient method starting at the point $x^0 = (1, 0)$. Note that the second coordinate of this point is 0, so the second coordinate for $\nabla f(x^0)$ is also 0. Consequently, the second coordinate of the next generated point $x^1$ by the method is equal to zero, etc. Thus, the entire sequence of points formed by the gradient method will have a zero second coordinate, which means that it converges to the saddle point $(0, 0)$.

> 🖼️ **Image Description:** A 3D plot showing a smooth, solid blue non-convex surface (shaped somewhat like a curved valley with a bump in the middle). Three distinct points are marked with colored dots on the bottom contours of the surface.
> *   An orange dot is centrally located on the small dividing ridge (the saddle point at $(0,0, f(0,0))$).
> *   A green dot marks the bottom of the right-side trough (local minimum at $(0,1, f(0,1))$).
> *   A red dot marks the bottom of the left-side trough (local minimum at $(0,-1, f(0,-1))$).

<span style="color:green">Figure:</span> The graph of the function (3), with three points $(0, 0, f(0, 0))$ in orange, $(0, 1, f(0, 1))$ in green, and $(0, -1, f(0, -1))$ in red.

---

### Slide 50

**Constrained Maxima and Minima**

Sometimes we need to find the extreme values of a function whose domain is constrained to lie within some particular subset, for example, a ball, polyhedron or along a curve.
We first consider a problem where a constrained minimum can be found by eliminating a variable.

**Example.**
Find the point $P(x, y, z)$ on the plane $2x + y - z - 5 = 0$ that is closest to the origin.
**Solution.**
The problem states to find a point that gives the minimum value of the function
$$ |\overrightarrow{OP}| = \sqrt{x^2 + y^2 + z^2} \quad \text{subjet to the constraint} \quad 2x + y - z - 5 = 0. $$
Note that
$$ \arg\min \left(\sqrt{x^2 + y^2 + z^2}\right) = \arg\min \left(x^2 + y^2 + z^2\right). $$
Thus, to avoid square roots, we will solve the problem
$$ \min \Big\{ f(x, y, z) := x^2 + y^2 + z^2, \quad \text{s.t.} \quad 2x + y - z - 5 = 0 \Big\}. $$
From the constraint, we find $z = 2x + y - 5$, and our problem reduces to solving the following problem
$$ \min_{(x,y) \in \mathbb{R}^2} \Big\{ h(x, y) = f(x, y, 2x + y - 5) = 5x^2 + 2y^2 + 4xy - 20x - 10y + 25 \Big\}. $$

---

### Slide 51

**Constrained Maxima and Minima**

For this, we set
$$ \nabla h(x, y) = \begin{pmatrix} 10x + 4y - 20 \\ 4x + 4y - 10 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x = \frac{5}{3}, \quad y = \frac{5}{6}. $$

Also, for any $(x, y) \in \mathbb{R}^2$, we have
$$ \Delta(x, y) := f''_{xx}f''_{yy} - (f''_{xy})^2 = 40 - 16 = 24 > 0, \quad \text{and} \quad f''_{xx} = 10 > 0. $$

Thus, the minimal value of the function $h(x, y)$ at the point $\left(\frac{5}{3}, \frac{5}{6}\right)$. The $z$-coordinate of the corresponding point on the plane $z = 2x + y - 5$ is $z = -\frac{5}{6}$. Therefore, the point we seek is
$$ \text{Closest point: } P\left(\frac{5}{3}, \frac{5}{6}, -\frac{5}{6}\right). $$
The distance from $P$ to the origin is $\frac{5}{\sqrt{6}} \approx 2.04$.

Attempts to solve a constrained maximum or minimum problem by substitution, as in the previous example, do not always go smoothly. Therefore, in the next we explore a powerful method for finding extreme values of constrained functions: method of **Lagrange multipliers**.

---

### Slide 52

**Constrained Maxima and Minima: Lagrange Multipliers**

method of **Lagrange multipliers** says that <span style="color:red">the local extreme values of a function $f(\mathbf{x})$, $\mathbf{x} \in \mathbb{R}^n$, whose variables are subject to a constraint $g(\mathbf{x}) = 0$ are to be found on the surface $g = 0$ among the points where $\nabla f = \lambda \nabla g$ for some scalar $\lambda$ (called a **Lagrange multiplier**).</span>

Note that in the previous example, for the function $f(x, y, z) = x^2 + y^2 + z^2$, and $g(x, y, z) = 2x + y - z - 5 = 0$, at the point $P\left(\frac{5}{3}, \frac{5}{6}, -\frac{5}{6}\right)$, we have
$$ \nabla f(P) = \begin{pmatrix} \frac{10}{3} & \frac{5}{3} & -\frac{5}{3} \end{pmatrix}^\top, \ \nabla g(P) = \begin{pmatrix} 2 & 1 & -1 \end{pmatrix}^\top \implies \nabla f(P) = \frac{5}{3}\nabla g(P), \lambda = \frac{5}{3}. $$

Let us first mention the following theorem, stated here in $\mathbb{R}^3$ for simplicity, though it holds in the general $\mathbb{R}^n$ case as well.

**Theorem (Orthogonal Gradient Theorem)**
*Suppose that $f(x, y, z)$ is differentiable in a region whose interior contains a smooth curve*
$$ C: \quad \mathbf{r}(t) = x(t)\hat{\mathbf{i}} + y(t)\hat{\mathbf{j}} + z(t)\hat{\mathbf{k}}, \quad t \in \mathbb{R}. $$
*If $P_0$ is a point on $C$ where $f$ has a local maximum or minimum relative to its values on $C$, then $\nabla f$ is orthogonal to the curve's tangent vector $\mathbf{r}'$ at $P_0$.*

---

### Slide 53

**Constrained Maxima and Minima: Lagrange Multipliers**

**Proof.**
The values of $f$ on $C$ are given by the composition $f(x(t), y(t), z(t))$, whose derivative with respect to $t$ is
$$ \frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \frac{\partial f}{\partial z}\frac{dz}{dt} = \nabla f \cdot \mathbf{r}'(t). $$
At any point $P_0(x(t_0), y(t_0), z(t_0))$ where $f$ has a local maximum or minimum relative to its values on the curve, $\frac{df}{dt} = 0$, so $\nabla f(P_0) \cdot \mathbf{r}'(t_0) = 0$. $\square$

This theorem is essential to the method of Lagrange multipliers, as we can see from the following argument:
Suppose that $f(\mathbf{x})$ and $g(\mathbf{x})$ are differentiable functions and that $\mathbf{x}_0$ is a point on the rsurface $g(\mathbf{x}) = 0$ where $f$ has a local maximum or minimum value relative to its other values on the surface. We assume also that $\nabla g \neq \mathbf{0}$ at points on the surface $g(\mathbf{x}) = 0$. Then $f$ takes on a local maximum or minimum at $\mathbf{x}_0$ relative to its values on every differentiable curve through $\mathbf{x}_0$ on the surface $g(\mathbf{x}) = 0$. Therefore, $\nabla f$ is orthogonal to the tangent vector of every such differentiable curve through $\mathbf{x}_0$. Moreover, so is $\nabla g$ (because $\nabla g$ is perpendicular to the level surface $g(\mathbf{x}) = 0$. Hence, at the point $\mathbf{x}_0$, $\nabla f, \nabla g$ are parallel, that is $\nabla f(\mathbf{x}_0) = \lambda\nabla g(\mathbf{x}_0)$ for some $\lambda \in \mathbb{R}^*$.

---

### Slide 54

**Constrained Maxima and Minima: Lagrange Multipliers**

Therefore, we can formulate the following result.

**Theorem**
*Let $\mathbf{x}_0 \in G \subseteq \mathbb{R}^n$ be a regular point for $g$ (that is $\nabla g(\mathbf{x}_0) \neq \mathbf{0}$). If $\mathbf{x}_0$ is an extremum for $f$ constrained to $G$, there exists a unique constant $\lambda_0 \in \mathbb{R}$, called **Lagrange multiplier**, such that*
$$ \nabla f(\mathbf{x}_0) = \lambda_0\nabla g(\mathbf{x}_0). $$

> 🖼️ **Image Description:** A geometric illustration of Lagrange Multipliers. The blue curve $G$ represents the constraint $g(\mathbf{x}) = c$. Faint grey curves represent the level sets of the objective function $f$. At a specific point $\mathbf{x}_0$ where the blue curve $G$ is exactly tangent to one of the grey level curves of $f$, two vectors are drawn starting from $\mathbf{x}_0$: $\nabla f$ points outwards orthogonally to the level set of $f$, and $\nabla g$ points outwards orthogonally to the constraint curve $G$. Because the curves are tangent at $\mathbf{x}_0$, the two gradient vectors $\nabla f$ and $\nabla g$ are perfectly parallel.

<span style="color:green">Figure:</span> At a constrained extremum the gradients of $f$ and $g$ are parallel.

---

### Slide 55

**Constrained Maxima and Minima: Lagrange Multipliers**

There is an equivalent formulation for the previous theorem, that associates to $\mathbf{x}_0$ an unconstrained stationary point relative to a new function depending on $f$ and $g$.

**Definition (The Lagrangian in the case of one equality constraint)**
Let $f$ and $g$ be differentiable function. Set $\Omega = \text{dom } f \cap \text{dom } g \subseteq \mathbb{R}^n$. The function $\mathcal{L} : \Omega \times \mathbb{R} \to \mathbb{R}$ defined by
$$ \mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda g(\mathbf{x}) $$
is called **Lagrangian (function)** of $f$ **constrained to** $g$.

The gradient of $\mathcal{L}$ looks as follows
$$ \nabla_{(\mathbf{x},\lambda)}\mathcal{L}(\mathbf{x}, \lambda) = \begin{pmatrix} \nabla_{\mathbf{x}}\mathcal{L}(\mathbf{x}, \lambda) \\ \frac{\partial \mathcal{L}}{\partial \lambda} (\mathbf{x}, \lambda) \end{pmatrix}^\top = \begin{pmatrix} \nabla f(\mathbf{x}) - \lambda\nabla g(\mathbf{x}) & g(\mathbf{x}) \end{pmatrix}^\top. $$

Hence the condition $\nabla_{(\mathbf{x},\lambda)}\mathcal{L}(\mathbf{x}_0, \lambda_0) = \mathbf{0}$, expressing that $(\mathbf{x}_0, \lambda_0)$ is stationary for $\mathcal{L}$, is equivalent to the system
$$ \begin{cases} \nabla f(\mathbf{x}_0) = \lambda\nabla g(\mathbf{x}_0), \\ g(\mathbf{x}_0) = 0. \end{cases} $$

---

### Slide 56

**Constrained Maxima and Minima: Lagrange Multipliers**

<span style="color:red">Thus to find the local maximum and minimum values of the function $f(\mathbf{x})$ subject to $g(\mathbf{x})$ (if they exist), we write the system of $n + 1$ equations in $n + 1$ unknowns $\mathbf{x} = (x_1, \dots, x_n)$ and $\lambda$,</span>
$$ \color{red}{\begin{cases} \nabla f(\mathbf{x}) = \lambda_0\nabla g(\mathbf{x}), \\ g(\mathbf{x}) = 0. \end{cases}} $$

**Example 1.**
Find the largest and smallest values that the function $f(x, y) = xy$ takes on the ellipse $\frac{x^2}{8} + \frac{y^2}{2} = 1$.
**Solution.** Define $g(x, y) = \frac{x^2}{8} + \frac{y^2}{2} - 1$. The Lagrangian function is
$$ \mathcal{L}(x, y, \lambda) = f(x, y) - \lambda g(x, y) = xy - \lambda \left( \frac{x^2}{8} + \frac{y^2}{2} - 1 \right). $$
Thus,
$$ \nabla \mathcal{L}(x, y, \lambda) = \begin{pmatrix} y - \frac{\lambda}{4}x \\ x - \lambda y \\ \frac{x^2}{8} + \frac{y^2}{2} - 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \implies \begin{cases} y - \frac{\lambda}{4}x = 0, & (1) \\ x - \lambda y = 0, & (2) \\ \frac{x^2}{8} + \frac{y^2}{2} - 1 = 0. & (3) \end{cases} $$

---

### Slide 57

**Constrained Maxima and Minima: Lagrange Multipliers**

From the equation (1) and (2), we get $y = 0$ or $\lambda = \pm 2$.
We now consider these two cases.
**Case 1:** If $y = 0$, then $x = y = 0$. But $(0, 0)$ is not on the ellipse. Hence, $y \neq 0$.
**Case 2:** If $y \neq 0$, then $\lambda = \pm 2$ and $x = \pm 2y$. Substituting this in the equation (3) gives $y = \pm 1$.

Therefore, the function $f(x, y) = xy$ has critical points on the ellipse at the four points $(\pm 2, 1)$, $(\pm 2, -1)$.
The absolute maximum is
$$ f(2, 1) = f(-2, -1) = 2, $$
and the absolute minimum is
$$ f(-2, 1) = f(2, -1) = -2. $$

> 🖼️ **Image Description:** A 2D graph demonstrating Lagrange Multipliers. A blue ellipse represents the constraint curve $\frac{x^2}{8} + \frac{y^2}{2} = 1$. Several grey hyperbola branches represent the level curves of the objective function $f(x,y)=xy$, labeled $xy=2$, $xy=-2$, etc. At the four points where the hyperbola branches are perfectly tangent to the ellipse (the critical points), gradient vectors are drawn. A red vector labeled $\nabla f = \mathbf{i} + 2\mathbf{j}$ points outward from the tangency point in the first quadrant. A parallel cyan vector labeled $\nabla g = \frac{1}{2}\mathbf{i} + \mathbf{j}$ points in the exact same direction, visually confirming $\nabla f = \lambda \nabla g$.

Here is the complete line-by-line transcript of the presentation starting from slide 58, formatted simply and safely to ensure it displays correctly without errors. Image descriptions are included where applicable.

***

### Slide 58

**Constrained Maxima and Minima: Lagrange Multipliers**

**Example 2.**
Find the point on the manifold $x^4 + y^4 + z^4 = 1$ that is closest and is farthest to the origin.

**Solution.**
Define $g(\mathbf{x}) = g(x, y, z) = x^4 + y^4 + z^4 - 1$. The problem is finding

$\min_{(x,y,z) \in G} (\text{or} \max) \{f(x, y, z) = ||\mathbf{x}||^2 = x^2 + y^2 + z^2\}$ s.t. $G = \{(x, y, z) | g(x, y, z) = 0\}$.

The Lagrangian function is
$\mathcal{L}(x, y, z, \lambda) = f(x, y, z) - \lambda g(x, y, z) = x^2 + y^2 + z^2 - \lambda(x^4 + y^4 + z^4 - 1)$.

Thus,
$\nabla\mathcal{L}(x, y, z, \lambda) = [2x - 4\lambda x^3, 2y - 4\lambda y^3, 2z - 4\lambda z^3, x^4 + y^4 + z^4 - 1]^T = [0, 0, 0, 0]^T$
$\implies$
$x = 2\lambda x^3$, (1)
$y = 2\lambda y^3$, (2)
$z = 2\lambda z^3$, (3)
$x^4 + y^4 + z^4 - 1 = 0$. (4)

As $f$ is invariant under sign change in its arguments, $f(\pm x, \pm y, \pm z) = f(x, y, z)$, and similarly for $g$, we can just look for solutions belonging in the first octant ($x \ge 0, y \ge 0, z \ge 0$).

***

### Slide 59

**Constrained Maxima and Minima: Lagrange Multipliers**

From equations (1), (2) and (3), with $\lambda > 0$, we find

$x = 0$ or $x = \frac{1}{\sqrt{2\lambda}}$, $y = 0$ or $y = \frac{1}{\sqrt{2\lambda}}$, $z = 0$ or $z = \frac{1}{\sqrt{2\lambda}}$,

combined in all possible ways.

*   The point $(x, y, z) = (0, 0, 0)$ is to be excluded because it fails to satisfy the last equation (4).
*   The choices $(\frac{1}{\sqrt{2\lambda}}, 0, 0)$, $(0, \frac{1}{\sqrt{2\lambda}}, 0)$ or $(0, 0, \frac{1}{\sqrt{2\lambda}})$ in equation (4) give $\lambda = \frac{1}{2}$.
*   Similarly, $(x, y, z) = (\frac{1}{\sqrt{2\lambda}}, \frac{1}{\sqrt{2\lambda}}, 0)$, $(\frac{1}{\sqrt{2\lambda}}, 0, \frac{1}{\sqrt{2\lambda}})$ or $(0, \frac{1}{\sqrt{2\lambda}}, \frac{1}{\sqrt{2\lambda}})$ satisfy the fourth equation if $\lambda = \frac{1}{\sqrt{2}}$, while $(\frac{1}{\sqrt{2\lambda}}, \frac{1}{\sqrt{2\lambda}}, \frac{1}{\sqrt{2\lambda}})$ fulfills it if $\lambda = \frac{\sqrt{3}}{2}$.

The solutions then are:

$\mathbf{x}_1 = (1, 0, 0), f(\mathbf{x}_1) = 1; \quad \mathbf{x}_2 = (0, 1, 0), f(\mathbf{x}_2) = 1; \quad \mathbf{x}_3 = (0, 0, 1), f(\mathbf{x}_3) = 1;$

$\mathbf{x}_4 = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0), f(\mathbf{x}_4) = \sqrt{2}; \quad \mathbf{x}_5 = (\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}}), f(\mathbf{x}_5) = \sqrt{2};$

$\mathbf{x}_6 = (0, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}), f(\mathbf{x}_6) = \sqrt{2}; \quad \mathbf{x}_7 = (\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}), f(\mathbf{x}_7) = \sqrt{3}.$

***

### Slide 60

**Constrained Maxima and Minima: Lagrange Multipliers**

In conclusion, the first octant contains 3 points of $G$, $\mathbf{x}_1$, $\mathbf{x}_2$, $\mathbf{x}_3$, with the shortest distance to the origin, and 1 farthest point $\mathbf{x}_7$. The distance function on $G$ has stationary points $\mathbf{x}_4$, $\mathbf{x}_5$, $\mathbf{x}_6$, but no minimum nor maximum.

*[Image Description: A 3D plot showing a smooth, curved surface patch (a portion of the manifold $x^4 + y^4 + z^4 = 1$ restricted to the first octant), colored in a translucent light blue gradient. The axes are labeled $x, y, z$. Several specific points are marked on this surface: $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3$ lie exactly on the intersections of the surface with the $x, y,$ and $z$ axes respectively. $\mathbf{x}_4, \mathbf{x}_5, \mathbf{x}_6$ lie on the boundary curves connecting the axes. $\mathbf{x}_7$ lies in the center of the surface patch.]*

Figure: The graph of the feasible (admissible) set $G$ (first octant only) and the stationary points of $f$ on $G$.

***

### Slide 61

**Constrained Maxima and Minima: Lagrange Multipliers**

**Lagrange Multipliers for the case with multiple equality constraints.**
Let us consider the problem

$\min_{\mathbf{x} \in G} (\text{or} \max) f(\mathbf{x})$

where the feasible set $G$ defined by $m < n$ equalities of the type

$g_1(\mathbf{x}) = 0, \quad g_2(\mathbf{x}) = 0, \quad \dots, \quad g_m(\mathbf{x}) = 0.$

If $\mathbf{x}_0 \in G$ is a constrained extremum for $f$ on $G$ and regular for each $g_i$ (that is $\nabla g_i(\mathbf{x}_0) \neq \mathbf{0}$), then there exist $m$ Lagrange multipliers $\lambda_1, \lambda_2, \dots, \lambda_m$, and Lagrangian is

$\mathcal{L}(\mathbf{x}, \lambda_1, \lambda_2, \dots, \lambda_m) := f(\mathbf{x}) - \sum_{i=1}^m \lambda_i g_i(\mathbf{x}) \quad \forall \mathbf{x} = (x_1, \dots, x_n) \in G.$

To find the stationary points, we write the system of $n + m$ equations with $n + m$ unknowns $x_1, \dots, x_n, \lambda_1, \dots, \lambda_m$,

$\begin{cases} \nabla f(\mathbf{x}) = \sum_{i=1}^m \lambda_i \nabla g(\mathbf{x}), \\ g_i(\mathbf{x}) = 0 \quad i = 1, 2, \dots, m. \end{cases}$

We will explain this method in the following examples.

***

### Slide 62

**Constrained Maxima and Minima: Lagrange Multipliers**

**Example 1.**
The plane $x + y + z = 1$ cuts the cylinder $x^2 + y^2 = 1$ in an ellipse. Find the points on the ellipse that lie **closest** to and **farthest** from the origin.

*[Image Description: A 3D illustration showing a vertical semi-transparent orange cylinder with the equation $x^2 + y^2 = 1$. A tilted, semi-transparent light blue plane with the equation $x + y + z = 1$ slices diagonally through the cylinder. The intersection of the plane and the cylinder forms an ellipse, outlined in bright blue. Two distinct points are highlighted on this ellipse: $P_1$ (marked in blue, located at the lower front part of the ellipse) and $P_2$ (marked in red, located at the higher back part of the ellipse). Coordinate points $(1, 0, 0)$ and $(0, 1, 0)$ are marked with black dots where the ellipse crosses the horizontal axes. The $x, y, z$ axes are clearly shown.]*

***

### Slide 63

**Constrained Maxima and Minima: Lagrange Multipliers**

**Solution.**
The objective function is $f(x, y, z) = x^2 + y^2 + z^2$, and the constraints are

$g_1(x, y, z) = x + y + z - 1 = 0, \quad g_2(x, y, z) = x^2 + y^2 - 1 = 0.$

The Lagrangian is

$\mathcal{L}(x, y, z, \lambda_1, \lambda_2) = f(x, y, z) - \lambda_1 g_1(x, y, z) - \lambda_2 g_2(x, y, z)$
$= x^2 + y^2 + z^2 - \lambda_1(x + y + z - 1) - \lambda_2(x^2 + y^2 - 1).$

Thus,

$\nabla\mathcal{L} = [2x - \lambda_1 - 2\lambda_2 x, 2y - \lambda_1 - 2\lambda_2 y, 2z - \lambda_1, -(x + y + z - 1), -(x^2 + y^2 - 1)]^T = [0, 0, 0, 0, 0]^T$
$\implies$
$2x = 2\lambda_2 x + \lambda_1,$ (1)
$2y = 2\lambda_2 y + \lambda_1,$ (2)
$2z = \lambda_1,$ (3)
$x + y + z = 1,$ (4)
$x^2 + y^2 = 1.$ (5)

From the first three equations, we find $(1 - \lambda_2)x = z$, $(1 - \lambda_2)y = z$. These equations are satisfied simultaneously if either $\lambda_2 = 1$ and $z = 0$ or $\lambda_2 \neq 1$ and $x = y = z/(1 - \lambda_2)$.

***

### Slide 64

**Constrained Maxima and Minima: Lagrange Multipliers**

In the first case, where $z = 0$, solving Equations (4) and (5) simultaneously to find the corresponding points on the ellipse gives the two points $(1, 0, 0)$ and $(0, 1, 0)$.
In the second case, where $x = y$, Equations (4) and (5) give

$2x^2 - 1 = 0 \quad \text{and} \quad 2x + z - 1 = 0 \implies x = \pm \frac{1}{\sqrt{2}} \quad \text{and} \quad z = 1 \mp \sqrt{2}.$

The corresponding points on the ellipse are

$P_1 = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 1 - \sqrt{2}) \quad \text{and} \quad P_2 = (-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 1 + \sqrt{2}).$

At critical points $(1, 0, 0)$, $(0, 1, 0)$, $P_1$, and $P_2$ we have

$f_{\min} = f(1, 0, 0) = f(0, 1, 0) = 1, \quad f(P_1) = 4 - 2\sqrt{2}, \quad \text{and} \quad f_{\max} = f(P_2) = 4 + 2\sqrt{2}.$

The value $f(P_1) = 4 - 2\sqrt{2}$ is neither the largest nor the smallest among the values of $f$ at the critical points, so $f$ does not have an absolute extremum at $P_1$.
The points on the ellipse closest to the origin are $(1, 0, 0)$ and $(0, 1, 0)$. The point on the ellipse farthest from the origin is $P_2$.

***

### Slide 65

**Constrained Maxima and Minima: Lagrange Multipliers**

**Example 2.** Find the extrema points of $f(x, y, z) = 3x + 3y + 8z$ constrained to the intersection of two cylinders, $x^2 + z^2 = 1$ and $y^2 + z^2 = 1$.

**Solution.** Define $g_1(x, y, z) = x^2 + z^2 - 1$, $g_2(x, y, z) = y^2 + z^2 - 1$. The Lagrangian is

$\mathcal{L}(x, y, z, \lambda_1, \lambda_2) = f(x, y, z) - \lambda_1 g_1(x, y, z) - \lambda_2 g_2(x, y, z)$
$= 3x + 3y + 8z - \lambda_1(x^2 + z^2 - 1) - \lambda_2(y^2 + z^2 - 1).$

Thus,

$\nabla\mathcal{L} = [3 - 2\lambda_1 x, 3 - 2\lambda_2 y, 8 - 2\lambda_1 z - 2\lambda_2 z, -(x^2 + z^2 - 1), -(y^2 + z^2 - 1)]^T = \mathbf{0}$
$\implies$
$3 = 2\lambda_1 x,$
$3 = 2\lambda_2 y,$
$8 = 2(\lambda_1 + \lambda_2)z,$
$x^2 + z^2 - 1 = 0,$
$y^2 + z^2 - 1 = 0.$

From the first three equations, we find $x = \frac{3}{2\lambda_1}$, $y = \frac{3}{2\lambda_2}$, $z = \frac{4}{\lambda_1 + \lambda_2}$, (with $\lambda_1 \neq 0, \lambda_2 \neq 0, \lambda_1 + \lambda_2 \neq 0$), so the remaining equations give $\lambda_1 = \lambda_2 = \pm\frac{5}{2}$.
Therefore, the extrema points are $P_1(\frac{3}{5}, \frac{3}{5}, \frac{4}{5})$ and $P_2(-\frac{3}{5}, -\frac{3}{5}, -\frac{4}{5})$, and we find

$f_{\max} = f(P_1) = 10, \quad f_{\min} = f(P_2) = -10.$

***

### Slide 66

**Constrained Maxima and Minima: Linear Programming Problem**

In general, we can solve the optimization problems in which the feasible set is defined by **inequalities** not only equalities. For example,
consider $f(x, y) = x + 2y$ on the set $G$ defined by the inequalities

$\begin{cases} x + 2y + 8 \ge 0, \\ 5x + y + 13 \ge 0, \\ x - 4y + 11 \ge 0, \\ 2x + y - 5 \le 0, \\ 5x - 2y - 8 \le 0. \end{cases}$

*[Image Description: A 2-dimensional coordinate graph plotting the $x$ and $y$ axes. Five grey lines intersect to form an enclosed, light blue shaded pentagonal region labeled $G$. The five vertices of this pentagon are clearly marked with points $A, B, C, D,$ and $E$.]*

The set $G$ is the pentagon having vertices (thus, it is irregular set) $A = (0, -4)$, $B = (-2, -3)$, $C = (-3, 2)$, $D = (1, 3)$, $E = (2, 1)$ and obtained as intersection of the five half-planes defined by the above inequalities.
The function $f$ attains minimum and maximum on the boundary of $G$; and since $f$ is linear on the perimeter, any extremum point must be a vertex. Thus it is enough to compare the values at the corners $\color{red}{f(A) = f(B) = -8}$, $f(C) = 1$, $\color{magenta}{f(D) = 7}$, $f(E) = 4$. $f$ restricted to $G$ is $\color{red}{\text{smallest at each point of } AB}$ and $\color{magenta}{\text{largest at } D}$. This problem is called **linear programming problem** is one of the parts of the mathematical optimization, which represents the core of AI and machine learning.

***

### Slide 67

**Constrained Maxima and Minima: Exercises**

**Exercise 1.** Find the points on the ellipse $x^2 + 2y^2 = 1$ where $f(x, y) = xy$ has its extreme values.
**Exercise 2.** Use the method of Lagrange multipliers to find
1.  **Minimum on a hyperbola.** The minimum value of $x + y$, subject to the constraints $xy = 16, x > 0, y > 0$.
2.  **Maximum on a line.** The maximum value of $xy$, subject to the constraint $x + y = 16$.

**Exercise 3. Extrema on a sphere.** Find the maximum and minimum values of $f(x, y, z) = x - 2y + 5z$ on the sphere $x^2 + y^2 + z^2 = 30$.
**Exercise 4.** Maximize the function $f(x, y, z) = x^2 + 2y - z^2$ subject to the constraints $2x - y = 0$ and $y + z = 0$.
**Exercise 5.** Find the extreme values of $f(x, y, z) = 2x^2 + yz$ on the intersection of the cylinder $x^2 + z^2 = 9$ and the plane $y - z = 4$.
**Exercise 6. Extrema on a curve of intersection.** Find the extreme values of $f(x, y, z) = x^2yz + 1$ on the intersection of the plane $z = 1$ with the sphere $x^2 + y^2 + z^2 = 10$.
**Exercise 6. Extrema on a circle of intersection.** Find the extreme values of the function $f(x, y, z) = xy + z^2$ on the circle in which the plane $y - x = 0$ intersects the sphere $x^2 + y^2 + z^2 = 4$.

***

### Slide 68

**Taylor’s Formula for Functions with Several Variables**

Let $f(x, y)$ have continuous first and second partial derivatives in an open region $R$ containing a point $P(a, b)$ where $f_x' = f_y' = 0$. Let $h$ and $k$ be increments small enough to put the point $S(a + h, b + k)$ and the line segment joining it to $P$ inside $R$. We parametrize the segment $PS$ as

$x = a + th, \quad y = b + tk, \quad 0 \le t \le 1.$

If $F(t) = f(a + th, b + tk)$, the Chain Rule gives

$F'(t) = f_x' \frac{dx}{dt} + f_y' \frac{dy}{dt} = h f_x' + k f_y'. \quad (4)$

*[Image Description: A diagram showing an open region $R$ shaded in light green. Inside the region, there is a blue line segment representing a parametrized path. The starting point is $P(a, b)$ at $t=0$ (red dot). A typical intermediate point on the segment is marked as $(a+th, b+tk)$ (red dot). The ending point of the segment is $S(a+h, b+k)$ at $t=1$ (red dot).]*

Since $f_x'$ and $f_y'$ are differentiable (because they have continuous partial derivatives), $F'$ is a differentiable function of $t$ and

$F''(t) = \frac{\partial F'}{\partial x}\frac{dx}{dt} + \frac{\partial F'}{\partial y}\frac{dy}{dt} = \frac{\partial}{\partial x}(h f_x + k f_y) \cdot h + \frac{\partial}{\partial y}(h f_x + k f_y) \cdot k$
$= h^2 f_{xx} + 2hk f_{xy} + k^2 f_{yy}. \quad (5)$

***

### Slide 69

**Taylor’s Formula for Functions with Two Variables**

The formulas (4) and (5), for $F'$ and $F''$, can be obtained by applying to $f(x, y)$ the differentiation operators

$(h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y})$ and $(h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y})^2 = h^2\frac{\partial^2}{\partial x^2} + 2hk\frac{\partial^2}{\partial x \partial y} + k^2\frac{\partial^2}{\partial y^2}.$

In more general, we have the following formula,

$F^{(n)}(t) = \frac{d^n}{dt^n} F(t) = (h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y})^n f(x, y), \quad (6)$

If the partial derivatives of $f$ through order $n + 1$ are continuous throughout a rectangular region centered at $(a, b)$, we may extend the Taylor formula for $F(t)$ to

$F(t) = F(0) + F'(0)t + \frac{F''(0)}{2!}t^2 + \dots + \frac{F^{(n)}(0)}{n!}t^{(n)} + \text{remainder},$

and take $t = 1$ to obtain

$F(1) = F(0) + F'(0) + \frac{F''(0)}{2!} + \dots + \frac{F^{(n)}(0)}{n!} + \text{remainder}. \quad (7)$

Let us substitute $a := x_0, b := y_0, h := x - x_0$ and $k := y - y_0$. By applying (6) at $t = 0$, in the last equality (7), we get in the neighbourhood of the point $(x_0, y_0)$ the following formula.

***

### Slide 70

**Taylor’s Formula for Functions with Two Variables**

**Taylor’s Formula for $\color{red}{f(x, y) \text{ at the Point } (x_0, y_0)}$.**
Suppose $f(x, y)$ and its partial derivatives through order $n + 1$ are continuous throughout an open rectangular region $R$ centered at a point $\mathbf{x}_0 := (x_0, y_0)$. Then,

$f(x, y) = \underbrace{f(\mathbf{x}_0) + (x - x_0)f_x'(\mathbf{x}_0) + (y - y_0)f_y'(\mathbf{x}_0)}_{\text{Linearization}}$
$+ \frac{1}{2!} \Big( (x - x_0)^2 f_{xx}''(\mathbf{x}_0) + 2(x - x_0)(y - y_0)f_{xy}''(\mathbf{x}_0) + (y - y_0)^2 f_{yy}''(\mathbf{x}_0) \Big)$
$+ \frac{1}{3!} \Bigg( (x - x_0)^3 f_{xxx}'''(\mathbf{x}_0) + 3(x - x_0)^2(y - y_0)f_{xxy}'''(\mathbf{x}_0) + 3(x - x_0)(y - y_0)^2 f_{xyy}'''(\mathbf{x}_0)$
$\quad + (y - y_0)^3 f_{yyy}'''(\mathbf{x}_0) \Bigg) + \dots +$
$+ \frac{1}{n!} \Bigg( (x - x_0)^n \frac{\partial^n f}{\partial x^n}(\mathbf{x}_0) + n(x - x_0)^{n-1}(y - y_0)\frac{\partial^n f}{\partial x^{n-1} \partial y}(\mathbf{x}_0) + \dots +$
$\quad + (y - y_0)^n \frac{\partial^n f}{\partial y^n}(\mathbf{x}_0) \Bigg) + R_n(x, y).$

***

### Slide 71

**Taylor’s Formula for Functions with Two Variables**

Where $R_n(x, y)$ is called the **remainder of $n$-th order** for Taylor's formula, and it has the following form

$R_n(x, y) = \frac{1}{(n + 1)!} \Bigg( (x - x_0)^{n+1} \frac{\partial^{n+1} f}{\partial x^{n+1}}(\xi, \eta) + (n + 1)(x - x_0)^n(y - y_0)\frac{\partial^{n+1} f}{\partial x^n \partial y}(\xi, \eta) +$
$\quad \dots + (y - y_0)^{n+1} \frac{\partial^{n+1} f}{\partial y^{n+1}}(\xi, \eta) \Bigg)$

where $(\xi, \eta) = (x_0 + c(x - x_0), y_0 + c(y - y_0))$, for $0 < c \le 1$.

*   Taylor’s formula provides polynomial approximations of multi-variable functions.
*   The first three terms of Taylor’s formula give the function’s linearization.
*   The first $n$ derivative terms give the polynomial.
*   The last term gives the approximation error.

***

### Slide 72

**Taylor’s Formula for Functions Two Several Variables: Example**

**Example.** Find a quadratic approximation to $f(x, y) = \sin x \sin y$ near the origin. How accurate is the approximation if $|x| \le 0.1$ and $|y| \le 0.1$?
**Solution.** For $n = 2$, near $\mathbf{0} := (0, 0)$, we have

$f(x, y) = f(0, 0) + (x f_x'(\mathbf{0}) + y f_y'(\mathbf{0})) + \frac{1}{2} (x^2 f_{xx}''(\mathbf{0}) + 2xy f_{xy}''(\mathbf{0}) + y^2 f_{yy}''(\mathbf{0})) + R_2(x, y),$

where

$R_2(x, y) := \frac{1}{6} \Big( x^3 f_{xxx}''' + 3x^2 y f_{xxy}''' + 3xy^2 f_{xyy}''' + y^3 f_{yyy}''' \Big) \Big|_{(\xi, \eta)}, (\xi, \eta) = (cx, cy), 0 < c \le 1.$

Calculating the values of the partial derivatives,

$f(\mathbf{0}) = \sin x \sin y \Big|_{(0,0)} = 0, \quad f_{xx}''(\mathbf{0}) = -\sin x \sin y \Big|_{(0,0)} = 0,$
$f_x'(\mathbf{0}) = \cos x \sin y \Big|_{(0,0)} = 0, \quad f_{xy}''(\mathbf{0}) = \cos x \cos y \Big|_{(0,0)} = 1,$
$f_y'(\mathbf{0}) = \sin x \cos y \Big|_{(0,0)} = 0, \quad f_{yy}''(\mathbf{0}) = -\sin x \sin y \Big|_{(0,0)} = 0.$

We have the result

$f(x, y) = \sin x \sin y \approx xy$

***

### Slide 73

**Taylor’s Formula for Functions Two Several Variables: Exercises**

The error in the approximation is

$E(x, y) := R_2(x, y) = \frac{1}{6} (x^3 f_{xxx}''' + 3x^2 y f_{xxy}''' + 3xy^2 f_{xyy}''' + y^3 f_{yyy}''') \Big|_{(cx, cy)}.$

The third derivatives never exceed 1 in absolute value because they are products of sines and cosines. Also, $|x| \le 0.1$ and $|y| \le 0.1$. Hence

$|E(x, y)| \le \frac{1}{6} ((0.1)^3 + 3(0.1)^3 + 3(0.1)^3 + (0.1)^3) = \frac{8}{6} (0.1)^3 \le \boxed{0.00134}$

That is, the error will not exceed $0.00134$ if $|x| \le 0.1$ and $|y| \le 0.1$.

$\color{red}{\text{Exercises}}$
1.  Use Taylor's formula for $\color{red}{f(x, y)}$ at the origin to find quadratic and cubic approximations of $\color{red}{f}$ near the origin.
    $\color{red}{f(x, y) = xe^y, f(x, y) = e^x \cos y, f(x, y) = \ln(2x + y + 1), f(x, y) = \frac{1}{1 - x - y + xy}.}$
2.  Use Taylor's formula to find a quadratic approximation of $\color{red}{f(x, y) = \cos x \cos y}$ and $\color{red}{f(x, y) = e^x \sin y}$ at the origin. Estimate the error in the approximation if $\color{red}{|x| \le 0.1}$ and $\color{red}{|y| \le 0.1.}$

***

### Slide 74

**Thank You for Your Attention!**