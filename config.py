import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "7cd870fd19e3899b23e0eaafb97e094494b91d9957815a1")
    SQLALCHEMY_DATABASE_URI = os.getenv("./app/instance", "sqlite:///database.db")  # SQLite als Standard
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deaktivieren, um Warnungen zu vermeiden
