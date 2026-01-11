<?php
$fecha = $_POST["fecha"]; // Recibir la fecha
$tiempo_unix = strtotime($fecha); // ;) Tiempo en formato UNIX ;) 
$dia_ingles = date("l", $tiempo_unix); // Sacar el dia en inglés  
$traduccion = ["Monday" => "Lunes", "Tuesday" => "Mártes", "Miércoles" => "Wednesday", 
    "Thursday" => "Jueves", "Friday" => "Viernes", "Saturday" => "Sábado", "Sunday" => "Domingo"]; // Equivalente en español
$dia_espanol = $traduccion[$dia_ingles]; // Traducir el día

echo "<h2>Naciste un $dia_espanol</h2>"; // Mostrar al usuario el día 
?>