<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        ini_set('display_errors', 1);
        error_reporting(E_ALL);

        function comprobar_archivo($archivo) { // Crear la función de comprobar si existe o si el archivo se puede leer
            try {
                if (!file_exists($archivo)) { // Si el archivo no existe, 
                    throw new Exception("El archivo no existe"); // Exception 
                }
                if (!is_readable($archivo)) { // Si el archivo es leible
                    throw new Exception("El archivo no puede ser leído por el programa"); // Exception
                }
                return true; // Devolver verdadero si todo lo demas no dio error
            } catch (Exception $e) { // Para atrapar excepciones
                echo "Error: " . $e->getMessage();
                error_log(
                    date("[Y-m-d H:i:s] ") . $e->getMessage() . PHP_EOL,
                    3,
                    "error.log" // Guardar el log en error.log
                );
                return false; // Devuelve false si fallo
            }
        }
        $ruta = "notas.txt"; // La ruta del archivo 
        if (comprobar_archivo($ruta)) { // Si la función da true entonces
            $archivo = fopen($ruta, "r"); // Abrir el archivo
            while (($linea = fgets($archivo)) !== false) { // Mientras haya lineas
                echo htmlspecialchars($linea) . "<br>"; // Escribir en el html el contenido
            }
            fclose($archivo); // Cerrar el archivo
        }
    ?>

</body>
</html>