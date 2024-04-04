# The True and False values have to start with the capital, otherwise they are not considered as
# Python boolean data type
game_over = True
print(game_over)

# Dynamic Typing
var_data_type=True
# The type(variable name) function returns the data type of that variable
print(type(var_data_type))
var_data_type="my dog"
print(type(var_data_type))
var_data_type= 67/4
print(type(var_data_type))
var_data_type=None
print(type(var_data_type))
'''
The None value: sometimes when you write code you face with a situation that you want set a variable
to nothingness , not zero or not anything else. For example, if you collect information about a person
'''
# One option is to set it as empty string like
child = ""
print(child)
# Another way is to set that as None:
child = None
print(child)
''''
Pay attention to the way a None value is returned when you do not use the print() function in terminal. 
Other languages have the same concept called null.
'''
child

