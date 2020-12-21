from systemdb import sql_connection


def db_listar_productos():
    strsql = "SELECT ref, nombre, precio, cantidad, imagen FROM productos;"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql)
    productos = cursor.fetchall()
    con.close()
    return productos


def db_producto_by_ref(referencia):
    strsql = "SELECT ref, nombre, precio, cantidad, imagen FROM productos WHERE ref = ?"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, [referencia])
    producto = cursor.fetchone()
    con.close()
    return producto


def db_agregar_producto(referencia, nombre, precio, cantidad, imagen):
    strsql = "INSERT INTO productos ('ref', 'nombre', 'precio', 'cantidad', 'imagen') VALUES (?, ?, ?, ?, ?)"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, [referencia, nombre, precio, cantidad, imagen])
    con.commit()
    con.close()


def db_editar_producto(referencia, nombre, precio, cantidad, imagen):
    strsql = "UPDATE productos SET nombre = ?, precio = ?, cantidad = ?, imagen = ? WHERE ref = ?"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, [nombre, precio, cantidad, imagen, referencia])
    con.commit()
    con.close()


def db_eliminar_producto(referencia):
    strsql = "DELETE FROM productos WHERE ref = ?"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, [referencia])
    con.commit()
    con.close()


def db_producto_by_text(text):
    strsql = "SELECT ref, nombre, precio, cantidad, imagen FROM productos WHERE nombre like ?"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, ["%" + text + "%"])
    productos = cursor.fetchall()
    con.close()
    return productos

