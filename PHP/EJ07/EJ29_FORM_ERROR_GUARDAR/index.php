<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio 29 · Formulario con persistencia</title>
</head>
<body>

<h1>Formulario de registro</h1>

<form method="post">
    <label>
        Nombre:
        <input type="text" name="nombre" required>
    </label>
    <br><br>

    <label>
        Email:
        <input type="text" name="email" required>
    </label>
    <br><br>

    <label>
        Edad:
        <input type="number" name="edad" required>
    </label>
    <br><br>

    <label>
        Comentario:
        <br>
        <textarea name="comentario" maxlength="200"></textarea>
    </label>
    <br><br>

    <button type="submit">Enviar</button>
</form>

<hr>

<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

/**
 * Valida los datos del formulario
 */
function validarFormulario($nombre, $email, $edad, $comentario) {

    if (strlen(trim($nombre)) < 3) {
        throw new Exception("El nombre debe tener al menos 3 caracteres");
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new Exception("El email no es válido");
    }

    if (!filter_var($edad, FILTER_VALIDATE_INT, [
        "options" => ["min_range" => 0, "max_range" => 120]
    ])) {
        throw new Exception("La edad debe ser un número entre 0 y 120");
    }

    if (strlen($comentario) > 200) {
        throw new Exception("El comentario supera los 200 caracteres");
    }
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    try {
        // Recoger datos
        $nombre     = $_POST["nombre"] ?? "";
        $email      = $_POST["email"] ?? "";
        $edad       = $_POST["edad"] ?? "";
        $comentario = $_POST["comentario"] ?? "";

        // Validación
        validarFormulario($nombre, $email, $edad, $comentario);

        // Preparar línea de guardado
        $fecha = date("Y-m-d H:i:s");

        $linea = $fecha . " | "
               . $nombre . " | "
               . $email . " | "
               . $edad . " | "
               . str_replace(["\n", "\r"], " ", $comentario)
               . PHP_EOL;

        // Guardar datos
        if (file_put_contents("registros.txt", $linea, FILE_APPEND) === false) {
            throw new Exception("No se pudo escribir en registros.txt");
        }

        echo "<p style='color:green;'>Guardado correcto</p>";

    } catch (Exception $e) {

        // Mensaje amigable
        echo "<p style='color:red;'>Error: " . htmlspecialchars($e->getMessage()) . "</p>";

        // Log detallado
        $lineaLog = date("Y-m-d H:i:s") . " | EJ29 | "
                  . $e->getMessage() . " | "
                  . __FILE__ . " | "
                  . $e->getLine() . PHP_EOL;

        file_put_contents("errores.log", $lineaLog, FILE_APPEND);
    }
}
?>

</body>
</html>
