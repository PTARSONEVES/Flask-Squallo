from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://ptarsoneves:Strolandia1@database-1.cizel514jz3i.us-east-2.rds.amazonaws.com/py_squallo"
#app.config["SECRET_KEY"] = 'ab7754702a1328315b9c1864'
db.init_app(app)
bcrypt = Bcrypt(app)
#login_manager.init_app(app)
#login_manager.login_view = "page_login"
#login_manager.login_message = "Por favor, realize seu login"
#login_manager.login_message_category = "info"


@app.route("/")
def page_home():
    return render_template('home.html',titulopagina='Home')