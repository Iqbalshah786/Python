magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

print("")

# Using range() to Make a List of Numbers

numbers = list(range(1,6))
print(numbers) # [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))
print(even_numbers)

myTry = []
for num in range(1, 11):
    myTry.append(num**2)
print(myTry)

# List Comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)


# Simple Statistics with a List of Numbers
digits = list(range(0, 11))
print(min(digits)) # 0
print(max(digits)) # 10
print(sum(digits)) # 55