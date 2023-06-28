from app import app, db, bcrypt
from flask import render_template, request, redirect, url_for, flash
from database import cadastra_usuario, obtem_usuario
from forms import CadastroForm, LoginForm
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from models import User

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
    if form.validate_on_submit():
        usuario = form.usuario.data
        senha = form.senha.data
        usuario_logado = User.query.filter_by(usuario=usuario).first()
        if usuario_logado == None:
            return redirect(url_for('page_cadastro'))
        else:
            senha_usuario = usuario_logado.senha
            senha_confere = bcrypt.check_password_hash(senha_usuario,senha)
            if senha_confere:
                login_user(usuario_logado)
                return redirect(url_for('page_home'))
            else:
                print("Senha não confere")
#        else:
#            flash(f'Usuário e/ou senha incorreto(s)! Tente novamente.', category='danger')
    return render_template('login.html',titulopagina='Página de Login',idpage='loginpage',form=form)