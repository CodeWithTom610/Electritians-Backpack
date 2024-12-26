import os

class Config:
    # SECRET_KEY is used to secure sessions and cookies, should be kept secret.
    # It's fetched from environment variables for security, with a fallback default value.
    SECRET_KEY = os.getenv("SECRET_KEY", "7cd870fd19e3899b23e0eaafb97e094494b91d9957815a1")
    
    # SQLALCHEMY_DATABASE_URI is the URI used to connect to the database.
    # Here, it's trying to fetch a database path from the environment variables (could be used for production).
    # If not found, it defaults to using SQLite with a local database named 'database.db'.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///database.db")  # Changed to use "DATABASE_URI" as env var name
    
    # SQLALCHEMY_TRACK_MODIFICATIONS disables tracking modifications of objects,
    # which is unnecessary and can lead to performance overhead.
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable to avoid warnings in SQLAlchemy logs
