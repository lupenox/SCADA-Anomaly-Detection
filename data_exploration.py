import pandas as pd

# Load the dataset
file_path = "data/gas_pipeline_dataset.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Basic Info:")
print(df.info())
print("\n")

# Display the first few rows
print("First 5 Rows:")
print(df.head())
print("\n")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())
print("\n")

# Display basic statistics
print("Basic Statistics:")
print(df.describe())
