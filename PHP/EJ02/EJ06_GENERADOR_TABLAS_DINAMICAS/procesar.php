<?php
    $alto_tabla = $_POST["altura_tabla"]; // Coger los datos del formulario
    $ancho_tabla = $_POST["ancho_tabla"]; // Coger los datos del formulario
    echo "<table border='1'>"; // Crear una tabla con un borde
    for ($iteraciones_alto = 0; $iteraciones_alto < $alto_tabla; $iteraciones_alto++) { 
        echo "<tr>"; // Crear una fila
        for ($iteraciones_ancho = 0; $iteraciones_ancho < $ancho_tabla; $iteraciones_ancho++) {
            echo "<td>$iteraciones_alto,$iteraciones_ancho</td>"; // Crear una columna con sus coordenadas
        }
        echo "</tr>"; // Cerrar la fila
    }
    echo "</table>"; // Cerrar la tabla
?>
