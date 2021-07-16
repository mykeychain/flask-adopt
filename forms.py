"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, AnyOf, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pet."""

    name = StringField("Pet Name",
                    validators = [InputRequired()])
    species = StringField("Species",
                    validators = [InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL",
                    validators = [Optional(), URL()])
    age = StringField("Age",
                    validators = [InputRequired(), AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes = StringField("Notes")



class EditPetForm(FlaskForm):
    """Form for editing pet info."""

    photo_url = StringField("Photo URL",
                    validators = [Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Availability")