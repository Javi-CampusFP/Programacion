<?php
// app/Vistas/layout.php
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado de alumnos</title>
</head>
<body>
    <div>
        <p>Base de datos alumnos CRUD | Javier Blázquez Cerezo</p>
    </div>
    <?php
        // Esto es para incluir el contenido de la vista
        require $vistaContenido;
    ?>
</body>
</html>