<?php
require_once __DIR__ . '/ConexionDB.php';
require_once __DIR__ . '/Alumno.php';
class RepositorioAlumnos{
    private $conexion = null;
    public function __construct(){
        $this->conexion = ConexionDB::obtenerConexion();
    }
    public function obtenerTodos(){
        $sql = "SELECT * FROM alumnos ORDER BY fecha_creacion DESC";
        $stmt = $this->conexion->query($sql);
        $alumnos = [];
        while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)){
            $alumnos[] = new Alumno(
            $fila['id'],
            $fila['nombre'],
            $fila['email'],
            $fila['fecha_creacion']);
        }
        return $alumnos;
    }
}
?>