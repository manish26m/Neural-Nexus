import pandas as pd

# Load data from CSV file
data = pd.read_csv("D:/STUDY/Coding/Jupyter Notebook/DATA SCIENCE/EDA/LOAN DATA analysis/DATA SET/Loan 1.csv")

# Display the DataFrame
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a dictionary
data1 = {
    "Customer ID": ["C-26247", "C-35067", "C-34590", "C-16668", "C-12196", "C-2600", "C-9047", "C-2206", "C-25607", "C-11606"],
    "Name": ["Tandra Olszewski", "Jeannette Cha", "Keva Godfrey", "Elva Sackett", "Sade Constable", "Gina Weir", "Lacey Cybulski", "Karrie Dickison", 
             "Tona Wigington", "Hellen Alexis"],
    "Gender": ["F", "F", "F", "M", "F", "F", "M", "M", "M", "F"],
    "Age": [47, 57, 52, 65, 60, 59, 43, 65, 64, 27],
    "Income (USD)": [3472.69, 1184.84, 1266.27, 1369.72, 1939.23, 2944.81, 1957.31, 1403.63, 1604.65, 949.17],
    "Income Stability": ["Low", "Low", "Low", "High", "High", "Low", "Low", "High", "Low", "Working"],
    "Profession": ["Commercial associate", "Working", "Working", "Pensioner", "Pensioner", "Working", "Working", "Pensioner", "Working", "Working"],
    "Type of Employment": ["Managers", "Sales staff", "", "", "", "Sales staff", "Sales staff", "", "", "Laborers"],
    "Location": ["Semi-Urban", "Rural", "Semi-Urban", "Rural", "Urban", "Semi-Urban", "Rural", "Semi-Urban", "Semi-Urban", "Rural"],
    "Loan Amount Request (USD)": [137088.98, 104771.59, 176684.91, 97009.18, 109980, 31465.78, 150334.11, 121029.27, 39475.31, 24703.89]
}
data2 = pd.DataFrame(data1)
print(data2)

# Creating a DataFrame from a CSV file and selecting specific columns
selected_columns = ["Customer ID", "Name", "Gender", "Income (USD)"]
df_from_csv = pd.read_csv("D:/STUDY/Coding/Jupyter Notebook/DATA SCIENCE/EDA/LOAN DATA analysis/DATA SET/Loan 1.csv", usecols=selected_columns)
print(df_from_csv.head())

# Data inspection
print("DataFrame Info:")
print(df.info())

print("First 5 Rows:")
print(df.head(5))

print("Summary Statistics:")
print(df.describe())

print("Missing Values Per Column:")
print(df.isnull().sum())

print("Column Names:")
print(df.columns)

print("Data Types of Each Column:")
print(df.dtypes)
