fruit = "Banana"
fruit = fruit.lower()
color = "Green"
color = color.lower()

if fruit.lower() == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe")
