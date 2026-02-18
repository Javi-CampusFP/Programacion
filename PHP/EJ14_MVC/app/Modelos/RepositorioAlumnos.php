<?php
require_once __DIR__ . '/ConexionDB.php';
class RepositorioAlumnos{
    private static $conexion;
    function __construct(){
        self::$conexion = ConexionDB::obtenerConexion();
    }
    public function insertar($alumno){
        // Sentencia SQL que se va a ejecutar
        $sentencia = "INSERT INTO ALUMNOS (nombre,email,edad,fecha_creacion) VALUES (:nombre,:email,:edad,:fecha)";
        // Preparar la consulta para evitar inyecciones SQL
        $stmt = self::$conexion->prepare($sentencia);
        // Reemplazar los strings que empiecen por :"x" por la variable del array que se le pasa
        $stmt->execute([
            ":nombre" => $alumno->nombre,
            ":email" => $alumno->email,
            ":edad" => $alumno->edad,
            ":fecha" => $alumno->fecha_creacion
        ]);
    }
}
?>
