from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError

class CadastroForm(FlaskForm):
    usuario = StringField(
        label="Nome do Usuário:", 
        validators=[
            Length(
                min=2, 
                max=100
            ),
            DataRequired()
        ])
    email = EmailField(
        label="E-mail:",
        validators=[
            Email(),
            DataRequired()
        ]
        )
    senha = PasswordField(
        label="Senha:",
        validators=[
            Length(min=6),
            DataRequired()
        ])
    cnfsenha = PasswordField(
        label="Confirme a senha:",
        validators=[
            EqualTo('senha'),
            DataRequired()
        ])
    submit = SubmitField(
        label="Cadastrar"
        )
    
class LoginForm(FlaskForm):
    usuario = StringField(label="Nome do Usuário:", validators=[DataRequired()])
    senha = PasswordField(label="Senha:",validators=[DataRequired()])
    submit = SubmitField(label="Login")