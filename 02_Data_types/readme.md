# Variable name rules and restrctions:

Variables names can **start with a letter or underscore.**

* ✅ _dog , dogs    
* ❌ 2dogs


The rest of the name **can consist of letters, numbers, or underscores.**
**Example :**
* ✅ dog2 , dog_2    
* ❌ Hi@you

**Names are case-sensitive**

* DOGS != Dogs

# Variable naming convention:

- Most variables should be **snake_case** (underscores between words)


* Variables that start and end with **two underscores** (called **"dunder"** for double underscore) are
supposed to be **private** or **left alone**
  - __no_change__
- Most variables should be also be lowercase, with some exceptions:
  - **UpperCamelCase** usually refers to a class (in OOP)
  - **CAPITAL_SNAKE_CASE** usually refers to **constants** (e.g. PI = 3.14)

# Data types:

| Data type | Description                                                |
|-----------|------------------------------------------------------------|
| boolean   | True or False values                                       |
| int       | An integer (1, 2, 3)                                       |
| float     | A floating-point number with decimal precision              |
| complex   | A complex number in the form of a + bj, where a and b are real numbers and j is the imaginary unit |
| str       | A sequence of Unicode characters                           |
| list      | An **ordered** sequence of values of other data types, e.g. [1, 2, 3] or ["a", "b", "c"] |
| tuple     | An **ordered** immutable sequence of values                |
| set       | An **unordered** collection of unique elements              |
| frozenset | An **immutable** version of set                            |
| dict      | A collection of key-value pairs, e.g. {"first_name": "Morteza", "last_name": "Kiadi"} |
| NoneType  | Represents the absence of a value (similar to null in other languages) |


# Type Casting
Type casting in Python refers to the process of converting one data type into another. Python provides several built-in functions for type casting, such as **int(), float(), str(), list(), tuple(), set(), dict(),** etc.

# Dynamic Typing: 
In Python, the variable data types are set when their values are assigned. The data type
changes happen automatically when their values are assigned. This is different than other languages that are
**statically typed** and you should set its data type ahead and stay with it (like: **int variable=10**)
