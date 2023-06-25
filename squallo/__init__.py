from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://ptarsoneves:Strolandia1@database-1.cizel514jz3i.us-east-2.rds.amazonaws.com/py_squallo"
app.config["SECRET_KEY"] = '71ca79b597f1dd9c15f77b12'
db.init_app(app)
bcrypt = Bcrypt(app)
#login_manager.init_app(app)
#login_manager.login_view = "page_login"
#login_manager.login_message = "Por favor, realize seu login"
#login_manager.login_message_category = "info"

from squallo import routes