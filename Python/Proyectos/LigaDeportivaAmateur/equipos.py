# Importar librerias
from tabulate import tabulate
# from general import comprobarString
# Declarar funciones

def menu():
    lista = ["Crear equipo","Listar equipos","Buscar por id","Actualizar datos","Desactivar equipo","Salir"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion

def agregarEquipo(id, lista):
    nombreEquipo = str(input("Introduce el nombre del equipo: "))
    ciudadEquipo = str(input("Introduce la ciudad del equipo: "))
    while len(nombreEquipo) == 0 or len(ciudadEquipo) == 0:
        if len(nombreEquipo) == 0:
            nombreEquipo = str(input("Error. El nombre del equipo no puede estar vacio. Intentálo de nuevo: "))
        else:
            ciudadEquipo = str(input("Error. El nombre de la ciudad no puede estar vacio. Intentálo de nuevo: "))
    lista.append({"id" : id, "nombre" : nombreEquipo, "ciudad" : ciudadEquipo, "activo" : True})
    print(f"El equipo con nombre {nombreEquipo} y id {id} de la ciudad {ciudadEquipo} ha sido creado y activado correctamente.")

def listarEquipos(lista):
    print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))
    """opciones = ["Mostrar todos", "Solo activos", "Solo inactivos"]
    indice = 1
    for entrada in opciones:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción: "))
    match opcion:
        case 1:
            print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))
        case 2:
            activo = True
            print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))
        case 3:
            activo = False
        case 4:
            print("El número introducido esta fuera de rango.")"""

def buscarIdEquipo():
    print()

def actualizarDatos():
    print()

def desactivarEquipo():
    print()
