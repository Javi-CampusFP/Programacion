# Importar librerias
from tabulate import tabulate
from utiles import comprobarString
from utiles import generarId
# Declarar funciones
# Función principal del menú
def menu():
    # Creo la lita con las entradas
    lista = ["Crear equipo","Listar equipos","Buscar por id","Actualizar datos","Desactivar equipo","Salir"]
    # Un número hace que sea más fácil de mantener que ponerlo directamente en el string de la lista
    indice = 1
    for entrada in lista:
        # Recorrer la lista e imprimir cada elemento
        print(f"{indice}. {entrada}")
        indice = indice + 1
    # Pedir una opción
    opcion = int(input("Introduce una opción del menú: "))
    # Retornar el número
    return opcion

# Agregar equipo, pidiendo el nombre y la ciudad
def agregarEquipo(id, lista):
    # Declarar las variables
    nombreEquipo = str
    ciudadEquipo = str
    # usar la función que he importado del módulo general
    nombreEquipo = comprobarString(nombreEquipo, "nombre")
    ciudadEquipo = comprobarString (ciudadEquipo, "ciudad")
    # Agregarlo a la lista
    lista.append({"id" : id, "nombre" : nombreEquipo, "ciudad" : ciudadEquipo, "activo" : True})
    # Mostrar un input al usuario
    print(f"El equipo con nombre {nombreEquipo} y id {id} de la ciudad {ciudadEquipo} ha sido creado y activado correctamente.")

# Listar equipos inactivos o activos o todos
def listarEquipos(lista):
    opciones = ["Mostrar todos", "Solo activos", "Solo inactivos"]
    indice = 1
    # Hago un mini menú para que el usuario pueda decidir entre filtrar por activos o inactivos
    for entrada in opciones:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción: "))
    match opcion:
        case 1:
            # Hago uso de tabulate, como es una lista con diccionarios dentro, hay que poner headers="keys"
            # El formato de la tabla en grid (uno de los más simples)
            print(tabulate(lista, headers="keys", tablefmt="grid"))
        case 2:
            # Declaro la lista donde se van a agregar los equipos que están activos
            activos = []
            for elemento in lista:
                # Recorro la lista, si el elemento con posicion ["activo"] es igual a true entonces agregar a
                # la lista elemento (se agrega el diccionario)
                if elemento["activo"]:
                    activos.append(elemento)
            if len(activos) > 0:
                # Si se encontro algún activo se imprime la tabla activos
                print(tabulate(activos, headers="keys", tablefmt="grid"))
            else:
                # Si no se encontro nada se indica al usuario
                print("No hay equipos activos.")
        case 3:
            # Aqui aplica lo mismo pero para los inactivos
            inactivos = []
            for elemento in lista:
                if not elemento["activo"]:
                    inactivos.append(elemento)
            if len(inactivos) > 0:
                print(tabulate(inactivos, headers="keys", tablefmt="grid"))
            else:
                print("No hay equipos inactivos")
        case _:
            print("El número introducido está fuera de rango.")

# Buscar por id
def buscarIdEquipo(lista):
    encontrado = False
    # Indicamos si no se encontro el equipo, si se encuentra, añadimos el diccionario a la lista y la imprimimos
    equipo = []
    id = int(input("Introduce un id de equipo a buscar: "))
    # Recorrer la lista en busca de que coincida por elemento en la posicion "id" con la misma que introdujo el usuario
    for elemento in lista:
        if elemento["id"] == id:
            # Cambiar encontrado a true
            encontrado = True
            # Añadir a la lista equipo
            equipo.append(elemento)
            # Imprimir la lista equipo por pantalla
            print(tabulate(equipo, headers="keys", tablefmt="grid"))
    if not encontrado:
        print(f"No se ha encontrado ningun equipo con el id '{id}'")

# Actualizar datos de un equipo por id
def actualizarDatos(lista):
    # Los elementos que podemos actualizar por cada equipo
    id = int(input("Introduce el id del equipo a actualizar: "))
    encontrado = False
    # Busca el elemento en la lista
    for elemento in lista:
        # Si el elemento con posicion id coincide con la id introducida por el usuario
        if elemento["id"] == id:
            # Actualizar encontrado a True
            encontrado = True
            # Declarar un mini menú
            actualizar = ["Nombre", "Ciudad", "Activo"]
            indice = 1
            for entrada in actualizar:
                print(f"{indice}. {entrada}")
                indice = indice + 1
            eleccion = int(input("Introduce una opción para actualizar: "))
            match eleccion:
                # Cambiar el nombre del equipo (no puede estar vacia)
                case 1:
                    nombreEquipo = str
                    print(f"Nombre actual: '{elemento["nombre"]}'")
                    nombreEquipo = comprobarString(nombreEquipo, "nombre")
                    elemento["nombre"] = nombreEquipo
                # Cambiar la ciudad del equipo (no puede estar vacia)
                case 2:
                    ciudadEquipo = str
                    print(f"Ciudad actual: '{elemento["ciudad"]}'")
                    ciudadEquipo = comprobarString (ciudadEquipo, "ciudad")
                    elemento["ciudad"] = ciudadEquipo
                # Cambiar de activo a inactivo y de inactivo a activo
                case 3:
                    if not elemento["activo"]:
                        elemento["activo"] = True
                        print(f"El equipo con nombre '{elemento["nombre"]}' ha sido actualizado a '{elemento["activo"]}'")
                    else:
                        elemento["activo"] = False
                        print(f"El equipo con nombre '{elemento["nombre"]}' ha sido actualizado a '{elemento["activo"]}'")
                case _:
                    print("Error. El número introducido está fuera de rango. Introduzca un número válido")
    if not encontrado:
        print(f"No se ha encontrado ningun equipo con el id '{id}'")

# Desactivar equipo por id
def desactivarEquipo(lista):
    # Pedimos un input al usuario
    id = int(input("Introduce un id de equipo para desactivar: "))
    encontrado = False
    # Recorrer cada elemento en la lista
    for elemento in lista:
        if elemento["id"] == id:
            encontrado = True
            # Si la posicion activo antes era Falso, actualizar a verdadero
            if not elemento["activo"]:
                elemento["activo"] = True
                print(f"El elemento con id '{id}' ha sido actualizado a '{elemento["activo"]}'")
            # Sino, actualizar la posición a Falso
            else:
                elemento["activo"] = False
                print(f"El elemento con id '{id}' ha sido actualizado a '{elemento["activo"]}'")
    if not encontrado:
        print(f"No se ha encontrado ningun equipo con el id '{id}'")
