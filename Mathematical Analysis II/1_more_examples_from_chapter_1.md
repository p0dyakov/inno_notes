### 1. Интегрирование методом подстановки (Substitution Rule)
*Базовый метод нахождения неопределенных интегралов.*

**Набор 1 (Стандартные задачи):**
1.  $I_1 = \int \frac{dx}{5-12x-9x^2}$
2.  $I_2 = \int \frac{3x-2}{2-3x+5x^2} dx$
3.  $I_3 = \int \frac{dx}{\sqrt{17-4x-x^2}}$
4.  $I_4 = \int \frac{3x-6}{\sqrt{x^2-4x+5}} dx$
5.  $I_5 = \int \frac{(1+\sqrt{x})^{1/3}}{\sqrt{x}} dx$
6.  $I_6 = \int \frac{\sin(2x)}{\sqrt{1+\sin^4 x}} dx$
7.  $I_7 = \int \frac{dx}{1+\sqrt[3]{x+1}}$
8.  $I_8 = \int (2x+1)e^{2x^2+2x-1} dx$
9.  $I_9 = \int \frac{e^{2x}}{\sqrt[4]{1+e^x}} dx$
10. $I_{10} = \int \frac{\ln(2x)}{x \ln(4x)} dx$
11. $I_{11} = \int \frac{1}{x^2} \cos\left(\frac{1}{x}\right) dx$
12. $I_{12} = \int \sqrt{\sin x} \cos^5 x \, dx$
13. $I_{13} = \int \frac{\sin(2x)}{\sqrt{25\sin^2 x + 9\cos^2 x}} dx$
14. $I_{14} = \int \frac{e^{\tan x} + \cot x}{\cos^2 x} dx$
15. $I_{15} = \int \frac{(x+1)e^x}{\cos^2(xe^x)} dx$

**Набор 2 (Задачи из MIT Integration Bee и смешанные):**
16. $I_1 = \int \frac{2x}{\sqrt{1-x^4}} dx$
17. $I_2 = \int \frac{\ln(\ln x)}{x \ln x} dx$
18. $I_3 = \int \frac{\cos(\sqrt{x})}{\sqrt{x}} dx$
19. $I_4 = \int \frac{dx}{\sqrt{x}-1}$
20. $I_5 = \int \frac{dx}{\sqrt{e^x-1}}$
21. $I_6 = \int \frac{dx}{x\sqrt{x^2-2}}$
22. $I_7 = \int \frac{dx}{5+4\sqrt{x}+x}$
23. $I_8 = \int \frac{dx}{x^3-x}$
24. $I_9 = \int \frac{dx}{x(1+x^5)}$
25. $I_{10} = \int x^x (1+\ln x) dx$
26. $I_{11} = \int x e^{x^2+x^2} dx$ (возможно опечатка в оригинале, вероятно $xe^{x^2}$)
27. $I_{12} = \int x^3 \sqrt{x^2+1} dx$
28. $I_1 = \int \frac{x^3-2}{\sqrt{x^2+x+1}} dx$
29. $I_2 = \int \frac{x^4-5x^3+6x-7}{\sqrt{x^2+2x+3}} dx$
30. $I_1 = \int \frac{e^{\sin x}}{\tan x \cdot \csc x} dx$
31. $I_2 = \int \tan^2 x dx$
32. $I_3 = \int \sin x \tan^2 x dx$
33. $I_4 = \int \frac{1+\cot x}{1-\cot x} dx$
34. $I_5 = \int \frac{dx}{1+3e^x}$
35. $I_6 = \int \sqrt{\csc x - \sin x} \, dx$
36. $I_7 = \int \frac{x^6-1}{x^4+x^3-x-1} dx$
37. $I_8 = \int (e^x \cos x - e^x \sin x) dx$
38. $I_9 = \int \sin x \sqrt{1+\tan^2 x} \, dx$
39. $I_{10} = \int (\cos^4 x - \sin^4 x) dx$
40. $I_{11} = \int \frac{x}{\sqrt{2+4x}} dx$
41. $I_{12}^* = \int (x+1)^2 (x-1)^{1/3} dx$
42. $I_{13}^* = \int \frac{\ln x \cos x - (\frac{\sin x}{x})}{\ln^2 x} dx$

