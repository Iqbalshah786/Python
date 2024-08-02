**Python File Handling**
=======================
Python provides several ways to interact with files, including reading, writing, and manipulating file contents. In this guide, we will cover the basics of file handling in Python.

**Reading from a File**
----------------------
To read from a file in Python, you can use the `open()` function, which returns a file object. This file object has several methods and attributes that allow you to read and manipulate the file contents.
### Example: Reading from a File
```python
# Open the file in read mode
file = open('example.txt', 'r')
# Read the contents of the file
contents = file.read()
# Print the contents
print(contents)
# Close the file
file.close()
```
**Writing to a File**
---------------------
To write to a file in Python, you can use the `open()` function with the `'w'` mode. This will create a new file if it does not exist, or overwrite the existing file if it does.
### Example: Writing to a File
```python
# Open the file in write mode
file = open('example.txt', 'w')
# Write to the file
file.write('Hello, World!')
# Close the file
file.close()
```
**Modes for Opening Files**
---------------------------
The `open()` function takes two arguments: the file name and the mode. The mode specifies how the file should be opened. Here are some common modes:
* `'r'`: Open the file for reading (default)
* `'w'`: Open the file for writing, truncating the file if it already exists
* `'a'`: Open the file for appending, adding new content to the end of the file
* `'x'`: Open the file for exclusive creation, failing if the file already exists
* `'b'`: Open the file in binary mode
* `'t'`: Open the file in text mode (default)
### Example: Appending to a File
```python
# Open the file in append mode
file = open('example.txt', 'a')
# Append to the file
file.write('This is appended content.')
# Close the file
file.close()
```
**File Object Methods**
------------------------
* `readline()`: Read a single line from the file
* `readlines()`: Read all lines from the file and return them as a list
* `seek()`: Move the file pointer to a specific position in the file
* `tell()`: Return the current position of the file pointer
* `truncate()`: Truncate the file to a specific length
### Example: Reading a File Line by Line
```python
# Open the file in read mode
file = open('example.txt', 'r')
# Read the file line by line
for line in file:
print(line.strip())
# Close the file
file.close()
```
**File Object Attributes**
---------------------------
File objects have several attributes that provide information about the file. Here are some common attributes:
* `name`: The name of the file
* `mode`: The mode in which the file was opened
* `closed`: A boolean indicating whether the file is closed
* `encoding`: The encoding of the file (if it was opened in text mode)
### Example: Checking if a File is Closed
```python
# Open the file in read mode
file = open('example.txt', 'r')
# Check if the file is closed
print(file.closed) # Output: False
# Close the file
file.close()
# Check if the file is closed
print(file.closed) # Output: True
```
**Exceptions**
--------------
When working with files, several exceptions can occur. Here are some common exceptions:
* `FileNotFoundError`: Raised when a file is not found
* `PermissionError`: Raised when you do not have permission to access a file
* `IOError`: Raised when an I/O error occurs (e.g. when reading or writing to a file)
### Example: Catching a FileNotFoundError
```python
try:
# Open the file in read mode
file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
print("The file was not found.")
```

**Best Practices**
------------------
### Example: Using the with Statement
```python
# Open the file in read mode using the with statement
with open('example.txt', 'r') as file:
# Read the contents of the file
contents = file.read()
# The file is automatically closed when we exit the with block
```
**Working with Binary Files**
---------------------------
When working with binary files, you need to open the file in binary mode (`'b'`) and use the `read()` and `write()` methods to read and write binary data.
### Example: Reading and Writing a Binary File
```python
# Open the file in binary read mode
with open('example.bin', 'rb') as file:
# Read the binary data from the file
data = file.read()
# Open the file in binary write mode
with open('example.bin', 'wb') as file:
# Write binary data to the file
file.write(b'Hello, World!')
```
**Working with CSV and JSON Files**
---------------------------------
Python has built-in modules for working with CSV and JSON files.
### Example: Reading and Writing a CSV File
```python
import csv
# Open the file in read mode
with open('example.csv', 'r') as file:
# Create a CSV reader
reader = csv.reader(file)
# Read the CSV data
for row in reader:
print(row)
# Open the file in write mode
with open('example.csv', 'w') as file:
# Create a CSV writer
writer = csv.writer(file)
# Write CSV data to the file
writer.writerow(['Name', 'Age'])
writer.writerow(['John', 30])
```
### Example: Reading and Writing a JSON File
```python
import json
# Open the file in read mode
with open('example.json', 'r') as file:
# Read the JSON data from the file
data = json.load(file)
# Open the file in write mode
with open('example.json', 'w') as file:
# Write JSON data to the file
json.dump({'name': 'John', 'age': 30}, file)
```
**Conclusion**
----------
In this guide, we covered the basics of file handling in Python. We learned how to open and close files, read and write file contents, and work with different file modes and formats. We also learned about best practices for working