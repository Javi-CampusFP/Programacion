# importar librerias
from utiles import comprobarString
from utiles import leer_int
# Declarar funciones

def menu():
    # Declarar una lista con las entradas
    lista = ["Alta de jugador","Listar jugadores","Buscar jugador por id",
    "Actualizar jugador","Desactivar jugador","Salir"]
    indice = 1
    # Recorrer la lista e imprimir el indice a su vez
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    # Pedir input del usuario y retornarlo
    opcion = int(input("Introduce una opción del menú: "))
    return opcion

# Función para dar de alta a un jugador
def darAltaJugador(id, jugadores, equipo):
    # Declarar las variables para que no den error
    nombreJugador = str
    posicion = str
    # Declarar las variables de encontrado y activo en falso, si encuentra el equipo,
    # simplemente le ponemos en encontrado = True, y si activo es Falso, entonces se lo podemos indicar.
    encontrado = False
    activo = False
    sustitucion = False
    # Introducir el id del equipo
    idEquipo = int(input("Introduce el id del equipo a agregar el nuevo jugador: "))
    # para cada elemento en la lista del equipo
    for elemento in equipo:
        # Validar si el elemento en la posición id es igual a idEquipo, si es, entonces seguir
        # con el condicional
        if elemento["id"] == idEquipo:
            encontrado = True
            # Si es activo, cambiar la variable a activo
            if elemento["activo"] == True:
                activo = True
                # Pedir nombre y posición
                nombreJugador = comprobarString(nombreJugador, "nombre")
                posicion = comprobarString(posicion, "posición")
                # Comprobar si en el diccionario ya existe en ese mismo equipo y en la posición que intentamos
                # meter el nuevo jugador, si hay, se le indica y se pone como sustituto
                for jugador in jugadores:
                    if jugador["equipo"] == idEquipo and jugador["posicion"] == posicion:
                        print(f"Error. El equipo con id '{idEquipo}' ya tiene a un jugador en esa posición.")
                        sustitucion = True
                        print(f"El nuevo jugador con id de jugador '{id}' ha sido puesto como sustituto en la posición '{posicion}'")
    jugadores.append({"id" : id, "nombre" : nombreJugador, "equipo" : idEquipo, "posicion" : posicion})

    if encontrado == False or activo == False:
        print(f"El equipo con id '{id}' no ha sido encontrado o el equipo con id {idEquipo} esta inactivo.")

# Función para listar a los jugadores de una lista
def listarJugadores(jugadores):
    print()
# Función para buscar a un jugador por id
def jugadorPorId(jugadores):
    print()
# Función para actualizar a un jugador
def actualizarJugador(jugadores):
    print()
# Función para desactivar a un jugador
def desactivarJugador(jugadores):
    print()
