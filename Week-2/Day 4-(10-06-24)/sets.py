
# What are Sets?
# Sets are a data structure in Python that store unordered collections of unique elements.
# They are mutable but do not allow duplicate elements.
# Syntax: my_set = {element1, element2, ...}

# Creating Sets
# Creating a set
my_set = {1, 2, 3, 4}
print("my_set:", my_set)  # Outputs: {1, 2, 3, 4}

# Creating an empty set
empty_set = set()
print("empty_set:", empty_set)  # Outputs: set()

# Creating a set with the set() function
another_set = set([1, 2, 3, 2])
print("another_set:", another_set)  # Outputs: {1, 2, 3} (duplicates are removed)

# Adding and Removing Elements
# Adding an element
my_set.add(5)
print("my_set after adding 5:", my_set)  # Outputs: {1, 2, 3, 4, 5}

# Removing an element
my_set.remove(3)
print("my_set after removing 3:", my_set)  # Outputs: {1, 2, 4, 5}

# Using discard() to remove an element that might not exist
my_set.discard(10)  # No error if 10 is not in the set
print("my_set after discarding 10:", my_set)  # Outputs: {1, 2, 4, 5}

# Set Operations
# Union: Combines elements from both sets.
# Intersection: Finds common elements between sets.
# Difference: Elements in one set but not in the other.
# Symmetric Difference: Elements in either set, but not in both.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)
print("Union:", union_set)  # Outputs: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)  # Outputs: {3}

# Difference
difference_set = set_a.difference(set_b)
print("Difference:", difference_set)  # Outputs: {1, 2}

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_set)  # Outputs: {1, 2, 4, 5}

# Set Methods
# set.add(element): Adds an element to the set.
# set.remove(element): Removes an element from the set (raises error if not found).
# set.discard(element): Removes an element if it exists, does nothing otherwise.
# set.pop(): Removes and returns an arbitrary element.
# set.clear(): Removes all elements from the set.

# Adding and removing elements
my_set.add(6)
print("After adding 6:", my_set)  # Outputs: {1, 2, 4, 5, 6}

my_set.remove(1)
print("After removing 1:", my_set)  # Outputs: {2, 4, 5, 6}

my_set.discard(10)  # Discards 10, no error
print("After discarding 10:", my_set)  # Outputs: {2, 4, 5, 6}

# Pop element
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop:", my_set)  # Outputs: {remaining elements}

# Clear set
my_set.clear()
print("After clear:", my_set)  # Outputs: set()

# Looping Through Sets
# Looping through set elements
for element in set_a:
    print("Element:", element)  # Outputs each element in set_a