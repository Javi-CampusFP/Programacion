<?php
    // Array
    $usuarios = [
    ["usuario" => "admin", "clave" => "1234"],
    ["usuario" => "pepe",  "clave" => "hola"],
    ["usuario" => "ana",   "clave" => "secreto"]
    ];
    // Variables globales necesarias
    $usuarioFormulario = $_POST["usuario"];
    $claveFormulario = $_POST["clave"];
    $encontrado = false;
    $nombre_usuario = "";
    // Recorrer el diccionario
    foreach ($usuarios as $user){
        // Si en la posicion X tiene password X, 
        if ($user["usuario"] == $usuarioFormulario && $user["clave"] == $claveFormulario){
            $encontrado = true; // Cambiar encontrado a true
            $nombre_usuario = $user["usuario"];
        };
    };
    // Si el usuario fue encontrado, indicarlo
    if($encontrado){
        echo "<br><p>Bienvenido ". $nombre_usuario."</p>";
    }
    // Si el usuario no fue encontrado, indicarlo tambien
    else{
        echo "<p style='color:red;'>Acceso denegado</p>";
    };
?>