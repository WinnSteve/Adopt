"""forms"""

from flask_wtf import FlaskForm
from wtforms import IntergerField, TextAreaField, StringField, BooleanField, SelectField
from wtforms.validators import NumberRange, URL, InputRequired, Optional, Length


class AddPetForm(FlaskForm):
    """form to add pets"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        #
        choices=[("cat"), ("dog"), ("porcupine")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """for to edit existing pets"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
