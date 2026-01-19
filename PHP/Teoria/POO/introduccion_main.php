<?php
require_once ("introduccion_POO.php");

$miMascota = new Mascota();
$miMascota->nombre = "Toby";
$miMascota->tipo = "perro";

// Usar los métodos
$miMascota->presentar();
$miMascota->emitirSonido();
