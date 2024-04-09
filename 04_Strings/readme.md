# String Operators
The **+** operator concatenates strings:
```python
s = "spam"
t = "egg"

print(s+t) # spamegg
```
The * operator creates multiple copies of a string:
```python
n = 2 
print(s*n) # spamspam
```
The **in** and **not in** operators provide boolean testing of membership within a string:

```python
print(s in "I saw spamalot!") # true
```

# String Indexing
Strings are **ordered sequences of character data**. Indexing allows you to access individual characters in a string directly by using a numeric value. String indexing is **zero-based:** the first character in the string has index 0, the next is 1, and so on.

```python
s = "mybook"
print(s[0]) # m
print(s[1]) # y
print(s[len(s)-1]) # k
```
#### negative string indexing:
```python
print(s[-1]) # k
print(s[-3]) # o
```

# String Slicing
To **extract substrings from a string.** This technique is known as string **slicing.**

#### negative index slicing:
```python
s = "mybook"
print(s[-5:-1]) # yboo
print(s[-4:-1]) # boo
```
## slice with a stride:
#### sequence[start:stop:stride]:
- **start** is the starting index of the slice (inclusive).
- **stop** is the ending index of the slice (exclusive).
- **stride** is the step size or the distance between each element to include in the slice.
```python
y = "12345" * 5
print(y) # 1234512345123451234512345
print(y[::5]) # 11111
print(y[4::5]) # 55555
print(y[::-5]) # 55555
```
#### Reverse a String using Slicing:
```python
y = y[::-1]
print(y) # 5432154321543215432154321
```



# String escape characters:
The escape character is used when we want to use a character in a string that has special meaning in
Python like **“**

- The idea is we want to ignore their regular meaning and just take them as they are
(escape them). In order to escape a character you use **\\** before the character you want to escape.

## Example:
```python
print ("He said \" YES \" while he was crying")
```
Now, imagine the escape character itself has a meaning for Python, right? I mean \ character means escape. Then how would like print something like a mountain? : **/\\/\\/\\**

**The answer is you do that by escaping the \\.**

```python
print("/\\/\\/\\")
```

A backslash can be added at the end of a line to ignore the newline:
```python
print('This string will not include \
backslashes or newline characters.')
```

# Escape sequences

| Escape Sequence | Meaning                        | Example                     |
|-----------------|--------------------------------|-----------------------------|
| \<newline>      | Backslash and newline ignored  | N/A (explained in notes)   |
| \\              | Backslash (\)                  | `'\\'` -> \\               |
| \'              | Single quote (')               | `'\'\''` -> \''            |
| \"              | Double quote (")               | `"\""` -> "\""             |
| \a              | ASCII Bell (BEL)               | `print('\a')` -> (May produce visual feedback) |
| \b              | ASCII Backspace (BS)           | `print('hello\b')` -> hell |
| \f              | ASCII Formfeed (FF)            | `print('hello\fworld')` -> hello↵    world|
| \n              | ASCII Linefeed (LF)            | `print('hello\nworld')` -> hello↵<br>world|
| \r              | ASCII Carriage Return (CR)     | `print('hello\rworld')` -> world |
| \t              | ASCII Horizontal Tab (TAB)     | `print('hello\tworld')` -> hello   world |
| \v              | ASCII Vertical Tab (VT)        | `print('hello\vworld')` -> hello↵<br>world |
| \ooo            | Character with octal value ooo | `print('\141')` -> a       |
| \xhh            | Character with hex value hh    | `print('\x41')` -> A       |

# String Concatenation
That means adding two strings together. You use the + sign to concatenate.

- **Be mindful that all the items must have the string (str) data types. If they are not all strings, you can use
the str() function to change to string data types before concatenation.**

```python
first = "My name is: "
second = "John"
print(first + second)
```

# String Interpolation: 
This is sometimes called **“string formatting”** and for that reason, the string that has those interpolates
(inserts) is an **F-String.**
- With f strings, you do not have to worry about data types.

```python
age = 10
print(f"My age is {age}")
```

# Changing Case in String with Methods
One of the simplest tasks you can do with strings is change the case of the words in a string. Look at the following code, and try to determine what’s happening:
```python
name = iqbal shah
print(name.title()) # Iqbal Shah
name = Iqbal Shah
print(name.upper())
print(name.lower())
```
