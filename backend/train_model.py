# -*- coding: utf-8 -*-
"""
train_model.py

This script downloads the Crop Recommendation Dataset containing N, P, K and environmental features,
preprocesses the data, trains a Random Forest Classifier model, evaluates its accuracy,
and saves the trained model as a serialized pickle file for the Flask backend to use.

Author: AgriAI Developer Team
Date: June 24, 2026
"""

import os
import urllib.request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODEL_DIR = os.path.join(BASE_DIR, "model")
DATASET_PATH = os.path.join(DATASET_DIR, "crop_recommendation.csv")
MODEL_PATH = os.path.join(MODEL_DIR, "crop_model.pkl")

# Harvestify Raw URL of the Kaggle Crop Recommendation dataset on GitHub (contains N, P, K)
DATASET_URL = "https://raw.githubusercontent.com/Gladiator07/Harvestify/master/Data-processed/crop_recommendation.csv"

def download_dataset():
    """Downloads the crop recommendation dataset from a reliable public GitHub URL if it doesn't exist or is invalid."""
    if not os.path.exists(DATASET_DIR):
        os.makedirs(DATASET_DIR, exist_ok=True)
        print(f"[INFO] Created dataset directory: {DATASET_DIR}")
        
    need_download = False
    if not os.path.exists(DATASET_PATH):
        need_download = True
    else:
        # Check if the existing file is valid and contains N, P, K
        try:
            temp_df = pd.read_csv(DATASET_PATH, nrows=5)
            if 'N' not in temp_df.columns:
                print("[WARNING] Existing CSV does not contain N, P, K features. Deleting and re-downloading...")
                os.remove(DATASET_PATH)
                need_download = True
        except Exception:
            os.remove(DATASET_PATH)
            need_download = True

    if need_download:
        print(f"[INFO] Downloading dataset from {DATASET_URL}...")
        try:
            req = urllib.request.Request(
                DATASET_URL, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req) as response, open(DATASET_PATH, 'wb') as out_file:
                out_file.write(response.read())
            print(f"[SUCCESS] Dataset successfully saved to {DATASET_PATH}")
        except Exception as e:
            print(f"[ERROR] Failed to download dataset: {e}")
            raise e
    else:
        print(f"[INFO] Valid dataset already exists at {DATASET_PATH}")

def train_and_evaluate():
    """Loads the dataset, trains a Random Forest model, prints evaluation metrics, and saves the model."""
    print("[INFO] Loading dataset...")
    df = pd.read_csv(DATASET_PATH)
    
    # Verify dataset features
    required_features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label']
    for feature in required_features:
        if feature not in df.columns:
            raise ValueError(f"Missing required column '{feature}' in the dataset. Column list: {list(df.columns)}")
            
    print(f"[INFO] Dataset loaded successfully. Shape: {df.shape}")
    print("[INFO] Crop classes count:", len(df['label'].unique()))
    print("[INFO] Crop classes in dataset:", sorted(df['label'].unique()))
    
    # Split into features (X) and target label (y)
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    
    # Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("[INFO] Training Random Forest Classifier model...")
    # Initialize Random Forest model with sensible defaults for precision agriculture
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"[SUCCESS] Model training complete! Test Set Accuracy: {accuracy * 100:.2f}%")
    
    # Detailed classification report
    print("\n[INFO] Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the trained model
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR, exist_ok=True)
        print(f"[INFO] Created model directory: {MODEL_DIR}")
        
    print(f"[INFO] Saving trained model to {MODEL_PATH}...")
    model_data = {
        'model': model,
        'features': list(X.columns),
        'classes': list(model.classes_)
    }
    joblib.dump(model_data, MODEL_PATH)
    print(f"[SUCCESS] Model successfully saved to {MODEL_PATH}")

if __name__ == "__main__":
    print("="*60)
    print("AgriAI - Machine Learning Sowing Recommendation Model Trainer")
    print("="*60)
    download_dataset()
    train_and_evaluate()
    print("="*60)
