<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

<h1>Búsqueda de palabra en texto.txt</h1>

<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

$archivo = "texto.txt";
$palabra = "PHP"; // palabra a buscar (simulada)

try {
    // Caso 1: palabra vacía → excepción
    if (trim($palabra) === "") {
        throw new Exception("La palabra a buscar está vacía");
    }

    // Caso 2: archivo no existe → excepción
    if (!file_exists($archivo)) {
        throw new Exception("El archivo texto.txt no existe");
    }

    // Leer contenido completo
    $contenido = file_get_contents($archivo);

    if ($contenido === false) {
        throw new Exception("No se pudo leer el archivo texto.txt");
    }

    // Contar ocurrencias
    $contador = substr_count($contenido, $palabra);

    echo "<p>La palabra <strong>$palabra</strong> aparece <strong>$contador</strong> veces</p>";

} catch (Exception $e) {

    // Mostrar error
    echo "<p style='color:red;'>Error: " . $e->getMessage() . "</p>";

    // Guardar error en log
    $error = date("[Y-m-d H:i:s] ") . $e->getMessage() . PHP_EOL;
    file_put_contents("errores.log", $error, FILE_APPEND);
}
?>

</body>
</html>
