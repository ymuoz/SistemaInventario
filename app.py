from flask import Flask
from flask import render_template, url_for

app = Flask(__name__, template_folder="front-end")

@app.route("/")
def home():
    return render_template('menu-general.html')

@app.route("/login")
def login():    
    return render_template('login-adm.html')

@app.route("/crearproducto")
def crearproducto():
    return render_template('crear-producto.html')

@app.route("/modificarproducto")
def modificarproducto():
    return render_template('crear-producto.html')

@app.route("/eliminarproducto")
def eliminarproducto():
    return render_template('crear-producto.html')

@app.route("/registrarusuario")
def registrarusuario():
    return render_template('registrar_usuario.html')

@app.route("/actualizarinventario")
def actualizarinventario():
    return render_template('actualizar-inventario.html')

@app.route("/buscarproducto")
def buscarproducto():
    return render_template('buscar-producto.html')

if __name__ == "__main__":
    app.run(debug=True)