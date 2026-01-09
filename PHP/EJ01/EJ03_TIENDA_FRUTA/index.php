<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket de Compra - Tienda de Fruta</title>
</head>
<body>
    <div class="form-container">
        <h1>Ticket de Compra - Tienda de Fruta</h1>
        <form action="./procesar.php" method="POST">
            <?php
            $productos = ["Manzana" => 1.5, "Naranja" => 2.0, "Sandía" => 5.0]; // Un array con el nombre y el precio por unidad
            foreach ($productos as $nombre => $precio){ // Recorrer el array 
                echo "<label for='' >Producto: $nombre <br> Precio por unidad: $precio <br> Cantidad: "; // Nombre de la etiqueta dinámico
                echo "<input type='number' name='cantidad_$nombre' min='0' value='0'>"; // Nombre del botón dinámico 
                echo "<br>"; 
            }?>
            <input type="submit" value="Enviar"> 
        </form>
    </div>
</body>
</html>
