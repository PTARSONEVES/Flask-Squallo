from app import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=10), nullable=False, unique=True)
    email = db.Column(db.String(length=255), nullable=False, unique=True)
    email_verified_at = db.Column(db.DateTime, nullable=True)
    senha = db.Column(db.String(length=60), nullable=False, unique=True)
    remember_token = db.Column(db.String(length=100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)


    @property
    def senhacrip(self):
        return self.senhacrip

    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8')

    def converte_senha(self, senha_texto_claro):
        return bcrypt.check_password_hash(self.senha, senha_texto_claro)


