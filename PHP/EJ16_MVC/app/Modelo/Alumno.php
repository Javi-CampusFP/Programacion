<?php
// app/Modelo/Alumno.php
class Alumno{
    // Se declaran los campos de la tabla de la base de datos
    public $id;
    public $nombre;
    public $email;
    public $edad;
    public $fecha_creacion;
    // Se usa el construct para reasignar los datos de la clase
    public function __construct($id,$nombre,$email,$edad,$fecha_creacion){
        $this->id = $id;
        $this->nombre = $nombre;
        $this->email = $email;
        $this->edad = $edad;
        $this->fecha_creacion = $fecha_creacion;
    }
}
?>