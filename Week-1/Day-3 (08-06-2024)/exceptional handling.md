### Exception Handling in Python: Key Points and Examples

**1. What is an Exception?**
- **Definition:** An object representing an error or unusual condition disrupting normal flow.
- **Example:** `ZeroDivisionError` for division by zero.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

**2. Importance of Exception Handling**
- **Prevents Program Crashes:** Allows the program to handle errors gracefully.
- **Debugging Aid:** Provides valuable information for fixing issues.

**3. Basic Syntax**
- **Try-Except Block:**

```python
try:
    # code that might raise an exception
except ExceptionType:
    # code to handle the exception
```

**4. Handling Multiple Exceptions**
- **Multiple Except Blocks:**

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid value!")
```

- **Single Except Block for Multiple Types:**

```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print("Error:", e)
```

**5. Using Else and Finally Blocks**
- **Else Block:** Runs if no exceptions are raised.
- **Finally Block:** Runs regardless of exceptions, useful for cleanup.

```python
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Cleanup operations")
```

**6. Common Built-in Exceptions**
- **SyntaxError:** Incorrect syntax.
- **IndentationError:** Incorrect indentation.
- **NameError:** Undefined variable.
- **TypeError:** Operation on incompatible types.
- **ValueError:** Correct type but inappropriate value.
- **ZeroDivisionError:** Division by zero.

**7. Custom Exceptions**
- **Definition and Usage:**

```python
class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Value cannot be negative")

try:
    check_value(-5)
except CustomError as e:
    print("Custom error occurred:", e)
```

**8. Avoiding Broad Except Clauses**
- **Be Specific:** Catch only expected exceptions.
- **Avoid Bare `except:`**

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input!")
```

**9. Raising Exceptions**
- **Syntax:** `raise ExceptionClass("Error message")`

```python
def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print("Error:", e)
```

**10. Exception Handling at Different Levels**
- **Local Level:** Within specific functions.
- **Intermediate Level:** Across multiple functions or modules.
- **Global Level:** At the main entry point of the application.

**11. Documenting Exceptions**
- **Docstrings:** Include descriptions of exceptions raised.

```python
def divide(x, y):
    """
    Divide two numbers.
    Args:
        x (int): The dividend.
        y (int): The divisor.
    Raises:
        ValueError: If `y` is zero.
    Returns:
        float: The result of the division.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

### Example Questions and Solutions

1. **Function that divides two numbers and raises `ZeroDivisionError`:**

```python
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2

try:
    print(divide_numbers(10, 2))
    print(divide_numbers(5, 0))
except ZeroDivisionError as e:
    print("Error:", e)
```

2. **Palindrome Check with Custom Exception:**

```python
class PalindromeError(Exception):
    pass

def is_palindrome(input_str):
    if not isinstance(input_str, str):
        raise PalindromeError("Input must be a string")
    clean_str = input_str.replace(" ", "").lower()
    return clean_str == clean_str[::-1]

try:
    print(is_palindrome("racecar"))
    print(is_palindrome(123))
except PalindromeError as e:
    print(e)
```

3. **Iterate through list and handle `ZeroDivisionError`:**

```python
numbers = [10, 0, 5, 20, 3]

for num in numbers:
    try:
        result = num / 0
    except ZeroDivisionError:
        print(f"Error: Cannot divide {num} by zero")
    finally:
        print("Iteration completed")
```

4. **Convert string to integer with `ValueError` handling:**

```python
try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    print("Integer value:", num)
except ValueError as e:
    print("Error:", e)
```

5. **Square root of a number with custom exception:**

```python
import math

class NegativeNumberError(Exception):
    pass

def sqrt(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return math.sqrt(num)

try:
    print(sqrt(25))
    print(sqrt(-4))
except NegativeNumberError as e:
    print(e)
```

These notes and examples cover the key aspects of exception handling in Python, providing a comprehensive overview of how to manage errors effectively.
