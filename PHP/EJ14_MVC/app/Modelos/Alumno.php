<?php 
class Alumno{
    // Son los campos de la tabla alumnos de la base de datos
    public $nombre;
    public $email;
    public $edad;
    public $fecha_creacion;
    // Construct para pasarlo como argumentos
    public function __construct($nombre, $email, $edad, $fecha_creacion){
        $this->nombre = $nombre;
        $this->email = $email;
        $this->edad = $edad;
        $this->fecha_creacion = $fecha_creacion; 
    }
}
?>
