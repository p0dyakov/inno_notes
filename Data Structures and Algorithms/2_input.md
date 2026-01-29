<!-- Here is the transcribed and formatted content from the provided PDF documents, organized by file and page/slide.

# File 1: Topic 2. Problem set (theory)

### Page 1

**Header:** Innopolis University | Data Structures and Algorithms (Spring 2025)

**Topic 2. Problem set (theory)**

**Problem 2.1.** Consider taking a list/stack/queue $A$ and producing a new list/stack/queue that has the same elements in reverse order, by only using the corresponding ADT methods (you are not allowed to rely on a particular implementation). Write down a pseudocode for efficient `reverse` method performing in $O(n)$ for the case when:

1.  $A$ is a `DoublyLinkedList` (you can only use List ADT methods).

For each of the following write down the time complexity of `reverse` and briefly (1–2 sentences) justify your analysis.

2.  $A$ is an `ArrayList` (you can only use List ADT methods)
3.  $A$ is a `LinkedList` without a tail pointer (you can only use List ADT methods)
4.  $A$ is a `LinkedList` with a tail pointer (you can only use List ADT methods)
5.  $A$ is an `ArrayStack` (you can only use Stack ADT methods)
6.  $A$ is a `LinkedStack` (you can only use Stack ADT methods)
7.  $A$ is an `ArrayQueue` (you can only use Queue ADT methods)
8.  $A$ is a `LinkedQueue` (you can only use Queue ADT methods)

**Problem 2.2.** Suggest an implementation of a queue using two stacks:
1.  Write down in text the main idea of your representation.
2.  Write down pseudocode for the two main queue methods:
    *   `offer(x)`
    *   `poll()`
3.  Briefly justify correctness for each method.
4.  Write down asymptotic worst case time complexity for each method.
5.  Briefly justify asymptotic complexities for each method.

**Problem 2.3.** Let $A$ be an array of $n$ integers. Show how to effectively compute in how many ways it is possible to select $k$ elements of $A$ such that their sum is equal to $m$:
1.  Write down in text the main idea for a **brute force** algorithm that counts all subsets $I \subseteq \{1, \dots, n\}$ of size $k$ such that $\sum_{i \in I} A[i] = m$. You may use iterative or recursive approach.
2.  Write down pseudocode of the algorithm.
3.  Compute the asymptotic time complexity of the algorithm and briefly justify it.

**References**
[CLRS] Cormen, T.H., Leiserson, C.E., Rivest, R.L. and Stein, C., 2022. *Introduction to algorithms, Fourth Edition*. MIT press.

***

# File 2: Lecture 2 Slides

### Slide 1
**Title:** Data Structures and Algorithms
**Subtitle:** Lecture 2. Elementary Data Structures. Recursion and Backtracking.
**Speaker:** Nikolai Kudasov
**Affiliation:** Lab of programming languages and compilers, Innopolis University

### Slide 2: Objectives
Today you will learn and be able to:
1.  describe what an Abstract Data Type and Data Structure are
2.  recall List, Stack, and Queue ADTs and their implementations
3.  compute time complexity of operations for those implementations
4.  reproduce time complexity analysis of those operations
5.  implement and analyse simple recursive algorithms
6.  replace recursion with loops and explicit stack
7.  implement recursion with backtracking

For more on today’s topic, see:
*   Cormen et al. 2022, §10.1–10.3
*   Goodrich, Tamassia, and Goldwasser 2014, §6–7

### Slide 3: Outline
*   Abstract Data Types and Data Structures
*   Lists
*   Stacks
*   Queues
*   Recursion
*   Recursion vs Explicit Stack
*   Brute Force and Backtracking
*   Backtracking

### Slide 4
**Abstract Data Types and Data Structures**

### Slide 5: Abstract Data Types
**Abstract Data Type (ADT)** is a mathematical model of a data type:
ADT determines:
1.  **operations** and **constructors** available for values of a given type
2.  **type signature of operations**: what types of values the operations take as input and return as output
3.  **properties (laws)** that the operations must adhere to

Intuitively, ADT is an “interface”.

### Slide 6-7: Abstract Data Type (examples)
**"Number"** can be seen as an ADT:
1.  **operations:** construct zero/one/etc., add two numbers ($+$), ...
2.  **operation signatures:** addition ($+$) takes two numbers and returns another number, ...
3.  **properties:** for any numbers $x, y$ we have $x + y = y + x$, ...

**Sets** can be seen as ADTs:
1.  **operations:** construct an empty set, construct a singleton set, make a union ($\cup$) of two sets, ...
2.  **operation signatures:** union ($\cup$) takes two sets and returns another set, ...
3.  **properties:** for any sets $x, y$ we have $x \cup y = y \cup x$, ...

