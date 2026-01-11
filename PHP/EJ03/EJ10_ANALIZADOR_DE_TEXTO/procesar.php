<?php
    $texto = $_POST["area_texto"]; // Coger el texto desde el index.html
    $recorrer = str_split($texto); // Hace el string recorrible por un foreach
    $catacteres_totales = 0; // Iniciar contador de caracteres
    $delimitador = ' '; // Establecer el delimitador (Donde se considera que termina una palabra)
    $palabras = 0; // Establecer el contador de palabras
    $texto_invertido = strrev($texto); // Definir una variable con el texto del reves
    foreach($recorrer as $caracter){ // Recorrer todos los caracteres del texto
        $caracteres_totales = $caracteres_totales + 1; // Sumar 1 cada iteración del bucle  
        if ($caracter == $delimitador){ // Compara si el carácter es el mismo que el delimitador
            $palabras = $palabras + 1; // Suma 1 al contador de palabras
        }
    }
    echo "<h2> TEXTO ORIGINAL </h2>";
    echo "<p>$texto</p>";
    echo "<h2> CARÁCTERES TOTALES </h2>";
    echo "<br>";
    echo "<p> NÚMERO DE CARÁCTERES: $caracteres_totales</p>";
    echo "<br>";
    echo "<h2>NÚMERO DE PALABRAS</h2>";
    echo "<br>";
    echo "<p> NÚMERO DE PALABRAS: $palabras</p>";
    echo "<br>";
    echo "<h2>TEXTO DEL REVÉS</h2>";
    echo "<p>$texto_invertido</p>";
?>