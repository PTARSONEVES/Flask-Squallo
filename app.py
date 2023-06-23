
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page_home():
    return render_template('home.html',titulopagina='Home')