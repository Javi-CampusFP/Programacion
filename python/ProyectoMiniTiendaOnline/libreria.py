# Función para generar un id automáticamente
def generar_id(id):
    # Generar la id de un artículo nuevo
    id = id + 1
    # Devuelve el valor
    return id
# Leer float declarado en la función
def leer_float(mensaje, minimo=None):
    precio = float(input("Introduce un precio mayor a 0 (> 0): "))
    while precio <= minimo:
        print(mensaje)
        precio = float(input("Introduce un precio mayor a 0 (> 0): "))
    return precio
# Leer entero declarado en la función
def leer_int(mensaje, minimo=None):
    # Meter el stock en una variable
    stock = int(input("Introduce un stock mayor o igual a 0 (=> 0): "))
    # Si el stock es menor al minimo declarado, se muestra mensaje de error y se pide otra vez el stock
    while stock < minimo:
        print(mensaje)
        stock = int(input("Introduce un stock mayor o igual a 0 (=> 0): "))
    return stock

# Menú de usuarios
def menu_general():
    menu = ["1. Gestionar productos", "2. Gestionar usuarios", "3. Carrito y ventas", "4. Salir del programa"]
    for entrada in menu:
        print(entrada)
