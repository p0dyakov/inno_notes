Заголовок такого формата:
```
---
title: "W12. Introduction to Vector Calculus"
author: "Mohammad Alkousa"
date: "April 22, 2026"
format: html
engine: knitr
---
```
Есть неделя W<N> где <N> номер недели
Разрешено W<N>-W<X>; W<N>A; W<N>B

Есть 
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

Для некоторых разделов могут отстутствовать
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

Другие заголовки этого уровня запрещены

Practice пишется ТОЛЬКО если в исходниках недели есть явные нумерованные
задачи/примеры (Task/Example/Exercise/Problem с номером). Нет явных задач —
секция опускается целиком, выдумывать задачи запрещено.

MA I/II содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

SSAD содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Practice** - тут именно 3

ITP содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Practice** - тут именно 3

TCS содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

DSA содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

AGLA I/II содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

AWA содержит
#### **1. Theory**

LDM содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Formulas**
#### **4. Practice**

CA содержит
#### **1. Theory**
#### **2. Definitions**
#### **3. Practice** - опционально

все заголовки не попадающие под правило должны быть отмечены в отчёте

Разделители `---` (а также `***`, `___`, `<hr>`) разрешены ТОЛЬКО между
секциями верхнего уровня `#### **N. ...**` — непосредственно перед
следующим `####`. Внутри секций разделители запрещены: в Theory между
`##### 1.x` подразделами их нет, подразделы отделяются только заголовками.
Нарушение отмечается в отчёте (проверка действует для семестров
с `course_map.json`; semester-1/2/3 заморожены и не проверяются).


Каждый пример имеет формат

##### **4.1. Calculate Triple Integrals** (Lab 12, Task 1)
##### **<N>.1. <Title>** (<Source> <X>, Task 1)

N - 3/4
. после в конце номера обязательна
<Title> не содержит Lecture, Chapter, Lab и тд, не содержит Slide, Slide
**4.1. Calculate Triple Integrals** выделено ** 
<Source> может быть только Lab, Lecture, Tutorial, Chapter, Midterm, Final, Test, Homework
<X>
для Lab, Lecture, Tutorial X - это должен быть номер файла
Для Test - римская I/II
Для Midterm Final разрешён год 2025 например
Другие названия source запрещены
<X> обязан указывать на реально существующий файл транскрипта недели:
`(Lecture 1, …)` требует `Lecture*.md`, `(Tutorial 1, …)` — `Tutorial*.md`,
`(Lab 1, …)` — `Lab.md`, `(Chapter 1, …)` — `Chapter.md` и т.д.
(детерминированный гейт `validate_practice_sources.py`: однозначные
перепутанные виды чинятся сами, неоднозначные уводят статью в карантин).
Если в исходниках недели такого вида файла нет — такой source запрещён,
выдумывать номера задач/примеров под несуществующий источник нельзя.
Для Chapter-источников без нумерованных задач номера Task — сквозные
внутри статьи (self-checks), это нормально

### 404.qmd - игнорируем
### index.qmd - игнорируем
.ru файлы временно игнорируем

внутри summary могут быть вложенные заголовки разных уровней, но обязательно большего уровня, чем ####, то есть #####, ###### и тд

заголовок, который идёт после Theory должен быть либо ##### 1.1 либо ###### 1.1.1


### Pre-bake: новые .qmd выпекаются заранее и отдельно
Сломанная страница роняет весь deploy-site, поэтому каждый новый или
изменённый `.qmd` обязан быть полностью испечён ДО пуша, отдельно от общей
сборки сайта:
`python3 scripts/agent/prebake.py [файлы...]` — без аргументов берёт
новые/изменённые `.qmd` против `origin/main`. Проверяет fix_formatting без
нарушений именно по этим файлам, затем делает полный `quarto render`
каждого файла. Ненулевой exit = пушить нельзя.
`pre-push`-хук гоняет быструю проверку (`--format-only`); полная выпечка —
на Windows/dev-машине или в CI.

### Machine-checkable bans (fix_formatting gate)

- ASCII-art diagrams are banned: a fenced block whose lines are mostly
  box-drawing/dash-pipe compositions is a violation, not a style choice.
  Redraw as mermaid/tikz per exemplars.
- Equation tags must be unique (any style): duplicates are renumbered
  deterministically and stale (N) references remapped before validation.
- Textual cross-references (`equation (N)`, `Eq. (N)`, ranges) must point at
  an existing `\tag{N}` in the same file — dangling refs are gate violations.
- Every ` ```{tikz} ` figure must carry `#| echo: false` (or `%|` style),
  otherwise Quarto prints the tikz source as a code listing above the figure.
- Lists are always tight: no blank lines between items of one list; item
  math (`$$` lines, even labeled/multiline), continuation paragraphs and
  nested sublists attach directly (indented, no blank line). Blank lines
  inside a list force a loose list with gaps between items.
- Practice items are only `Example` (teacher demonstrates) or `Task`
  (student assignment): source labels like `(Tutorial 1, Task 2)` or
  `(Lab 5, Example)`. `Problem`, `Practice Task(s)`, `Exercise` and any
  other kinds are violations, not style choices.
- ATX headings start their own line with a blank line before (auto-fixed);
  a `$$` paragraph must pair within itself (unpaired `$$` and `rotate=`
  text in tikz are gate violations). Figures stay readable: horizontal
  labels with clearance or white chips, legend box when crowded, tight
  bounding box, fig-height at most 3.5 (plus a CSS max-height backstop).

### Banned: Pitfalls blocks (fix_formatting gate)

- Pitfalls are banned in ALL forms: `#####`/`######` headings containing
  "Pitfall(s)" and bullets starting with **Key/Common Pitfall(s):**.
  Never write them. If a violation flags one, delete the entire block:
  heading/bullet plus body up to the next heading (nested list for bullets).

