<?php
class Reloj{
    public $marca;
    public function __construct($marca){
        $this->marca = $marca;
    }
}
class SmartWatch extends Reloj{
    public $sistemaOperativo;
    public function __construct($marca,$sistemaOperativo){
        parent::__construct($marca);
        $this->sistemaOperativo = $sistemaOperativo; 
    }
    public function mostrarDatos(){
        echo "Tengo un reloj $this->marca, sistema $this->sistemaOperativo";
    }
}
?>