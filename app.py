from flask import Flask, render_template, url_for, flash, redirect, session
from systemdb import init_db
from forms import FormularioLogin, FormularioRegistrarUsuario, FormularioEditarProducto
from werkzeug import security
from usuarios_service import db_usuario_by_username, db_agregar_usuario
from productos_service import db_producto_by_ref, db_agregar_producto

app = Flask(__name__)
init_db()
app.config.update(SECRET_KEY="GRUPO3-R")

rutas_admin = [
    ["/", "Inicio"],
    ["/registrar_usuario", "Registrar Usuario"],
    ["/agregar_producto", "Agregar Producto"],
    ["/logout", "Salir"]
]
rutas_vendedor = [
    ["/", "Inicio"],
    ["/actualizar_inventario", "Actualizar Inventario"],
    ["/buscar_producto", "Buscar Producto"],
    ["/logout", "Salir"]
]
rutas_no_user = [["/login", "Login"]]


@app.route("/")
def index():
    if ("rol" in session):
        rol = session["rol"]
        if (rol == "admin"):
            session["rutas"] = rutas_admin
        else:
            session["rutas"] = rutas_vendedor
    else:
        session["rutas"] = rutas_no_user
    return render_template("index.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if ("rol" in session):
        return redirect(url_for("index"))

    form = FormularioLogin()

    if form.validate_on_submit():
        username = form.usuario.data
        password = form.password.data
        usuariodb = usuario_by_username(username)
        if (usuariodb is not None) and (security.check_password_hash(usuariodb[1], password)):
            session["rol"] = usuariodb[3]
            session["rutas"] = rutas_admin
            return redirect(url_for("index"))
        else:
            session["rutas"] = rutas_no_user
            flash("Usuario o contraseña incorrectos")

    return render_template("login.html", form=form)


@app.route("/logout", methods=("GET", "POST"))
def logout():
    if ("rol" in session):
        session.pop("rol", None)
        session["rutas"] = rutas_no_user
        return redirect(url_for("index"))
    return redirect(url_for("login"))


@app.route("/registrar_usuario", methods=("GET", "POST"))
def registrar_usuario():
    if ("rol" not in session):
        return redirect(url_for("login"))
    else:
        rol = session["rol"]
        if (rol != "admin"):
            flash("Error.  No está autorizado para realizar el registro de usuarios.")
            return redirect(url_for("index"))

    form = FormularioRegistrarUsuario()

    if form.validate_on_submit():
        username = form.usuario.data
        password = form.password.data
        confirm = form.confirm.data
        email = form.email.data
        rol = form.rol.data
        usuariodb = usuario_by_username(username)
        if (usuariodb is None):
            agregar_usuario(username, password, email, rol)
            flash("Usuario agregado con éxito.")
        else:
            flash("Usuario ya existe.  No se puede agregar un duplicado.")

    return render_template("registrar_usuario.html", form=form)


@app.route("/agregar_producto", methods=("GET", "POST"))
def agregar_producto():
    if ("rol" not in session):
        return redirect(url_for("login"))
    else:
        rol = session["rol"]
        if (rol != "admin"):
            flash("Error.  No está autorizado para agregar un producto.")
            return redirect(url_for("index"))

    form = FormularioEditarProducto()

    if form.validate_on_submit():
        ref = form.ref.data
        nombre = form.nombre.data
        precio = form.precio.data
        cantidad = form.cantidad.data
        imagen = form.imagen.data

        productodb = db_producto_by_ref(ref)
        if (productodb is None):
            db_agregar_producto(ref, nombre, precio, cantidad, imagen)
            flash("Producto agregado con éxito.")
        else:
            flash("Producto ya existe.  No se puede agregar un duplicado.")

    return render_template("agregar_producto.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
