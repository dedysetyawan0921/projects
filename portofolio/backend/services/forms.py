from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from models import Services

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    icon = StringField('Icon', validators=[DataRequired()])
    submit = SubmitField('Create')
    
