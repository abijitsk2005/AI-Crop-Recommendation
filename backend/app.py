# -*- coding: utf-8 -*-
"""
app.py

Main entry point for the Flask REST API. Provides endpoints for crop recommendation
prediction, history retrieval, database analytics, and contact query handling.
Configured with CORS and supports serving the frontend directly as a static folder.

Author: AgriAI Developer Team
Date: June 24, 2026
"""

import os
import sys
import numpy as np
import joblib
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Add parent directory to path so we can import utils
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from utils.db_manager import (
    init_db,
    save_prediction,
    get_history,
    get_analytics,
    save_contact_message,
    get_contact_messages
)
from utils.crop_details import get_crop_data

# Initialize Flask app, pointing to the parent directory for serving the frontend static files
app = Flask(__name__, static_folder="../", static_url_path="")
CORS(app)  # Enable CORS for all routes to support cross-origin API integration

# Load the trained ML model
MODEL_PATH = os.path.join(BASE_DIR, "model", "crop_model.pkl")
model = None
model_classes = None

def load_ml_model():
    """Helper function to load the trained model."""
    global model, model_classes
    if not os.path.exists(MODEL_PATH):
        print(f"[ERROR] Trained model not found at {MODEL_PATH}. Please run 'train_model.py' first.")
        return False
        
    try:
        model_data = joblib.load(MODEL_PATH)
        model = model_data['model']
        model_classes = np.array(model_data['classes'])
        print(f"[SUCCESS] Machine Learning model loaded successfully from {MODEL_PATH}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to load model file: {e}")
        return False

# Initialize database tables and load model on startup
init_db()
load_ml_model()

