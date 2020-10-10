import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask , request 
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '3d9659f769b6a6363ebce31a3393c470'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

class config:
    MAIL_SERVER = os.environ.get('MAIL_SERVER' , 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT' , '587'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL' , True)
    MAIL_USERNAME= os.environ.get('EMAIL_USERNAME' , 'churchillotiende@gmail.com')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD' , 'maginevi@11055')
   
mail = Mail(app)
from flask_blog import routes