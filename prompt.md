## **Task Overview**

You will transform source material (presentations transcript) into a complete Quarto document (.qmd). Your output MUST:
- Cover ALL topics from the source material
- Be fully understandable for students who did NOT attend the lecture
- Explain concepts from scratch with sufficient context and detail
- Follow the exact structure and formatting specified below

**Work incrementally but comprehensively:** Write the document in logical parts to prevent errors, but ensure you cover ALL material in total.

---

## **Document Structure Requirements**

### **YAML Header** (REQUIRED)

```yaml
---
title: "W[X]. [Topic 1], [Topic 2], [Topic 3]"
author: "[Author of course]"
date: "[Current date in 'MMMM D, YYYY' format]"
format: html
engine: knitr
---
```

**Rules:**
- Title MUST be a comma-separated list of main topics
- Date MUST use full month name (e.g., "November 6, 2025")

---

### **Section 1: Summary** (REQUIRED)

Start with: `#### **1. Summary**`

#### **Heading Structure**
- Use `#####` for main subsections: `##### **1.1 Topic Name**`
- Use `######` for nested subsections: `###### **1.1.1 Subtopic**`
- Make headings **concise, descriptive titles** (e.g., `##### **1.1 Vectors**`), NOT questions
- Do NOT format this heading as a list item

#### **Content Requirements**
1. **Explain for absolute beginners:** Write as if the reader has never encountered this topic
2. **Define key terms comprehensively:**
   - Provide clear, concise definitions
   - Add sufficient context, details, and analogies
   - Explain WHY concepts matter, not just WHAT they are
   - Avoid jargon without first explaining it
3. **Use formatting for emphasis:**
   - **Bold** for key terms on first introduction
   - *Italics* for important concepts or emphasis
4. **Include diagrams where helpful:**
   - Insert `<!-- DIAGRAM HERE -->` comment where a visual would aid understanding
   - Do NOT mention the diagram in surrounding text
   - The comment should appear on its own line with blank lines above and below
5. **Mathematical expressions:**
   - Use LaTeX: `$...$` for inline math, `$$...$$` for display math
   - NEVER use single backticks for math (even single variables)
6. **Correct errors and enhance clarity:**
   - Fix any mistakes in source material
   - Add missing formulas where needed
   - Restructure for better pedagogical flow if necessary

#### **Lists in Summary**
- ALWAYS precede lists with a blank line
- Keep list items concise but complete

---

### **Section 2: Definitions** (REQUIRED)

Start with: `#### **2. Definitions**`

Provide a bulleted list of essential terms with concise, precise definitions:
```
*   **Term**: Clear, complete definition.
*   **Another Term**: Definition with necessary context.
```

**Rules:**
- Include ALL key terms introduced in the summary
- Definitions should be self-contained (understandable without reading the summary)
- Bold the term name only

---

### **Section 3: Formulas** (REQUIRED FOR MATH)

Start with: `#### **3. Formulas**`

Provide a bulleted list of formulas relevant for problem-solving:
```
*   **Formula Name**: $formula$ (with conditions if applicable)
*   **Another Formula**: $$display\_formula$$
```

**Critical Rules:**
- Write GENERAL formulas useful for exams, not example-specific formulas
- Include all formulas a student would need to memorize/reference
- Provide formula names or descriptions
- Include domain restrictions or conditions where applicable

---

### **Section 4: Examples** (REQUIRED) (SECTION 3 IF FORMULAS MISSING)

Start with: `#### **4. Examples**`

#### **Problem Selection**
You MUST include:
1. ALL explicit problems/exercises from source material
2. Examples that appear as demonstrations (reformulate as problems)
3. Lecture examples, tutorial problems, lab exercises, and any additional tasks

#### **Organization**
Sort problems in this order:
1. Lecture examples
2. Tutorial problems
3. Lab exercises
4. Other additional tasks

Within each category, sort in ascending numerical order.

#### **Format for Each Example**

```markdown
##### **4.[N]. [Problem Title]** ([Source], [Location])

[Clear problem statement exactly as in source]

<details>
<summary>Click to see the solution</summary>

[Optional: **Key Concept:** Brief explanation of the main idea or technique]

[Solution with clear step-by-step explanation]

1.  **Step Name:** Explanation and calculation
2.  **Next Step:** Continue with numbered steps
    *   Use sub-bullets for details within a step
    *   Show all work clearly

[For problems with multiple parts, use **(a)**, **(b)**, etc.]

**Answer:** [Final answer clearly stated]

</details>
```

#### **Example Source Attribution Format**
- `(Lecture [N], Example [M])`
- `(Tutorial [N], Problem [M])`
- `(Lab [N], Problem [M])`
- `(Lab [N], Exercise [M])`

