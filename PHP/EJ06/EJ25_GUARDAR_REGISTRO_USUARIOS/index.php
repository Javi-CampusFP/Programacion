<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

<h1>Registro de usuarios</h1>

<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

try {
    // Datos simulados
    $nombre = "Miguel";
    $email  = "miguel@email.com";

    // Validaciones con excepciones
    if (trim($nombre) === "") {
        throw new Exception("El nombre está vacío");
    }

    if (strpos($email, "@") === false) {
        throw new Exception("El email no contiene @");
    }

    // Preparar línea a guardar
    $fecha = date("Y-m-d H:i:s");
    $linea = $fecha . " | " . $nombre . " | " . $email . PHP_EOL;

    // Escritura en modo append (crea el archivo si no existe)
    if (file_put_contents("usuarios.txt", $linea, FILE_APPEND) === false) {
        throw new Exception("No se pudo escribir en usuarios.txt");
    }

    echo "<p style='color: green;'>Usuario guardado correctamente</p>";

} catch (Exception $e) {

    echo "<p style='color: red;'>Error: " . $e->getMessage() . "</p>";

    // Guardar error en errores.log
    $error = date("[Y-m-d H:i:s] ") . $e->getMessage() . PHP_EOL;
    file_put_contents("errores.log", $error, FILE_APPEND);
}
?>

</body>
</html>
