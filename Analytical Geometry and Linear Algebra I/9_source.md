Here is the full text from the presentations, transcribed without any changes.

***

### Презентация 1: ANALYTIC GEOMETRY AND LINEAR ALGEBRA. Lecture 9

**Страница 1**
ANALYTIC GEOMETRY AND LINEAR ALGEBRA
AGLA - I
INNOPOLIS University
Conic sections
Quadratic forms
Ellipse, Hyperbola, Parabola
Teacher Assistant
Senior Insructor
Eugene Marchuk
PhD in Robotics
November 10, 2025

**Страница 2**
Conic sections
Example 1.
Find the equations of the tangent and normal lines to the ellipse
3x² + 2y² = 5 at point Q(-1, 1).
2 of 55

**Страница 3**
Vectors
Solution.
Step 1. Find the derivative of the given function.
3x² + 2y² – 5 = 0
d/dx (3x² + 2y²-5) = 3 * d/dx (x²) + 2 * d/dx (y²) - d/dx (5)
= 3 * 2x + 2 * 2y * y' - 0
d/dx (3x² + 2y² - 5) = 6x + 4y'y
6x + 4y'y = 0
y' = -3x / 2y
3 of 55

**Страница 4**
Conic sections
Step 2. Find the tangent line.
The value of derivative at the given point Q(-1,1) is nothing but
slope of tangent line yt = k₁x + b₁:
y'(-1, 1) = - (3 * (-1)) / (2 * 1) ⇒ k₁ = 3/2
After substitution:
1 = (3/2) * (-1) + b₁
yQ slope xQ shift
b₁ = 5/2
Therefore, the tangent line is:
Yt = (3/2)x + 5/2
4 of 55