#### **Solution Requirements**
1. **Start with context:** If helpful, provide a "Key Concept" section explaining the approach
2. **Number steps clearly:** Use sequential numbering for main steps
3. **Show all work:** Don't skip algebraic steps or logical reasoning
4. **Explain as you go:** Each step should include WHY you're doing it, not just WHAT
5. **Format final answers clearly:** Use bold "**Answer:**" followed by the result
6. **For code examples:**
   - Include complete, runnable code
   - Add detailed comments explaining each section
   - Use proper language tags in code blocks (e.g., ```java, ```c, ```python)

---

## **Formatting Rules**

### **Mathematics**
- **Inline math:** Use `$expression$` (e.g., `$x^2 + 1$`)
- **Display math:** Use `$$expression$$` for centered formulas
- **NEVER** use single backticks for math expressions, even single characters

### **Code**
- Use single backticks **only** for: inline code, variables, functions, file paths
- Use code blocks with language tags for full code examples:
  ````
  ```language
  code here
  ```
  ````

### **Lists**
- ALWAYS precede lists with a blank line
- This applies to bulleted lists, numbered lists, and nested lists

### **Spacing**
- Do NOT add unnecessary blank lines between headings
- DO add blank lines before lists and code blocks
- Add blank lines around `<!-- DIAGRAM HERE -->` comments

### **Images** (if applicable)
- Reference images with: `![](filename.png){width=80%}`
- Use relative paths only

---

## **Complete Example**

```qmd
---
title: "W8-W9. Vector Addition, Scalar Multiplication"
author: "Zakhar Podyakov"
date: "September 18, 2025"
format: html
engine: knitr
---

{{< video 8.mp4 >}}

[Quiz](https://example.com/quiz) | [Flashcards](https://example.com/flashcards)

#### **1. Summary**
##### **1.1 Introduction to Vectors**
A **vector** is a mathematical object possessing both magnitude (length) and direction. Unlike a **scalar**, which is just a number (like temperature: 20°C), a vector tells you both "how much" and "which way." Think of a vector as an instruction: "move 5 meters north" contains both a distance (magnitude) and a direction.

###### **1.1.1 Geometric Representation**
Visually, we represent a vector as an arrow. The arrow's length represents the vector's magnitude, and the direction the arrow points represents its direction.

<!-- DIAGRAM HERE -->

###### **1.1.2 Algebraic Representation**
Mathematically, we write vectors as ordered lists of numbers called **components**. In 2D space (denoted $\mathbb{R}^2$), a vector has two components:
$$ \vec{v} = \begin{pmatrix} x \\ y \end{pmatrix} $$

##### **1.2 Vector Operations**
We can perform arithmetic operations on vectors.

###### **1.2.1 Vector Addition**
To add two vectors, add their corresponding components:
$$ \vec{u} + \vec{v} = \begin{pmatrix} u_1 + v_1 \\ u_2 + v_2 \end{pmatrix} $$

Geometrically, use the **tip-to-tail method**: place the tail of the second vector at the tip of the first. The result goes from the tail of the first to the tip of the second.

<!-- DIAGRAM HERE -->

###### **1.2.2 Scalar Multiplication**
To multiply a vector by a scalar (number), multiply each component:
$$ c\vec{v} = \begin{pmatrix} cv_1 \\ cv_2 \end{pmatrix} $$

This **scales** the vector: if $c = 2$, the vector doubles in length. If $c = -1$, it flips direction.

#### **2. Definitions**
*   **Vector**: A mathematical object with both magnitude and direction.
*   **Scalar**: A quantity described by a single number, with magnitude but no direction.
*   **Components**: The numerical values that define a vector's position in each dimension.
*   **Magnitude (Norm)**: The length of a vector, calculated as $||\vec{v}|| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$.

#### **3. Formulas**
*   **Vector Addition**: $\vec{u} + \vec{v} = \begin{pmatrix} u_1 + v_1 \\ u_2 + v_2 \end{pmatrix}$
*   **Scalar Multiplication**: $c\vec{v} = \begin{pmatrix} cv_1 \\ cv_2 \end{pmatrix}$
*   **Vector Subtraction**: $\vec{u} - \vec{v} = \begin{pmatrix} u_1 - v_1 \\ u_2 - v_2 \end{pmatrix}$
*   **Norm of a Vector**: $||\vec{v}|| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$
*   **Unit Vector**: $\hat{v} = \frac{\vec{v}}{||\vec{v}||}$

#### **4. Examples**
##### **4.1. Find the Sum of Two Vectors** (Lecture 8, Example 1)
Given $\vec{u} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$, find $\vec{u} + \vec{v}$.

<details>
<summary>Click to see the solution</summary>

**Key Concept:** To add vectors, add corresponding components.

1.  **Add the first components:** $3 + 1 = 4$
2.  **Add the second components:** $-2 + 4 = 2$
3.  **Form the result vector:**
    $$ \vec{u} + \vec{v} = \begin{pmatrix} 4 \\ 2 \end{pmatrix} $$

**Answer:** $\begin{pmatrix} 4 \\ 2 \end{pmatrix}$

</details>

##### **4.2. Calculate Vector Magnitude** (Tutorial 8, Problem 3)
Find the magnitude of $\vec{w} = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$.

<details>
<summary>Click to see the solution</summary>

1.  **Apply the magnitude formula:** $||\vec{w}|| = \sqrt{w_1^2 + w_2^2}$
2.  **Substitute values:** $||\vec{w}|| = \sqrt{(-3)^2 + 4^2}$
3.  **Calculate:**
    *   $||\vec{w}|| = \sqrt{9 + 16} = \sqrt{25} = 5$

**Answer:** 5

</details>

##### **4.3. Scalar Multiplication and Direction** (Lab 9, Exercise 2)
Given $\vec{a} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, find:

a) $3\vec{a}$
b) $-2\vec{a}$

