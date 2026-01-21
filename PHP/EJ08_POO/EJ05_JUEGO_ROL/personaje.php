<?php
class Personaje {
    
    public $nombre;
    public $nivel;
    public $puntosVida;
    public $puntosAtaque;
    
    public function atacar($objetivo){
        $objetivo->puntosVida = $objetivo->puntosVida - $puntosAtaque;
        echo "$this->nombre provoco un ataque que le quito $this->puntosAtaque puntos de vida a $objetivo->nombre <br>";
        if ($objetivo->puntosVida <= 0){
            echo "$this->nombre ha eliminado a: $objetivo->nombre <br>";
        } else{
            echo "$objetivo->nombre ahora tiene $objetivo->puntosVida <br>";
        }
    }
    
    public function curarse (){
        $recuperacion = 5;
        $this->puntosVida = $this->puntosVida + $recuperacion;
        echo "$this->nombre se ha recuperado la vida en $recuperacion puntos. <br>";
    }
    
    public function subirNivel(){
        echo "$this->nombre ahora es nivel $this->nivel ! <br>";
        $this->nivel = $this->nivel + 1;
        $this->puntosAtaque = ($this->nivel * 0.10) + $this->puntosAtaque;
        echo "$this->nombre ahora produce $this->puntosAtaque puntos de ataque! <br>"; 
    }
}
?>