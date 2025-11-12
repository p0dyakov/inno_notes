# File 1: Lecture Slides

## Slide 1
Introduction to Programming
Lecture 11
Introduction to Java
Final methods & classes; interfaces
Eugene Zouev
Fall Semester 2025
Innopolis University

## Slide 2
What We Have Learnt
• Classes and class instances
• Value types and reference types
•
Encapsulation, overloading
Inheritance: single & multiple
• Static & dynamic types
• Method overriding
•
Polymorphism
• Casts & type checks
•
•
Abstract classes & methods
Packages
2/36

## Slide 3
Today:
Interface & implementation (again)
Final methods & classes
Interfaces

## Slide 4
Interface & Implementation 1
What should be inherited: interface and/or implementation?
class Airplane {
public void fly()
{
// Standard flying algorithm
}
}
class Airbusa extends Airplane {
}
...
// here fly() is not overriden;
// standard algorithm is used
class Airbusß extends Airplane {
...
// fly() is not overriden;
// standard algorithm is used
=
Airplane a
new AirbusA();
a.fly(); // Airplane's fly
...
=
Airplane b
new AirbusB();
b.fly(); // Airplane's fly
Here, the implementation
of fly() is inherited
- Is it always good?
}
4/36

## Slide 5
Interface & Implementation 2
class Airplane {
}
public void fly()
pub
What should be inherited:
interface and/or implementation?
{
// Standard flying algorithm
}
Airplane c
=
class Airbusa extends Airplane
{
...
}
class AirbusB extends Airplane
}
{
...
class Boeing extends Airplane {
...
// Standard fly() algorithm is
// inherited!
//
-
But here should be another
// algorithm!
new Boeing();
c.fly(); // Airplane's fly
What happens?
Here, Boeing has to fly by
Airbus' algorithm!?..
Is it correct?
Apparently not!
Will the compiler report a bug?
No!! - the code is formally
correct
}
5/36

## Slide 6
Interface & Implementation 3
abstract class Airplane {
public abstract void fly();
protected void defaultFly()
{
// Standard flying algorithm
}
Solution:
separate interface and
implementation!
Airplane a
=
new AirbusA();
a.fly(); // Airplane's fly
}
class Airbusa extends Airplane {
void fly() { defaultFly();
}
class Airbusß extends Airplane {
}
void fly() { defaultFly(); };
class Boeing extends Airplane {
public void fly() {
// Boeing's own
// flying algorithm
}
}
...
Airplane b
=
new AirbusB();
b.fly(); // Airplane's fly
...
Airplane c = new Boeing();
c.fly(); // Boeing's fly
Here, Boeing has its own
flying algorithm.
6/36

## Slide 7
Interface & Implementation 4
abstract class Airplane {
public abstract void fly();
protected void defaultFly()
The same solution in C#
{
// Standard flying algorithm
}
}
class AirbusA : Airplane {
}
public override void fly() { defaultFly(); }
class AirbusB : Airplane {
}
public override void fly() { defaultFly(); };
class Boeing : Airplane {
}
public override void fly() { /* Boeing's flying alg. */ }
7/36

## Slide 8
Interface & Implementation 5
Conclusions
When you design a base class, and...
-
If you need to provide only interface - make the method
abstract (or pure virtual in C++); hide or restrict its
implementation (e.g., as a separate method).
-
If you want to provide both interface and implementation
for derived classes - make the method virtual (explicitly as
in C++/C#, or implicitly as in Java).
-
If you wouldn't like to allow derived classes to modify the
behavior of the method - make this method non-virtual
(impossible in Java: all methods are virtual).
8/36

## Slide 9
Final Methods
▫ Method overriding is one of Java's most powerful features.
▫ However, dynamic calls are a bit slower than "usual" calls when the method is selected statically.
▫ Therefore, sometimes it might be reasonable to prevent late binding.
▫ For that, the final specifier is used. Methods declared as final cannot be overridden.
Late binding:
The concrete method to be
called depends on the
dynamic type of the object
Early binding:
The concrete
method to be called
is selected using
the static type of
the object
9/36

## Slide 10
Final Methods
class Base {
public final void method() {
System.out.println("Base's meth");
}
class Base {
}
public void method() {
System.out.println("Base's meth");
}
class Derived extends Base {
public void method() { // ERROR! Can't override
}
System.out.println("Derived's meth"); }
}
class Derived extends Base {
public void method() {
}
System.out.println("Derived's meth"); }
}
}
=
Base b
b.method();
b
b.method();
=
new Base();
// Base's meth
new Derived();
// Derived's meth
10/36

## Slide 11
Final Methods
Methods declared as final can sometimes provide a
performance enhancement.
Why:
• The compiler is free to inline calls to final methods
because it "knows" they will not be overridden by a
subclass.
When a small final method is called, the Java compiler
can copy the bytecode of the method directly to the
compiled code of the calling method, thus eliminating
the costly overhead associated with a method call.
Early binding
11/36

## Slide 12
Final Methods
class Base {
public final void method() {
System.out.println("Base's method");
}
}
class Derived extends Base {
// No overriden method
...
}
=
new Base();
// Base's method
Base b
b.method();
b
=
new Derived();
b.method();
Early binding:
Both calls refer to the same method.
Therefore, the compiler knows the
method statically, and can:
-
// Base's method again!
Either generate more efficient
code for the call
Or replace the call for the body of
the method method “in place":
inlining.
12/36

## Slide 13
Final Classes
Sometimes it's reasonable to prevent
a class from being inherited.
final class Base
{
}
...
class Derived extends Base
{
}
...
ERROR: Can't subclass Base
•
Declaring a class as final
implicitly declares all of its
methods as finals, too.
•
It's illegal to declare a class as
both abstract and final
Why? - try to explain.
Since an abstract class is incomplete by
itself and relies upon its subclasses to
provide complete implementations.
13/36

## Slide 14
Interfaces
(as a special language construct,
but not as a concept)

## Slide 15
Two Views at the World
• The world consists of (abstract and real) objects
• Objects have state (characteristics)
• Objects have relationships with other objects
• All entities in the world are doing something (are "active").
• Therefore, the basic characteristics of an entity is its behavior.
• Various kinds of behavior are in some relationships with each other.
Class-based approach
OOP!
Interface-based approach
15/36

## Slide 16
Interfaces 1
As a natural continuation
of the previous considerations:
Interface as a special language construct
interface Features
{
int numOfLegs();
boolean canFly();
boolean canSwim();
...
}
Interfaces is a good
alternative to
multiple inheritance
Each class implementing this interface
must contain methods with specified
signature and corresponding
implementation.
C++, Eiffel: no interfaces (abstract
classes or "deferred" classes)
C#, Java: interfaces
An interface is a contract between a class and the outside world.
When a class implements an interface, it promises to provide the
behavior published by that interface.
16/36

## Slide 17
Interfaces 2
interface Features
{
int numOfLegs();
boolean canFly();
boolean canSwim();
...
}
• No bodies: classes should provide implementations
• No access specifiers: (obviously) public by default.
• Interface is not a class: no new operator, no interface instances.
• Interfaces cannot have data - only function signatures.
• Interface is a contract of an implementing class
• Interface can be treated as (an abstract) type.
class Lion implements Features
{
... }
...
Features f1 = new Features();
// Error: cannot create
// instances of interfaces
Features f2 = new Lion();
// Correct
17/36

## Slide 18
Interfaces 3
interface Features
{
int numOfLegs();
bool canFly();
bool canSwim();
}
If a class is declared as
implementing an interface...
class Lion implements Features
{
int numOfLegs() { return 4; }
boolean canFly() { return false; }
boolean canSwim() { return true; }
}
Features f = new Lion(); // OK
...
if ( f.canFly() ) ...
...This means that the class is
responsible to (it must) provide
implementations to all features
declared in the interface it is
implementing!
...And after that we can treat a lion
as a set of its features
18/36

## Slide 19
Interfaces 4
A class can implement several interfaces:
a (kind of) easier and clearer replacement
for multiple inheritance
class Person implements iBodyParams, iskills, iRelations, ...
{
...
}
Person john = new Person();
...
iskills johnsSkills = john;
...
// Consider "john" as a set of his skills...
...
19/36

## Slide 20
Interfaces Can Inherit
An interface can inherit from other interface(s):
interface speedFeatures {
float maxSpeed();
float maxAcceleration();
}
interface engineFeatures extends speedFeatures {
float numofcyls();
float enginePower();
}
class Car implements engineFeatures
{
...
}
Must implement interfaces from both
speedFeatures & engineFeatures
20/36

## Slide 21
Classes Inherit Interfaces
Interfaces are inherited (as classes):
interface HasLegs {
int noLegs();
}
class Mammal implements HasLegs
{
int noLegs() { return 4; }
}
class Lion extends Mammal
{
...
}
Lion inherits interface's
implementation from its base class
...
Lion a = new Lion();
int legs = a.noLegs();
21/36

## Slide 22
Interfaces With Inheritance
Interfaces can be used together with inheritance:
interface colorFeatures {
Color color();
Border border();
}
abstract class Shape {
abstract void Draw();
...
}
class Rectangle extends Shape
{
...
}
class coloredRectangle extends Rectangle implements colorFeatures
{
// Inherits from Rectangle
// and implements features from colorFeatures
}
In some sense, interfaces
are orthogonal to
inheritance mechanism...
22/36

## Slide 23
Interfaces & Type Checks
Type check operators are applicable
to interfaces as well:
interface Printable { void print(); }
interface Movable { void move(); }
interface Serializable { void serialize(); }
abstract class Shape { ... }
class Rectangle extends Shape
implements Printable, Movable, Serializable
{ ... }
Shape a = new Rectangle();
if (a instanceof Printable )
((Printable)a).print(); // valid if a is really Pintable
if (a instanceof Movable )
((Movable)a).move(); // valid if a is really Movable
Interfaces can be empty!
Sometimes that's useful:
they act like "tags".
23/36

## Slide 24
Nested Interfaces
class Someclass {
public interface Nested
{
boolean isNotNegative(int x);
}
}
class MyClass implements Someclass.Nested
{
boolean isNotNegative(int x)
{
return x<0 ? false : true;
}
}
class Demo
{
public static void Main() {
SomeClass.Nested obj = new MyClass();
if (obj.isNotNegative(10))
System.out.println("10 is not negative");
}
}
interface SharedConstants {
int No = 0;
int Yes = 1;
int MayBe = 2;
int Later = 3;
int Soon = 4;
int Never = 5;
}
24/36

## Slide 25
Interfaces as Facets
Interfaces can be treated as various views
at an object (clients' points of views).
Client
View
View
Client
View "Facet"
Pictures are taken from a lecture of Prof J.Gutknecht, ETH Zürich
25/36

## Slide 26
Interfaces vs Abstract Classes
Similarities:
- Both represent an abstraction.
- Cannot create instances of both.
Differences:
- Interface is a "pure" abstraction: i.e., only abstraction of behavior (can specify only functionality, but not the object state - the latter is already not so!)
- Abstract class can contain a) abstract specification of behavior, b) non-abstract functionality, and c) object state.
The favorite question on
many job interviews!
26/36

