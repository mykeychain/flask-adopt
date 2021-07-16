"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired, AnyOf, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name",
                    validators = [InputRequired()])
    species = StringField("Species",
                    validators = [InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL",
                    validators = [Optional(), URL()])
    age = StringField("Age",
                    validators = [InputRequired(), AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes = StringField("Notes")