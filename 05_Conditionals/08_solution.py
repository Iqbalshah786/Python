password  = "12345678910"
password_length = len(password)

if password_length < 6:
    strength = "Weak"
elif password_length <= 10:
    strength = "Medium"
elif password_length > 10:
    strength = "Strong"

print("Password strength is: ", strength)