---

### 2. Интегрирование по частям (Integration by Parts)
1.  $I_1 = \int x 2^x dx$
2.  $I_2 = \int x \sinh x \, dx$
3.  $I_3 = \int x \ln(1+\frac{1}{x}) dx$
4.  $I_4 = \int x \cos(5x-7) dx$
5.  $I_5 = \int (x^2-6x+2)e^{3x} dx$
6.  $I_6 = \int \sin x \ln(\tan x) dx$
7.  $I_7 = \int x \tan^2(2x) dx$
8.  $I_8 = \int \arccos(5x-2) dx$
9.  $I_9 = \int \frac{\arcsin x}{x^2} dx$
10. $I_{10} = \int x^2 \sqrt{x^2+a^2} dx$
11. $I_{11} = \int x e^x \sin^2 x \, dx$
12. $I_{12} = \int x e^{\sqrt{x}} dx$
13. $I_{13} = \int \frac{\ln(\sin x)}{\sin^2 x} dx$
14. $I_{14} = \int \cos(\ln x) dx$
15. $I_{15} = \int x^3 \ln\left(\frac{x+3}{x-3}\right) dx$
16. **Рекуррентные формулы:** Найти формулу понижения степени для:
    *   $I_n = \int \cos^n x \, dx$
    *   $\int \cot^n x \, dx$
    *   $\int x^n \sin x \, dx$
    *   $I_{m,n} = \int \sin^m x \cos^n x \, dx$

---

### 3. Интегрирование тригонометрических и гиперболических функций
1.  $I_1 = \int \sin^5 x \sqrt[3]{\cos x} \, dx$
2.  $I_2 = \int \frac{\cos^3 x}{2+\sin x} dx$
3.  $I_3 = \int \frac{dx}{\sin x + 2\cos x + 6}$
4.  $I_4 = \int \frac{dx}{\cos(2x) - \sin(2x)}$
5.  $I_5 = \int \frac{\sin^2 x}{\cos^6 x} dx$
6.  $I_6 = \int \sin x \sin(3x) dx$
7.  $I_7 = \int \cos x \cos 3x \cos 5x \, dx$
8.  $I_8 = \int \frac{\cos^2 x}{\sin(4x)} dx$
9.  $I_9 = \int \frac{\cos(3x)}{\sin^5 x} dx$
10. $I_{10} = \int \cosh x \cosh(2x) \cosh(3x) dx$
11. $I_{11} = \int \sinh^2(2x) \cosh^2(2x) dx$
12. $I_{12} = \int \sinh^2 x \cosh^4 x \, dx$
13. $I_{13} = \int \frac{dx}{\sinh x \cosh^2 x}$
14. $I_{14} = \int \frac{\cosh^5 x}{\sinh x} dx$
15. $I_{15} = \int \frac{\sinh(2x) + 4\sinh x}{\cosh^3 x - 3\cosh x} dx$

---

### 4. Интегрирование рациональных функций (Partial Fractions)
1.  $I_1 = \int \frac{x^2+2x-1}{2x^3+3x^2-2x} dx$
2.  $I_2 = \int \frac{x^4-2x^2+4x+1}{x^3-x^2-x+1} dx$
3.  $I_3 = \int \frac{2x^2-x+4}{x^3+4x} dx$
4.  $I_4 = \int \frac{1-x+2x^2-x^3}{x(x^2+1)^2} dx$
5.  $I_5 = \int \frac{x^5+x^4-8}{x^3-4x} dx$
6.  $I_6 = \int \frac{7x^2+26x-9}{x^4+4x^3+4x^2-9} dx$
7.  $I_7 = \int \frac{2x^2+41x-91}{x^3-2x^2-11x+12} dx$
8.  $I_8 = \int \frac{x^6-2x^4+3x^3-9x^2+4}{x^5-5x^3+4x} dx$
9.  $I_9 = \int \frac{x^5-2x^2+3}{x^2-4x+4} dx$
10. $I_{10} = \int \frac{x^2+1}{x(x-1)^3} dx$

