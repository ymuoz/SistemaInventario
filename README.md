# Sistema de inventarios para tienda de accesorios  

# Problemática del cliente

Actualmente nuestra problemática consiste en que no es fácil y rápido contar con el estado de real del inventario de la tienda en un momento dado, lo cual genera inconformidad con nuestros clientes porque al llegar a comprar no sabemos si tenemos unidades suficientes, lo cual genera una mala imagen de nuestra misión como empresa.

# Requerimientos

Requerimos de una aplicación web que nos permita realizar la gestión del inventario de accesorios de nuestra tienda y así conocer, en cualquier momento, el stock disponible en bodega para cualquier producto.

# La aplicación debe proveer las siguientes funcionalidades:
    
1. Registrar  usuarios.  Este registro solo debe ser realizado por el administrador, el cual se supone es una cuenta que existe desde el despliegue de la aplicación. Para este registro, el administrador debe autenticarse contra la aplicación y luego seleccionar la opción registrar, en donde debería suministrar la siguiente información para registrar un nuevo usuario: nombre de usuario, contraseña y correo electrónico.  La aplicación debe enviar un e-mail al correo del nuevo usuario registrado con las credenciales asignadas.
    
Nota: los usuarios al ser creados deben registrarse con un perfil: Administrador, y Vendedor, y se crean con estado Activo (la actualización del estado de un usuario a inactivo no será parte del grupo de requerimientos a implementar)

2. Proveer un portal de acceso, donde los usuarios puedan acceder al sistema, si se autentican, usando usuario y contraseñas, exitosamente. En caso contrario debe indicarle que su usuario y contraseña no existe. Esto debe cumplir con los requerimientos mínimos de seguridad (que el usuario exista, que la contraseña sea la correcta, que el usuario esté activo).
    
3. Ofrecer la opción para recuperar la contraseña en caso de olvido para los usuarios. Esta opción puede ser implementada, por ejemplo, por medio del envío de un e-mail al correo electrónico registrado para el usuario donde se envía el dato plano (esto no se considera una buena práctica, lo normal es que enviemos un link con una clave temporal y se diligencie nuevamente la nueva clave con confirmación). Sin embargo, solo enviar el correo electrónico será considerado suficiente.
    
4. Permitir la creación, actualización y eliminación de productos. Esto solo debe ser realizado por el administrador. Es decir, el usuario administrador puede crear, actualizar y/o dar de baja a un accesorio. En la creación de un artículo se debería ingresar referencia (un identificador para el producto), nombre del producto, cantidad, una imagen del producto. 
    
5. Un usuario autenticado (administrador, o vendedor) puede buscar un producto usando una palabra clave para el nombre y esta búsqueda mostrará una galería de imágenes.
    
6. Un usuario autenticado (vendedor) puede actualizar las cantidades de un producto particular. Es decir, se debe permitir actualizar la cantidad de un producto haciendo clic en la respectiva imagen del producto.

El ingreso al sistema requiere que de un login correcto, y una vez dentro el acceso a las opciones dependerá del perfil de ese usuario.

Vista inicio de sesión

Vista Formulario de registro de productos

Vista galeria de productos

Nota: Las imágenes aquí expuestas son sugeridas, no es obligación replicarlas en su proyecto. También, tener en cuenta que estas imágenes son para hacernos una idea sobre el bosquejo de la aplicación web. 
