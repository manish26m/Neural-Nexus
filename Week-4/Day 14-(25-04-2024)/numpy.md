
# Introduction to NumPy

NumPy (Numerical Python) is a fundamental library for numerical operations in Python. It provides efficient support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays.

## Benefits of Using NumPy

- **Compact and Fast**: NumPy arrays are more compact in memory and faster in execution compared to standard Python lists.
- **Mathematical Functions**: It provides a wide range of mathematical functions and operations optimized for scientific computing.
- **Integration**: It integrates well with other scientific libraries like SciPy and Matplotlib, making it a cornerstone of the scientific Python ecosystem.

## Installing NumPy

To install NumPy, you can use pip:

```sh
pip install numpy
```

Or if you're using conda:

```sh
conda install numpy
```

## Verifying Installation

To verify that NumPy is installed correctly, you can run the following commands in a Python environment:

```python
import numpy as np
print(np.__version__)
```

## NumPy Arrays

NumPy's main object is the homogeneous multidimensional array. These arrays are a grid of values, all of the same type, indexed by a tuple of non-negative integers.

### Attributes

Here are some attributes of NumPy arrays:

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(f"Shape: {array.shape}")
print(f"Data type: {array.dtype}")
print(f"Size: {array.size}")
print(f"Number of dimensions: {array.ndim}")
```

### Creating Arrays

NumPy offers several functions to create arrays:

```python
# From a list
array = np.array([1, 2, 3])

# From a tuple
array = np.array((1, 2, 3))

# From a list of lists
array = np.array([[1, 2, 3], [4, 5, 6]])

# Using functions like arange, zeros, ones, linspace, etc.
array = np.arange(0, 10, 2)
array = np.zeros((3, 4))
array = np.ones((2, 3))
array = np.linspace(0, 1, 5)
```

## Array Operations and Broadcasting

NumPy supports element-wise operations and broadcasting, which allows for efficient computation:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
result = a + b

# Element-wise multiplication
result = a * b

# Broadcasting example
a = np.array([[1], [2], [3]])
b = np.array([4, 5, 6])
result = a + b
```

## Indexing and Slicing

You can index and slice NumPy arrays in a manner similar to Python lists:

```python
array = np.array([1, 2, 3, 4, 5, 6])

# Indexing
element = array[0]

# Slicing
sub_array = array[1:5]
```

## Array Manipulation

NumPy provides several functions to manipulate arrays:

```python
array = np.array([[1, 2], [3, 4]])

# Reshape
reshaped = array.reshape((4,))

# Flatten
flattened = array.flatten()

# Transpose
transposed = array.T
```

## Stacking and Splitting Arrays

You can stack and split arrays using the following functions:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stacking
stacked = np.vstack((a, b))
stacked = np.hstack((a, b))

# Splitting
split = np.split(a, 2)
```

## Adding and Removing Elements

You can add or remove elements from arrays:

```python
array = np.array([1, 2, 3, 4, 5])

# Adding elements
new_array = np.append(array, [6, 7])

# Removing elements
new_array = np.delete(array, [0, 1])
```
