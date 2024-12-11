from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate  # Für Migrationen


# Initialize Extensions without App Context
db = SQLAlchemy()
bootstrap = Bootstrap5()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()
knowledgebase_items_charstoshow = 200 # Creating Global Variable for Knowledgebase

def create_app():
    app = Flask(__name__, static_url_path='/static')

    # Load configurations
    app.config.from_object('config.Config')

    # Initialize Extensions within App Context
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)  # Migration initialisieren

    login_manager.login_view = "admin_login"


    # Import Blueprints and Models after App is created and Extensions initialized
    from .routes import main
    from .models import Admin_User  # Import Models after db.init_app
    app.register_blueprint(main)

    return app

@login_manager.user_loader
def load_user(user_id):
    from.models import Admin_User
    return Admin_User.query.get(user_id)
