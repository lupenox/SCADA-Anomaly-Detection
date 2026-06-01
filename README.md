# SCADA Anomaly Detection

A Python machine learning project for detecting anomalous or potentially malicious activity in SCADA/industrial control system data.

This project focuses on taking SCADA-related datasets, converting them into a usable CSV format, cleaning/preprocessing the data, training classification models, and generating prediction/evaluation outputs.

## What this project does

The project currently includes scripts and notebook work for:

- Converting ARFF datasets into CSV format
- Exploring raw SCADA/ICS datasets with pandas
- Cleaning data before model training
- Converting the `result` label column into machine-readable values
- Training anomaly detection / attack classification models
- Saving trained models with `joblib`
- Running predictions on new data
- Producing evaluation output such as classification reports and confusion matrices

The main goal is to classify SCADA activity as normal or anomalous/attack-related using supervised machine learning.

## Project focus

SCADA systems are used in industrial environments such as utilities, pipelines, water systems, and other critical infrastructure. Because these systems can be targeted by cyberattacks, anomaly detection can help identify suspicious behavior in sensor readings, commands, or network-style event data.

This repository is an educational cybersecurity and machine learning project, not a production-ready industrial monitoring system.

## Current project files

Based on the current project structure/history, the project includes work such as:

| File | Purpose |
|---|---|
| `convert_arff_to_csv.py` | Converts ARFF datasets into CSV files for easier processing with pandas. |
| `explore_data.py` | Loads a dataset and prints basic information, first rows, statistics, and missing-value counts. |
| `clean_data.py` | Cleans/preprocesses the dataset, including label conversion and numeric scaling. |
| `train_svm.py` | Trains an SVM classifier, evaluates it, saves the model, and generates a confusion matrix. |
| `predict_new_data.py` | Loads a saved model and predicts labels for new data. |
| Jupyter notebook files | Experimental notebook workflow for loading data, preprocessing, training, and evaluating models. |

## Machine learning approach

The project experiments with supervised classification models, including:

- Support Vector Machine / SVM
- Logistic Regression in notebook experiments

The workflow generally looks like this:

```text
Raw ARFF/CSV dataset
        ↓
Convert or load dataset
        ↓
Explore and inspect data
        ↓
Clean/preprocess labels and features
        ↓
Train ML model
        ↓
Evaluate predictions
        ↓
Save model and output results
```

## Expected folders

The scripts expect a structure similar to this:

```text
SCADA-Anomaly-Detection/
├── data/
│   ├── 10_water_final.arff
│   ├── 10_water_final.csv
│   ├── 10_water_final_cleaned.csv
│   └── new_data.csv
├── models/
│   └── svm_model_water.pkl
├── outputs/
│   ├── confusion_matrix.png
│   └── new_data_predictions.csv
├── convert_arff_to_csv.py
├── explore_data.py
├── clean_data.py
├── train_svm.py
└── predict_new_data.py
```

Some datasets, generated models, or output files may not be included in the repository depending on file size, privacy, or local experiment setup.

## Requirements

This project uses Python and common data science / machine learning libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib liac-arff
```

Depending on the ARFF parser used, you may also need:

```bash
pip install scipy
```

## How to run

### 1. Convert an ARFF dataset to CSV

```bash
python convert_arff_to_csv.py
```

### 2. Explore the dataset

```bash
python explore_data.py
```

### 3. Clean/preprocess the data

```bash
python clean_data.py
```

### 4. Train the SVM model

```bash
python train_svm.py
```

This should train the classifier, print evaluation metrics, save the trained model, and generate a confusion matrix image.

### 5. Predict on new data

```bash
python predict_new_data.py
```

This loads a saved model, runs predictions on a new CSV file, and writes the predicted labels to the `outputs/` folder.

## Output

The project can generate:

- Trained model files such as `.pkl` files
- Classification reports printed in the terminal
- Confusion matrix visualizations
- CSV prediction outputs for new data

## Status

This project is currently a work-in-progress / educational prototype. It demonstrates the basic workflow for SCADA anomaly detection using machine learning, but it still needs improvements before being considered complete.

Planned or useful future improvements:

- Add a `requirements.txt`
- Make file paths configurable with command-line arguments
- Add better error handling for missing datasets/folders
- Add multiple model comparisons
- Add clearer dataset documentation
- Add saved evaluation metrics
- Improve preprocessing consistency between training and prediction
- Add reproducible notebooks and example outputs

## Portfolio relevance

This project demonstrates skills in:

- Cybersecurity concepts for industrial control systems
- Python scripting
- Data cleaning and preprocessing
- Machine learning with scikit-learn
- Model evaluation
- Working with real-world dataset formats such as ARFF and CSV
- Building a practical security-focused ML pipeline

## Disclaimer

This project is for learning, research, and portfolio purposes. It should not be used as-is to monitor or secure real industrial systems without significant validation, testing, and production hardening.
