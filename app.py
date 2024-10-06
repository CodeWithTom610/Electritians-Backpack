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
    header = StringField("News Header", validators=[DataRequired()])
    content = StringField("News Content", validators=[DataRequired()])
    author = StringField("Author")
    imagepath = StringField("Image Path")
    submit = SubmitField("Save News")

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
    form = LogoutForm()
    if form.validate_on_submit():
        logout_user()
        return redirect(url_for('admin_login'))

    # Fetch existing news cards
    news_cards = New_Card.query.all()
    return render_template('admin-dashboard.html', form=form, news_cards=news_cards)

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
    form = NewsForm()
    if form.validate_on_submit():
        new_card = New_Card(
            header=form.header.data,
            content=form.content.data,
            author=form.author.data,
            imagepath=form.imagepath.data
        )
        db.session.add(new_card)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))

    return render_template('news_management.html', form=form)

# Admin Logout
@app.route('/admin/logout', methods=["POST"])
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('news'))

# Edit an existing news card
@app.route('/admin/edit_news/<int:news_id>', methods=["GET", "POST"])
@login_required
def edit_news(news_id):
    news_card = New_Card.query.get_or_404(news_id)
    form = NewsForm(obj=news_card)  # Form mit den existierenden Daten der News-Karte vorfüllen

    if form.validate_on_submit():
        news_card.header = form.header.data
        news_card.content = form.content.data
        news_card.author = form.author.data
        news_card.imagepath = form.imagepath.data
        db.session.commit()  # Änderungen speichern
        return redirect(url_for('admin_dashboard'))

    return render_template('edit_news.html', form=form, news_card=news_card)


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

###############################################################################################################
############################              Run Dialog              #############################################
###############################################################################################################

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)