# Introduction to Tuples
# Tuples are ordered and immutable collections of items.

# Creating Tuples
# A tuple can be created by placing items inside parentheses, separated by commas.
my_tuple = (1, 2, 3)
print("my_tuple:", my_tuple)  # Outputs: (1, 2, 3)

# Creating a tuple without parentheses
my_tuple_no_parens = 1, 2, 3
print("my_tuple_no_parens:", my_tuple_no_parens)  # Outputs: (1, 2, 3)

# Creating a tuple with a single element (comma is required)
single_element_tuple = (5,)
print("single_element_tuple:", single_element_tuple)  # Outputs: (5,)
print("Type of single_element_tuple:", type(single_element_tuple))  # Outputs: <class 'tuple'>

# Accessing Tuple Elements
# Elements in a tuple can be accessed using indexing
print("First element:", my_tuple[0])  # Outputs: 1

# Unpacking Tuples
# Tuples can be unpacked into variables
a, b, c = my_tuple
print("Unpacked values:", a, b, c)  # Outputs: 1 2 3

# Tuple Methods
# Count and Index Methods
example_tuple = (1, 2, 3, 1, 2, 1)
print("Count of 1:", example_tuple.count(1))  # Outputs: 3
print("Index of first 2:", example_tuple.index(2))  # Outputs: 1

# Nested Tuples
# Tuples can contain other tuples
nested_tuple = (1, (2, 3), (4, 5))
print("Nested tuple element:", nested_tuple[1])  # Outputs: (2, 3)

# Immutability of Tuples
# Tuples are immutable, so their elements cannot be changed
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)  # Outputs: 'tuple' object does not support item assignment

# Iterating Over a Tuple
# You can iterate over the elements of a tuple using a for loop
for item in my_tuple:
    print("Item:", item)  # Outputs: 1 2 3

# Why Use Tuples?
# Tuples are useful when you want to ensure the data cannot be modified.
# They can be used as keys in dictionaries because they are immutable.

# Example: Using tuples in a dictionary
coordinates = {(0, 0): "origin", (1, 2): "point 1"}
print("Dictionary with tuple keys:", coordinates)  # Outputs: {(0, 0): 'origin', (1, 2): 'point 1'}