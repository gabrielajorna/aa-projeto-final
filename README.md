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

## Página dinâmica

A rota "/noticias" chama uma função de WebScraping e toda vez que a página é acionada, notícias novas aparecerão. 
Para ter sua página dinâmica: 
- [ ] Crie um arquivo.py para o código de raspagem;
- [ ] Dentro do arquivo.py principal do site, chame este outro arquivo, importando a função. 

## Envio de e-mail

Ao acessar a página dinâmica, este código aciona o SMTP e envia um e-mail com todo conteúdo. Note que o e-mail de destinarário e remetende é definido dentro do app.py.
Para ter o seu envio de e-mail:
- [ ] Altere os e-mails para quem gostaria de enviar;
- [ ] Altere o conteúdo da raspagem
- [ ] Salve suas credenciais de conexão no arquivo `.env`
