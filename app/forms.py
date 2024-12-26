# Import necessary modules from Flask-WTF and WTForms
from flask_wtf import FlaskForm  # Base class for creating forms
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField,
    TextAreaField,
    DateField
)  # Form field types
from wtforms.validators import DataRequired, length, NumberRange  # Validators for form fields

# Form for Resistance Calculator Tool
class ResistorForm(FlaskForm):
    # Field to input the voltage (required)
    Voltage = StringField("Spannung [V]", validators=[DataRequired()])
    # Field to input the current (required)
    Current = StringField("Stromstärke [A]", validators=[DataRequired()])
    # Submit button for the form
    submit = SubmitField("Berechnen")

# Form for User Login
class LoginForm(FlaskForm):
    # Field to input the username (required)
    username = StringField("Benutzername", validators=[DataRequired()])
    # Field to input the password (required)
    password = PasswordField("Passwort", validators=[DataRequired()])
    # Checkbox to stay logged in
    remember = BooleanField("Eingeloggt bleiben?")
    # Button to submit the login form
    loginbutton = SubmitField("Login")

# Form for News Creation/Editing
class NewsForm(FlaskForm):
    # Field to input the news title (required)
    header = StringField("Titel", validators=[DataRequired()])
    # Field to input the news content (required)
    content = StringField("Inhalt", validators=[DataRequired()])
    # Optional field to credit the image creator
    credits = StringField("Bildentwickler")
    # Optional field to provide the image path
    imagepath = StringField("Bildpfad")
    # Button to save the news
    submit = SubmitField("Speichern")

# Form for Admin User Creation/Editing
class UserForm(FlaskForm):
    # Field to input the user's full name (required)
    name = StringField("Vollständiger Name", validators=[DataRequired()])
    # Field to input the username (required)
    username = StringField("Benutzername", validators=[DataRequired()])
    # Field to input the user's email address (required)
    e_mail = EmailField("E-Mail Adresse", validators=[DataRequired()])
    # Field to input the user's password (required, with length constraints)
    password = PasswordField("Passwort", validators=[DataRequired(length(8, 128))])
    # Button to save the user
    submit = SubmitField("Speichern")

# Form for Resetting Passwords
class ResetForm(FlaskForm):
    # Field to input the new password (required, with length constraints)
    password = PasswordField("Neues Passwort", validators=[DataRequired(), length(8, 128)])
    # Field to confirm the new password (required, with length constraints)
    password_repeat = PasswordField("Wiederhole neues Passwort", validators=[DataRequired(), length(8, 128)])
    # Field to input the reset token (required)
    reset_token = StringField("Trage hier deinen Reset Token ein.", validators=[DataRequired()])
    # Button to save the new password
    submit = SubmitField("Speichern")

# Form for Creating New Knowledge Base Entries
class New_Knowledgebase_Entry(FlaskForm):
    # Field to input the entry title (required)
    title = StringField("Titel", validators=[DataRequired()])
    # Field to input the entry content (required)
    content = TextAreaField("Inhalt - Fülle den Eintrag mit Leben", validators=[DataRequired()])
    # Field to input the author's name (required)
    author = StringField("Autor", validators=[DataRequired()])
    # Checkbox to indicate if the article includes an image
    imagepathbool = BooleanField("Umfasst der Artikel ein Bild?")
    # Field to input the image path (optional, with specific notes for internal images)
    imagepath = StringField("Bild Link - Bitte beachte, dass nur BMW-Interne Bilder ohne Attribution des Autors veröffentlicht werden dürfen!")
    # Field to input the creation date of the entry (required)
    date_of_creation = DateField("Erstellungsdatum", validators=[DataRequired()])
    # Button to create the new knowledge base entry
    submit = SubmitField("Erstellen")
