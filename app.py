###############################################################################################################
#############################               Packages            ###############################################
###############################################################################################################

from    flask                                   import      *
from    flask_wtf                               import      FlaskForm
from    wtforms                                 import      *
from    wtforms.validators                      import      *
from    flask_bootstrap                         import      Bootstrap5
from    flask_sqlalchemy                        import      SQLAlchemy


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

###############################################################################################################
############################                Routes                #############################################
###############################################################################################################

class ResistorForm(FlaskForm):
    Voltage = IntegerField("Trage hier die Spannung [U] in Volt (V) ein.", validators=[DataRequired("Bitte gebe die Spannung ein!")])
    Current = IntegerField("Trage hier noch die Stromstärke [I] in Ampére (A) ein.")
    

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

@app.route('/admin')
def             admin_login():
    return      render_template(
                                                            'admin_login.html', 
                title                           =           "Login | EBT-Backpack")


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

###############################################################################################################
############################              Run Dialog              #############################################
###############################################################################################################
with                                             app.        app_context():
    db.                                                      create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)