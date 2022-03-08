from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# Aqui vamos criar as classes responsaveis por criar as tabelas e campos no banco de dados

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.png')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(MutableList.as_mutable(PickleType), default=['Não Informado'])

    def contar_posts(self):
        return len(self.posts)

    def contar_cursos(self):
        return len(self.cursos)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

class Curso(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    curso = database.Column(database.String, nullable=False)
