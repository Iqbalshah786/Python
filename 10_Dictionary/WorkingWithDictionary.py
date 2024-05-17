# dictionaries can store an almost limitless amount of information
# A dictionary in Python is a collection of key-value pairs.
alien_0 = {'color': 'green', 'points': 5}

# Accessing Values in a Dictionary
print(alien_0['color'])
print(alien_0['points'])


# Working with Dictionaries
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_postition'] = 25
print(alien_0)
#It’s sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it.
# Typically, you will use empty dictionaries when storing user-supplied data
# in a dictionary or when writing code that generates a large number of keyvalue pairs automatically
alien_1 = {'color:red , points: 5'}

# Modifying Values in a Dictionary
print(f"The alien 0 is  {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien 0 now is {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'medium'
print(f"Original x_position: {alien_0['x_position']}")
#Moving the alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3

# The new position is the old position plus the new position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position:  {alien_0['x_position']}")
alien_0['points'] = 5
print(alien_0)
# Removing Key-Value Pairs
del alien_0['points']
print(alien_0)

# Be aware that the deleted key-value pair is removed permanently
#  A Dictionary of Similar Object
favourite_languages = {
    'jen':'Java',
    'hanif':'C',
    'iqbal':'Python',
    'aliyan':'C++',
}
language = favourite_languages['iqbal'].title()
print(f"Iqbal's favorite language is {language}")

# Using get() to Access Values
# you can use the get() method to set
# a default value that will be returned if the requested key doesn’t exist.


a_try = favourite_languages.get('mustan','Not included in the list')
print(a_try)

# If you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None. The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value

# Looping Through All Key-Value Pairs
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
}
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# the method items(),  returns a sequence 
# of key-value pairs. The for loop then assigns each of these pairs to the two variables provided.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name,languge in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {languge.title()}")

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(f"{name.title()}")
#default behaviour
print("")
for name in favorite_languages:
    print(name)

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi! {name.title()}.")

    if name in friends:
        languge = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {languge}")
if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# # Looping Through All Values in a Dictionary
print("")
print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())

# # This approach pulls all the values from the dictionary without check- ing for repeats.
# #  This might work fine with a small number of values, but in a poll with a large number of respondents, 
# # it would result in a very repetitive list. To see each language chosen without repetition, we can use a set. 
# # A set is a collection in which each item must be unique:

print("")
print("The following languages have been mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())
print()

# # Nesting
# # A List of Dictionaries

aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] =='yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

 
# #show first five aliens
for alien in aliens[:5]:
    print(alien)
#show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
# # Summarize the order.
print(f"You ordered a {pizza['crust']} - crust pizza  "
      "with the following toppings: ")

for  topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
}
print(favorite_languages.items())
for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are: ")
    else:
        print(f"\n{name.title()}'s favorite language is: ")

    for language in languages:
            print(f"\t{language.title()}")
   

# A Dictionary in a Dictionary

users = {
    'einstein' :{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie': {
          'first': 'marie',
          'last': 'curie',
          'location': 'paris',
          },
}
for username , user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")

