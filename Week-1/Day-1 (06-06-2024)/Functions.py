# 1. Functions in Python

# Functions are a fundamental concept in programming languages and play a crucial role in organizing and reusing code.
# They allow developers to break down complex tasks into smaller, more manageable pieces, making the code easier to understand, maintain, and debug.
# Functions also enable code reusability, as they can be called multiple times from different parts of a program, promoting modularity and efficiency.
# Additionally, functions facilitate collaboration among developers by allowing them to work on different parts of a program independently, and they contribute to the overall efficiency and performance of a program.

# 2. Syntax of a Function
# Now let's understand the syntax of functions;

# 2.1. def keyword: This keyword signals the start of a function definition.
# 2.2. Function Name: Use lowercase, with underscores for separation.
# 2.3. Parentheses (): These enclose any parameters (arguments) the function might accept. If the function doesn't take any arguments, you'll still have empty parentheses.
# 2.4. Colon: This follows the parentheses and indicates the start of the function body.
# 2.5. Indented Block: The indented block (usually 4 spaces or a tab), contains the statements that define the function's behavior. This block can include calculations, variable assignments, conditional statements.
# 2.6. Optional return Statement: This statement (if present), specifies the value the function will return when called. If no return statement is present, the function implicitly returns None.

def greet(name):  # Function definition with parameter 'name'
    """This function prints a greeting message."""
    print("Hello", name + "!")

# Function call with argument 'J'
greet("J")
# Output: Hello J!

# 3. Parameters in Functions
# Parameters, also known as arguments, are the inputs a function receives when it's called. They provide a way to customize the function's behavior for different scenarios. Here's a breakdown of different types of parameters in Python:

# 3.1. Positional Arguments:
# These are arguments passed to the function in the same order they are defined in the function declaration. The function expects a specific number of arguments based on the order.

def calculate_area(length, width):
    """This function calculates the area of a rectangle."""
    return length * width

# Calling the function with positional arguments
area = calculate_area(5, 3)  # length = 5, width = 3
print(area)  # Output: 15

# 3.2. Keyword Arguments:
# These arguments are passed by name when calling the function. The order doesn't matter as long as you associate the value with the correct parameter name.

def greet(name, message="Hello"):
    """This function greets someone with an optional message."""
    print(message, name + "!")

# Calling with keyword arguments (notice order is switched)
greet(message="Hi", name="J")  # Output: Hi J!

# 3.3. Default Arguments:
# These arguments have pre-defined values assigned within the function definition. If no value is passed during the function call, the default value is used.

def greet(name="World"):
    """This function greets someone by name."""
    print("Hello", name + "!")

# Calling with default argument
greet()  # Output: Hello World!

# Calling with a custom argument
greet("J")  # Output: Hello J!

# 3.4. Variable Length Arguments (*args):
# This allows a function to accept an arbitrary number of positional arguments. These arguments are packed into a tuple inside the function.

def calculate_average(*numbers):
    """This function calculates the average of any number of arguments."""
    if len(numbers) == 0:
        print("Please provide at least one number.")
        return
    return sum(numbers) / len(numbers)

# Calling with variable arguments
average = calculate_average(10, 20, 30)
print(average)  # Output: 20.0

# Calling without arguments
calculate_average()  # Output: Please provide at least one number.

# 3.5. Keyword Variable Length Arguments (**kwargs):
# Similar to variable length arguments, but these arguments are captured in a dictionary. You can pass any number of keyword arguments, and they are accessible as key-value pairs within the function.

def full_name(first, last, *, middle=""):
    """This function combines first, middle, and last name."""
    return first + " " + middle + " " + last

# Calling with keyword arguments (notice 'middle' is named)
print(full_name(first="Vanshika", last="Singh", middle="J."))  # Output: Vanshika J. Singh

# You can also use positional arguments for the first two parameters
print(full_name("Shubhdeep", "Sidhu", middle="Singh"))  # Output: Shubhdeep Singh Sidhu

# 3.6. Keyword-Only Arguments:
# Introduced in Python 3.5, these arguments must be preceded by * in the function definition. They can only be passed by keyword name, not by position.

def divide(dividend, *, divisor=1):
    """This function divides two numbers with an optional divisor (default 1)."""
    return dividend / divisor

# Calling with keyword argument (notice 'divisor' comes after *)
print(divide(dividend=10, divisor=2))  # Output: 5.0

# This would cause an error because 'divisor' is not a positional argument
# print(divide(10, 2)) 

# 4. Passing Function as Arguments
# In Python, functions are first-class objects, meaning you can treat them like any other data type. This allows you to pass functions as arguments to other functions. This powerful concept is often referred to as higher-order functions. Here's how it works:

# 4.1. Higher-Order Functions:
# A higher-order function is a function that:
# - Takes one or more functions as arguments.
# - May or may not return a function itself.
# These functions provide more flexibility in how you approach problems and can make your code more concise and readable.

# 4.2. Passing Functions as Arguments (Example):
# Consider you have two functions:
# - shout(text): Converts the input text to uppercase and returns it.
# - whisper(text): Converts the input text to lowercase and returns it.
# Now, you can create a higher-order function modify_text that takes another function and a text as arguments. This allows you to decide how you want to modify the text (shout or whisper) at runtime:

def shout(text):
    """This function converts text to uppercase."""
    return text.upper()

def whisper(text):
    """This function converts text to lowercase."""
    return text.lower()

def modify_text(text, func):
    """This function applies a provided function (func) to the text."""
    return func(text)

# Calling modify_text with different functions
yelled_text = modify_text("Hello world!", shout)
print(yelled_text)  # Output: HELLO WORLD!

whispered_text = modify_text("HELLO WORLD!", whisper)
print(whispered_text)  # Output: hello world!

# 5. Lambda Function
# In Python, lambda functions offer a concise way to define anonymous functions. These functions are useful for short, single-expression operations, often used within other functions or as arguments themselves.

# 5.1. Anonymous Functions:
# Lambda functions lack a formal name, hence the term "anonymous."
# They are defined using the lambda keyword followed by arguments, a colon, and the expression to be evaluated.

# 5.2. Lambda Function Syntax
# lambda arguments : expression

# arguments: This is a comma-separated list of arguments the lambda function can accept. It can be empty if the function doesn't take any arguments.
# expression: This is the code that the lambda function will execute. The expression must be evaluated to a single value.

# 5.3. Examples

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# Using lambda with sort() for custom sorting
names = ["John", "Emma", "Kelly", "Jason"]
names.sort(key=lambda name: len(name))
print(names)  # Output: ['John', 'Emma', 'Kelly', 'Jason']

# Using lambda with filter() to filter out even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
