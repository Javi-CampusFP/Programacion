<?php
require_once "banco.php"; 

$accion = $_POST["accion"];
$cantidad = $_POST["cantidad"];

$cuenta = new Banco();
$cuenta->titular = "Juan";
$cuenta->saldo = 1000;
$cuenta->tipoDeCuenta = "Ahorros";

if ($accion == "ingresar") {
    $cuenta->depositar($cantidad);
} elseif ($accion == "retirar") {
    $cuenta->retirar($cantidad);
}

echo "<br>";
$cuenta->mostrarInfo();
