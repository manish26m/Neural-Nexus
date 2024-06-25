# Introduction to NumPy

# NumPy (Numerical Python) is a fundamental library for numerical operations in Python.
# It provides efficient support for large, multi-dimensional arrays and matrices,
# along with a collection of high-level mathematical functions to operate on these arrays.

# Benefits of Using NumPy
# - Compact and Fast: NumPy arrays are more compact in memory and faster in execution compared to standard Python lists.
# - Mathematical Functions: It provides a wide range of mathematical functions and operations optimized for scientific computing.
# - Integration: It integrates well with other scientific libraries like SciPy and Matplotlib, making it a cornerstone of the scientific Python ecosystem.

# Importing NumPy
import numpy as np

# Verifying Installation
# To verify that NumPy is installed correctly, you can run the following command:
print(np.__version__)

# NumPy Arrays
# NumPy's main object is the homogeneous multidimensional array. These arrays are a grid of values,
# all of the same type, indexed by a tuple of non-negative integers.

# Creating Arrays
# From a list
array_from_list = np.array([1, 2, 3])

# From a tuple
array_from_tuple = np.array((1, 2, 3))

# From a list of lists
array_from_list_of_lists = np.array([[1, 2, 3], [4, 5, 6]])

# Using functions like arange, zeros, ones, linspace, etc.
array_arange = np.arange(0, 10, 2)
array_zeros = np.zeros((3, 4))
array_ones = np.ones((2, 3))
array_linspace = np.linspace(0, 1, 5)

# Array Attributes
array = np.array([1, 2, 3, 4, 5])
print(f"Shape: {array.shape}")
print(f"Data type: {array.dtype}")
print(f"Size: {array.size}")
print(f"Number of dimensions: {array.ndim}")

# Array Operations and Broadcasting
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
result_add = a + b

# Element-wise multiplication
result_multiply = a * b

# Broadcasting example
a_broadcast = np.array([[1], [2], [3]])
b_broadcast = np.array([4, 5, 6])
result_broadcast = a_broadcast + b_broadcast

# Indexing and Slicing
array_indexing_slicing = np.array([1, 2, 3, 4, 5, 6])

# Indexing
element = array_indexing_slicing[0]

# Slicing
sub_array = array_indexing_slicing[1:5]

# Array Manipulation
array_manipulation = np.array([[1, 2], [3, 4]])

# Reshape
reshaped = array_manipulation.reshape((4,))

# Flatten
flattened = array_manipulation.flatten()

# Transpose
transposed = array_manipulation.T

# Stacking and Splitting Arrays
a_stack_split = np.array([[1, 2], [3, 4]])
b_stack_split = np.array([[5, 6], [7, 8]])

# Stacking
stacked_v = np.vstack((a_stack_split, b_stack_split))
stacked_h = np.hstack((a_stack_split, b_stack_split))

# Splitting
split = np.split(a_stack_split, 2)

# Adding and Removing Elements
array_add_remove = np.array([1, 2, 3, 4, 5])

# Adding elements
new_array_add = np.append(array_add_remove, [6, 7])

# Removing elements
new_array_remove = np.delete(array_add_remove, [0, 1])
