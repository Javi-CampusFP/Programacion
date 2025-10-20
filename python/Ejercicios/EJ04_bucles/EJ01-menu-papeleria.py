# Menú para mostrarle las opciones disponibles al usuario
print("1. Mostrar productos")
print("2. Añadir productos al carrito")
print("3. Ver total de la compra")
print("4. Salir")
# Pedirle al usuario una acción
opcion = int(input("Introduce un número de índice para realizar una operación: "))
# Declarar los productos disponibles en un diccionario
productosDisponibles = {"bolígrafo" : 1.2, "cuaderno" : 3.5, "carpeta" : 2.8, "lapíz" : 0.8}
# Una lista que almacenara los productos que el usuario quiera comprar
carrito = []
# Total de la compra
total = 0
# Bucle while que se repite hasta que el usuario quiere salir
while opcion != 4:
    # Match case para el menú
    match opcion:
        case 1:
            # para cada producto en la lista imprime el precio y el nombre del producto
            for producto in productosDisponibles:
                print(f"Producto: {producto} - Precio: {productosDisponibles[producto]}")
        case 2:
            # Introduce los productos a elegir y añadelos a la lista llamada carrito
            productoElegido = str(input("Escriba el producto deseado (Introduzca 'fin' para acabar): "))
            while productoElegido.lower() != "fin":
                if productoElegido in productosDisponibles:
                    carrito.append(productoElegido)
                    print(f"El producto {productoElegido} ha sido agregado exitosamente a su carrito.")
                    # Suma el total de el precio de todos los productos
                    total = total + productosDisponibles[productoElegido]
                else:
                    # Si el producto no existe se le indica al usuario
                    print(f"Error. El producto {productoElegido} no existe.")
                    # Se pide al usuario otro input para que el bucle no sea infinito
                productoElegido = str(input("Escriba el producto deseado (Introduzca 'fin' para acabar): "))
        case 3:
            # Imprimir todos los productos junto con el total
            for productosCarrito in carrito:
                print(f"Producto: {productosCarrito} con precio: {productosDisponibles[productosCarrito]}")
            print(f"El total de la compra es: {total}")
        case _:
            # En caso de que se introduzca un número de índice no válido
            print("Error. Número introducido incorrecto (1 al 4). Inténtalo de nuevo: ")
    print("1. Mostrar productos")
    print("2. Añadir productos al carrito")
    print("3. Ver total de la compra")
    print("4. Salir")
    opcion = int(input("Introduce un número de índice para realizar una operación: "))
else:
    print("Has salido del programa.")
