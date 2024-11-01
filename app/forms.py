from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, length, NumberRange

class ResistorForm(FlaskForm):
    Voltage = StringField("Spannung [V]", validators=[DataRequired()])
    Current = StringField("Stromstärke [A]", validators=[DataRequired()])
    submit = SubmitField("Berechnen")

class LoginForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired()])
    password = PasswordField("Passwort", validators=[DataRequired()])
    remember = BooleanField("Eingeloggt bleiben?")
    loginbutton = SubmitField("Login")

class NewsForm(FlaskForm):
    header = StringField("Titel", validators=[DataRequired()])
    content = StringField("Inhalt", validators=[DataRequired()])
    credits = StringField("Bildentwickler")
    imagepath = StringField("Bildpfad")
    submit = SubmitField("Speichern")

class UserForm(FlaskForm):
    name = StringField("Vollständiger Name", validators=[DataRequired()])
    username = StringField("Benutzername", validators=[DataRequired()])
    e_mail = EmailField("E-Mail Adresse", validators=[DataRequired()])
    password = PasswordField("Passwort", validators=[DataRequired(length(8, 128))])
    submit = SubmitField("Speichern")

class ResetForm(FlaskForm):
    password = PasswordField("Neues Passwort", validators=[DataRequired(), length(8, 128)])
    password_repeat = PasswordField("Wiederhole neues Passwort", validators=[DataRequired(), length(8, 128)])
    reset_token = StringField("Trage hier deinen Reset Token ein.", validators=[DataRequired()])
    submit = SubmitField("Speichern")