### Slide 8: Data Structures
**Data Structure** is a concrete data representation and implementation for the operations.

*   Intuitively, **ADT** is an “interface”.
*   Intuitively, **data structure** is a concrete implementation of an ADT.

### Slide 9-10: Data Structures (examples)
Class `java.math.BigDecimal` is a data structure, implementing arbitrary-precision signed decimals:
1.  data representation involves a list of (chunks of) digits
2.  operations perform addition (and other operations), handling the list of digits explicitly

Java’s `java.util.HashSet` implements a set using a “hash-table” with separate chaining:
1.  values of a set are stored in linked lists, which are stored in array cells according to hash values
2.  union is implemented by inserting all elements of one set to the other

### Slide 11: Data Structure Building Blocks
Most data structures rely on the following two mechanisms to represent data in memory:

1.  **Contiguous blocks of data (via arrays):**
    *   *Image Description:* A row of adjacent square cells labelled A, B, C, D, E, F, followed by empty cells.
2.  **Linked structures (via pointers/references):**
    *   *Image Description:* A diagram showing nodes. Node A points to Node B, which points to Node D. There is a node C above D pointing to D. Node D points to Node E, which points to Node F. Node F points to a null set symbol ($\emptyset$).

### Slide 12
**Lists**

### Slide 13: List ADT
Intuitively, a List is a sequence of arbitrary elements.
We will consider List as a type that supports the following operations:
1.  create an empty list
2.  get list size (number of elements in the list)
3.  check if the list is empty
4.  get, set, add or remove an element <span style="color:red">at a given index</span>

### Slide 14-22: List (example)
Without knowing the implementation details, we can still represent the state of the list abstractly:

1.  create an empty list — `[]`
2.  add $A$ at index 0 — `[A]`
3.  add $B$ at index 0 — `[B, A]`
4.  add $C$ at index 2 — `[B, A, C]`
5.  get element at index 1 — `A`
6.  remove element at index 1 — `[B, C]`
7.  add $D$ at index 1 — `[B, D, C]`
8.  set element at index 2 to $G$ — `[B, D, G]`
9.  get element at index 0 — `B`

### Slide 23: List (Java)
An interface for lists in Java can look like this:
```java
public interface List<E> {
    int size();
    boolean isEmpty();
    E get(int i) throws IndexOutOfBoundsException;
    E set(int i, E e) throws IndexOutOfBoundsException;
    void add(int i, E e) throws IndexOutOfBoundsException;
    remove(int i) throws IndexOutOfBoundsException;
}
```

### Slide 24: Implementing Lists
There are two main implementations for lists:
1.  **Array-based (`ArrayList`)**
    *   All elements (or references) are stored in a single array
    *   Works well in most cases
2.  **Node-based (`LinkedList`)**
    *   List is represented by a collection of interconnected **nodes**
    *   Every node stores an element (or a reference to it) and a reference to the next node in the list
    *   Provides good worst case guarantees for some operations

### Slide 25: Array List (Java)
An array-based list implementation can be done as follows:
*Figure 1: Array List implementation (Goodrich, Tamassia, and Goldwasser 2014, §7).*
*(Code snippet showing class structure with `CAPACITY`, `data` array, `size` integer, and constructors).*

### Slide 26-27: Array List (Java): set and get
*Figure 2: Array List implementation of get and set.*
*(Code snippet showing `get(i)` returning `data[i]` and `set(i, e)` updating `data[i]`)*

**Question:** What is the time complexity of `get` and `set`?

### Slide 28: Array List (insert and shift)
When inserting in the middle of an array, we have to shift some elements to the right by one place:
*   *Image Description:* Three rows showing the array state.
    1.  **Initial array:** Contains A, B, C, D, E, F.
    2.  **After shift:** A, B, C remain. D moves to index 4, E to index 5, F to index 6. Index 3 is empty.
    3.  **After insert:** X is inserted at index 3. Final state: A, B, C, X, D, E, F.

### Slide 29-30: Array List (Java): add
*Figure 3: Array List implementation of add method.*
*(Code snippet showing `checkIndex`, `resize` check, a loop shifting elements `data[k+1] = data[k]`, and inserting the new element)*

**Question:** What is the time complexity of `add`?

### Slide 31-32: Array List (remove and shift)
When removing an element from the middle of an array, we have to shift some elements to the left by one place:
*   *Image Description:* Three rows showing the array state.
    1.  **Initial array:** A, B, C, D, E, F.
    2.  **After delete:** D is removed. E and F are shifted left to fill the gap.
    3.  **After shift:** Final state: A, B, C, E, F.