## Slide 27
Interfaces: Ad-hoc Polymorphism
interface Frog {
boolean isGreen();
boolean canJump();
boolean canSwim();
boolean likesToQuack();
}
class Somebody // NO interfaces
{
boolean isGreen() { return true; }
boolean canJump() { return true; }
boolean canSwim() { return true; }
boolean likesToQuack() { return true; }
}
Somebody likeAFrog = new Somebody();
Frog frog = likeAFrog; // ????
If the last conversion is allowed
in a language, then this is so
called ad-hoc polymorphism.
Or... "duck typing":
«Если нечто ходит как утка, плавает
как утка и крякает как утка, то это,
скорее всего, утка и есть».
<<If somebody walks like
a duck, swims like a duck
and cries like a duck
this is obviously the duck».
-
27/36

## Slide 28
Enumerations
An example:
Suppose we are going to control the traffic lights
with three states: red, yellow and green.
How do we do that?
From the "C" part
of the course
Conventional solution
const int green = 0;
const int yellow = 1;
const int red = 2;
Why these numbers?
Why not 4, 12, 78?
...
This is enumeration type!
Advanced
solution
enum Lights {
green,
yellow,
red
};
...
Lights tl;
...
tl = 777; // ERROR
These are enumerators
In general, we are not interested
in actual values behind green,
yellow & red!
int tl;
...
tl = 777;
This variable serves as a
model of a traffic lights
What happens if we write this?
However...
"Behind the scenes", the enumerator
values are just integers, starting from 0.
28/36

