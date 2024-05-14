# creating List 
Letters = ["a","b","c","d"]
zeros = [0] * 5 # [0, 0, 0, 0, 0]
combined = Letters + zeros # ['a', 'b', 'c', 'd', 0, 0, 0, 0, 0]
numbers = list(range(20)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
chars = list("Hello world!")# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']

# Finding the Length of a List
print(len(Letters))

# nestedList
matrix = [[1,2],[3,4]]
print(matrix)

# Accessing Elements in a List
# we use square brackets to access items in the list
print(Letters[0]) # a
# we can use negative index to access elements from the end of list
print(Letters[-1]) # d

# Modifying Elements in a List
new_list = ["lemon","Masala","Mint","water"]
new_list[1] = "Sugar"
print(new_list) # ['lemon', 'Sugar', 'Mint', 'water']
new_list[0:2] = ["watermelon","mango"]
print(new_list) # ['watermelon', 'mango', 'Mint', 'water']

# List Slicing

print(Letters[0:3]) # ['a', 'b', 'c']
print(Letters[0::2]) # gets every 2 item in the list
print(Letters[::-1]) # returns the list in reverse order

# Appending Elements to the End of a List
# The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list.

Letters.append("e")

# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert() method.
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']

# Removing Elements from a List
# If you know the position of the item you want to remove from a list, you can use the del statement and it does not return the value also it removes the first occurrence.
del motorcycles[0]
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# Removing an Item Using the pop() Method
# pop() also removes the item from the list but it returns the value
last_owned = motorcycles.pop()
print(last_owned) #suzuki
print(motorcycles) # ['honda', 'yamaha']

# Popping Items from Any Position in a List
# You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses:

first_owned = motorcycles.pop(0)
print(first_owned) # honda

# Removing an Item by Value
# The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrence and it does not return the value


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("yamaha")
print(motorcycles)


# Organizing a list
# The sort() method changes the order of the list permanently.Sorting a List Permanently with the sort() Method

cars = ["bmw", "audi", "toyoto", "sabura"]
cars.sort()
#The cars are now in alphabetical order, and we can never revert to the original order
print(cars) # ['audi', 'bmw', 'sabura', 'toyoto']
cars.sort(reverse=True)

print(cars) # ['toyoto', 'sabura', 'bmw', 'audi']

# Sorting a List Temporarily with the sorted() Function
cars = ["bmw", "audi", "toyoto", "sabura"]
print(f"Here is the original list: \n{cars}")
print(f"Here is the sorted list: \n{sorted(cars)}")
print(f"Here is the original list again: \n{cars}")

# Printing a List in Reverse Order
# The reverse() method changes the order of a list permanently,but you can revert to the original order anytime by applying reverse() to the same list a second time.
cars.reverse()
print(cars)
cars.reverse()
print(cars)