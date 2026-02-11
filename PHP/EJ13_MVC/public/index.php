<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
require_once __DIR__ . '/../app/Controladores/ControladorAlumnos.php';
$controlador = new ControladorALumnos();
$accion = $_GET['accion'] ?? 'listar';
switch ($accion){
    case 'listar':
        $controlador->listar();
        break;
    default:
        echo "Acción no válida.";
        break;
}
?>