## Slide 29
Enumerations: More Examples
A model of a compass
enum Compass
{
NORTH,
SOUTH,
EAST,
WEST
}
Week days
public enum Day
{
SUNDAY,
MONDAY,
TUESDAY,
WEDNESDAY,
THURSDAY,
FRIDAY,
SATURDAY
}
Enumeration members -
enumerators - are actually
constants.
Historically (from C or even
from the Assembler era)
constant names were written
with UPPERCASE letters.
This is NOT a requirement -
just a tradition...
29/36

## Slide 30
Enumerations: More Examples
public enum Day
{
SUNDAY,
MONDAY,
TUESDAY,
WEDNESDAY,
THURSDAY,
FRIDAY,
SATURDAY
}
public void tell_it_like_it_is(Day day) //
{
switch (day) {
case MONDAY:
System.out.println("Mondays are bad.");
break;
case FRIDAY:
System.out.println("Fridays are better.");
break;
// ...
default:
System.out.println("Midweek days are so-so.");
break;
}
}
30/36

## Slide 31
Enumerations
Java extensions
Java enum types are much more powerful than
their counterparts in other languages.
• Enum members can be initialized.
• The enum class body can include methods,
constructors, and other fields.
• The compiler automatically adds some special
methods when it creates an enum.
• Enum members can have... bodies (!)
Actually, enums are classes in Java!
31/36

## Slide 32
Enumerations
Java extensions
Enum members can be initialized
The value associated
with the enumerator
enum Coin
{
PENNY(1), NICKEL(5), DIME (10), QUARTER(25);
private final int value;
Coin(int value) { this.value = value; }
}
Values (in cents)
of American coins
!
!!
Private by
default
...
Coin c = DIME;
...
The enum constructor!
The value of 10 is
automatically
associated with c
32/36

## Slide 33
Enumerations
Java extensions
Enumerations can have methods
enum Coin
{
PENNY(1), NICKEL(5), DIME(10), QUARTER(25);
Coin(int value) { this.value = value; }
private final int value;
public int value() { return value; }
}
...
Coin c = DIME;
int v = c.value();
...
Returns 10
33/36

## Slide 34
Enumerations
Enum predefined methods
Java extensions
From the Java
Reference Manual
public static E[] values();
Returns an array containing the constants of this
enum type, in the order they're declared. This
method may be used to iterate over the constants:
public class Test {
enum Season { WINTER, SPRING, SUMMER, FALL }
public static void main(String[] args) {
for (Season s : Season.values())
System.out.println(s);
}
}
Output
WINTER
SPRING
SUMMER
FALL
34/36

