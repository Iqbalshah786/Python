while True:
    password = input("Enter a password: ")

    if (
        any(char.isdigit() for char in password) and
        any(char.isupper()for char in password) and
        len(password)>=5
    ):
        print("Password is fine")
        break
    else:
        print("Password does not meet the policy requirements. Please try again.")

