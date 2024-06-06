
# Python Input and Output

# Input statement
name = input("What's your name? ")
print("Nice to meet you,", name)

# Output statement with keyword arguments
print("Hello", "World", sep=", ", end="!")

# Data Types in Python
int_num = 10
float_num = 3.14
complex_num = 2 + 3j
string = "Hello, World!"
boolean = True
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
dict_example = {"name": "Alice", "age": 30}
set_example = {1, 2, 3, 4, 5}
frozenset_example = frozenset([1, 2, 3, 4, 5])

# Expressions and Operators
a = 10
b = 3

# Arithmetic Operators
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3 (floor division)
print(a % b)  # 1 (remainder)
print(a ** b) # 1000 (power)

# Comparison Operators
print(a == b) # False
print(a != b) # True
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False

# Logical Operators
print(a > 5 and b < 5)  # True
print(a > 5 or b < 1)   # True
print(not(a > 5 and b < 5)) # False

# Type Casting
int_from_float = int(3.14)  # 3
float_from_int = float(10)  # 10.0
string_from_int = str(100)  # "100"
list_from_string = list("Hello")  # ['H', 'e', 'l', 'l', 'o']
tuple_from_list = tuple([1, 2, 3, 4, 5])  # (1, 2, 3, 4, 5)
set_from_list = set([1, 2, 3, 4, 5])  # {1, 2, 3, 4, 5}

print(int_from_float)
print(float_from_int)
print(string_from_int)
print(list_from_string)
print(tuple_from_list)
print(set_from_list)

# Conditional Statements
a = 10
b = 5

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

# Looping Statements
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Jumping Statements
# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

# Special Functions
fruits = ["apple", "banana", "cherry"]

# len()
print(len(fruits))  # Output: 3

# id()
print(id(fruits))  # Output: Unique ID of the list object

# type()
print(type(fruits))  # Output: <class 'list'>

# range()
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

