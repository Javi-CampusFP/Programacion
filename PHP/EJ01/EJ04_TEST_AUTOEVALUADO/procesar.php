<?php
    $respuestasCorrectas = [
        "p1" => "1", // índice de respuesta correcto
        "p2" => "0", // índice de respuesta correcto
        "p3" => "2" // índice de respuesta correcto
    ];
    $aciertos = 0;// El número de aciertos empieza en 0
    $numero_preguntas = 0; // El número de preguntas totales empieza en 0
    foreach($respuestasCorrectas as $preguntas => $respuestas){ // Recorrer las respuestas con el índice de la pregunta correcta
        $respuesta = $_POST[$preguntas]; // 
        if ($respuesta == $respuestas){ // Si la respuesta es igual a la respuesta correcta 
            $aciertos ++; // Aumentar el número de aciertos si se acerto la pregunta
        };
        $numero_preguntas ++; // Aumentar el número de preguntas
    };
    echo "<p>Has acertado $aciertos / $numero_preguntas .</p>"; // Indica el número de respuestas acertadas / preguntas totales
?>