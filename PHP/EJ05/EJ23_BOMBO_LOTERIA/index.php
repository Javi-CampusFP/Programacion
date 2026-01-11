<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>El Bombo de la Lotería</title>
    <style>
        .bola {
            display: inline-block;
            width: 40px;
            height: 40px;
            line-height: 40px;
            border-radius: 50%;
            background-color: #3498db;
            color: white;
            text-align: center;
            margin: 5px;
            font-weight: bold;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>El Bombo de la Lotería</h1>

    <form method="POST">
        <label for="cantidad">¿Cuántos números quieres sacar?</label>
        <input type="number" name="cantidad" id="cantidad" required min="1"><br><br>

        <label for="rango">¿Rango máximo?</label>
        <input type="number" name="rango" id="rango" required min="1"><br><br>

        <button type="submit">Sacar números</button>
    </form>

    <hr>

    <?php
    if (isset($_POST['cantidad']) && isset($_POST['rango'])) {
        $cantidad = intval($_POST['cantidad']);
        $rango = intval($_POST['rango']);

        // Control básico: no pedir más números que el rango
        if ($cantidad > $rango) {
            echo "<p style='color:red;'>Error: No puedes pedir más números que el rango máximo.</p>";
        } else {
            $numeros = [];

            while (count($numeros) < $cantidad) {
                $num = rand(1, $rango);
                if (!in_array($num, $numeros)) {
                    $numeros[] = $num;
                }
            }

            sort($numeros); // Ordenar de menor a mayor

            echo "<h2>Números de la lotería:</h2>";
            foreach ($numeros as $n) {
                echo "<div class='bola'>{$n}</div>";
            }
        }
    }
    ?>
</body>
</html>
