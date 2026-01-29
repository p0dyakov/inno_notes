<!-- # File 1: Lab 1 (Introduction)

### Slide 1: Title Page
**Innopolis University**

# Lab 1
## Introduction

**Team:**
Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer

Software Systems Analysis and Design
Spring Semester 2026

### Slide 2: Agenda
**Agenda**

*   Introduction
*   Rules
*   Questions for discussion
*   Exercises

### Slide 3: TAs
**TAs**

*   **Ahmed Nouralla** (a.shaaban@innopolis.university)
*   **Alaa Aldin Hajjar** (a.hajjar@innopolis.university)
*   **Damir Nurtdinov** (d.nurtdinov@innopolis.university)
*   **Marko Pezer** (m.pezer@innopolis.university)

### Slide 4: Rules
**What will we use?**
*   C++20 standard
*   Preferred IDEs: VS Code, CodeBlocks
*   For today: you can use `https://cpp.sh`

**During the labs:**
*   Try not to be late
*   Speak English
*   Scan QR code for attendance at the end of the lab

### Slide 5: Questions for discussion
*   What are the differences between C and C++?
*   What are the three types of memory that C++ programs use?
*   What are the differences between pointers and references in C++?
*   Is it allowed to create a reference to a pointer? Vice versa?
*   What is *type deduction*?

### Slide 6: Hello World
```cpp
#include <iostream>

int main()
{
    std::cout << "Hello world" << std::endl;
    return 0;
}
```

### Slide 7: Namespaces
```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "Hello world" << endl;
    return 0;
}
```

### Slide 8: Task 1
**Task 1**
Write a program that accepts time period given in seconds and returns it in the following format: *hours : minutes : seconds*

| Input | Output |
| :--- | :--- |
| 124660 | 34:37:40 |

### Slide 9: Task 2
**Task 2**
Write your own function for swapping values of two integers using:
a) Passing by pointer
b) Passing by reference

### Slide 10: Task 3
**Task 3**
Write a program that accepts a number of elements (*N*) of the array of integers and then *N* elements. After user inserts the array, your program should remove all duplicates from it. Solve this task using:
a) Arrays
b) Vectors

| Input | Output |
| :--- | :--- |
| 8<br>1 3 5 3 3 4 1 2 | 1 3 5 4 2 |

### Slide 11: The End
**The end.**

Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer
Software Systems Analysis and Design
Spring Semester 2026

---

# File 2: Tutorial 1

### Slide 1: Title Page
**System Software Analysis and Design**

# Tutorial 1

Spring Semester 2026
Innopolis University
Munir Makhmutov

### Slide 2: Agenda
*   Rules and Regulations
*   Some first C++ programs
*   Namespaces
*   Arrays vs Vectors
*   Structured binding

### Slide 3: Organization - Contents
*   **Lectures:** Theory, general stuff. Language concepts will be presented first.
*   **Tutorials:** Extra stuff. Examples to illustrate what was presented during the lecture + particular aspects.
*   **Labs:** Allow you to get practical experience in programming.

### Slide 4: Organization - Moodle
*   All information will be on Moodle (`http://moodle.innopolis.university`)
*   There you will find:
    *   The lecture and tutorial materials, just after the class
    *   And the lab sessions with exercises and information about the assignments
    *   Plus any other information and all your grades

### Slide 5: Exams, Evaluation & Grading - Examinations
**Examinations**
*   **Assignments:** 4 (to be evaluated regularly)
*   **Midterm examination:** Moodle Quiz (March 10)
*   **Final examination:** Written form

### Slide 6: Exams, Evaluation & Grading - Assessment
**Assessment**
*   Mid-term Exam (25%)
*   Final Exam (30%)
*   Assignments (40%)
*   Lab attendance (5%)
*   Bonus (5%)

**Grading**
*   A [90, 100]
*   B [75, 90)
*   C [60, 75)
*   D [0, 60)

### Slide 7: The Very First Program Example 1
*The first impression: a lot of details.*
*The second impression: no one detail is clear ☺.*

```cpp
#include <iostream>
int main()
{
    std::cout << "Hello world" << std::endl;
    return 0;
}
```

### Slide 8: The Very First Program Example 1 (Analysis)
*[Image Description: The code from the previous slide is shown with red arrows pointing to specific parts explaining them]*

*   **`#include <iostream>`**: Preprocessor directive: the contents of the file whose name is in angle brackets gets textually included to the program. This is the name of the text file from the standard C++ library. What’s included: declarations of entities used in the program.
*   **`int main()`**: This is the "main" function. The program starts its execution from this function. It’s called by the environment.
*   **`return 0;`**: The value of 0 is returned by the `main` function. The convention is that 0 denotes the successful completion. The return statement completes the function execution and returns the control back to the caller (to the environment in case of main).
*   **Comment:** All this looks like in C...

