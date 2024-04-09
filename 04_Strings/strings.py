#String Operators
# The + operator concatenates strings: 
s = "spam"
t = "egg"

print(s+t) # spamegg

# The * operator creates multiple copies of a string:
n = 2 
print(s*n) # spamspam

# The in and not in operators provide boolean testing of membership within a string:
print(s in "I saw spamalot!") # true

# String Indexing
s = "mybook"
print(s[0]) # m
print(s[1]) # y
print(s[5]) # k
print(s[len(s)-1]) # k

# negative string indexing:
print(s[-1]) # k
print(s[-3]) # o

# String Slicing
print(s[:]) # returns a copy of the string
print(s[2:5]) # boo

# negative index slicing:
print(s[-5:-1]) # yboo
print(s[-4:-1]) # boo

# slice with a stride:
print(s[0:6:2]) # mbo
print(s[0:6:3]) # mo

y = "12345" * 5
print(y) # 1234512345123451234512345
print(y[::5]) # 11111
print(y[4::5]) # 55555
print(y[::-5]) # 55555

# Reverse a String using Slicing
y = y[::-1]
print(y) # 5432154321543215432154321


# Escape characters 
print("Hello \t World")
print("Hello \nWorld")

feedback = "He said, \"Tea is awsome.\""
print(feedback)

print('This string will not include \
backslashes or newline characters.')


# String interpolation
age = 10
print(f"My age is {age}")

name = "Iqbal"
print(f"{name}, happy birthday ahead of time to your {age+1} years old")

#Change title in a string with methods

name = "iqbal shah"
print(name.title()) # Iqbal Shah
name = "Iqbal Shah"
print(name.upper())
print(name.lower())



# python built in string functions

# strip
favorite_languae = "python "
print(favorite_languae)
favorite_languae = favorite_languae.rstrip() # strips white space from right side
favorite_languae = " python"
print(favorite_languae)
favorite_languae = favorite_languae.lstrip() # strips white space from left side
print(favorite_languae)
# both sides at once using strip()
favorite_languae = " programming language "
print(favorite_languae)
favorite_languae = favorite_languae.strip()
print(favorite_languae)

# len()
my_str = "programming"
print(len(my_str)) # 11

# enumerate()
list_enumerate = list(enumerate(my_str))
print(list_enumerate)
# captilize()
print(my_str.capitalize())
#find()
print(my_str.find("g"))
text = "Python is fun"
# split the text from space
print(text.split())
# The split() method returns a list of strings.

