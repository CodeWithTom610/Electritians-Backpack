from flask import Blueprint, render_template, redirect, url_for, send_from_directory, app, flash
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, NewsForm, UserForm, ResetForm
from .models import New_Card, Admin_User, Tool_Cards
from .utils import check_password, hash_password, count_entries, send_token
from . import db
import os
import string
import random

main = Blueprint('main', __name__)


@main.route('/')
def news():
    news = New_Card.query.all()
    return render_template('index.html', title="Home | EBT-Backpack", news=news)

@main.route('/admin', methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin_User.query.filter_by(username=form.username.data).first()
        if user and check_password(form.password.data, user.password):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("main.admin_dashboard"))
    return render_template('admin_login.html', title="Login | EBT-Backpack", form=form)

@main.route('/tools-complete')
def tools_complete():
    return render_template('alle_tools.html')

# Manage News (Add/Edit News)
@main.route('/admin/news', methods=["GET", "POST"])
@login_required
def manage_news():
   
    news = New_Card.query.all()
    print(news)

    return render_template('edit_news.html', title="Neuigkeiten Bearbeiten | EBT-Backpack", username=current_user.username, news=news)

# Admin Logout
@main.route('/admin/logout', methods=["GET", "POST"])
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('main.news'))

@main.route('/admin/edit-news/<int:news_id>', methods=["GET", "POST"])
@login_required
def edit_news(news_id):
    username = current_user.name
    news_card = New_Card.query.get_or_404(news_id)
    form = NewsForm(obj=news_card)
    if form.validate_on_submit():
        news_card.header = form.header.data
        news_card.content = form.content.data
        news_card.author = form.author.data
        news_card.imagepath = form.imagepath.data
        db.session.commit()  # Änderungen speichern
        return redirect(url_for('main.admin_dashboard'))
    
    return render_template('news-management.html', news_card=news_card, form=form, username=username, title=f"Bearbeite Karte id: {news_id} | EBT-Backpack")

@main.route('/admin/edit-news/new-entry', methods=["GET", "POST"])
@login_required
def new_entry():
    username = current_user.name
    form = NewsForm()
    if form.validate_on_submit():
        new_card = New_Card(header=form.header.data, content=form.content.data, author=form.author.data, imagepath=form.imagepath.data)
        db.session.add(new_card)
        db.session.commit()  # Änderungen speichern
        return redirect(url_for("main.manage_news"))
    return render_template('new-entry-news.html', username=username, form=form, title="Neuer Eintrag | EBT-Backpack")

@main.route('/admin/delete-news/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_card(id):
    news_card = New_Card.query.get_or_404(id)  # Abrufen der Karte, die gelöscht werden soll
    db.session.delete(news_card)  # Karte löschen
    db.session.commit()  # Änderungen speichern
    return redirect(url_for('main.manage_news'))  # Zurück zur Manage-Seite

@main.route('/admin/users')
@login_required
def users():
    username = current_user.name
    users = Admin_User.query.all()
    return render_template("manage-users.html", title="Benutzer | EBT-Backpack", users = users, username = username)

@main.route("/admin/users/check_user/<int:user_id>")
@login_required
def check_user(user_id):
    current_user_id = current_user.id
    if current_user_id == user_id:
        flash("Du kannst nicht deinen eigenen Benutzer löchen wenn du angemeldet bist.")
        return redirect(url_for("main.users"))
    else:
        return redirect(url_for("main.delete_user", user_id=user_id))


@main.route('/admin/users/delete_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    user = Admin_User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.users'))

@main.route('/admin/users/new_user', methods=['GET', 'POST'])
@login_required
def new_user():
    form = UserForm()
    username = current_user.name
    if form.validate_on_submit():
        hashed_pw = hash_password(form.password.data)
        characters = string.ascii_letters + string.digits + string.punctuation
        token = "".join(random.choice(characters) for i in range(8))
        hashed_token = hash_password(token)
        send_token(token, form.e_mail.data)
        new_user = Admin_User(username=form.username.data, password=hashed_pw, e_mail=form.e_mail.data, name=form.name.data, token=hashed_token)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.users'))
    return render_template("new-user.html", title="Neuer Benutzer | EBT-Backpack", form=form, username=username)

@main.route('/admin/users/reset/password/<int:user_id>', methods=['GET', 'POST'])
def reset_password(user_id):
    username = current_user.name
    title=f"Passwort Reset für Benutzer: {user_id}"
    user = Admin_User.query.get_or_404(user_id)
    token = user.token
    form = ResetForm()
    if form.validate_on_submit():
        if form.password.data == form.password_repeat.data and check_password(form.reset_token.data, token):
            hashed_pw = hash_password(form.password.data)
            user.password = hashed_pw
            db.session.commit()
        else:
            title="Passwörter stimmen nicht überein oder Token ist ungültig."
    return render_template("reset-password.html", title=title, username = username, form=form)

# Admin Dashboard
@main.route('/admin/dashboard', methods=["GET", "POST"])
@login_required
def admin_dashboard():
    username = current_user.name
    news_cards = New_Card.query.all()
    count_user = count_entries()
    count_news = New_Card.query.count()
    count_tools = Tool_Cards.query.count()
    return render_template('admin-dashboard.html', news_cards=news_cards, username=username, title="Dashboard | EBT-Backpack", count_user = count_user, count_news=count_news, count_tools=count_tools)

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')