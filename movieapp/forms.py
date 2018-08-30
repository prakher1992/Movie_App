from flask_wtf import FlaskForm
from wtforms import StringField,DateTimeField,SubmitField
from wtforms.validators import DataRequired,Length

class AddMovieForm(FlaskForm):
    name=StringField('name',validators=[DataRequired(),Length(min=2,max=10)])
    datetime=StringField('datetime',validators=[DataRequired()])
    location=StringField('location',validators=[DataRequired()])
    submit=SubmitField('Submit')