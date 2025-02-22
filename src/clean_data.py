import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(input_path, output_path):
    print("Loading dataset...")
    df = pd.read_csv(input_path)
    
    print("Handling outliers in 'measurement' column...")
    if 'measurement' in df.columns:
        df = df[df['measurement'].between(df['measurement'].quantile(0.01), df['measurement'].quantile(0.99))]
    
    print("Converting 'result' column to integers...")
    if 'result' in df.columns:
        df['result'] = df['result'].apply(lambda x: int(str(x).strip("b'")))
    
    print("Scaling numeric features...")
    numeric_columns = df.select_dtypes(include=['float64']).columns
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    
    print(f"Saving cleaned data to {output_path}...")
    df.to_csv(output_path, index=False)
    print("Cleaning complete!")

input_file = "data/10_water_final.csv"
output_file = "data/10_water_final_cleaned.csv"

clean_data(input_file, output_file)
