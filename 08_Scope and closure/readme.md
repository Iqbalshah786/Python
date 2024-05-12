# Understanding Scopes and Closures in Python

In Python, scopes and closures play a crucial role in how variables are accessed and maintained within functions. Let's explore some examples to understand these concepts better.

## Scopes

### Global and Local Scopes

Python uses a hierarchical structure for variable scopes. Variables declared outside any function have a global scope, while variables declared inside a function have a local scope.

```python
username = "iqbal"

def func():
    username = "abc"
    return username

print(username)  # Output: iqbal
print(func())     # Output: abc

```

In the above example, the username variable has different values in the global and local scopes.

## Enclosing Scopes

Variables defined in an outer function can be accessed by inner functions due to Python support for closures.

```python
def f1():
    x = 5
    def f2():
        print(x)
    return f2

result = f1()
result()

```

Here, f2 can access the x variable defined in the enclosing scope of f1

## Closures

### Creating Closures
Closures allow functions to retain references to variables from outer scopes even after the outer function has finished executing.

```python

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3

```

In this example, the increment function maintains and increments the count variable from the outer scope of counter using the nonlocal keyword.

## Power of Closures

Closures can be used to create functions that remember the value of their enclosing scope variables.

```python
def power_of(n):
    def inner_function(x):
        return x ** n
    return inner_function

square = power_of(2)
cube = power_of(3)

print(square(3))  # Output: 9
print(cube(3))    # Output: 27
```

Here, inner_function retains the value of n from the power_of function, allowing it to calculate squares and cubes.