<?php
    // public/index.php
    require_once __DIR__ . '/../app/Controladores/ControladorAlumno.php';
    // Hacemos que se vean los errores y que se reporten todos
    ini_set('display_errors',1);
    error_reporting(E_ALL);
    // Creamos el controlador
    $controlador = new ControladorAlumno;
    // Cojo el parametro
    $accion = $_GET['accion'] ?? 'listar'; // Por defecto listamos si no hay acción
    // Compruebo con el switch case
    switch ($accion){
        // Muestra el formulario vacío con los datos del alumno
        case 'formularioEditar':
            $controlador->formularioEditar();
            break;
        // Recibe el POST del formulario y guarda los cambios
        case 'editar':
            $controlador->editar();
            break;
        // Listar a los alumnos
        case 'listar':
            $controlador->listar();
            break;
        // Si se tuvo exito actualizando/borrando
        case 'exito':
            $controlador->exito();
            break;
        // Si la opción no coincide con nada
        default:
            echo "La opción seleccionada no es válida.";
            break;
    }
?>