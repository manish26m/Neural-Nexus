
# Pandas Installation
# Run this in your terminal or Jupyter notebook to install pandas
# pip install pandas
# For Python 3: pip3 install pandas

# Virtual Environment Installation (run these commands in terminal)
# Create a new virtual environment (e.g., named 'myenv')
# python -m venv myenv

# Activate the virtual environment
# Windows: myenv\Scripts\activate
# macOS/Linux: source myenv/bin/activate

# Install Pandas
# pip install pandas

# Install Pandas within a Jupyter notebook
# !pip install pandas

# Verifying Installation
import pandas as pd  # If there's no error, Pandas is installed
print("Pandas is installed.")

# Check the Pandas version
print("Pandas version:", pd.__version__)

# Creating a Pandas Series

# From Lists
data = [10, 20, 30, 40]
s = pd.Series(data, index=["a", "b", "c", "d"])
print("Series from list:")
print(s)

# From Arrays
import numpy as np
array_data = np.array([1.1, 2.2, 3.3, 4.4])
s_from_array = pd.Series(array_data, index=["x", "y", "z", "w"])
print("Series from array:")
print(s_from_array)

# From Dictionaries
dict_data = {"Apple": 100, "Banana": 200, "Cherry": 300}
s_from_dict = pd.Series(dict_data)
print("Series from dictionary:")
print(s_from_dict)

# Exploring Series Attributes and Methods

# Common Attributes
print("Index:", s.index)
print("Values:", s.values)
print("Data type:", s.dtype)
print("Size:", s.size)

# Common Methods
print("First two elements:", s.head(2))
print("Last two elements:", s.tail(2))
print("Sorted values:", s.sort_values())
print("Mean of the Series:", s.mean())
