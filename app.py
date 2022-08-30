from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Hola mundo! Los saludo cordialmente desde Flask'


@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Adios {nombre}! Me despido cordialmente desde Flask'

@app.route('/edad/<int:edad>')
def anios(edad):
    return f'Hola! Tu edad es {edad} anios'