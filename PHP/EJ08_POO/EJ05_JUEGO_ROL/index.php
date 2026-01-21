<?php
include_once("personaje.php");
$p1 = new Personaje();
$p1->nombre = "Guerrero";
$p1->nivel = 1;
$p1->puntosVida = 25;
$p1->puntosAtaque = 6;

$p2 = new Personaje();
$p2->nombre = "Mago";
$p2->nivel = 1;
$p2->puntosVida = 18;
$p2->puntosAtaque = 7;

$p3 = new Personaje();
$p3->nombre = "Arquero";
$p3->nivel = 1;
$p3->puntosVida = 20;
$p3->puntosAtaque = 5;

$p4 = new Personaje();
$p4->nombre = "Asesino";
$p4->nivel = 1;
$p4->puntosVida = 16;
$p4->puntosAtaque = 8;

$p1->atacar($p4); 
$p4->atacar($p1); 

$p2->atacar($p3); 
$p3->atacar($p2); 

$p4->atacar($p2); 
$p1->atacar($p4); 

$p3->atacar($p1); 
$p1->atacar($p3); 

echo "<br><strong> El ganador es {$p1->nombre}</strong>";
?>
