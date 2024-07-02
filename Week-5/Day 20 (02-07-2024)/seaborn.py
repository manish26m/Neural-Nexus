# Install seaborn if not already installed
# %pip install seaborn

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets from seaborn
flights_data = sns.load_dataset("flights")
penguins_data = sns.load_dataset("penguins")
tips_data = sns.load_dataset("tips")

# Display the first 10 rows of the flights dataset
print(flights_data.head(10))

# LINEPLOT
# Creating a simple line plot using a DataFrame
line_data = {'Time': [1, 2, 3, 4, 5], 'Value': [3, 5, 2, 4, 6]}
df = pd.DataFrame(line_data)
sns.lineplot(x='Time', y='Value', data=df)
plt.show()

# Line plot using lists
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sns.lineplot(x=x, y=y)
plt.show()

# Line plot using the flights dataset
sns.lineplot(x="year", y="passengers", data=flights_data)
plt.show()

# Styled line plot with hue and style
sns.lineplot(x="year", y="passengers", data=flights_data, hue="month", style="month", markers=True, dashes=False)
plt.show()

# Customized line plot with matplotlib features
plt.figure(figsize=(10, 6))
sns.lineplot(x="year", y="passengers", data=flights_data, hue="month", style="month", markers=True, dashes=False)
plt.title("Monthly Passenger")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.show()

# HISTOGRAM
# Simple histogram of penguins' flipper length
sns.histplot(data=penguins_data, x="flipper_length_mm", bins=[170, 175, 180, 185, 190, 195], color="green")
plt.show()

# Histogram with KDE (Kernel Density Estimate)
sns.histplot(data=penguins_data, x="flipper_length_mm", bins=30, binwidth=3, kde=True)
plt.show()

# Histogram with multiple hues
sns.histplot(data=penguins_data, x="flipper_length_mm", hue="species", multiple="stack")
plt.show()

# Histogram using different elements
sns.histplot(penguins_data, x="flipper_length_mm", hue="species", element="step")
plt.show()

# Histogram with different statistics
sns.histplot(data=tips_data, x="size", stat="percent")
plt.show()

# Histogram with dodge
sns.histplot(data=tips_data, x="day", hue="sex", multiple="dodge", shrink=.8)
plt.show()

# BARPLOT
# Simple bar plot
sns.barplot(x="island", y="body_mass_g", data=penguins_data)
plt.show()

# Bar plot with hue
sns.barplot(x="island", y="body_mass_g", data=penguins_data, hue="sex")
plt.show()

# Pivot flights dataset for bar plot
flights_wide = flights_data.pivot(index="year", columns="month", values="passengers")
sns.barplot(data=flights_wide)
plt.show()

sns.barplot(y=flights_wide["Jun"], x=flights_wide.index)
plt.show()

# HEATMAP
# Heatmap of correlation in tips dataset
corr_matrix = tips_data.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, linewidth=2, cmap="crest")
plt.show()

# SCATTERPLOT
# Simple scatter plot
sns.scatterplot(data=tips_data, x="total_bill", y="tip")
plt.show()

# Scatter plot with formatting
sns.scatterplot(data=tips_data, x="total_bill", y="tip", hue="time", style="time", size="size", palette="deep", alpha=0.8)
plt.show()

# KDEPLOT
# Simple KDE plot
sns.kdeplot(x="total_bill", data=tips_data)
plt.show()

# KDE plot with hue
sns.kdeplot(x="total_bill", data=tips_data, hue="sex")
plt.show()

# KDE plot with fill and additional formatting
sns.kdeplot(data=tips_data, x="total_bill", hue="time", fill=True, palette="flare", alpha=0.5, cut=0)
plt.title("Density Plot of Total Bill by Time of Day")
plt.show()

# RUGPLOT
# Rug plot with KDE
sns.kdeplot(data=tips_data, x="tip")
sns.rugplot(data=tips_data, x="tip")
plt.show()

# Rug plot with scatter plot
sns.scatterplot(data=tips_data, x="total_bill", y="tip")
sns.rugplot(data=tips_data, x="total_bill", y="tip", height=0.07, alpha=1)
plt.show()

# BOXPLOT
# Simple box plot
sns.boxplot(x="day", y="total_bill", data=tips_data)
plt.show()

# Box plot with hue and customizations
sns.boxplot(x="day", y="total_bill", data=tips_data, hue="time", showmeans=True, meanprops={"marker":"*", "markeredgecolor":"b"}, order=["Fri", "Sat"], palette="plasma")
plt.show()

# VIOLIN PLOT
# Simple violin plot
sns.violinplot(x="day", y="total_bill", data=tips_data)
plt.show()

# Violin plot with order and hue
sns.violinplot(x="time", y="total_bill", data=tips_data, order=["Dinner", "Lunch"], split=True, hue="time")
plt.show()

# PAIRPLOT
# Pairplot of the tips dataset
sns.pairplot(tips_data)
plt.show()

# Pairplot with hue and specific variables
sns.pairplot(tips_data, hue="sex", x_vars=["total_bill", "tip"], y_vars=["total_bill", "tip"])
plt.show()
