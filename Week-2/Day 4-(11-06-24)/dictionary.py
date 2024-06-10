# What are Dictionaries?
# Dictionaries are a data structure in Python that store key-value pairs.
# They are unordered, mutable, and indexed by keys.
# Syntax: my_dict = {"key1": "value1", "key2": "value2"}

# Creating Dictionaries
# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("my_dict:", my_dict)  # Outputs: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Creating an empty dictionary
empty_dict = {}
print("empty_dict:", empty_dict)  # Outputs: {}

# Using the dict() function
another_dict = dict(name="Bob", age=30, city="Los Angeles")
print("another_dict:", another_dict)  # Outputs: {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}

# Accessing and Modifying Elements
# Accessing elements by key
print("Name:", my_dict["name"])  # Outputs: Alice

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"
print("Updated my_dict:", my_dict)  # Outputs: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

# Modifying an existing value
my_dict["age"] = 26
print("Modified my_dict:", my_dict)  # Outputs: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Dictionary Methods
# dict.get(key): Returns the value for key if it exists, else returns None.
print("Age:", my_dict.get("age"))  # Outputs: 26
print("Country:", my_dict.get("country"))  # Outputs: None

# dict.keys(): Returns a view object containing all the keys.
print("Keys:", my_dict.keys())  # Outputs: dict_keys(['name', 'age', 'city', 'email'])

# dict.values(): Returns a view object containing all the values.
print("Values:", my_dict.values())  # Outputs: dict_values(['Alice', 26, 'New York', 'alice@example.com'])

# dict.items(): Returns a view object containing all the key-value pairs.
print("Items:", my_dict.items())  # Outputs: dict_items([('name', 'Alice'), ('age', 26), ('city', 'New York'), ('email', 'alice@example.com')])

# dict.pop(key): Removes the item with key and returns its value.
email = my_dict.pop("email")
print("Popped email:", email)  # Outputs: alice@example.com
print("Dictionary after pop:", my_dict)  # Outputs: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# dict.update(other_dict): Updates the dictionary with elements from another dictionary.
my_dict.update({"country": "USA", "phone": "123-456-7890"})
print("Updated my_dict:", my_dict)  # Outputs: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA', 'phone': '123-456-7890'}

# Looping Through Dictionaries
# Looping through keys
for key in my_dict:
    print("Key:", key)  # Outputs: name age city country phone

# Looping through values
for value in my_dict.values():
    print("Value:", value)  # Outputs: Alice 26 New York USA 123-456-7890

# Looping through key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Outputs: Key-value pairs