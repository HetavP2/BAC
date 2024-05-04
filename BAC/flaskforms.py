from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, NumberRange
from wtforms.fields import SelectField, DateField, EmailField, FieldList


# Create login form
class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=80)])