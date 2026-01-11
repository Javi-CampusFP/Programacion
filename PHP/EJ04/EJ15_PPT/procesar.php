<?php
$array = ["piedra", "tijeras", "papel"]; // array con posiciones para un rand range

$seleccion = $_POST["seleccion"]; // coger el valor de la selección del index.html
$posicion = rand(0, 2); // del 0 al 2, elegir un número (posición del array)
$seleccion_sistema = $array[$posicion]; // Almacenarlo en una variable

echo "<p>CPU eligió: $seleccion_sistema</p>"; // Indicar que eligio la CPU
echo "<p>Tú elegiste: $seleccion</p>"; // Indicarle al usuario que eligio

if ($seleccion_sistema == $seleccion) { // Si la selección del sistema y la del usuario es la misma, entonces empate
    echo "<h2>EMPATE</h2>"; // Comunicar el resultado
} else if (
    ($seleccion_sistema == "piedra"  && $seleccion == "tijeras") ||
    ($seleccion_sistema == "tijeras" && $seleccion == "papel")   ||
    ($seleccion_sistema == "papel"   && $seleccion == "piedra")
) { // Analizar todas las posibilidades donde la CPU gano
    echo "<h2>LA CPU GANÓ</h2>"; // Comunicar que la CPU gano
} else {
    echo "<h2>GANASTE TÚ</h2>"; // Comunicar que el usuario gano
}
?>