<details>
<summary>Click to see the solution</summary>

**Key Concept:** Scalar multiplication scales the vector. Positive scalars keep the direction; negative scalars reverse it.

**(a) $3\vec{a}$:**
1.  **Multiply each component by 3:**
    $$ 3\vec{a} = \begin{pmatrix} 3(2) \\ 3(1) \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \end{pmatrix} $$

**(b) $-2\vec{a}$:**
1.  **Multiply each component by -2:**
    $$ -2\vec{a} = \begin{pmatrix} -2(2) \\ -2(1) \end{pmatrix} = \begin{pmatrix} -4 \\ -2 \end{pmatrix} $$

**Answer:**

a) $\begin{pmatrix} 6 \\ 3 \end{pmatrix}$
b) $\begin{pmatrix} -4 \\ -2 \end{pmatrix}$

</details>
```

---

## **After Completion**

**For mathematics courses ONLY:** After generating the guide, update the `0.qmd` file in the same folder:
1. Add all new general formulas from your guide's "Section 3: Formulas"
2. Organize them under appropriate category headings
3. Follow the same formatting style as existing entries in `0.qmd`

**For non-mathematics courses:** No action needed.

---

## **Key Principles**

1. **Completeness:** Cover EVERY topic from source material
2. **Clarity:** Write for students learning independently
3. **Structure:** Follow the exact format specified
4. **Accuracy:** Correct errors, verify formulas, ensure mathematical rigor
5. **Pedagogical quality:** Explain WHY, not just WHAT
6. **Consistency:** Maintain formatting throughout the entire document

---

| Course | Author(s) |
|:-------|:----------|
| Academic Writing and Argumentation I–II | Georgy Gelvanovsky |
| Analytical Geometry and Linear Algebra I–II | Salman Ahmadi-Asl |
| Mathematical Analysis I–II | Mohammad Alkousa |
| Data Structures and Algorithms | Nikolai Kudasov |
| Software Systems Analysis and Design | Eugene Zouev, Munir Makhmutov |
| Theoretical Computer Science | Manuel Mazzara |
| Computer Architecture | Artem Burmyakov |
| Introduction to Programming | Eugene Zouev, Munir Makhmutov |
| Logic and Discrete Math | Andrey Frolov |



1. Example vs Task
Example = профессор показывает решение (демонстрационный пример из лекции)
Task = студент решает самостоятельно (Lab, Tutorial, Assignment, Problem Set)

2. Порядок секций внутри #### **N. Examples**
Lab → Assignment/Problem Set → Lecture/Chapter → Tutorial → Test/Midterm/Final Recap → Mock Test/Midterm/Final → Test/Midterm/Final

3. Нумерация Source без номера
Если в скобках написано (Source, ...) без номера — заменить на (Source N, ...) где N = номер недели.

4. Bare Task без источника
Если пример помечен только как (Task X.Y) без указания источника (Lab/Lecture/Tutorial) — установить правильный источник, спросив у меня какой источник.

5. Renumber после изменений
После добавления или перестановки примеров всегда запускать:

python renumber_examples.py "semester-X/Subject/N.qmd" [--format "4.{}"]
Флаг --format нужен если prefix не 4 (например 3.{} для файлов где секция Examples = #### **3. Examples**).

6. Регенерация ai_artifacts_review
После всех изменений в оригинальных файлах запустить:

python fix_formatting.py
ai_artifacts_review генерируется автоматически — его руками не трогать.

7. Исключения
Mathematical Analysis II / 1.qmd — не трогать порядок (400 примеров, нумерация по категориям намеренная).

8. Формат заголовка примера

##### **N.M. Descriptive Title** (Source, Type Number)
Где:

N = номер секции Examples в файле (обычно 4, иногда 3)
M = порядковый номер примера (после renumber)
Source = Lab N, Assignment N, Lecture N, Tutorial N, Problem Set N, Midterm YYYY и т.д.
Type = Task или Example (по правилу 1)

9. Структура примера

##### **N.M. Title** (Source, Task/Example K)

Problem statement.

<details>
<summary>Click to see the solution</summary>

**Key Concept:** ...

1. Step
2. Step

**Answer:** ...

</details>

10. Язык
Все примеры — на английском, профессиональный академический стиль, LaTeX для математики.