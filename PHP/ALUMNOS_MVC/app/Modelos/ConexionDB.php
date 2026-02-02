<?php
    class ConexionDB{
        private static $conexion = null;
        public static function obtenerConexion(){
            if (self::$conexion === null){
                $host = "localhost";
                $baseDatos = "centro";
                $usuario = "root";
                $password = "";
                try {
                    // El data source name tiene que tener esta sintaxis
                    $dsn = "mysql:host=$host;dbname=$baseDatos;charset=utf8mb4";
                    // Por separado asi no dejo hardcodeado nada, paso a la clase PDO los parametros
                    self::$conexion = new PDO($dsn, $usuario, $password);
                    // Hacemos que PDO lance excepciones si hay errores.
                    self::$conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                }
                catch (PDOException $error) {
                    die("Error en la conexión con la base de datos.");
                }
            }
            return self::$conexion;
        }
    }
?>