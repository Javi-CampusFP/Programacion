# importar librerias
from utiles import comprobarString, leer_int_mayor
from tabulate import tabulate
# Declarar funciones

def menu():
    # Declarar una lista con las entradas
    lista = ["Alta de jugador","Listar jugadores","Buscar jugador por id",
    "Actualizar jugador","Desactivar jugador","Salir"]
    indice = 1
    # Recorrer la lista e imprimir el indice a su vez
    print()
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    # Pedir input del usuario y retornarlo
    print()
    opcion = int(input("Introduce una opción del menú: "))
    return opcion

# Función para dar de alta a un jugador
def darAltaJugador(id, jugadores, equipos):
    # Declarar las variables para que no den error
    nombreJugador = str
    posicion = str
    posicionNueva = str
    # Declarar las variables de encontrado y activo en falso, si encuentra el equipo,
    # simplemente le ponemos en encontrado = True, y si activo es Falso, entonces se lo podemos indicar.
    encontrado = False
    activo = False
    # Introducir el id del equipo
    idEquipo = leer_int_mayor("id del equipo", 0)
    # para cada elemento en la lista del equipo
    for equipo in equipos:
        # Validar si el elemento en la posición id es igual a idEquipo, si es, entonces seguir
        # con el condicional
        if equipo["id"] == idEquipo:
            encontrado = True
            # Si es activo, cambiar la variable a activo
            if equipo["activo"] == True:
                activo = True
                # Pedir nombre y posición
                nombreJugador = comprobarString(nombreJugador, "nombre")
                posicion = comprobarString(posicion, "posición")
                jugadorActivo = True
                # Comprobar si en el diccionario ya existe en ese mismo equipo y en la posición que intentamos
                # meter el nuevo jugador, si hay, se le indica y se pone como sustituto
                for jugador in jugadores:
                    if (jugador["posicion"] == posicion) and (jugador["activo"] == True):
                        print(f"Error. Ya hay un jugador en el equipo con id '{idEquipo}' que esta activado.")
                        print("Cambia la posición, o indique si es sustituto (introduzca la misma posición para convertirlo en sustituto):")
                        print(f"Posición en conflicto: {posicion}")
                        posicionNueva = comprobarString(posicionNueva, "posición")
                        if posicion == posicionNueva:
                            jugadorActivo = False
                        else:
                            jugadorActivo = True
                jugadores.append({"id" : id, "nombre" : nombreJugador, "equipo" : idEquipo, "posicion" : posicion, "activo" : jugadorActivo})
                print(f"El jugador con id {id} ha sido agregado correctamente al equipo {idEquipo}")
    # Si no se encuentra o no esta activo indicarlo
    if encontrado == False or activo == False:
        print(f"El equipo con id '{id}' no ha sido encontrado o el equipo con id {idEquipo} esta inactivo.")

# Función para listar a los jugadores de una lista
def listarJugadores(jugadores):
    # Declarar las opciones disponibles que se indican en el ejercicio
    encontrado = False
    opciones = ["Todos los jugadores", "De un equipo en concreto (un id)"]
    indice = 1
    idEquipo = int
    # Recorrer la lista de opciones
    for entrada in opciones:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    # Pedir un input al usuario
    opcion = int(input("Introduce un número: "))
    match opcion:
        # Todos los jugadores
        case 1:
            print(tabulate(jugadores, headers="keys", tablefmt="grid"))
        # De un equipo en concreto
        case 2:
            lista = []
            idEquipo = leer_int_mayor("id del equipo", 0)
            for jugador in jugadores:
                if jugador["equipo"] == idEquipo:
                    encontrado = True
                    # Agregamos el jugador dentro de la lista que luego vamos a mostrar
                    lista.append(jugador)
            # Mostrar la lista
            print(tabulate(lista, headers="keys", tablefmt="grid"))
        # El usuario ha metido un número fuera del rango
        case _:
            print("Error. El número introducido está fuera de rango. Introduzca un número válido")
    # No se ha encontrado el equipo con esa id
    if encontrado == False:
        print(f"El equipo con id '{idEquipo}' no tiene ningún jugador o no existe.")

