def divide(a, b):   
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Please provide two numbers"
    
print(divide(1, 0))  # Cannot divide by zero
print(divide(1, 'a'))  # Please provide two numbers
print(divide(1, 2))  # 0.5