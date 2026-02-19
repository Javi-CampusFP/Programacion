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
    // Función que sirve para actualizar datos de la base de datos
    public function actualizar($alumno){
        $sql = "UPDATE alumnos SET nombre = :nombre, email = :email, edad = :edad, fecha_creacion = :fecha_creacion WHERE id = :id";
        $stmt = self::$conexion->prepare($sql);
        $stmt->execute([
            ':nombre'=> $alumno->nombre,
            ':email' => $alumno->email,
            ':edad' => $alumno->edad,
            ':fecha_creacion' => $alumno->fecha_creacion,
            ':id' => $alumno->id
        ]);
    }
    // Se le pasa un ID como argumento 
    public function obtenerPorId($id){
        // La sentencia para coger al alumno con X id
        $sql = "SELECT * FROM alumnos WHERE id = :id"; 
        $stmt = self::$conexion->prepare($sql);
        $stmt->execute([':id' => $id]);
        // Si la fila existe, entonces devolvera el alumno
        if($fila = $stmt->fetch(PDO::FETCH_ASSOC)){
        $alumno = new Alumno(
            $fila['id'],
            $fila['nombre'],
            $fila['email'],
            $fila['edad'],
            $fila['fecha_creacion']
        );
        return $alumno;
        }
        // Si no se encontro al alumno, se devuelve null
        return null;
    }
}
?>
