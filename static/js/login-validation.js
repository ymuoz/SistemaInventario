function validar_formulario()
{
    var userid = document.forms["formulario"]["userid"].value;
    var password = document.forms["formulario"]["password"].value;
    var error = "";
    if (userid === "") {
        error = "Debe digitar un nombre de usuario.\n";
    }
    if (password === "") {
        error = error + "Debe digitar un password.";
    }
    if (error !== "") {
        alert(error);
        return false;
    }
    
    return true;
}