# matplotlib_examples.py

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Use a specific style sheet
plt.style.use('ggplot')

# --- Pie Charts ---
# Basic Pie Chart
dept = ["HR", "SALES", "TECHNICAL", "SERVICE"]
cnt = [23, 17, 34, 21]

plt.pie(cnt, labels=dept, autopct="%1.2f%%")
plt.title("Basic Pie Chart")
plt.show()

# Pie Chart with Additional Features
labels = ['ML', 'DS', 'AI', 'POWERBI']
sizes = [40, 70, 50, 40]
colors = ['lightblue', 'red', 'green', 'yellow']
explode = [0, 0, 0.3, 0]

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.2f%%', shadow=True, startangle=90)
plt.title("Pie Chart with Additional Features")
plt.show()

# Pie Chart with Styling
slices = [32324, 45346, 34534, 45346, 34535]
labels = ["Java", "Python", "C", "C++", "SQL"]
explode = [0, 0.1, 0, 0, 0]

plt.pie(slices, labels=labels, shadow=True, startangle=90, explode=explode, autopct="%1.1f%%",
        wedgeprops={'edgecolor': 'black', 'linewidth': 2}, colors=colors)
plt.title("Pie Chart with Styling")
plt.show()

# --- Line Charts ---
# Basic Line Plot
x = [1, 2, 3, 4, 5, 6]
y = [4, 5, 6, 3, 2, 3]

plt.plot(x, y, color="green")
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Line Plot with NumPy
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x**2

plt.plot(x, y)
plt.title("Line Plot with NumPy")
plt.show()

# Multiple Line Plots in a Single Plot
x1 = [2, 4, 6, 8, 10]
y1 = [1, 2, 3, 4, 5]

plt.plot(x, y, linestyle='-.', marker='*', label="Line 1")
plt.plot(x1, y1, color="red", marker="o", label="Line 2")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Line Plots")
plt.legend()
plt.show()

# --- Subplots ---
plt.subplot(2, 2, 1)
plt.plot(x, y, 'y')
plt.title("Subplot 1")

plt.subplot(2, 2, 2)
plt.plot(x1, y1, color="red", marker="o")
plt.title("Subplot 2")

plt.subplot(2, 2, 3)
plt.plot(x, y, 'g')
plt.title("Subplot 3")

plt.tight_layout()
plt.show()

# --- Customizing Line Charts ---
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, label='All Developers')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, label='Python Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

# Changing Line Styles
plt.plot(ages_x, dev_y, color='k', linestyle='--', label='All Developers')
plt.plot(ages_x, py_dev_y, color='r', label='Python Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

# Adding Markers and Grids
plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='x', ms=7, lw=2, label='All Developers')
plt.plot(ages_x, py_dev_y, color='r', marker='o', ms=4, lw=1, label='Python Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.grid(True)
plt.show()

# Adding More Data
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, dev_y, color='k', linewidth=3, marker='x', label='All Developers')
plt.plot(ages_x, py_dev_y, color='r', linewidth=3, marker='o', label='Python Developers')
plt.plot(ages_x, js_dev_y, color='b', linewidth=3, marker='X', label='JavaScript Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.grid(True)
plt.show()

# --- Bar Charts ---
# Basic Bar Chart
langs = ["C++", "Python", "C", "Java"]
students = [23, 14, 54, 23]

plt.bar(langs, students, color="red")
plt.title("Language vs Number of Students")
plt.show()

# Adding More Details to a Bar Chart
plt.bar(ages_x, dev_y, color='r', label='All Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

# Combining Line and Bar Charts
plt.bar(ages_x, dev_y, color='r', label='All Developers')

plt.plot(ages_x, py_dev_y, color='g', linewidth=3, marker='o', label='Python Developers')
plt.plot(ages_x, js_dev_y, color='b', linewidth=3, marker='X', label='JavaScript Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

# Handling Overlapping Bars using NumPy
width = 0.25
x_indexes = np.arange(len(ages_x))

plt.bar(x_indexes - width, dev_y, width=width, color='r', label='All Developers')
plt.bar(x_indexes, py_dev_y, width=width, color='g', label='Python Developers')
plt.bar(x_indexes + width, js_dev_y, width=width, color='b', label='JavaScript Developers')

plt.title('Median Salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()