---

### 5. Сложные и другие методы интегрирования (Other Techniques)
1.  $I_1 = \int \sin x \cosh x \, dx$
2.  $I_2 = \int \frac{e^x \cos^2(\sqrt[3]{1+e^x})}{\sqrt[3]{1+e^x}} dx$
3.  $I_3 = \int (2x+1)e^{\arctan x} dx$
4.  $I_4 = \int x(1+x^2)^{-3/2} e^{\arctan x} dx$
5.  $I_5 = \int \frac{x \cos x - \sin x}{x^2} dx$
6.  $I_6 = \int \frac{1}{x^3} \sqrt[5]{\frac{x}{x+1}} dx$
7.  $I_7 = \int \frac{x^2}{(a^2-x^2)^{3/2}} dx \quad (a>0)$
8.  $I_8 = \int \frac{dx}{x^2\sqrt{a^2-x^2}} \quad (a>0)$
9.  $I_9 = \int \arctan(1-\sqrt{x}) dx$
10. $I_{10} = \int \frac{\arcsin x}{(1-x^2)\sqrt{1-x^2}} dx$
11. $I_{11} = \int \frac{dx}{3x+\sqrt[3]{x^2}}$
12. $I_{12} = \int x\sqrt[4]{x-2} dx$
13. $I_{13} = \int \frac{x\sqrt[3]{x+2}}{x+\sqrt[3]{x+2}} dx$
14. $I_{14} = \int \frac{dx}{\sqrt[3]{4x^2+4x+1}-\sqrt{2x+1}}$
15. $I_{15} = \int \frac{dx}{x\sqrt{5x^2-2x+1}}$

---

### 6. Определенные интегралы (Definite Integrals & Substitution)
*Вычислить следующие определенные интегралы:*
1.  $I_1 = \int_0^1 \frac{10\sqrt{x}}{(1+\sqrt{x^3})^2} dx$
2.  $I_2 = \int_{-\pi}^{\pi} \frac{\cos x}{\sqrt{4+3\sin x}} dx$
3.  $I_3 = \int_1^4 \frac{1}{\sqrt{x}(1+2\sqrt{x})^{10}} dx$
4.  $I_4 = \int_{-1}^{-1/2} x^{-2} \sin^2\left(1+\frac{1}{x}\right) dx$
5.  $I_5 = \int_2^{16} \frac{1}{2x\sqrt{\ln x}} dx$
6.  $I_6 = \int_0^{\pi/3} \frac{\sin(2x)}{\sqrt{1+3\sin^2 x}} dx$
7.  $I_7 = \int_0^1 \frac{1}{(1+\sqrt{x})^4} dx$
8.  $I_8 = \int_0^{\pi/2} \cos x \sin(\sin x) dx$
9.  $I_9 = \int_0^{\sqrt{3}/2} x \arctan(2x) dx$
10. $I_{10} = \int_0^{2\pi} x^2 \cos(4x) dx$

---

