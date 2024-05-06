while True:
    user_input = int(input("Enter number between 1 and 10: "))
    if 1 <= user_input <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")