# lógica del juego (funciones puras y utilidades)
import numpy as np
import random
from rich import print
# dtype data type, puedes definirlo como entero, y asi no salen como float en la matriz del tablero

# La función para crear el tablero
def generarTablero():
    return np.zeros((3, 3), dtype=int)

# Defino linea() que es más corto que hacer el print
def linea():
    print("------------------------------------------")

# Esta es la función que muestra las opciones al inicio, al usuario
def menu(lista):
    # Un índice automático
    indice = 1
    linea()
    # Recorro la lista e imprimo junto con el índice
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    linea()
    # Pedir la opción al usuario
    opcion = int(input("Introduce un número de índice: "))
    # Retornar el valor de la opción elegida 
    return opcion

# Recoger los nombres de los usuarios
def recogerNombre(jugadores):
    # Pido el nombre del jugador
    numeroJugador = len(jugadores) + 1 
    nombre = str(input(f"Introduce un nombre de jugador nº{numeroJugador}: "))
    # Mientras el nombre del jugador tenga una longitud igual a 0,
    # Pedir el nombre otra vez.
    while len(nombre) == 0:
        print("Error. El nombre no puede estar vacio.")
        nombre = str(input(f"Introduce un nombre de jugador nº{numeroJugador}: "))
    jugadores.append(nombre)

# Esta función se ejecuta siempre 1 vez, al inicio de la partida
# Elige el jugador que va a empezar a mover primero.
def primerTurnoElegirJugador (jugadores):
    # Hace la elección
    eleccion = random.randint(0,1)
    match eleccion:
        # El jugador número 1 empieza
        case 0:
            print(f"El jugador con nombre '{jugadores[eleccion]}' empieza el primer turno.")
            return 0
        # El jugador número 2 empieza
        case 1:
            print(f"El jugador con nombre '{jugadores[eleccion]}' empieza el primer turno.")
            return 1

def comprobarSiguienteTurno (turno,jugadores):
    match turno:
        case 0:
        # Si el anterior turno, el jugador 1 hizo un movimiento, ahora lo hara el jugador 2
            print(f"Turno del jugador con nombre: {jugadores[1]}")
            return 1
        # Si el anterior turno, el jugador 2 hizo un movimiento, ahora lo hara el jugador 1
        case 1:
            print(f"Turno del jugador con nombre: {jugadores[0]}")
            return 0

def comprobarEmpate (tablero):
    print()
def comprobarVictoria (tablero):
    print()

def comprobarNumeroFueraRango(coordenada):
    while input > 2 or input < 0:
        print(f"Error. La coordenada '{coordenada}' no puede salirse fuera del tablero")
        input = int(input(f"Introduce la coordenada '{coordenada}':"))