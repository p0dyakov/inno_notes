Here is the complete, line-by-line transcript of the problem statements extracted from the provided files, translated and formatted entirely in English as requested. All interface elements, menus, and sidebars have been ignored to focus solely on the problem content.

***

# File 1: Problem A

## Page 1

**A. The Spectacular Photo**
time limit per test: 1.5 seconds
memory limit per test: 256 megabytes

Astronomers observed $N$ shooting stars streaking across the night sky. Some of them happen to align along a secret "cosmic path" — which **at least** a quarter of the stars lie along it.

Your task is to figure out the straight line along which the most shooting stars travel, so you can capture a spectacular photo!

**Input**
The first line contains a single integer $N$ ($4 \le N \le 10^6$) — the number of shooting stars.

Each of the following $N$ lines contains two integers $x_i$ and $y_i$ ($-10^9 \le x_i, y_i \le 10^9$) — the coordinates of the $i$-th star.

**Output**
On the first line, print an integer $K$ — the maximum number of points that lie on a single straight line.

On the next line print $K$ integers $ind_1, ind_2, ..., ind_K$ — the indices of the points that lie on this line, in ascending order (sorted by index).

Note that if multiple lines pass through the same maximum number of points, then any valid line may be reported, also note that indexing starts from $1$.

**Example**

**input**
```text
8
-4 -4
2 2
3 7
-4 1
0 5
1 -7
-3 -4
3 3
```

**output**
```text
3
1 2 8
```

**Note**
In the first test case, it can be shown that the optimal answer is a line that passes through the points $(-4, -4)$, $(2, 2)$, and $(3, 3)$, which correspond to the indices $1$, $2$, and $8$, respectively.

## Page 2

> **Image Description:** 
> The image displays a 2D Cartesian coordinate system with a solid black vertical y-axis and a solid black horizontal x-axis. A solid red diagonal line passes through three points plotted in red: $(-4, -4)$, $(2, 2)$, and $(3, 3)$. There are four other points scattered on the graph, each marked with a different color:
> *   $(-4, 1)$ plotted in blue.
> *   $(0, 5)$ plotted in green.
> *   $(-3, -4)$ plotted in black.
> *   $(1, -7)$ plotted in purple.
> 
> Below the graph, there is a caption that reads: "The plot of the points in the first test case."

*(No other problem text is present on this page, only the image and interface elements.)*

## Page 3
*(No problem text present on this page.)*

***

# File 2: Problem B

## Page 1

**B. Almost Unbiased**
time limit per test: 1 second
memory limit per test: 256 megabytes

A university maintains a database of student records. Each record contains:
*   ID — a unique integer identifying the student.
*   Full name — two strings (first name and last name).
*   Gender — a character.
*   Age — an integer.

The database is implemented using a **Binary Search Tree (BST)** ordered by ID.

The initial records may be inserted into the BST in **any order** you choose.

A group of data science experts obtained a copy of the university database in order to perform statistical analysis on the students, and they are trying to obtain an unbiased dataset.

The experts perform $M$ operations. Each operation is one of the following:

*   `insert <ID> <first name> <last name> <gender> <age>` — Add a new student record (from an old database the experts have) to the current database. It is guaranteed that the ID does not already exist and it is **randomly** generated.
*   `remove <ID>` — Remove the student record with the given ID if it exists. It is guaranteed that the ID is **randomly** generated.

After performing these operations, the experts perform $Q$ search queries:

*   `search <ID>` — print the record associated with the given ID.

Your task is to simulate this system and answer the search queries.

**Notes:**
*   You are **not** allowed to use rotations or any self-balancing tree structure.
*   At the beginning of your source code, include a short comment (2–3 sentences) explaining the strategy you use to determine the order in which the IDs are inserted into the BST, and why this approach helps keep the tree efficient.

**Input**
The first line contains three integers, $N$, $M$, and $Q$ — the number of initial records, the number of insert/remove operations, and the number of search queries, respectively.

Each of the following $N$ lines contains a student record with the following format:
*   `<ID> <first_name> <last_name> <gender> <age>`

Each of the following $M$ lines contains one of the following queries:
*   `insert <ID> <first_name> <last_name> <gender> <age>` — Add a new student record to the database.
*   `remove <ID>` — Remove the student record with the given ID if it exists.

Each of the following $Q$ lines contains a search query with the following format:

## Page 2

*   `search <ID>` — Print the record information of the given ID if it exists.

**Constraints:**
*   $(1 \le N, M, Q \le 10^5)$
*   $(1 \le ID \le 10^9)$
*   first_name and last_name are strings consisting of English letters and $(3 \le |first\_name|, |last\_name| \le 11)$
*   gender is a character (either `"M"` or `"F"`).
*   $(17 \le age \le 30)$.

It's guaranteed that no two records in the database have the same ID at the same time.

**Output**
Print $Q$ lines where the $i$-th line answers the $i$-th search query. If the ID doesn't exist, print "`NOT FOUND`". Otherwise print the record information with the following format:

*   `<first name> <last name> <gender> <age>`

**Example**

**input**
```text
3 4 3
1 Ivan Ivanov M 21
2 Alexender Alexenderov M 19
3 Maria Marianova F 23
insert 10 Alma Stepanova F 20
remove 5
insert 429 Andrei Korolev F 19
remove 2
search 429
search 3
search 2
```

**output**
```text
Andrei Korolev F 19
Maria Marianova F 23
NOT FOUND
```

**Note**
In the first test case, the initial database contains $3$ records with the following IDs: $[1, 2, 3]$.

Let's consider the state of the database after each operation:

*   `insert 10 Alma Stepanova F 20`
    $\rightarrow$ a new record will be added: $[1, 2, 3, 10]$.
*   `remove 5`
    $\rightarrow$ nothing will happen since ID $5$ doesn't exist in the database.
*   `insert 429 Andrei Korolev F 19`
    $\rightarrow$ a new record will be added: $[1, 2, 3, 10, 429]$.
*   `remove 2`
    $\rightarrow$ the record with ID $2$ will be removed, so the final state of the database: $[1, 3, 10, 429]$.

Now let's consider the search queries:

*   `search 429`
    $\rightarrow$ `Andrei Korolev F 19`
*   `search 3`
    $\rightarrow$ `Maria Marianova F 23`
*   `search 2`
    $\rightarrow$ `NOT FOUND`

## Page 3
*(No problem text present on this page.)*

***

# File 3: Problem C 
*(Note: Originally in Russian, translated entirely to English as requested)*

## Page 1

**C. Lord of the Matrices**
time limit per test: 1.3 seconds
memory limit per test: 256 megabytes

You are given 3 matrices of size $N \times N$: $A$, $B$, and $C$.

Your task is to determine whether it is true that $A \times B = C$ in $O(N^2)$ time, in order to confirm your status as the **lord of the matrices**.

**Input data**
The first line contains an integer $N$ ($1 \le N \le 1500$).

Then follows matrix $A$.

Then follows matrix $B$.

Then follows matrix $C$.

Each matrix is given by $N$ lines, in each of which there are $N$ integers ($0 \le M_{ij} \le 10^9$, $M \in \{A, B, C\}$), separated by spaces.

**Output data**
Print `Yes` if $A \times B = C$. Otherwise, print `No`.

**Example**

**input**
```text
5
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
```

**output**
```text
Yes
```

**Note**
In the first test $B$ is an **identity matrix** and since $A = C$, then $A \times B = C$ is true.

## Page 2
*(No problem text present on this page.)*

## Page 3
*(No problem text present on this page.)*