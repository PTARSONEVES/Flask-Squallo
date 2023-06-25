from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField

class CadastroForm(FlaskForm):
    usuario = StringField(label="Nome do Usuário:")
    email = EmailField(label="E-mail:")
    senha = PasswordField(label="Senha:")
    cnfsenha = PasswordField(label="Confirme a senha:")
    submit = SubmitField(label="Cadastrar")