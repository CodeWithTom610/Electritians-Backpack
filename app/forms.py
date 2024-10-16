from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ResistorForm(FlaskForm):
    Voltage = IntegerField("Spannung [V]", validators=[DataRequired()])
    Current = IntegerField("Stromstärke [A]", validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired()])
    password = PasswordField("Passwort", validators=[DataRequired()])
    remember = BooleanField("Eingeloggt bleiben?")
    loginbutton = SubmitField("Login")

class NewsForm(FlaskForm):
    header = StringField("Titel", validators=[DataRequired()])
    content = StringField("Inhalt", validators=[DataRequired()])
    author = StringField("Autor")
    imagepath = StringField("Bildpfad")
    submit = SubmitField("Speichern")

class UserForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired()])
    password = PasswordField("Passwort", validators=[DataRequired()])
    submit = SubmitField("Speichern")

class ResetForm(FlaskForm):
    password = PasswordField("Neues Passwort", validators=[DataRequired()])
    password_repeat = PasswordField("Wiederhole neues Passwort", validators=[DataRequired()])
    submit = SubmitField("Speichern")