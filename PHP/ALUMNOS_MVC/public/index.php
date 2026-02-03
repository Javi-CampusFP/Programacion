<?php
// public/index.php
ini_set('display_errors',1);
error_reporting(E_ALL);
// Incluimos el controlador en su ruta.
require_once __DIR__ . '/../app/Controladores/ControladorAlumnos.php';
// Creamos el controlador
$controlador = new ControladorAlumnos();
// Leemos la acción (acción por defecto: Listar)
$accion = $_GET['accion'] ?? ['listar'];
// Decidir que acción realizar
switch ($accion){
    case 'listar':
        $controlador->listar();
        break;
    case 'crear':
        $controlador->crear();
        break;
    case 'guardar':
        $controlador->guardar();
        break;
    case 'borrar':
        $controlador->borrarPorId();
        break;
    default:
        echo "Acción no válida.";
}
?>