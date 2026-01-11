<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Buscador de Películas</title>
    <style>
        .tarjeta {
            border: 1px solid #333;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            width: 250px;
        }
        .titulo {
            font-weight: bold;
        }
        .genero {
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Buscador de Películas</h1>

    <!-- Formulario para seleccionar género -->
    <form method="POST">
        <label for="genero">Selecciona un género:</label>
        <select name="genero" id="genero">
            <option value="Acción">Acción</option>
            <option value="Comedia">Comedia</option>
        </select>
        <button type="submit">Buscar</button>
    </form>

    <hr>

    <?php
    // Array multidimensional de películas
    $peliculas = [
        ["Titulo" => "Rápido y Furioso", "Genero" => "Acción", "EdadMinima" => 13],
        ["Titulo" => "La Máscara", "Genero" => "Comedia", "EdadMinima" => 7],
        ["Titulo" => "Misión Imposible", "Genero" => "Acción", "EdadMinima" => 12],
        ["Titulo" => "Superbad", "Genero" => "Comedia", "EdadMinima" => 16],
        ["Titulo" => "John Wick", "Genero" => "Acción", "EdadMinima" => 18],
    ];

    // Comprobar si el formulario fue enviado
    if (isset($_POST['genero'])) {
        $generoSeleccionado = $_POST['genero'];
        $encontradas = 0; // Contador para saber si hay resultados

        foreach ($peliculas as $pelicula) {
            if ($pelicula['Genero'] == $generoSeleccionado) {
                $encontradas++;
                echo "<div class='tarjeta'>";
                echo "<p class='titulo'>{$pelicula['Titulo']}</p>";
                echo "<p class='genero'>{$pelicula['Genero']}</p>";
                echo "<p>Edad mínima: {$pelicula['EdadMinima']}</p>";
                echo "</div>";
            }
        }

        if ($encontradas === 0) {
            echo "<p>No hay resultados para el género seleccionado.</p>";
        }
    }
    ?>
</body>
</html>