### Slide 9: The Very First Program Example 2
```cpp
#include <iostream>
int main()
{
    std::cout << "Hello world" << std::endl;
    return 0;
}
```

### Slide 10: The Very First Program Example 2 (Analysis)
**...and this is C++ specifics**
*[Image Description: Code analysis focusing on C++ specific syntax]*

*   **`std::`**: The name `std` denotes **namespace**: a special construct for avoiding possible name clashes. By convention, all entities from the standard library are declared within this namespace.
*   **`std::cout`**: `std::cout` is called **qualified name**. It refers to the library entity `cout` declared within the `std` namespace. Semantically, `cout` denotes the console output stream.
*   **`<<`**: Normally, `<<` is the low-level **shift operator** applying to integers. But here it applies to operands of other types. How it’s possible? This is because the `<<` operator was **overloaded**. In other words, `std` namespace contains the **different version** of this operator.
*   **`"Hello world"`**: This is the **string literal**. Its type is by definition `const char*`.

### Slide 11: C++ Namespaces (Structure of C)
What’s the overall structure of a **C** program?
*   A sequence of declarations.
*   Nothing else.

```c
int a, b, c;
struct S { ... };
int main()
{
    ...
    return 0;
}
```

### Slide 12: C++ Namespaces (Structure of Java)
What’s the overall structure of a **Java** program?
*   A sequence of class declarations.
*   (Some extension: packages).

```java
class C1 { ... }
class C2 { ... }
public class C3 {
    public static void main(String[] s) {
        ...
    }
}
```

### Slide 13: C++ Namespaces (Motivation)
**We need a more advanced mechanism for structuring big and huge programs**

### Slide 14: C++ Namespaces (Definition)
In C++, we have a bit more advanced (but still lightweight) structuring mechanism: **namespaces**.

The way to **group** a set of related declarations into the single higher-level construct.

### Slide 15: C++ Namespaces (Syntax)
```cpp
namespace Subsystem1
{
    class C1 { ... };
    int a, b;
    void f() { ... }
}
...
namespace Subsystem2
{
    class C2 { ... };
    class C3 {
        int main() {
            ...
            return 0;
        }
    };
}
```

### Slide 16: C++ Namespaces (Access)
The very first point: how to get access to entities of a namespace from outside of it?
*   The answer is **qualified naming**: a name of an entity is qualified by the name of its namespace.

**Format:** `namespace-name :: name`

### Slide 17: C++ Namespaces (Access Example)
```cpp
namespace Subsystem1
{
    class C1 { ... };
    int a, b;
    void f() { ... }
}
...
int x = Subsystem1::a;
Subsystem1::f();
```
*Note: The code `Subsystem1::f()` shows access to function `f` from the `Subsystem1` namespace.*

### Slide 18: C++ Namespaces (Multi-file)
Additional aspects of namespace mechanism.
1.  Namespaces can be extended to several files (translation units).

*   **Translation unit 1:**
    ```cpp
    namespace Subsystem1 {
        class C1 { ... };
        int a, b;
        void f() { ... }
    }
    ```
*   **Translation unit 2:**
    ```cpp
    namespace Subsystem1 {
        class C2 { ... };
        int x, y;
        void ff() { ... }
    }
    ```
*Note: These are parts of the same namespace.*

### Slide 19: C++ Namespaces (Nested)
2.  Namespaces can be **nested**.

```cpp
namespace OurBigSystem
{
    class C1 { ... };
    void f() { ... }
    namespace MySubsystem
    {
        class C2 { ... };
        void myFun() { ... }
        int a, b;
    }
}
...
int x = OurBigSystem::MySubsystem::a;
```

### Slide 20: C++ Namespaces (Unnamed)
3.  The whole program is considered as an **unnamed namespace**.

```cpp
int a;
namespace Subsystem
{
    int a;
}
...
int x = Subsystem::a;  // Access to a from Subsystem
int y = a;
int z = ::a;           // Access to global a
```

### Slide 21: C++ Namespaces (Standard Library)
4.  All entities composing the C++ standard library are enclosed by the **std** namespace.

```cpp
std::vector<int> myVec;
std::cout << "Hello world" << std::endl;
```
`vector`, `cout`, `endl` are declared in the `std` namespace.

### Slide 22: C++ Namespaces (Using declarations 1)
5.  **Using-declarations** are used for simplifying compound names.

```cpp
namespace System {
    ...
    namespace Subsystem {
        int a;
    }
}
...
int x = System::Subsystem::a;
```

### Slide 23: C++ Namespaces (Using declarations 2)
```cpp
namespace System {
    ...
    namespace Subsystem {
        int a;
    }
}
...
using namespace System::Subsystem;
int x = a;
```

### Slide 24: C++ Namespaces (Best Practices)
**Don't forget to add:**
`using namespace std;`
when you use things from the standard library!

**However, not a good practice to add full `std`, instead add partially, e.g.:**
`using std::cout;`

