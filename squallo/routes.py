from squallo import app, db, bcrypt
from flask import render_template, jsonify, request, redirect, url_for
from squallo.database import cadastra_usuario
from squallo.forms import CadastroForm, LoginForm
from datetime import datetime

@app.route("/")
def page_home():
    return render_template('home.html',titulopagina='Home',idpage='homepage')

@app.route("/cadastro",methods=['GET','POST'])
def page_cadastro():
    form=CadastroForm()
    if form.validate_on_submit():
        data_atual = datetime.now()
        usuario = form.usuario.data
        email = form.email.data
        senha_ini = form.senha.data
        senha = bcrypt.generate_password_hash(senha_ini).decode('utf-8')
        criacao = str(data_atual.strftime("%Y-%m-%d %H-%M-%S"))
        cadastra_usuario(usuario,email,senha,criacao)
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            print(f"Erro ao cadastrar usuário {err}")
    return render_template('cadastro.html',titulopagina='Cadastro de Usuário',idpage='cadusu',form=form)

@app.route("/login",methods=['GET','POST'])
def page_login():
    form=LoginForm()
    return render_template('login.html',titulopagina='LogIn',idpage='login',form=form)