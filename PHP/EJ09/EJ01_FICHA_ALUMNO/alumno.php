<?php
class Alumno{
    public $nombre;
    public $curso;
    public function __construct($nombre, $curso){
        $this->nombre = $nombre;
        $this->curso = $curso;
    }
    public function presentarse(){
        echo "Soy $this->nombre y estudio $this->curso .";
    }
}
?>