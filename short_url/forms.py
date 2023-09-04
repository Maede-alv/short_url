from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class UrlForm(FlaskForm):
    url = StringField(
        "Paste the URL to be shortened",
        validators=[InputRequired()],
        render_kw={"placeholder": "Enter the link here"}
    )
    submit = SubmitField("Shorten URL")