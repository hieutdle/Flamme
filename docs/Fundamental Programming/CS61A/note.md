# USB CS61A Note

## Higher-Order Functions

Higher-order functions are functions that either:

- Take one or more functions as arguments.
- Return a function as their result

```py
def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first n terms of a sequence.

    >>> summation(5, cube)
    225
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1

    return total
```

## Function Composition

Function composition is the process of combining two or more functions to create a new function.

```py
def square(x):
    return x * x


def triple(x):
    return x * 3


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


print(square(5))
print(triple(5))

25
15

squiple = compose1(square, triple)
print(squiple(5))

225

tripare = compose1(triple, square)
print(tripare(5))

75
```

## Lambda functions

They're just...functions with different syntax. Lambda is a convenience feature to more easily define small, one-off functions.

```py
square = lambda x: x * x

(lambda x: x * x)(5)

def square(x):
    return x * x

```

Only `def` statement give the function an intrinsic name.

`repr()` is a built-in function that returns a string representation of an object

```py
repr(square)
<function <lambda> at 0x7fa3a158d300>
<function square at 0x7fa3a158d3a0>
```

## Currying

Transforming a multi-argument function into single-argument, higher-order function.

Start with a function that takes multiple arguments -> convert it into a series of nested functions:

```py
f(a, b, c) → f(a)(b)(c)
```

```py
def add(x, y, z):
    return x + y + z

def add(a):
    return lambda b: lambda c: a + b + c

# Usage
result = add(1)(2)(3)
print(result)
```

## Decorators

Modify or enhance the behavior of functions or methods