**Question:** What is the time complexity of `remove`?

### Slide 33: Array List (time complexity)
| Method | Complexity |
| :--- | :--- |
| `size()` | $O(1)$ |
| `is_empty()` | $O(1)$ |
| `get(i)` | $O(1)$ |
| `set(i, x)` | $O(1)$ |
| `add(i, x)` | <span style="color:red">$O(n)$</span> |
| `remove(i)` | <span style="color:red">$O(n)$</span> |

Can we provide more precise bounds for `add` and `remove`?

### Slide 34: Array List (adding/removing at the end)
Note shifting is not required when adding at the end of an array:
*   *Image Description:* Array [A, B, C, D, E, F]. X is added to the next available slot at index 6. No shifting occurred.

Similarly, when removing the last element of an array, we do not need to shift.

### Slide 35: Array List (time complexity, revised)
| Method | Time complexity |
| :--- | :--- |
| `size()` | $O(1)$ |
| `is_empty()` | $O(1)$ |
| `get(i)` | $O(1)$ |
| `set(i, x)` | $O(1)$ |
| `add(i, x)` | <span style="color:blue">$O(n - i)$</span> |
| `remove(i)` | <span style="color:blue">$O(n - i)$</span> |

### Slide 36-37: Array List (full array)
What should we do when inserting into a full array? We need to make more space!
*   *Image Description:*
    *   **Initial array:** Size 4, contains A, B, C, D. It is full.
    *   **New array:** Size 8. A, B, C, D are copied into the first 4 slots.
    *   **After insert:** X is added after D.
**Question:** What should be the size of the new array?

### Slide 38: Dynamic Array List
Idea: **double** the array size when it is full.
In this case we will not have to copy elements too often:
1.  Imagine that we start with an array of **capacity** 1 and **size** 0.
2.  Repeatedly add 1000 elements to the end of the array list.
3.  What is the minimum/maximum cost of each insertion?
4.  How many times did we have to copy the first element of the array list?
5.  What is the total cost of adding 1000 elements to the initial array list?

### Slide 39: Array List (time complexity)
| Method | Time complexity |
| :--- | :--- |
| `size()` | $O(1)$ |
| `is_empty()` | $O(1)$ |
| `get(i)` | $O(1)$ |
| `set(i, x)` | $O(1)$ |
| `add(i, x)` | <span style="color:blue">$O(n - i)$ amort.</span> |
| `remove(i)` | <span style="color:blue">$O(n - i)$</span> |

*(Footnote: We will learn about amortized analysis later.)*

### Slide 40: Singly Linked List
Singly Linked List stores its elements in separate **nodes**, which reference each other:
*   *Image Description:* A diagram titled `sampleList` pointing to a node containing A. A points to B, B points to C, C points to D (wait, the arrows snake: A->C->B->D... actually looking closely at slide 40, A->B is not direct. A points to next node C? No, the boxes are labeled A, C, E, B, D, F).
    *   *Correction based on slide:* Box `sampleList` points to the first node containing `A`. `A`'s next pointer points to the node containing `C`. `C` points to `E`. (Lower row): `B` points to `D`, `D` points to `F`. The arrows actually connect `A` -> `B` -> `C` -> `D` -> `E` -> `F` -> `null` (symbol $\emptyset$).

### Slide 41: Linked List (terminology)
*   *Image Description:* Same linked list as above. The first node (A) is labeled **head of sampleList**. The last node (F) is labeled **tail of sampleList**.
*   First node is called **head**, last node is called **tail**.

### Slide 42-43: Singly Linked List (get and set)
To access an element at index $i$:
1.  Start from the head of the list.
2.  Follow the reference to the next node $i$ times.
3.  Now we are at the node with index $i$!

**Question:** What is the time complexity for `get` and `set`?

### Slide 44-46: Singly Linked List (add)
To add an element at an index:
1.  Start from the head of the list.
2.  Follow the reference to the next node ($i - 1$) times.
3.  Create a new node with the added element and referencing the next node in the list.
4.  Update current node to point to the newly created one.

*   *Image Description:*
    *   **Initial list:** A -> B -> C -> $\emptyset$.
    *   **After add(2, X):** Node X is created. B now points to X. X points to C. Result: A -> B -> X -> C -> $\emptyset$.

**Questions:**
*   What is the time complexity of `add`?
*   What happens when $i = 0$?

### Slide 47-48: Singly Linked List (addFirst)
To add at the beginning of a list:
1.  Create a new node with the added element and referencing the head of the list.
2.  Update the head pointer of the list to point to the newly created one.

