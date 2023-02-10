from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class AboutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    birth = DateField('Birth', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[(DataRequired())])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    image_link = StringField('Image Link', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    submit = SubmitField('Create')