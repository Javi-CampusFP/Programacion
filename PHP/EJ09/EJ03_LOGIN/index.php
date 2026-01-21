<?php
include_once("usuario.php");
$usuario = new Login("manolo",1234);
$usuario->comprobar();
$usuario2 = new Login("manolito",1923);
$usuario2->comprobar();
?>