*   *Image Description:* New node X points to old head A. `sampleList` pointer updated to point to X.
**Question:** What is the time complexity of adding at the head?

### Slide 49-51: Singly Linked List (addLast)
To add at the tail:
1.  Start from the head of the list.
2.  Follow the reference until we find the tail.
3.  Create a new node with the added element.
4.  Update the tail to point to the newly created one.

**Questions:**
*   What is the time complexity of adding at the tail?
*   Will it help to store an explicit tail reference?

### Slide 52-54: Singly Linked List (remove)
To remove at an index:
1.  Start from the head of the list.
2.  Follow the reference to the next node ($i - 1$) times.
3.  Update current node to reference the node after the removed one.

*   *Image Description:* List A -> B -> C -> $\emptyset$. Removing B (index 1). A is updated to point directly to C. B is disconnected.

**Questions:**
*   What is the time complexity of `remove`?
*   What happens when $i = 0$?

### Slide 55-56: Singly Linked List (removeFirst)
To remove head of the list:
1.  Set head pointer of the list to point to the second node (or null).

*   *Image Description:* `sampleList` pointer moves from A to B.

**Question:** What is the time complexity of `removeFirst`?

### Slide 57: Singly Linked List (removing tail)
**Exercise 2.1**
Suggest an algorithm for removing the tail of a list.
What is the time complexity of your suggested algorithm?
Does it help if we explicitly keep track of the tail with an extra pointer?

### Slide 58: List (time complexity)
| Method | ArrayList | SinglyLinkedList |
| :--- | :--- | :--- |
| `size()` | $O(1)$ | $O(1)$ |
| `is_empty()` | $O(1)$ | $O(1)$ |
| `get(i)` | $O(1)$ | <span style="color:red">$O(i)$</span> |
| `set(i, x)` | $O(1)$ | <span style="color:red">$O(i)$</span> |
| `add(i, x)` | <span style="color:blue">$O(n - i)$ amort.</span> | <span style="color:blue">$O(i)$</span> |
| `addFirst(x)` | <span style="color:red">$O(n)$</span> | <span style="color:green">$O(1)$</span> |
| `addLast(x)` | <span style="color:green">$O(1)$ amort.</span> | <span style="color:red">$O(n)$ or $O(1)$</span> |
| `remove(i)` | <span style="color:blue">$O(n - i)$</span> | <span style="color:blue">$O(i)$</span> |
| `removeFirst()` | <span style="color:red">$O(n)$</span> | <span style="color:green">$O(1)$</span> |
| `removeLast()` | <span style="color:green">$O(1)$</span> | <span style="color:red">$O(n)$</span> |

### Slide 59: Doubly Linked List
Doubly Linked List stores all elements in separate **nodes** that reference each other in **both directions**:
*   *Image Description:* Nodes A, B, C, D. A points to B, B to A. B points to C, C to B, etc. Ends point to $\emptyset$.

### Slide 60-69: Doubly Linked List (analysis)
How does having a backwards pointer affect the time complexities?
1.  **How are `set` and `get` affected?**
    *   both methods have the same worst case $O(n)$ complexity
    *   but, more precisely, we can do $O(\min(i, n - i))$ (Why?)
2.  **How does time complexity of `add` change?**
    *   in general, we have $O(\min(i, n - i))$
    *   however, adding at the ends works in $O(1)$
3.  **How does time complexity of `remove` change?**
    *   in general, we have $O(\min(i, n - i))$
    *   however, removing at (both!) ends works in $O(1)$

### Slide 70: List (time complexity)
| Method | ArrayList | SinglyLinkedList | DoublyLinkedList |
| :--- | :--- | :--- | :--- |
| `size()` | $O(1)$ | $O(1)$ | $O(1)$ |
| `is_empty()` | $O(1)$ | $O(1)$ | $O(1)$ |
| `get(i)` | $O(1)$ | $O(i)$ | <span style="color:red">$O(\min(i, n - i))$</span> |
| `set(i, x)` | $O(1)$ | $O(i)$ | <span style="color:red">$O(\min(i, n - i))$</span> |
| `add(i, x)` | $O(n - i)$ amort. | $O(i)$ | <span style="color:blue">$O(\min(i, n - i))$</span> |
| `addFirst(x)` | $O(n)$ | $O(1)$ | $O(1)$ |
| `addLast(x)` | $O(1)$ amort. | $O(n)$ or $O(1)$ | $O(1)$ |
| `remove(i)` | $O(n - i)$ | $O(i)$ | <span style="color:blue">$O(\min(i, n - i))$</span> |
| `removeFirst()` | $O(n)$ | $O(1)$ | $O(1)$ |
| `removeLast()` | $O(1)$ | $O(n)$ | $O(1)$ |

