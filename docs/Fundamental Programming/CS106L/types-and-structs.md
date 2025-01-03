# Lecture 2: Types and Structs

**CS 106L: Standard C++ Programming (Autumn 2024):**

* Course Website: [Stanford](https://web.stanford.edu/class/cs106l/)
* Recordings: [Youtube](https://youtube.com/playlist?list=PLCgD3ws8aVdolCexlz8f3U-RROA0s5jWA&si=iaFdVf21mVLtKiIU)

## Types

A **type** refers to the “category” of a variable

C++ comes with built-in types:

* `int 106`
* `double 71.4`
* `string “Welcome to CS106L!”`
* `bool true false`
* `size_t 12 // Non-negative`

### Static Typing

* Every variable must declare a type
* Once declared, the type cannot change

### Why static typing?

* More efficient
* Easier to understand and reason about
* Better error checking

```python
def add_3(x):
    return x + 3

add_3("CS106L") # Oops, that's a string. Runtime error!
```

```cpp
int add_3(int x) {
    return x + 3;
}

add_3("CS106L"); // Can't pass a string when int expected. Compile time error!
```

### Function Overloading

Defining two functions with the same name but different signatures

```cpp
double func(int x) { // (1)
    return (double) x + 3; // typecast: int → double
}

double func(double x) { // (2)
    return x * 3;
}

func(2); // uses version (1), returns (5.0)
func(2.0); // uses version (2), returns (6.0)
```

## Structs

Structs bundle data together

```cpp
struct StanfordID {
    string name; // These are called fields
    string sunet; // Each has a name and type
    int idNumber;
};

StanfordID id; // Initialize struct
id.name = "Jacob Roberts-Baca"; // Access field with ‘.’
id.sunet = "jtrb";
id.idNumber = 6504417;
```

Returning multiple values

```cpp
StanfordID issueNewID() {
    StanfordID id;
    id.name = "Jacob Roberts-Baca";
    id.sunet = "jtrb";
    id.idNumber = 6504417;
    return id;
}
```

List Initialization

```cpp
// Order depends on field order in struct. ‘=‘ is optional
StanfordID jrb = { "Jacob Roberts-Baca", "jtrb", 6504417 };
StanfordID fi { ”Fabio Ibanez", ”fibanez", 6504418 };
```

Using list initialization

```cpp
StanfordID issueNewID() {
    StanfordID id = { "Jacob Roberts-Baca", "jtrb", 6504417 };
    return id;
}

StanfordID issueNewID() {
    return { "Jacob Roberts-Baca", "jtrb", 6504417 };
}
```

A **struct** bundles **named variables** into a new type

### std::pair

```cpp
struct Order {
    std::string item;
    int quantity;
};

Order dozen = { "Eggs", 12 };


std::pair<std::string, int> dozen { "Eggs", 12 };
std::string item = dozen.first; // "Eggs"
int quantity = dozen.second; // 12
```

`std::pair` is a **template**

```cpp
template <typename T1, typename T2>
struct pair {
    T1 first;
    T2 second;
};
std::pair<std::string, int>

struct pair {
    std::string first;
    int second;
};
```

## std ― The C++ Standard Library

See the official standard at [cppreference.com!](cppreference.com)

To use `std::pair`, you must `#include` it. `std::pair` is defined in a header file called ``utility``

```cpp
#include <utility>

std::pair<double, double> p { 1.0, 2.0 };

namespace std {
    template
    <typename T1, typename T2>
    struct pair {
        T1 first;
        T2 second;
    };
}
```

## The using keyword

Typing out long type names gets tiring

We can create type aliases with the `using` keyword

```cpp
std::pair<bool, std::pair<double, double>> solveQuadratic(double a, double b, double c)

using Zeros = std::pair<double, double>;
using Solution = std::pair<bool, Zeros>;
```

## The auto keyword

The auto keyword tells the compiler to infer the type

```cpp
std::pair<bool, std::pair<double, double>> result = solveQuadratic(a, b, c);

auto result = solveQuadratic(a, b, c);
// This is exactly the same as the above! 
// result still has type std::pair<bool, std::pair<double, double>>
// We just told the compiler to figure this out for us!
```
