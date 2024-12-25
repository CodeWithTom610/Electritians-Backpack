from flask_login import UserMixin
from . import db
from datetime import datetime
from time import gmtime, strftime

date_today = strftime("%d.%m.%Y", gmtime())

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
    __tablename__ = 'knowledge_base_items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    imagepath = db.Column(db.String(200), nullable=True)
    imagepathbool = db.Column(db.Boolean, nullable=False, default=False)
    date_of_creation = db.Column(db.DateTime, nullable=False, default=datetime.time)

    def __init__(self, title, content, author, imagepath, imagepathbool, date_of_creation):
        self.title = title
        self.content = content
        self.author = author
        self.imagepath = imagepath
        self.imagepathbool = imagepathbool
        self.date_of_creation = date_of_creation

