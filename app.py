from flask import Flask
# 1ª linha ta importando o Flask - que e um framework.
# variavel para guardar o arquivo
app = Flask(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Hello World"