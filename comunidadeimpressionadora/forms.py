from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

# esse arquivo é responsável por criar as classes dos dois formulários da pagina de login
# aqui definimos os campos dos formulários, e suas respectivas especificidades, como, por exemplo
# se o campo é obrigatório, quantos caracteres minimos vai aceitar, se é um campo de email, senha, etc..

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired('Preencha esse campo')])
    email = StringField('E-mail', validators=[DataRequired('Preencha esse campo'), Email('Endereço de email inválido')])
    senha = PasswordField('Senha', validators=[DataRequired('Preencha esse campo'), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired('Preencha esse campo'), EqualTo('senha', 'Deve ser idêntico ao campo Senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    # aqui iniciamos a funcao com a designação "validade_", para que a funcao validate_on_submit() no arquivo
    # routes possa rodar esse metodo para verificar se esse email já existe no banco de dados

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro email ou faça login para continuar')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired('Preencha esse campo'), Email('Endereço de email inválido')])
    senha = PasswordField('Senha', validators=[DataRequired('Preencha esse campo'), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired('Preencha esse campo')])
    email = StringField('E-mail', validators=[DataRequired('Preencha esse campo'), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail.')


# Formulário de Posts
class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired('Preencha esse campo'), Length(2,140)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired('Preencha esse campo')])
    botao_submit = SubmitField('Criar Post')

# Formulário de contato
class FormContato(FlaskForm):
    assunto = StringField('Assunto', validators=[DataRequired('Preencha esse campo'), Length(10,100)])
    texto = TextAreaField('Texto da mensagem', validators=[DataRequired('Preencha esse campo')])
    botao_submit = SubmitField('Enviar mensagem')