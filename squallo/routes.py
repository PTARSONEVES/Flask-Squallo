from squallo import app, db
from flask import render_template, jsonify, request
from squallo.database import cadastra_usuario
from squallo.forms import CadastroForm

@app.route("/")
def page_home():
    return render_template('home.html',titulopagina='Home',idpage='homepage')

@app.route("/cadastro",methods=['GET','POST'])
def page_cadastro():
    form=CadastroForm()
    if form.validate_on_submit():
        print('sim')
        usuario = form.usuario.data
        email = form.email.data
        senha = form.senha.data
        cadastra_usuario(usuario=usuario,email=email,senha=senha)
    else:
        print('Não')
        print(form.usuario)
    return render_template('cadastro.html',titulopagina='Cadastro de Usuário',idpage='cadusu',form=form)