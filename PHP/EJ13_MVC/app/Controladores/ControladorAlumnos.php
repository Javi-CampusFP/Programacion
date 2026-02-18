<?php
require_once __DIR__ . "/../Modelos/RepositorioAlumnos.php";
class ControladorAlumnos{
    private $repositorio;
    public function __construct(){
        $this->repositorio = new RepositorioAlumnos;
    }
    public function listar(){
        try{
            // Obtiene los datos del repositorio 
            $datos = $this->repositorio->obtenerTodos();
            // Pasa el array y la vista correspondiente
            $this->renderizar("alumnos/listar", ['alumnos' => $datos]);
        } catch(Exception $error){
            $this->registrarError("No se pudo listar a los alumnos.", $error);
            $this->renderizar("alumnos/listar", [
                'cursos' => [],
                'error' => 'No se pudieron cargar los alumnos. Revisa errores.log'
            ]);
        }
    }
    // Esta función coge datos y la ruta de la vista.
    public function renderizar($vista, $datos=[]){
        extract($datos);
        $archivosVista = __DIR__ . "/../vistas/" . $vista . ".php";
        if (!file_exists($archivosVista)){
            throw new Exception("La vista " . $vista . " no ha sido encontrada.");
            return;
        }
        $vistaContenido = $archivosVista;
        // Esto es para que si esta vacio, siempre salga el layout al menos
        require_once __DIR__ . "/../vistas/layout.php";
    }
    public function registrarError($contexto,$error){
        $ruta = __DIR__ . "/../../storage/errores.log";
        $linea = "ERROR: $contexto | $error";
        file_put_contents($ruta, $linea, FILE_APPEND);
    }
}
?>