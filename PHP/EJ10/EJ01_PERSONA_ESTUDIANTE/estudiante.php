<?php
class Persona{
    public $nombre;
    public $edad;
    public function __construct($nombre,$edad){ // Clase persona con atributos de una persona
        $this->nombre = $nombre;
        $this->edad = $edad;
    }
}
class Estudiante extends Persona{
    public $curso;
    public function __construct($nombre,$edad,$curso){
        parent::__construct($nombre,$edad);
        $this->curso = $curso;
    }
    public function mostrarDatos(){
        echo "Hola, me llamo $this->nombre, tengo $this->edad años del curso de $this->curso .";
    }
}
?>