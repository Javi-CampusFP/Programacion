<?php
require_once "tareas.php";

$tarea1 = new Tarea();
$tarea1->nombre = "Estudiar PHP";
$tarea1->descripcion = "Repasar POO";
$tarea1->fechaLimite = "2026-01-25";

$tarea2 = new Tarea();
$tarea2->nombre = "Hacer ejercicio";
$tarea2->descripcion = "Correr 30 minutos";
$tarea2->fechaLimite = "2026-01-22";

$tareas = [$tarea1, $tarea2];

$tarea2->editarDescripcion("Correr 30 minutos y sacar al perro");
$tarea2->marcarCompletada();
foreach ($tareas as $tarea){
    $tarea->mostrarTarea();
}