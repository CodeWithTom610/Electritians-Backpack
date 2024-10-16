###############################################################################################################
#############################               Packages            ###############################################
###############################################################################################################

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_bcrypt import Bcrypt

###############################################################################################################
#############################            Configuration           ##############################################
###############################################################################################################

# Initialize Flask App
app = Flask(__name__, static_url_path='/static')

# Initialize Bootstrap App
bootstrap = Bootstrap5(app)

# Configure Flask App
app.config["SECRET_KEY"] = "7cd870fd19e3899b23e0eaafb97e094494b91d9957815a1"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# Initialize Database
db = SQLAlchemy(app)

# Initialize Flask Login
login_manager = LoginManager(app)
login_manager.login_view = "admin_login"


@login_manager.user_loader
def load_user(user_id):
    return Admin_User.query.filter_by(id=user_id).first()


# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)


def hash_password(plain_password: str):
    pw_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')
    return pw_hash


def check_password(plain_password: str, password_hash: any):
    checked_pw = bcrypt.check_password_hash(password_hash, plain_password)  # returns True
    return checked_pw

###############################################################################################################
############################                Forms                 #############################################
###############################################################################################################

class ResistorForm(FlaskForm):
    Voltage = IntegerField("Trage hier die Spannung [U] in Volt (V) ein.", validators=[DataRequired("Bitte gebe die Spannung ein!")])
    Current = IntegerField("Trage hier noch die Stromstärke [I] in Ampére (A) ein.", validators=[DataRequired("Bitte gebe eine Stromstärke ein!")])

class LoginForm(FlaskForm, UserMixin):
    username = StringField("Bitte Benutzernamen eingeben:", validators=[DataRequired()])
    password = PasswordField("Bitte Passwort eingeben:", validators=[DataRequired()])
    remember = BooleanField("Eingeloggt bleiben?")
    loginbutton = SubmitField("Login")

    def is_active(self):
        return True

class LogoutForm(FlaskForm, UserMixin):
    logoutbutton = SubmitField("Logout")

class NewsForm(FlaskForm):
    header = StringField("Titel", validators=[DataRequired()])
    content = StringField("Text/Inhalt", validators=[DataRequired()])
    author = StringField("Autor")
    imagepath = StringField("Bildname")
    submit = SubmitField("Speichern")

class UserForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired()])
    password = PasswordField("Passwort", validators=[DataRequired()])
    submit = SubmitField("Speichern")

class ResetForm(FlaskForm):
    password = PasswordField("Neues Passwort", validators=[DataRequired()])
    password_repeat = PasswordField("Wiederhole neues Passwort", validators=[DataRequired()])
    submit = SubmitField("Speichern")

###############################################################################################################
############################                Routes                #############################################
###############################################################################################################

# Main Dashboard (Home Page)
@app.route('/')
def news():
    news = New_Card.query.all()  # Abrufen aller News-Karten
    return render_template(
        'index.html',
        title="Home | EBT-Backpack",
        news=news
    )

# Tools page
@app.route('/tools-complete')
def tools_complete():
    return render_template('alle_tools.html', title="Alle Tools | EBT-Backpack")

# Admin Dashboard
@app.route('/admin/dashboard', methods=["GET", "POST"])
@login_required
def admin_dashboard():
    username = current_user.username
    news_cards = New_Card.query.all()
    count_user = count_entries()
    count_news = New_Card.query.count()
    count_tools = Tool_Cards.query.count()
    return render_template('admin-dashboard.html', news_cards=news_cards, username=username, title="Dashboard | EBT-Backpack", count_user = count_user, count_news=count_news, count_tools=count_tools)

def logout():
    logout_user()

def count_entries():
    count = Admin_User.query.count()
    countint = int(count)
    return countint

# Admin Login
@app.route('/admin', methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin_User.query.filter_by(username=form.username.data).first()
        user_password = user.password
        checked_pw = check_password(form.password.data, user_password)
        if user and checked_pw:
            login_user(user, remember=form.remember.data)
            return redirect(url_for("admin_dashboard"))
    return render_template('admin_login.html', title="Login | EBT-Backpack", form=form)



# Manage News (Add/Edit News)
@app.route('/admin/news', methods=["GET", "POST"])
@login_required
def manage_news():
   
    news = New_Card.query.all()

    return render_template('edit_news.html', title="Neuigkeiten Bearbeiten | EBT-Backpack", username=current_user.username, news=news)

# Admin Logout
@app.route('/admin/logout', methods=["GET", "POST"])
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('news'))

@app.route('/admin/edit-news/<int:news_id>', methods=["GET", "POST"])
@login_required
def edit_news(news_id):
    username = current_user.username
    news_card = New_Card.query.get_or_404(news_id)
    form = NewsForm(obj=news_card)
    if form.validate_on_submit():
        news_card.header = form.header.data
        news_card.content = form.content.data
        news_card.author = form.author.data
        news_card.imagepath = form.imagepath.data
        db.session.commit()  # Änderungen speichern
        return redirect(url_for('admin_dashboard'))
    
    return render_template('news-management.html', news_card=news_card, form=form, username=username, title=f"Bearbeite Karte id: {news_id} | EBT-Backpack")

@app.route('/admin/edit-news/new-entry', methods=["GET", "POST"])
@login_required
def new_entry():
    username = current_user.username
    form = NewsForm()
    if form.validate_on_submit():
        new_card = New_Card(header=form.header.data, content=form.content.data, author=form.author.data, imagepath=form.imagepath.data)
        db.session.add(new_card)
        db.session.commit()  # Änderungen speichern
        return redirect(url_for("manage_news"))
    return render_template('new-entry-news.html', username=username, form=form, title="Neuer Eintrag | EBT-Backpack")

@app.route('/admin/delete-news/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_card(id):
    news_card = New_Card.query.get_or_404(id)  # Abrufen der Karte, die gelöscht werden soll
    db.session.delete(news_card)  # Karte löschen
    db.session.commit()  # Änderungen speichern
    return redirect(url_for('manage_news'))  # Zurück zur Manage-Seite

@app.route('/admin/users')
@login_required
def users():
    username = current_user.username
    users = Admin_User.query.all()
    return render_template("manage-users.html", title="Benutzer | EBT-Backpack", users = users, username = username)

@app.route('/admin/users/delete_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    user = Admin_User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/admin/users/new_user', methods=['GET', 'POST'])
@login_required
def new_user():
    form = UserForm()
    username = current_user.username
    if form.validate_on_submit():
        hashed_pw = hash_password(form.password.data)
        new_user = Admin_User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))

    return render_template("new-user.html", title="Neuer Benutzer | EBT-Backpack", form=form, username=username)

@app.route('/admin/users/reset/password/<int:user_id>', methods=['GET', 'POST'])
def reset_password(user_id):
    form = ResetForm()
    username = current_user.username
    title=f"Passwort Reset für Benutzer: {user_id}"
    if form.validate_on_submit():
        if form.password.data == form.password_repeat.data:
            user = Admin_User.query.get_or_404(user_id)
            hashed_pw = hash_password(form.password.data)
            user.password = hashed_pw
            db.session.commit()
        else:
            title="Passwörter müssen übereinstimmen!"
    return render_template("reset-password.html", title=title, username = username, form=form)


###############################################################################################################
############################           Database Models         ################################################
###############################################################################################################

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

###############################################################################################################
############################              Run Dialog              #############################################
###############################################################################################################

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)