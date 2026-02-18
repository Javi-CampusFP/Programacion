<?php
// app/Modelo/RepositorioAlumnos.php
require_once __DIR__ . '/ConexionDB.php';
require_once __DIR__ . '/Alumno.php';
class RepositorioAlumnos{
    private static $conexion;
    // Hace la conexión con la base de datos
    public function __construct(){
        self::$conexion = ConexionDB::obtenerConexion();
    }
    // Borrar X registro
    public function borrar($id){
        $sql = "DELETE FROM alumnos WHERE id=:id"; // Sentencia SQL
        $stmt = self::$conexion->prepare($sql); // Prepara la sentencia
        $stmt->execute([':id' => $id]); // Ejecuta la sentencia para evitar SQL Injection.
    }
    public function listar(){
        // Sentencia SQL y "preparar" la query
        $sql = "SELECT * FROM alumnos;";
        $stmt = self::$conexion->query($sql);
        // Creo el array de alumnos
        $alumnos = [];
        // Mientras haya más filas que recorrer, el array de alumnos recive clases nuevas y las mete en un array
        while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)){
            $alumnos[] = new Alumno(
            $fila['id'],
            $fila['nombre'],
            $fila['email'],
            $fila['edad'],
            $fila['fecha_creacion']
            );
        }
        // Devuelve el array, da igual si es vacío o no.
        return $alumnos;
    }
}
?>
