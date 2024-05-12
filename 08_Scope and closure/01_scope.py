username = "iqbal"

def func():
    username = "abc"
    return username

print(username) # iqbal
print(func()) # abc


x = 20

def func2(y):
    z = x + y
    return z

print(func2(10))

# def func3():
#     global x
#     x = 10
# func3()
# print(x)


def f1():
    x = 5
    def f2():
        print(x)
    return f2

result = f1()
result()


def power_of(n):
    def inner_function(x):
        return x ** n
    return inner_function

square = power_of(2)
cube = power_of(3)

print(square(3))  # Output: 9
print(cube(3))    # Output: 27

def outer_def(message):
    def inner_def():
        print(message)
    return inner_def

my_func = outer_def("Hellow, World!")
my_func()



def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter()) # Output: 1
print(my_counter()) # Output: 2
print(my_counter()) # Output: 3
 
