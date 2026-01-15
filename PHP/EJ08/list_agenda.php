<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Listar agenda</title>
</head>
<body>

<?php
    ini_set('display_errors', 0);
    error_reporting(E_ALL);

    $ARCHIVO = "./agenda.txt";
    $LOG = "./errores.log";

    function escribir_error($mensaje) {
        $f = fopen("./errores.log", "a");
        if ($f) {
            fwrite($f, date("Y-m-d H:i:s") . " - " . $mensaje . "\n");
            fclose($f);
        }
    }
?>

<div style="text-align:center">
    <h2>LISTA DE CONTACTOS</h2>

<?php
    if (!file_exists($ARCHIVO)) {
        escribir_error("No existe agenda.txt");
        echo "<p>No hay contactos guardados.</p>";
    } else {
        $f = fopen($ARCHIVO, "r");

        if (!$f) {
            escribir_error("No se pudo abrir agenda.txt");
            echo "<p>Error al leer la agenda.</p>";
        } else {
            echo "<table border='1' align='center'>";
            echo "<tr><th>Nombre</th><th>Apellidos</th><th>Teléfono</th><th>Apodo</th><th>Email</th></tr>";

            $hay_datos = false;

            while (!feof($f)) {
                $linea = trim(fgets($f));

                if ($linea == "") continue;

                $datos = explode("|", $linea);

                if (count($datos) < 5) {
                    escribir_error("Linea mal formada: $linea");
                    continue;
                }

                $hay_datos = true;

                echo "<tr>";
                echo "<td>$datos[0]</td>";
                echo "<td>$datos[1]</td>";
                echo "<td>$datos[2]</td>";
                echo "<td>$datos[3]</td>";
                echo "<td>$datos[4]</td>";
                echo "</tr>";
            }

            fclose($f);

            echo "</table>";

            if (!$hay_datos) {
                echo "<p>No hay contactos guardados.</p>";
            }
        }
    }
?>

<br>
<a href="./index.html"><button>Volver</button></a>

</div>

</body>
</html>
