from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

CREDENCIAIS = {
    'mysql' : os.getenv('MYSQLCONECT'),
    'secret' : os.getenv('SECRET_KEY'),
    'secsalt': os.getenv('SECURITY_PASSWORD_SALT')
}


db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = CREDENCIAIS.get('mysql')
app.config["SECRET_KEY"] = CREDENCIAIS.get('secret')
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = "page_login"
login_manager.login_message = "Por favor, realize seu login"
login_manager.login_message_category = "info"

import routes, models