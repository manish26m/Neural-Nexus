# Python Lists - Code Notes

# Creating a list
my_list = [1, "hello", 3.14, [1, 2, 3]]

# Ordered and Indexable
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: hello

# Mutable
my_list[1] = "world"
print(my_list)  # Output: [1, 'world', 3.14, [1, 2, 3]]

# Heterogeneous
heterogeneous_list = [10, "Python", 23.5, [5, 6]]

# Dynamic
my_list.append(42)
print(my_list)  # Output: [1, 'world', 3.14, [1, 2, 3], 42]

# Iterable
for item in my_list:
    print(item)

# List Methods
# Append
my_list.append("new")
print(my_list)  # Output: [1, 'world', 3.14, [1, 2, 3], 42, 'new']

# Insert
my_list.insert(1, "inserted")
print(my_list)  # Output: [1, 'inserted', 'world', 3.14, [1, 2, 3], 42, 'new']

# Remove
my_list.remove("world")
print(my_list)  # Output: [1, 'inserted', 3.14, [1, 2, 3], 42, 'new']

# Copy (Shallow and Deep Copy)
import copy
shallow_copy = my_list.copy()
deep_copy = copy.deepcopy(my_list)

# Count
count = my_list.count(42)
print(count)  # Output: 1

# Extend
my_list.extend([99, 100])
print(my_list)  # Output: [1, 'inserted', 3.14, [1, 2, 3], 42, 'new', 99, 100]

# Index
index = my_list.index(3.14)
print(index)  # Output: 2

# Sort
numbers = [5, 3, 6, 2, 10]
numbers.sort()
print(numbers)  # Output: [2, 3, 5, 6, 10]

# Reverse
numbers.reverse()
print(numbers)  # Output: [10, 6, 5, 3, 2]

# Clear
numbers.clear()
print(numbers)  # Output: []

# Pop
popped_item = my_list.pop()
print(popped_item)  # Output: 100
print(my_list)  # Output: [1, 'inserted', 3.14, [1, 2, 3], 42, 'new', 99]







#List comprehension:-
## Sum of n natural number

summ=lambda x : sum(x)
result=summ([x for x in range(10)])
print(result)


# Simple Indexing Example

# Define a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Accessing elements using positive indexing
print("First element:", my_list[0])   # Output: apple
print("Second element:", my_list[1])  # Output: banana

# Modifying an element
my_list[1] = 'blueberry'
print("Modified list:", my_list)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']


# Slicing in Python Lists - Code Notes

# Define a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Positive Slicing
subset_pos = my_list[1:4]  # Select elements from index 1 up to (but not including) index 4
print("Positive Slicing:", subset_pos)  # Output: ['banana', 'cherry', 'date']

# Negative Slicing
subset_neg = my_list[-3:-1]  # Select elements from the third last up to (but not including) the last element
print("Negative Slicing:", subset_neg)  # Output: ['cherry', 'date']

# Retrieve: Extracting a portion of the list
subset_retrieve = my_list[2:5]  # Extract elements from index 2 up to (but not including) index 5
print("Retrieve:", subset_retrieve)  # Output: ['cherry', 'date', 'elderberry']

# Update: Modifying elements within a slice of the list
my_list[1:3] = ['blueberry', 'coconut']  # Replace elements from index 1 up to (but not including) index 3
print("Update:", my_list)  # Output: ['apple', 'blueberry', 'coconut', 'date', 'elderberry']

# Delete: Removing elements from a slice of the list
del my_list[2:4]  # Remove elements from index 2 up to (but not including) index 4
print("Delete:", my_list)  # Output: ['apple', 'blueberry', 'elderberry']

# Insert: Adding elements into a specific position within the list
my_list[2:2] = ['orange', 'pear']  # Insert elements before index 2
print("Insert:", my_list)  # Output: ['apple', 'blueberry', 'orange', 'pear', 'elderberry']


# Slicing and Operations

f = ["apple", "banana", "cherry", "date", "elderberry"]

s1 = f[1:4]
print("1 to 4:", s1)

s2 = f[1:6:2]
print("1 to 6, step 2:", s2)

s3 = f[-3:]
print("Last 3:", s3)

s4 = f[-2:-5:-1]
print("Last 2 in reverse:", s4)

mid = f[2:5]
print("Middle:", mid)

f[1:3] = ["blueberry", "cranberry"]
print("Updated:", f)

del f[2:4]
print("Deleted:", f)

