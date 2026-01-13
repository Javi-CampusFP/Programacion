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
    function comprobar_archivo($archivo) {
        try {
            if (!file_exists($archivo)) {
                throw new Exception("El archivo no existe");
                return false;
            }

            if (!is_readable($archivo)) {
                throw new Exception("El archivo no puede ser leído por el programa");
                return false;
            }
        } 
        catch (Exception $e) {
            echo "Error: " . $e->getMessage();

            error_log(
                date("[Y-m-d H:i:s] ") . $e->getMessage() . PHP_EOL, 3, "error.log"
            );
        }
        return true;
    }
    $ruta = "notas.txt";
    $sin_error = comprobar_archivo($ruta);
    if ($sin_error){
        
    }
    ?>
</body>
</html>