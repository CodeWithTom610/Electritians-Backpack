from . import bcrypt
from .models import Admin_User

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)

def count_entries():
    count = Admin_User.query.count()
    countint = int(count)
    return countint