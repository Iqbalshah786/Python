# Hash Tables in Python

## Introduction

A hash table (or hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. In Python, the built-in `dict` type provides the functionality of a hash table.

## Key Concepts

- **Key-Value Pair**: Hash tables store data in key-value pairs. Each key is unique and is used to retrieve the associated value.
- **Hash Function**: A hash function takes an input (or key) and returns a fixed-size string of bytes. The output is typically a 'hash code' which is used as an index to place the key-value pair into the hash table.
- **Collision Handling**: Two different keys can produce the same hash code (collision). Python handles collisions using separate chaining with linked lists.

## Operations

### 1. Insertion
Adding a key-value pair to the hash table.

```python
my_dict = {}
my_dict['key'] = 'value'
```

### 2. Lookup
Retrieving a value by its key.

```python
value = my_dict['key']
```

###  3. Deletion
Removing a key-value pair from the hash table.

```python
del my_dict['key']
```
### 4. Update
Modifying the value associated with a key.

```python
my_dict['key'] = 'new_value'
```


## Advantages of Hash Tables

* **Fast Lookup:** On average, hash tables have O(1) time complexity for lookups.

* **Efficient:** They are efficient for large datasets. 

## Disadvantages of Hash Tables
* **Collisions:** Collisions can affect performance and need to be managed.

* **Memory Usage:** Hash tables can consume more memory compared to other data structures like lists.


# Implementing Hash Tables in Python

## Creating a Hash Table

```python
my_dict = {}  # An empty dictionary
```
## Inserting Elements
```python
my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['location'] = 'New York'
```
## Accessing Elements
```python
name = my_dict['name']  # Returns 'John'
```
## Deleting Elements
```python
del my_dict['age']
```


# Dictionary Methods

### Python dictionaries come with many useful methods:

* **dict.get(key, default):** Returns the value for key if key is in the dictionary, else default.

* **dict.keys():** Returns a new view of the dictionary’s keys.

* **dict.values():** Returns a new view of the dictionary’s values.

* **dict.items():** Returns a new view of the dictionary’s items (key, value).

* **dict.update([other]):** Updates the dictionary with the key/value pairs from other, overwriting existing keys.

* **dict.pop(key, default):** Removes the specified key and returns the corresponding value. If the key is not found, default is returned if provided, otherwise KeyError is raised.

* **dict.clear():** Removes all items from the dictionary.

# Performance Considerations

## Time Complexity:
* **Average:** O(1) for insertions, deletions, and lookups.

* **Worst-case:** O(n) in case of many collisions.
 

## Space Complexity:

* Requires additional memory for the hash table structure and handling collisions.


