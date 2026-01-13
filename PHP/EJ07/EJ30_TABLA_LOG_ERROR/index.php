<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        table {
            border-collapse: collapse;
        }
        td, th {
            border: 1px solid #333;
            padding: 6px 10px;
        }
        th {
            background-color: #eee;
        }
    </style>
</head>
<body>

<h1>Listado de registros</h1>

<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

$archivo = "registros.txt";

try {
    // CASO A: no existe el fichero
    if (!file_exists($archivo)) {
        throw new Exception("No existe registros.txt");
    }

    $handle = fopen($archivo, "r");
    if ($handle === false) {
        throw new Exception("No se pudo abrir registros.txt");
    }

    echo "<table>";
    echo "<tr>
            <th>Fecha y hora</th>
            <th>Nombre</th>
            <th>Email</th>
            <th>Edad</th>
            <th>Comentario</th>
          </tr>";

    $lineaNumero = 0;
    $hayRegistrosValidos = false;

    while (($linea = fgets($handle)) !== false) {
        $lineaNumero++;
        $linea = trim($linea);

        if ($linea === "") {
            continue; // ignorar líneas vacías
        }

        // Separar campos
        $partes = explode("|", $linea);

        // CASO B: línea mal formateada
        if (count($partes) !== 5) {

            $log = date("Y-m-d H:i:s") . " | EJ30 | "
                 . "Línea mal formateada: $linea | "
                 . __FILE__ . " | línea $lineaNumero" . PHP_EOL;

            file_put_contents("errores.log", $log, FILE_APPEND);
            continue;
        }

        // Limpiar espacios
        $fecha      = trim($partes[0]);
        $nombre     = trim($partes[1]);
        $email      = trim($partes[2]);
        $edad       = trim($partes[3]);
        $comentario = trim($partes[4]);

        echo "<tr>";
        echo "<td>" . htmlspecialchars($fecha) . "</td>";
        echo "<td>" . htmlspecialchars($nombre) . "</td>";
        echo "<td>" . htmlspecialchars($email) . "</td>";
        echo "<td>" . htmlspecialchars($edad) . "</td>";
        echo "<td>" . htmlspecialchars($comentario) . "</td>";
        echo "</tr>";

        $hayRegistrosValidos = true;
    }

    fclose($handle);

    echo "</table>";

    if (!$hayRegistrosValidos) {
        echo "<p>No hay registros válidos para mostrar</p>";
    }

} catch (Exception $e) {

    // Mensaje amigable
    echo "<p>No hay registros todavía</p>";

    // Log del error
    $log = date("Y-m-d H:i:s") . " | EJ30 | "
         . $e->getMessage() . " | "
         . __FILE__ . " | "
         . $e->getLine() . PHP_EOL;

    file_put_contents("errores.log", $log, FILE_APPEND);
}
?>

</body>
</html>
