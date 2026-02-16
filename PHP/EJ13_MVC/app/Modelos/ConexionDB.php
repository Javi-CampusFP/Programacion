<?php
class ConexionDB{
    private static $conexion;
    public static function obtenerConexion(){
        if (self::$conexion === null){
            $host = "localhost";
            $bd = "centro";
            $user = "root";
            $password = "curso";
            try{
                $dsn = "mysql:host=$host;dbname=$bd;charset=utf8mb4";
                self::$conexion = new PDO($dsn, $user, $password);
            } catch(PDOException $error){
                die("Error a la conexión de la base de datos");
            }
        }
        return self::$conexion;
    }
}
?>