<?php
class ControladorTareas{
    public function listar(){
        echo "";
    }
    public function crear(){
        echo "";
    }
    public function guardar(){
        echo "";
    }
    public function renderizar($datos) { // Nota: Estos comentarios los ha realizado una IA
        require __DIR__ . '/../Vistas/layout.php';    
        extract($datos);
        $archivoVista = __DIR__ . '/../Vistas/' . $vista . '.php';
    }
}
?>