<?php
require_once __DIR__ . 'ConexionDB.php';
require_once __DIR__ . 'Alumno.php';
class RepositorioAlumnos{
    private $conexion;
    function __construct(){
        self::$conexion->ConexionDB::obtenerConexion;
    }
    // create
    function insertar($alumno){
        // Insert into sentencia sql. Los ':' se ponen porque luego se van a sanitizar los caracteres
        $sql = "INSERT INTO alumnos (nombre,email,edad,fecha_creacion) VALUES :nombre, :email, :edad, :fecha";
        // Parece ser que stmt es una variable que hace PDO cuando se ejecuta. No hace falta definirla.
        $stmt = $this->conexion->prepare($sql);
        $stmt->execute([
            ':nombre' => $alumno->nombre,
            ':email' => $alumno->email,
            ':edad' => $alumno->edad,
            ':fecha' => $alumno->fechaCreacion
        ]);
    }
    // read
    function obtenerTodos(){
        $sql = "SELECT * FROM alumnos ORDER BY fecha_creacion DESC";
        // Cuando se hace un select no es necesario sanitizar el texto porque es salida de datos.
        $stmt = $this->conexion->query($sql);
        // Creo el array alumnos
        $alumnos = [];
        // Leemos fila por fila. Hasta que fetch de false (se quedo sin filas)
        while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)){
            // Convertir el array que da fetch en un array usable
            $alumnos[] = new Alumno($fila['id'],$fila['nombre'],$fila['email'],
            $fila['edad'],$fila['fecha_creacion']);
        }
        return $alumnos;
    }
    // delete
    function eliminar($id){
        $sql = "DELETE FROM alumnos WHERE id = :id";
        // Sanitizar el texto pa no liarla con algun usuario graciosillo
        $stmt = $this->conexion->prepare($sql);
        $stmt->execute([':id' => $id]);
    }
}
?>