# Import necessary modules
from flask_login import UserMixin  # Provides user authentication support
from . import db  # Imports the SQLAlchemy database instance
from datetime import datetime  # For handling dates and times
from time import gmtime, strftime  # For formatting and working with GMT time

# Get today's date in the format "dd.mm.yyyy"
date_today = strftime("%d.%m.%Y", gmtime())

# Model for News Cards
class New_Card(db.Model):
    __tablename__ = "NewsCards"  # Database table name
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    header = db.Column(db.String, nullable=False)  # Title of the news card (required)
    content = db.Column(db.String, nullable=False)  # Content of the news card (required)
    credits = db.Column(db.String, nullable=False)  # Credits for the image (required)
    imagepath = db.Column(db.String, nullable=False)  # Path to the associated image (required)

# Model for Admin Users
class Admin_User(db.Model, UserMixin):
    __tablename__ = "Admin_Users"  # Database table name
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String, nullable=False)  # Full name of the admin (required)
    username = db.Column(db.String, nullable=False)  # Admin's username (required)
    e_mail = db.Column(db.String, nullable=False)  # Admin's email address (required)
    password = db.Column(db.String, nullable=False)  # Admin's hashed password (required)
    token = db.Column(db.String, nullable=True)  # Optional field for reset or authentication tokens

# Model for Tool Cards
class Tool_Cards(db.Model):
    __tablename__ = "Tool_Cards"  # Database table name
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    tool_name = db.Column(db.String, nullable=False)  # Name of the tool (required)
    tool_description = db.Column(db.String, nullable=False)  # Description of the tool's purpose (required)
    endpoint = db.Column(db.String, nullable=False)  # API or URL endpoint for the tool (required)
    category = db.Column(db.Integer, nullable=False)  # Category ID linking to ToolCategories (required)

# Model for Tool Categories
class ToolCategories(db.Model):
    __tablename__ = "Tool_Categories"  # Database table name
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String, nullable=False)  # Name of the category (required)

# Model for Knowledge Base Items
class KnowledgeBaseItems(db.Model):
    __tablename__ = 'knowledge_base_items'  # Database table name

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Title of the knowledge base entry (required)
    content = db.Column(db.Text, nullable=False)  # Content of the knowledge base entry (required)
    author = db.Column(db.String(100), nullable=False)  # Author of the knowledge base entry (required)
    imagepath = db.Column(db.String(200), nullable=True)  # Path to the associated image (optional)
    imagepathbool = db.Column(db.Boolean, nullable=False, default=False)  # Indicates if an image is included (default: False)
    date_of_creation = db.Column(db.Date, nullable=False, default=datetime.time)  # Date when the entry was created (required)

    # Constructor to initialize the model fields
    def __init__(self, title, content, author, imagepath, imagepathbool, date_of_creation):
        self.title = title  # Set the title
        self.content = content  # Set the content
        self.author = author  # Set the author's name
        self.imagepath = imagepath  # Set the image path
        self.imagepathbool = imagepathbool  # Set whether an image is included
        self.date_of_creation = date_of_creation  # Set the date of creation


# Model for uploading files to local db
class fileUploads(db.Model):
    __tablename__ = "fileUploads" # Database table name
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    filename = db.Column(db.String(50)) # Filename of the uploaded file
    data = db.Column(db.LargeBinary) # Binary Data of uploaded file