from flask import Flask, render_template, url_for
from scraping import raspar_insper

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

  html = """
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
  for materia in raspar_insper(headers, url_insper):
    html+= f'<li> <a href="{materia["url"]}">{materia["titulo"]}</a> </li>'
    html+= """
        </ul>
        </p>
    </body>
    </html>
    """
    return html