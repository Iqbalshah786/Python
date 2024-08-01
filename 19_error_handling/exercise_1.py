while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good job, you entered a number")
        break


