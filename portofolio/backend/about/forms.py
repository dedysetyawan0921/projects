from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email
from models import Bio

class AboutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    birth = DateField('Birth', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[(DataRequired())])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    image_link = StringField('Image Link', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])