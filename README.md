<h1 align="center"> Comunidade Impressionadora </h1>
<h4 align="center">Projeto desenvolvido durante curso Python Impressionador com finalidade de estudo e treinamento de desenvolvimento de Websites.</h4>

<p align="center">
<a href="#tecnologias"> Tecnologias</a> | <a href="#informacao-uso">Como Usar</a>
</p>

[View demo](#)

<p align="left"> <img src="https://komarev.com/ghpvc/?username=correaito&label=Profile%20views&color=0e75b6&style=flat" alt="correaito" /> </p>

![imagem](https://img.shields.io/badge/-Python-orange) ![imagem](https://img.shields.io/badge/-Flask-black) ![imagem](https://img.shields.io/badge/-Bootstrap-blue)  ![imagem](https://img.shields.io/badge/-HTML-red) ![imagem](https://img.shields.io/badge/-CSS-green)

<a id="tecnologias" class="anchor"></a>
### :rocket:  Tecnologias

------------
Esse projeto foi desenvolvido como um Projeto Pessoal, com as seguintes tecnologias:

- [Python](https://www.python.org/ "Heading link")
- [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Heading link")
- [Bootstrap](https://getbootstrap.com/ "Heading link")
- [Font Awesome](https://fontawesome.com/ "Heading link")

<a id="informacao-uso" class="anchor"></a>
### :information_source:  Como Usar
------------
Para clonar e executar este aplicativo, você precisará apenas clonar e abrir em seu navegador. 

Da sua linha de comando:

    # Clone este repositório
    $ git clone https://github.com/correaito/comunidade_python.git
    
    # Vá para o repositório
    $ cd comunidade_python
    
    # Instale as extensões
    $ pip install flask
    $ pip install Flask-Login
    $ pip install sqlalchemy
    $ pip install yagmail
    $ pip install bcrypt
    
 Depois, execute os comandos no terminal de seu IDE para limpar o banco de dados:
 
     # Importe o database
     $ from comunidadeimpressionadora import database
     
     # e execute o comando para limpar todas as tabelas
     $ database.drop_all()
     # e o comando criar todas as tabelas novamente
     $ database.create_all()
     
 Na linha 26 do arquivo routes, configure a conta de email do yagmail para envio de mensagens da área Contato do site:
 
    # Altere o email e senha para a conta que irá disparar os emails de contato
        if form.validate_on_submit():
        usuario = yagmail.SMTP(user='teste@gmail.com', password='123') 
        
  E na linha 30 desse mesmo arquivo, altere o destinatário das mensagens:
  
    usuario.send(to='teste@gmail.com',
     
    
Agora, para executar o script, dentro do PyCharm, abra o arquivo main.py, clique com o botão direito do mouse, e depois em "Run main.py", ou com <kbd>SHIFT</kbd> + <kbd>CTRL</kbd> + <kbd>F10</kbd>.

Ao fazer isso, o servidor do Flask será executado no terminal do próprio PyCharm e uma URL para acessá-lo será exibida

![Isso é uma imagem](https://dkrn4sk0rn31v.cloudfront.net/2019/10/14171039/2019-10-14-16-06-55-image.png)

Clicando na rota disponibilizada, o navegador padrão do computador irá abrir e executar nosso projeto.

------------
:trophy: Meu primeiro repositório, então..seja paciente. :hand_over_mouth: <br>
Feito com ♥ por Alan Garmatter. [Visite meu LinkedIn](https://www.linkedin.com/in/alan-garmatter-8a05601b8/)! 👋 
