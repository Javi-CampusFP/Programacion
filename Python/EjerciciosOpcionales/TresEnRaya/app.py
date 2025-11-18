# Importo la librería que he creado
import ttt_core
from ttt_core import linea
# Variables
# Creo la variable opción para que no me de error en el while
opcion = 0
# Lista de las opciones del ménu
lista = ["Jugador vs Jugador","Jugador vs Máquina","Salir"]
# Lógica del juego
# Mientras no se elija la opción para salir se repite
while opcion != 3:
    # Jugadores que hay en la partida, necesario para función
    jugadores = []
    # Resultado de la partida por defecto es "N/A"
    resultado = "N/A"
    # Pedir la opción
    opcion = ttt_core.menu(lista)
    # El turno del jugador, saber a que jugador le toca
    jugadorTurno = 0
    # Saber si es el primer turno o no. Por defecto es "sí"
    primerTurno = True
    # Genero el tablero llamando a la función y lo guardo en la variable tablero
    tablero = ttt_core.generarTablero()
    match opcion:
        # Jugador vs Jugador
        case 1:
            # Mientras el resultado sea "N/A" (ni empate, ni victoria):
            while resultado == "N/A":

                # Si es el primer turno de la partida, pedir el nombre de los jugadores
                if primerTurno:
                    print("Has accedido al modo Jugador vs Jugador.")
                    # Pido el nombre de los jugadores
                    while len(jugadores) != 2:
                        ttt_core.recogerNombre(jugadores)
                    jugadorTurno = ttt_core.primerTurnoElegirJugador(jugadores)
                    primerTurno = False
                else:
                    # Después de cada turno, un resumen de como va el tablero
                    linea()
                    print(tablero)
                    linea()
                    # El jugador siguiente introduce una coordenada
                    jugadorTurno = ttt_core.comprobarSiguienteTurno(jugadorTurno,jugadores)
                    ejeY = ttt_core.comprobarPosicion("Y")
                    ejeX = ttt_core.comprobarPosicion("X")
                    while tablero[ejeY,ejeX] == "X" or tablero[ejeY,ejeX] == "O":
                        print("Error. Esa casilla ya esta ocupada. Elija otra distinta.")
                        ejeY = ttt_core.comprobarPosicion("Y")
                        ejeX = ttt_core.comprobarPosicion("X")
                    match jugadorTurno:
                        case 0:
                            tablero[ejeY,ejeX] = "X"
                        case 1:
                            tablero[ejeY,ejeX] = "O"
                    resultado = ttt_core.comprobarResultado(tablero,jugadorTurno,jugadores)
        # Juego contra la IA
        case 2:
            while resultado == "N/A":
                print()
            print()
        # Has salido del juego.
        case 3:
            print("Has salido del juego.")
        case _:
            print()
