
from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    password_repeat = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
