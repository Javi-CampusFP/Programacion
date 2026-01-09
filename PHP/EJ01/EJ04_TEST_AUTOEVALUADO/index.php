<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEST AUTOEVALUADO</title>
</head>
<body>
    <?php 
        $preguntas = [
            "¿Cuál es la capital de España?" => ["Berlín", "Madrid", "Roma"], // Respuesta correcta índice 0 
            "¿Cuánto es 2 + 2?" => ["4","5","22"], // Respuesta correcta índice 1
            "¿Cuál de estos es un lenguaje de programación?" => ["HTML","CSS","JavaScript"] // Respuesta correcta índice 2 
        ]; // Las preguntas se asocian con las respuestas posibles para hacerlo más dinámico
        echo "<form action='procesar.php' method='POST'>";
        $numero_pregunta = 1; // El número de pregunta 
        foreach ($preguntas as $pregunta => $datos){ // para cada pregunta
            echo "<h3> PREGUNTA $numero_pregunta </h3>"; // Escribir el número de pregunta
            echo "<p>$pregunta</p>"; // La pregunta en si
            foreach ($datos as $index => $respuesta){ // Recorrer todas las respuestas posibles
                echo "<label><input type='radio' name='p$numero_pregunta' value='$index'> $respuesta</label><br>";
            };
            $numero_pregunta ++; // Aumentar el número de pregunta al final
        };
        echo '<input type="submit" value="Enviar">'; // Poner el boton de enviar 
        echo "</form>";// Cerrar el formulario
    ?>
</body>
</html>