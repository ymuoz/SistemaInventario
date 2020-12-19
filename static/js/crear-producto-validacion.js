function validar_formulario()
{
    var nombre = document.forms["formulario"]["nombre"].value;
    var ref = document.forms["formulario"]["ref"].value;
    var cantidad = document.forms["formulario"]["cantidad"].value;
    var precio = document.forms["formulario"]["precio"].value;
    var error = "";

    if (nombre === "") {
        error = "Debe digitar un nombre.\n";
    }
    if (ref === "") {
        error += "Debe digitar una referencia.\n";
    }
    if (cantidad === "") {
        error += "Debe digitar una cantidad.\n";
    }
    if (precio === "") {
        error += "Debe digitar un precio.";
    }
    if (error !== "") {
        alert(error);
        return false;
    }
    
    return true;
}