<!-- Here is the transcribed content organized by file and slide, including image descriptions and formatted text.

---

# File 1: Lab 2 - C++ Classes, but without OOP

## Slide 1
**Image Description:** Title slide with a dark blue background. The Innopolis University logo is in the top left. The title "Lab 2" is in large white text, followed by a green underline and the subtitle "C++ Classes, but without OOP". The authors (Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer) and course details are at the bottom.

**Text Content:**
**Innopolis University**

# Lab 2
**C++ Classes, but without OOP**

Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer
Software Systems Analysis and Design
Spring Semester 2026

---

## Slide 2
**Image Description:** A slide titled "Agenda" with a green vertical bar next to the title. It lists the topics to be covered in bullet points.

**Text Content:**
# Agenda

*   Recap
*   Code Style
*   Constructors and Destructors
*   Static vs Dynamic Object Declaration
*   Operator Functions
*   Exercises

---

## Slide 3
**Image Description:** A slide titled "Lecture Recap" listing review questions about memory, constructors, destructors, and qualifiers.

**Text Content:**
# Lecture Recap

*   When is the heap memory used? What about stack memory?
*   What is memory leakage, and with which type of memory is it associated?
*   What are the four main types of constructors in C++?
*   Constructors are for initializing an object’s member data, what are the destructors for?
*   What is the difference between `constexpr` and `const`?
*   What is a member function?

---

## Slide 4
**Image Description:** A slide titled "Code Style" focusing on Qt coding standards and CLion settings. It contains hyperlinks to JetBrains and Qt documentation.

**Text Content:**
# Code Style

