from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, equal_to, NumberRange


class FormularioLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message="Nombre de usuario requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida")])
    enviar = SubmitField('Iniciar Sesión')


class FormularioRegistrarUsuario(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message="Nombre de usuario requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida")])
    confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Contraseña requerida"), equal_to('password', message='Password no coincide.')])
    rol = SelectField('Rol', choices=[('admin', 'Administrador'), ('vendedor', 'Vendedor')],
                      validators=[DataRequired(message="Rol requerida")])
    email = StringField('email', validators=[DataRequired(message="Email requerida")])
    enviar = SubmitField('Agregar')


class FormularioAgregarProducto(FlaskForm):
    ref = StringField('Referencia', validators=[DataRequired(message="Referencia requerida")])
    nombre = StringField('Nombre del Producto', validators=[DataRequired(message="Nombre requerido")])
    precio = IntegerField('Precio', validators=[NumberRange(min=0, message="Debe ser mayor o igual a cero")])
    cantidad = IntegerField('Cantidad', validators=[NumberRange(min=0, message="Debe ser mayor o igual a cero")])
    imagen = StringField('Imagen')
    enviar = SubmitField('Grabar')


class FormularioBuscarProducto(FlaskForm):
    buscar = StringField('Palabra clave')
    enviar = SubmitField('Buscar')

