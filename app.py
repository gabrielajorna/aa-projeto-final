from flask import Flask, render_template, url_for
from scraping import raspar_insper
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()
import os

app=Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/sobremim")
def sobremim():
  return render_template('sobremim.html')
  
@app.route("/portfolio")
def portfolio():
  return render_template('portfolio.html')

@app.route("/contato")
def contato():
  return render_template('contato.html')

@app.route("/noticias")
def noticias():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    url_insper = "https://www.insper.edu.br/imprensa/"

    html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Conheça o Insper</title>
</head>
<body>
    <h1>Conheça o Insper</h1>
    <p>
    Conheça as iniciativas do Insper, instituição em que estou me formando Jornalista de Dados:
    <ul>
"""
    # Aqui você pode adicionar os itens raspatos na lista <ul> do HTML
    for materia in raspar_insper(headers, url_insper):
        html_template += f'<li> <a href="{materia["url"]}">{materia["titulo"]}</a> </li>'

    html_template += """
    </ul>
    </p>
</body>
</html>
"""

    smtp_server = "smtp-relay.brevo.com"
    port = 587
    email = os.environ['EMAIL']
    password = os.environ['PASS'] 
    remetente = "gabrielajorna@gmail.com"  
    destinatarios = ["gabrielajorna@gmail.com","alvarojusten@gmail.com"] 
    titulo = "Conheça o Insper"
    texto = html_template
  
    server = smtplib.SMTP(smtp_server, port)  # Inicia a conexão com o servidor
    server.starttls()  # Altera a comunicação para utilizar criptografia
    server.login(email, password)  # Autentica

    # Preparando o objeto da mensagem
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = ",".join(destinatarios)
    mensagem["Subject"] = titulo
    conteudo_html = MIMEText(html_template, "html")  # Adiciona a versão em HTML
    mensagem.attach(conteudo_html)

    # Envio do email
    server.sendmail(remetente, destinatarios, mensagem.as_string())

    return html_template