<?php
// app/Controladores/ControladorAlumno.php
require_once __DIR__ . '/../Modelo/ConexionDB.php';
class ControladorAlumno{
    private static $repositorio;
    public function __construct(){
        self::$repositorio = new ConexionDB();
    }
    public function listar(){
        echo "";
    }
    public function borrar(){
        echo "";
    }
}
?>