from werkzeug import security
from systemdb import sql_connection


def db_listar_usuarios():
    strsql = "SELECT * FROM usuarios;"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql)
    usuarios = cursor.fetchall()
    con.close()
    return usuarios


def db_usuario_by_username(username):
    strsql = "SELECT * FROM usuarios WHERE username = ?"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, [username])
    usuario = cursor.fetchone()
    con.close()
    return usuario


def db_agregar_usuario(username, password, email, rol):
    strsql = "INSERT INTO usuarios ('username', 'password', 'email', 'rol') VALUES (?, ?, ?, ?)"
    con = sql_connection()
    cursor = con.cursor()
    password_hash = security.generate_password_hash(password)
    cursor.execute(strsql, [username, password_hash, email, rol])
    con.commit()
    con.close()

