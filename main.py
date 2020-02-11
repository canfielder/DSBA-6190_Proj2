from flask import Flask, request, render_template
from flask.logging import create_logger
import logging

import joblib

# Import from Python Scripts
from python_scripts.model import InputForm
from python_scripts.custom_functions import create_dataframe, scale

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


# App Pages
@app.route('/', methods = ['GET', 'POST'])
def predict():
    
    form = InputForm(request.form)
    LOG.info(f"Form Require: {form}")
    
    if request.method == 'POST' and form.validate():
        # Convert Input Table Data to DataFrame
        df_input = create_dataframe(form)
        LOG.info(f"Convert Input to DataFrame: {df_input}")
        
        # Scale Input Data per Sklearn model parameters
        df_scaled = scale(df_input)
        LOG.info(f"Scale Input Data: {df_scaled}")
        
        # Predict Wine Quality
        prediction = list(clf.predict(df_scaled))
        LOG.info(f"Predict: {prediction}")
    
    else:
        prediction = None
    
    return render_template('index.html', form = form, result = prediction)
    

if __name__ == '__main__':
    clf = joblib.load('wine_predict/wine_quality_prediction.joblib')
    app.run(debug=True, host='0.0.0.0')