## Slide 35
Enumerations
Java extensions
Enum members can have bodies
enum Operation {
// Each constant supports an arithmetic operation
abstract double eval(double x, double y);
PLUS { double eval(double x, double y) { return x + y; } },
MINUS { double eval(double x, double y) { return x - y; } },
TIMES { double eval(double x, double y) { return x * y; } },
DIVIDE { double eval(double x, double y) { return x / y; } };
public static void main(String args[]) {
double x = Double.parseDouble(args);
double y = Double.parseDouble(args);
for (Operation op : Operation.values())
System.out.println(x + " " + op + " " + y + " = " + op.eval(x, y));
}
}
Double: class wrapper of
the double type.
parseDouble: method
converting String to double
Output
2.0 PLUS 4.0 = 6.0
2.0 MINUS 4.0 = -2.0
2.0 TIMES 4.0 = 8.0
2.0 DIVIDE 4.0 = 0.5
35/36

## Slide 36
What We Have Learnt Today
• What's inherited:
class interface and/or its implementation?
• Final methods: to forbid overriding
• Final classes: to forbid inheritance
• Interface: another way for organizing programs
• Enumeration types: more powerful than before
36/36

# File 2: Lab Slides

## Slide 1
Introduction to Programming
Lab 10
Alaa Aldin Hajjar, Amer Al Badr, Damir Nurtdinov,
Ikechi Kalu Ndukwe, Marko Pezer

## Slide 2
Agenda
• Enumerations in Java
• UML Class Diagram
• Java Collections Framework
2

## Slide 3
Enums in Java
The enum is a special "class" that represents a group of constants (unchangeable
variables, like final variables).
1 enum Level {
2 LOW,
3 MEDIUM,
4 HIGH
5 }
1 public class Main {
2 public static void main(String[] args) {
3 Level myVar = Level.MEDIUM;
4
5 switch(myVar) {
6 case LOW:
7 System.out.println("Low level");
8 break;
9 case MEDIUM:
10 System.out.println("Medium level");
11 break;
12 case HIGH:
13 System.out.println("High level");
14 break;
15 }
16 }
17 }
3

## Slide 4
Enums in Java: Fields & Methods
1 public enum Level {
2 HIGH (3), //calls constructor with value 3
3 MEDIUM(2), //calls constructor with value 2
4 LOW (1) //calls constructor with value 1
5 ; // semicolon needed when fields / methods follow
6
7 private final int levelCode;
8
9 Level(int levelCode) {
10 this.levelCode = levelCode;
11 }
12
13 public int getLevelCode() {
14 return this.levelCode;
15 }
16 }
1 public enum Level {
2 HIGH {
3 @Override
4 public String asLowerCase() {
5 return HIGH.toString().toLowerCase();
6 }
7 },
8 MEDIUM {
9 @Override
10 public String asLowerCase() {
11 return MEDIUM.toString().toLowerCase();
12 }
13 },
14 LOW {
15 @Override
16 public String asLowerCase() {
17 return LOW.toString().toLowerCase();
18 }
19 };
20 public abstract String asLowerCase();
21 }
22
4

## Slide 5
Enums in Java
enum Color {
RED,
GREEN,
BLUE;
private Color()
{
System.out.println("Constructor called for : " + this.toString());
}
public void colorInfo()
{
System.out.println("Universal Color");
}
}
public class Test {
public static void main(String[] args) {
Color c1 = Color.RED;
System.out.println(c1);
c1.colorInfo();
}
}
Output:
Constructor called for : RED
Constructor called for : GREEN
Constructor called for : BLUE
RED
Universal Color
5

## Slide 6
Exercise 1: Enums
• Write a simple Vending Machine program, which allows money insertion and
buying a single drink and returning the money (unlimited in machine). Before
money insertion, the Vending Machine should show the menu with prices
• Create enum Drinks with beverage drinks (Coke Cola, Sprite, Fanta) with
parameters name and price. Create enum Money with applicable banknotes with
parameter denomination. Assume that coins cannot be used
• Handle exceptions if needed (not enough money, negative values, etc.), if familiar
with exceptions. Otherwise, use error messages
• Assume that if the Vending Machine cannot return the money, because of missing
such a banknote in Money enum, it will return banknote with the closest lesser
nomination, e.g. instead of 5.5$ the customer will be returned 5$. Provide
adequate interaction with the customer
6

## Slide 7
Exercise 1: Enums
• Write a simple Vending Machine program, which allows money insertion and
buying a single drink and returning the money (unlimited in machine). Before
money insertion, the Vending Machine should show the menu with prices
• Create enum Drinks with beverage drinks (Coke Cola, Sprite, Fanta) with
parameters name and price. Create enum Money with applicable banknotes with
parameter denomination. Assume that coins cannot be used
• Handle exceptions if needed (not enough money, negative values, etc.), if familiar
with exceptions. Otherwise, use error messages
• Assume that if the Vending Machine cannot return the money, because of missing
such a banknote in Money enum, it will return banknote with the closest lesser
nomination, e.g. instead of 5.5$ the customer will be returned 5$. Provide
adequate interaction with the customer
7

## Slide 8
Exercise 2: Hospital Management System
We want to implement a hospital management system where we can manage
appointments, bills, patients and doctors.
The users in this system can choose from the main menu what type of user they are,
depending on that, they can make some actions.
We want to keep track of the bills. A bill is defined by a unique ID, it has a name and an
amount.
Don't forget to Draw UML diagram first then implement it
8

