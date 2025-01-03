# Lecture 3: Initialization and References

**CS 106L: Standard C++ Programming (Autumn 2024):**

* Course Website: [Stanford](https://web.stanford.edu/class/cs106l/)
* Recordings: [Youtube](https://youtube.com/playlist?list=PLCgD3ws8aVdolCexlz8f3U-RROA0s5jWA&si=iaFdVf21mVLtKiIU)

## Initialization

**What?**: “Provides initial values at the time of construction” - [cppreference.com](cppreference.com)

### 1. Direct initialization

```cpp
#include <iostream>
int main() {
    int numOne = 12.0;
    int numTwo(12.0);
    std::cout << "numOne is: " << numOne << std::endl;
    std::cout << "numTwo is: " << numTwo << std::endl;
    return 0;
}
```

**Notice‼:** is 12.0 an int? **NO** C++ Doesn’t Care.

```cpp
Number One is: 12
Number Two is: 12
```

**Problems:**

```cpp
#include <iostream>
int main() {
    // Direct initialization with a floating-point value
    int criticalSystemValue(42.5);

    // Critical system operations...
    // ...
    std::cout << "Critical system value: " << criticalSystemValue << std::endl; return 0;
}

Critical system value: 42
```

C++ doesn’t care in this case, it doesn’t type check with direct initialization. So C++ said “Meh, I’ll store 42.5 as an int,” and we possibly now have an error. This is commonly called a **narrowing conversion**

### 2. Uniform initialization (C++ 11)

```cpp
#include <iostream>
int main() {
    // Notice the brackets
    int numOne{12.0};
    // should be 12 instead of 12.0
    // int numOne{12};
    float numTwo{12.0};
    std::cout << "numOne is: " << numOne << std::endl;
    std::cout << "numTwo is: " << numTwo << std::endl;
    return 0;
}
```

With uniform initialization C++ does care about types!

```cpp
type `double` cannot be narrowed to `int`
```

Uniform initialization is awesome because:

1. It’s safe! It doesn’t allow for narrowing conversions—which can lead to unexpected behaviour (or critical system failures :o)
2. It’s ubiquitous it works for all types like vectors, maps, and custom
classes, among other things!

```cpp
#include <iostream>
#include <map>

int main() {
 // Uniform initialization of a map
    std::map<std::string, int> ages{
            {"Alice", 25},
            {"Bob" , 30},
            {"Charlie", 35}
        };

    // Accessing map elements
    std::cout << "Alice's age: " << ages["Alice"] << std::endl;
    std::cout << "Bob's age: " << ages.at("Bob") << std::endl;

   // Uniform initialization of a vector
    std::vector<int> numbers{1, 2, 3, 4, 5};
    // Accessing vector elements
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

### 3. Structured Binding (C++ 17)

* A useful way to initialize some variables from data structures with fixed sizes at compile time
* Ability to access multiple values returned by a function
* Can use on objects where the size is known at compile-time

```cpp
#include <iostream>
#include <tuple>
#include <string>

std::tuple<std::string, std::string, std::string> getClassInfo() {
    std::string className = "CS106L";
    std::string buildingName = "Turing Auditorium";
    std::string language = "C++";
    return {className, buildingName, language};
}

int main() {
    auto classInfo = getClassInfo();
    std::string className = std::get<0>(classInfo);
    std::string buildingName = std::get<1>(classInfo);
    std::string language = std::get<2>(classInfo);
    std::cout << "Come to " << buildingName << " and join us for " << className
    << " to learn " << language << "!" << std::endl;
    return 0;
}
```

## References

**What?**: “Declares a name variable as a reference” tldr: a reference is an alias to an already-existing thing - [cppreference.com](cppreference.com).

Use an ampersand (&)

```cpp
int num = 5;
int& ref = num;
ref = 10; // Assigning a new value through the reference
std::cout << num << std::endl; // Output: 10
```

`num` is a variable of type `int`, that is assigned to have the value 5. `ref` is a variable of type `int&`, that is an alias to `num`. So when we assign 10 to `ref`, we also change the value of `num`, since `ref` is an alias for `num`.

A **reference** refers to the same memory as its associated variable!. Passing in a variable by reference into a function just means “Hey take in the actual piece of memory, don’t make a copy!” Passing in a variable by value into a function just means “Hey make a copy, don’t take in the actual variable!”

### A classic reference-copy bug

```cpp
#include <iostream>
#include <math.h>
#include <vector>

void shift(std::vector<std::pair<int, int>> &nums) {
    for (auto [num1, num2] : nums) {
        num1++;
        num2++;
    }
}
```

We’re not modifying `nums` in this function! We ar modifying the std::pair’s inside of nums.

### A classic reference-copy bug: fixed!

```cpp hl_lines="2"
void shift(std::vector<std::pair<int, int>> &nums) {
    for (auto& [num1, num2] : nums) {
        num1++;
        num2++;
    }
}
```

## l-values and r-values

An **l-value** can be to the left or the right of an equal sign!

```cpp
int y = x

✅ AND ✅

x = 344
```

An **r-value** can be ONLY to the right of an equal sign!

`21` can be an r-value for instance because you can have something like:

```cpp
int y = 21

❌ BUT NOT ❌

21 = x
```

### l-value and r-value PAIN

l-value and r-value PAIN

```cpp
#include <stdio.h>
#include <cmath>
#include <iostream>

int squareN(int& num) {
    return std::pow(num, 2);
}

int main()
{
    int lValue = 2;
    auto four = squareN(lValue);
    auto fourAgain = squareN(2);
    std::cout << four << std::endl;
    return 0;
}

error: candidate function not viable: expects an lvalue for 1st argument
int squareN(int& num){
    ^
```

`num` is an **l-value**!

* **r-values** are temporary. Notice that `num` is being passed in by reference!
* We cannot pass in an r-value by reference because they’re temporary!

## const

**What?**: A qualifier for objects that declares they cannot be modified  - [cppreference.com](cppreference.com).

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec{ 1, 2, 3 };  /// a normal vector
    const std::vector<int> const_vec{ 1, 2, 3 };  /// a const vector
    std::vector<int>& ref_vec{ vec };  /// a reference to 'vec'
    const std::vector<int>& const_ref{ vec };  /// a const reference

    vec.push_back(3); /// this is ok!
    const_vec.push_back(3); /// no, this is const!
    ref_vec.push_back(3); /// this is ok, just a reference!
    const_ref.push_back(3); /// this is const, compiler error!
    return 0;
}
```

You can’t declare a non-const reference to a const variable

```cpp
#include <iostream>
#include <vector>

int main()
{
    /// a const vector
    const std::vector<int> const_vec{ 1, 2, 3 };
    std::vector<int>& bad_ref{ const_vec };  /// BAD
    const std::vector<int>& bad_ref{ const_vec }; /// Good!

    return 0;
}
```

## Compiling C++ programs

* A few popular compilers include clang and g++
* Here is how to compile a program using g++

```bash
g++ -std=c++11 main.cpp -o main
```

* `g++`: This is the compiler command
* `-std=c++11` This specifies the c++ version you want to compile in
* `main.cpp`: This is the source file
* `-o`: This means that you’re going to give a specific name to your  executable
* `main`: In this case it’s main

```bash
g++ -std=c++11 main.cpp
```

This is also valid, your  executable will be something like `a.out`
