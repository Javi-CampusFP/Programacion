<?php
class Login{
    public $usuario;
    public $password;
    public function __construct($usuario,$password){
        $this->usuario = $usuario;
        $this->password = $password;
    }
    public function comprobar(){
        if ($this->password != 1234){
            echo "Contraseña incorrecta.";
            echo "<br>";
        } else {
            echo "Acceso concedido a $this->usuario <br>";
        }
    }
}
?>