<?php
class Notificacion{
    public $mensaje;
    public function __construct($mensaje){
        $this->mensaje = $mensaje;
    }
    public function enviar(){
        echo "Enviando $this->mensaje";
    }
}
class Email extends Notificacion{
    public $destinatario;
    public function __construct($mensaje,$destinatario){
        parent::__construct($mensaje);
        $this->destinatario = $destinatario;
    }
    public function enviar(){
        echo "Para: $this->destinatario <br>";
        parent::enviar(); // Llama al método de la función padre enviar. 
    }
}
?>