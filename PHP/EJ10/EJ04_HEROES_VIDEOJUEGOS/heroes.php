<?php
class Personaje{
    public $nombre;
    public $puntosVida;
    public function __construct($nombre,$puntosVida){
        $this->nombre = $nombre;
        $this->puntosVida = $puntosVida;
    }
}
class Guerrero extends Personaje{
    public $arma;
    public function __construct($nombre,$puntosVida){
        parent::__construct($nombre,$puntosVida);
        $this->arma = "espada";
    }
    public function imprimir(){
        echo "$this->nombre con $this->puntosVida y con un/a $this->arma";
    }
}
?>