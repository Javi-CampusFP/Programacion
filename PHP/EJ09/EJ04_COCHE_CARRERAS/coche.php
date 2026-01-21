<?php
class CocheF1{
    public $piloto;
    public $velocidad = 0;
    public function __construct($piloto){
        $this->piloto = $piloto;
    }
    public function acelerar(){
        $this->velocidad = $this->velocidad + 20;
        echo "<br> La velocidad del piloto $this->piloto es de $this->velocidad km/h. <br>";

    }
}
?>