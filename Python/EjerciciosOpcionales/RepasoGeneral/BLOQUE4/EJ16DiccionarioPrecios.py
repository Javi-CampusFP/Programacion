# Crea un diccionario con al menos 3 productos y su precio.
# Pide al usuario uno de los productos y muestra su precio.
# Si el producto no existe, muestra un mensaje de error.
productos = []
contador = 0
while contador != 1:
    contador = contador + 1
    nombre = str(input("Introduce el nombre del producto: "))
    precio = float(input(f"Introduce el precio del producto {nombre}: "))
    productos.append({"nombre" : nombre, "precio" : precio})
productoBuscar = str(input("Introduce el nombre del producto a buscar: "))
encontrado = False
for nombres in productos:
    if nombres["nombre"] == productoBuscar:
        encontrado = True
        print(f"El precio es: {nombres["precio"]}")
if not encontrado:
    print(f"El producto con nombre {productoBuscar} no ha sido encontrado.")