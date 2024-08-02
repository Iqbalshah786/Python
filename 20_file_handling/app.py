import os

# r = read
# a = append 
# w = write
# x = create

# Read - error if file does not exist
# f = open("names.txt","r") # default is read if not specified
# print(f.read())
# print(f.read(4)) # read first 4 characters of the file
# print(f.readline()) # read first line of the file
# print(f.readline()) # reads second line of the file


# for line in f:
#     print(line)
# f.close() # every time you open a file, you should close it

# trying to read a file that does not exist
# try:
#     f = open("name_list.txt")
#     print(f.read())
# except:
#     print("The file you want to read does not exits")
# finally:
#     f.close()

# Append - creates a file if it does not exist
# f = open("names.txt","a")
# f.write("Sharif")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# Write overwrites the file
# f = open("context.txt","w")
# f.write("I deleted all of the context") # overwrites the file
# f.close()

# f = open("context.txt")
# print(f.read())
# f.close()



# Two ways to create a new file

# Opens a file fo writing. Creates a new file if it does not exist.

# f = open("new_file.txt","w")
# f.close()

# creates the specified file but returns an error if the file already exists

# if not os.path.exists("ibs.txt"):
#     f = open("ibs.txt","x")
#     f.close()

# delete a file
# avoid an if error if it doesnot exits

# if os.path.exists("ibs.txt"):
#     os.remove("ibs.txt")
# else:
#     print("The file does not exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)
