from flask import Flask, render_template, redirect, url_for, abort

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

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404