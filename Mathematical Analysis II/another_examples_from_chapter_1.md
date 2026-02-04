Ниже представлен полный список всех **разобранных примеров (Examples)** из представленной первой главы (Chapter 1). Задачи сгруппированы по темам в порядке их появления в лекциях, что соответствует нарастанию сложности: от дифференциалов до несобственных интегралов и рядов.

---

### 1. Дифференциал и Первообразная (Differential & Antiderivative)
*Вводные примеры на определение дифференциала и проверку первообразной.*
1.  Найти дифференциал: $d(\tan x) = \frac{1}{\cos^2 x} dx$
2.  Найти дифференциал: $d(e^{\cos x + 5}) = -\sin x \cdot e^{\cos x + 5} dx$
3.  Проверка первообразной: $F(x) = \frac{1}{3}e^{x^3}$ для функции $f(x) = x^2 e^{x^3}$.
4.  Проверка первообразной: $F(x) = \frac{1}{10}(2x+1)^5 - \frac{1}{6}(2x+1)^3$ для функции $f(x) = x\sqrt{2x+1}$.
5.  Неопределенный интеграл (аналог примера 3): $\int x^2 e^{x^3} dx = \frac{1}{3}e^{x^3} + C$.
6.  Неопределенный интеграл (аналог примера 4): $\int x\sqrt{2x+1} dx = \dots$

### 2. Основные правила интегрирования (Basic Integration Rules)
*Примеры на подведение под знак дифференциала и табличные интегралы.*
7.  **Example 1:** $I_1 = \int \frac{\ln x}{x} dx = \frac{\ln^2 x}{2} + C$
8.  **Example 2:** $I_2 = \int \frac{dx}{x \ln^2 x} = -\frac{1}{\ln x} + C$
9.  **Example 3:** $I_3 = \int \frac{\arcsin x}{\sqrt{1-x^2}} dx = \frac{(\arcsin x)^2}{2} + C$
10. **Example 4:** $I_4 = \int (\sin x + \frac{1}{\sin^3 x} + \cos^2 x)\cos x \, dx$
11. **Example 5:** $I_5 = \int (\cos^2 x - 3^{4x} + \sqrt[3]{x} + \frac{5}{1+x^2}) dx$
12. **Example 6:** $I_6 = \int \frac{\sqrt{x^2-3} - 3\sqrt{x^2+3}}{\sqrt{x^4-9}} dx$

### 3. Метод подстановки (Integration by Substitution)
*От общих формул к конкретным вычислениям.*
13. **Example 1 (Общий вид):** $I_{ex1} = \int \frac{dx}{ax^2+bx+c}$
14. **Example 2 (Общий вид):** $I_{ex2} = \int \frac{\alpha x + \beta}{ax^2+bx+c} dx$
15. **Practical example:** $I = \int \frac{2x+5}{5x^2-2x-1} dx$
16. **Example 3:** $I_{ex3} = \int \frac{dx}{\sqrt{3x^2+5x-1}}$
17. **Example 4:** $I_{ex4} = \int \frac{x+3}{\sqrt{4x^2+4x+3}} dx$
18. **Example 5 (Метод Эрмита-Остроградского):** $I_{ex5} = \int \frac{1-x+x^2}{\sqrt{1+x-x^2}} dx$

### 4. Интегрирование по частям (Integration by Parts)
19. **Example 1:** $I = \int (x+5)\sin(2x+1) dx$
20. **Example 2:** $I = \int (x^2+5)\arctan x \, dx$
21. **Example 3 (Возвратный интеграл):** $I = \int e^x \sin x \, dx$
22. **Example 4:** $I = \int (2x^2+5x-1)\ln(3x) dx$

### 5. Интегрирование рациональных функций (Rational Functions)
23. **Example 1:** $I_1 = \int \frac{x^2+2}{(x+1)^3(x-2)} dx$
24. **Example 2:** $I_2 = \int \frac{x}{(x^2+1)(x-1)} dx$
25. **Example 3 (С заменой):** $I_3 = \int \frac{dx}{x^4(x^3+1)^2}$

### 6. Тригонометрические и гиперболические функции
26. **Example 1 (Универсальная подстановка):** $I_1 = \int \frac{dx}{1-\sin x}$
27. **Example 2:** $I_2 = \int \frac{dx}{\sin x + 2\cos x + 6}$
28. **Example 3:** $I_3 = \int \frac{\sin^3 x}{2+\cos x} dx$
29. **Example 4:** $I_4 = \int \frac{\cos^3 x}{\sin^4 x} dx$
30. **Example 5:** $I_5 = \int \sin^4 x \, dx$
31. **Example 6:** $I_6 = \int \frac{\sin^2 x}{\cos^6 x} dx$
32. **Example 7:** $I_7 = \int \cos^2(3x)\sin x \, dx$
33. **Example 1 (Гипербол.):** $I_1 = \int \frac{\cosh x + 2\sinh x - 1}{\sinh x(\cosh x - 3\sinh x - 1)} dx$
34. **Example 2 (Гипербол.):** $I_2 = \int \sinh x \sinh 7x \, dx$
35. **Example 3 (Гипербол.):** $I_3 = \int \sinh^3 x \, dx$

