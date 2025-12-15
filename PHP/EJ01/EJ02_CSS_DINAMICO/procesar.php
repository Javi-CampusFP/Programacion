<?php
    // Recoger los datos del post del formulario
    $color_elegido = $_POST["color_elegido"];
    $size_letra = $_POST["size_letra"];
    $titular = $_POST["titular"];
    $alineacion = $_POST["alineacion"];
    // Si el usuario no mete ninguna posición, asignar left por defecto
    if($alineacion == ""){
        $alineacion = "left";
    };
    // Escribir html en la página
    echo "<h1 style='background-color: $color_elegido; font-size: $size_letra; text-align: $alineacion;'>$titular</h1>";

?>