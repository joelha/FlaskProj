from flask.ext.wtf import Form

from wtforms import TextField, PasswordField, validators
from wtforms.validators import Required


class UsernamePasswordForm(Form):
    username = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])