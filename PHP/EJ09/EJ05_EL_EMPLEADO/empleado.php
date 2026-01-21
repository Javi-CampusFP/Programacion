<?php
class Empleado{
    public $nombre;
    public $puesto;
    public $sueldo;
    public function __construct($nombre,$puesto,$sueldo){
        $this->nombre = $nombre;
        $this->puesto = $puesto;
        $this->sueldo = $sueldo;
    }
    public function revisar_sueldo(){
        while ($this->sueldo < 1000 ){ // Mientras el sueldo sea menor a 1000
            $this->sueldo = $this->sueldo + 200;
            echo "<br> El sueldo de $this->nombre con puesto $this->puesto se ha actualizado a: $this->sueldo";
        }
        if ($this->sueldo >= 1000){
            echo "<br> El sueldo de $this->nombre es correcto.";
        }
    }
}
?>