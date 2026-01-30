<?php
    $pizza_tamano = $_POST["pizza_tamano"]; // Pilla el tamaño de la pizza
    if ($pizza_tamano == "mediana"){
        $total = 10;
    }else{
        $total = 5;
    };
    $ingredientes = $_POST["ingredientes"];
    $total = count($ingredientes) + $total; // Se suma la cantidad de ingredientes al total (porque cada uno de ellos extra suma 1 al total) 
    echo "<h3>Pizza $pizza_tamano solicitada correctamente.</h3>";
    echo "<ul>";
    foreach($ingredientes as $ingrediente){ // Recorrer todos los ingredientes y mostrarlos en una lista
        echo "<li>$ingrediente</li>";
    };
    echo "</ul>";
    echo "<h4>TOTAL: $total € </h4>" // Mostrar el total de la factura
?>