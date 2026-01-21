<?php
class Banco {
    public $titular;
    public $saldo;
    public $tipoDeCuenta;

    public function depositar($cantidad) {
        if ($cantidad <= 0) {
            echo "La cantidad a depositar debe ser mayor que 0.<br>";
        } else {
            $this->saldo += $cantidad;
            echo "Depósito exitoso. Nuevo saldo: $this->saldo<br>";
        }
    }

    public function retirar($cantidad) {
        if ($cantidad <= 0) {
            echo "La cantidad a retirar debe ser mayor que 0.<br>";
        } elseif ($cantidad > $this->saldo) {
            echo "Fondos insuficientes.<br>";
        } else {
            $this->saldo -= $cantidad;
            echo "Retiro exitoso. Nuevo saldo: $this->saldo<br>";
        }
    }

    public function mostrarInfo() {
        echo "Titular: $this->titular<br>";
        echo "Tipo de cuenta: $this->tipoDeCuenta<br>";
        echo "Saldo: $this->saldo<br>";
    }
}
