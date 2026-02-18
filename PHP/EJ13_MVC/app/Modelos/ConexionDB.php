<?php
require_once __DIR__ . '/../Controladores/ControladorAlumnos.php';
class ConexionDB{
    private static $conexion;
    public static function obtenerConexion(){
        if (self::$conexion === null){
            $host = "localhost";
            $bd = "centro_campusfp";
            $user = "root";
            $password = "curso";
            try{
                // data source name tiene que tener esta estructura
                $dsn = "mysql:host=$host;dbname=$bd;charset=utf8mb4";
                // Intentar realizar la conexión
                self::$conexion = new PDO($dsn, $user, $password);
                self::$conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            } catch(PDOException $error){
                die("Error a la conexión de la base de datos");
            }
        }
        return self::$conexion;
    }
}
?>