<?php
    class ControladorNotas{
        // Pide las notas al modelo y carga la vista.
        public function listar(){
        }
        // Muestra el formulario.
        public function crear(){
        }
        // Valida, y guarda o muestra un error.
        public function guardar(){
        }
        // Cargar un layout y dentro, la vista.
        public function renderizar(){
        }
        // Guardar en storage/errores.log
        public function registrarError($contexto,$e){
            $archivoLog = __DIR__ . '/../../storage/errores.log';
            $fecha = date('Y-m-d H:i:s');
            $linea = $fecha . " | " . $contexto . " | " . $e->getMessage() . "\n";
            file_put_contents($archivoLog, $linea, FILE_APPEND);
        }
    }
?>