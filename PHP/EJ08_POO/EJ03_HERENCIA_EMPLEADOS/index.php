<?php
require_once("empleado.php");
// Crear empleados
$empleado1 = new Empleado();
$empleado1->nombre = "Juan Pérez";
$empleado1->sueldo = 1200;
$empleado1->aniosExperiencia = 3;
$empleado1->calcularBonus();
$empleado1->mostrarDetalles();

echo "<hr>";

$empleado2 = new Empleado();
$empleado2->nombre = "María Gómez";
$empleado2->sueldo = 1500;
$empleado2->aniosExperiencia = 6;
$empleado2->calcularBonus();
$empleado2->mostrarDetalles();

echo "<hr>";

$empleado3 = new Empleado();
$empleado3->nombre = "Carlos López";
$empleado3->sueldo = 1000;
$empleado3->aniosExperiencia = 1;
$empleado3->calcularBonus();
$empleado3->mostrarDetalles();

// Consultor 1
$consultor1 = new Consultor();
$consultor1->nombre = "Laura Martínez";
$consultor1->sueldo = 1500;
$consultor1->aniosExperiencia = 4; // heredado pero no usado en bonus
$consultor1->horasPorProyecto = 250;
$consultor1->calcularBonus();
$consultor1->mostrarDetalles();
echo "Horas por proyecto: $consultor1->horasPorProyecto<br><hr>";

// Consultor 2
$consultor2 = new Consultor();
$consultor2->nombre = "Miguel Torres";
$consultor2->sueldo = 1800;
$consultor2->aniosExperiencia = 6;
$consultor2->horasPorProyecto = 420;
$consultor2->calcularBonus();
$consultor2->mostrarDetalles();
echo "Horas por proyecto: $consultor2->horasPorProyecto<br><hr>";

// Consultor 3
$consultor3 = new Consultor();
$consultor3->nombre = "Sofía Rojas";
$consultor3->sueldo = 1300;
$consultor3->aniosExperiencia = 2;
$consultor3->horasPorProyecto = 90;
$consultor3->calcularBonus();
$consultor3->mostrarDetalles();
echo "Horas por proyecto: $consultor3->horasPorProyecto<br><hr>";
?>
