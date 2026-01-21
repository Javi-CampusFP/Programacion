<?php
include_once("carrito.php");
// Incluir tu clase Carrito aquí
$miCarrito = new Carrito();

// Agregar productos al carrito
$miCarrito->agregarProducto("Manzanas", 2.5, 3);   // 3 manzanas a $2.5 c/u
$miCarrito->agregarProducto("Pan", 1.2, 2);        // 2 panes a $1.2 c/u
$miCarrito->agregarProducto("Leche", 1.5, 1);      // 1 leche a $1.5 c/u
$miCarrito->agregarProducto("Huevos", 0.3, 12);    // 12 huevos a $0.3 c/u

// Mostrar los productos del carrito
echo "<h2>Detalle del carrito:</h2>";
$miCarrito->mostrarDetalleCarrito();

// Calcular el total
echo "<h2>Total del carrito:</h2>";
$miCarrito->calcularTotal();

// Quitar un producto (ejemplo: Pan)
$miCarrito->quitarProducto("Pan");

echo "<h2>Carrito después de quitar Pan:</h2>";
$miCarrito->mostrarDetalleCarrito();
$miCarrito->calcularTotal();
?>
