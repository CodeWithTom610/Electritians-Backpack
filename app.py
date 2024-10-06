###############################################################################################################
#############################               Packages            ###############################################
###############################################################################################################

from    flask                                   import      *
from    flask_wtf                               import      FlaskForm
from    wtforms                                 import      StringField,PasswordField,IntegerField, BooleanField, SubmitField
from    wtforms.validators                      import      DataRequired
from    flask_bootstrap                         import      Bootstrap5
from    flask_sqlalchemy                        import      SQLAlchemy
from    flask_login                             import      *
from    flask_bcrypt                            import      *


###############################################################################################################
#############################            Configuration           ##############################################
###############################################################################################################

#   Initialize Flask App        ###############################################################################
app                                             =           Flask(__name__, static_url_path='/static')

#   Initialize Bootstrap App    ###############################################################################
bootstrap                                       =           Bootstrap5(app)


#   Configure Flask App         ##############################################################################

app.config["SECRET_KEY"]                        =           "7cd870fd19e3899b23e0eaafb97e094494b91d9957815a1"
app.config["SQLALCHEMY_DATABASE_URI"]           =           "sqlite:///database.db"

#   Initialize Database         ##############################################################################
db                                              =           SQLAlchemy()
db.                                             init_app    (app)

#   Initialize Flask Login      ##############################################################################
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "admin_login"
@login_manager.user_loader
def load_user(user_id):
    return Admin_User.query.filter_by(id=user_id).first()

#   Initialize Bcrypt           #############################################################################
bcrypt = Bcrypt(app)
def hash_password(plain_password: str):
    pw_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')
    return pw_hash

def check_password(plain_password:str, password_hash:any):
    checked_pw = bcrypt.check_password_hash(password_hash, plain_password) # returns True
    return checked_pw

###############################################################################################################
############################                Routes                #############################################
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

    

###############################################################################################################
############################                Routes                #############################################
###############################################################################################################

@app.route('/')
def             news():
    news                                        =           New_Card.query.all()
    return      render_template(
                                                            'index.html',
                title                           =           "Home | EBT-Backpack",
                news                            =           news)

@app.route('/tools-complete')
def             tools_complete():
    return      render_template(
                                                            'alle_tools.html',
                title                           =           "Alle Tools | EBT-Backpack")

@app.route('/admin/dashboard', methods=["GET", "POST"])
@login_required
def admin_dashboard():
    form = LogoutForm()
    if form.validate_on_submit():
        logout_user()

    return render_template('admin-dashboard.html', form = form)

@app.route('/admin', methods=["GET", "POST"])
def             admin_login():
    form                                        =           LoginForm()
    if                                          form.       validate_on_submit():
        user                                    =           Admin_User.query.filter_by(username=form.username.data).first()
        user_password = user.password
        checked_pw = check_password(form.password.data, user_password)
        if  user          and     checked_pw:
            
            login_user(user, remember=form.remember.data)
            return redirect(url_for("admin_dashboard")) 
    return      render_template(
                                                            'admin_login.html', 
                title                           =           "Login | EBT-Backpack",
                form                            =           form)


###############################################################################################################
############################           Database Models         ################################################
###############################################################################################################

class New_Card                                              (db.Model):
    __tablename__                               =           "NewsCards"
    id                                          =            db.Column(
                                                             db.Integer,
                                                             primary_key   =   True)
    header                                      =            db.Column(
                                                             db.String,
                                                             unique=True,
                                                             nullable=False)
    content                                     =            db.Column(
                                                             db.String)
    author                                      =            db.Column(
                                                             db.String)
    imagepath                                   =            db.Column(
                                                             db.String)
    
class Admin_User                                           (db.Model, UserMixin):
    __tablename__                               =           "Admin_Users"
    id                                          =            db.Column(
                                                             db.Integer,
                                                             primary_key    =   True)
    username                                    =            db.Column(
                                                             db.String,
                                                             unique=True,
                                                             nullable=False)
    password                                    =            db.Column(
                                                             db.String,
                                                             nullable=False)

###############################################################################################################
############################              Run Dialog              #############################################
###############################################################################################################
with                                             app.        app_context():
    db.                                                      create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