### 7. Иррациональные функции и Подстановки (Radical Functions & Transformations)
36. **Example 1:** $I_1 = \int \frac{\sqrt{x}}{\sqrt[4]{x^3+1}} dx$
37. **Example 2:** $I_2 = \int \frac{\sqrt{x-4}}{x} dx$
38. **Example 1 (Триг. замена):** $I_1 = \int \frac{\sqrt{25-x^2}}{x} dx$ (замена $x=5\sin t$)
39. **Example 2 (Гипербол. замена):** $I_2 = \int \sqrt{x^2-4} dx$ (замена $x=2\cosh t$)

### 8. Теорема Ньютона-Лейбница (FTC & Definite Integrals)
40. **Example 1 (Производная интеграла):** Найти $\frac{dy}{dx}$ для $y = \left(\int_0^x (t^3+1)^{10} dt\right)^3$
41. **Example 2 (Производная интеграла):** Найти $\frac{dy}{dx}$ для $y = x \int_2^{x^2} \sin(t^3) dt$
42. **Example 1 (Замена в определенном интеграле):** $I_1 = \int_0^2 \frac{5x}{(4+x^2)^2} dx$
43. **Example 2:** $I_2 = \int_0^1 \arctan(\sqrt{x+3}) dx$
44. **Example 3 (MIT Integration Bee):** $I_3 = \int_0^2 \sqrt{x + \sqrt{x + \sqrt{x + \dots}}} \, dx$

### 9. Приложения определенного интеграла (Applications)
**Площадь (Area):**
45. **Example:** Площадь между осью x и графиком $f(x) = x^3 - x^2 - 2x, -1 \le x \le 2$.
46. **Example 1:** Площадь области между параболой $y = 2-x^2$ и прямой $y=-x$.
47. **Example 2:** Площадь области между кривыми $y=\sin x, y=\cos x$ при $x=0$ и $x=\pi/2$.

**Объем (Volume):**
48. **Example:** Вывод формулы объема правильной пирамиды с высотой $h$ и квадратным основанием со стороной $a$.
49. **Example 1:** Вывод формулы объема шара радиуса $r$.
50. **Example 2:** Объем тела вращения области между $f(x) = \frac{1}{2}+x^2$ и $g(x)=x$ на $[0,2]$ вокруг оси x.
51. **Example 3:** Объем тела вращения области $y=\sqrt{x}, y=2, x=0$ вокруг оси y.

**Длина дуги (Arc Length):**
52. **Example 1:** Длина графика $y = \frac{4\sqrt{2}}{3}x^{3/2}-1$ на $0 \le x \le 1$.
53. **Example 2:** Длина кривой $y = \sqrt[3]{(x/2)^2}$ на $0 \le x \le 2$.

**Площадь поверхности (Surface Area):**
54. **Example 1:** Площадь поверхности вращения $y=x^3$ ($0 \le x \le 1$) вокруг оси x.
55. **Example 2:** Площадь поверхности вращения $y=x^2$ ($1 \le x \le 2$) вокруг оси y.

### 10. Несобственные интегралы и Ряды (Improper Integrals & Series)
**Вычисление и сходимость:**
56. **Example 1:** $\int_1^{\infty} \frac{\ln x}{x^2} dx$ (Интегрирование по частям).
57. **Example 2:** $\int_{-\infty}^{\infty} \frac{dx}{1+x^2}$ (Разбиение на два интервала).
58. **Example 3:** Исследование интеграла $I_p = \int_1^{\infty} \frac{dx}{x^p}$ в зависимости от $p$.
59. **Example 1 (Тип II, разрыв):** $\int_1^2 \frac{dx}{1-x}$ (Расходится).
60. **Example 2 (Тип II, разрыв):** $\int_1^2 \frac{dx}{(x-2)^{2/3}}$ (Сходится).

**Тесты сходимости (Comparison Tests):**
61. **Example 1:** $\int_1^{\infty} e^{-x^2} dx$ (Сравнение с $e^{-x}$).
62. **Example 2:** $\int_1^{\infty} \frac{\sin^2 x}{x^2} dx$ (Сравнение с $1/x^2$).
63. **Example 3:** $\int_1^{\infty} \frac{dx}{\sqrt{x^2-1}}$ (Сравнение с $1/x$).
64. **Example 1 (Limit Comparison):** $I_1 = \int_1^{\infty} \frac{dx}{1+x^2}$.
65. **Example 2:** $I_2 = \int_1^{\infty} \frac{1-e^{-x}}{x} dx$.
66. **Example 3:** $\int_0^{\infty} \frac{x^2}{4x^4+5x+25} dx$.
67. **Example 4:** $\int_0^{\infty} \frac{x}{\sqrt{x^4+x^2+2}} dx$.

**Интегральный признак Коши (Cauchy Integral Test):**
68. **Example 1:** Ряд $\sum \frac{1}{n^p}$ (p-series).
69. **Example 2:** Ряд $\sum_{n=1}^{\infty} \frac{1}{\sqrt{n}e^{\sqrt{n}}}$ (Исследование через интеграл).
70. **Example 3:** Ряд $\sum_{n=2}^{\infty} \frac{2^{\ln(\ln n)}}{n \ln n}$.