### Slide 25: C++ Namespaces (Name Clashes)
6.  Namespaces can prevent **name clashes**.

```cpp
int a;
namespace Subsystem1 {
    ...
    int a;
}
...
namespace Subsystem2 {
    ...
    int a;
}
...
Subsystem1::a = 777;
Subsystem2::a = 999;
a = 333;
```
*Note: These are different `a`'s.*

### Slide 26: The Second Program Example (1)
**The task:** Find a given value in an array.

**Version 1**
```cpp
int find1 ( int array[20], int x )
{
    for ( int i = 0; i < 20; i++ )
    {
        if ( array[i] == x ) return i; // success
    }
    return -1; // fail
}
```

### Slide 27: The Second Program Example (1) - Critique
*[Image Description: The code from Slide 26 is shown with the array size `20` circled in red]*

**Are you happy with this solution?**

### Slide 28: Arrays in C/C++
**Syntax:** `T A[size];`
*   `T`: Type of array elements.
*   `A`: Array identifier.
*   `size`: Specifies the number of array elements; this is an expression of an integer type. In general, `size` should be a constant expression.

**Examples:**
```cpp
int Array[10];
const int x = 7;
void* Ptrs[x*2+5];
int Matrix[10][100];
```

**The only operator on arrays:**
*   Getting access to an element:
    ```cpp
    int el5 = Array[5];
    Array[7] = 7;
    ```

### Slide 29: Arrays & Pointers
```cpp
int Array[10];
```
By definition, array name is treated as a **pointer** to the first array element. To be more precise, array name is a **constant pointer**.

Therefore, these two constructs are semantically identical:
`int Array[10];`  <==> `const int* Array;`

**Accessing elements:**
`Array[0]` is equivalent to `*Array`

*[Image Description: A diagram showing memory layout. "Array" points to "Element 0", followed by Element 1, Element 2... Element 9]*

**Note:** Don't forget about pointer arithmetics! ☺

### Slide 30: The Second Program Example (2)
**Version 2**
```cpp
int* find2 ( int* array, int n, int x )
{
    const int* p = array;
    for ( int i = 0; i < n; i++ )
    {
        if ( *p == x ) return p; // success
        p++;
    }
    return nullptr; // fail
}
```
**Usage:**
```cpp
int A[20];
...
int* res = find2(A, 20, 5.5);
```

### Slide 31: The Third Program Example (1) - Observations
**Observations:**
*   Arrays in C (together with underlying pointers) are quite flexible mechanism.
*   In general, arrays are low-level language feature that is a permanent source of various bugs that are sometimes extremely hard to discover.
*   Being low-level feature, arrays (together with pointers) are the favorite means for hacking.
*   Being flexible, arrays at the same time are quite limited in functionality.

### Slide 32: The Third Program Example (1) - Conclusion
**Conclusion:**
C++ suggests another mechanism that is a very attractive replacement for arrays: **vectors**.

B. Stroustrup directly recommends to use vectors instead of arrays everywhere.

### Slide 33: The Third Program Example (2) - Arrays
`int A[20];`
*   Array declaration
*   Contains elements of type `int`
*   Internally, array elements are adjacent
*   The size of array is **fixed** and cannot change
*   Access to array elements is by indexing
*   Arrays are a part of the core C++ language

### Slide 34: The Third Program Example (2) - Vectors
`vector<int> A;`
*   Vector declaration
*   Contains **any number** of elements of type `int`
*   The size of vector is **dynamically changed**
*   Access to vector elements is by indexing (!)
*   Vectors are a part of the C++ standard library
*   Vectors have much more rich functionality
*   Vectors are as efficient as arrays

*Note: Actually, vectors are templates ("generics" as in Java), and use the syntax with angle brackets. However, it's not necessary to know all "generic" machinery. – Just use it!*

### Slide 35: The Third Program Example (3) - Initialization
```cpp
vector<int> v1;
```
*   `v1` is the vector of some number of integer values.
*   Initially, the size of `v1` is 0 (no elements).

```cpp
vector<int> v2 = { 1, 2, 3 };
```
*   This is one way of initializing vectors (New but intuitively clear construct).

```cpp
vector<int> v3;
v3.push_back(10);
v3.push_back(20);
v3.push_back(30);
```
*   Another way of initializing vectors: dynamic adding elements to vectors.
*   `vector<int>` is a **class** and it has a number of member functions ("methods").

