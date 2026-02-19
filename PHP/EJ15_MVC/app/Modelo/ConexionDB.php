<?php
// app/Modelo/ConexionDB.php
class ConexionDB{
    private static $conexion = null;
    public static function obtenerConexion(){
        // Si la conexión es null, entonces se intenta hacer la conexión
        if (self::$conexion === null){
            // Datos necesarios para la conexión de la base de datos
            $host = "localhost";
            $bd = "centro";
            $user = "root";
            $password = "curso";
            // Intenta realizar la conexión
            try {
                $dsn = "mysql:host=$host;dbname=$bd;charset=utf8mb4";
                self::$conexion = new PDO($dsn, $user, $password);
                self::$conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            // Si ocurre algun error se captura y se manda al log y se muestra un mensaje amigable al usuario
            } catch (Exception $error){
                $ruta = __DIR__ . '/../../storage/errores.log';
                $fila = date("Y-m-d H:i:s") . " | BD CONEXIÓN | $error";
                file_put_contents($ruta,$fila,FILE_APPEND);
                die("Error a la conexión con la base de datos.");
            }
        }
        return self::$conexion;
    }
}
?>