from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddUserForm(Form):
    username = TextField('username', [DataRequired(), Length(min=3, max=25)])
    email = TextField(
        'email',
        [DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField(
        'password',
        [DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField(
        'Repeat password',
        [DataRequired(), EqualTo('password', message='Passwords must match.')])
