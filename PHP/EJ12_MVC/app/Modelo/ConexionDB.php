<?php
class ConexionDB {
    private static $conexion = null;
    public static function obtenerConexion(){
        // Si la conexión no se ha establecido, se prepara y se conecta.
        if (self::$conexion === null){
            $host = 'localhost';
            $baseDatos = 'formacion';
            $usuario = 'root';
            $password = 'curso';
            try {
                $dsn = "mysql:host=$host;dbname=$baseDatos;charset=utf8mb4";
                self::$conexion = new PDO($dsn, $usuario, $password);
            } catch (PDOException $error){
                die("Error de conexión con la base de datos.");
            }
        }
        // Si la conexión ya se ha establecido, se devuelve a si misma.
        return self::$conexion;
    }
}
?>