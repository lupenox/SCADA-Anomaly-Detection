import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def train_svm(data_path, model_path):
    print("Loading cleaned dataset...")
    df = pd.read_csv(data_path)

    print("Splitting dataset...")
    X = df.drop(columns=['result'])
    y = df['result']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    print("Training SVM model...")
    model = SVC(kernel='linear', decision_function_shape='ovr', random_state=42)
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)
    print("Classification Report:\n", classification_report(y_test, y_pred))

    print("Saving model...")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    print("Generating confusion matrix...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')

    output_path = "outputs/confusion_matrix.png"
    plt.savefig(output_path)
    print(f"Confusion matrix saved to {output_path}")

data_path = "data/10_water_final_cleaned.csv"
model_path = "models/svm_model_water.pkl"

train_svm(data_path, model_path)
