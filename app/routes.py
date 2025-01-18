# Import necessary modules and components from Flask and other dependencies
from io import BytesIO
from flask import Blueprint, render_template, redirect, url_for, send_from_directory, app, flash, request, session, send_file
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, NewsForm, UserForm, ResetForm, ResistorForm, New_Knowledgebase_Entry, Searching_Bar
from .models import New_Card, Admin_User, Tool_Cards, ToolCategories, KnowledgeBaseItems, fileUploads
from .utils import check_password, hash_password, count_entries, send_token, upload_file_to_server
from . import db
import os
import string
import random
from .tools import ResistanceCalculating
from . import knowledgebase_items_charstoshow

# Define the main Blueprint for the application
main = Blueprint('main', __name__)

# ----------- PUBLIC ROUTES -----------

# Home Page - Display news cards
@main.route('/')
def news():
    # Fetch all news cards from the database
    news = New_Card.query.all()
    return render_template('index.html', title="Home | EBT-Backpack", news=news)

# ----------- ADMIN AUTHENTICATION -----------

# Admin Login Page
@main.route('/admin', methods=["GET", "POST"])
def admin_login():
    form = LoginForm()  # Instantiate the login form
    if form.validate_on_submit():  # Validate the submitted form
        # Fetch the admin user by username
        user = Admin_User.query.filter_by(username=form.username.data).first()
        # Check if the user exists and the password is correct
        if user and check_password(form.password.data, user.password):
            login_user(user, remember=form.remember.data)  # Log the user in
            return redirect(url_for("main.admin_dashboard"))  # Redirect to admin dashboard
        else:
            flash("Wrong username or password", 'warning')  # Display error message
    return render_template('admin_login.html', title="Login | EBT-Backpack", form=form)

# Admin Logout
@main.route('/admin/logout', methods=["GET", "POST"])
@login_required  # Ensure only logged-in users can access this route
def admin_logout():
    logout_user()  # Log out the current user
    return redirect(url_for('main.news'))  # Redirect to the home page

# ----------- ADMIN NEWS MANAGEMENT -----------

# Manage News - Display and edit news cards
@main.route('/admin/news', methods=["GET", "POST"])
@login_required  # Ensure only logged-in users can access this route
def manage_news():
    # Fetch all news cards from the database
    news = New_Card.query.all()
    return render_template('edit_news.html', title="Neuigkeiten Bearbeiten | EBT-Backpack", username=current_user.username, news=news)

# Edit an Existing News Card
@main.route('/admin/edit-news/<int:news_id>', methods=["GET", "POST"])
@login_required
def edit_news(news_id):
    username = current_user.name  # Get the current admin's username
    news_card = New_Card.query.get_or_404(news_id)  # Fetch the news card by ID
    form = NewsForm(obj=news_card)  # Prepopulate the form with the news card data
    if form.validate_on_submit():  # Validate the submitted form
        # Update the news card fields with the form data
        news_card.header = form.header.data
        news_card.content = form.content.data
        news_card.credits = form.credits.data
        news_card.imagepath = form.imagepath.data
        db.session.commit()  # Save the changes to the database
        return redirect(url_for('main.admin_dashboard'))  # Redirect to admin dashboard
    return render_template('news-management.html', news_card=news_card, form=form, username=username, title=f"Bearbeite Karte id: {news_id} | EBT-Backpack")

# Create a New News Card
@main.route('/admin/edit-news/new-entry', methods=["GET", "POST"])
@login_required
def new_entry():
    username = current_user.name  # Get the current admin's username
    form = NewsForm()  # Instantiate the news form
    if form.validate_on_submit():  # Validate the submitted form
        # Create a new news card with the form data
        new_card = New_Card(
            header=form.header.data,
            content=form.content.data,
            credits=form.credits.data,
            imagepath=form.imagepath.data
        )
        db.session.add(new_card)  # Add the new card to the database
        db.session.commit()  # Save the changes
        return redirect(url_for("main.manage_news"))  # Redirect to the manage news page
    return render_template('new-entry-news.html', username=username, form=form, title="Neuer Eintrag | EBT-Backpack")

