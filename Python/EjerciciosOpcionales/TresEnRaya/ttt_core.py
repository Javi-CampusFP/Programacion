# lógica del juego (funciones puras y utilidades)
import numpy as np
import random
from rich import print
# dtype data type, puedes definirlo como entero, y asi no salen como float en la matriz del tablero

# La función para crear el tablero
def generarTablero():
    # dtype es para definir el tipo. Objeto deja cambiar de floats a strings.
    return np.zeros((3, 3), dtype=object)
def separacion():
    print()
    print("------------------------------------------")
    print()

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

def comprobarResultado(tablero,turno,jugadores):
    hayResultado = False
    variable = str()
    match turno:
        case 0:
            variable = "X"
        case 1:
            variable = "O"
    # Comprobar si se ha ganado horizontalmente

    # Recorrer toda la fila en un rango de 3
    for fila in range(3):
        # Establecer un contador
        contador = 0
        # Recorrer todas las columnas en un rango de 3
        for col in range(3):
            # Si la posición fila,col tiene un dato igual a variable:
            if tablero[fila,col] == variable:
                # Sumar 1 a contador
                contador = contador + 1
            # Si el contador es tres, entonces ha ganado el jugador con una fila horizontal
            if contador == 3:
                hayResultado = True
                separacion()
                print(f"¡El jugador '{jugadores[turno]}' ha ganado! ")
                separacion()
                return "victoria"
    # Comprobar si se ha ganado verticalmente con el mismo método
    for columna in range(3):
        contador = 0
        for fila in range(3):
            if tablero[fila,columna] == variable:
                contador = contador + 1
            if contador == 3:
                hayResultado = True
                separacion()
                print(f"¡El jugador '{jugadores[turno]}' ha ganado! ")
                separacion()
                return "victoria"
    # Diagonal principal
    contador = 0
    for indice in range(3):
        fila = indice
        columna = indice
        if tablero[fila, columna] == variable:
            contador += 1
    if contador == 3:
        hayResultado = True
        separacion()
        print(f"¡El jugador '{jugadores[turno]}' ha ganado! ")
        separacion()
        return "victoria"

    # Diagonal secundaria
    contador = 0
    for indice in range(3):
        fila = indice
        columna = 2 - indice
        if tablero[fila, columna] == variable:
            contador += 1
    if contador == 3:
        hayResultado = True
        separacion()
        print(f"¡El jugador '{jugadores[turno]}' ha ganado! ")
        separacion()
        return "victoria"

    # Si no quedan casillas con el valor 0, y no hay un resultado, entonces se lanza un empate.
    if 0 not in tablero and not hayResultado:
        print("Ha habido un empate.")
        return "Empate"
    else:
        return "N/A"

def comprobarPosicion(eje):
    coordenada = int(input(f"Introduce una coordenada en el eje '{eje}': ")) - 1
    while (coordenada > 2) or (coordenada  < 0):
        print(f"Error. La coordenada en el eje '{eje}' no puede salirse fuera del tablero")
        coordenada = int(input("Introduce una coordenada: "))
    return coordenada
# Esta función cálcula si la IA realizara un movimiento perfecto
# Dependiendo de la dificultad elegida.
def probabilidadMax(dificultad):
    # Margen de error, a la alza de la dificultad
    aleatoriedad = random.randint(0,10) * 0.01
    match dificultad:
        case 1:
            return aleatoriedad + 0.40
        case 2:
            return aleatoriedad + 0.60
        case 3:
            return aleatoriedad + 0.90
        case _:
            print("Error. Ha introducido un número fuera de rango.")

def calculoProbabilidad(probabilidad):
    suerte = random.randint(0,100) * 0.01
    if suerte > probabilidad:
        return False
    else:
        return True

def posicionRandom(posiciones,tablero):
    rangoLongitud = len(posiciones) - 1
    seleccion = random.randint(0,rangoLongitud)
    tablero[seleccion] = "X"

def posicionesLibres(tablero):
    movimientosDisponibles = []
    for col in range(3):
        for fila in range(3):
            if tablero[col,fila] == 0:
                movimientosDisponibles.append((col,fila))
    return movimientosDisponibles

def algoritmoMinimax(tablero,posiciones,profundidad,esta_maximizando,turno,jugadores):
    if comprobarResultado(tablero,turno,jugadores) == "victoria" and (turno == 1):
        return int(100000)
    elif comprobarResultado(tablero,turno,jugadores) == "victoria" and (turno == 0):
        return int(-100000)
    elif comprobarResultado(tablero,turno,jugadores) == "Empate":
        return 0
    if esta_maximizando:
        maximo = -10000
        for row in range(3):
            for col in range(3):
                print()
