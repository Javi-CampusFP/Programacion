# Menú
print("1. Mostrar inventario")
print("2. Vender producto")
print("3. Añadir producto nuevo")
print("4. Calcular valor total del stock")
print("5. Salir")
opcion = int(input("Introduce un número de índice: "))
# Declaramos el inventario con las tuplas dentro
inventario = {"leche" : (1.2, 10), "pan" : (0.9, 20)}
while opcion != 5:
    match opcion:
        # Mostrar inventario
        case 1:
            # Recorre toda la lista e imprime el producto y la posicion en la tupla indicada
            for producto in inventario:
                print(f"- {producto} Precio: {inventario[producto][0]} Stock: {inventario[producto][1]}")
        # Vender producto
        case 2:
            # Introduce el nombre del producto, y si no hay stock o si no existe se lo indica al usuario
            producto = str(input("Introduce el producto a vender: "))
            if producto not in inventario or inventario[producto][1] == 0:
                print("El producto elegido no esta disponible o no hay stock")
            else:
                stockNuevo = inventario[producto][1] - 1
                precio = inventario[producto][0]
                # Te cargas los valores antiguos y creas una nueva tupla asociandola a la posicion:
                # inventario[producto]
                inventario[producto] = (precio, stockNuevo)
        # Añadir producto nuevo
        case 3:
            # Pedimos los datos necesarios y actualizamos el diccionario.
            nombreProducto = str(input("Introduce el nombre del producto nuevo: "))
            precioProducto = float(input("Introduce el precio por unidad del producto nuevo: "))
            stockProducto = int(input("Introduce el stock total del producto nuevo: "))
            inventario.update({nombreProducto : (precioProducto, stockProducto)})
        # Calcular el valor total del stock
        case 4:
            valorTotal = 0
            # Recorremos todos los items dentro de inventario y los sumamos en el valor total
            for nombre, (precio, cantidad) in inventario.items():
                valorTotal = valorTotal + (precio * cantidad)
            print("El valor total del stock es: ", valorTotal)
        # Número introducido inválido
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Mostrar inventario")
    print("2. Vender producto")
    print("3. Añadir producto nuevo")
    print("4. Calcular valor total del stock")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
