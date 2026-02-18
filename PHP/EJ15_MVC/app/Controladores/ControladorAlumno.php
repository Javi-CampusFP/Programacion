<?php
// app/Controladores/ControladorAlumno.php
require_once __DIR__ . '/../Modelo/RepositorioAlumnos.php';
class ControladorAlumno{
    private static $repositorio;
    // Crear la conexión con el repositorio
    public function __construct(){
        self::$repositorio = new RepositorioAlumnos();
    }
    // Función para listar a los alumnos
    public function listar(){
        try {
            // Obtiene todos los alumnos disponibles
            $alumnos = self::$repositorio->listar();
            // Renderiza la vista pasando los datos también
            $this->renderizar("alumnos/listar",['alumnos' => $alumnos]);
        } catch (Exception $error){
            echo "Hubo un error al listar a los alumnos.";
            $this->registrarError("LISTAR",$error);
            return;
        }
    }
    // Función para borrar a un alumno
    public function borrar(){
        // El ID del alumno a borrar
        $id = $_GET['id'] ?? '';
        if (!ctype_digit($id)){
            throw new Exception("Error, el ID debe de ser númerico");
        }
        // Intenta borrarlo, si hay algun error, se avisa al usuario y se registra el error
        try {
            self::$repositorio->borrar($id);
            header("Location: index.php?accion=exito");
        } catch (Exception $error){
            $this->registrarError("BORRAR", $error);
            echo "Hubo un error al borrar al alumno.";
            return;    
        }
    }
    // Esto es para que si se borra correctamente, se le indica al usuario
    public function exito(){
        $this->renderizar("alumnos/exito");
    }
    // Función para registrar un error
    public function registrarError($contexto,$error){
        $ruta = __DIR__ . '/../../storage/errores.log';
        $linea = date("Y-m-d H:i:s") . " | $contexto | $error";
        file_put_contents($ruta,$linea,FILE_APPEND);
    }
    // Renderizar la vista con los datos
    public function renderizar($vista, $datos=[]){
        // Extraer los datos del array assoc
        extract($datos);
        // Construir la ruta a la vista
        $archivoVista = __DIR__ . '/../Vistas/' . $vista . '.php';
        // Si el archivo no existe, el flujo del código se corta
        if (!file_exists($archivoVista)){
            echo "Error, la vista $vista no existe.";
            return;    
        }
        $vistaContenido = $archivoVista;
        // Mostrar el contenido de el layout.php
        require __DIR__ . "/../Vistas/layout.php";
    }
}
?>