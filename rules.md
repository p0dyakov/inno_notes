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
