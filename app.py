from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
import logging
from logging.handlers import RotatingFileHandler
import os

# -------------------------------
# Setup Logging
# -------------------------------
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "app.log")
log_format = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"

handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
logging.basicConfig(handlers=[handler], level=logging.INFO, format=log_format)

logger = logging.getLogger(__name__)

# -------------------------------
# Load Model Assets
# -------------------------------
try:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    label_encoders = joblib.load("label_encoders.pkl")
    feature_names = joblib.load("feature_names.pkl")
    logger.info("Model and assets loaded successfully.")
except Exception as e:
    logger.exception("Failed to load model or assets.")
    raise e

categorical_features = ['mainroad', 'guestroom', 'basement', 'hotwaterheating',
                        'airconditioning', 'prefarea', 'furnishingstatus']

# -------------------------------
# Flask App Initialization
# -------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        logger.info(f"Received input: {data}")

        for key in data:
            if key not in categorical_features:
                data[key] = float(data[key])

        input_df = pd.DataFrame([data])

        for col in categorical_features:
            encoder = label_encoders.get(col)
            input_df[col] = encoder.transform([input_df[col][0]])

        input_df = input_df[feature_names]
        input_scaled = scaler.transform(input_df)
        input_scaled_df = pd.DataFrame(input_scaled, columns=feature_names)

        prediction = model.predict(input_scaled_df)[0]
        formatted_prediction = f"₹ {prediction:,.2f}"

        logger.info(f"Prediction successful: {formatted_prediction}")
        return render_template("index.html", prediction=formatted_prediction)

    except Exception as e:
        logger.exception("Prediction failed due to an error.")
        return render_template("index.html", prediction=f"Error: {e}")

if __name__ == '__main__':
    logger.info("Starting Flask server...")
    app.run(debug=True)
