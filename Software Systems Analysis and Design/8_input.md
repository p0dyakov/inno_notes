Here is the complete, line-by-line transcript of the provided presentations, beautifully formatted using Markdown, divided by files and individual slides, with detailed descriptions of all images, diagrams, and code structures.

---

# File 1: Tutorial 9 - Design Patterns

## Slide 1
**System Software Analysis and Design**
Tutorial 9
**Design Patterns**
**Introduction by Program Examples**

Spring Semester 2026
Innopolis University
Munir Makhmutov

## Slide 2
**Agenda**

*   Singleton
*   Prototype
*   Builder

2/26

## Slide 3
**Design Patterns: Taxonomy**

*   **Creational:** Deal with the best way to create instances of objects.
*   **Structural:** Describe how classes and objects can be combined to form larger structures.
*   **Behavioral:** Are concerned with the assignment of responsibilities between objects, or, encapsulating behavior in an object and delegating requests to it.

*[Image Description: A diagram categorizing design patterns into three main groups, displayed in blue rectangular boxes with lists of patterns inside. The "Creational" box contains: Abstract Factory, Singleton (highlighted in red), Factory Method, Builder (highlighted in red), and Prototype (highlighted in red). The "Structural" box contains: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. The "Behavioral" box contains: Chain of Responsibility, Command (undo/redo), Interpreter, Iterator, Mediator, Strategy, Visitor, Observer, State (highlighted in red), Memento, Template Method.]*

3/26

## Slide 4
**Singleton**

**Ensuring a single instance:**
The Singleton pattern ensures that there is only one instance of a class throughout the entire application.

**Global access:**
The Singleton pattern provides a global point of access to the single instance of a class.

**Lazy initialization:**
This means that the instance is not created until it is first requested, which can help to improve performance and memory usage.

**Thread safety:**
Ensuring that multiple threads cannot create multiple instances of the class simultaneously.

4/26

## Slide 5
**Singleton**

*[Image Description: A UML class diagram demonstrating the Singleton design pattern. There is a "Client" box with an arrow pointing to a "Singleton" class box. The "Singleton" class contains a private attribute `- instance: Singleton` and two methods: a private constructor `- Singleton()` and a public method `+ getInstance(): Singleton`. An arrow loops back from the top of the Singleton box to itself. A note attached to the `getInstance()` method contains the following pseudocode:
```text
if (instance == null) {
  // Note: if you're creating an app with
  // multithreading support, you should
  // place a thread lock here.
  instance = new Singleton()
}
return instance
```
]*

5/26

## Slide 6
**Singleton**

*   **Is Singleton considered to be an anti-pattern?**
    *   No, the Singleton design pattern is not considered an anti-pattern. However, it can be overused and misused.
    *   It should be used judiciously and with care, taking into account the specific requirements and constraints of the application.

6/26

## Slide 7
**Singleton Steps 1-3**

1.  Add a private static field to the class for storing the singleton instance.
2.  Declare a public static creation method for getting the singleton instance.
3.  Implement “lazy initialization” inside the static method. It should create a new object on its first call and put it into the static field. The method should always return that instance on all subsequent calls.

7/26

## Slide 8
**Singleton Steps 4-5**

4.  Make the constructor of the class private. The static method of the class will still be able to call the constructor, but not the other objects.
5.  Go over the client code and replace all direct calls to the singleton’s constructor with calls to its static creation method.

8/26

## Slide 9
**Singleton Pros**

*   You can be sure that a class has only a single instance
*   You gain a global access point to that instance
*   The singleton object is initialized only when it’s requested for the first time

9/26

## Slide 10
**Singleton Cons**

*   Violates the *Single Responsibility Principle*. The pattern solves two problems at the time
*   The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other
*   The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times
*   It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don’t write the tests. Or don’t use the Singleton pattern.

10/26

## Slide 11
**Prototype**

*   **Prototype** is a creational pattern that dynamically creates new objects based on existing objects: cloning technique

11/26

## Slide 12
**Prototype**

*[Image Description: A UML class diagram illustrating the Prototype pattern. A "Client" box has a dependency arrow pointing to an interface named «interface» Prototype. The Prototype interface has a public method `+ clone(): Prototype`. Below it, a class named `ConcretePrototype` implements the interface. It has a private attribute `- field1`, a constructor `+ ConcretePrototype(prototype)`, and overrides `+ clone(): Prototype`. Further down, a class named `SubclassPrototype` inherits from `ConcretePrototype`. It adds `- field2`, a constructor `+ SubclassPrototype(prototype)`, and overrides `+ clone(): Prototype`. 
There are grey note boxes attached to the classes containing pseudocode:
- Connected to Client: `copy = existing.clone()`
- Connected to ConcretePrototype's constructor: `this.field1 = prototype.field1`
- Connected to ConcretePrototype's clone(): `return new ConcretePrototype(this)`
- Connected to SubclassPrototype's constructor: `super(prototype) \n this.field2 = prototype.field2`
- Connected to SubclassPrototype's clone(): `return new SubclassPrototype(this)`]*

12/26

## Slide 13
**Prototype Applicability**

*   When your code shouldn’t depend on the concrete classes of objects that you need to copy
*   When you want to reduce the number of subclasses that only differ in the way they initialize their respective objects.

13/26

## Slide 14
**Prototype Steps 1-2**

1.  Create the prototype interface and declare the clone method in it. Or just add the method to all classes of an existing class hierarchy, if you have one.
2.  A prototype class must define the alternative constructor that accepts an object of that class as an argument. The constructor must copy the values of all fields defined in the class from the passed object into the newly created instance. If you’re changing a subclass, you must call the parent constructor to let the superclass handle the cloning of its private fields.

14/26

## Slide 15
**Prototype Steps 3-4**

3.  The cloning method usually consists of just one line: running a `new` operator with the prototypical version of the constructor. Note, that every class must explicitly override the cloning method and use its own class name along with the `new` operator. Otherwise, the cloning method may produce an object of a parent class.
4.  Optionally, create a centralized prototype registry to store a catalog of frequently used prototypes.

15/26

## Slide 16
**Prototype Pros and Cons**

*   **Pros**
    *   You can clone objects without coupling to their concrete classes
    *   You can get rid of repeated initialization code in favor of cloning pre-built prototypes
    *   You can produce complex objects more conveniently
    *   You get an alternative to inheritance when dealing with configuration presets for complex objects
*   **Cons**
    *   Cloning complex objects that have circular references might be very tricky

16/26

## Slide 17
**Builder**

**Readable and maintainable Code:**
When a class has a large number of fields, creating constructors with many parameters can make the code difficult to read and maintain

**Flexibility:**
With the Builder pattern, you can create objects step by step, setting only the fields that you need. This makes the code more adaptable to changing requirements

**Enforces Immutability:**
Once the object is created, its fields cannot be modified, ensuring that the object's state remains consistent throughout its lifetime.

17/26

## Slide 18
**Builder**

**Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

18/26

## Slide 19
**Builder**

*[Image Description: A UML class diagram depicting the Builder pattern. The "Client" is at the top. It has a dependency on a "Director" class and an interface `«interface» Builder`. 
The "Director" class has a private attribute `- builder: Builder` and methods: `+ Director(builder)`, `+ changeBuilder(builder)`, and `+ make(type)`. 
The `Builder` interface defines construction steps: `+ reset()`, `+ buildStepA()`, `+ buildStepB()`, `+ buildStepZ()`.
Two concrete classes implement the `Builder` interface: `ConcreteBuilder1` and `ConcreteBuilder2`. Both have their specific fields (e.g., `- result: Product1`) and implement the builder steps alongside a `+ getResult()` method. They output `Product1` and `Product2` respectively.
Note boxes contain code explanations:
- Attached to Client: `b = new ConcreteBuilder1(); d = new Director(b); d.make(); Product1 p = b.getResult();`
- Attached to Director's make(): `builder.reset(); if (type == "simple") { builder.buildStepA(); } else { builder.buildStepB(); builder.buildStepZ(); }`
- Attached to ConcreteBuilder2's reset(): `result = new Product2()`
- Attached to ConcreteBuilder2's buildStepB(): `result.setFeatureB()`
- Attached to ConcreteBuilder2's getResult(): `return this.result`]*

19/26

## Slide 20
**Builder Applicability**

*   To get rid of a “telescoping constructor”.
*   When you want your code to be able to create different representations of some product (for example, stone and wooden houses).
*   To construct Composite trees or other complex objects.

20/26

## Slide 21
**Builder Steps 1-3**

1.  Make sure that you can clearly define the common construction steps for building all available product representations. Otherwise, you won’t be able to proceed with implementing the pattern.
2.  Declare these steps in the base builder interface.
3.  Create a concrete builder class for each of the product representations and implement their construction steps.

21/26

## Slide 22
**Builder Steps 4-5**

4.  Think about creating a director class. It may encapsulate various ways to construct a product using the same builder object.
5.  The client code creates both the builder and the director objects. Before construction starts, the client must pass a builder object to the director. Usually, the client does this only once, via parameters of the director’s class constructor. The director uses the builder object in all further construction. There’s an alternative approach, where the builder is passed to a specific product construction method of the director.

22/26

## Slide 23
**Builder Step 6**

6.  The construction result can be obtained directly from the director only if all products follow the same interface. Otherwise, the client should fetch the result from the builder.

23/26

## Slide 24
**Builder Pros and Cons**

*   **Pros**
    *   You can construct objects step-by-step, defer construction steps or run steps recursively.
    *   You can reuse the same construction code when building various representations of products.
    *   *Single Responsibility Principle*. You can isolate complex construction code from the business logic of the product.
*   **Cons**
    *   The overall complexity of the code increases since the pattern requires creating multiple new classes.

24/26

## Slide 25
**Summary**

*   Singleton
*   Prototype
*   Builder

25/26

## Slide 26
**References**

*   https://refactoring.guru/design-patterns/singleton
*   https://refactoring.guru/design-patterns/prototype
*   https://refactoring.guru/design-patterns/builder
*   https://javarush.com/groups/posts/2365-patternih-proektirovanija-singleton
*   https://habr.com/ru/companies/otus/articles/552412/

26/26

---

# File 2: Lab 8 - Design Patterns Implementation

## Slide 1
**Innopolis University**
**Lab 8**
**Design Patterns: Singleton, State, Prototype, and Builder**

Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer 
Software Systems Analysis and Design
Spring Semester 2026

## Slide 2
**Agenda**

*   Recap
*   Singleton Design Pattern
*   State Design Pattern
*   Prototype Design Pattern
*   Builder Design Pattern
*   Lab Tasks

Software Systems Analysis and Design 2026
2

## Slide 3
**Lecture Recap**

1.  What are **design patterns**? Why do we need them?
2.  What are the **three types** of design patterns? How are they different?
3.  Give **three examples** for each design pattern type.
4.  Which design pattern prohibits the creation of multiple objects from a class?
5.  True or False: The **State** pattern encapsulates the behavior for each state in an object.
6.  When to use the **Prototype** pattern and what advantage it can provide?
7.  What are the differences between the **Builder** and the **Prototype** patterns?

Software Systems Analysis and Design 2026
3

## Slide 4
**Singleton Design Pattern**

*[Image Description: A C++ code block demonstrating the Singleton design pattern.]*
```cpp
1   class Singleton {
2   private:
3       static Singleton* instance;
4       Singleton() {} // Private ctor
5   
6   public:
7       static Singleton* getInstance() {
8           if (instance == nullptr) {
9               instance = new Singleton();
10          }
11          return instance;
12      }
13  };
```

*   Ensures a class has only one instance and provides a global point of access to it.
*   Logger classes, Configuration classes, Access to shared resources.

Software Systems Analysis and Design 2026
4

## Slide 5
**State Design Pattern**

*[Image Description: Two side-by-side C++ code blocks demonstrating the State design pattern.]*

**Left Block:**
```cpp
1   class State {
2   public:
3       virtual void review() = 0;
4       virtual ~State() = default;
5   };
6   
7   class Draft : public State {
8   public:
9       void review() override {
10          std::cout << "Draft: Reviewing changes\n";
11      }
12  };
13  
14  class Published : public State {
15  public:
16      void review() override {
17          std::cout << "Published: Review not allowed\n”;
18      }
19  };
```

**Right Block:**
```cpp
20  class Document {
21  private:
22      std::unique_ptr<State> state;
23  public:
24      Document(std::unique_ptr<State> initialState)
25      : state(std::move(initialState)) { }
26  
27      void setState(std::unique_ptr<State> newState) {
28          state = std::move(newState);
29      }
30  
31      void review() {
32          state->review();
33      }
34  };
```

Software Systems Analysis and Design 2026
5

## Slide 6
**Prototype Design Pattern (1 / 2)**

*[Image Description: Two side-by-side C++ code blocks demonstrating the Prototype design pattern interfaces and classes.]*

**Left Block:**
```cpp
1   class Car { // prototype 
2   public:
3       // Pure virtual function for cloning
4       virtual Car* clone() const = 0;
5       
6       // Displays car specs
7       virtual void specs() const = 0;
8       
9       // Virtual destructor
10      virtual ~Car() {}
11  };
12  
```

**Right Block:**
```cpp
13  class Sedan : public Car { // concrete prototype 
14  private:
15      std::string color;
16  public:
17      Sedan(const std::string& color) : color(color) {}
18  
19      Car* clone() const override {
20          return new Sedan(*this); // Return a copy of this object
21      }
22      
23      void specs() const override {
24          std::cout << "Sedan Car - Color: " << color << std::endl;
25      }
26  };
27  
```

Software Systems Analysis and Design 2026
6

## Slide 7
**Prototype Design Pattern (2 / 2)**

*[Image Description: A C++ code block showing the `main` function implementation for the Prototype pattern example.]*
```cpp
28  int main() {
29      Car* originalCar = new Sedan("Red");
30      Car* clonedCar = originalCar->clone();
31      
32      originalCar->specs(); // Outputs: Sedan Car - Color: Red
33      clonedCar->specs(); // Outputs: Sedan Car - Color: Red
34      
35      delete originalCar; // Clean up original
36      delete clonedCar; // Clean up clone
37      
38      return 0;
39  }
```

Software Systems Analysis and Design 2026
7

## Slide 8
**Builder Design Pattern (1 / 2)**

*[Image Description: Two side-by-side C++ code blocks defining the components of the Builder design pattern.]*

**Left Block:**
```cpp
1   class PC {
2       std::string m_cpu, m_ram, m_storage;
3   public:
4       void setCPU(std::string cpu) { m_cpu = cpu; }
5       void setRAM(std::string ram) { m_ram = ram; }
6       void setStorage(std::string storage) { m_storage = storage; }
7       void showSpecs() { ... }
8   };
9   
10  class PCBuilder {
11  public:
12      virtual ~PCBuilder() = default;
13      virtual void buildCPU() = 0;
14      virtual void buildRAM() = 0;
15      virtual void buildStorage() = 0;
16      virtual PC getResult() = 0;
17  };
```

**Right Block:**
```cpp
18  class GamingPCBuilder : public PCBuilder {
19      PC m_pc;
20  public:
21      GamingPCBuilder() { m_pc = PC(); }
22  
23      void buildCPU() override {
24          m_pc.setCPU("Intel i9-13900K");
25      }
26      
27      void buildRAM() override {
28          m_pc.setRAM("32GB DDR5");
29      }
30      
31      void buildStorage() override {
32          m_pc.setStorage("2TB NVMe SSD");
33      }
34      
35      PC getResult() override { return m_pc; }
36  };
```

Software Systems Analysis and Design 2026
8

## Slide 9
**Builder Design Pattern (2 / 2)**

*[Image Description: Two side-by-side C++ code blocks defining the Director class and the `main` function for the Builder design pattern.]*

**Left Block:**
```cpp
34  class Director {
35      PCBuilder* m_builder;
36  public:
37      void setBuilder(PCBuilder* builder) {
38          m_builder = builder;
39      }
40      
41      PC construct() {
42          m_builder->buildCPU();
43          m_builder->buildRAM();
44          m_builder->buildStorage();
45          return m_builder->getResult();
46      }
47  };
48  
```

**Right Block:**
```cpp
49  // Usage
50  int main() {
51      Director director;
52      GamingPCBuilder builder;
53      
54      director.setBuilder(&builder);
55      
56      PC pc = director.construct();
57      
58      pc.showSpecs();
59      
60      return 0;
61  }
```

Software Systems Analysis and Design 2026
9

## Slide 10
**Task 1: Smart Document Editor**

In this lab task, you will develop a "Smart Document Editor" system that showcases the application of three fundamental design patterns: **Singleton**, **State**, and **Prototype**.

The system manages documents with varying states and allows for the efficient creation of documents based on prototypes.

Additionally, a centralized logging mechanism will be incorporated using the Singleton pattern, providing insights into the system's operations, such as state transitions and document cloning.

Software Systems Analysis and Design 2026
10

## Slide 11
**Task 1: Smart Document Editor (cont.)**

**Part 1: Singleton - Logging Mechanism**

**Implement a Logger Class:**
*   Design a **Logger** class that follows the **Singleton** pattern to ensure only one instance exists throughout the application.
*   Include a method **log(const std::string& message)** for logging messages to the console or a file.

Software Systems Analysis and Design 2026
11

## Slide 12
**Task 1: Smart Document Editor (cont.)**

**Part 2: State - Document State Management**

**Abstract DocumentState Class:**
*   Create an abstract class **DocumentState** with a virtual method **handleInput(const std::string& input)** to represent how a document behaves when receiving input in different states.

**Concrete State Classes:**
*   Implement derived classes for specific states (**DraftState**, **ReviewState**, **FinalState**) that override **handleInput**.

**State Transition in Document:**
*   In the Document class, manage the current state using a **DocumentState\*** and implement a method **changeState(DocumentState\* newState)** for state transitions.

Software Systems Analysis and Design 2026
12

## Slide 13
**Task 1: Smart Document Editor (cont.)**

**Part 3: Prototype Design Pattern - Document Creation**

**Abstract DocumentPrototype Class:**
*   Design an abstract **DocumentPrototype** class with a **clone()** method for cloning document prototypes.

**Concrete Document Classes:**
*   Implement concrete classes (**ReportType**, **InvoiceType**) that inherit from **DocumentPrototype** and override the **clone()** method, incorporating default settings.

**Prototype Usage:**
*   Demonstrate the cloning of document prototypes to create new documents, incorporating the Singleton Logger to log cloning actions.

Software Systems Analysis and Design 2026
13

## Slide 14
**Task 1: Smart Document Editor (cont.)**

**Part 4: Main function**

Create a main function to showcase the entire system's functionality.
*   Demonstrate the creation of document prototypes and the cloning of these prototypes to produce new documents.
*   Demonstrate the transitions in document state (draft, reviewed, published).
*   Use the Singleton Logger to log significant events, such as document state changes and cloning operations.

Software Systems Analysis and Design 2026
14

## Slide 15
**Task 2: Document Builder**

Illustrate the use of the builder design pattern to create objects of a “Document” class.

*   Create a “**Document**” class with:
    *   Three private member string variables: *header*, *body*, and *footer*.
    *   Setters for the private members
    *   print() function to show the document content
*   Create an abstract “**DocumentBuilder**” class with pure virtual functions to build the document sections and a concrete “**ReportBuilder**” implementing the abstract class with some report-specific sections.
*   Create a “**Director**” class with a *make()* function that uses the “ReportBuilder” to incrementally construct the document.
*   Illustrate the system usage in the *main()* function.

Software Systems Analysis and Design 2026
15

## Slide 16
**The end.**

Ahmed Nouralla, Alaa Aldin Hajjar, Damir Nurtdinov, Marko Pezer
Software Systems Analysis and Design
Spring Semester 2026

---

# File 3: Lecture 9 - Design Patterns

## Slide 1
**System Software Analysis and Design**
**Lecture 9**
**Design Patterns**
**Introduction by Program Examples**

Spring Semester 2026
Innopolis University
Eugene Zouev

## Slide 2
**An Informal Definition**

*   A **design pattern** is an **architectural scheme** - a certain organization of classes, objects & methods – that provides applications with a standardized solution to a common problem.
*   Each pattern describes a problem that occurs over and over again in our environment, and then describes the core of the solution to this problem in such a way that you can use this solution a million times over, without ever doing it the same way twice.“ - Gamma et al.
*   Since 1994, various books have catalogued important patterns. Best known is **Design Patterns** by **Erich Gamma**, **Richard Helm**, **Ralph Johnson**, **John Vlissides**, Addison-Wesley 1994.

“Gang of Four” ☺
2/30

## Slide 3
**References**

*[Image Description: A collage of four book covers about design patterns:
1. "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (also shown as a Russian edition below it: "Паттерны проектирования"). A red explosion graphic is drawn above this book.
2. "Design Patterns Explained: A New Perspective on Object-Oriented Design" by Alan Shalloway, James R. Trott.
3. "Design Patterns in Java" by Steven John Metsker, William C. Wake.
4. "Design Patterns in C#" by Steven John Metsker.
At the bottom right, a tilted red box with text says: "A lot of explanations in Internet".]*

3/30

## Slide 4
**Important remarks**

*   All design patterns exploit **OOP paradigm**
*   While studying design patterns we will be using the following languages:
    **Java** **C#** **C++**
*   Lectures: Design patterns by examples
    We will have a lot of program examples ☺
*   Tutorials: Design patterns in UML notation

4/30

## Slide 5
**DP: Motivation & Rationale**

"Designing object-oriented software is hard and designing reusable object-oriented software is even harder.“
Erich Gamma

*   Experienced object-oriented designers make good designs while novices struggle.
*   Object-oriented systems have recurring patterns of classes and objects.
*   Patterns solve specific design problems and make OO designs more flexible, elegant, and ultimately reusable.

*[Image Description: A red right-pointing arrow points to the following text block:]*
**Conclusion:**
DP is (almost completely) about OOP

5/30

## Slide 6
**Design Patterns: Taxonomy**

*   **Creational:** Deal with the best way to create instances of objects.
*   **Structural:** Describe how classes and objects can be combined to form larger structures.
*   **Behavioral:** Are concerned with the assignment of responsibilities between objects, or, encapsulating behavior in an object and delegating requests to it.

*[Image Description: A table diagram categorizing design patterns. The "Creational" box includes: Abstract Factory, Singleton (highlighted in red), Factory Method, Builder, Prototype (highlighted in red). The "Structural" box includes: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. The "Behavioral" box includes: Chain of Responsibility, Command (undo/redo), Interpreter, Observer, Iterator, State (highlighted in red), Mediator, Memento, Strategy, Template Method, Visitor. 
To the right of the table, a yellow box contains the text: "There is no strong theory behind design patterns; rather, patterns summarize the big & real practical experience of using OOP for various applications."]*

6/30

## Slide 7
**Singleton**

## Slide 8
**The Single Instance?**

**How to prohibit any creation, except the very first one?**
Or, simply speaking, how to provide
creation of exactly one instance of a class?

**Why have such an exotic class?**
- Cache file
- File with virtual memory pages in OS or VM
- Some kinds of dialogue windows in UI
- Device drivers
- etc.

**Why not to use just a global variable?** (or a static variable)
- Uncontrolled access
- Cannot control creation time

8/30

## Slide 9
**Some attempts**

(Yes, this is a very simple task but let’s attack it stadially).

- Suppose we have a class:
```java
class myClass { ... }
```
- How to create an instance?
```java
new myClass()
```
- Can we create many instances? Of course!
- How to prevent creation?
```java
class myClass
{
    private myClass() { }
}
```
- Does this solution really prevent creation? - No:

```java
class myClass
{
    private myClass() { }
    public static myClass getInstance() {
        return new myClass();
    }
}
```
*[Image Description: A thin blue box placed next to the last code block reads: "What should we add to this code to make the uniqueness of the instance created?"]*

9/30

## Slide 10
**The Solution: Singleton Pattern**

**Java**

*[Image Description: A Java code block showing the Singleton pattern. Surrounding the code are three text bubbles pointing to specific parts of the code.]*

```java
public class Singleton
{
    private static Singleton unique;

    private Singleton() { }

    public static Singleton getInstance()
    {
        if ( unique == null )
            unique = new Singleton();
        return unique;
    }
}
```

*[Bubble 1 pointing to `private static Singleton unique;` and the start of the `getInstance()` method:]*
This static member keeps the reference to the single instance of the class. It is initialized by `null` at the very beginning of the program, and gets the reference to the instance after the very first call to `getInstance`.

*[Bubble 2 pointing to `private Singleton() { }`:]*
**Private constructor:** only class itself can create instances of the class

*[Bubble 3 pointing to the `if (unique == null)` block inside `getInstance()`:]*
The first call to the method creates the unique instance of the class. The following calls just return the same instance

*[Bottom Box:]*
There is no other way to get access to `unique` except via call to `getInstance`.

10/30

## Slide 11
**The Singleton Pattern: Exercises**

1.  Implement the pattern in
    - C# (very simple)
    - C++ (just simple)
2.  Try to explain yourself why the solution is incomplete.
    - Hint: consider a multithreaded program with Singleton.
3.  Write a multithreaded program (in any language) illustrating the incorrect work of the Singleton pattern.
4.  Suggest a solution improving the problem and making Singleton an industrial-strength pattern.

12/30 *(Note: Slide number as per original document)*

## Slide 12
**State**
Singleton

## Slide 13
**Pattern State**

**The State pattern:**
*   Allows an object to alter its behavior when its internal state changes.
    The object will appear to change its class.

**Conceptual basis:**
*   Finite state machines (automata).
    A (virtual) system that can have a **state** at each moment.
    When an action is performed, the machine **changes its state**.

13/30

## Slide 14
**Pattern State Example: Lexical Analyzer**

*   **Lexical analyzer:** the first part of the compiler toolchain.
*   What does typical lexical analyzer do:
    it decomposes the source program text into **tokens**.
*   **Token:** a minimal language unit that has a concrete meaning.
*   Token examples: identifiers, literals, delimiters, operator signs etc.

*[Image Description: A schematic workflow diagram. On the left is a green box labeled "Source program text". A red arrow points from it into a dashed box labeled "Compiler". Inside the "Compiler" box are green blocks labeled "Tokens" followed by "...". A red arrow points out of the "Compiler" box into a green box on the right labeled "Compiler output".]*

14/30

## Slide 15
**Pattern State Example: Lexical Analyzer**

Example: Scanning identifiers and integers
*   **Identifier:** a sequence of letters & digits
*   **Integer literal:** a sequence of digits

**States and actions that change the state.**

States:
- Initial state
- A letter is read
- A digit is read
- Another character is read

Actions:
- initializing buffer
- it’s a part of identifier: adding letter to buffer
- it’s a part of id. or integer adding it to buffer
- identifier or integer has taken

15/30

## Slide 16
**Pattern State Example: Lexical Analyzer**

**Finite State Machine**
Автомат с конечным числом состояний

*[Image Description: A state machine diagram with circles representing states and arrows representing transitions. 
- State "S" (Initial state: prepare the buffer for an identifier or an integer). 
- An arrow labeled "Letter" points from "S" to state "1". (Add the letter to the buffer). 
- From state "1", an arrow labeled "Other" points to state "3" (An identifier was detected; add it to the symbol table). 
- From state "1", a looping arrow points back to state "1" labeled "Digit or letter". 
- An arrow labeled "Digit" points from "S" to state "4". (Add the digit to the buffer).
- From state "4", an arrow labeled "Other" points to state "5" (An integer constant was detected; convert it to the binary form).
- From state "4", a looping arrow points back to state "4" labeled "Digit".]*

16/30

## Slide 17
**Pattern State Example: Water**

What is **water**? Various **states** and some actions that **change the state**.

Three states:
- Solid (ice)
- Liquid
- Gas

Three actions:
- Heating
- Freezing
- Cooling

The task:
**To design a device that controls actions on water.**

*[Image Description: A state diagram showing four circles representing states of water: "Liquid", "Solid", "Gas", and "High-temp. Gas". Blue arrows indicate transitions between them. 
- "Solid" transitions to "Liquid" via an arrow labeled "Heating".
- "Liquid" transitions to "Solid" via an arrow labeled "Freezing".
- "Liquid" transitions to "Gas" via an arrow labeled "Heating".
- "Gas" transitions to "Liquid" via an arrow labeled "Cooling".
- "Gas" transitions to "High-temp. Gas" via an arrow labeled "Heating".]*

Water changes its state depending on its current state and on the action being performed
17/30

## Slide 18
**Pattern State Example: Water**

*[Image Description: Two C# code blocks. A blue arrow points from a yellow note reading "Do you know what's this?" to the `{ get; set; }` property in the second code block.]*

```csharp
// Water states
enum WaterState
{
    SOLID,
    LIQUID,
    GAS
}
```

```csharp
class Water
{
    // Current state of water
    public WaterState State { get; set; }

    // Initialization
    public Water(WaterState ws) { State = ws; }

    // Actions
    public void Heating() { ... }
    public void Freezing() { ... }
    public void Cooling() { ... }
}
```

**Straightforward implementation**

18/30

## Slide 19
**Pattern State Example: Water**

**Straightforward implementation**

*[Image Description: Two C# code blocks showing the implementation of the `Heating()` and `Freezing()` methods using standard if/else statements. A red box with text points to the code block: "Do you like the implementation?"]*

```csharp
public void Heating()
{
    if ( State == WaterState.SOLID ) 
    {
        // Ice to liquid
        State = WaterState.LIQUID;
    }
    else if ( State == WaterState.LIQUID )
    {
        // Liquid to gas
        State = WaterState.GAS;
    }
    else if ( State == WaterState.GAS )
    {
        // Increasing temperature
        ...
    }
}
```

```csharp
public void Freezing()
{
    if ( State == WaterState.LIQUID )
    {
        // Liquid to ice
        State = WaterState.SOLID;
    }
    else if ( State == WaterState.GAS )
    {
        // Gas to liquid
        State = WaterState.LIQUID;
    }
    else if ( State == WaterState.GAS )
    {
        ...
    }
}
```

19/30

## Slide 20
**Pattern State Example: Water**

*[Image Description: The exact same C# code blocks from the previous slide are shown on the left side of the screen.]*

```csharp
public void Heating()
{
    if ( State == WaterState.SOLID ) 
    {
        // Ice to liquid
        State = WaterState.LIQUID;
    }
    else if ( State == WaterState.LIQUID )
    {
        // Liquid to gas
        State = WaterState.GAS;
    }
    else if ( State == WaterState.GAS )
    {
        // Increasing temperature
        ...
    }
}
```

```csharp
public void Freezing()
{
    if ( State == WaterState.LIQUID )
    {
        // Liquid to ice
        State = WaterState.SOLID;
    }
    else if ( State == WaterState.GAS )
    {
        // Gas to liquid
        State = WaterState.LIQUID;
    }
    else if ( State == WaterState.GAS )
    {
        ...
    }
}
```

**Problems with straightforward implementation:**
*   States and actions are separated. For adding a new state (“High-temp. gas”) all actions should be updated accordingly.
*   The new state should be added to each action’s algorithm: `if` statement should be updated.

**Solution:**
*   **Treat a state as an object with functionality.**

20/30

## Slide 21
**Pattern State Example: Water**

**Solution:**
*   **Treat a state as an object** with functionality.

**Step 1:**
*   Declare the common interface for all classes representing states

*[Image Description: A red arrow points from the old `enum WaterState` code block to a new `interface WaterState` code block. Next to it are declarations of three new classes implementing the interface, labeled "See Step 3".]*

```csharp
// Water states
enum WaterState
{
    SOLID,
    LIQUID,
    GAS
}
```
**=>**
```csharp
// Water states
interface WaterState
{
    void Heating(Water water);
    void Freezing(Water water);
    void Cooling(Water water);
}
```

```csharp
class SolidWater: WaterState
class LiquidWater: WaterState
class GasWater: WaterState
```

21/30

## Slide 22
**Pattern State Example: Water**

**Step 2:**
*   Redesign `Water`

*[Image Description: A C# code block showing the updated `Water` class. A speech bubble points to the methods calling `State.Action(this);`]*

```csharp
class Water
{
    // Current state of water
    public WaterState State { get; set; }

    // Initialization
    public Water(WaterState ws) { State = ws; }

    // Actions
    public void Heating() { State.Heating(this); }
    public void Freezing() { State.Freezing(this); }
    public void Cooling() { State.Cooling(this); }
}
```

*[Speech bubble text:]*
Each water’s action redirects the control to the corresponding state object.
**Note:** there is NO `if` statements in the implementation.

22/30

## Slide 23
**Pattern State Example: Water**

**Step 3:**
*   Declare classes representing states

*[Image Description: A diagram showing the `interface WaterState` pointing to a layered sequence of concrete class implementations: `class SolidWater`, `class GasWater`, and specifically detailing `class LiquidWater`.]*

```csharp
// Water states
interface WaterState
{
    void Heating(Water water);
    void Freezing(Water water);
    void Cooling(Water water);
}
```

```csharp
class LiquidWater: WaterState
{
    void Heating(Water water) {
        // liquid to gas
        water.State = new GasWater();
    }
    void Freezing(Water water) {
        // liquid to ice
        water.State = new SolidWater();
    }
    void Cooling(Water water) {
        // cooling liquid – no change
    }
}
```

```csharp
class GasWater: WaterState
{
}
```

```csharp
class SolidWater: WaterState
{
}
```

23/30

## Slide 24
**Pattern State Example: Water**

**Step 4:**
*   What if we need to add a new state?
*   E.g., “high-temp. gas”?

*[Image Description: A list of classes inheriting from WaterState is shown on the left. The new `class HTGasWater: WaterState` is highlighted in red. A speech bubble points to the detailed code block for the new class.]*

```csharp
class SolidWater: WaterState
class LiquidWater: WaterState
class GasWater: WaterState
class HTGasWater: WaterState
```

*[Speech bubble text:]*
We just add new class to the hierarchy without changing existing classes

```csharp
class HTGasWater: WaterState
{
    void Heating(Water water) {
        // heating – no change
    }
    void Freezing(Water water) {
        // high-temp.gas to gas
        water.State = new GasWater();
    }
    void Cooling(Water water) {
        // high-temp.gas to gas
        water.State = new GasWater();
    }
}
```

24/30

## Slide 25
**Pattern State: Advantages**

*   Pattern State encapsulates the behavior for each state in the object.
*   How to add a new state:
    Just define the new class without changing existing classes.
*   How to update the behavior of a state:
    Just change the corresponding class.

25/30

## Slide 26
**Prototype**
Singleton
State

## Slide 27
**Pattern Prototype**

**The Prototype pattern:**
*   Prototype dynamically creates new objects based on existing objects: cloning technique.

**When to use:**
*   If the type of object being created should be determined dynamically.
*   If simple technique is enough.
    (Will see **Abstract Factory** for similar purposes later).
*   If cloning is more preferable than creating by **new** and launching a constructor (for simple objects).

27/30

## Slide 28
**Pattern Prototype**

**Example: geometric figures** ☺
Suppose we have to work with various geometric figures dynamically creating them.
Instead of creating a new figure “from scratch”, we prefer to create a copy of an existing figure with the same attributes: **to create a clone**.

*[Image Description: A C# code block demonstrating an interface. Speech bubbles point to parts of the code to explain them.]*

```csharp
interface iFigure
{
    iFigure Clone();
    void Display();
}
```

*[Speech bubble 1 pointing to the whole interface:]*
All figures should implement this interface

*[Speech bubble 2 pointing to `iFigure Clone();`:]*
Common interface for cloning: it hides the concrete algorithm of cloning of a particular figure

28/30

## Slide 29
**Pattern Prototype**

*[Image Description: Two C# code blocks showing the `Rectangle` and `Circle` classes implementing the `iFigure` interface. Red arrows point from a speech bubble to the `Clone()` methods in both classes.]*

```csharp
class Rectangle: iFigure
{
    int width, height;
    public Rectangle(int w, int h) 
    {
        width = w;
        height = h;
    }
    public IFigure Clone()
    {
        return new Rectangle(this.width,this.height);
    }
    public void Display()
    {
        ...
    }
}
```

```csharp
class Circle : iFigure
{
    int radius;
    public Circle(int r) { radius = r; }

    public IFigure Clone() {
        return new Circle(this.radius);
    }
    public void Display() {
        ...
    }
}
```

*[Speech bubble pointing to `Clone()` methods in both classes:]*
**Clone** method encapsulates the real cloning algorithm: it might be creation by **new**, or using system-based tools like `MemberwiseClone()` from .NET

29/30

## Slide 30
**Pattern Prototype**

**Example of use:**

*[Image Description: A C# code block showing the main Program. Speech bubbles point to specific clone calls.]*

```csharp
class Program
{
    static void Main(string[] args)
    {
        iFigure figure;
        iFigure clone;
        ...
        figure = new Rectangle(30,40);
        clone = figure.Clone();
        ...
        figure = new Circle(30);
        clone = figure.Clone();
    }
}
```

*[Speech bubble pointing to `clone = figure.Clone();` (Rectangle)]*
`Clone` method call creates the copy of `Rectangle`

*[Speech bubble pointing to `clone = figure.Clone();` (Circle)]*
The same call creates the copy of `Circle`

30/30