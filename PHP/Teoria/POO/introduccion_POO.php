<?php
class Mascota{
    public $nombre;
    public $tipo;
    public function presentar(){
        echo "Hola, soy $this->nombre y soy un(a) $this->tipo.";
    }
    public function emitirSonido(){
        if ($this->tipo == "perro"){
            echo "¡Guau guau!";
        } elseif($this->tipo == "gato"){
            echo "Miau miau!";
        } else{
            echo "Este animal no tiene un sonido definido.";
        }
    }
}