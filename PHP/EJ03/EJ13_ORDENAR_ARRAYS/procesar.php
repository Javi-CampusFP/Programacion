<?php
$array = $_POST["array_numero"]; // Coger un string del index.html
$array = explode(',', $array); // Convertirlo en un array
sort($array); // Ordenar el array
echo "<p>La lista de números ordenados es:</p>";
echo "<p>" . implode(', ', $array) . "</p>"; // Esta función me la ha dicho ChatGPT.
?>