## Slide 9
Exercise 2: Hospital Management System
We have three types of users:
• Patient: this user is identified by a unique ID and have a name. They can pay the bill. A
bill belongs to a patient and each patient has one bill.
• Receptionist: this user can give appointments to as many patients as they want. A
patient gets an appointment from one receptionist.
The receptionist can also generate bills. A bill is generated by one receptionist.
• Doctor: this user can check as many patients as he wants, a patient is checked by
one doctor.
9

## Slide 10
UML - Class diagram simple example
public class Person {
private String name;
private int age;
// constructor
// other methods
}
class University {
List<Department > department;
}
class Department {
List<Professor > professors;
}
class Professor extends Person {
List<Department > department;
List<Professor> friends;
}
[Diagram showing class relationships:
- University has a 1 to many (1..*) association with Department.
- Department has a 1 to many (1..*) aggregation with Professor.
- Professor is a specialization (Inheritance) of Person.
- Professor has a 0 to many (0..*) association with Department.
- Professor has a 0 to many (0..*) association with itself (friends).
Legend shows symbols for Association, Navigable association, Inheritance, Realization/Implementation, Dependency, Aggregation, and Composition.]
10

## Slide 11
UML
[A UML class diagram showing a banking system.
- A Bank has many (1..*) Tellers and many (1..*) Customers.
- A Customer has one Bank. A Customer can have multiple (1..*) Accounts, multiple (1..*) Loans, and can interact with multiple (1..*) Tellers.
- A Teller belongs to one Bank.
- An Account belongs to one Customer.
- A Loan belongs to one Customer.
- Checking and Savings are types of Accounts (implied inheritance).
Classes have attributes and methods listed, e.g., Customer has +Id, +Name, +Address and methods like +DepositMoney(), +WithdrawMoney(). Relationships show multiplicity, e.g., 1, +1, +1..*, +0..*.]
11

## Slide 12
Collections
1. List:
An ordered list of objects, which are stored in the order in which they are added to the
list. The elements of the list are accessed by index
2. Set:
A set of non-repeating objects. Only one null reference is allowed in a collection of this
type
3. Map:
Map is used to map each element from one set of objects (keys) to another (values). In
this case, each element from the set of keys is assigned a set of values. At the same
time, one element from a set of values can correspond to 1, 2 or more elements from a
set of keys
12

## Slide 13
Collections Hierarchy
[A diagram shows the Java Collections Framework hierarchy.
- The root is the Collection interface.
- Collection is extended by Set, List, and Queue interfaces.
- Set is implemented by HashSet. SortedSet extends Set and is implemented by TreeSet. LinkedHashSet implements Set.
- List is implemented by ArrayList, Vector, and LinkedList. Stack extends Vector.
- Queue is extended by Deque. Deque is implemented by LinkedList.
- A separate hierarchy starts with the Map interface.
- Map is implemented by HashTable, LinkedHashMap, and HashMap.
- SortedMap extends Map and is implemented by TreeMap.]
13

## Slide 14
List Template
interface ListADT<E>{
int size();
void clear();
boolean isEmpty();
boolean add(E e);
boolean remove(E o);
E get(int index);
E set(int index, E element);
void add(int index, E element);
E remove(int index);
}
14

## Slide 15
List Example
1 // Importing all utility classes
2 import java.util.*;
3
4 // Main class
5 class GFG {
6
7 // Main driver method
8 public static void main(String args[])
9 {
10 // Creating an object of List interface,
11 // implemented by ArrayList class
12 List<String> al = new ArrayList<>();
13
14 // Adding elements to object of List interface
15 // Custom elements
16 al.add("Geeks");
17 al.add("Geeks");
18 al.add(1, "For");
19
20 // Print all the elements inside the
21 // List interface object
22 System.out.println(al);
23 }
24 }
15

## Slide 16
Exercise 3 (List)
Write a program to create a List of animals. Create 4 methods: adding,
removing, updating and displaying the animals
16

## Slide 17
Set Template
interface SetADT<E> {
int size();
void clear();
boolean isEmpty();
boolean add(E e);
boolean remove(E o);
}
17

## Slide 18
Set Example
1 // Importing utility classes
2 import java.util.*;
3
4 // Main class
5 public class GFG {
6
7 // Main driver method
8 public static void main(String[] args)
9 {
10 // Demonstrating Set using HashSet
11 // Declaring object of type String
12 Set<String> hash_Set = new HashSet<String>();
13
14 // Adding elements to the Set
15 // using add() method
16 hash_Set.add("Geeks");
17 hash_Set.add("For");
18 hash_Set.add("Geeks");
19 hash_Set.add("Example");
20 hash_Set.add("Set");
21
22 // Printing elements of HashSet object
23 System.out.println(hash_Set);
24 }
25 }
18

## Slide 19
Exercise 4 (Set)
Write a program program that creates a Set with Strings and then removes all
elements of the Set with the odd length and leaves elements with even length
19

