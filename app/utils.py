from . import bcrypt
from .models import Admin_User
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Function to hash a password
def hash_password(password: str) -> str:
    """
    Hashes the provided password using bcrypt.

    Parameters:
    password (str): The plain text password to hash.

    Returns:
    str: The hashed password as a UTF-8 encoded string.
    """
    # Generate a bcrypt hash of the password and decode it to UTF-8 string
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Function to check if a given password matches the hashed password
def check_password(password: str, hashed_password: str) -> bool:
    """
    Checks if the provided password matches the hashed password.

    Parameters:
    password (str): The plain text password to check.
    hashed_password (str): The hashed password to compare against.

    Returns:
    bool: True if the password matches the hashed password, False otherwise.
    """
    # Compare the plain password with the hashed password
    return bcrypt.check_password_hash(hashed_password, password)

# Function to count the number of Admin Users
def count_entries() -> int:
    """
    Counts the total number of admin users in the database.

    Returns:
    int: The number of admin users.
    """
    # Query the database to count the number of Admin_User entries
    count = Admin_User.query.count()
    
    # Convert the count result into an integer
    countint = int(count)
    
    # Return the count as an integer
    return countint

# Function to send a reset token to the user's email
def send_token(reset_token: str, e_mail: str):
    """
    Sends a password reset token to the user's email using SendGrid.

    Parameters:
    reset_token (str): The password reset token to send.
    e_mail (str): The recipient email address.
    """
    # Create the email message using SendGrid's Mail helper class
    message = Mail(
        from_email='ebt-backpack@tomwalla.work.gd',  # Sender's email address
        to_emails=e_mail,                          # Recipient's email address
        subject='EBT-Packpack Wilkommen',          # Subject of the email
        html_content=f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./static/style_e_mail.css">  <!-- Link to custom CSS file -->
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
    
    # Send the email via the SendGrid API, using the API key from environment variables
    SendGridAPIClient(os.getenv("SENDGRID_API_KEY")).send(message)





