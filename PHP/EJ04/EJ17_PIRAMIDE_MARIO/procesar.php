<?php
$numero_escalones = $_POST["numero_filas"]; // Coger el número del index.html 
$fila = '*'; // El carácter que quiero que se ponga en una fila
for($iteracion = 1; $iteracion <= $numero_escalones; $iteracion ++){ // Iterar 
    echo "<p>$fila</p><br>"; // Imprimir la fila
    $fila .= '*'; // Concatenar '*' a la variable 'fila' para añadir otro más cada iteración
}
?>