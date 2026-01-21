<?php
include_once("empleado.php");
$becario = new Empleado("Manolo","Becario",800);
$jefa = new Empleado("Manola","Jefa",2500);
$becario->revisar_sueldo();
$jefa->revisar_sueldo();
?>