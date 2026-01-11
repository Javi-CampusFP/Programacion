<?php
    $prohibidas = ["tonto", "feo", "loco", "gilipollas", "retrasado", "imbecil"];   // Palabras prohibidas
    $comentario = $_POST['area_texto'] ?? '';  // Texto recibido del textarea
    $reemplazos = []; // Creo un array vacio

    // Creo un array de reemplazos con asteriscos de la misma longitud que cada palabra
    foreach ($prohibidas as $palabra) {
        $reemplazos[] = str_repeat('*', strlen($palabra)); // Append al array con un str_repeat de la longitud de la palabra
    }

    // Reemplazo todas las palabras prohibidas por los asteriscos
    $comentario_filtrado = str_replace($prohibidas, $reemplazos, $comentario); 

    // Muestro el comentario dentro de un div
    echo "<div style='border:1px solid black; padding:10px; width:400px; margin-top:10px;'>
            <p>$comentario_filtrado</p>
        </div>";
?>