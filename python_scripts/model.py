from wtforms import Form, FloatField, validators


class InputForm(Form):
    fixed_acidity = FloatField(
        label='Fixed Acidity ', default=0,
        validators=[validators.InputRequired()])
    volatile_acidity = FloatField(
        label='Volatile Acidity ', default=0,
        validators=[validators.InputRequired()])
    citric_acid = FloatField(
        label='Citric Acid ', default=0,
        validators=[validators.InputRequired()])
    residual_sugar = FloatField(
        label='Residual Sugar ', default=0,
        validators=[validators.InputRequired()])
    chlorides = FloatField(
        label='Chlorides ', default=0,
        validators=[validators.InputRequired()])
    free_sulfur_dioxide = FloatField(
        label='Free Sulfur Dioxide ', default=0,
        validators=[validators.InputRequired()])
    total_sulfur_dioxide = FloatField(
        label='Total Sulfur Dioxide ', default=0,
        validators=[validators.InputRequired()])
    density = FloatField(
        label='Density ', default=0,
        validators=[validators.InputRequired()])
    ph = FloatField(
        label='pH ', default=0,
        validators=[validators.InputRequired()])
    sulphates = FloatField(
        label='Sulphates ', default=0,
        validators=[validators.InputRequired()])
    alcohol = FloatField(
        label='Alcohol ', default=0,
        validators=[validators.InputRequired()])
