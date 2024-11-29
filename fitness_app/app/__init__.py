from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    imcs = db.relationship('IMC', backref='user', lazy=True)
    aguas = db.relationship('Agua', backref='user', lazy=True)
    calorias = db.relationship('Calorias', backref='user', lazy=True)


# Histórico de IMC
class IMC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imc = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "imc": self.imc,
            "data": self.data.strftime('%Y-%m-%d %H:%M:%S'),  # Formatar datetime como string
            "user_id": self.user_id,
        }


# Histórico de Água Diária
class Agua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agua_diaria = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "agua_diaria": self.agua_diaria,
            "data": self.data.strftime('%Y-%m-%d %H:%M:%S'),  # Formatar datetime como string
            "user_id": self.user_id,
        }


# Histórico de Gasto Calórico
class Calorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gasto_calorico = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "gasto_calorico": self.gasto_calorico,
            "data": self.data.strftime('%Y-%m-%d %H:%M:%S'),  # Formatar datetime como string
            "user_id": self.user_id,
        }


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Register") 

    def validate_username(self, username):
        existing_user_username  = User.query.filter_by(username=username.data).first()

        if existing_user_username:
            raise ValidationError("Esse nome de usuário já existe. Escolha um diferente")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login") 


@login_manager.unauthorized_handler
def unauthorized():
    # Adiciona uma mensagem de aviso
    flash("Você precisa estar logado para acessar esta funcionalidade.")
    # Redireciona para a página de login
    return redirect(url_for('main.login'))





def create_app():
    app = Flask(__name__)

    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SECRET_KEY'] = 'fitnessappkeydatabase'
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    # app.config.from_object('config.Config')

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app