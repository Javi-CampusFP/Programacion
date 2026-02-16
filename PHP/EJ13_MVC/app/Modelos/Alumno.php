<?php
class Alumno{
    public $id;
    public $nombre;
    public $email;
    public $fechaCreacion;
    function __construct($id,$nombre,$email,$fecha){
        $this->id = $id;
        $this->nombre = $nombre;
        $this->email = $email;
        $this->fechaCreacion = $fecha;
    }
}
?>