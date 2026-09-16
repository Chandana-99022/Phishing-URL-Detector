import os
import sys

import pandas as pd
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

# Get project root folder
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Add project root to Python path
sys.path.insert(0, PROJECT_ROOT)

from model.feature_extraction import extract_features


# Load trained model
MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "model",
    "phishing_model.pkl"
)

model_package = joblib.load(MODEL_PATH)

model = model_package["model"]
feature_names = model_package["features"]


# Create Flask app
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Phishing URL Detector API is running!"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({
            "error": "Please provide a URL"
        }), 400

    url = str(data["url"]).strip()

    if not url:
        return jsonify({
            "error": "URL cannot be empty"
        }), 400

    # Extract URL features
    features = extract_features(url)

    # Keep features in the same order as training
    X = pd.DataFrame(
        [[features[name] for name in feature_names]],
        columns=feature_names
    )

    # Prediction
    prediction = model.predict(X)[0]

    # Confidence
    probabilities = model.predict_proba(X)[0]
    confidence = max(probabilities) * 100

    if prediction == 1:
        result = "PHISHING"
    else:
        result = "LEGITIMATE"

    return jsonify({
        "url": url,
        "prediction": result,
        "confidence": round(confidence, 2)
    })


if __name__ == "__main__":
    print("====================================")
    print("   PHISHING URL DETECTOR BACKEND")
    print("====================================")
    print("Server running at: http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )