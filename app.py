from flask import Flask
from flask import render_template, url_for

app = Flask(__name__, template_folder="front-end")

@app.route("/")
def home():
    return render_template('menu-general.html')

@app.route("/login")
def home1():    
    return "Hola mundo!"

@app.route("/crearproducto")
def crearproducto():
    return "Hola mundo!"

@app.route("/modificarproducto")
def modificarproducto():
    return "Hola mundo!"

@app.route("/eliminarproducto")
def eliminarproducto():
    return "Hola mundo!"

@app.route("/registrarusuario")
def registrarusuario():
    return "Hola mundo!"

@app.route("/actualizarinventario")
def actualizarinventario():
    return "Hola mundo!"

if __name__ == "__main__":
    app.run(debug=True)