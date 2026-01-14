<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 31 | Añadir contactos</title>
</head>
<body>
    <div style="text-align:center">
        <h2>FORMULARIO AÑADIR CONTACTO</h2>

        <form action="" method="post">
            <label>Nombre</label>
            <input type="text" name="nombre" minlength="4" maxlength="20" required>
            <br><br>

            <label>Apellidos</label>
            <input type="text" name="apellidos" minlength="6" maxlength="40" required>
            <br><br>

            <label>Teléfono</label>
            <input type="tel" name="telefono" minlength="9" maxlength="12" required>
            <br><br>

            <label>Apodo</label>
            <input type="text" name="apodo" minlength="6" maxlength="20" required>
            <br><br>

            <label>Email</label>
            <input type="email" name="email" minlength="6" maxlength="50" required>
            <br><br>

            <input type="submit" value="Registrar">
        </form>

        <br>
        <a href="./index.html"><button>Volver</button></a>
        <br>
    </div>

<?php
    ini_set('display_errors', 1);
    error_reporting(E_ALL);

    $ARCHIVO = "./agenda.txt";

    function encontrar_caracter($caracter, $string){
        for ($i = 0; $i < strlen($string); $i++) {
            if ($string[$i] == $caracter) {
                return true;
            }
        }
        return false;
    }

    function crear_contacto($ruta){
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {

            $nombre = $_POST['nombre'] ?? '';
            $apellidos = $_POST['apellidos'] ?? '';
            $telefono = $_POST['telefono'] ?? '';
            $apodo = $_POST['apodo'] ?? '';
            $email = $_POST['email'] ?? '';

            // Validar email (usando tu función)
            $email_correcto = encontrar_caracter("@", $email);

            if (!$email_correcto) {
                echo "<p style='text-align:center; color:red;'>El correo no es correcto</p>";
                return false;
            }

            // Guardar contacto SIN borrar los anteriores
            file_put_contents(
                $ruta,
                "$nombre|$apellidos|$telefono|$apodo|$email\n",
                FILE_APPEND
            );

            return true;
        }
        return false;
    }

    if (crear_contacto($ARCHIVO)) {
        echo "<p style='text-align:center; color:green;'>El contacto se añadió correctamente</p>";
    }
?>
</body>
</html>
