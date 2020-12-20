from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, equal_to, NumberRange


class FormularioLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message="Nombre de usuario requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida")])
    enviar = SubmitField('Iniciar Sesión')


class FormularioRegistrarUsuario(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message="Nombre de usuario requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida")])
    confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Contraseña requerida"), equal_to('password', message='Password no coincide.')])
    rol = StringField('Rol', validators=[DataRequired(message="Contraseña requerida")])
    email = StringField('email', validators=[DataRequired(message="Contraseña requerida")])
    enviar = SubmitField('Agregar')


class FormularioEditarProducto(FlaskForm):
    ref = StringField('Referencia', validators=[DataRequired(message="Referencia requerida")])
    nombre = StringField('Nombre del Producto', validators=[DataRequired(message="Nombre requerido")])
    precio = IntegerField('Precio', validators=[NumberRange(min=0, message="Debe ser mayor o igual a cero")])
    cantidad = IntegerField('Cantidad', validators=[NumberRange(min=0, message="Debe ser mayor o igual a cero")])
    imagen = StringField('Imagen')
    enviar = SubmitField('Agregar')
