from flask_login import UserMixin
from . import db

class New_Card(db.Model):
    __tablename__ = "NewsCards"
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    credits = db.Column(db.String, nullable=False)
    imagepath = db.Column(db.String, nullable=False)

class Admin_User(db.Model, UserMixin):
    __tablename__ = "Admin_Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    e_mail = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable = True)

class Tool_Cards(db.Model):
    __tablename__ = "Tool_Cards"
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String, nullable=False)
    tool_description = db.Column(db.String, nullable=False)
    endpoint = db.Column(db.String, nullable=False)
    category = db.Column(db.Integer, nullable=False)

class ToolCategories(db.Model):
    __tablename__ = "Tool_Categories"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

class KnowledgeBaseItems(db.Model):
    __tablename__ = "KnowledgeBaseItems"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author = db.Column(db.String)
    imagepathbool = db.Column(db.String)
    imagepath = db.Column(db.String)
    endpointbool = db.Column(db.String)
    endpoint = db.Column(db.String)
