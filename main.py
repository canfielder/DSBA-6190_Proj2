from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# Functions
def scale(payload):
    """Scales Payload"""

    LOG.info(f"Scaling Payload: {payload}")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

# App Pages
@app.route('/')
def home():
    html = f"<h2>Sklearn Wine Quality Prediction Home</h2>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    
    json_payload = request.get_json()
    LOG.info(f"JSON payload: {json_payload}")
    
    inference_payload = pd.read_json(json_payload)
    LOG.info(f"inference payload DataFrame: {inference_payload}")
    
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    clf = joblib.load('wine_predict/wine_quality_prediction.joblib')
    app.run(debug=True, host='0.0.0.0')