## Slide 20
Map Template
interface MapADT<K,V> {
int size();
void clear();
boolean isEmpty();
V get(K key);
V put(K key, V value);
V remove(K key);
}
20

## Slide 21
Map Example
1 // Java Program to Demonstrate Working of Map interface
2 import java.util.*;
3 class GFG {
4 // Main driver method
5 public static void main(String args[])
6 {
7 // Creating an empty HashMap
8 Map<String, Integer> hm = new HashMap<String, Integer>();
9
10 // Inserting pairs in above Map
11 // using put() method
12 hm.put("a", new Integer(100));
13 hm.put("b", new Integer(200));
14 hm.put("c", new Integer(300));
15 hm.put("d", new Integer(400));
16
17 // Traversing through Map using for-each loop
18 for (Map.Entry<String, Integer> me : hm.entrySet()) {
19 // Printing keys
20 System.out.print(me.getKey() + ":");
21 System.out.println(me.getValue());
22 }
23 }
24 }
21

## Slide 22
Exercise 5 (Map)
Write a program which creates the Map<String, Integer> and then reports if user
input contains repetitive values (and their count) or not
22

## Slide 23
Exercise 3 (Homework): Online Book Reader
[Image of a mobile application UI for an online book reader. The main screen shows "Recommended Books," "Top Authors," and "Popular this week." A second screen shows the details for a book titled "Freedom is space for the spirit," including a plot synopsis and a "BUY NOW $19.99" button.]
Asked in Amazon, Microsoft, and many more interviews
23

## Slide 24
Exercise 6 (Homework): Online Book Reader
Hint: Let's assume we want to design a basic online reading system which provides the
following functionality:
• Searching the database of books and reading a book.
• User membership creation and extension.
• Only one active user at a time and only one active book by this user
The class OnlineReaderSystem represents the body of our program. We could
implement the class such that it stores information about all the books, deals with user
management, and refreshes the display, but that would make this class rather hefty.
Instead, we've chosen to tear off these components into Library, UserManager, and
Display classes.
24

## Slide 25
Exercise 6 (Homework): Online Book Reader
• First try to design the logic with UML.
• Then start coding...
25

## Slide 26
References
• Overview of Inheritance, Interfaces and Abstract Classes in Java | by Isaac Jumba | Medium
• Polymorphism in Java
• List Interface in Java with Examples
• Set Interface in Java
• Map Interface in Java
• Set (Java Platform SE 7 )
• Map (Java Platform SE 8 )
• Java Iterator
• Java - How to Use Iterator?
• Interface vs abstract classes
• Interface vs abstract classes
26

# File 3: Tutorial Slides

## Slide 1
Introduction to
Programming
Tutorial 11
Munir Makhmutov
Fall Semester 2025
Innopolis University

## Slide 2
Agenda
• Interface
• Enumerations
• Java Collections framework
• Iterator
• Examples
2

## Slide 3
Interface
• In Java, an interface specifies the behavior of a class by providing
an abstract type
• It needs to be implemented and its non-default (abstract)
methods should be implemented by extending classes (not only).
Interface cannot be instantiated
• It can't have constructors
• It can have static methods since JDK8
• Class can implement multiple interfaces
• Interface can extend (not implement) other interfaces
• Public Default methods with bodies appeared since JDK8
3

## Slide 4
Interface
• Interface can't have a state, only constants (public static final added automatically)
• By default all methods are public
    - Can't be package-private and protected
• Since JDK9 private methods can be created (can be used inside by
default and other private methods).
    - Can be static and non-static
    - Not considered as default method even with the body
4

## Slide 5
Interface Example
• Let's check the code
5

## Slide 6
Enumerations
From previous lecture
Java extensions
Java enum types are much more powerful than
their counterparts in other languages.
• Enum members can be initialized.
• The enum class body can include methods and
other fields
• The compiler automatically adds some special
methods when it creates an enum
• Enum members can have... bodies (!)
6

## Slide 7
Enumerations
From previous lecture
Java extensions
Enum members can be initialized
enum Coin {
PENNY , NICKEL , DIME , QUARTER ;
}
7

## Slide 8
Enumerations
From previous lecture
Java extensions
Enum members can be initialized
The value associated
with the enumerator
enum Coin {
PENNY(1), NICKEL(5), DIME(10), QUARTER(25);
}
Values (in cents)
of American coins
!
8

## Slide 9
Enumerations
From previous lecture
Java extensions
Enum members can be initialized
The value associated
with the enumerator
enum Coin {
PENNY(1), NICKEL(5), DIME(10), QUARTER(25);
private final int value;
Coin(int value) { this.value = value; }
}
Values (in cents)
of American coins
!
!!
Private by
default
The enum constructor!
9

## Slide 10
Enumerations
From previous lecture
Java extensions
Enum members can be initialized
Private by
default
enum Coin {
The value associated
with the enumerator
PENNY(1), NICKEL(5), DIME (10), QUARTER(25);
private final int value;
Coin(int value) { this.value = value; }
}
Values (in cents)
of American coins
!
!!
...
Coin c = Coin.DIME;
...
The enum constructor!
The value of 10 is
automatically
associated with c
10

