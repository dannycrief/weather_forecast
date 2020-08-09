from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ForecastForm(FlaskForm):
    city = StringField('city')
    date = DateField('date', format='%d-%m-%y', validators=[DataRequired()])
    temperature = StringField('temperature')


class LoginForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')


class CreateUserForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