*   Use Qt’s coding style for C++.
*   On Clion: go to **Settings -> Editor -> Code style -> C/C++ -> Set from…** Choose **Qt**.
*   Find “format code” shortcut based on your OS.
*   Some links: [JetBrains format code](#), [Qt coding style](#)

---

## Slide 5
**Image Description:** A slide titled "Constructors". It displays a C++ code snippet defining `class C` with a public integer `a`, showing a default constructor, a conversion constructor, a copy constructor using `this` pointer, and a two-argument constructor. Line numbers are visible on the left.

**Text Content:**
# Constructors

```cpp
class C
{
public:
    int a;
    C() : a{0} {} // default
    
    C(int i) : a(i) {} // conversion
    
    C(C &other)
    { this->a = other.a; } // copy
    
    C(int i, int j)
    { a = i + j; } // ...
};
```

---

## Slide 6
**Image Description:** A slide titled "Constructors and Destructors". It shows a C++ class `Test` with an integer `x`. It demonstrates a constructor that prints a message when called and initialized `x` to 0, and a destructor `~Test()` that prints a message when the object is destroyed.

**Text Content:**
# Constructors and Destructors

```cpp
class Test
{
public:
    int x;
    Test() : x(0)
    {
        cout << "Constructor is called here" << endl;
    }
    ~Test()
    {
        cout << "Destructor is called" << endl;
    }
};
```

---

## Slide 7
**Image Description:** A slide titled "Dynamic vs Static Object Declaration". It shows a full C++ program structure with `main` and a function `foo`. Inside `foo`, an object `staticTest` is declared statically. The output messages "main starts here" and "main ends here" frame the function call.

**Text Content:**
# Dynamic vs Static Object Declaration

```cpp
#include <iostream>
using namespace std;
class Test {...};

void foo()
{
    Test staticTest; // static declaration
}

int main()
{
    cout << "main starts here" << endl;
    foo();
    cout << "main ends here" << endl;
    return 0;
}
```

---

## Slide 8
**Image Description:** A slide titled "Dynamic vs Static Object Declaration". It modifies the previous code example. Inside `foo`, it now shows dynamic allocation using `new Test()`. It also comments out an alternative way using `auto`.

**Text Content:**
# Dynamic vs Static Object Declaration

```cpp
#include <iostream>
using namespace std;
class Test {...};

void foo()
{
    Test *dynamicTest1 = new Test(); // dynamic declaration
    // auto dynamicTest2 = new Test(); // another option
}

int main()
{
    cout << "main starts here" << endl;
    foo();
    cout << "main ends here" << endl;
    return 0;
}
```

---

## Slide 9
**Image Description:** A slide titled "Task 1". It describes a programming exercise to create a `Box` class with specific requirements regarding member variables and constructors.

**Text Content:**
# Task 1

Write a program that contains a class `Box`.

*   Box should have the length, width, and height as member variables. The variables should be of type `unsigned int`.
*   Box should have three constructors: default, copy, conversion.
*   Box should have the assignment operator.

---

## Slide 10
**Image Description:** A slide titled "Task 2". It lists four member functions (`getVolume`, `scale`, `isBigger`, `isSmaller`) to be added to the `Box` class, with syntax highlighting for return types and arguments.

**Text Content:**
# Task 2

Add and implement the following member functions to the class `Box`:

*   `unsigned getVolume();` // returns the volume of the box.
*   `void scale(unsigned scaleValue);` // multiply each side of the box with scaleValue.
*   `bool isBigger(unknown other);` // this box is larger than the other (you decide what the type should be)
*   `bool isSmaller(unknown other);` // this box is smaller than the other (you decide what the type should be)

---

## Slide 11
**Image Description:** A slide titled "Task 3". It asks to add operator overloads for `*` (multiplication) and `==` (equality) to the `Box` class, describing the expected behavior of each.

**Text Content:**
# Task 3

Add the following operators to the class `Box`: `{ *, ==}`

*   `*` // Box with each side of the original box multiplied with an unsigned integer (scale value).
*   `==` // returns true if the sides of two boxes are the same (they may be shuffled), false otherwise

---

## Slide 12
**Image Description:** A slide titled "Task 4". It asks to create a `Cube` class and a conversion operator to convert a `Cube` into a `Box`.

**Text Content:**
# Task 4

Add another class `Cube`. Add an operator to convert an object of type `Cube` to object of type `Box`.

---

## Slide 13
**Image Description:** The closing slide with "The end." in large white text on a dark blue background. The university logo is in the top left, and footer information is at the bottom.

**Text Content:**
# The end.

Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer
Software Systems Analysis and Design
Spring Semester 2026

---
---

# File 2: Tutorial 2 - Declarations & Initialization in C++

## Slide 1
**Image Description:** Title slide using a comic-style font (likely Comic Sans) in blue and red. The title is "System Software Analysis and Design", subtitle "Tutorial 2: Declarations & Initialization in C++".

**Text Content:**
**System Software Analysis and Design**

Tutorial 2
Declarations & Initialization in C++

Spring Semester 2026
Innopolis University
Eugene Zouev

---

## Slide 2
**Image Description:** A slide listing "The Plan for Today" with four main bullet points about declarations, type conversions, constants, and type specifications.

**Text Content:**
# The Plan for Today

*   Entity declarations
*   Initialization forms
*   Type conversions: basics & improvements
*   More on constants: `constexpr`
*   Type specification simplified

---

## Slide 3
**Image Description:** A transition slide with the text "Entities & Declarations" in orange.

**Text Content:**
# Entities & Declarations

---

## Slide 4
**Image Description:** A slide explaining "C++ Entities & Declarations". It lists types of entities (Value, Object, Reference, Function, Type, Template) with informal definitions in blue text. A side note references ISO Standard Sect 6.1.

**Text Content:**
# C++ Entities & Declarations

*   So, a C++ program consists of a sequence of **declarations**. Each declaration introduces an **entity**.
*   What is C++ entity?
    **Value, object, reference, function, type, template, …** (See the C++ Standard, Sect 6.1, par 3 for the full list of entities)
*   **Informally:**
    *   **Value:** A literal constant
    *   **Object:** A named or unnamed part of memory with a value
    *   **Reference:** A synonym to some object
    *   **Type:** A predefined or user-defined type (class)
    *   **Function:** A sequence of constructs specifying the local context and some actions.

---

## Slide 5
**Image Description:** A slide titled "C/C++: Variable Object Declarations". It shows a code block with variables `x`, `y`, `f1`, `d1`, and `d2`. Red arrows point from the code to text boxes explaining the initialization status and type of each variable.

**Text Content:**
# C/C++: Variable Object Declarations

```cpp
int x;
int y = 0123;
float f1 = 0.1;
double d1, d2 = 0x555;
```

*   **x**: variable becomes available in the current context; The type of `x` is a default integer type; The initial value of `x` is not defined.
*   **y**: variable becomes available in the current context; its type is integer, and the initial value is 83 (0123 octal).
*   **f1**: variable becomes available in the current context; its type is default float, and the initial value is 0.1.
*   **d1, d2**: The single declaration introduces two variables: `d1` and `d2`; their type is `double`; the initial value for `d1` is not specified, and for `d2` is 1365.0 (0x555 hex).

---

## Slide 6
**Image Description:** A slide detailing the "Common form (simplified)" of a declaration. It breaks down the syntax `S T name initializer;` with red arrows identifying parts like Storage class specifier, Type specifier, Name, Initializer, and Delimiter.

**Text Content:**
# C/C++: Variable Object Declarations

**Common form (simplified)**

`S T name initializer;`

*   **S:** Storage class specifier
*   **T:** Type specifier
*   **name:** The name of the object introduced
*   **initializer:** Specifies the initial value of the object
*   **;**: Delimiter

**Notes:**
*   S & initializer can be omitted; in that case, default meaning is assumed.
*   S & T can go in an arbitrary order.
*   Syntax allows several pairs “name/initializer”.
*   “initializer” may have different syntactic forms.

**Semantics of Declaration:**
See the previous slide.

---

## Slide 7
**Image Description:** A slide titled "Four (?) initialization forms". It lists initialization using `=`, `()`, braces `{}` (Since C++11), and braces with equals. It introduces the concept of "Uniform initialization" (braced-init-list).

**Text Content:**
# Four (?) initialization forms

```cpp
int y = 0;      // initializer after ‘=‘
int x(0);       // initializer in parentheses
int z { 0 };    // initializer in braces (Since C++11)
int t = { 0 };  // initializer in braces with ‘=‘
```

**Uniform initialization**
The idea was to define a syntax construct that could represent **all possible kinds** of initialization.
The syntax construct is **braced initialization** (to be more precise, *braced-init-list*).

---

## Slide 8
**Image Description:** A slide discussing "Uniform initialization". It shows two examples: one showing how braces prevent narrowing conversions (error with `int sum1 {x+y+z}`), and another showing that empty braces `{}` correctly initialize objects, whereas empty parentheses `()` declare functions (the "Most Vexing Parse").

**Text Content:**
# Uniform initialization

More things become possible with `{ }`. Here are just two of them:

**No narrowing conversions**
```cpp
double x, y, z;
...
int sum2(x+y+z);    // OK, but data loss
int sum3 = x+y+z;   // OK, but data loss
int sum1 { x+y+z }; // Error: More careful checks
```

**Object vs Function Declaration**
```cpp
class C { ... };

C c1();    // not object but function declarations
int x1();  

C c2{};    // OK: object declarations ☺
int x2{};
```

**References:**
*   ISO Standard, Section 11.6.4
*   Scott Meyers, Effective Modern C++, O’Reily.

---

## Slide 9
**Image Description:** A slide listing "Nineteen (!!) initialization forms". It displays a long list of code examples showing different ways to initialize integers and auto variables, noting which ones work, which are errors, and referencing Nicolai Josuttis.

**Text Content:**
# Nineteen (!!) initialization forms ☺

```cpp
int i1;              // undefined value
int i2 = 42;         // note: inits with 42
int i3(42);          // inits with 42
int i4 = int(42);    // inits with 42
int i5{42};          // inits with 42
int i6 = {42};       // inits with 42
int i7{};            // inits with 0
int i8 = {};         // inits with 0
auto i9 = 42;        // inits with 42
auto i10{42};        // C++11: std::initializer_list<int>, C++14:int
auto i11 = {42};     // inits std::initializer_list<int> with 42
auto i12 = int{42};  // inits int with 42
int i13();           // declares a function
int i14(7, 9);       // compile-time error
int i15 = (7, 9);    // OK, inits int with 9 (comma operator)
int i16 = int(7, 9); // compile-time error
int i17(7, 9);       // compile-time error
auto i18 = (7, 9);   // OK, inits int with 9 (comma operator)
auto i19 = int(7, 9);// compile-time error
```

*Nicolai Josuttis - The author of «C++ Templates»*

---

## Slide 10
**Image Description:** A transition slide with the text "Type Conversions: Some improvements" in orange.

**Text Content:**
# Type Conversions
**Some improvements**

---

## Slide 11
**Image Description:** A slide explaining "Type Conversions". It distinguishes between "standard" and "user-defined" conversions. It lists examples of standard conversions (array-to-pointer, int to boolean) and mentions conversion functions for user-defined types.

**Text Content:**
# Type Conversions

Two kinds of type conversions are defined in the C++ language:
**standard** and **user-defined**

**Standard:**
See Section 7.3 of the ISO C++ Standard for the full set and explanation of standard conversions.
Some examples are:
*   array-to-pointer
*   integer to boolean
*   double to long integer
*   pointer to a derived class to pointer to the base class
*   ...

**User-defined:**
The user can define his/her **own conversion rules** for user-defined types (classes). The language feature is called **conversion functions**. (See the lecture).

Standard and user-defined conversions can be combined (by some rules) within the same expression.

---

## Slide 12
**Image Description:** A slide showing "The problem with uncontrolled type conversions". It shows a function `foo(double x)` accepting inputs like `3` (int) and `true` (bool). It then shows the solution using `delete` to explicitly forbid `int` and `bool` overloads.

**Text Content:**
# Type Conversions

The problem with **uncontrolled** type conversions:

```cpp
void foo(double x) { ... }

foo(3.14);  // OK: double literal gets passed to the function
foo(3);     // OK: integer literal gets converted to double and passed
foo(true);  // OK: boolean literal gets converted to double and passed
```

How to **restrict** such a freedom?
**Explicitly forbid variants that are not desirable!**

```cpp
void foo(double x) { ... }
void foo(int) = delete;
void foo(boolean) = delete;

foo(3.14);   // OK
foo(3);      // Error
foo(true);   // Error
```

**Function overloading:** the existence of several functions with the same name but with different signatures.

---

## Slide 13
**Image Description:** A slide asking how to restrict freedom even more. It demonstrates using a template that is deleted `template<typename T> void foo(T) = delete;` to prohibit *any* conversion except the specific `double` overload provided.

**Text Content:**
# Type Conversions

How to restrict such a freedom **even more**:
To **prohibit any kind of conversion** except just one?

```cpp
template<typename T>
void foo(T) = delete;

void foo(double x) { ... } // Accepts double, const double, double& etc.

foo(3.14);    // OK: double literal gets passed to the function
foo(3);       // Compile-time error: instantiation foo<int> is “deleted”
foo(true);    // Compile-time error: instantiation foo<boolean> is “deleted”
foo(A());     // Compile-time error: instantiation foo<A> is “deleted”
```

---

## Slide 14
**Image Description:** A transition slide with the text "`constexpr` specifier" in blue and orange.

**Text Content:**
# `constexpr` specifier

---

## Slide 15
**Image Description:** A slide titled "(More on) Constant Expressions". It compares `const int x` (Any-expression) with `constexpr int y` (A-constant-expression). It notes that `constexpr` was introduced in C++11 and implies `const`.

**Text Content:**
# (More on) Constant Expressions

```cpp
const int x = Any-expression; 
// In general, cannot be used in context requiring constant-expressions

constexpr int y = A-constant-expression; // Since C++11
// Can be used in contexts requiring constant expressions
```

**Informally:**
Constant expression is an expression whose value can be calculated at compile time.
(See ISO Std 5.20 for more precise definition).

**Note:** Generally, `constexpr` implies `const`.

---

## Slide 16
**Image Description:** A slide showing a code example of `constexpr` in a `struct A`. It highlights a `constexpr` constructor and shows valid and invalid usages based on whether the input is constant.

**Text Content:**
# Constant Expression: An Example

```cpp
int x; // not constant

struct A {
    constexpr A(bool b) : m(b?42:x) { }
    int m;
};

constexpr int v = A(true).m;  
// OK: constructor call initializes m with the value 42

constexpr int w = A(false).m; 
// Error: initializer for m is x, which is non-constant
```

The real value of `constexpr` is as a **guarantee** that the value will be computable at compile-time.
(ISO Std, Section 5.20, §2.20)

---

## Slide 17
**Image Description:** A slide titled "`constexpr`-functions". It explains that functions can be `constexpr`. The example compares `Sqr1` (constexpr) and `Sqr2` (normal int), showing that only `Sqr1` can be used to initialize a `constexpr` variable.

**Text Content:**
# `constexpr`-functions

Not only objects, but also **functions and constructors** can be declared with `constexpr`.
The main idea behind this is that such functions (calls to these functions) **can be used in constant expressions**.

**Example:**
```cpp
constexpr int Sqr1(int arg) { return arg * arg; }
int Sqr2(int arg) { return arg * arg; }

constexpr int s1 = Sqr1(5); // OK
constexpr int s2 = Sqr2(5); // Error
```

---

## Slide 18
**Image Description:** A slide detailing the requirements for `constexpr` functions. It lists rules: non-virtual, single return statement, arguments/return type must be literal types, and constructors only use init-lists.

**Text Content:**
# `constexpr`-functions

**`constexpr` specifier:**
*   Applies to both member and non-member functions, and for constructors;
*   Declares that the function can be used in constant expressions;

**Requirements on `constexpr`-functions:**
*   It must be non-virtual;
*   Its body should contain the single return statement;
*   The arguments and return type must be of literal types (i.e., typically scalar types or aggregates of those);
*   For constructors, only init-list is allowed.

---

## Slide 19
**Image Description:** A slide titled "One more example". It shows a template class `list<int N>`. It demonstrates passing the result of a `constexpr` function `sqr1(X)` as a template argument, while `sqr2(X)` fails.

**Text Content:**
# One more example

```cpp
template<int N>
class list { }

constexpr int sqr1(int arg) { return arg * arg; }
int sqr2(int arg) { return arg * arg; }

int main()
{
    const int X = 2;
    list<sqr1(X)> mylist1; // OK: sqr1 is constexpr
    list<sqr2(X)> mylist2; // Error: sqr2 is not constexpr
    return 0;
}
```

---

## Slide 20
**Image Description:** A slide asking "`const` & `constexpr` together?". It explains that `constexpr` implies `const` for objects, so using both is redundant on the object itself. However, it shows a pointer example `constexpr const int *NP` where they apply to different parts (pointer vs pointee).

**Text Content:**
# `const` & `constexpr` together?

In most cases, it doesn’t make sense when both specifiers apply to the same object:
`constexpr` for objects always implies `const`.

```cpp
constexpr const int N = 5; // Always the same as below
constexpr int N = 5;
```

However, it can be necessary if specifiers apply to **different parts** of a declaration:

```cpp
static constexpr int N = 3;
int f()
{
    constexpr const int *NP = &N; 
    // constexpr applies to the pointer (NP)
    // const applies to the data (*NP)
}

constexpr void f() const; 
// constexpr applies to function
// const applies to 'this'
```

---

## Slide 21
**Image Description:** A transition slide with the text "How Types are Specified in C/C++?" in orange.

**Text Content:**
# How Types are Specified in C/C++?

---

## Slide 22
**Image Description:** A slide explaining complex type specifications. It shows a complex pointer declaration `int (*(a4[10]))(int);` and simplifies it using `typedef` and the newer `using` declaration. It ends with a home exercise in a red box.

**Text Content:**
# Type Specifications

Does it seem too cryptic? ☺
There are two ways to make specifications of complex types simpler...

**Example:**
`int (*(a4[10]))(int);`
*Type of `a4` is array of 10 elements of type pointer to function with one integer parameter and return type is integer.*

**The first way (came from C): `typedef` specifier**
```cpp
typedef int (*PtrFun)(int);
PtrFun a4[10];
```
*Here, `PtrFun` is **not an object** but a **synonym of some type** – namely the type “pointer to function”.*

**The second way: `using` declaration**
```cpp
using PtrFun = int (*)(int);
PtrFun a4[10];
```

**The home exercise:**
Try to define the type “array of 10 pointers to functions” using `using` declaration.

---
---

# File 3: Lecture 2 - Introduction to Classes without OOP

## Slide 1
**Image Description:** Title slide in blue and red text. "Lecture 2: Introduction to Classes without OOP".

**Text Content:**
**System Software Analysis and Design**

Lecture 2
**Introduction to Classes without OOP**

Spring Semester 2026
Innopolis University
Eugene Zouev

---

## Slide 2
**Image Description:** A slide titled "What Do We Know By Now". It lists concepts covered previously: Types (atomic, compound), Qualifiers (constant), arrays, pointers, references, and type conversions.

**Text Content:**
# What Do We Know By Now

*   The notion of type;
    Predefined & user-defined types;
    Atomic & compound types;
    Basic types & type modifiers
*   Constant types;
    Array types
    Pointer types
    Reference types
*   Type conversions

---

## Slide 3
**Image Description:** A slide titled "What Shall We Discuss Today". It lists: User-defined types (classes), questions about object types, and Classes in C++.

**Text Content:**
# What Shall We Discuss Today

*   User-defined types: the first view at classes
*   What do we need to know about object types?
*   Classes in C++

---

## Slide 4
**Image Description:** A slide defining "C++ Classes". It lists three views of a class: Compound type, User-defined type behaving like predefined types, and basis for OOP. A code box shows a `class Point`. A sidebar lists "Encapsulation, Inheritance, Polymorphism".

**Text Content:**
# C++ Classes
**What is class? - the very first view**

1.  A user-defined **compound type**
2.  A user-defined type that **might behave by the same rules** as predefined types
3.  A basis for **object-oriented software design & development** (Encapsulation, Inheritance, Polymorphism)

```cpp
class Point
{
    double x;
    double y;
};
Point p1, p2;
```
*“Class is a type” – ISO Std, Chap.9*

---

## Slide 5
**Image Description:** A slide titled "What Do We Need To Know About Object Types?". It lists 8 questions covering Declaration, Creation, Removal, Copying, Assignment, Moving, Conversion, and Usage. Green text notes that C++ provides explicit answers to these, unlike other languages where defaults are assumed.

**Text Content:**
# What Do We Need To Know About Object Types?

1.  How to **declare** objects of a given type? *(Yes, we know how to do that: via object declaration)*
2.  How to **create** objects of a given type?
3.  How to **remove** objects of a given type?
4.  How to **copy** objects of a given type?
5.  How to **assign** objects (a value of) a given type?
6.  How to **move** (values of) objects of a given type?
7.  How to **convert** objects of a given type to (values of) objects of some other type? *(Yes, we know how to do that: via type conversion)*
8.  How to **work** with objects of a given type?

*C++ gives **explicit** and **precise** answers: for all kinds of types – both standard and user-defined.*

---

## Slide 6
**Image Description:** A slide for "Point 1: How to Declare Objects?". It explains static (`T v = expression;`) and dynamic (`T v {expression}`) declaration semantics, separating "Static semantics" (compiler view) from "Dynamic semantics" (runtime view).

**Text Content:**
# Point 1: How to Declare Objects?

`T v = expression;`
`T v {expression};`

**Static semantics:** (How compiler treats the declaration)
*   Add new name (v) to the current context; make it available to following program constructs.

**Dynamic semantics:** (What happens while program is running)
*   Allocate memory for the new object (in stack).
*   Calculate expression from the expression.
*   Perform type conversion(s) to T, if necessary.
*   Store the value of the expression in v.

---

## Slide 7
**Image Description:** A slide covering Points 2 & 3: Create/Remove Objects. It contrasts `int x = 7;` (Stack/Static lifetime) with `int* p = new int(7);` (Heap/Dynamic lifetime). It explains that stack objects die at end of scope, while heap objects exist until `delete`.

**Text Content:**
# Points 2,3: How to Create/Remove Objects?
**Two ways for creating objects: static & dynamic**

```cpp
{
    int x = 7;
    int* p = new int(7); // Common notation: new T(expr)
    ...
    delete p;
}
```

**Object x:**
*   Is created **by its declaration** (in stack).
*   Is accessed **by its name**;
*   Exists **until the end of the scope** where it was created (**statically** determined lifetime)

**Object pointed to by p:**
*   Is created by the **explicit creation operator** (in heap).
*   It is **unnamed object**; is accessed via the pointer.
*   Exists until the **explicit deletion operator** is performed (**dynamically** determined lifetime) – or until the whole program terminates.

---

## Slide 8
**Image Description:** A slide applying Creation/Removal to "user-defined types". It shows `class Point` and explains that special member functions (Constructors/Destructors) handle this.

**Text Content:**
# Points 2,3: How to Create/Remove Objects?
**And what about user-defined types?**

```cpp
class Point {
    int x;
    int y;
};

{
    Point* p1 = new Point();    // Default constructor
    Point* p2 = new Point(7);   // Constructor
    ...
    delete p1;                  // Destructor
}
```

**The C++ answer:**
A developer of a user-defined type can **explicitly specify semantics** for creating and destroying objects of that type.
*Special member functions that can be defined as parts of a class.*

---

## Slide 9
**Image Description:** A slide covering Points 4 & 5: Copy/Assign. It uses `float` examples to distinguish Initialization (`float y = x1`) from Assignment (`y = x2`). A red box highlights that Initialization deals with object creation, while Assignment works with existing objects.

**Text Content:**
# Points 4,5: How to Copy/Assign Objects?
**For objects of fundamental types, it seems trivial:**

```cpp
{
    float x1 = 7.7, x2 = 8.8;
    ...
    float y = x1;   // Initialization
    y = x2;         // Assignment
}
```

**Why make the difference??**
*   **Initialization** deals with the object being created.
*   **Assignment** works with the object that was created before.

---

## Slide 10
**Image Description:** A slide applying Copy/Assign to `class Point`. It identifies default constructors, copy initialization, and user-defined assignment operators.

**Text Content:**
# Points 4,5: How to Copy/Assign Objects?
**What about objects of user-defined types?**

```cpp
class Point { ... };

{
    Point a;        // Object declaration without initialization (Default constructor)
    Point b = a;    // Object declaration with initialization (Constructor)
    
    Point c;
    c = a;          // Assignment (User-defined assignment operator !!)
}
```

**The C++ Answer:**
A developer of a user-defined type can **explicitly specify semantics for copying and assignment** for objects of that type.

---

## Slide 11
**Image Description:** A slide for "Point 6: How to Move Objects?". It introduces the concept of Moving (Copying value + Removing from recipient). It distinguishes "Moving while initialization" and "Move assignment".

**Text Content:**
# Point 6: How to Move Objects?

**Moving:** Passing a value of an object to some other object.
Can be treated as:
(a) Copying the value, and
(b) Removing the value from the recipient.

Keeping in mind the initialization vs assignment distinction, it’s reasonable to separate the idea of movement into two:
*   **Moving while initialization**
*   **Move assignment**

*The importance of the “move” notion is really actual for objects of user-defined types.*

---

## Slide 12
**Image Description:** A slide covering Point 7: Conversions. It shows Implicit (`int i = 5.6`) vs Explicit (`(char*)p`) conversions. It lists standard conversions (int to double) and asks about user-defined ones.

**Text Content:**
# Point 7: How to Convert Objects?

An object of some type can be converted to an object of some other type... **implicitly** or **explicitly**.

```cpp
float v = 777;
int i = 5.6;     // Implicit

int x = 77;
int* p = &x;
char* pc = (char*)p; // Explicit. Is it safe???
```

**Explicit conversion notations:**
*   Old C-style: `(T)expression`
*   New functional-style: `T(expression)` -> `v = float(7);`

**Standard conversions:** Integer to double, Integer to boolean, Array to pointer, etc.

---

## Slide 13
**Image Description:** A slide applying Conversions to `class Point`. It shows code attempts to initialize a Point with an integer and assign an integer to a Point, stating that developers can specify these semantics.

**Text Content:**
# Point 7: How to Convert Objects?
**How to convert objects of user-defined types?**

```cpp
class Point { ... };
...
{
    Point a(5); // Is it possible to initialize a class object by an integer?
    int m = a;  // Is it possible to initialize an integer by a class object?
    
    Point c;
    c = 1;      // Is it possible to convert integer to a class object?
}
```

**The C++ answer:**
A developer of a user-defined type can **explicitly specify semantics for initializations and conversions** for that type.

---

## Slide 14
**Image Description:** A slide covering Point 8: Working with Objects. It discusses access (name vs pointer) and manipulation (standard operators). It asks if arithmetic operators (`+`) can be applied to `Point` objects.

**Text Content:**
# Point 8: How Work With Objects?

1.  **How to access objects:**
    *   By its name (for statically defined ones)
    *   Via a pointer to it (for dynamically created ones)

2.  **How to manipulate objects:**
    *   Using operators defined for the object’s type
    *   Using user-defined operations

```cpp
class Point { ... };
...
{
    Point a1, a2;
    a1 = a1 + 1;    // Is it possible to apply arithmetic operators?
    a2 = a2 + a1;   // to objects of user-defined types??
}
```

---

## Slide 15
**Image Description:** A slide answering the previous question. It states that developers can define semantics for standard operators.

**Text Content:**
# Point 8: How Work With Objects?

**The C++ Answer:**
A developer of a user-defined type **can define his/her own semantics for standard operators** for objects of that type.

---

## Slide 16
**Image Description:** A slide categorizing C++ Class Members. It lists: Ordinary members (State), Member functions (Behavior), and Special member functions (Constructors, Destructor, Operator functions, Conversion functions).

**Text Content:**
# C++ Classes
**Which kinds of class members are there in C++?**

*   **(Ordinary or data) members** -> Object **state**
*   **Member functions** -> Object **behavior**
*   **Special** member functions:
    *   **Constructors** -> The ways objects **get created**
    *   **Destructor** -> The way objects **get destroyed**
    *   **Operator functions** -> The ways objects participate in **operations**
    *   **Conversion functions** -> The ways objects **get converted**

---

## Slide 17
**Image Description:** A slide showing a `class Point` declaration with data members `x, y`, a method `Move`, a default constructor, and a parameterized constructor. It annotates the code parts with their definitions (members, methods, constructors).

**Text Content:**
# C++ Classes

```cpp
class Point
{
    double x, y;
    void Move(double dx, double dy) {
        x += dx; y += dy;
    }
    Point() { // default constructor
        x = 0.0; y = 0.0;
    }
    Point(double x0, double y0) {
        x = x0; y = y0;
    }
};
Point p1; // default ctor
Point p2(1.5, 3.5); // 2nd ctor
Point* p = new Point(); // default ctor
```

*   **Class members:** represent the structure/state.
*   **Class member functions ("methods"):** specify operations/behavior.
*   **Constructors:** specify actions taken on object creation.

---

## Slide 18
**Image Description:** A slide discussing access to members. It shows code attempting to access `p1.x` and `p->y`. It notes "A problem is here..." with a sad face, implying access control issues.

**Text Content:**
# C++ Classes
**How to get access and work with class objects?**

1.  **Copying objects:** `p1 = p2;`
2.  **Getting (direct) access to object’s members:**
    ```cpp
    p1.x = 0.5;
    double v = p2.y;
    p->y += 1.0;
    ```
3.  **Working with objects via member functions:**
    ```cpp
    p1.Move(0.5, 0.5);
    ```

**A problem is here... ** (Implicitly referring to default private access).

---

## Slide 19
**Image Description:** A slide explaining `public` and `private` keywords. It circles the private part (data) as "Class implementation" and the public part (methods) as "Class interface".

**Text Content:**
# C++ Classes: public & private members

```cpp
class Point
{
private: // Class implementation
    double x, y;
public:  // Class interface
    void Move(...) { ... }
    Point() { ... }
    ...
};
```

**The rule:**
*   Members specified as **private** are not accessible by users of the class objects (only from within the class itself).
*   Members specified as **public** are accessed by the users of the object (are “visible” from outside).

---

## Slide 20
**Image Description:** A slide showing the syntax for accessing members: `name.member` and `ptr->member`. It suggests a pattern: make data private, access via public functions.

**Text Content:**
# C++ Classes: Access to Members

**The common notation for accessing public members:**

1.  Via the object name: **`name.member`**
2.  Via the pointer to an object: **`ptr->member`**

**The usual “pattern”:**
*   Make data members **private**
*   Allow access to data members only via **member functions**.

---

## Slide 21
**Image Description:** A slide showing "Partial access". It adds `getX()` and `getY()` getters to the class. It shows that direct access `p1.x` is an error, while `p->getX()` is OK.

**Text Content:**
# C++ Classes: Access to Members
**How to make a partial access to object members – that is, to be able only to read their values but not modify?**

```cpp
class Point {
    ...
    double getX() { return x; }
    double getY() { return y; }
};

p1.x = 7.7;         // error
double w = p2.getY(); // ok
double z = p->getX(); // ok
```

---

## Slide 22
**Image Description:** A slide listing types of constructors in C++. It shows a `class C` with examples of Default, Conversion (`int`), Copy (`C&`), and "Other" (`int, int`) constructors.

**Text Content:**
# Classes & Constructors
**Which kinds of constructors are there in C++?**

*   **Default** constructor
*   **Copy** constructor
*   Move constructor (grayed out)
*   **Conversion** constructor
*   Other constructors

```cpp
class C {
    int a;
    C() { a = 0; }            // Default constructor
    C(int i) { a = i; }       // Conversion constructor
    C(C& c) { a = c.a; }      // Copy constructor
    C(int i, int j) { ... }   // Other
};
```

---

## Slide 23
**Image Description:** A slide showing object creation. It compares Java (dynamic only) with C++ (static `C c;` and dynamic `new C()`).

**Text Content:**
# Classes & Constructors
**How to create objects of user-defined types?**
*   By declaring them (“static” way)
*   By creating them (“dynamic” way)

**Note:** There is the only one way to create class objects in Java: dynamic.

```cpp
class C { ... }; // Class declaration

C c;             // Object declaration (Static)
C* pc = new C(); // New operator (Dynamic)
```
*Default constructors are invoked in both cases.*

---

## Slide 24
**Image Description:** A slide showing when different constructors are called. `c1` calls default, `c2(1)` calls conversion, `c3(c2)` calls copy.

**Text Content:**
# Classes & Constructors
**When and how various kinds of constructors are used (called)?**

```cpp
class C { ... };

C c1;           // Default constructor
C c2(1);        // Conv. constructor
C c3(c2);       // Copy constructor
C c4(7,8);
```

---

## Slide 25
**Image Description:** A slide illustrating differences in initialization syntax. It points out that `C c3();` is a function declaration. It shows chains like `C c6 = C(1)` (Conversion + Copy). It introduces `C c1{1,2}` notation.

**Text Content:**
# Classes & Constructors
**What’s the difference between…**

*   `C c1;` -> Default constructor
*   `C c2 = C();` -> Default constructor + copy constructor
*   `C c3();` -> **Function declaration! ☺**
*   `C c4(1);` -> Conversion constructor
*   `C c5 = 1;` -> Conv. constructor + copy constructor
*   `C c6 = C(1);` -> Conversion constructor
*   `C c7(c6);` -> Conversion constructor (?) *Note: Likely typo in OCR/Image, context implies Copy constructor*
*   `c8 = 2;` -> Conv. constructor + Assignment operator

**New notation:** `C c1{1,2};`

---

## Slide 26
**Image Description:** A slide showing a "conceptual scheme" where temporary objects are created and then copied. For example, `C c3 = 1` conceptually uses the Conversion constructor to make a temp, then Copy constructor to make `c3`.

**Text Content:**
# Classes & Constructors

**A conceptual scheme:** create a temp object and then use it to create another object (by copying it).

```cpp
class C { ... };

int main() {
    C c1;        // Default ctor
    C c2(1);     // Conversion ctor
    C c3 = 1;    // Conversion ctor + Copy ctor
    C c4 = C(1); // Conversion ctor + Copy ctor
    C c5 = C();  // Default ctor + Copy ctor
    ...
}
```

---

## Slide 27
**Image Description:** A slide explaining compiler optimization. The code shows output statements in constructors. It notes that while the conceptual scheme implies temp objects, the compiler *must* (in many cases) create the object directly, omitting the copy constructor.

**Text Content:**
# Classes & Constructors

**Compiler must create the new object directly (without using a temp object)**

```cpp
// ... definitions with cout ...
int main() {
    C c3 = 1;    // Conversion ctor; no copy ctor!
    C c4 = C(1); // Conversion ctor; no copy ctor!
    C c5 = C();  // Default ctor; no copy ctor!
}
```
*It’s allowed for a compiler to create the new object directly.*

---

## Slide 28
**Image Description:** A slide showing that even if the copy constructor is optimized away, accessibility checks still happen. If the Copy Constructor is `private`, lines like `C c4 = C(1);` generate errors.

**Text Content:**
# Classes & Constructors

```cpp
class C {
    ...
private:
    C( C& c ) ... // Copy ctor is private
};

int main() {
    C c3 = 1;    // Error: copy ctor is private!
    C c4 = C(1); // Error: copy ctor is private!
    ...
}
```
*Compiler treats this as error even if the copy ctor is not really used!*

---

## Slide 29
**Image Description:** A slide introducing "Operator Functions". It explains that C++ allows introducing operator versions for user-defined types.

**Text Content:**
# C++ Classes: Operator Functions

*   The C++ type system is heterogeneous: two kinds of types (predefined and user-defined types) in general behave differently. In particular, there is a set of predefined operators for predefined types.
*   However, it's allowed to introduce the versions of the operators for user-defined types (classes).

---

## Slide 30
**Image Description:** A slide comparing a named function `moveDia` with `operator+=`. Both perform `x += v; y += v;`.

**Text Content:**
# C++ Classes: Operator Functions

**The idea:** suppose we want to define a way to move a point by some distance across the diagonal.

**Named function:**
`void moveDia(double v) { x += v; y += v; }`

**Operator function:**
`void operator+=(double v) { x += v; y += v; }`

We can specify the same action introducing operator `+=` for (objects of) our class!

---

## Slide 31
**Image Description:** A side-by-side comparison of usage. `p.moveDia(0.5)` vs `p += 0.5`.

**Text Content:**
# C++ Classes: Operator Functions

**Using function:**
```cpp
Point p(1.5, 3.5);
p.moveDia(0.5);
```

**Using operator:**
```cpp
Point p(1.5, 3.5);
p += 0.5;
```

---

## Slide 32
**Image Description:** A slide showing a "More common picture" of operator overloading. It includes `operator+` (returning new object), `operator[]` (subscripting), and `operator()` (function call).

**Text Content:**
# C++ Classes: Operator Functions

```cpp
class C {
    int member;
public:
    C& operator+(C& c1) { return C(member+c1.member); }
    int operator[](int p) { return member-p; }
    int operator()(int p) { return member+p; }
};

C sum = c1+c2;  // ≡ c1.operator+(c2);
int inc = sum[1]; // ≡ sum.operator[](1);
int dec = sum(3); // ≡ sum.operator()(3);
```

---

## Slide 33
**Image Description:** A slide explaining the common syntax `T operator OpSign (...)`. It lists rules: Arity and preference cannot change, no new operators can be created, but common ones (including `new`, `delete`, `[]`, `()`) can be redefined.

**Text Content:**
# C++ Classes: Operator Functions

**Common syntax**
`T operator OpSign ( Parameters ) { Actions }`

*   Operator’s **arity** and **preference** shouldn’t change.
*   It’s **not allowed** to introduce **new** operators. (Extendable but not modifiable).
*   All operators of “common use” can be redefined (+, -, *, /, …) AS WELL AS operators like indexing `[]`, function calls `()`, `new` and `delete` operators.

---

## Slide 34
**Image Description:** A slide introducing "Conversion Functions". It asks if a user-defined object can be used in an `if` condition like a boolean.

**Text Content:**
# C++ Classes: Conversion Functions

**Example with a predefined type**
```cpp
void f() {
    int a = expression;
    if ( a > 0 ) ...
}
```
By definition, the if condition must be `boolean`.

*Can we use an object of a user-defined type in such a condition?*
*Can we make the behavior of an object of a user-defined type similar to that of a predefined type?*

---

## Slide 35
**Image Description:** A slide showing `operator bool()`. It demonstrates that defining this allows `if (c1)` to work.

**Text Content:**
# C++ Classes: Conversion Functions

```cpp
class C {
    int member;
public:
    operator bool() { return member != 0; } // Conversion function
};

void f() {
    C c1(1);
    if ( c1 ) // ≡ if ( c1.operator bool() )
        Do something
}
```

---

## Slide 36
**Image Description:** A slide showing the syntax for conversion functions: `operator TargetType()`. It notes there is no return type specified (it's inferred) and no parameters.

**Text Content:**
# C++ Classes: Conversion Functions

**Common syntax**

`operator TargetType() { Actions }`

*   No result type.
*   No parameters, but still empty parentheses.

---

## Slide 37
**Image Description:** A slide about Destructors. It defines their purpose (release resources/memory). It shows implicit calls (end of scope) and explicit calls `delete pc`. It also shows a syntax `c.C::~C()` which calls the destructor but leaves the object existing (dangerous).

**Text Content:**
# Constructors & Destructors

**What is destructor for?** – to destroy the object
*   To release resources the object has acquired
*   To release memory the object occupied

```cpp
class C { ... ~C() { ... } };

void f() {
    C c;        // Implicit object creation
    C* pc = new C(); // Explicit object creation
    
    c.C::~C();  // Compiler-generated destructor call (explicit call here)
    // Object pointed to by pc still exists
}
```

---

## Slide 38
**Image Description:** A slide discussing "Explicit destructor calls". It marks automatic destruction as "Not recommended" if manually called before. It shows `delete pc` as the recommended way for dynamic objects.

**Text Content:**
# Constructors & Destructors
**Explicit destructor calls**

```cpp
void f() {
    C c;
    C* pc = new C();
    
    c.C::~C();      // Not recommended: c will be destroyed automatically later.
    
    delete pc;      // Recommended
    pc->C::~C();    // Not recommended
}
```

---

## Slide 39
**Image Description:** A slide distinguishing Conversion Constructors (Other Type -> Class) from Conversion Functions (Class -> Other Type).

**Text Content:**
# Constructors & Conversions

**Conversion constructors & conversion functions**

```cpp
class C {
    C(int i) { ... }      // Conversion constructor: to convert some type to user-defined type
    operator bool() { ... } // Conversion function: to convert user-defined type to some other type
};

C c = C(1);
if ( c ) { ... }
```

---

## Slide 40
**Image Description:** A slide showing ambiguity. If Class A has a constructor taking B, and Class B has a conversion operator to A, `A a = b;` is ambiguous.

**Text Content:**
# Constructors & Conversions
**Ambiguity**

```cpp
class B;
class A {
    A ( B& b ) { ... } // Conversion constructor: B -> A
};
class B {
    operator A() { ... } // Conversion function: B -> A
};

B b;
A a = b; // Ambiguity!
// What to apply? A(b) or b.operator A()?
```

---

## Slide 41
**Image Description:** A slide titled "Classes & Fundamental Types". It argues that C++ makes classes similar to fundamental types. It compares Initialization: `int i(1)` vs `C c(1)`.

**Text Content:**
# Classes & Fundamental Types

The great idea of C++: to make user-defined types (classes) **very similar** to fundamental types.

**1) Initialization**

```cpp
int i(1);
C c(1);
C c1(c);
```
*Declaration of an object of the predefined type: standard semantics.*
*Conversion & copy constructors.*

---

## Slide 42
**Image Description:** A slide comparing Assignment. `i = 7` vs `c = 7` (using assignment operator).

**Text Content:**
# Classes & Fundamental Types

**2) Assigning new values**