### 7. Теорема Ньютона-Лейбница и Функции, определенные интегралом
**Вычисление интегралов (FTC Part 2):**
1.  $I_1 = \int_1^4 (3x^2 - \frac{x^3}{4}) dx$
2.  $I_2 = \int_0^1 (x^2 + \sqrt{x}) dx$
3.  $I_3 = \int_0^{\pi/3} 4\frac{\sin u}{\cos^2 u} du$
4.  $I_4 = \int_{-\pi/3}^{\pi/3} \sin^2 t \, dt$
5.  $I_5 = \int_1^8 \frac{(\sqrt[3]{x}+1)(2-\sqrt[3]{x^2})}{\sqrt[3]{x}} dx$
6.  $I_6 = \int_{-4}^3 |x-1| dx$
7.  $I_7 = \int_0^{\pi} \frac{1}{2} (\cos x + |\cos x|) dx$
8.  $I_8 = \int_{1/2}^{1/\sqrt{2}} \frac{4}{\sqrt{1-x^2}} dx$
9.  $I_9 = \int_0^{\pi} f(x) dx$, где $f(x) = \begin{cases} \sin x, & 0 \le x < \pi/2 \\ \cos x, & \pi/2 \le x \le \pi \end{cases}$
10. $I_{10} = \int_{-2}^2 f(x) dx$, где $f(x) = \begin{cases} 2, & -2 \le x \le 0 \\ 4-x^2, & 0 < x \le 2 \end{cases}$

**Найти ошибку в вычислениях:**
*   $\int_{-2}^1 x^{-4} dx = [\frac{x^{-3}}{-3}]_{-2}^1$
*   $\int_{\pi/3}^{\pi} \sec\theta \cdot \tan\theta \, d\theta = [\sec\theta]_{\pi/3}^{\pi} = -3$

**Производная интеграла по верхнему пределу (FTC Part 1):**
*Найти $\frac{dy}{dx}$ для следующих функций:*
1.  $y = \int_1^x \frac{1}{u} du \quad (x>0)$
2.  $y = \int_{\sqrt{x}}^0 \sin(v^2) dv$
3.  $y = \int_{\tan x}^0 \frac{dt}{1+t^2}$
4.  $y = \int_{2x}^{3x} \frac{t^2-1}{t^2+1} dt$
5.  $y = \int_x^{x^2} e^{\theta^2} d\theta$
6.  $y = \int_{\sqrt{x}}^{2x} \arctan(q) dq$
7.  $y = \int_{1-2x}^{1+2x} t \sin t \, dt$
8.  $y = \int_{\cos x}^{\sin x} \ln(1+2v) dv$

---

### 8. Суммы Римана (Riemann Sums)
**Exercise 1:** Для каждой функции построить график, разбить интервал на 4 части, построить прямоугольники и найти сумму Римана $\sum_{k=1}^4 f(c_k)\Delta x_k$, где $c_k$ — это (a) левый край, (b) правый край, (c) середина интервала.
1.  $f(x) = x^2 - 1, \quad x \in [0, 2]$
2.  $f(x) = \sin x, \quad x \in [-\pi, \pi]$

**Exercise 2:** Найти формулу для суммы Римана, разбивая интервал на $n$ равных частей и используя правые концы. Затем найти предел при $n \to \infty$.
1.  $f(x) = 2x, \quad x \in [0, 1]$
2.  $f(x) = 3x + 2x^2, \quad x \in [0, 1]$

---

### 9. Несобственные интегралы и Ряды (Improper Integrals & Series)
**Exercise 1. Определить сходимость интегралов и вычислить сходящиеся:**
1.  $\int_3^{\infty} \frac{dx}{(x-2)^{3/2}}$
2.  $\int_{-\infty}^{\infty} x e^{-x^2} dx$
3.  $\int_1^{\infty} \frac{e^{-1/x}}{x^2} dx$
4.  $\int_2^{\infty} \frac{dx}{x^2+2x-3}$
5.  $\int_0^{\infty} e^{-\sqrt{x}} dx$
6.  $\int_1^{\infty} \frac{dx}{\sqrt{x}+x\sqrt{x}}$
7.  $\int_{-1}^2 \frac{x}{(x+1)^2} dx$
8.  $\int_0^9 \frac{dx}{\sqrt[3]{x-1}}$
9.  $\int_0^4 \frac{dx}{x^2-x-2}$
10. $\int_0^1 \frac{e^{1/x}}{x^3} dx$

