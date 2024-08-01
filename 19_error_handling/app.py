def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize("hello", "cyan") # ValueError
colorize([],"cyan") # TypeError
colorize("hello", "blahblah")  # ValueError : color is invalid color