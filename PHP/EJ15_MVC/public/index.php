<?php
    // public/index.php
    require_once __DIR__ . '/../app/Controladores/ControladorAlumno.php';
    // Hacemos que se vean los errores y que se reporten todos
    ini_set('display_errors',1);
    error_reporting(E_ALL);
    // Creamos el controlador
    $controlador = new ControladorAlumno;
    // Cojo el parametro
    $accion = $_GET['accion'] ?? '';
    // Compruebo con el switch case
    switch ($accion){
        // 
        case 'borrar':
            $controlador->borrar();
            break;
        // 
        case 'listar':
            $controlador->listar();
            break;
        // 
        default:
            echo "La opción seleccionada no es válida.";
            break;
    }
?>