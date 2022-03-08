from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# esse aquivo é responsável por criar o aplicativo através do Flasks

app = Flask(__name__)
# configurar o banco de dado
app.config['SECRET_KEY'] = '51590b44fc921eafa09854fca59207f6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# aqui iremos instanciar o gerenciador de login do nosso app
login_manager = LoginManager(app)
# a pagina que será redirecionado quando o usuario nao estiver autenticado
login_manager.login_view = 'login'
#mensagem que irá aparecer quando a pagina estiver bloqueada
login_manager.login_message = "Sem login, sem chance!"
login_manager.login_message_category = 'alert-danger'

# e por fim, importar o arquivo de rotas
from comunidadeimpressionadora import routes
