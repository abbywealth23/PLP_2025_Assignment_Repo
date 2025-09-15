#  Task
# Step 1: Import necessary libraries
import pandas as pd
from sklearn.datasets import load_iris

# Step 2: Load the Iris dataset
iris = load_iris()

# Step 3: Convert to a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Step 4: Display the first few rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Step 5: Explore the structure
print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Missing Values in Each Column:")
print(df.isnull().sum())

# Step 6: Clean the dataset (drop or fill missing values)
# In this case, no missing values — but here's how you'd handle them:
df_cleaned = df.dropna()  # or df.fillna(method='ffill') if you prefer filling

print("\n✅ Dataset cleaned (if needed). Preview:")
print(df_cleaned.head())


# Task 2
