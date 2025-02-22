import pandas as pd

def explore_data(file_path):
    print(f"Loading dataset from {file_path}...")
    df = pd.read_csv(file_path)
    
    print("\nBasic Information:")
    print(df.info())
    
    print("\nFirst 5 Rows:")
    print(df.head())
    
    print("\nSummary Statistics:")
    print(df.describe())
    
    print("\nMissing Values:")
    print(df.isnull().sum())

file_path = "data/Event_Export_082217.csv"
explore_data(file_path)

