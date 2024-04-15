age = 0

if age <= 0:
    print("Invalid age")
    exit()
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")