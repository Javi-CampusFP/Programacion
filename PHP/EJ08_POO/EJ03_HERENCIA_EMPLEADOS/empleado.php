<?php 
class Empleado {
    public $nombre;
    public $sueldo;
    public $aniosExperiencia;
    public $bonusTotal;

    public function calcularBonus(){
        $bonusCada2Anios = 0.05; // 5% del sueldo
        $bonuses = floor($this->aniosExperiencia / 2);
        $this->bonusTotal = $this->sueldo * $bonusCada2Anios * $bonuses;
        $this->sueldo = $this->sueldo + $this->bonusTotal;
    }

    public function mostrarDetalles(){
        echo "Nombre del empleado: $this->nombre<br>";
        echo "Sueldo del empleado: $this->sueldo<br>";
        echo "Años de experiencia: $this->aniosExperiencia<br>";
        echo "Bonuses: $this->bonusTotal<br>";
    }
}

class Consultor extends Empleado {
    public $horasPorProyecto;

    public function calcularBonus(){
        $bonusCada100 = 0.05; // 5% del sueldo
        $bonuses = floor($this->horasPorProyecto / 100);
        $this->bonusTotal = $this->sueldo * $bonusCada100 * $bonuses;
        $this->sueldo = $this->sueldo + $this->bonusTotal;
    }
}
?>
