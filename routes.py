from app import app, db, bcrypt
from flask import render_template, request, redirect, url_for, flash
from database import cadastra_usuario, obtem_usuario
from forms import CadastroForm, LoginForm
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from ftoken import gera_token, confirma_token



@app.route("/")
def page_home():
    return render_template('home.html',titulopagina='Home',idpage='homepage')

@app.route("/cadastro",methods=['GET','POST'])
def page_cadastro():
    form=CadastroForm(request.form)
    if form.validate_on_submit():
        data_atual = datetime.now()
        usuario = form.usuario.data
        email = form.email.data
        senha_ini = form.senha.data
        senha = bcrypt.generate_password_hash(senha_ini).decode('utf-8')
        criacao = str(data_atual.strftime("%Y-%m-%d %H-%M-%S"))
        cadastra_usuario(usuario,email,senha,criacao)
        token = gera_token(email)
        print('TOKEN: ',token)
        confirma_url = url_for() ('confirma_email',token=token,_external=True)
        print('URL GERADA: ',confirma_url)
        html = render_template('includes/ativa_cadastro.html',confirma_url=confirma.url)
        subject="Por favor, confirme seu e-mail"
        send_email(email,subject,html)

        login_user()

        flash('Um link de confirmação foi enviado para o seu e-mail','success')
        print(token)
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            print(f"Erro ao cadastrar usuário {err}")
    return render_template('cadastro.html',titulopagina='Cadastro de Usuário',idpage='cadusu',form=form)

@app.route("/confirma/<token>")
@login_required
def confirma_email(token):
    try:
        email = confirma_token(token)
    except:
        flash('O link enviado é inválido ou está expirado.','danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Conta já confirmada. Por favor, fça seu login!','success')
    else: 
        user.email_verified_at = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Sua conta já está confirmada. Obrigado!!!','success')
    return redirect(url_for('page_home'))



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

@app.route("/logout")
@login_required
def page_logout():
    logout_user()
    return redirect(url_for('page_home'))