# Función para buscar a un jugador por id
def jugadorPorId(jugadores):
    # Leer el entero y almacenarlo en un id
    id = leer_int_mayor("id del jugador",0)
    encontrado = False
    lista = []
    for jugador in jugadores:
        # Comprobar si el jugador tiene el id correcto
        if jugador["id"] == id:
            encontrado = True
            lista.append(jugador)
            # Imprimir el jugador
            print(tabulate(lista, headers="keys", tablefmt="grid"))
    if encontrado == False:
        print(f"El jugador con id '{id}' no existe.")

# Función para actualizar a un jugador
def actualizarJugador(jugadores, equipos):
    id = leer_int_mayor("id del jugador", 0)
    encontrado = False
    for jugador in jugadores:
        if jugador["id"] == id:
            encontrado = True
            lista = ["Nombre", "Posición", "Equipo", "Activo", "Sustitución"]
            indice = 1
            for entrada in lista:
                print(f"{indice}. {entrada}")
                indice = indice + 1
            # Input del usuario para el número de índice

def actualizarJugador(jugadores, equipos):
    id = leer_int_mayor("id del jugador", 0)
    encontrado = False
    for jugador in jugadores:
        if jugador["id"] == id:
            encontrado = True
            opcion = int(input("Introduce un número de índice: "))
            match opcion:
                # Actualizar nombre
                case 1:
                    nombreJugador = str
                    nombreJugador = comprobarString(nombreJugador, "nombre de jugador")
                    # Posición jugador, con clave nombre, es igual al nuevo nombre
                    jugador["nombre"] = nombreJugador
                # Actualizar posición
                case 2:
                    nombrePosicion = str
                    nombrePosicion = comprobarString(nombrePosicion, "posición")
                    # Posición jugador, con clave posicion, es igual a la nueva posición
                    for jugadorPosicion in jugadores:
                        if (jugadorPosicion["posicion"] == nombrePosicion
                        and jugadorPosicion["activo"] == True
                        and jugadorPosicion["equipo"] == jugador["equipo"]):
                            print(f"La nueva posición ya esta ocupada por otro jugador. El jugador con id '{jugador["id"]}' tendra la posición de suplente")
                            jugador["activo"] = False
                # Actualizar equipo
                case 3:
                    equipoEncontrado = False
                    print("Introduce el id del equipo a actualizar: ")
                    idEquipo = leer_int_mayor("id del equipo", 0)
                    for equipo in equipos:
                        if equipo["id"] == idEquipo:
                           equipoEncontrado = True
                    if equipoEncontrado == False:
                        print(f"El equipo '{idEquipo}' no existe.")
                    else:
                        for jugadorPosicion in jugadores:
                            if (jugadorPosicion["posicion"] == jugador["posicion"]
                                and jugadorPosicion["equipo"] == idEquipo):
                                    print(f"El jugador con id '{id}' tiene la misma posición que el jugador con id '{jugadorPosicion["id"]} en el equipo con id {idEquipo}'")
                # Actualizar activo/inactivo
                case 4:
                    if jugador["activo"] == False:
                        for jugadorPosicion in jugadores:
                            if jugador["posicion"] == jugadorPosicion["posicion"]:
                                print(f"El jugador con id '{jugadorPosicion["id"]}' tiene la misma posición que el jugador a activar.")
                                print(f"Se ha actualizado el jugador con id '{jugadorPosicion["id"]}' ha sido actualizado a inactivo ")
                                jugadorPosicion["activo"] = False
                        jugador["activo"] = True
                    else:
                        jugador["activo"] = False
                case _:
                    print("Error. El número introducido está fuera de rango. Introduzca un número válido")

# Función para desactivar a un jugador
def desactivarJugador(jugadores):
    id = leer_int_mayor("id del jugador", 0)
    for jugador in jugadores:
        if jugador["id"] == id:
            if jugador["activo"] == False:
                jugador["activo"] = True
            else:
                jugador["activo"] = False
            print(f"El jugador con id '{id}' ha sido cambiado a {jugador["activo"]}")
