<?php
    class Carrito{
        public $productos = [];
        public function agregarProducto ($nombre,$precio,$cantidad){
            $producto_nuevo = [$nombre,$precio,$cantidad];
            $this->productos[] = $producto_nuevo;
        }
        public function quitarProducto($nombre){
            $nuevo = [];
            foreach($this->productos as $producto){
                if ($producto[0] !== $nombre){
                    $nuevo[] = $producto;
                }
            }
            $this->productos = $nuevo;
        }
        public function calcularTotal(){
            $total = 0;
            foreach ($this->productos as $producto){
                $total = $total + ($producto[1] * $producto[2]);
            }
            echo "<hr><br>$total<br><hr>";
        }
        public function mostrarDetalleCarrito(){
            foreach($this->productos as $producto){
                echo "<hr>";
                echo "Nombre del producto: $producto[0] <br>";
                echo "Precio del producto: $producto[1] <br>";
                echo "Cantidad del producto: $producto[2] <br>";
                echo "<hr>";
            }
        }
    }
?>