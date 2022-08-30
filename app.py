from flask import Flask, render_template, redirect, url_for

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

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))