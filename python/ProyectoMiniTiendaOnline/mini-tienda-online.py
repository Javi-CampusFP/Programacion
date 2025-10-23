# Variables globales

# Modelo de datos seleccionado: A
# Diccionario de articulos metido dentro de una lista
articulos = [{"id" : 1, "nombre" : "Ratón", "precio" : 12.5, "stock": 20, "activo": True}]
# Definir la variable opcion.
opcion = int
# Declaramos id producto 1, porque ya hay uno con id 1
idProducto = 1
# Mensaje de error en int y en float
mensajeError = "Error. El número introducido no es válido."

# Funciones
# Función de mostrar el menú
def menu_articulos():
    menu = ["1. Crear artículo", "2. Listar artículos", "3. Buscar artículo", "4. Actualizar artículo", "5. Eliminar un artículo", "6. Alternar activo/inactivo", "7. Salir"]
    for entrada in menu:
        print(entrada)

# Función para generar un id automáticamente
def generar_id(idArticulos):
    idArticulos = idArticulos + 1
    return idArticulos

# Función para listar los productos disponibles
def listar_articulos(listaArticulos, solo_activos=None):
    indice = 0
    for articulo in listaArticulos[indice]:
        for cosa,cosas in articulo.items():
            print(articulo,cosas)
        indice = indice + 1

def buscar_articulo_por_id(listaArticulos, id_busqueda):
    print(listaArticulos)
def actualizar_articulo(listaArticulos):
    print()
def eliminar_articulo(listaArticulos):
    print()
def alternar_activo(listaArticulos):
    print()

def leer_float(mensaje, minimo=None):
    minimo = float(input("Introduce un precio mayor a 0 (> 0): "))
    while minimo < 0:
        print(mensaje)
        minimo = float(input("Introduce un precio mayor a 0 (> 0): "))
    return minimo

def leer_int(mensaje, minimo=None):
    minimo = float(input("Introduce un stock mayor o igual a 0 (=> 0): "))
    while minimo < 0:
        print(mensaje)
        minimo = float(input("Introduce un stock mayor o igual a 0 (=> 0): "))
    return minimo

# Lógica del código
while opcion != 7:
    menu_articulos()
    print(articulos)
    opcion = int(input("Introduce una opción: "))
    match opcion:
        # Crear artículo
        case 1:
            idProducto = generar_id(idProducto)
            # articulos = [{"id" : 1, "nombre" : "Ratón", "precio" : 12.5, "stock": 20, "activo": True}]
            nombre = str(input("Introduce el nombre del producto: "))
            precio = leer_float(mensajeError)
            stock = leer_int(mensajeError)
            if stock == 0:
                activo = False
            else:
                activo = True
            articulos.append({"id" : idProducto, "Nombre" : nombre, "Precio" : precio, "Stock" : stock, "Activo" : activo})
        # Listar artículos
        case 2:
            listar_articulos(articulos)
        # Buscar artículo por id
        case 3:
            print()
        # Actualizar artículo
        case 4:
            print()
        # Eliminar artículo
        case 5:
            print()
        # Alternar activo/inactivo
        case 6:
            print()
        # Si el usuario mete el número 7, se le indica
        case 7:
            print("Has salido del programa.")
        # Si el usuario mete un número inválido, indicarselo. (Fuera de rango)
        case _:
            print("Número introducido inválido. ")