```cpp
i = 7;      // Predefined assignment operator
c = 7;      // Assignment operator for objects of type C
c1 = c2;
```

---

## Slide 43
**Image Description:** A slide comparing Expressions. `i = k+m` vs `c = c1+c2` (using `operator+`).

**Text Content:**
# Classes & Fundamental Types

**3) Expressions**

```cpp
i = k+m;    // Predefined + operator
c = c1+c2;  // User-defined plus operator
```

---

## Slide 44
**Image Description:** A slide comparing Conversions in boolean contexts. `if (i)` vs `if (c)` (using `operator bool`).

**Text Content:**
# Classes & Fundamental Types

**4) Conversions**

```cpp
if ( i ) ... // Standard conversion int -> bool
if ( c ) ... // User-defined conversion function C -> bool
```

---

## Slide 45
**Image Description:** A slide summarizing the similarity. It shows a class `C` with constructors, assignment, arithmetic, and conversion operators, effectively mocking an integer.

**Text Content:**
# Classes & Fundamental Types

This class behaves (almost) exactly as other fundamental types; it can be used everywhere together with other types.

```cpp
class C {
    int m;
public:
    C(int i) { m = i; }
    C(C& c) { m = c.m; }
    C& operator=(C& c) { m = c.m; }
    C& operator+(C& c) { return m+c.m; }
    operator bool() { return m != 0; }
};
```
*What else: Relational operators; Conversions to other types; Similar support for unknown types (!?)*

---

## Slide 46
**Image Description:** The final summary slide listing the key takeaways of the lecture.

**Text Content:**
# Summary

*   What do we need to know about object types?
*   Two ways for creating objects
*   Initialization vs assignment
*   Class as a user-defined compound type
*   Class members; access to members
*   Constructors & destructors
*   Special member functions:
    *   operator functions
    *   conversion functions
*   Classes & fundamental types: difference & similarity -->