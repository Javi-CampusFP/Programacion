<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Barra de Progreso de Ventas</title>
    <style>
        .contenedor {
            width: 100%;
            background-color: #ddd;
            border-radius: 5px;
            overflow: hidden;
            margin-top: 10px;
        }
        .barra {
            height: 30px;
            background-color: #4CAF50;
            text-align: center;
            line-height: 30px;
            color: white;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Barra de Progreso de Ventas</h1>

    <form method="POST">
        <label for="objetivo">Objetivo de Ventas (€):</label>
        <input type="number" name="objetivo" id="objetivo" required min="1"><br><br>

        <label for="actual">Ventas Actuales (€):</label>
        <input type="number" name="actual" id="actual" required min="0"><br><br>

        <button type="submit">Calcular Progreso</button>
    </form>

    <?php
    if (isset($_POST['objetivo']) && isset($_POST['actual'])) {
        $objetivo = floatval($_POST['objetivo']);
        $actual = floatval($_POST['actual']);

        // Evitar división por cero
        if ($objetivo == 0) {
            echo "<p style='color:red;'>Error: El objetivo no puede ser cero.</p>";
        } else {
            // Calcular porcentaje
            $porcentaje = round(($actual * 100) / $objetivo);
            if ($porcentaje > 100) $porcentaje = 100; // Limitar al 100%

            echo "<div class='contenedor'>";
            echo "<div class='barra' style='width: {$porcentaje}%;'>{$porcentaje}%</div>";
            echo "</div>";
        }
    }
    ?>
</body>
</html>