### Slide 36: The Third Program Example (4) - Access & Size
```cpp
vector<int> v4 = { 1, 2, 3 };
int x = v4[0];
v4[2] = 777;
```
*   Use the usual notation to access to vector elements! (Later we will see why it's possible in C++).

```cpp
vector<int> v5;
for ( int i = 0; i < some-expr; i++)
    v5.push_back(i*10);
cout << v5.size() << endl;
```
*   The size of the vector changes **dynamically**.
*   To get the current vector size, use the `size()` member function.

### Slide 37: The Third Program Example (5) - Loop
**Array Style:**
```cpp
int A[10];
for (int i = 0; i < 10; i++)
    A[i] = A[i]*25;
```
*   This is the usual way for working with array elements collectively.

**Vector Style (Advanced For-loop):**
```cpp
vector<int> v6 = { 1, 2, 3, 4 };
int sum = 0;
for ( int elem : v6 )
    sum += elem;
```
*   Here, `elem` is the variable that is **local** to the for-loop.
*   `elem` gets the value of consequent vector elements.

### Slide 38: The Third Program Example (6) - The Problem
```cpp
vector<int> v6 = { 1, 2, 3, 4 };
for ( int elem : v6 )
    elem = elem*10;
```
**What are values of v6 elements after the loop has finished?**
*   The vector elements didn't change! **Why?**

### Slide 39: The Third Program Example (6) - The Solution (References)
```cpp
vector<int> v6 = { 1, 2, 3, 4 };
for ( int& elem : v6 )
    elem = elem*10;
```
*   Here, `elem` is not a value, but the **reference** to the current vector element (i.e., a **synonym** of that element).

### Slide 40: The Third Program Example (6) - Type Deduction
```cpp
vector<int> v6 = { 1, 2, 3, 4 };
for ( auto& elem : v6 )
    elem = elem*10;
```
*   Another advanced C++ feature: We **don't need** to specify the `elem` type explicitly: the compiler can do that itself.
*   This feature is called **type deduction** (or **type inference**). We will discuss this feature later in details.

### Slide 41: To Conclude... (Vectors)
**There are many more vector features**
`v.assign`, `v.at`, `v.back`, `v.begin`, `v.capacity`, `v.clear`, `v.end`, `v.erase` ...

**A recommendation, not a task ☺:**
*   Experiment with these vector features: either on labs or at home.
*   Use vectors everywhere when arrays are needed.

### Slide 42: To Conclude... (Standard Library)
**There are many more data structures in the C++ standard library:**
`vector<int>`, `list<int>`, `stack<int>`, `queue<int>` ...

**A recommendation, not a task ☺:**
*   Experiment with these data structures.
*   Don't reinvent the wheel – use the C++ library ☺.

### Slide 43: Structured Binding
**Simplified (Since C++17)**
```cpp
auto [ x, y, z ] = expression ;
auto [ x, y, z ] { expression } ;
auto [ x, y, z ] ( expression );
```

### Slide 44: Structured Binding (Explanation)
1.  Introduces variables from brackets to the current scope.
2.  Binds them to **subobjects** or **elements** of the object from *expression*.

### Slide 45: Structured Binding (Examples 1)
```cpp
int a[2] = { 1, 2 };

auto [x,y] = a;

auto& [xr, yr] = a;
```

### Slide 46: Structured Binding (Mechanism 1)
*[Image Description: Diagram explaining `auto [x,y] = a;`]*

*   **Imaginary name:** A temporary array `e` is created. Array `a` gets copied to `e`.
*   `x` refers to `e[0]`, and `y` refers to `e[1]`.

### Slide 47: Structured Binding (Mechanism 2)
*[Image Description: Diagram explaining `auto& [xr, yr] = a;`]*

*   `xr` refers to `a[0]`, and `yr` refers to `a[1]`.

### Slide 48: Structured Binding (Examples 2 - Structs)
```cpp
struct S {
    int x;
    const double y;
};
S f();

const auto [x, y] = f();
```
**Deconstruction:**
*   `x` is of type `int`
*   `y` is of type `const double`

### Slide 49: Structured Binding (Examples 3 - Tuples)
```cpp
std::tuple<int,int&> f();

auto [x, y] = f();
// x is of type int;
// y is of type int&

const auto [z, w] = f();
// z is of type const int;
// w is of type int&
```

### Slide 50: Structured Binding (References)
*   ISO Standard, Section 11.5
*   `http://en.cppreference.com/w/cpp/language/structured_binding`

### Slide 51: Summary
**So, what we have discussed today:**

Some small improvements & examples, and... three C++ features:
*   Namespaces
*   Vectors as an advanced arrays
*   New for-loops (See also Appendix)
*   Structured binding

### Slide 52: Appendix - for-range (1)
**For's advanced form (Since C++11)**

```cpp
for ( range-declaration : range-expression )
    loop-statement
```

### Slide 53: Appendix - for-range (2)
**Range-declaration:**
A declaration of a named variable, whose type is the type of the element of the sequence represented by *range_expression*, or a reference to that type. Typically, `auto` specifier is used for automatic type deduction.

**Range-expression:**
Any expression that represents a suitable sequence (either an array or an object for which `begin` and `end` member functions or free functions are defined) or a *braced list*.

### Slide 54: Appendix - for-range: examples (1)
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {0, 1, 2, 3, 4, 5};

    for (const int& i : v)  // access by const reference
        cout << i << ' ';

    for (auto i : v)        // access by value, the type of i is int
        cout << i << ' ';

    for (int n : {0, 1, 2, 3, 4, 5}) // the initializer may be a braced-init-list
        cout << n << ' ';

    int a[] = {0, 1, 2, 3, 4, 5};
    for (int n : a)         // the initializer may be a usual array
        cout << n << ' ';
}
```

### Slide 55: Appendix - for-range: examples (2)
```cpp
    // ... previous code ...
    for (int n : a)
        cout << 1 << ' ';   // No need for any loop ☺☺
}
```

### Slide 56: Appendix - for-range: informal semantics (1)
`for ( range-declaration : range-expression ) loop-statement`

*range-expression* is evaluated to determine the **sequence** or **range** to iterate. Each element of the sequence, in turn, is **dereferenced** and **assigned** to the variable with the type and name given in *range-declaration*.

*   ISO Standard, Section 6.5.4
*   `http://en.cppreference.com/w/cpp/language/range-for`

