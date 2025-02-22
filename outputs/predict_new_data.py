import pandas as pd
import joblib

def predict_new_data(model_path, data_path, output_path):
    print("Loading model...")
    model = joblib.load(model_path)
    
    print("Loading new dataset...")
    df = pd.read_csv(data_path)
    X = df.drop(columns=['result'], errors='ignore') 

    print("Making predictions...")
    predictions = model.predict(X)

    print(f"Saving predictions to {output_path}...")
    output = pd.DataFrame({'Predicted': predictions})
    output.to_csv(output_path, index=False)
    print("Predictions saved!")

model_path = "models/svm_model.pkl"
data_path = "data/new_data.csv"
output_path = "outputs/new_data_predictions.csv"
predict_new_data(model_path, data_path, output_path)
