<?php
$productos = ["Manzana" => 1.5,"Naranja" => 2.0,"Sandía"  => 5.0]; // El mismo array que tenia el index.php
$total = 0; // Precio total del ticket final
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ticket de Compra</title>
</head>
<body>

<h1>Ticket de Compra</h1>

<table border="1" cellpadding="8">
    <tr>
        <th>Producto</th>
        <th>Precio</th>
        <th>Cantidad</th>
        <th>Subtotal</th>
    </tr>

<?php
foreach ($productos as $nombre => $precio) { // Iterar el array 
    $cantidad = $_POST["cantidad_$nombre"]; // Recoge la cantidad de los productos
    $subtotal = $cantidad * $precio; // Calcula el precio total de X producto
    $total += $subtotal; // Sumar el subtotal con el total

    if ($cantidad > 0) { // Si la cantidad es mayor a cero, poner los datos del producto
        echo "<tr>";
        echo "<td>$nombre</td>";
        echo "<td>$precio €</td>";
        echo "<td>$cantidad</td>";
        echo "<td>$subtotal €</td>";
        echo "</tr>";
    }
}
?>

<tr>
    <td colspan="3"><strong>Total</strong></td>
    <td><strong><?php echo $total; ?> €</strong></td>
</tr>
</table>

</body>
</html>
