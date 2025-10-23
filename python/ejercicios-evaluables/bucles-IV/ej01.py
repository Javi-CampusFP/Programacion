print("1. Mostrar productos")
print("2. Añadir producto al carrito")
print("3. Ver total de la compra")
print("4. Salir")
opcion = int(input("Introduce un número de índice: "))

productos = {"bolígrafo" : 1.2, "cuaderno" : 3.5, "carpeta" : 2.8, "lapíz" : 1.0}
carrito = []
totalCarrito = 0

while opcion != 4:
	match opcion:
		case 1:
			for producto in productos:
				print()
				print(f"Producto: {producto} Precio: {productos[producto]}")
		case 2:
			introducirProducto = str(input("Introduce el nombre del producto: "))
			if introducirProducto in productos:
				carrito.append(introducirProducto)
				print(f"El producto {introducirProducto} fue agregado exitosamente al carrito.")
				
				precioProducto = productos[introducirProducto]
				totalCarrito = precioProducto + totalCarrito
			else:
				print(f"El producto: '{introducirProducto}' no esta en la lista de producto disponibles.")
		case 3:
			for productoCarrito in carrito:
				print()
				print(f"Producto en el carrito: {carrito[productoCarrito]} Precio: {productos[productoCarrito]}")
			print(f"El total a pagar es: {totalCarrito}")
		case _:
			print("Introduce un número de índice válido.")
	print("1. Mostrar productos")
	print("2. Añadir producto al carrito")
	print("3. Ver total de la compra")
	print("4. Salir")
	opcion = int(input("Introduce un número de índice: "))