[The best explanation of Python decorators](https://gist.github.com/Zearin/2f40b7b9cfc51132851a)

In Python, `*args` and `**kwargs` are special syntax used to pass a variable number of arguments to a function. They allow you to handle an arbitrary number of positional and keyword arguments.

1. **`*args`**:
   - Used to pass a variable number of positional arguments.
   - When a function uses `*args`, it collects any extra positional arguments passed to the function and stores them as a tuple.
   - For example:
     `def func(*args):     print(args)  func(1, 2, 3)  # Output: (1, 2, 3)`
   - Here, `func(1, 2, 3)` passes three arguments, which are collected in `args` as a tuple `(1, 2, 3)`.
2. **`**kwargs`\*\*:
   - Used to pass a variable number of keyword arguments.
   - When a function uses `**kwargs`, it collects any extra keyword arguments as a dictionary.
   - For example:
     `def func(**kwargs):     print(kwargs)  func(a=1, b=2)  # Output: {'a': 1, 'b': 2}`
   - In this case, `func(a=1, b=2)` creates a dictionary `kwargs` containing the keys and values `{ 'a': 1, 'b': 2 }`.

```py
def trace1(fn):
    def traced(x):
        print("Before the function call")
        result = print(fn(x))
        print("After the function call")
        return result

    return traced  # Ensure the wrapper function is returned


# Original function
def square(x):
    return x * x


# Manually applying the decorator
decorated_square = trace1(square)
decorated_square(5)  # Output: Decorator applied manually


# Using the decorator with @ syntax
@trace1
def square_with_decorator(x):
    return x * x


square_with_decorator(5)  # Output: Decorator applied via @trace1
```

```py
@trace1
def triple(x):
    return 3 * x
```

is identical to

```py
def triple(x):
    return 3 * x
triple = trace1(triple)
```

## Recursive Functions

A function is called recursive if the body of that function calls itself, either directly or indirectly

- The `def` statement header is similar to other functions
- Conditional statements check for **base case**
- Base cases are evaluated **without recursive calls**
- Recursive cases are evaluated **with recursive calls**

```py
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
```

## Tuples

Tuples are immutable sequences. Immutable values are protected from mutation.

```py
t = (1, 2, 3)
```

## Iterators

A container can provide an iterator that provides access to its elements in some order

- `iter(iterable)`: Return an iterator over the elements of an iterable value
- `next(iterator)`: Return the next element from an iterator

```py
s = [1, 2, 3]
t = iter(s)
next(t)  # 1
next(t)  # 2

u = iter(s)
next (u)  # 1
next(t) # 3
```

The order of items in a dictionary is the order in which they were added (Python 3.6+). Historically, the order of items in a dictionary was arbitrary order (Python 3.5 and earlier).

## Built-in Functions for Iterators

- `map(func, iterable)`: Iterate over func(x) for x in iterable
- `filter(func, iterable)`: Iterate over x in iterable if func(x)
- `zip(*iterables)`: Iterate over co-indexed (x, y) pairs
- `reversed(sequence)`: Iterate over x in a sequence in reverse order

To view the contents of an iterator, place the resulting elements into a container

- list(iterable): Create a list containing all x in iterable
- tuple(iterable): Create a tuple containing all x in iterable
- sorted(iterable): Create a sorted list containing all x in iterable

```py
s = [1, 2, 3]
list(zip(s,reversed(s)))  # [(1, 3), (2, 2), (3, 1)]
```

## Generators

- A **generator function** is a function that `yield`s values instead of `return`ing them.
- A normal function `return`s once; a **generator function** `yield`s multiple times.
- A **generator** is an iterator created automatically by a generator function.
- When a **genreator function is called**, it returns a **generator** that iterates over the `yield`ed values.

```py
def evens(start, end):
    # 2 = 1 + 1%2
    even = start + (start % 2)
    while even <= end:
        yield even
        even += 2


print(list(evens(1, 10)))

# [2, 4, 6, 8, 10]

t = evens(2, 10)
print(next(t))
# 2
print(next(t))
# 4
```

## String Representations

The `repr` function returns a Python expression (a string) that evaluates to an equal object

```py
repr(object) -> string

Return the canonical string representation of the object.
For most object types, eval(repr(object)) == object.
```

The result of calling `repr` on a value is what Python prints in an interactive session.

In Python, all objects produce two string representations:
• The `str` is legible to humans
• The `repr` is legible to the Python interpreter
The str and repr strings are often the same, but not always

```py
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> str(half)
'1/2'
>>> repr(half)
'Fraction(1, 2)'
```

## String Interpolation

String interpolation involves evaluating a string literal that contains expressions.

Using string concatenation:

```py
>>> from match import pi
>>> 'pi starts with' + str(pi) + '...'
'pi starts with 3.14159...'

>>> print('pi start with' + str(pi) + '...')
pi starts with 3.14159...
```

Using string interpolation:

```py
>>> f'pi starts with {pi}...'
'pi starts with 3.14159...'
```

## Class Attributes

Class attributes are shared among all instances of a class because they are attributes of the class itself, not of the instances.

```py
class Account:
    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
```

## Polymorphic function

A function that applies to many (poly) differents forms (morph) of data

`str` and `repr` are both polymorphic; they apply to any object

`repr` invokes a zero-arugment method `__repr__` on its argument

`str` invokes a zero-argument method `__str__` on its argument

The behavior of `repr` is slightly more complicated than invoking `__repr__` on its argument

- An instance attribute called **repr** is ignored!. Only class attributes are found

```py
def repr(x):
    return type(x).__repr__(x)
```

- An instance attribute called `__str__` is ignored.
- If no `__str__` attribute is found, use `repr` string

## Interfaces

Message passing: Objects interact by looking up attributes on each other (passing messages)

The attribute look-up rules allow different data types to respond to the same messaage.

A **share message** (attribute name) that elicits similar behavior from different object classes is a powerful method of abstraction

An interface is a set of shared messages, along with a specification of what they mean

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



```

## Special Methods Names in Python

- `__init__`: Method invoked automatically when an object is constructed
- `__repr__`: Method invoked to display an object as a Python expression
- `__add__`: Method invoked to add one object to another
- `__bool__`: Method invoked to convert an object to True or False
- `__float__`: Method invoked to convert an object to a float (real number)

```py
one + two
bool(one)
# same behavior
one.__add__(two)
one.__bool__()
```

## Declarative Programming

In **declarative languages** such as SQL & Prolog:

- A program is a description of the desired result
- The interpreter figures out how to generate the result

In **imperative languages** such as Python & Scheme:

- A program is a description of computational processes
- The interpreter carries out execution/evaluation rules
