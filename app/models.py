from flask_login import UserMixin
from . import db

class New_Card(db.Model):
    __tablename__ = "NewsCards"
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String)
    author = db.Column(db.String)
    imagepath = db.Column(db.String)

class Admin_User(db.Model, UserMixin):
    __tablename__ = "Admin_Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

class Tool_Cards(db.Model):
    __tablename__ = "Tool_Cards"
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String, unique=True)
    tool_description = db.Column(db.String, unique=True)
    endpoint = db.Column(db.String, unique=True)
