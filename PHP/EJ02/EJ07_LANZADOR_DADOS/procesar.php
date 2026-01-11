<?php
    $dados_lanzar = $_POST["dados_lanzar"];
    for($dados = 0; $dados < $dados_lanzar; $dados ++){ // Iterar hasta lanzar el número de dados deseado
        $aleatorio = rand(1,6); // Generar un número aleatorio
        echo "<div style='justify-content: center; display:flex; align-items: center; text-align: center; 
        width: 130px; height: 130px; margin: 10px;
        background-color: black; color: white;'>"; // Este es el div con todos los parametros para que quede "bonito" 
        echo "<p>$aleatorio</p>"; // El número final
        echo "</div>"; // Cierro el div 
    }
?>