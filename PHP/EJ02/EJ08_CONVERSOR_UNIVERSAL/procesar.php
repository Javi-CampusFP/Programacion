<?php
    $cantidad = $_POST["cantidad"]; // Coger cantidad 
    $conversion = $_POST["conversion"]; // Coger tipo de conversion
    if (($conversion == "metros_pies" or $conversion == "pies_metros") and $cantidad <= 0){
        echo "<p>Error. La cantidad a convertir no puede ser menor a 0.</p>";
    }else{
        switch ($conversion){ // Switch que contempla distintas conversiones
            case "euros_dolares": // Conversión de euros a dolares
                $base = "euros";
                $conversionado = "dolares";
                $multiplicar = 0.14; // Asi es como esta a la hora de hacer este ejercicio el euro a dolar
                $total = $cantidad * $multiplicar;
                break;
            case "dolares_euros": // Conversión de dolares a euros
                $base = "dolares";
                $conversionado = "euros";
                $multiplicar = 0.86;
                $total = $cantidad * $multiplicar;
                break;
            case "metros_pies": // Conversión de metros a pies
                $base = "metros";
                $conversionado = "pies";
                $multiplicar = 3.28; 
                $total = $cantidad * $multiplicar;
                break;
            case "pies_metros": // Conversión de pies a metros
                $base = "pies";
                $conversionado = "metros";
                $multiplicar = 0.30;
                $total = $cantidad * $multiplicar;
                break;
            default: // Si ninguna de las anteriores se cumple
                echo "Conversión no válida.";
                break;
        }
        echo "<p>Cantidad original de $base: $cantidad </p>
        <br>
        <p>Cantidad convertida a $conversionado: $total</p>"; // Muestra el total de la cantidad al usuario
    }
?> 