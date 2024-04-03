from flask import Flask, render_template, url_for

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
