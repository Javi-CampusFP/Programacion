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
    // Esta función edita los datos 
    public function editar(){
        try {
            // Obtiene los datos del alumno
            $alumnoEditar = self::$repositorio->obtenerPorId($_POST['id']);
            if (empty($alumnoEditar)){
                throw new Exception("Alumno no encontrado.");
            }
            // Actualiza los datos del alumno nuevo 
            $alumno = new Alumno(
                $_POST['id'],
                $_POST['nombre'],
                $_POST['email'],
                $_POST['edad'],
                $alumnoEditar->fecha_creacion
            );
            // Reemplaza los datos del alumno antiguo
            self::$repositorio->actualizar($alumno);
            // Redirige a la vista de 'exito'.
            header("Location: index.php?accion=exito");
            return;
            // Si hay algun error se muestra un mensaje amigable, se registra y se cierra.
        } catch (Exception $error){
            echo "Hubo un error al intentar actualizar a los alumnos.";
            $this->registrarError("ACTUALIZAR",$error);
            return;
        }
    }
    // Esta función es para acceder al formulario 
    public function formularioEditar(){
        $id = $_GET['id'] ?? null;
        $alumno = self::$repositorio->obtenerPorId($id);
        $this->renderizar("alumnos/actualizar", ['alumno' => $alumno]);
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