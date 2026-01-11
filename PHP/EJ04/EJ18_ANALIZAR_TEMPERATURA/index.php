<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $dias = 5; // Días que queremos como input
        echo "<form action='./procesar.php' method='post'>"; // Iniciar formulario
        for($dia = 1; $dia <= $dias; $dia ++){ // Iterar hasta hacer X iteraciones
            echo "<label>Témperatura día $dia : </label>"; // indicar que input se refiere
            echo "<input type='number' name='temperaturas[]'>"; // Meter todo en un array cómun
            echo "<br>"; // break row (pa los espacios)
        }
        echo "<input type='submit' value='Calcular media...'>"; // Botón de enviar
        echo "</form>"; // Cerrar formulario
    ?> 
</body>
</html>