### Slide 57: Appendix - for-range: informal semantics (2)
**Since C++17**

Equivalent logic:
```cpp
{
    auto && __range = range_expression;
    auto __begin = begin_expr ;
    auto __end = end_expr ;
    for ( ; __begin != __end; ++__begin)
    {
        range_declaration = *__begin;
        loop_statement
    }
}
```
**Details:**
*   If *range-expression* is an array:
    *   `begin_expr` is `__range`
    *   `end_expr` is `__range + __bound` (array size)
*   If *range-expression* is an object of a class type C:
    *   `begin_expr` is `__range.begin()`
    *   `end_expr` is `__range.end()`
    *   (The assumption is that class C contains member functions `begin()` & `end()`).

---

# File 3: Lecture 1

### Slide 1: Title Page
**System Software Analysis and Design**

# Lecture 1
## Introduction to the Course
## Introduction to C++

Spring Semester 2026
Innopolis University
Eugene Zouev

### Slide 2: Why the Course?
*   Programming is the fundamental skill in computer science – whatever area you choose in your professional career.
*   A professional should know several programming languages...
*   ...Moreover: (s)he should be able to quickly learn any new language, software technology or a framework...
*   And for that, you should know **basic concepts** that are common to many (if not all) programming languages: type, algorithm, control flow, expressions/statements, syntax/semantics, software lifecycle, OOP, and many other.

*Note: I'm sure you have some experience in practical programming. But do you really understand (and can explain) notions used in your code?*

### Slide 3: The Overall Structure of the Course
**Three main parts of the course**

**The fall semester**
*   **The C language:** Small, system-level (but still general-purpose) language.
*   **The Java language:** Powerful application language.

**The spring semester**
*   **The C++ language:** Fast and powerful general-purpose language with **deep semantics**.
*   **Design patterns:** How to design, organize and structure complex OO programs.

### Slide 4: Before we start... (1)
**A remark about language syntax & semantics**

*   **Syntax:** A set of rules that regulate the structure of programs and their parts (constructs).
*   **Semantics:** The **meaning** of the constructs.
    *   *Static semantics:* How programs get compiled.
    *   *Dynamic semantics:* How programs get executed.

*[Image Description: A "Wrong" view is depicted where Syntax and Semantics boxes are roughly equal in size/importance.]*

### Slide 5: Before we start... (2)
**Reality:**

*[Image Description: A "Reality" view is depicted where the Syntax box is very small and the Semantics box is huge.]*

**Conclusion for programmers:**
Pay most attention on the language **semantics** rather than on syntax.

### Slide 6: An Informal Remark
**Do not trust me 100% ☺☹**

**Reasons:**
*   C++ is a *very complicated language*, and its implementations often treat many language features *differently*.
*   C++ is a *very complicated language*, and its normative reference ("ISO Standard") contains a number of ambiguities, "white places" and "dark spots" (e.g., "**undefined behavior**" ☺☹).
*   C++ is a *very complicated language*, and I am just a person (not a compiler ☺) therefore I might *misunderstand* and/or *cannot explain* some language features (including basic ones ☺).

**Conclusion:**
**Check everything I am saying on your compiler(s)**

### Slide 7: The Tentative Course Program
1.  **Jan, 20:** C++ type system; references & constants types
2.  **Jan, 27:** Classes **without OOP**
3.  **Feb, 3:** C++ classes & the basics of OOP
4.  **Feb, 10:** C++ classes (cntd)
5.  **Feb, 17:** C++ templates
6.  **Feb, 24:** C++ templates & generic programming; adapters; Lambdas & functional programming
7.  **Mar, 3:** C++ stand. library; the notion of iterator, iterator examples
8.  **Mar, 10:** **Midterm exam**
9.  **Mar, 17:** Design patterns: an introduction
10. **Mar, 24:** Design patterns 2
11. **Mar, 31:** Design patterns 3
12. **Apr, 7:** Design patterns 4
13. **Apr, 14:** Design patterns 5
14. **Apr, 21:** Design patterns 6
15. **Apr, 28:** Design patterns 7
    **~May:** **Final exam**

