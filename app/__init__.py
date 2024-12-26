from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate  # Importing Migrate for database migrations

# Initialize Extensions without App Context
db = SQLAlchemy()  # SQLAlchemy for database interaction
bootstrap = Bootstrap5()  # Flask-Bootstrap for frontend styling and templates
login_manager = LoginManager()  # Manages user login sessions
bcrypt = Bcrypt()  # Handles password hashing and verification
migrate = Migrate()  # Manages database migrations (schema changes)

# Global variable for controlling the number of characters shown in the Knowledgebase
knowledgebase_items_charstoshow = 200

def create_app():
    """
    Factory function to create and configure the Flask app.
    
    Returns:
    app (Flask): Configured Flask application instance.
    """
    app = Flask(__name__, static_url_path='/static')  # Initialize the Flask app and static file path

    # Load configuration settings from the 'config' module
    app.config.from_object('config.Config')

    # Initialize the extensions with the app context
    db.init_app(app)  # Initialize the SQLAlchemy extension
    bootstrap.init_app(app)  # Initialize Flask-Bootstrap for styling
    login_manager.init_app(app)  # Initialize Flask-Login for user session management
    bcrypt.init_app(app)  # Initialize Bcrypt for password hashing
    migrate.init_app(app, db)  # Initialize Flask-Migrate for database migrations

    login_manager.login_view = "admin_login"  # Specify the login route for Flask-Login

    # Import Blueprints and Models after the app is created and extensions are initialized
    from .routes import main  # Import the main blueprint for routes
    from .models import Admin_User  # Import Admin_User model after db initialization
    app.register_blueprint(main)  # Register the main blueprint with the app

    return app  # Return the fully configured app instance

@login_manager.user_loader
def load_user(user_id):
    """
    Callback function for loading a user by their ID. This function is called by 
    Flask-Login to load the currently logged-in user from the database.

    Parameters:
    user_id (int): The ID of the user to load.

    Returns:
    Admin_User (object): The user object from the database, or None if not found.
    """
    from .models import Admin_User  # Import Admin_User model
    return Admin_User.query.get(user_id)  # Query the database and return the user with the given ID
