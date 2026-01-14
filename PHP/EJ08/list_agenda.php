<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 31 | Listar contactos</title>
</head>
<body>
    <h2>LISTAR CONTACTOS</h2>
    <table>
        <?php
            function comprobar_archivo($archivo){
                try {
                    if (!file_exists($archivo)){
                        throw new Exception("No existe el archivo");
                    }
                }
                catch (Exception $error){
                    $mensaje = 1;
                    file_put_contents("error.log",$mensaje,FILE_APPEND);
                    echo "Ha ocurrido un error.";
                }
            } 
        ?>
    </table>
</body>
</html>