### Slide 8: Part Divider
**End of Introductory Part**

# The C++ Language

### Slide 9: C++ Origins
*   **B. Stroustrup:** "C With Classes", AT&T/Bell Labs, 1980
*   **Predecessors:**
    *   **C** language as a common basis;
    *   **Simula-67** with the notion of class

**Bjarne Stroustrup** - A History of C++: 1979-1991
`http://www.stroustrup.com/hopl2.pdf`

*[Image Description: Photo of Bjarne Stroustrup sitting at a desk with a computer.]*

### Slide 10: References 1
*   **ISO C++ International Standard**: The latest publicly-available "Working Draft" is ok: `http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/n4993.pdf`
*   **E. Зуев, А. Чупринов**: Стандарт С++: перевод, комментарии, примеры. Might be found in the University library (?); no electronic version.
*   **B. Stroustrup's books**: *Programming: Principles and Practice Using C++* (Second Edition).
*   **Internet sources**:
    *   `www.stackoverflow.com`
    *   `www.cppreference.com`
    *   `https://blog.smartbear.com/c-plus-plus/`
    *   `www.ibm.com/developerworks/`

*[Image Description: Cover of Bjarne Stroustrup's book "Programming: Principles and Practice Using C++".]*

### Slide 11: References 2
*   **A Tour of C++ (Second Edition)** by Bjarne Stroustrup
*   **Язык программирования C++. Краткий курс, второе издание** by Бьярне Страуструп
    *   ISBN-13: 978-0134997834
    *   ISBN-10: 0134997840

*[Image Description: Covers of the English and Russian versions of "A Tour of C++".]*

### Slide 12: References 3
*   **C++ Templates. The Complete Guide**, David Vandevoorde, Nicolai M. Josuttis. Addison-Wesley, 2003, ISBN 0-201-73484-2.
*   **Russian translation:** Шаблоны С++. Справочник разработчика.

*[Image Description: Covers of the English and Russian versions of "C++ Templates".]*

### Slide 13: References 4
*   **Ivan Čukić:** *Functional Programming in C++*
*   **Jacek Galowicz:** *C++ 17 STL Cookbook*

*[Image Description: Covers of the two books listed.]*

### Slide 14: C++ Timeline
*   **1980:** "C With Classes"
*   **1991:** The start of the standardization process
*   **1998:** The first ISO Standard (C++98)

**Timeline:**
*   **C++11:** Move semantic, Unified initialization, **auto** and decltype, Lambda functions, constexpr.
*   **C++14:** Reader-writer locks, Generalized lambda functions.
*   **C++17:** Fold expressions, constexpr if, Structured binding declarations, string_view, Parallel algorithm of the STL, The filesystem library, std::any, std::optional, std::variant.
*   **C++20:** Operator <=>, constexpr extensions, **Concepts**, Contracts, Ranges, Coroutines, Modules.

The evolution of C++: all its new features give a **new quality** to the language. This is definitely **another language** than "good old" C++...

### Slide 15: C++ Timeline 2
**C++ 23**
*   Better concepts
*   Better modules
*   Better coroutines
*   Better Range library
*   Reflection (Experimental)
*   *Not all features are implemented yet...*

**C++ 26 (coming)**
*   Reflection
*   Pattern matching
*   Contracts (Pre- & postconditions)

### Slide 16: C++: A First View
**The language relies on programmer's mastery**

*   **Very complicated language:** For learning, using, and implementing ☺.
*   **Awkward & bulky syntax:** The overall design of the language is ~~bad~~ not good.
*   **Very many concepts supported:** Very **powerful & detailed semantics**.
*   **Full spectrum of features:** from high to low level.
*   **Efficient compilation.**
*   **C is the predecessor and the basis of C++.**

*[Image Description: A photo of the Sutyagin House, a ridiculously tall, chaotic, and precarious wooden skyscraper, symbolizing the complexity and "patched-together" nature of C++.]*

### Slide 17: Is C++ Hard to Understand?
**The task:** To print the famous message to the console ☺

**C:**
```c
#include <stdio.h>
int main() {
    printf("Hello, world!\n");
    return 0;
}
```

**C++:**
```cpp
#include <iostream>
int main() {
    std::cout << "Hello world" << std::endl;
    return 0;
}
```

**Python:**
```python
print("Hello world")
```

### Slide 18: The C/C++ Memory Model
Each C/C++ program uses three kinds of memory:
1.  **Program:** Sequence of machine code instructions. Program cannot modify this memory (self-modified programs are not allowed).
2.  **Heap (Dynamic memory):** Dynamically allocated objects. The discipline of using heap is defined by program **dynamic semantics**, i.e., at runtime.
3.  **Stack:** Local objects. The discipline of using stack is defined by the (static) **program structure**.

*[Image Description: Diagrams representing the three memory areas. Program is a dotted rectangle. Heap is an amorphous green blob. Stack is a vertical stack structure.]*

### Slide 19: The Notion of Type (1)
**Type (of an object/entity) is:**
*   A set of **values** that an object of the type can have.
*   A set of **operators** on objects of that type.
*   A set of **relationships** between the type and other types.

### Slide 20: The Notion of Type (2)
**Examples:**

1.  **`int i;`**
    *   **Values:** Integer numbers within the range...
    *   **Operators:** Creation, destruction, copying, moving, Arithmetic & comparison operators, Shifts...
    *   **Relationships:** Conversions to boolean, float...

2.  **`class C { ... };`**
    *   **Values:** Cartesian product of class members' sets.
    *   **Operators:** Creation, destruction, copying, **moving**, Access to class members, User-defined operators.
    *   **Relationships:** Between this type and its base class(es), User-defined conversion operators.

*Note: Moving operators are C++ specifics!*

### Slide 21: C++ Type System
**Hierarchy:**
*   **Fundamental types:**
    *   **Atomic types:**
        *   Integers
        *   Characters
        *   Floating
        *   ...
    *   **Pointers**
*   **User-defined types:**
    *   **Compound types:**
        *   Arrays
        *   Structures
        *   Unions
        *   Classes
        *   Enumerations

*[Image Description: A tree diagram illustrating the classification of C++ types.]*

### Slide 22: C++ Arithmetic Types
**Integral types ≡ Integer types**

*   **Signed integer types:**
    *   Standard: `signed char`, `short int`, `int`, `long int`, `long long int`
    *   Extended: Implementation-defined
*   **Unsigned integer types:**
    *   Standard: `unsigned char`, `unsigned short int`, `unsigned int`, `unsigned long int`, `unsigned long long int`
    *   Extended: Implementation-defined
*   **Narrow character types:**
    *   Ordinary: `char` (Underlying: `unsigned char` or `signed char`)
    *   `signed char`, `unsigned char`
    *   `char8_t` (Underlying: `unsigned char`)
*   **Others:**
    *   `bool`
    *   `char16_t` (Underlying: `uint_least16_t`)
    *   `char40_t` (Underlying: `uint_least16_t`)
    *   `wchar_t`

**Floating-point types:**
*   `float`
*   `double`
*   `long double`

### Slide 23: C++ Types & Type Specifiers
**Informal classification:**

*   **Predefined (language-defined):** Integers, Reals, Characters... (Represented by keywords: `int`, `double`, `char`...).
*   **User-defined types:** Classes, Enumerations... (Represented by their identifiers: `myClass`).
*   **"Modified" types:** Constant types, Pointer types, Reference types, Function types, Arrays. (Represented by special syntax: `const`, `*`, `&`, `[]`).

### Slide 24: C++ Compound Types
*   **arrays** of objects of a given type;
*   **functions**, which have parameters of given types and return void or references or objects of a given type;
*   **pointers** to cv void or objects or functions (including static members of classes) of a given type;
*   **references** to objects or functions of a given type;
*   **classes** containing a sequence of objects of various types...
*   **unions**, which are classes capable of containing objects of different types at different times;
*   **enumerations**...
*   **pointers to non-static class members**...

### Slide 25: Today: Some C++ Specifics
*   References
*   Constant types
*   `auto` specifier

### Slide 26: C++ References
**Reference: A synonym to some object**

**Syntax:** `T& r = o;` (Declaration of a reference to an object of type T; initializer denotes an object referenced).

```cpp
int x;
int& r = x; // r becomes synonym to x
...
r = 7;      // the same as x = 7
x = 777;
int v = r;  // v is 777
```

### Slide 27: C++ References Examples
```cpp
void f ( double& a )
{ a += 3.14; }

double d = 7.0;
f(d); // d has the value of 10.14
```
*Compare with `void f ( double a )` where `d` would not change.*

```cpp
int v[20];
int& f ( int i ) { return v[i]; }

f(3) = 7; // now the 4th element of the array v has the value of 7
```

### Slide 28: C++ References - Why do we need them?
To avoid copying large structures when passing them to functions.

*   **Without reference:** `void f(Huge a)` -> The big structure gets copied to `f`.
*   **With reference:** `void f(Huge& a)` -> The reference to the big structure is passed to `f` (no copy).

### Slide 29: C++ References - Some rules
**References are not objects; They are synonyms to some objects.**

*   No pointers to references
*   No arrays of references
*   No references to references
*   No "constant" references

```cpp
int* p;
int*& rp = p; // OK: reference to a pointer

const int x = 7;
int& ri = x; // OK: reference to an integer initialized by a reference to the constant integer
```

### Slide 30: C++ References - Operators
**No specific operators on references – just because references are not objects.**

```cpp
int a;
int& r = a;

r = 3;  // a = 3
r++;    // a++
r+=7;   // a += 7
```

### Slide 31: Pointers vs References: A Comparison

| Feature | Pointers | References |
| :--- | :--- | :--- |
| **Syntax** | Explicitly declared | Explicitly declared |
| **Status** | Pointers are **objects**; they occupy memory | References are **not objects** but synonyms to objects |
| **Value** | Values are **addresses** of objects | References themselves do not have values |
| **Initialization** | Can be non-initialized (null pointers) | Should be initialized; they always refer to an object (no "null" references) |
| **Operators** | Explicit address-of & dereferencing operators | No special operators on references |

### Slide 32: Constant Types
`const T` denotes the set of objects of type `T` that **cannot change their values** - NOTHING ELSE.

*   `T` and `const T` are **different** types.
*   `T` and `const T` represent the same set of values.

**Examples:**
*   `long int`: Set of long integer values
*   `const long int`: Set of long integer constants
*   `myClass`: Set of instances of type `myClass`
*   `const myClass`: Set of constant instances of type `myClass`

### Slide 33: Constants: two kinds
1.  **Compile-time constant:**
    ```cpp
    const int b = 777;
    ```
    777 is the compile-time expression ("constant expression"); the compiler can calculate the value and replace occurrences of `b`.

2.  **Run-time constant:**
    ```cpp
    int a = 5;
    const int x = a+b;
    ```
    `a+b` is a run-time expression; the compiler cannot calculate the value of the initializer.

### Slide 34: Constant Expressions
**Legal contexts for constant expressions:**
`const int x = Expression;`
`float A[x];` (Only constant expressions are legal for array sizes).

*   **OK:** `x` is the "usual" constant.
*   **Error:** cannot change the value of a constant (`x = 5;`).
*   **Error:** cannot declare array with a non-compile-time calculated size.

*Note: some extensions to the notion of constant expression exist (`constexpr` specifier).*

### Slide 35: Constants & Pointers
*   `T* ptr1;` - Pointer to an object of type `T`; no restrictions.
*   `const T* ptr2;` - Pointer to a **constant object** of type `T`; cannot use `ptr2` to modify object pointed to by it.
*   `T* const ptr3 = &v;` - **Constant pointer** to an object of type `T`; cannot modify the value of `ptr3`.
*   `const T* const ptr4 = &pc;` - **Constant pointer** to a **constant object** of type `T`.

### Slide 36: `auto` specifier
**In the past (and in C now):** `auto` was a storage-class specifier.
**Now (C++):** `auto` is the **type-specifier**.

```cpp
auto x = 7;
```
The type of `x` is **deduced** by the compiler from the type of its initializer.
The idea is that the compiler **automatically** determines the type of the object being declared. The process is called **type deducing**.

### Slide 37: `auto` specifier - Deduction Rules
**Common rules for deduction:**
`auto var = some-expression;`

| Type of *some-expression* | Type of *var* |
| :--- | :--- |
| `T*`, `const T*` | `T*`, `const T*` |
| `T`, `const T`, `T&`, `const T&` | `T` (const/ref dropped) |

`auto& var = some-expression;`

| Type of *some-expression* | Type of *var* |
| :--- | :--- |
| `T`, `const T` | `error` (for T), `const T` |
| `T&` | `T&` |

### Slide 38: `auto` specifier: examples
*   `auto x = 7;` -> type of `x` is `int`.
*   `auto a[] = { 1, 2, 3 };` -> type is deduced as `std::initializer_list<int>`.
*   `const auto *v = &x;` -> `v` has type `const int*`.
*   `static auto y = 0.0;` -> `y` has type `double`.
*   `auto int r;` -> **Error**: `auto` is not a storage-specifier anymore.
*   `auto m;` -> **Error**: Needs initializer.
*   `auto a=5, b={1,2};` -> **Error**: Mismatched types/initialization.

### Slide 39: `auto` specifier: examples (Simplification)
**Simplification of syntax!**

Instead of:
```cpp
vector<double*>* v = new vector<double*>(77);
```

You can write:
```cpp
auto v = new vector<double*>(77);
```

### Slide 40: `auto` specifier (Meme)
Would it be possible to write something like as follows:
`auto f(auto, auto) { auto; }`

*C'mon, the compiler infers the rest from the context!*
*[Image Description: Man laughing/facepalming.]*

### Slide 41: Conclusions
**What we have considered today:**
*   Introductory remarks
*   (To remind) Syntax & semantics
*   C++: common words & references
*   (To remind) C/C++ memory model
*   (To remind) The notion of type
*   C++ type system
*   Reference & constant types
*   `auto` specifier -->