f[1:1] = ["kiwi", "mango"]
print("Inserted:", f)

# Searching and Sorting

f = ["apple", "banana", "cherry", "date", "elderberry"]

found = "date" in f
print("Found 'date':", found)

where = f.index("banana")
print("Position of 'banana':", where)

for i in f:
    if i == "date":
        print("Found 'date' iteratively")
        break

f.sort()
print("Sorted:", f)

f.sort(reverse=True)
print("Reverse sorted:", f)

# Special Methods

from functools import reduce

n = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, n)
print("Total sum:", total)

cubes = list(map(lambda x: x ** 3, n))
print("Cubes:", cubes)

evens = list(filter(lambda x: x % 2 == 0, n))
print("Even numbers:", evens)

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
pairs = list(zip(names, scores))
print("Name-Score pairs:", pairs)


# Question 1: List Operations
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1. Add a new fruit "fig" to the end of the list
fruits.append("fig")
print("1. Added 'fig':", fruits)

# 2. Insert "grape" at the 2nd position (index 1)
fruits.insert(1, "grape")
print("2. Inserted 'grape':", fruits)

# 3. Remove the first occurrence of "banana"
fruits.remove("banana")
print("3. Removed 'banana':", fruits)

# 4. Return the first and last element of the list
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("4. First and last fruits:", first_fruit, last_fruit)


# Question 2: Indexing and Slicing
# Get the third fruit from the list
third_fruit = fruits[2]
print("5. Third fruit:", third_fruit)

# Retrieve a slice containing the first three fruits
first_three_fruits = fruits[:3]
print("6. First three fruits:", first_three_fruits)

# Retrieve a slice containing the last two fruits using negative indexing
last_two_fruits = fruits[-2:]
print("7. Last two fruits:", last_two_fruits)

# Update the second fruit to "blueberry"
fruits[1] = "blueberry"
print("8. Updated second fruit:", fruits)


# Question 3: List Methods and Functions
numbers = [1, 2, 3, 4, 5]

# Append the number 6 to the list of numbers
numbers.append(6)
print("9. Appended 6:", numbers)

# Insert the number 0 at the beginning of the list
numbers.insert(0, 0)
print("10. Inserted 0 at beginning:", numbers)

# Remove and return the last element from the list
last_element = numbers.pop()
print("11. Removed and returned last element:", last_element, "Remaining list:", numbers)

# Return the count of occurrences of the number 2
count_2 = numbers.count(2)
print("12. Count of '2':", count_2)

# Return the index of the number 3
index_3 = numbers.index(3)
print("13. Index of '3':", index_3)

# Reverse the order of the list
numbers.reverse()
print("14. Reversed list:", numbers)


# Question 4: List Comprehensions
# Create a list of even numbers from 0 to 20
even_numbers = [x for x in range(21) if x % 2 == 0]
print("15. Even numbers:", even_numbers)

# Create a list of squares of numbers from 1 to 10
squares = [x ** 2 for x in range(1, 11)]
print("16. Squares from 1 to 10:", squares)

# Create a list of uppercase words from a list of words
words = ["hello", "world", "python", "lists"]
uppercased = [word.upper() for word in words]
print("17. Uppercased words:", uppercased)

# Create a flattened list from a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print("18. Flattened list from nested list:", flattened)


# Question 5: Searching and Sorting
# Check if "cherry" is in the list of fruits
has_cherry = "cherry" in fruits
print("19. Is 'cherry' in the list?", has_cherry)

# Find the index of "date" in the list
date_index = fruits.index("date")
print("20. Index of 'date':", date_index)

# Sort the list of fruits in ascending order
fruits.sort()
print("21. Sorted fruits:", fruits)

# Sort the list of fruits in descending order
fruits.sort(reverse=True)
print("22. Reverse sorted fruits:", fruits)


# Question 6: Special Methods
from functools import reduce

# Calculate the sum of the list of numbers using reduce
total_sum = reduce(lambda x, y: x + y, numbers)
print("23. Total sum using reduce:", total_sum)

# Create a list of cubes of numbers using map
cubes = list(map(lambda x: x ** 3, numbers))
print("24. Cubes using map:", cubes)

# Filter out the odd numbers from a list
even_only = list(filter(lambda x: x % 2 == 0, numbers))
print("25. Even numbers using filter:", even_only)

# Zip two lists to create pairs of names and scores
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
name_score_pairs = list(zip(names, scores))
print("26. Name-Score pairs:", name_score_pairs)
