<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

<h1>Gestor de tareas</h1>

<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

$archivo = "tareas.txt";


$opcion = 1; // cambia a 2 o 3 para probar

try {
    switch ($opcion) {
        // AÑADIR TAREA
        case 1:
            $tarea = "Comprar leche"; // tarea simulada

            if (trim($tarea) === "") {
                throw new Exception("La tarea está vacía");
            }

            $fecha = date("Y-m-d H:i:s");
            $linea = $fecha . " | " . $tarea . PHP_EOL;

            if (file_put_contents($archivo, $linea, FILE_APPEND) === false) {
                throw new Exception("No se pudo escribir en tareas.txt");
            }

            echo "<p style='color:green;'>Tarea añadida correctamente</p>";
            break;

        // LISTAR TAREAS
        case 2:

            // Si no existe  no es error fatal
            if (!file_exists($archivo)) {
                echo "<p>No hay tareas todavía</p>";
                file_put_contents($archivo, ""); // crear archivo vacío
                break;
            }

            $handle = fopen($archivo, "r");
            if ($handle === false) {
                throw new Exception("No se pudo abrir tareas.txt");
            }

            $hayTareas = false;

            while (($linea = fgets($handle)) !== false) {
                echo htmlspecialchars($linea) . "<br>";
                $hayTareas = true;
            }

            fclose($handle);

            if (!$hayTareas) {
                echo "<p>El archivo existe pero no tiene tareas</p>";
            }

            break;

        // SALIR
        case 3:
            echo "<p>Saliendo del programa...</p>";
            break;

        default:
            throw new Exception("Opción de menú inválida");
    }

} catch (Exception $e) {

    echo "<p style='color:red;'>Error: " . $e->getMessage() . "</p>";

    $error = date("[Y-m-d H:i:s] ") . $e->getMessage() . PHP_EOL;
    file_put_contents("errores.log", $error, FILE_APPEND);
}
?>

</body>
</html>
