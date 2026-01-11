<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./styles.css">
    <title>Calculadora de IMC</title>
</head>
<body>
    <?php
    $peso = $_POST["peso"];
    $altura = $_POST["altura"];
    $altura_metros = $altura / 100;
    $imc = $peso / ($altura_metros**2);
    if ($imc < 18.5) { // Si el IMC es menor a 18.5
        $estado = "Bajo peso";
        $clase = "alerta-amarilla";
    } elseif ($imc >= 18.5 && $imc <= 24.9) { // Si el IMC esta entre 18.5 y 24.9
        $estado = "Peso normal";
        $clase = "alerta-verde";
    } else { // Sino, sobrepeso. 
        $estado = "Sobrepeso";
        $clase = "alerta-roja";
    }

    // Salida
    echo "<p>Altura introducida: $altura_metros m</p>";
    echo "<p>Peso introducido: $peso kg</p>";
    echo "<div class='$clase'>";
    echo "<p>IMC: $imc </p>";
    echo "<br><p>$estado</p>";
    echo "</div>";

    ?>
</body>
</html>