## Slide 11
Enumerations
From previous lecture
Java extensions
Enumerations can have methods
enum Coin {
PENNY(1), NICKEL(5), DIME(10), QUARTER(25);
Coin(int value) { this.value = value; }
private final int value;
public int getValue() { return value; }
}
...
Coin c = Coin.DIME;
int v = c.getValue();
...
Returns 10
11

## Slide 12
Enumerations
From previous lecture
Java extensions
Enum predefined methods
public static E[] values();
From the Java
Reference Manual
Returns an array containing the constants of this
enum type, in the order they're declared. This
method may be used to iterate over the constants:
12

## Slide 13
Enumerations
From previous lecture
Java extensions
Enum predefined methods
public static E[] values();
From the Java
Reference Manual
Returns an array containing the constants of this
enum type, in the order they're declared. This
method may be used to iterate over the constants:
public class Test {
enum Season { WINTER, SPRING, SUMMER, FALL }
public static void main(String[] args) {
for (Season s : Season.values())
System.out.println(s);
}
}
Output
WINTER
SPRING
SUMMER
FALL
13

## Slide 14
Enumerations
Java extensions
Enum predefined methods
public final int ordinal();
From the Java
Reference Manual
Returns the ordinal of this enumeration constant
(its position in its enum declaration, where the
initial constant is assigned an ordinal of zero):
public class Test {
enum Season { WINTER, SPRING, SUMMER, FALL }
public static void main(String[] args) {
for (Season s : Season.values())
System.out.println(s.ordinal());
}
}
Output
0
1
2
3
14

## Slide 15
Enumerations
Java extensions
Enum members can have bodies
enum Operation {
PLUS { double eval(double x, double y) { return x + y; } },
MINUS { double eval(double x, double y) { return x - y; } },
TIMES { double eval(double x, double y) { return x * y; } },
DIVIDE { double eval(double x, double y) { return x / y; } };
// Each constant supports an arithmetic operation
abstract double eval(double x, double y);
public static void main(String args[]) {
double x = Double.parseDouble(args);
double y = Double.parseDouble(args);
for (Operation op : Operation.values())
System.out.println(op.ordinal() + ": " + x + " " + op + " " + y +
" = " + op.eval(x, y));
}
}
15

## Slide 16
Enumerations
Java extensions
Enum members can have bodies
enum Operation {
PLUS { double eval(double x, double y) { return x + y; } },
MINUS { double eval(double x, double y) { return x - y; } },
TIMES { double eval(double x, double y) { return x * y; } },
DIVIDE { double eval(double x, double y) { return x / y; } };
// Each constant supports an arithmetic operation
abstract double eval(double x, double y);
public static void main(String args[]) {
double x = Double.parseDouble(args);
double y = Double.parseDouble(args);
for (Operation op : Operation.values())
System.out.println(op.ordinal() + ": " + x + " " + op + " " + y +
" = " + op.eval(x, y));
}
}
Output
0: 2.0 PLUS 4.0 = 6.0
1: 2.0 MINUS 4.0 = -2.0
2: 2.0 TIMES 4.0 = 8.0
3: 2.0 DIVIDE 4.0 = 0.5
16

## Slide 17
Collections Framework
The main purpose of Collections Framework in Java is to
store a collection of some elements
The standard set of Java collections serves to relieve
the programmer of the need to independently
implement recursive data types (Lists, Trees) and
provides it with additional features
Collections can store any reference data type
17

## Slide 18
Lists
An ordered list of objects, which are stored in the
order in which they are added to the list. The elements
of the list are accessed by index
Requires java.util.List
package to be imported
Requires java.util.ArrayList
package to be imported
List<Integer> list = new ArrayList<>();
list.add(5);
list.add(new Integer(0));
System.out.println(list); //
18

## Slide 19
List Template
interface ListADT<T> {
public void add(T t);
public T remove(T t);
public void clear();
public int size();
public get (int index);
public set (int index, T t);
}
19

## Slide 20
List Example
import java.util.*;
// Main class
class GFG {
// Main driver method
public static void main(String args[])
{
// Creating an object of List interface,
// implemented by ArrayList class
List<String> al = new ArrayList<>();
// Adding elements to object of List interface
// Custom elements
al.add("Geeks");
al.add("Geeks");
al.add(1, "For");
// Print all the elements inside the
// List interface object
System.out.println(al);
}
}
20

## Slide 21
Sets
A set of non-repeating objects. Only one null reference
is allowed in a collection of this type
Requires java.util.Set
package to be imported
Requires java.util.HashSet
package to be imported
Set<Integer> set = new HashSet<>();
set.add(5);
set.add(new Integer(5));
System.out.println(set); //
21

## Slide 22
Set Template
interface SetADT<T> {
public void add(T t);
public T remove(T t);
public void clear();
public int size();
public get (int index);
public set (int index,T t);
}
22

## Slide 23
Set Example
// Java program Illustrating Set Interface
// Importing utility classes
import java.util.*;
// Main class
public class GFG {
// Main driver method
public static void main(String[] args)
{
// Demonstrating Set using HashSet
// Declaring object of type String
Set<String> hash_Set = new HashSet<String>();
// Adding elements to the Set
// using add() method
hash_Set.add("Geeks");
hash_Set.add("For");
hash_Set.add("Geeks");
hash_Set.add("Example");
hash_Set.add("Set");
// Printing elements of HashSet object
System.out.println(hash_Set);
}
}
23

