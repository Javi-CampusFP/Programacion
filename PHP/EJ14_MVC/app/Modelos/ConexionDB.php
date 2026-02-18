<?php 
class ConexionDB{
    private static $conexion = null;

    public static function obtenerConexion(){
        if (self::$conexion === null){
            $host = "localhost";
            $bd = "centro";
            $user = "root";
            $password = "curso";
            // Intentar la conexión a la base de datos
            try {
                // data source name (las siglas) tiene que tener esta estructura
                $dsn = "mysql:host=$host;dbname=$bd;charset=utf8mb4";
                // Intentar realizar la conexión
                self::$conexion = new PDO($dsn, $user, $password);
                self::$conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            // Si surge algun error, registrarlo y terminar el proceso.
            } catch (PDOException $error){
                ControladorAlumnos::registrarError("CONEXIÓN BASE DE DATOS",$error->getMessage());
                die("Error de conexión a la base de datos.");
            }
        }
        // Devuelve la conexión a la base de datos
        return self::$conexion;
    }
}
?>