# Delete a News Card
@main.route('/admin/delete-news/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_card(id):
    # Fetch the news card by ID
    news_card = New_Card.query.get_or_404(id)
    db.session.delete(news_card)  # Delete the news card
    db.session.commit()  # Save the changes
    return redirect(url_for('main.manage_news'))  # Redirect to the manage news page

# ----------- ADMIN USER MANAGEMENT -----------

# View and Manage Admin Users
@main.route('/admin/users')
@login_required
def users():
    username = current_user.name  # Get the current admin's username
    users = Admin_User.query.all()  # Fetch all admin users
    return render_template("manage-users.html", title="Benutzer | EBT-Backpack", users=users, username=username)

# Check and Validate User Deletion
@main.route("/admin/users/check_user/<int:user_id>")
@login_required
def check_user(user_id):
    current_user_id = current_user.id  # Get the current admin's user ID
    if current_user_id == user_id:  # Prevent self-deletion
        flash("Du kannst nicht deinen eigenen Benutzer löchen wenn du angemeldet bist.")
        return redirect(url_for("main.users"))  # Redirect to the users page
    else:
        return redirect(url_for("main.delete_user", user_id=user_id))  # Redirect to delete user

# Delete an Admin User
@main.route('/admin/users/delete_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    user = Admin_User.query.get_or_404(user_id)  # Fetch the user by ID
    db.session.delete(user)  # Delete the user
    db.session.commit()  # Save the changes
    return redirect(url_for('main.users'))  # Redirect to the users page
# Create a New Admin User
@main.route('/admin/users/new_user', methods=['GET', 'POST'])
@login_required
def new_user():
    form = UserForm()  # Instantiate the user form
    username = current_user.name  # Get the current admin's username
    if form.validate_on_submit():  # Validate the submitted form
        # Hash the provided password
        hashed_pw = hash_password(form.password.data)
        # Generate a unique token
        characters = string.ascii_letters + string.digits + string.punctuation
        token = "".join(random.choice(characters) for i in range(8))
        hashed_token = hash_password(token)  # Hash the token
        send_token(token, form.e_mail.data)  # Send the token to the user's email
        # Create a new user with the form data
        new_user = Admin_User(
            username=form.username.data,
            password=hashed_pw,
            e_mail=form.e_mail.data,
            name=form.name.data,
            token=hashed_token
        )
        db.session.add(new_user)  # Add the new user to the database
        db.session.commit()  # Save the changes
        return redirect(url_for('main.users'))  # Redirect to the users page
    return render_template("new-user.html", title="Neuer Benutzer | EBT-Backpack", form=form, username=username)

# Reset an Admin User's Password
@main.route('/admin/users/reset/password/<int:user_id>', methods=['GET', 'POST'])
@login_required
def reset_password(user_id):
    username = current_user.name  # Get the current admin's username
    user = Admin_User.query.get_or_404(user_id)  # Fetch the user by ID
    token = user.token  # Retrieve the user's reset token
    form = ResetForm()  # Instantiate the reset password form
    if form.validate_on_submit():  # Validate the submitted form
        # Check if the passwords match and the token is valid
        if form.password.data == form.password_repeat.data and check_password(form.reset_token.data, token):
            hashed_pw = hash_password(form.password.data)  # Hash the new password
            user.password = hashed_pw  # Update the user's password
            db.session.commit()  # Save the changes
        else:
            flash("Passwörter stimmen nicht überein oder Token ist ungültig.", 'danger')
    return render_template("reset-password.html", title=f"Passwort Reset für Benutzer: {user_id}", username=username, form=form)

# ----------- ADMIN DASHBOARD -----------

# Admin Dashboard - Display summary statistics
@main.route('/admin/dashboard', methods=["GET", "POST"])
@login_required
def admin_dashboard():
    username = current_user.name  # Get the current admin's username
    # Fetch data for dashboard statistics
    news_cards = New_Card.query.all()
    count_user = count_entries()
    count_categories = ToolCategories.query.count()
    count_news = New_Card.query.count()
    count_tools = Tool_Cards.query.count()
    return render_template(
        'admin-dashboard.html',
        news_cards=news_cards,
        username=username,
        title="Dashboard | EBT-Backpack",
        count_user=count_user,
        count_news=count_news,
        count_tools=count_tools,
        count_categories=count_categories
    )

# ----------- TOOL MANAGEMENT -----------

# View All Tools
@main.route('/tools-complete')
def tools_complete():
    tools = Tool_Cards.query.all()  # Fetch all tool cards
    return render_template('alle_tools.html', tools=tools)

# Resistance Calculator Tool
@main.route("/tools/resistance-calculator", methods=["GET", "POST"])
def resistance_calculator():
    form = ResistorForm()  # Instantiate the resistor form
    voltage_text = "Spannung"
    current_text = "Stromstärke"
    if form.validate_on_submit():  # Validate the submitted form
        try:
            # Convert input values to floats
            voltage = float(form.Voltage.data)
            current = float(form.Current.data)
            # Calculate resistance
            result = ResistanceCalculating.ResistanceCalculatorSingle(voltage, current)
            return render_template('widerstandsrechner.html', form=form, result=result, voltage_text=voltage_text, current_text=current_text)
        except ValueError:
            flash("Alle Werte müssen Zahlen sein und in der korrekten Form angegeben werden! (e.g. 0,1 = 0.1)", 'danger')
        except ZeroDivisionError:
            flash("Werte dürfen nicht null sein! (Illegale Mathematische Operation!)", 'danger')
    return render_template('widerstandsrechner.html', form=form, voltage_text=voltage_text, current_text=current_text)


# Total Resistance Calculator Tool
@main.route("/tools/total-resistance-calculator", methods=["GET", "POST"])
def total_resistance_calculator():
    if request.method == "POST":
        resistorlist = request.form.getlist('resistors[]')
        for entry in resistorlist:
            if entry == "":
                resistorlist.remove(entry)
            else:
                pass
        try:
            calculator=ResistanceCalculating()
            formatted_resistorlist = list(map(float, resistorlist))
            total_resistance = calculator.total_resistance_parallel(formatted_resistorlist)
            return render_template('total_resistance_calculator.html', total_resistance=total_resistance) 
        except ZeroDivisionError:
            flash("Werte dürfen nicht null sein! (Illegale Mathematische Operation!)", 'danger')
            
    return render_template('total_resistance_calculator.html')

# View Tools Specific to Resistance Calculators
@main.route("/tools-complete/resistance-calculators")
def resistance_calculators():
    tools = Tool_Cards.query.filter_by(category=0).all()  # Fetch resistance calculator tools
    if tools:
        return render_template("wiederstands_tools.html", tools=tools)

# ----------- KNOWLEDGE BASE -----------

# View All Knowledge Base Entries
@main.route("/knowledgebase", methods=["GET", "POST"])
def knowledgebase():
    # Fetch all knowledge base items from the database
    knowledgebase_items = KnowledgeBaseItems.query.all()
    # Instantiate the search form
    form = Searching_Bar()
    # Check if the form is submitted
    if request.method == "POST":
        # Check if the search field is not empty
        print(form.searchField.data)
        if form.searchField.data != "":
            # Fetch the search query
            search = form.searchField.data
            # Filter the knowledge base items by the search query
            knowledgebase_items = KnowledgeBaseItems.query.filter(KnowledgeBaseItems.title.contains(search) | KnowledgeBaseItems.content.contains(search) | KnowledgeBaseItems.author.contains(search) | KnowledgeBaseItems.date_of_creation.contains(search)).all()
            # Return the search results
            return render_template("knowledgebase.html", items=knowledgebase_items, chars_to_show=knowledgebase_items_charstoshow, form=form)
        # If the search field is empty, return all knowledge base items
        else:
            # Fetch all knowledge base items
            knowledgebase_items = KnowledgeBaseItems.query.all()
            # Return all knowledge base items
            return render_template("knowledgebase.html", items=knowledgebase_items, chars_to_show=knowledgebase_items_charstoshow, form=form)
    return render_template("knowledgebase.html", items=knowledgebase_items, chars_to_show=knowledgebase_items_charstoshow, form=form)

# View a Single Knowledge Base Entry
@main.route("/knowledgebase/entry/<int:entry_id>")
def knowledgebase_entry(entry_id):
    # Fetch the knowledge base entry and file by ID
    entry = KnowledgeBaseItems.query.get_or_404(entry_id)
    file = fileUploads.query.get_or_404(entry_id)
    filename = file.filename
    formatted_content = entry.content.replace("\r\n", "<br>").replace("\r", "<br>").replace("\n", "<br>")
    formatted_text = formatted_content.replace(" ", "&nbsp;")  # Optional: Für Beibehaltung von Leerzeichen
    return render_template("knowledgebase_entry_view.html", entry=entry, filename=filename, formatted_text=formatted_content)

# Create a New Knowledge Base Entry
@main.route('/knowledgebase/entry/new', methods=["GET", "POST"])
def knowledgebase_new():
    form = New_Knowledgebase_Entry()  # Instantiate the knowledge base form
    if (form.validate_on_submit()) or (request.method == "POST"):  # Validate the submitted form
        # Handle optional image path
        if form.imagepath.data == "":
            form.imagepathbool.data = False
        else:
            form.imagepathbool.data = True

        # Create a new knowledge base entry
        new_know_entry = KnowledgeBaseItems(
            title=form.title.data,
            content=form.content.data,
            author=form.author.data,
            imagepath=form.imagepath.data,
            imagepathbool=form.imagepathbool.data,
            date_of_creation=form.date_of_creation.data
        )
        file = request.files['file']
        upload = fileUploads(filename=file.filename, data=file.read())
        db.session.add(upload) # Add uploaded files to database
        db.session.add(new_know_entry)  # Add the new entry to the database
        db.session.commit()  # Save the changes
        return redirect(url_for('main.knowledgebase'))  # Redirect to the knowledge base page
    return render_template('new_knowledgebase_entry.html', form=form)

# Delete a Knowledge Base Entry
@main.route('/knowledgebase/entry/delete/<int:id>')
def delete_know_entry(id):
    # Fetch the entry and file by ID
    entry = KnowledgeBaseItems.query.get_or_404(id)
    file = fileUploads.query.get_or_404(id)
    db.session.delete(entry)  # Delete the entry
    db.session.delete(file)   # Delete the file
    db.session.commit()  # Save the changes
    return redirect(url_for('main.knowledgebase'))

# Edit a Knowledge Base Entry
@main.route('/knowledgebase/entry/edit/<int:id>', methods=["GET", "POST"])
def edit_know_entry(id):
    entry = KnowledgeBaseItems.query.get_or_404(id)  # Fetch the entry by ID
    file = fileUploads.query.get_or_404(id) # Fetch the file by ID
    filename = file.filename
    form = New_Knowledgebase_Entry(obj=entry)  # Prepopulate the form with entry data
    if form.validate_on_submit():  # Validate the submitted form
        # Update the entry fields with the form data
        file_new = request.files['file']
        entry.title = form.title.data
        entry.content = form.content.data
        entry.author = form.author.data
        entry.imagepath = form.imagepath.data
        entry.imagepathbool = form.imagepathbool.data
        entry.date_of_creation = form.date_of_creation.data
        file.filename = file_new.filename
        file.data = file_new.read()
        db.session.commit()  # Save the changes
        return redirect(url_for("main.knowledgebase"))  # Redirect to the knowledge base page
    return render_template("edit_know_entry.html", form=form, file=file, id=id, filename=filename)

# ----------- FILE DOWNLOAD -----------
@main.route('/download/<upload_id>')
def download(upload_id):
    upload = fileUploads.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True )