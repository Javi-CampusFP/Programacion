<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>El Encriptador Hacker</title>
</head>
<body>
    <h1>El Encriptador Hacker (Leet Speak)</h1>

    <!-- Formulario -->
    <form method="POST">
        <label for="frase">Escribe tu frase:</label><br>
        <textarea name="frase" id="frase" rows="4" cols="50"><?php echo isset($_POST['frase']) ? htmlspecialchars($_POST['frase']) : ''; ?></textarea><br><br>
        <button type="submit">Hackear frase</button>
    </form>

    <hr>

    <?php
    if (isset($_POST['frase'])) {
        $frase = $_POST['frase'];

        // Diccionario de sustitución
        $buscar = ['A','E','I','O','S'];
        $reemplazar = ['4','3','1','0','5'];

        // Reemplazo usando str_ireplace para ignorar mayúsculas/minúsculas
        $fraseHackeada = str_ireplace($buscar, $reemplazar, $frase);

        echo "<p>Frase original: <strong>" . htmlspecialchars($frase) . "</strong></p>";
        echo "<p>Frase Hackeada: <strong>" . $fraseHackeada . "</strong></p>";
    }
    ?>
</body>
</html>
