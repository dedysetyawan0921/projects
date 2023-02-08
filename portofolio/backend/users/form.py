from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User


class CreateUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(
        min=2, max=20,  message="Panjang harus minimal 2 dan maksimal 20 karakter")])
    email = StringField('Email', validators=[DataRequired(), Email(
        message='Pastikan Email yang anda masukkan benar')])
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=8, message="Password tidak boleh kurang dari 8 karakter")])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Create User')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Telah Digunakan')

    def calidate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Ini Telah Digunakan')


class Login(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(message="Masukkan email yang benar")])
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=8, message="Password tidak boleh kurang dari 8 karakter")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