### Slide 71: Break (5 min)

### Slide 72: Stacks

### Slide 73-75: Stack ADT
Stack is a restricted version of a list:
1.  we can only add (`push`) or remove (`pop`) the “top” element
2.  we can “get” (`peek`) only the “top” element

Thus, stack is a sequence where the last added element is the first to remove: **Last-In-First-Out (LIFO)**.

Stack is used in many programs. For example:
1.  recursive function calls (call stack)
2.  visiting history (navigation “breadcrumbs”)
3.  nested typing contexts in compilers

### Slide 76: Stack (methods)
Here are the methods of a stack:
1.  `size()` — get the stack size (number of elements)
2.  `is_empty()` — check if the stack is empty
3.  `push(x)` — add an element at the top of the stack
4.  `pop()` — remove the top element of the stack
5.  `peek()` — get the top element of the stack (without removing)

### Slide 77: Stack (implementation)
We can take two approaches to stack implementation:
1.  use primitive arrays or linked structures
2.  use an already existing list implementation

### Slide 78-79: Array Stack
Pushing onto the stack:
*   Increment the top counter, store the new element.
Popping from the stack:
*   Decrement the top counter, return element that was top before decrement.

*   *Image Description:* Array with indices 0-9. Elements A, B, C, D, E, F occupy 0-5. Arrow "top (index 5)" points to F. Arrow "bottom (index 0)" points to A. size=6.

**Question:** What should we do when top = 0?

### Slide 80-82: Array Stack (pop)
Popping from the stack:
*   Decrement the top counter, return element that was top before decrement.

**Question:** Should we remove/cleanup after decrementing the top counter?
1.  for primitive data — **no**, this is (usually) unnecessary
2.  for references — **yes**, we need to remove the reference to enable <span style="color:red">garbage collection</span>

### Slide 83: Array Stack (time complexity)
| Method | ArrayStack |
| :--- | :--- |
| `size()` | $O(1)$ |
| `is_empty()` | $O(1)$ |
| `push(x)` | <span style="color:blue">$O(1)$ amort.</span> |
| `pop()` | $O(1)$ |
| `peek()` | $O(1)$ |

### Slide 84: Linked Stack
Pushing onto the stack:
*   Same as adding at the head of a linked list.
Popping from the stack:
*   Same as removing the head of a linked list.

*   *Image Description:* Linked list A -> C -> E -> F -> $\emptyset$. "top" points to A. "bottom" points to F.
Since all operations deal with one end of a list, it is enough to use a singly linked list.

### Slide 85-86: Stack (time complexity)
| Method | ArrayStack | LinkedStack |
| :--- | :--- | :--- |
| `size()` | $O(1)$ | $O(1)$ |
| `is_empty()` | $O(1)$ | $O(1)$ |
| `push(x)` | <span style="color:blue">$O(1)$ amort.</span> | $O(1)$ |
| `pop()` | $O(1)$ | $O(1)$ |
| `peek()` | $O(1)$ | $O(1)$ |

**Question:** Why is `ArrayStack` often preferable in practice?

### Slide 87: Queues

### Slide 88-90: Queue ADT
Queue is a restricted version of a list:
1.  we can add (`offer`) only at the **rear** of a queue
2.  we can remove (`poll`) only at the **front** of the queue
3.  we can get (`peek`) only the element at the front of the queue

Thus, queue is a sequence, where first added element is the first to be removed: **First-In-First-Out (FIFO)**.

Queue is used in many programs. For example:
1.  keeping track of jobs/tasks to perform
2.  process messages in a system and communication channels
3.  processing incoming requests in a web server

### Slide 91: Queue (methods)
Here is a list of queue methods:
1.  `size()` — get the queue size (number of elements)
2.  `is_empty()` — check if the queue is empty
3.  `offer(x)` — add element at the rear of the queue
4.  `poll()` — remove element from the front of the queue
5.  `peek()` — get the element at the front of the queue

### Slide 92: Array Queue
Offering to the queue:
*   Increment the rear counter, add the new element at the rear index.
Polling the queue:
*   Increment the front counter, return the element at the front of the queue (before increment).

*   *Image Description:* Array with elements A, B, C, D, E, F. `front` points to A (index 0). `rear` points to F (index 5).

### Slide 93: Array Queue (crawling)
After a few offers and polls, the content of the queue crawls to the right.
*   *Image Description:*
    *   Initial: [A...F]. front at A, rear at F.
    *   After offer(G): [A...F, G]. front at A, rear at G.
    *   After poll(): [empty, B...G]. front at B, rear at G. The active area moved right.

