# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Fernanda" # escreva seu nome
    idade = "18" # escreva sua idade
    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai_flask():
    nome="Fernando"
    idade="49"
    return render_template('pai.html' , nome = nome , idade = idade)
# defina a rota para a página da mãe
@app.route("/mae")
def mae_flask():
    nome="Érika"
    idade="48"
    return render_template('mae.html' , nome = nome , idade = idade)
# defina a rota para a página do amigo
@app.route("/irma")
def irma_flask():
    nome="Isadora"
    idade="14"
    return render_template('amigo.html' , nome = nome , idade = idade)
# adicione outras rotas, se você quiser




# execute o arquivo
app.run(debug=True)
