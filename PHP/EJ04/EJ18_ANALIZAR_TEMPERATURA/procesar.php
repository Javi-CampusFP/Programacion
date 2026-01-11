<?php
$temperaturas = $_POST['temperaturas']; // Coger las temperaturas del index.php
$record = 0; // Record de témperatura máximos
$record_min = 0; // Record de témperatura mínimos
$iteraciones = 0; // Número de iteraciones realizadas
$total_temperaturas = 0; // Total de grados para luego hacer la media
foreach ($temperaturas as $temperatura){ // Recorrer todos los elementos del array
    if ($temperatura > $record){ // Si la temperatura es mayor a la del record máximo
        $record = $temperatura; // Reasignar record de temperaturas máximas
    }
    else if ($temperatura < $record_min){ // Si la temperatura es menor al del record mínimo
        $record_min = $temperatura; // Reasignar record de temperaturas mínimas
    }
    $iteraciones = $iteraciones + 1;
    $total_temperaturas = $total_temperaturas + $temperatura; 
}
$media = $total_temperaturas / $iteraciones;
echo "<h2>El día que más calor hizo fue con una temperatura de: $record</h2><br>";
echo "<h2>El día que más frío hizo fue con una temperatura de: $record_min</h2><br>";
echo "<p>Total de media de los $iteraciones días: $media"
?>