from sklearn.preprocessing import StandardScaler
import pandas as pd

# Functions for use in Main.py

def scale(payload):
    """Scales Payload"""
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict
    

def create_dataframe(form):
    df_input = [
        ['fixed_acidity', form.fixed_acidity.data], 
        ['volatile_acidity', form.volatile_acidity.data], 
        ['citric_acid', form.citric_acid.data],
        ['residual_sugar', form.residual_sugar.data], 
        ['chlorides', form.chlorides.data], 
        ['free_sulfur_dioxide', form.free_sulfur_dioxide.data],
        ['total_sulfur_dioxide', form.total_sulfur_dioxide.data], 
        ['density', form.density.data], 
        ['ph', form.ph.data],
        ['sulphates', form.sulphates.data], 
        ['alcohol', form.alcohol.data], 
        ['citric_acid', form.chlorides.data]
    ]
    return df_input