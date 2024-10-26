from . import bcrypt
from .models import Admin_User
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)

def count_entries():
    count = Admin_User.query.count()
    countint = int(count)
    return countint

def send_token(reset_token, e_mail):
    message = Mail(
        from_email='ebt-backpack@tomwalla.work.gd',
        to_emails= e_mail,
        subject='EBT-Packpack Wilkommen',
        html_content=f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./static/style_e_mail.css">
    <title>Reset Token</title>
</head>
<body>
    <div class="email-container">
        <div class="email-header">
            <h1>Passwort zurücksetzen</h1>
        </div>
        <div class="email-body">
            <p>Hallo,</p>
            <p>Wilkommen bei EBT-Backpack. Anbei kriegst du deinen Reset Token.</p>
            <p>Dieser ist wichtig um dein Passwort zurückzusetzen. Speicher ihn deshalb gut und gib Ihn nicht an dritte weiter.</p>
            <p>Dein Widerherstellungstoken lautet: {reset_token}</p>
        </div>
        <div class="email-footer">
            <p>© 2024 EBT-Backpack. Alle Rechte vorbehalten.</p>
        </div>
    </div>
</body>
</html>""")
    SendGridAPIClient(os.getenv("SENDGRID_API_KEY")).send(message)
