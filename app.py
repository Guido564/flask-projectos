from flask import Flask, render_template, redirect, url_for, abort, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'soy_una_llave_secreta_jaja'


@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario desde la maquina: {session["username"]}'
    return 'No hay usuario desde la maquina'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

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

@app.route('/api/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)