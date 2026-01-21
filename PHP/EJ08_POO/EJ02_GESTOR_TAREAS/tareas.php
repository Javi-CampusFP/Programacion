<?php 
class Tarea{
    public $nombre;
    public $descripcion;
    public $fechaLimite;
    public function marcarCompletada(){
        $prefijo = " | Marcada como completada.";
        $this->nombre = $this->nombre . $prefijo;
    }
    public function editarDescripcion($nuevaDescripcion){
        $this->descripcion = $nuevaDescripcion;
    }
    public function mostrarTarea(){
        echo "<br> <br>";
        echo "La tarea con nombre: $this->nombre <br>";
        echo "Descripción: $this->descripcion <br>";
        echo "Fecha límite: $this->fechaLimite <br>";
        echo "<br> <br>";
    }
}