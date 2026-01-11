<?php
$cantidad = $_POST["cantidad"]; // Cantidad recogida en el index.html
$array = [50,20,10];
echo "<p>La cantidad $cantidad € necesita: </p>";
foreach ($array as $numero){
    $billetes = floor($cantidad / $numero);
    $cantidad = $cantidad % $numero;
    echo "<p>$billetes billetes de $numero €</p><br>";
}
echo "<p>$cantidad monedas de 1€</p>";
?>
