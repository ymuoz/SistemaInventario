from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder="front-end")

@app.route("/")
def home():
    return render_template('menu-general.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['userid']
        password = request.form['password']
        if username != 'admin' or password != 'secret':
            error = 'usuario y/o password inválidos.'
        else:
            return redirect(url_for('home'))

    return render_template('login_adm.html', error=error)

@app.route("/crearproducto", methods=['GET', 'POST'])
def crearproducto():
    error = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        ref = request.form['ref']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        if nombre == '' or ref == '' or cantidad == '' or precio=='':
            error = 'datos no válidos.'
        else:
            return redirect(url_for('home'))

    return render_template('crear-producto.html', error=error)

@app.route("/modificarproducto", methods=['GET', 'POST'])
def modificarproducto():
    return render_template('crear-producto.html')

@app.route("/eliminarproducto", methods=['GET', 'POST'])
def eliminarproducto():
    return render_template('crear-producto.html')

@app.route("/registrarusuario", methods=['GET', 'POST'])
def registrarusuario():
    return render_template('registrar_usuario.html')

@app.route("/actualizarinventario", methods=['GET', 'POST'])
def actualizarinventario():
    return render_template('actualizar-inventario.html')

@app.route("/buscarproducto", methods=['GET', 'POST'])
def buscarproducto():
    return render_template('buscar-producto.html')

if __name__ == "__main__":
    app.run(debug=True)