**Страница 5**
Conic sections
Step 3. Find the normal line.
By the known properties of perpendicular planar straight lines:
{ y₁ = k₁ * x + b₁
{ y₂ = k₂ * x + b₂
⇒ k₁ * k₂ = -1 ⇒ k₂ = -1/k₁
After substitution:
1 = (-2/3) * (-1) + b₂
yQ slope xQ shift
b₂ = 1/3
Therefore, the normal line is:
Yn = (-2/3)x + 1/3
5 of 55

**Страница 6**
Conic sections
desmos
[Graph showing the ellipse 3x² + 2y² = 5, the tangent line y = (3/2)x + 5/2, the normal line y = (-2/3)x + 1/3, and the point (-1,1)]
6 of 55

**Страница 7**
Conic sections
Example 2.
Find the eccentricity of an ellipse given that its major axis subtends
an angle of 120° at the endpoints of its minor axis.
7 of 55

**Страница 8**
Conic sections
Solution.
Step 1. Find the eccentricity of an ellipse.
We know, that for the axes of ellipse the identity is correct:
c² = a² - b²
where a is major axis and b is minor axis.
We may choose any quarter of the given ellipse and see, that it contains
rectangular triangle such that its legs are x and y:
(2x)² = x² + y²
y = √3 * x
8 of 55

**Страница 9**
Conic sections
We may conclude, that if:
y = √3 * x
then:
a = √3 * b
and eccentricity of the given ellipse is:
ε = c/a
ε = √ (1 - b²/a²)
ε = √ (2/3)
q.e.d.
9 of 55

**Страница 10**
Conic sections
[Graph of an ellipse showing the relationship between the major and minor axes and the 120-degree angle, which is composed of two 60-degree angles. Another angle of 30 degrees is also marked.]
10 of 55

**Страница 11**
Quadratic forms
A second-degree polynomial equation in two variables of conic can be
written in polynomial form:
Q(x, y) = Ax² + Bxy + Cy² + Dx + Ey + F = 0
or the same with the matrix of quadratic form:
[x y] [A B/2; B/2 C] [x; y] + [D E] [x; y] + F = 0
or the same with the matrix of quadratic equation:
[x y 1] [A B/2 D/2; B/2 C E/2; D/2 E/2 F] [x; y; 1] = Ax²+Bxy+Cy²+Dx+Ey+F
11 of 55

**Страница 12**
Ellipse, Hyperbola, Parabola
Example 3.
Prove that the curve given by 7x² + 48xy – 7y² – 62x – 34y + 98 = 0
is a hyperbola.
- Find the eccentricity of this hyperbola, coordinates of its center and foci.
- Find the equations of axes, asymptotes and directrices of this hyperbola.
12 of 55

**Страница 13**
Ellipse, Hyperbola, Parabola
Solution. Step 1. Mark the coefficients.
7x² + 48xy – 7y² – 62x – 34y + 98 = 0
A = 7; B = 48; C = -7;
D = -62; E = -34; F = 98.
Step 2. Define the type of conic section.
B² – 4AC = 48² – 4 * 7 * (-7) = 48² + 4 * 49
48² + 4 * 49 > 0, then, it is hyperbola.
13 of 55

**Страница 14**
Ellipse, Hyperbola, Parabola
Step 3. Calculate matrix of rotation.
Check if cot 2θ is equal to zero or not:
cot 2θ = (A - C) / B, cot 2θ = (7 - (-7)) / 48, cot 2θ = 7 / 24
cot 2θ ≠ 0, then:
cos 2θ = (A - C) / √((A - C)² + B²), cos 2θ = (7 - (-7)) / √((7 - (-7))² + 48²) = 7 / 25
cot 2θ > 0, then:
cos θ = + √(1/2 * (1 + cos 2θ))
cos θ = + √(1/2) * √(1 + 7/25) = √(1/2) * √(32/25) = 4/5
14 of 55

**Страница 15**
Ellipse, Hyperbola, Parabola
Using the proposed method, we assume that sin θ is always positive,
then:
sin θ = + √(1/2 * (1 - cos 2θ))
sin θ = + √(1/2) * √(1 - 7/25) = + √(1/2) * √(18/25) = 3/5
We don't need to find θ itself because in rotation matrix sines and cosines are used.
[x; y] = [cos θ -sin θ; sin θ cos θ] [x'; y']
[x; y] = [4/5 -3/5; 3/5 4/5] [x'; y']
15 of 55

**Страница 16**
Ellipse, Hyperbola, Parabola
Step 4. Changing of the frame.
{ x = x'(4/5) + y'(-3/5)
{ y = x'(3/5) + y'(4/5)
{ x = 1/5 (4x' - 3y')
{ y = 1/5 (3x' + 4y')
where x', y' are axes of new (v.1) coordinate system, whose axes are
parallel to axes of the hyperbola.
16 of 55

**Страница 17**
Ellipse, Hyperbola, Parabola
Step 5. Substitution. Rotation of coordinate frame around the
hyperbola.
7 * (1/5)² * (4x' - 3y')² + 48 * (1/5)² * (4x' – 3y') * (3x' + 4y') - 7 *
(1/5)² * (3x' + 4y')² - 62 * (1/5) * (4x' - 3y') - 34 * (1/5) * (3x' + 4y') +
+98 = 0
where x', y' are axes of new (v.1) coordinate system, after rotation.
17 of 55

**Страница 18**
Ellipse, Hyperbola, Parabola
Or the same in matrix form:
7x² + 48xy – 7y² – 62x – 34y + 98 = 0
[x y] [7 24; 24 -7] [x; y] + [-62 -34] [x; y] + 98 = 0
After substitution:
[x' y'] [4/5 3/5; -3/5 4/5] [7 24; 24 -7] [4/5 -3/5; 3/5 4/5] [x'; y'] +
+ [-62 -34] [4/5 -3/5; 3/5 4/5] [x'; y'] + 98 = 0
where x', y' are axes of new (v.1) coordinate system, after rotation.
18 of 55

**Страница 19**
Ellipse, Hyperbola, Parabola
After regrouping the factors:
[x' y'] [4/5 3/5; -3/5 4/5] [7 24; 24 -7] [4/5 -3/5; 3/5 4/5] [x'; y'] +
+ [-62 -34] [4/5 -3/5; 3/5 4/5] [x'; y'] + 98 = 0
19 of 55

**Страница 20**
Ellipse, Hyperbola, Parabola
After matrix multiplication we obtain:
[x' y'] [25 0; 0 -25] [x'; y'] + [-70 +10] [x'; y'] + 98 = 0
Expanding the matrix quadratic form into polynomial expression:
25 * (x')² - 25 * (y')² - 70 * (x') + 10 * (y') + 98 = 0
Forming full squares:
25 * (x' - 7/5)² - 25 * (y' - 1/5)² = 49 - 1 - 98
((y' - 1/5)²) / (√2)² - ((x' - 7/5)²) / (√2)² = 1
where x', y' are axes of new (v.1) coordinate system, after rotation.
20 of 55

**Страница 21**
On rotation and translation of conics
Step 6. Shifting.
{ x'' = x' - 7/5 ⇒ { x' = x'' + 7/5
{ y'' = y' - 1/5 ⇒ { y' = y'' + 1/5
⇒ [x'; y'] = [x''; y''] + [7/5; 1/5]
And canonical form is:
(y'')²/(√2)² - (x'')²/(√2)² = 1
where x'', y'' are axes of new (v.2) coordinate system, after shifting.
21 of 55

**Страница 22**
Ellipse, Hyperbola, Parabola
Step 7. Transformations.
[x; y]old = [4/5 -3/5; 3/5 4/5]new'→old ( [x''; y'']new'' + [7/5; 1/5]shift )new'
or the same:
[x; y]old = [4/5 -3/5; 3/5 4/5]new→old [x''; y'']new + [4/5 -3/5; 3/5 4/5]new→old [7/5; 1/5]shift in new
22 of 55

**Страница 23**
Ellipse, Hyperbola, Parabola
Step 8. Find the eccentricity of this hyperbola, coordinates of its
center and foci.
Firstly, find the parameters of hyperbola in its canonical form.
Eccentricity:
ε = √(1 + b²/a²)
ε = √2
Center of hyperbola has coordinates (0,0).
Foci of hyperbola have coordinates (0, ±2):
f = ±√(a² + b²)
23 of 55

**Страница 24**
Ellipse, Hyperbola, Parabola
Axes of hyperbola are:
y'' = 0 x'' = 0
the same in vector form:
[x''; y'']new'' = [t; 0]new''
[x''; y'']new'' = [0; t]new''
Asymptotes of hyperbola are:
[x''; y'']new'' = [t; t]new''
[x''; y'']new'' = [-t; t]new''
24 of 55

**Страница 25**
Ellipse, Hyperbola, Parabola
Step 9. Finally. Indicate the coordinates of origin and foci in the initial
coordinate system.
For origin:
[x; y]old = [4/5 -3/5; 3/5 4/5]new'→old ( [0; 0]new'' + [7/5; 1/5]shift )new' = [1; 1]old
For foci:
[x; y]old = [4/5 -3/5; 3/5 4/5]new'→old ( [0; ±2]new'' + [7/5; 1/5]shift )new' = [1; 1]old ± [-6/5; 8/5]old
25 of 55

**Страница 26**
Ellipse, Hyperbola, Parabola
For axes:
[x; y]old = [4/5 -3/5; 3/5 4/5] ( [0; t] + [7/5; 1/5] ) = [-3/5t + 1; 4/5t + 1]old = [1; 1]old + t[-3/5; 4/5]old
[x; y]old = [4/5 -3/5; 3/5 4/5] ( [t; 0] + [7/5; 1/5] ) = [4/5t + 1; 3/5t + 1]old = [1; 1]old + t[4/5; 3/5]old
26 of 55

**Страница 27**
Ellipse, Hyperbola, Parabola
For asymptotes:
[x; y]old = [4/5 -3/5; 3/5 4/5] ( [t; t] + [7/5; 1/5] ) = [1/5t + 1; 7/5t + 1]old = [1; 1]old + t[1/5; 7/5]old
[x; y]old = [4/5 -3/5; 3/5 4/5] ( [-t; t] + [7/5; 1/5] ) = [-7/5t + 1; 1/5t + 1]old = [1; 1]old + t[-7/5; 1/5]old
27 of 55

**Страница 28**
Ellipse, Hyperbola, Parabola
desmos
[Graph of the hyperbola, its canonical form, the original equation, its center, foci, and asymptotes.]
28 of 55

**Страница 29**
Ellipse, Hyperbola, Parabola
In problems we only have to find canonical forms without turning back
to initial coordinate system the appropriate way can be the method of
orthogonal invariants.
The method of orthogonal invariants works for all conics, but for
parabola it has to be slightly modified.
Let us turn the hyperbolic curve from previous task to its canonical
form.
29 of 55

**Страница 30**
Ellipse, Hyperbola, Parabola
Solution. Step 1. Mark the coefficients.
7x² + 48xy – 7y² – 62x – 34y + 98 = 0
A = 7; B = 48; C = -7;
D = -62; E = -34; F = 98.
Step 2. Define the type of conic section.
B² – 4AC = 48² – 4 * 7 * (-7) = 48² + 4 * 49
48² + 4 * 49 > 0, then, it is hyperbola.
30 of 55

**Страница 31**
Ellipse, Hyperbola, Parabola
Step 3. Compose a system of equations for orthogonal invariants.
{ Ã + Č = 0
{ Ã * Č = -625
{ Ã * Č * F̃ = -31250
Having solved the system, we obtain:
Ã = 25; Č = -25; F̃ = 50
Step 4. Compose the general equation after transformations.
Ãx² + Čy² + F̃ = 0
25x² – 25y² + 50 = 0
31 of 55

**Страница 32**
Ellipse, Hyperbola, Parabola
Step 5. Compose the canonic equation.
ỹ²/(√2)² - x̃²/(√2)² = 1
Step 6. Compose a system to find shifting.
{ Ax₀ + B/2 y₀ + D/2 = 0
{ B/2 x₀ + Cy₀ + E/2 = 0
⇒
{ 7x₀ + 24y₀ - 31 = 0
{ 24x₀ - 7y₀ - 17 = 0
⇒
{ x₀ = 1
{ y₀ = 1
Therefore, in initial coordinate system center of given hyperbola has
coordinates (1, 1).
32 of 55

**Страница 33**
Ellipse, Hyperbola, Parabola
Example 4.
Prove that a curve given by equation
x² + 2xy + y² + x = 0
is a parabola. Find the coordinates of its vertex and focus. Find the
equations of axis and directrix of this parabola.
33 of 55

**Страница 34**
Ellipse, Hyperbola, Parabola
Solution.
Step 1. Mark the coefficients.
A = 1; B = 2; C = 1;
D = 1; E = 0; F = 0.
Step 2. Define the type of conic section.
B² – 4AC = 2² – 4 * 1 * 1 = 4 - 4 = 0
0 = 0, then, it is a parabola.
34 of 55

**Страница 35**
Ellipse, Hyperbola, Parabola
Step 3. Calculate matrix of rotation.
cot 2θ = (A - C) / B
cot 2θ = (1 - 1) / 2 = 0
Then:
cos θ = √2 / 2
sin θ = √2 / 2
[x; y] = [√2/2 -√2/2; √2/2 √2/2] [x'; y']
35 of 55

**Страница 36**
Ellipse, Hyperbola, Parabola
Step 4. Changing of the frame.
{ x = x' cos θ – y' sin θ
{ y = x' sin θ + y' cos θ
{ x = x'√2/2 - y'√2/2
{ y = x'√2/2 + y'√2/2
{ x = √2/2 (x' - y')
{ y = √2/2 (x' + y')
where x', y' are axes of new (v.1) coordinate system, after rotation.
36 of 55

**Страница 37**
Ellipse, Hyperbola, Parabola
Step 5. Substitution. Rotation of coordinate frame around the parabola.
(√2/2)² * (x' - y')² + 2 * (√2/2)² * (x' - y') * (x' + y') +
+ (√2/2)² * (x' + y')² + (√2/2) * (x' - y') = 0
Adding, subtracting, multiplying and dividing the members of this
equation we obtain:
(x' + √2/8)² = 4 * √2/16 (y' + √2/16)
where x', y' are axes of new (v.1) coordinate system, after rotation.
37 of 55

**Страница 38**
Ellipse, Hyperbola, Parabola
Step 6. Shifting.
{ x'' = x' + √2/8
{ y'' = y' + √2/16
⇒
{ x' = x'' - √2/8
{ y' = y'' - √2/16
⇒ [x'; y'] = [x''; y''] - [√2/8; √2/16]
(x'')² = 4 * √2/16 y''
[x; y]old = [√2/2 -√2/2; √2/2 √2/2]new→old ( [x''; y'']new'' - [√2/8; √2/16]shift in new'' )
where x'', y'' are axes of new (v.2) coordinate system, after shifting.
38 of 55

**Страница 39**
Ellipse, Hyperbola, Parabola
Step 7. Finally. Indicate the coordinates of origin in the initial coordinate system.
The only difference between frame x'' (canonic form) and frame x'
(almost canonic form) is shifting without rotation, then we can derive:
[x'; y'] = [x''; y''] - [√2/8; √2/16] ⇒ [x'c; y'c] = [x''c; y''c] - [√2/8; √2/16]
[x'c; y'c] = [0; 0] - [√2/8; √2/16] ⇒ [x'c; y'c] = [-√2/8; -√2/16]
Now we can finally change the frame from x' to x (initial frame):
[xc; yc]old = [√2/2 -√2/2; √2/2 √2/2]new→old [-√2/8; -√2/16]new = [-1/16; -3/16]
39 of 55

**Страница 40**
Ellipse, Hyperbola, Parabola
Step 8. Find the coordinates of vertex and focus of parabola.
[xv; yv] = [xc; yc] ⇒ [xv; yv] = [-1/16; -3/16]
And
[xf; yf]old = [√2/2 -√2/2; √2/2 √2/2]new→old ( [0; √2/16]new'' - [√2/8; √2/16]shift in new'' ) = [-1/8; -1/8]
40 of 55

**Страница 41**
desmos
[Graph of the parabola x² + 2xy + y² + x = 0 and its various transformations and key points.]
41 of 55

**Страница 42**
Ellipse, Hyperbola, Parabola
The method of orthogonal invariants for parabola has to be slightly
modified.
Let us turn the parabolic curve from previous task to its canonical
form.
x² + 2xy + y² + x = 0
42 of 55

**Страница 43**
Ellipse, Hyperbola, Parabola
Solution.
Step 1. Mark the coefficients.
A = 1; B = 2; C = 1;
D = 1; E = 0; F = 0.
Step 2. Compose a system of equations for orthogonal invariants.
{ Č = A + C
{ D̃ = 2√(-Δ / (A+C))
Δ = det [A B/2 D/2; B/2 C E/2; D/2 E/2 F] = det [1 1 1/2; 1 1 0; 1/2 0 0] = -1/4
43 of 55

**Страница 44**
Ellipse, Hyperbola, Parabola
Having solved the system, we obtain:
Č = 2; D̃ = √2/2
Step 3. Compose the general equation after transformations.
Čy² + D̃x = 0
2y² + (√2/2)x = 0
Step 4. Compose the canonic equation.
y² = 4 * (√2/16)x
44 of 55

**Страница 45**
Apendix 1
If B = 0 and A < C, then θ = 0.
If B = 0 and A > C, then θ = π/2.
If B ≠ 0 and A = C, then θ = π/4, sin θ = √2/2, cos θ = √2/2.
If B ≠ 0, then:
cot 2θ = (A - C) / B
cos 2θ = (A - C) / √((A - C)² + B²)
P.S. You can also use the method of characteristic polynomial (the method was shown in Oleg's materials on rotations of conics).
45 of 55

**Страница 46**
Apendix 1
If cot 2θ < 0, then:
cos θ = -√(1/2 * (1 + cos 2θ))
If cot 2θ > 0, then:
cos θ = +√(1/2 * (1 + cos 2θ))
Using the proposed method, we assume that sin θ is always positive,
then:
sin θ = +√(1/2 * (1 - cos 2θ))
We don't need to find θ itself because in rotation matrix sines and
cosines are used.
[x; y] = [cos θ -sin θ; sin θ cos θ] [x'; y']
46 of 55

**Страница 47**
Apendix 1
To rotate any coordinate frame counterclockwise we use matrix of
rotation:
[x; y] = [cos θ -sin θ; sin θ cos θ] [x'; y']
But rotation matrix is also orthogonal matrix, then:
[x'; y'] = [cos θ -sin θ; sin θ cos θ]⁻¹ [x; y], [x'; y'] = [cos θ -sin θ; sin θ cos θ]ᵀ [x; y]
[x'; y'] = [cos θ sin θ; -sin θ cos θ] [x; y]
and this matrix rotates any coordinate frame clockwise.
47 of 55

**Страница 48**
Apendix 2
A second-degree polynomial equation in two variables of conic can be
written in matrix notation:
Ax² + Bxy + Cy² + Dx + Ey + F = 0 (1)
[x y] [A B/2; B/2 C] [x; y] + [D E] [x; y] + F = 0 (2)
[x y 1] [A B/2 D/2; B/2 C E/2; D/2 E/2 F] [x; y; 1] = Ax²+Bxy+Cy²+Dx+Ey+F
48 of 55

**Страница 49**
Apendix 2
The matrix Aq is called the matrix of the quadratic equation:
Aq = [A B/2 D/2; B/2 C E/2; D/2 E/2 F] (3)
and minor A₃₃ is called the matrix of the quadratic form:
A₃₃ = [A B/2; B/2 C] (4)
49 of 55

**Страница 50**
Apendix 2
If det Aq ≠ 0, the conic is not degenerate, and we can see what type
of conic section it is by computing the minor det A₃₃:
- Q is a hyperbola if and only if det A₃₃ < 0
or the same B² – 4AC > 0
- Q is a parabola if and only if det A₃₃ = 0
- Q is a ellipse if and only if det A₃₃ > 0
or the same B² – 4AC < 0
50 of 55

**Страница 51**
Apendix 2
If det Aq = 0, the conic is degenerate, but computing the minor
det A₃₃ still allows us to distinguish its form:
- Q is two intersecting lines (a hyperbola degenerated to its two asymptotes) if and only if det A₃₃ < 0
or the same B² – 4AC > 0
- Q is two parallel straight lines (a degenerate parabola) if and
only if det A₃₃ = 0
- Q is a single point (a degenerate ellipse) if and only if det A₃₃ > 0
or the same B² – 4AC < 0
51 of 55

**Страница 52**
Apendix 3
Alternative way to transform a general equation into canonic form can
be orthogonal invariants.
Ax² + Bxy + Cy² + Dx + Ey + F = 0
Now we assume that the term B responsible for rotation and the terms
D, E responsible for translation are canceled out in new coordinate
system. Therefore, the curve is neither rotated nor translated anymore.
The orthogonal invariants are:
A + C = Ã + Č
det [A B/2; B/2 C] = det [Ã 0; 0 Č]
det [A B/2 D/2; B/2 C E/2; D/2 E/2 F] = det [Ã 0 0; 0 Č 0; 0 0 F̃]
52 of 55

**Страница 53**
Apendix 3
For parabolic curves the method of orthogonal invariants has to be
slightly modified:
Čỹ² + D̃x = 0
A + C = Ã + Č = Č
det [A B/2; B/2 C] = det [0 0; 0 Č] = 0
det [A B/2 D/2; B/2 C E/2; D/2 E/2 F] = det [0 0 D̃/2; 0 Č 0; D̃/2 0 0] = -ČD̃²/4
Let it be:
Δ = det [A B/2 D/2; B/2 C E/2; D/2 E/2 F] ⇒ D̃ = 2√(-Δ / (A+C))
53 of 55

**Страница 54**
Apendix 3
Therefore:
{ Č = A + C
{ D̃ = 2√(-Δ / (A+C))
and:
y² = 4 * (1/2) * √(Δ / (A+C)³) * x
54 of 55

**Страница 55**
References
- Gilbert Strang. Linear Algebra and Its Applications. https:
//math.mit.edu/~gs/linearalgebra/ila5/indexila5.html
- Dimension (vector space). https:
//en.wikipedia.org/wiki/Dimension_(vector_space)
- Median (geometry).
https://en.wikipedia.org/wiki/Median_(geometry)
- https://matrixcalc.org
- https://www.desmos.com/calculator?lang=eng
55 of 55

***

### Презентация 2: Analytical Geometry and Linear Algebra, Tutorial 9

**Страница 1**
Analytical Geometry and Linear Algebra, Tutorial
Salman Ahmadi-Asl
November 10, 2025
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 1/24

**Страница 2**
Problem 1
As θ varies from 0 to 2π, the point M(2 + 3 cos θ, 1 + 3 sin θ) traces which
curve?
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 2/24

**Страница 3**
Step 1: Write the Parametric Equations
The coordinates of point M are given by:
x = 2 + 3 cos θ
y = 1 + 3 sin θ
where θ ∈ [0, 2π).
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 3/24

**Страница 4**
Step 2: Isolate Trigonometric Functions
From the parametric equations:
cos θ = (x - 2) / 3
sin θ = (y - 1) / 3
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 4/24

**Страница 5**
Step 3: Use Pythagorean Identity
We know the fundamental trigonometric identity:
cos² θ + sin² θ = 1
Substitute the expressions from the previous step:
((x - 2) / 3)² + ((y - 1) / 3)² = 1
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 5/24

**Страница 6**
Step 4: Simplify to Standard Form
((x - 2) / 3)² + ((y - 1) / 3)² = 1
(x - 2)²/9 + (y - 1)²/9 = 1
(x – 2)² + (y - 1)² = 9
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 6/24

**Страница 7**
Step 5: Identify the Curve
The equation:
(x – 2)² + (y - 1)² = 9
represents a circle in standard form:
(x − h)² + (y - k)² = r²
where:
- Center: (h, k) = (2, 1)
- Radius: r = √9 = 3
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 7/24

**Страница 8**
Final Answer
Solution
As θ varies from 0 to 2π, the point M(2 + 3 cos θ, 1 + 3 sin θ) traces a circle with:
- Center at (2, 1)
- Radius 3
- Equation: (x – 2)² + (y − 1)² = 9
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 8/24

**Страница 9**
Problem 1
Find the length of the tangent drawn from the point A(4,3) to the circle
given by the equation x² + y² – 2x – 4y + 1 = 0, (The length of AH in
the following figure).
[Drawing of a circle with center C, a point A outside the circle, and a tangent line from A to the circle at point H. A right angle is marked at H.]
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 9/24

**Страница 10**
Step 1: Identify the Circle's Center and Radius
Given circle equation:
x² + y² – 2x – 4y + 1 = 0
Complete the square:
(x² – 2x) + (y² – 4y) + 1 = 0
(x² – 2x + 1) + (y² – 4y + 4) + 1 - 1 - 4 = 0
(x – 1)² + (y − 2)² – 4 = 0
(x – 1)² + (y − 2)² = 4
So:
- Center C = (1, 2)
- Radius r = √4 = 2
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 10/24

**Страница 11**
Step 2: Distance from Point to Center
Point A = (4,3), Center C = (1, 2)
Distance formula:
AC = √( (4 – 1)² + (3 – 2)² )
= √( 3² + 1² )
= √( 9 + 1 )
= √10
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 11/24

**Страница 12**
Step 3: Apply Tangent Length Formula
For a circle with center C, radius r, and external point A:
Tangent length = √( (AC)² - r² )
Substitute values:
Tangent length = √( (√10)² – 2² )
= √( 10 - 4 )
= √6
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 12/24

**Страница 13**
Problem 3
Find the equation of the tangent line to the circle given by
x² + y² + 4x – 2y – 20 = 0
at the point P(2, 4).
Step 1: Verify the point lies on the circle
Substitute x = 2, y = 4 into the equation:
(2)² + (4)² + 4(2) - 2(4) – 20 = 4 + 16 + 8 - 8 - 20
= 28 - 28 = 0 ✓
The point P(2, 4) lies on the circle.
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 13/24

**Страница 14**
Problem 3 Solution (Continued)
Step 2: Implicit Differentiation
Differentiate both sides with respect to x:
d/dx(x²) + d/dx(y²) + d/dx(4x) - d/dx(2y) - d/dx(20) = 0
2x + 2y(dy/dx) + 4 - 2(dy/dx) = 0
Step 3: Solve for dy/dx
2y(dy/dx) - 2(dy/dx) = -2x - 4
2(y - 1)(dy/dx) = -2(x + 2)
dy/dx = -(x + 2) / (y - 1)
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 14/24

**Страница 15**
Problem 3 Solution (Final)
Step 4: Find the slope at P(2, 4)
m = dy/dx |(2,4) = -(2 + 2) / (4 - 1) = -4/3
Step 5: Equation of the tangent line
Using point-slope form:
y - y₁ = m(x – x₁)
y - 4 = -4/3(x - 2)
y = -4/3x + 8/3 + 4
y = -4/3x + 20/3
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 15/24

**Страница 16**
Problem 4
The point P(3, 2) lies on the ellipse defined by
4x² + 9y² = 72
a) Show that P lies on the ellipse. b) Find the slope of the normal line to
the ellipse at point P. c) Hence, find the equation of the normal line.
Part (a): Verify the point
Substitute x = 3, y = 2 into the equation:
4(3)² + 9(2)² = 4(9) + 9(4)
= 36 + 36 = 72 ✓
The point P(3, 2) lies on the ellipse.
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 16/24

**Страница 17**
Problem 4 Solution (Continued)
Part (b): Find slope of the normal
Step 1: Implicit Differentiation
d/dx(4x²) + d/dx(9y²) = d/dx(72)
8x + 18y(dy/dx) = 0
18y(dy/dx) = -8x
dy/dx = -4x / 9y
Step 2: Slope of tangent at P(3, 2)
m_tangent = - (4(3)) / (9(2)) = -12/18 = -2/3
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 17/24

**Страница 18**
Problem 4 Solution (Continued)
Step 3: Slope of normal
m_normal = -1 / m_tangent = -1 / (-2/3) = 3/2
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 18/24

**Страница 19**
Problem 4 Solution (Final)
Part (c): Equation of the normal line
Using point-slope form with m = 3/2 and point P(3, 2):
y - y₁ = m(x – x₁)
y - 2 = 3/2(x - 3)
y = 3/2x - 9/2 + 2
y = 3/2x - 5/2
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 19/24

**Страница 20**
Problem 5: Tangent to a Hyperbola
Problem
Consider the rectangular hyperbola given by the equation
xy = 12
a) Use implicit differentiation to find an expression for dy/dx. b) Find the
equation of the tangent line to the hyperbola at the point P(3,4). c)
Show that this tangent line intersects the x-axis at (6,0).
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 20/24

**Страница 21**
Solution to Problem 5
Part (a): Implicit Differentiation
d/dx(xy) = d/dx(12)
x(dy/dx) + y(1) = 0 (Product Rule)
x(dy/dx) = -y
dy/dx = -y/x
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 21/24

**Страница 22**
Problem 5 Solution (Continued)
Part (b): Equation of tangent line
Step 1: Verify point P(3, 4) lies on hyperbola
3 × 4 = 12 ✓
Step 2: Find slope at P(3,4)
m = dy/dx |(3,4) = -4/3
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 22/24

**Страница 23**
Problem 5 Solution (Continued)
Step 3: Equation of tangent line
y - 4 = -4/3(x - 3)
y = -4/3x + 4 + 4
y = -4/3x + 8
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 23/24

**Страница 24**
Thank You!
Questions?
Salman Ahmadi-Asl, Analytical Geometry and Linear Algebra, Tutc, November 10, 2025, 24/24

***

### Презентация 3: Parametric Equations & Tangents (Lab 9)

**Страница 1**
Parametric Equations & Tangents
Circles, Ellipses, and Implicit Differentiation
Salman Ahmadi-Asl
November 11, 2025
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 1/30

**Страница 2**
Overview
1 Parametric Equations of a Circle
2 Parametric Equations of an Ellipse
3 Review: Implicit Differentiation
4 Tangents via Implicit Differentiation
5 The General Implicit Formula
6 Applications and Examples
7 Summary and Applications
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 2/30

**Страница 3**
Parametric Equations of a Circle
Standard Equation of a Circle
The standard form for a circle centered at the origin (0,0) with radius r is:
x² + y² = r²
Parametric Form
We can describe the coordinates (x, y) of any point on the circle using a
parameter θ (the angle from the positive x-axis):
x = r cos θ
y = r sin θ
As θ goes from 0 to 2π, the point (x, y) traces the entire circle.
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 3/30

**Страница 4**
Visualizing the Circle Parameter
[A graph showing a circle centered at the origin with radius r. A point (r cos θ, r sin θ) is on the circle, forming an angle θ with the positive x-axis.]
x² + y² = r²
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 4/30

**Страница 5**
Circle: Standard vs Parametric Form
Standard Form
Center at origin (0,0), radius r:
x² + y² = r²
Center at (h, k), radius r:
(x − h)² + (y - k)² = r²
Parametric Form
Center at origin (0,0), radius r:
x = r cos θ
y = r sin θ
where 0 ≤ θ ≤ 2π
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 5/30

**Страница 6**
Circle: Parametric Form with Center Translation
General Parametric Form
Center at (h, k), radius r:
x = h + r cos θ
y = k + r sin θ
where 0 ≤ θ ≤ 2π
[A graph showing a circle centered at (h, k) with a point (h + r cos θ, k + r sin θ) on its circumference.]
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 6/30

**Страница 7**
Ellipse: Parametric Form with Center Translation
General Parametric Form
Center at (h, k), semi-axes a and b:
x = h + a cos θ
y = k + b sin θ
where 0 ≤ θ ≤ 2π
[A graph showing an ellipse centered at (h, k) with a point (h + a cos θ, k + b sin θ) on its circumference.]
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 7/30

**Страница 8**
Parametric Equations of an Ellipse
Standard Equation of an Ellipse
For an ellipse centered at the origin (0,0) with semi-major axis a
(horizontal) and semi-minor axis b (vertical):
x²/a² + y²/b² = 1
Parametric Form
The parametric equations are very similar to the circle, but scaled:
x = a cos θ
y = b sin θ
Again, as θ goes from 0 to 2π, the point (x, y) traces the entire ellipse.
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 8/30

**Страница 9**
Review: What is Implicit Differentiation?
- Used when we have equations where x and y are mixed together
- Examples: x² + y² = 25, x²/9 + y²/4 = 1, x³ + y³ = 6xy
- We differentiate both sides with respect to x
- When differentiating y terms, we use the chain rule:
d/dx(yⁿ) = nyⁿ⁻¹ * dy/dx
Why We Need It
- Solving for y explicitly can be messy or impossible
- Even when possible, explicit differentiation might be more complicated
- Provides a direct way to find slopes of tangent lines
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 9/30

**Страница 10**
Quick Practice Review
Example
Differentiate x² + y² = 25 with respect to x.
Solution
d/dx(x²) + d/dx(y²) = d/dx(25)
2x + 2y(dy/dx) = 0
2y(dy/dx) = -2x
dy/dx = -x/y
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 10/30

**Страница 11**
Why Implicit Differentiation?
- We often have curves defined implicitly (e.g., x² + y² = r²).
- It can be messy to solve for y explicitly, especially for ellipses.
- Implicit differentiation allows us to find the derivative dy/dx without
solving for y.
- This derivative gives us the slope of the tangent line at any point
(x, y) on the curve.
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 11/30

**Страница 12**
Tangent to a Circle: Example
Example
Find the equation of the tangent line to the circle x² + y² = 25 at the
point (3, 4).
Solution using Implicit Differentiation
1. Differentiate both sides with respect to x:
d/dx(x²) + d/dx(y²) = d/dx(25)
2x + 2y(dy/dx) = 0
2. Solve for dy/dx (the slope m):
2y(dy/dx) = -2x
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 12/30

**Страница 13**
Tangent to a Circle: Example (Cont.)
Solution (Cont.)
3. Evaluate the slope at the point (3, 4):
m = dy/dx |(3,4) = -3/4
4. Find the equation of the tangent line (Point-Slope Form):
y - y₁ = m(x – x₁)
y - 4 = -3/4(x - 3)
Final Answer: y = -3/4x + 25/4
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 13/30

**Страница 14**
Tangent to an Ellipse: Example
Example
Find the equation of the tangent line to the ellipse x²/9 + y²/4 = 1 at the
point (3/√2, √2).
Solution using Implicit Differentiation
1. Differentiate both sides with respect to x:
d/dx(x²/9) + d/dx(y²/4) = d/dx(1)
2x/9 + 2y/4 (dy/dx) = 0
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 14/30

**Страница 15**
Tangent to an Ellipse: Example (Cont.)
Solution (Cont.)
2. Solve for dy/dx:
2y/4 (dy/dx) = -2x/9
y/2 (dy/dx) = -2x/9
dy/dx = -4x/9y
3. Evaluate the slope at the point (3/√2, √2):
m = - (4 * (3/√2)) / (9 * (√2)) = - (12/√2) / (9√2) = -12 / (9*2) = -12/18 = -2/3
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 15/30

**Страница 16**
Tangent to an Ellipse: Example (Final)
Solution (Final Step)
4. Find the equation of the tangent line:
y - y₁ = m(x – x₁)
y - √2 = -2/3(x - 3/√2)
Final Answer: y = -2/3x + 2/√2 + √2 = -2/3x + 2√2
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 16/30

**Страница 17**
Towards a General Formula
Let's write our curve equation as:
F(x, y) = 0
- For a circle: F(x, y) = x² + y² – 25 = 0
- For an ellipse: F(x, y) = x²/9 + y²/4 – 1 = 0
- For any curve: F(x, y) = 0
The Big Question
Can we find a general formula for dy/dx in terms of F?
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 17/30

**Страница 18**
Partial Derivatives - A Quick Introduction
Partial Derivative with respect to x (Fₓ)
- Differentiate F(x, y) with respect to x
- Treat y as a constant
- Notation: Fₓ, ∂F/∂x, or F₁
Partial Derivative with respect to y (Fᵧ)
- Differentiate F(x, y) with respect to y
- Treat x as a constant
- Notation: Fᵧ, ∂F/∂y, or F₂
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 18/30

**Страница 19**
Partial Derivatives: Examples
Example
Example 1 For F(x, y) = x² + y² – 25:
Fₓ = ∂F/∂x = 2x
Fᵧ = ∂F/∂y = 2y
Example
Example 2 For F(x, y) = x²/9 + y²/4 – 1:
Fₓ = ∂F/∂x = 2x/9
Fᵧ = ∂F/∂y = 2y/4 = y/2
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 19/30

**Страница 20**
Practice: Partial Derivatives
Practice Problem 1
Find Fₓ and Fᵧ for F(x, y) = x³ + 3x²y – y³.
Practice Problem 2
Find Fₓ and Fᵧ for F(x, y) = sin(x) + cos(y).
Answers:
1. Fₓ = 3x² + 6xy, Fᵧ = 3x² - 3y²
2. Fₓ = cos(x), Fᵧ = -sin(y)
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 20/30

**Страница 21**
The General Implicit Differentiation Formula
The Main Result
dy/dx = -Fₓ/Fᵧ
- Fₓ: Partial derivative of F with respect to x
- Fᵧ: Partial derivative of F with respect to y
- Valid when Fᵧ ≠ 0 (denominator not zero)
Remember
This formula gives the slope of the tangent line to the curve F(x, y) = 0
at any point (x, y) on the curve.
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 21/30

**Страница 22**
Verifying with Circle Example
Example
Find dy/dx for the circle x² + y² = 25 using the general formula.
Solution
Step 1: Write as F(x, y) = x² + y² – 25 = 0
Step 2: Find partial derivatives:
Fₓ = 2x
Fᵧ = 2y
Step 3: Apply the formula:
dy/dx = -Fₓ/Fᵧ = -2x/2y = -x/y
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 22/30

**Страница 23**
Verifying with Ellipse Example
Example
Find dy/dx for the ellipse x²/9 + y²/4 = 1 using the general formula.
Solution
Step 1: Write as F(x, y) = x²/9 + y²/4 – 1 = 0
Step 2: Find partial derivatives:
Fₓ = 2x/9
Fᵧ = 2y/4 = y/2
Step 3: Apply the formula:
dy/dx = -Fₓ/Fᵧ = -(2x/9)/(y/2) = -2x/9 * 2/y = -4x/9y
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 23/30

**Страница 24**
New Example: More Complex Curve
Example
Find the slope of the tangent line to the curve x³ + y³ = 6xy at the point
(3, 3).
Solution using General Formula
Step 1: F(x, y) = x³ + y³ – 6xy = 0
Step 2: Find partial derivatives:
Fₓ = 3x² - 6y
Fᵧ = 3y² - 6x
Step 3: Apply the formula:
dy/dx = -Fₓ/Fᵧ = -(3x² - 6y)/(3y² - 6x)
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 24/30

**Страница 25**
New Example: Continued
Solution (Continued)
Step 4: Evaluate at point (3, 3):
dy/dx = -(3(3)² – 6(3))/(3(3)² – 6(3)) = -(27 - 18)/(27 - 18) = -9/9 = -1
Step 5: Tangent line equation:
y - 3 = -1(x - 3) ⇒ y = -x + 6
Check Your Understanding
Why can't we use explicit differentiation easily for this curve?
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 25/30

**Страница 26**
Practice with General Formula
Practice Problem 1
Use the general formula to find dy/dx for the curve sin(x) + cos(y) = 1.
Practice Problem 2
Find the slope of the tangent line to x²y + y²x = 2 at the point (1, 1).
Answers:
1. dy/dx = cos(x)/sin(y)
2. dy/dx = -1
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 26/30

**Страница 27**
Advanced Example: Finding Vertical Tangents
Example
Find the points on the curve x² + y³ – 3xy = 0 where the tangent is
vertical.
Solution
Step 1: F(x, y) = x² + y³ – 3xy = 0
Step 2: Find partial derivatives:
Fₓ = 2x – 3y
Fᵧ = 3y² - 3x
Step 3: Vertical tangent occurs when Fᵧ = 0:
3y² - 3x = 0 ⇒ x = y²
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 27/30

**Страница 28**
Advanced Example: Continued
Solution (Continued)
Step 4: Substitute x = y² into original equation:
(y²)² + y³ - 3(y²)y = 0
y⁴ + y³ - 3y³ = 0
y⁴ – 2y³ = 0
y³(y - 2) = 0
y = 0 or y = 2
Step 5: Find corresponding x values:
- When y = 0: x = (0)² = 0 → Point (0,0)
- When y = 2: x = (2)² = 4 → Point (4, 2)
Answer: Vertical tangents at (0,0) and (4, 2)
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 28/30

**Страница 29**
Summary of Key Points
1. For a curve defined by F(x, y) = 0, the derivative is:
dy/dx = -Fₓ/Fᵧ
2. Fₓ and Fᵧ are partial derivatives:
   - Fₓ: differentiate with respect to x, treat y as constant
   - Fᵧ: differentiate with respect to y, treat x as constant
3. This formula works when Fᵧ ≠ 0
4. The formula comes from the chain rule and has a beautiful geometric
interpretation
5. It's much more efficient than traditional implicit differentiation for
complex curves
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 29/30

**Страница 30**
Thank You!
Questions?
Salman Ahmadi-Asl, Parametric Equations & Tangents, November 11, 2025, 30/30 11, 2025, 30/30