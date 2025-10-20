# Definir el diccionario stock vacio
stock = {}
# Pedirle el input al usuario, la cantidad y el nombre
producto = str(input("Escriba el nombre del producto: "))
cantidad = int(input("Escriba la cantidad del producto disponible: "))
# Mientras producto no sea igual a fin añadir al diccionario 
while producto.lower() != "fin":
	stock.update({producto : cantidad})
	producto = str(input("Escriba el nombre del producto: "))
	if producto != "fin":
		cantidad = int(input("Escriba la cantidad del producto disponible: "))
# Imprimir cada producto con la cantidad que queda
for lista in stock:
# En cada stock en posicion [lista] almacenar en cantidadesProducto
	cantidadesProducto = stock[lista]
	print(f"De {lista} nos quedan {cantidadesProducto}")