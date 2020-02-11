import pandas as pd

# Functions for use in Main.py


def scale(payload, scaler):
    """Scales Payload"""
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


def create_dataframe(form):
    df_init = pd.DataFrame(
        columns=[
            'fixed_acidity', 'volatile_acidity', 'citric_acid',
            'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
            'total_sulfur_dioxide', 'density', 'ph', 'sulphates',
            'alcohol'
        ]
    )

    df_input = df_init.append(
        {
            'fixed_acidity': form.fixed_acidity.data,
            'volatile_acidity': form.volatile_acidity.data,
            'citric_acid': form.citric_acid.data,
            'residual_sugar': form.residual_sugar.data,
            'chlorides': form.chlorides.data,
            'free_sulfur_dioxide': form.free_sulfur_dioxide.data,
            'total_sulfur_dioxide': form.total_sulfur_dioxide.data,
            'density': form.density.data,
            'ph': form.ph.data,
            'sulphates': form.sulphates.data,
            'alcohol': form.alcohol.data
        },
        ignore_index=True
    )

    return df_input