@app.route('/')
def serve_index():
    """Serves the frontend homepage index.html."""
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    POST /predict
    
    Accepts JSON containing soil and climate parameters:
    {
      "N": 90,
      "P": 42,
      "K": 43,
      "temperature": 20.8,
      "humidity": 82.0,
      "ph": 6.5,
      "rainfall": 202.9
    }
    
    Validates features and runs Random Forest prediction.
    Returns predicted crop, confidence percentage, and sustainable farming details.
    """
    if model is None:
        # Try loading on demand if it wasn't loaded at startup
        if not load_ml_model():
            return jsonify({
                "status": "error",
                "message": "Prediction engine model is currently unavailable on the server."
            }), 503

    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No JSON payload received"}), 400

        # Required fields in the request
        required_fields = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
        errors = {}
        
        # Parse and validate values
        parsed_inputs = {}
        for field in required_fields:
            if field not in data:
                errors[field] = f"Field '{field}' is missing."
                continue
                
            val = data[field]
            try:
                parsed_inputs[field] = float(val)
            except (ValueError, TypeError):
                errors[field] = f"Field '{field}' must be a numeric value."
        
        if errors:
            return jsonify({"status": "validation_error", "errors": errors}), 400

        # Extract features for prediction
        n = parsed_inputs["N"]
        p = parsed_inputs["P"]
        k = parsed_inputs["K"]
        temp = parsed_inputs["temperature"]
        humid = parsed_inputs["humidity"]
        ph = parsed_inputs["ph"]
        rain = parsed_inputs["rainfall"]

        # Run range validations based on practical agriculture limits
        range_errors = []
        if not (0 <= n <= 200):
            range_errors.append("Nitrogen (N) must be between 0 and 200 mg/kg.")
        if not (0 <= p <= 150):
            range_errors.append("Phosphorus (P) must be between 0 and 150 mg/kg.")
        if not (0 <= k <= 150):
            range_errors.append("Potassium (K) must be between 0 and 150 mg/kg.")
        if not (-10 <= temp <= 60):
            range_errors.append("Temperature must be between -10°C and 60°C.")
        if not (0 <= humid <= 100):
            range_errors.append("Humidity must be between 0% and 100%.")
        if not (0 <= ph <= 14):
            range_errors.append("pH balance must be between 0 and 14.")
        if not (0 <= rain <= 1000):
            range_errors.append("Rainfall must be between 0 and 1000 mm.")

        if range_errors:
            return jsonify({"status": "validation_error", "errors": range_errors}), 400

        # Format input for model as a pandas DataFrame to match features and avoid warnings
        import pandas as pd
        input_data = pd.DataFrame([[n, p, k, temp, humid, ph, rain]], 
                                  columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
        
        # Predict class label
        prediction_label = model.predict(input_data)[0]
        
        # Predict probabilities to calculate confidence
        probabilities = model.predict_proba(input_data)[0]
        class_idx = np.where(model_classes == prediction_label)[0][0]
        confidence_score = float(probabilities[class_idx])
        
        # Format crop title
        crop_title = prediction_label.title()
        if crop_title == "Kidneybeans":
            crop_title = "Kidney Beans"
        elif crop_title == "Pigeonpeas":
            crop_title = "Pigeon Peas"
        elif crop_title == "Mothbeans":
            crop_title = "Moth Beans"
        elif crop_title == "Mungbean":
            crop_title = "Mung Bean"

        # Fetch extra agronomy information and sustainable tips
        extra_details = get_crop_data(prediction_label)

        # Save record to SQLite database for prediction history and analytics
        save_prediction(
            n, p, k, temp, humid, ph, rain, 
            crop_title, confidence_score
        )

        # Build response payload
        response = {
            "status": "success",
            "crop": crop_title,
            "confidence": f"{confidence_score * 100:.0f}%",
            "details": {
                "name": extra_details["name"],
                "icon": extra_details["icon"],
                "scientific": extra_details["scientific"],
                "season": extra_details["season"],
                "duration": extra_details["duration"],
                "demand": extra_details["demand"],
                "price": extra_details["price"],
                "fertilizer": extra_details["fertilizer"],
                "tips": extra_details["tips"],
                "explanation": extra_details["explanation"],
                "sustainable_tips": extra_details["sustainable_tips"]
            }
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server occurred an error processing prediction: {str(e)}"
        }), 500

@app.route('/history', methods=['GET'])
def get_prediction_history():
    """
    GET /history
    
    Retrieves the 10 most recent soil predictions saved in SQLite database.
    """
    limit = request.args.get('limit', default=10, type=int)
    history = get_history(limit)
    return jsonify({
        "status": "success",
        "count": len(history),
        "history": history
    }), 200

@app.route('/analytics', methods=['GET'])
def get_dashboard_analytics():
    """
    GET /analytics
    
    Retrieves crop counts ratios and total counts logged by the platform.
    Used to populate the administrator metrics dashboard.
    """
    stats = get_analytics()
    return jsonify({
        "status": "success",
        "analytics": stats
    }), 200

@app.route('/contact', methods=['POST'])
def submit_contact_query():
    """
    POST /contact
    
    Accepts contact message form:
    {
      "name": "John Doe",
      "email": "john@email.com",
      "subject": "Soil advice",
      "message": "Query body..."
    }
    
    Saves in SQLite database.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No JSON payload received"}), 400
            
        required = ["name", "email", "subject", "message"]
        errors = [f for f in required if f not in data or not str(data[f]).strip()]
        
        if errors:
            return jsonify({"status": "validation_error", "message": f"Fields missing: {errors}"}), 400
            
        name = data["name"].strip()
        email = data["email"].strip()
        subject = data["subject"].strip()
        msg_body = data["message"].strip()
        
        saved = save_contact_message(name, email, subject, msg_body)
        if saved:
            return jsonify({
                "status": "success",
                "message": "Message successfully recorded by agronomist desk."
            }), 201
        else:
            return jsonify({
                "status": "error",
                "message": "Internal error writing query message to disk."
            }), 500
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/messages', methods=['GET'])
def get_recent_messages():
    """
    GET /messages
    
    Retrieves inbound query messages for the Admin Message Center logs.
    """
    limit = request.args.get('limit', default=20, type=int)
    messages = get_contact_messages(limit)
    return jsonify({
        "status": "success",
        "count": len(messages),
        "messages": messages
    }), 200

if __name__ == "__main__":
    print("="*60)
    print("AgriAI Flask REST API Backend running on port 5000")
    print("Direct browser access: http://127.0.0.1:5000/")
    print("="*60)
    app.run(host="127.0.0.1", port=5000, debug=True)
