from scipy.io import arff
import pandas as pd

# Path to your ARFF file
arff_file_path = "data/gas_pipeline_dataset.arff"

# Load the ARFF file
data = arff.loadarff(arff_file_path)

# Convert to a Pandas DataFrame
df = pd.DataFrame(data[0])

# Save the DataFrame as a CSV file
csv_file_path = "data/gas_pipeline_dataset.csv"
df.to_csv(csv_file_path, index=False)

print(f"Dataset converted and saved to {csv_file_path}")