**Exercise 2. Исследовать на сходимость (используя тесты сходимости):**
1.  $\int_1^{\infty} \frac{x}{3x^4+5x^2+1} dx$
2.  $\int_2^{\infty} \frac{x^2-1}{\sqrt{x^6+16}} dx$
3.  $\int_0^{\infty} e^{-x^2} dx$
4.  $\int_1^{\infty} \frac{\ln x}{x+5}$

**Exercise 3. Исследовать поведение рядов:**
1.  $\sum_{n=1}^{\infty} \frac{e^{\arctan(n)}}{n^2+1}$
2.  $\sum_{n=2}^{\infty} \frac{1}{n\sqrt{\ln(n)}}$
3.  $\sum_{n=2}^{\infty} \frac{1}{n \ln^2(n)}$
4.  $\sum_{n=2}^{\infty} \frac{n}{e^{\sqrt{n}}}$
5.  $\sum_{n=2}^{\infty} \frac{1}{n \ln(n) \cdot (\ln(\ln(n)))^2}$

---

### 10. Приложения определенного интеграла (Applications)
**Вычисление площадей (Calculating Areas):**
*Найти площадь области, ограниченной кривыми:*
1.  $y = 4-x^2, \, y = -x+2, \, x=-2, \, x=3$
2.  $y = x^3+4x, \, x=-1, \, x=2$
3.  $y = \cos(2x), \, y=0, \, x=\pi/4, \, x=\pi/2$
4.  $y = -x^2+3x, \, y=2x^3-x^2-5x$
5.  $y = xe^{x^2}, \, y=2|x|$
6.  $y = |x^2-4|, \, y=(x^2/2)+4$

**Вычисление объемов (Calculating Volumes):**
*Найти объем тела вращения области вокруг указанной оси:*
1.  $y = e^x, \, y=0, \, x=0, \, x=\ln 3$ (вокруг оси x)
2.  $y = \frac{e^{3x}}{\sqrt{1+e^{6x}}}, \, x=0, \, x=1, \, y=0$ (вокруг оси x)
3.  $y = \sqrt{25-x^2}, \, y=3$ (вокруг оси x)
4.  $y = x^2, \, x=y^2$ (вокруг оси y)
5.  $x = 1-y^2, \, x=2+y^2, \, y=-1, \, y=1$ (вокруг оси y)
6.  $y = \sqrt{\frac{1-x^2}{x^2}} (x>0), \, x=0, \, y=0, \, y=1$ (вокруг оси y)

**Вычисление длины дуги (Calculating Lengths of Curves):**
1.  $y = \frac{1}{3}\sqrt{(x^2+2)^3}$ от $x=0$ до $x=3$
2.  $x = \frac{y^3}{3} + \frac{1}{4y}$ от $y=1$ до $y=3$
3.  $y = \frac{x^3}{3} + x^2 + x + \frac{1}{4(x+1)}$ от $x=0$ до $x=2$
4.  $x = (1+t)^2, \, y=(1+t)^3, \, 0 \le t \le 1$
5.  $x = e^t \cos t, \, y = e^t \sin t, \, 0 \le t \le \frac{\pi}{2}$
6.  $x = \cos t + t \sin t, \, y = \sin t - t \cos t, \, 0 \le t \le \pi$

**Вычисление площади поверхности (Calculating Areas of Surfaces):**
1.  $y = \sqrt{2x-x^2}, \, \frac{1}{2} \le x \le \frac{3}{2}$ (ось x)
2.  $x = \frac{1}{3}\sqrt{y^3} - \sqrt{y}, \, 1 \le y \le 3$ (ось y)
3.  $x = 2\sqrt{4-y}, \, 0 \le y \le \frac{15}{4}$ (ось y)
4.  $x = \frac{e^y+e^{-y}}{2}, \, 0 \le y \le \ln 2$ (ось y)
5.  $x = \sqrt[3]{y}, \, 1 \le t \le 8$ (ось x — *прим.: здесь видимо опечатка, должно быть $1 \le y \le 8$*)
6.  $y = \frac{x^3}{9}, \, 0 \le x \le 2$ (ось x)