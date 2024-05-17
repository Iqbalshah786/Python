# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
sample_tuple = (1, 2, 3, "a", "b", "c")
print(sample_tuple)

# Creating a tuple without parentheses (not recommended for beginners)
another_tuple = 1,2,'a','b'

# Accessing Tuple Elements
first_element = sample_tuple[0]
last_element = sample_tuple[-1]

# Slicing tuples
sub_tuple = sample_tuple[1:4]  # Output: (2, 3, "a")
print(sub_tuple)

# Tuple Operations
tuple1 = (1,2,3)
tuple2 = ('a','b','c')

# Concatenation
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)# Output: (1, 2, 3, "a", "b", "c")

# Repetition
repeated_tuple = tuple1 * 2
print(repeated_tuple) # Output: (1, 2, 3, 1, 2, 3)

# Tuple Methods
# count() method returns the number of occurrences of a specified value in a tuple.
print(sample_tuple.count(1)) # Output: 1

# index methods returns the index of the first occurrence of a specified value.
index_of_2 = sample_tuple.index(2)
print(index_of_2) # Output: 1
