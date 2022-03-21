# inicializar a imagem base (Alpine é uma pequena distro Linux, ocupa muito pouco espaço)
FROM python:3.9.7
# definir o atual diretório de trabalho
WORKDIR /docker-flask-test
# copiar o conteudo para o diretório de trabalho
ADD . /docker-flask-test/
# rodar pip para instalar as dependencias do aplicativo flask
RUN pip install -r requirements.txt
# definir o comando para inicializar o container
CMD ["python", "main.py"]