**Question:** What should we do when the queue hits the end of the array?

### Slide 94-95: Circular Array Queue
We can us a circular array and continue adding elements at the left end of the array, if there are available cells.
*   *Image Description:* Array is visualized as a loop. Indices wrap around.
Incrementing counters happens <span style="color:red">modulo</span> the size of the array.

**Question:** Will we ever have to resize the underlying array?

### Slide 96: Array Queue (time complexity)
| Method | ArrayQueue |
| :--- | :--- |
| `size()` | $O(1)$ |
| `is_empty()` | $O(1)$ |
| `offer(x)` | <span style="color:blue">$O(1)$ amort.</span> |
| `poll()` | $O(1)$ |
| `peek()` | $O(1)$ |

### Slide 97: Linked Queue
Offering to the queue:
*   Same as adding at the tail of a linked list.
Polling the queue:
*   Same as removing the head of a linked list.

*   *Image Description:* Linked list with explicit `list head` and `list tail` pointers. `front` corresponds to head, `rear` corresponds to tail.
It is enough to use a singly linked list with a tail pointer!

### Slide 98-99: Queue (time complexity)
| Method | ArrayQueue | LinkedQueue |
| :--- | :--- | :--- |
| `size()` | $O(1)$ | $O(1)$ |
| `is_empty()` | $O(1)$ | $O(1)$ |
| `offer(x)` | <span style="color:blue">$O(1)$ amort.</span> | $O(1)$ |
| `poll()` | $O(1)$ | $O(1)$ |
| `peek()` | $O(1)$ | $O(1)$ |

**Question:** Why is `ArrayQueue` often preferable in practice?

### Slide 100: Break (10 min)
### Slide 101: Quiz

### Slide 102: Recursion

### Slide 103-105: Recursion
Recursive algorithms break down the problem into cases:
1.  **base case** — problem has a direct (simple) solution
2.  **recursive case** — problem is reduced to one or more subproblem, solved with the same algorithm

### Slide 106-108: Recursion (example 1)
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
*   one base case
*   one recursive case with one recursive call
*   code matches closely the mathematical definition

**Questions:**
*   What is the time complexity?
*   What is the space complexity?

### Slide 109-111: Recursion (example 2)
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
*   two base cases
*   one recursive case with two recursive calls

**Questions:**
*   What is the time complexity?
*   What is the space complexity?

### Slide 112-114: Recursion (example 2, time complexity)
For recursive algorithms, we can often formulate their running time as a recurrence relation:
$$
T(n) = \begin{cases} 
1, & \text{if } n \leq 1 \\
T(n-1) + T(n-2), & \text{otherwise}
\end{cases}
$$
We can give the upper bound on the time complexity:
$$T(n) \leq 2T(n-1) \leq 2^n = O(2^n)$$

**Question:** Can you provide a more precise complexity analysis?

### Slide 115-118: Recursion (example 3)
```python
def binsearch(A, l, r):
    if l > r:
        return NOT FOUND
    else:
        mid := floor((l+r)/2)
        if A[mid] = x:
            return mid
        elif A[mid] > x:
            return binsearch(A, l, mid - 1)
        else:
            return binsearch(A, mid + 1, r)
```
*   one base case
*   one recursive case (with two branches, but one recursive call in each)

**Questions:**
*   How to prove correctness?
*   What is the time complexity?
*   What is the space complexity?

### Slide 119: Recursion vs Explicit Stack

### Slide 120-123: Call Stack
Recursive functions rely on a call stack:
1.  Every function call puts an “activation frame” on a call stack, containing:
    1.1 saved local variable values
    1.2 return address (where to continue computation)
    1.3 argument values
2.  When exiting a function, the top activation frame is popped, and the computation continues with the previous frame.

**Implications:**
1.  Using the call stack counts towards <span style="color:red">space usage</span>.
2.  Deep recursion may lead to <span style="color:red">stack overflow</span>.
3.  Some languages implement <span style="color:green">tail call optimization</span> (but we will not count on that).

### Slide 124-127: Explicit Call Stack (idea)
We can implement the call stack “manually”:
1.  Current function’s state is stored at the top of the stack:
    *   argument values
    *   state (where in the recursive procedure we are at the moment)
    *   local variable values
2.  Instead of a recursive call — push a new frame on the call stack
3.  Instead of existing function — pop the top frame from the stack
4.  Stop when the stack is empty

