<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
require_once __DIR__ . '/../app/Controladores/ControladorAlumnos.php';
$controlador = new ControladorAlumnos();
$accion = $_GET['accion'] ?? 'crear';
switch ($accion) {
    case 'crear':
        $controlador->crear();
        break;
    case 'guardar':
        $controlador->guardar();
        break;
    case 'correcto':
        $controlador->correcto();
        break;
    default:
        echo "Acción no válida";
}
