import pandas as pd
import arff

def convert_arff_to_csv(input_path, output_path):
    print(f"Converting {input_path} to {output_path}...")
    
    with open(input_path, 'r') as file:
        arff_data = arff.load(file) 
        df = pd.DataFrame(arff_data['data'], columns=[attr[0] for attr in arff_data['attributes']])
    
    df.to_csv(output_path, index=False)
    print("Conversion complete!")

input_file = "data/10_water_final.arff"
output_file = "data/10_water_final.csv"
convert_arff_to_csv(input_file, output_file)
