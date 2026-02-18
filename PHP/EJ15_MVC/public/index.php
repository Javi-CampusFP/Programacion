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
        // Se manda a borrar al controlador
        case 'borrar':
            $controlador->borrar();
            break;
        // Listar a los alumnos
        case 'listar':
            $controlador->listar();
            break;
        // Si se tuvo exito borrando X alumno.
        case 'exito':
            $controlador->exito();
            break;
        // Si la opción no coincide con nada de lo anterior, simplemente se indica que es invalida.
        default:
            echo "La opción seleccionada no es válida.";
            break;
    }
?>