### Slide 128-130: Using an explicit stack (example 1, tail recursion)
*Left (Recursive):*
```python
def factorial(n):
    return helper(n, 1)

def helper(n, r):
    if n == 0:
        return r
    else:
        return helper(n - 1, n * r)
```
*Right (Iterative/Explicit Stack):*
```python
def factorial(n):
    s = new empty stack
    s.push([n, 1])
    result = None
    while not s.is_empty():
        [n, r] = s.pop()
        if n == 0:
            result = r
        else:
            s.push([n - 1, n * r])
    return result
```
This example does not preserve the entire call stack:
1.  We do not pass the result of a recursive call to the callee
2.  Stack does not grow (hidden tail call optimization)

### Slide 131-133: Explicit Call Stack (example 2, one recursive call)
*Left (Recursive):*
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        r = factorial(n - 1)
        return n * r
```
1. function is “split” into BEFORE and AFTER recursive call.
2. recursive call output is passed via a special “register” `result`.

*Right (Explicit Stack):*
```python
def factorial(n):
    s = new empty stack
    s.push([n, BEFORE])
    result = None
    while not s.is_empty():
        frame = s.peek()
        if frame[1] == BEFORE:
            frame[1] = AFTER
            if n == 0:
                result = 1
                s.pop()
            else:
                s.push([n - 1, BEFORE])
        else:
            r = result
            result = n * r
            s.pop()
    return result
```

### Slide 134-137: Explicit Call Stack (example 3, two recursive calls)
*Left (Recursive):*
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        x = fibonacci(n - 1)
        y = fibonacci(n - 2)
        return x + y
```
1. function is “split” into BEFORE, BETWEEN and AFTER recursive calls.
2. recursive call output is passed via a special “register” `result`.
3. local variable `x` value is preserved on the stack.

*Right (Explicit Stack):*
```python
def fibonacci(n):
    s = new empty stack
    s.push([n, BEFORE, {x: None}])
    result = None
    while not s.is_empty():
        frame = s.peek()
        if frame[1] == BEFORE:
            if n <= 1:
                result = n
                s.pop()
            else:
                frame[1] = BETWEEN
                s.push([n - 1, BEFORE])
        elif frame[1] == BETWEEN:
            frame[2].x = result
            frame[1] = AFTER
            s.push([n - 2, BEFORE])
        else:
            y = result
            result = frame[2].x * y
            s.pop()
    return result
```

### Slide 138-141: Explicit Call Stack (example 4, tail recursion)
*Left (Recursive Binary Search):*
```python
def binsearch(A, l, r):
    if l > r: return NOT FOUND
    else:
        mid := floor((l+r)/2)
        if A[mid] = x: return mid
        elif A[mid] > x: return binsearch(A, l, mid - 1)
        else: return binsearch(A, mid + 1, r)
```

*Right (Explicit Stack):*
```python
def binsearch(A, l, r):
    s = new empty stack
    s.push([l, r])
    result = None
    while not s.is_empty():
        [l, r] = s.pop()
        if l > r:
            result = NOT FOUND
        else:
            mid := floor((l+r)/2)
            if A[mid] = x:
                result = mid
            elif A[mid] > x:
                s.push([l, mid - 1])
            else:
                s.push([mid + 1, r])
    return result
```
1. stack does not grow (tail call optimization)
2. it is enough to only pass arguments (no state or local variables)
3. loop body is very similar to the recursive function body

### Slide 142: Break (5 min)

### Slide 143: Brute Force and Backtracking

### Slide 144-145: Iterating over Sequences
**Problem**
**Input:** Sequence length $n$ and maximum digit $k$.
**Output:** All distinct sequences of $n$ digits (from 0 to $k$).

**Solution idea:**
*   Count from 0 in base ($k + 1$) number system
*   When all digits are $k$ — stop

### Slide 146: Iterating over Sequences (loop)
```python
function all_sequences(n, k):
    A = new array of size n
    for i = 1 to n
        A[i] = 0
    finished = False
    while not finished
        i = n
        while A[i] == k
            A[i] = 0
            i = i - 1
        if i < 1:
            finished = True
        else:
            A[i] = A[i] + 1
            print(A)
```

### Slide 147-148: Subsets
**Problem**
**Input:** Unordered array $A$ of size $n$, representing a set.
**Output:** All subsets of $A$.

**Idea:** each subset corresponds to a binary number of length $n$.

### Slide 149-152: Conditional Subsets
**Problem**
**Input:** Unordered array $A$ of size $n$, representing a set, and a number $k$.
**Output:** Number of subsets of $A$ such that the sum of elements of each subset is equal to $k$.

*   We can iterate over all subsets, compute and check the sum of elements for each subset.

**Questions:**
*   What is the time complexity of this algorithm?
*   Can we improve the algorithm?

