from flask import Flask, render_template, url_for, flash, redirect, session, request
from systemdb import init_db
from forms import FormularioLogin, FormularioRegistrarUsuario, FormularioBuscarProducto, FormularioAgregarProducto
from werkzeug import security
from usuarios_service import db_usuario_by_username, db_agregar_usuario
from productos_service import db_producto_by_ref, db_agregar_producto, db_producto_by_text, db_listar_productos, db_editar_producto, db_eliminar_producto

app = Flask(__name__)
init_db()
app.config.update(SECRET_KEY="GRUPO3-R")

rutas_admin = [
    ["/", "Inicio"],
    ["/registrar_usuario", "Registrar Usuario"],
    ["/agregar_producto", "Agregar Producto"],
    ["/buscar_producto", "Editar Producto"],
    ["/buscar_producto", "Eliminar Producto"],
    ["/buscar_producto", "Buscar Producto"],
    ["/logout", "Salir"]
]
rutas_vendedor = [
    ["/", "Inicio"],
    ["/buscar_producto", "Actualizar Inventario"],
    ["/buscar_producto", "Buscar Producto"],
    ["/logout", "Salir"]
]
rutas_no_user = [["/login", "Login"]]


@app.route("/")
def index():
    if "rol" in session:
        rol = session["rol"]
        if rol == "admin":
            session["rutas"] = rutas_admin
        else:
            session["rutas"] = rutas_vendedor
    else:
        session["rutas"] = rutas_no_user
    return render_template("index.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if "rol" in session:
        return redirect(url_for("index"))

    form = FormularioLogin()

    if form.validate_on_submit():
        username = form.usuario.data
        password = form.password.data
        usuariodb = db_usuario_by_username(username)
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
    if "rol" in session:
        session.pop("rol", None)
        session["rutas"] = rutas_no_user
        return redirect(url_for("index"))
    return redirect(url_for("login"))


@app.route("/registrar_usuario", methods=("GET", "POST"))
def registrar_usuario():
    if "rol" not in session:
        return redirect(url_for("login"))
    else:
        rol = session["rol"]
        if rol != "admin":
            flash("Error.  No está autorizado para realizar el registro de usuarios.")
            return redirect(url_for("index"))

    form = FormularioRegistrarUsuario()

    if form.validate_on_submit():
        username = form.usuario.data
        password = form.password.data
        confirm = form.confirm.data
        email = form.email.data
        rol = form.rol.data
        usuariodb = db_usuario_by_username(username)
        if usuariodb is None:
            db_agregar_usuario(username, password, email, rol)
            flash("Usuario agregado con éxito.")
        else:
            flash("Usuario ya existe.  No se puede agregar un duplicado.")

    return render_template("registrar_usuario.html", form=form)


@app.route("/agregar_producto", methods=("GET", "POST"))
def agregar_producto():
    if "rol" not in session:
        return redirect(url_for("login"))
    else:
        rol = session["rol"]
        if rol != "admin":
            flash("Error.  No está autorizado para agregar un producto.")
            return redirect(url_for("index"))

    form = FormularioAgregarProducto()

    if form.validate_on_submit():
        ref = form.ref.data
        nombre = form.nombre.data
        precio = form.precio.data
        cantidad = form.cantidad.data
        imagen = form.imagen.data

        productodb = db_producto_by_ref(ref)
        if productodb is None:
            db_agregar_producto(ref, nombre, precio, cantidad, imagen)
            flash("Producto agregado con éxito.")
        else:
            flash("Producto ya existe.  No se puede agregar un duplicado.")

    return render_template("agregar_producto.html", form=form)


@app.route("/buscar_producto", methods=("GET", "POST"))
def buscar_producto():
    if "rol" not in session:
        return redirect(url_for("login"))

    form = FormularioBuscarProducto()

    if request.method == "GET":
        productosdb = db_listar_productos()
    elif form.validate_on_submit():
        palabra = form.buscar.data
        productosdb = db_producto_by_text(palabra)
        if productosdb is None:
            flash("No se encuentra ningún producto con esa palabra.")

    return render_template("buscar_producto.html", form=form, productos=productosdb)


@app.route("/editar_producto/<ref>", methods=("GET", "POST"))
def editar_producto(ref):
    if "rol" not in session:
        return redirect(url_for("login"))

    form = FormularioAgregarProducto()

    if request.method == "GET":
        productodb = db_producto_by_ref(ref)
        if productodb is None:
            flash("No existe el producto.")
        else:
            form.ref.data = productodb[0]
            form.nombre.data = productodb[1]
            form.precio.data = productodb[2]
            form.cantidad.data = productodb[3]
            form.imagen.data = productodb[4]
            return render_template("editar_producto.html", form=form)
    else:
        if form.validate_on_submit():
            ref = form.ref.data
            nombre = form.nombre.data
            precio = form.precio.data
            cantidad = form.cantidad.data
            imagen = form.imagen.data
            db_editar_producto(ref, nombre, precio, cantidad, imagen)
            flash("Producto modificado con éxito.")

    return redirect(url_for("buscar_producto"))


@app.route("/eliminar_producto/<ref>", methods=("GET", "POST"))
def eliminar_producto(ref):
    if "rol" not in session:
        return redirect(url_for("login"))
    else:
        rol = session["rol"]
        if rol != "admin":
            flash("Error.  No está autorizado para eliminar un producto.")
            return redirect(url_for("buscar_producto"))

    productodb = db_producto_by_ref(ref)
    if productodb is None:
        flash("No existe el producto.")
    else:
        db_eliminar_producto(ref)
        flash("Producto eliminado con éxito.")

    return redirect(url_for("buscar_producto"))


if __name__ == '__main__':
    app.run(debug=True)
