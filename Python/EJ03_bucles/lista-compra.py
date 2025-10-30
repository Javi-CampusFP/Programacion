# Declaramos la lista vacía
listaCompra = []

# Pedimos un input al usuario
producto = input("Escribe un producto en la lista (introduce 'fin' para terminar): ")
# Comprobamos si el input es fin, sino, entramos en el bucle
while producto.lower() != "fin":
# Si producto ya está en la lista de la compra hacer el print
    if producto in listaCompra:
        print("Este objeto ya está adentro de la lista.")
# Sino meter el producto dentro de la lista
    else:
        listaCompra.append(producto)
        print(f"El producto '{producto}' ha sido agregado a la lista satisfactoriamente.")
# Volver a pedir el input
producto = input("Escribe un producto en la lista (introduce 'fin' para terminar): ")

print("La lista de productos de la compra es:")
# Recorrer la lista entera e imprimirla en pantalla
for listaProductos in listaCompra:
    print(f" - {listaProductos}")