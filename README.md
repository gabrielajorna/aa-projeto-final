# Meu site no ar
Neste repositório você pode conferir o conteúdo do Trabalho Final da Disciplina "Algoritmos de Automação" do Master em Jornalismo de Dados, Automação e Data Storytelling do Insper que contém:

- Site em Flask
- Página dinâmica com Web Scraping
- Integração com envio de e-mail 

## Para replicar este projeto: 

- Faça uma conta no Render.com para subir o seu site online;
- Faça uma conta no Brevo.com para usar o servidor de envio de e-mails automatizado;
- Construa suas páginas em HTML (use CSS para modificar o front-end se preferir);

Utilize o template de construção de site:

```
from flask import Flask, render_template
gunicorn

app=Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')
```
Obs: Para cada arquivo HTML criado, é necessário criar um @app.route com o nome dessa página, bem como devemos chamar o `return`dela

## Continue com:

## Próximos passos
- [ ] Implementar Web scraping
- [ ] Implementar envio de emails