### Slide 153: Conditional Subsets (iterative)
**Idea:**
*   Iterate over all binary numbers of length $n$ in a separate array.
*   Update current sum when for any digit change ($0 \to 1$ or $1 \to 0$).
*   If current sum is $k$, increment the result counter.

### Slide 154-156: Conditional Subsets (iterative algorithm)
```python
def subsets(A, n, k):
    S = new array of size n
    for i = 1 to n:
        S[i] = 0
    finished = False
    sum = 0
    count = 0
    while not finished:
        i = n
        while S[i] == 1:
            S[i] = 0
            i = i - 1
            sum = sum - A[i]
        if i < 1:
            finished = True
        else:
            S[i] = 1
            sum = sum + A[i]
        if sum == k:
            count = count + 1
    return count
```
**Questions:**
*   What is the time complexity of this algorithm?
*   What is the space complexity of this algorithm?

### Slide 157-159: Conditional Subsets (recursion)
**Idea:**
*   Let $F(A, k)$ be the number of subsets of $A$ with sum of elements equal to $k$.
*   Then, for the empty set:
    $$
    F(\emptyset, k) = \begin{cases} 
    1, & \text{if } k = 0 \\
    0, & \text{otherwise}
    \end{cases}
    $$
*   And if $|A| \geq 1$ then $A = \{x\} \cup B$ and
    $$F(\{x\} \cup B, k) = F(B, k) + F(B, k - x)$$

### Slide 160-162: Conditional Subsets (recursive algorithm)
```python
def subsets(A, n, k):
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    else:
        x = A[n]
        without_x = subsets(A, n - 1, k)
        with_x = subsets(A, n - 1, k - x)
        return (without_x + with_x)
```
**Questions:**
*   What is the time complexity of this algorithm?
*   What is the space complexity of this algorithm?

### Slide 163: Break (5 min)
### Slide 164: Backtracking

### Slide 165: Queen in Chess
Queen is a chess piece that moves an arbitrary distance horizontally, vertically, or diagonally.
*   *Image Description:* An $8 \times 8$ chess board with a Queen ($\mathbb{Q}$) in the center. Green dots mark all possible squares the queen can move to (entire vertical column, entire horizontal row, and both diagonals).

### Slide 166: N Queens Problem
Find a way to place $n$ queens on a board of size $n \times n$ such that no queen attacks another queen (i.e. no two queens share a horizonal, vertical, or diagonal line), or say that it is impossible.

For example, for $8 \times 8$ board one of the solutions is this:
*   *Image Description:* A valid arrangement of 8 queens on an 8x8 board.

### Slide 167-170: N Queens Problem (brute force idea)
*   Each queen should be in a separate horizonal
*   So for $i$-th queen it is enough to only find the proper column/vertical (there are only $n$ such lines)
*   When adding a new queen, we should make sure that it is not attacked by any other queens that are already on the board
*   If it is impossible to add $i$-th queen, then we must **backtrack** and try another position for an earlier queen

### Slide 171: N Queens Problem (search tree)
We can represent the search space as a tree.
For example, when $n = 2$, the search tree looks like this:
*   *Image Description:* A tree structure showing possible placements on a 2x2 board.
    *   Root branches to two nodes: Queen at (0,0) and Queen at (0,1).
    *   From Queen at (0,0), it branches to placing 2nd Queen at (1,0) (Conflict) and (1,1) (Conflict).
    *   From Queen at (0,1), it branches to (1,0) (Conflict) and (1,1) (Conflict).
    *   Shows no valid solution for N=2.

### Slide 172: N Queens Problem (search tree)
We can represent the search space as a tree.
For example, when $n = 3$, the search tree looks like this:
*   *Image Description:* A larger search tree for a 3x3 board exploring possible placements.

### Slide 173: N-queens (iterative approach)
*   Brute force is similar to iterating over sequences of length up to $n$.
*   However, we can <span style="color:green">prune entire branches</span> if a sequence prefix is not valid!

### Slide 174: N Queens Problem (iterative algorithm sketch)
```python
function queens(n)
    columns = new array of size n
    for i = 1 to n
        columns[i] = 1
    i = 1
    while (i <= n)
        j = columns[i]
        while (j <= n) and not safe(columns, i, j)
            j = j + 1
        if (j <= n)
            columns[i] = j
            i = i + 1
        else
            // backtrack
            columns[i] = 0
            i = i - 1
    return columns
```

### Slide 175: References
*   Cormen, Thomas H et al. (2022). *Introduction to algorithms*. MIT press.
*   Goodrich, Michael T, Roberto Tamassia, and Michael H Goldwasser (2014). *Data structures and algorithms in Java*. John Wiley & Sons.
*   Shen, Aleksandr (2015). *Programming: theorems and problems*. Litres. -->