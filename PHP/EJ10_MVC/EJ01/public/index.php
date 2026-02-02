
<?php
require_once __DIR__ . '/../app/Controladores/ControladorTareas.php';    
    $controlador = new ControladorTareas;
    $accion = $_GET['accion'] ?? 'listar';
    switch ($accion) {
        case 'listar':
            // Lista las tareas
            $controlador->listar();
            break;
        case 'crear':
            // Crea una tarea
            $controlador->crear();
            break;
        case 'guardar':
            // Guarda las tareas
            $controlador->guardar();
            break;
        default:
            echo "Acción no válida";
}
?>