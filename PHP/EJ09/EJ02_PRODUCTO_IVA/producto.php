<?php
class Producto{
    public $descripcion;
    public $precioSinIva;
    public function __construct($descripcion,$precioSinIva){
        $this->descripcion = $descripcion;
        $this->precioSinIva = $precioSinIva;
    }
    public function precioFinal(){
        echo "Descripción del producto: $this->descripcion";
        echo "<br>";
        echo "Precio sin IVA: $this->precioSinIva";
        echo "<br>";
        $precioFinal = $this->precioSinIva * 1.21; 
        echo "Precio con IVA: $precioFinal";
    }
}
?>