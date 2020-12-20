from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, equal_to


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

