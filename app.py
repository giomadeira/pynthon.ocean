import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash


#configuraçao 
DATABASE = "blog.db"
SECRET_KEY = 'pudim'

# variavel para guardar o arquivo
app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])



@app.route('/hello')
def pagina_inicial():
    return "Hello World"