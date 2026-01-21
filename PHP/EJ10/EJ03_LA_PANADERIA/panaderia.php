<?php
class Producto{
    public $nombre;
    public $precio;
    public function __construct($nombre,$precio){
        $this->nombre = $nombre;
        $this->precio = $precio;
    }
}
class Pastel extends Producto{
    public $sabor;
    public function __construct($nombre,$precio,$sabor){
        parent::__construct($nombre,$precio);
        $this->sabor = $sabor;
    }
    public function etiqueta(){
        echo "Pastel de $this->sabor : $this->nombre - $this->precio";
    }
}
?>