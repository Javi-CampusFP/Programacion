# Variables globales

# Modelo de datos seleccionado: A
# Diccionario de articulos
articulos = {"id" : 1, "nombre" : "Ratón", "precio" : 12.5, "stock": 20, "activo": True}
lista_articulos = []
# Definir la variable opcion.
opcion = int
idProducto = 1
# Funciones

# Función de mostrar el menú
def menu_articulos():
    menu = ["1. Crear artículo", "2. Listar artículos", "3. Buscar artículo", "4. Actualizar artículo", "5. Eliminar un artículo", "6. Alternar activo/inactivo", "7. Salir"]
    for entrada in menu:
        print(entrada)

# Función para generar un id automáticamente
def generar_id(articulos):
    articulos = articulos + 1
    return articulos

# Función para listar los productos disponibles
def listar_articulos(articulos, solo_activos=None):
    for articulo in lista_articulos:
        print(articulo)
 
def buscar_articulo_por_id(articulos, id_busqueda):
    print()
def actualizar_articulo(articulos):
    print()
def eliminar_articulo(articulos):
    print()
def alternar_activo(articulos):
    print()
def leer_float(mensaje, minimo=None):
    print()
def leer_int(mensaje, minimo=None):
    print()

while opcion != 7:
    menu_articulos()
    opcion = int(input("Introduce una opción: "))
    match opcion:
        # Crear artículo
        case 1:
            idProducto = generar_id(idProducto)
            print(idProducto)
        # Listar artículos
        case 2:
            listar_articulos()
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

# Lógica del código

# TO DO: 

# Crear: pedir nombre (str), 
# precio (float > 0), stock (int ≥ 0). Asignar id único y activo=True.

# Listar: mostrar todos, con opción de filtrar solo activos/inactivos 
# (puede ser una subopción).

# Buscar por id: mostrar ficha completa o “no encontrado”.

# Actualizar: permitir cambiar nombre/precio/stock de un id existente.

# Eliminar: borrar por id (o, si prefieres, marcar activo=False y 
# explicar en el menú).

# Alternar activo/inactivo: cambiar el campo activo.

# Validaciones: tipos y rangos. Si un dato no es válido, pedirlo otra vez.