## Slide 24
Maps
Map is used to map each element from one set of
objects (keys) to another (values). In this case, each
element from the set of keys is assigned a set of
values. At the same time, one element from a set of
values can correspond to 1, 2 or more elements from a
set of keys
Requires java.util.Map
package to be imported
Map<Integer, String> map = new HashMap<>();
map.put(1, "Peter");
map.put(2, "Alex");
map.put(-1,"Peter");
map.put(1,"Max");
System.out.println(map); // {-1=Peter, 1=Max, 2=Alex}
Requires java.util.HashMap
package to be imported
24

## Slide 25
Map Template
interface MapADT<K,V> {
public void add(K k,V v);
public T remove(K k);
public void clear();
public int size();
public get (K k);
public set (K k,V v);
}
25

## Slide 26
Map Example
// Java program to demonstrate
// the working of Map interface
import java.util.*;
class HashMapDemo {
public static void main(String args[])
{
Map<String, Integer> hm
= new HashMap<String, Integer>();
hm.put("a", new Integer(100));
hm.put("b", new Integer(200));
hm.put("c", new Integer(300));
hm.put("d", new Integer(400));
// Traversing through the map
for (Map.Entry<String, Integer> me : hm.entrySet()) {
System.out.print(me.getKey() + ":");
System.out.println(me.getValue());
}
}
}
26

## Slide 27
List vs Set vs Map
| List | Set | Map |
| :--- | :--- | :--- |
| Index-based methods to insert, update, delete, and search the elements | Unordered collection of objects | Java Map can store pairs of keys and values |
| It can have duplicate elements and we can also store null elements | Duplicate values cannot be stored | Each unique key is linked to a specific value |
| List preserves the insertion order, it allows positional access and insertion of elements | Duplicate item will be ignored in Set and it will not print in the final output | Once stored in a Map, you can later look up the value using just the key |
27

## Slide 28
Hierarchy
[A diagram shows the Java Collections Framework hierarchy.
- The root is the Collection interface.
- Collection is extended by Set, List, and Queue interfaces.
- Set is implemented by HashSet. SortedSet extends Set and is implemented by TreeSet. LinkedHashSet implements Set.
- List is implemented by ArrayList, Vector, and LinkedList. Stack is a subtype of Vector.
- Queue is extended by Deque. Deque is implemented by LinkedList.
- A separate hierarchy starts with the Map interface.
- Map is implemented by HashTable, LinkedHashMap, and HashMap.
- SortedMap extends Map and is implemented by TreeMap.]
28

## Slide 29
Set Implementations
| | HashSet | LinkedHashSet | TreeSet |
| :--- | :--- | :--- | :--- |
| **Element Ordering** | no | yes, addition order | yes, ascending order |
| **Thread safety** | no | no | no |
| **Algorithmic complexity of finding elements**| Ο(1) | Ο(1) | O(log n) |
| **Data structure under the hood** | hash table | hash table | red-black tree |
29

## Slide 30
Map Implementations
| | HashMap | HashTable | TreeMap |
| :--- | :--- | :--- | :--- |
| **Element Ordering** | no | no | yes |
| **null as value** | yes | no | yes/no |
| **Thread safety** | no | yes | no |
| **Algorithmic complexity of finding elements**| Ο(1) | Ο(1) | O(log n) |
| **Data structure under the hood**| hash table | hash table | red-black tree |
30

## Slide 31
Iterator in Java
An Iterator is an object that can be used to loop
through collections, like ArrayList and HashSet. It is
called an "iterator" because "iterating" is the technical
term for looping
Requires java.util.Iterator
package to be imported
Set<Integer> set = new HashSet<>();
set.add(5);
set.add(new Integer(5));
set.add(1);
The iterator() can be used
to get an Iterator for any
collection
Iterator<Integer> iterator = set.iterator();
while(iterator.hasNext()) {
System.out.print(iterator.next());
} // 15
31

## Slide 32
Iterator in Java
// Import the ArrayList class and the Iterator class
import java.util.ArrayList;
import java.util.Iterator;
public class Main {
public static void main(String[] args) {
// Make a collection
ArrayList<String> cars = new ArrayList<String>();
cars.add("Volvo");
cars.add("BMW");
cars.add("Ford");
cars.add("Mazda");
// Get the iterator
Iterator<String> it = cars.iterator();
// Print the first item
System.out.println(it.next());
}
}
32

## Slide 33
Main Implementations of List, Set, Map
| Interface | Class / Implementation | Description |
| :--- | :--- | :--- |
| List | ArrayList | List |
| | LinkedList | List |
| | Vector | Vector |
| | Stack | Stack |
| Set | HashSet | Lots of |
| | TreeSet | Lots of |
| | SortedSet (extension interface) | Sorted set |
| Map | HashMap | Map / Dictionary |
| | TreeMap | Map / Dictionary |
| | SortedMap (extension interface) | Sorted dictionary |
| | Hashtable | Hash table |
33

## Slide 34
Summary
• Enumerations
• Java Collections framework
• Iterator
• Examples
34