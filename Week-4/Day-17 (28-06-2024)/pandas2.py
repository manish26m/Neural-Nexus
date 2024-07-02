import pandas as pd

# Load the data from a CSV file
data = pd.read_csv("D:\STUDY\Coding\Jupyter Notebook\DATA SCIENCE\EDA\LOAN DATA analysis\DATA SET\Loan 1.csv")

# Create a DataFrame from the loaded data
df = pd.DataFrame(data)

# Display the DataFrame
print("Full DataFrame:")
print(df)

# Create a dictionary with the provided data
data_dict = {
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

# Create a DataFrame from the dictionary
df_dict = pd.DataFrame(data_dict)

# Display the DataFrame created from the dictionary
print("\nDataFrame from Dictionary:")
print(df_dict)

# Define the columns to select from the CSV file
selected_columns = ["Customer ID", "Name", "Gender", "Income (USD)"]

# Read the CSV file and select specific columns
df_from_csv = pd.read_csv("D:\STUDY\Coding\Jupyter Notebook\DATA SCIENCE\EDA\LOAN DATA analysis\DATA SET\Loan 1.csv", usecols=selected_columns)

# Display the first few rows to confirm the selection
print("\nSelected Columns from CSV:")
print(df_from_csv.head())

# Data Inspection
print("\nDataFrame Info:")
df.info()

print("\nFirst 5 Rows of the DataFrame:")
print(df.head(5))

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values per Column:")
print(df.isnull().sum())

print("\nColumn Names:")
print(df.columns)

print("\nData Types of Each Column:")
print(df.dtypes)
