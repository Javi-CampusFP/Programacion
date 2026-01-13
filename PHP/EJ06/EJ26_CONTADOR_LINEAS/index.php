<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

<h1>Contador de líneas de usuarios.txt</h1>

<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

$archivo = "usuarios.txt";

try {
    // Caso 1: el archivo no existe → excepción
    if (!file_exists($archivo)) {
        throw new Exception("El archivo usuarios.txt no existe");
    }

    // Abrir archivo
    $handle = fopen($archivo, "r");

    if ($handle === false) {
        throw new Exception("No se pudo abrir el archivo usuarios.txt");
    }

    $contador = 0;

    // Lectura línea a línea segura
    while (!feof($handle)) {
        $linea = fgets($handle);
        if ($linea !== false) {
            $contador++;
        }
    }

    fclose($handle);

    // Caso 2: existe pero está vacío (NO es error)
    if ($contador === 0) {
        echo "<p>El archivo está vacío</p>";
    } 
    // Caso 3: existe y tiene líneas
    else {
        echo "<p>El archivo tiene <strong>$contador</strong> líneas</p>";
    }

} catch (Exception $e) {

    // Mostrar error
    echo "<p style='color:red;'>Error: " . $e->getMessage() . "</p>";

    // Registrar error en errores.log
    $error = date("[Y-m-d H:i:s] ") . $e->getMessage() . PHP_EOL;
    file_put_contents("errores.log", $error, FILE_APPEND);
}
?>

</body>
</html>
