# Importo la librería que he creado
import ttt_core
from ttt_core import comprobarSiguienteTurno, linea, posicionesLibres
# Variables
# Creo la variable opción para que no me de error en el while
opcion = 0
# Lista de las opciones del ménu
lista = ["Jugador vs Jugador","Jugador vs Máquina","Salir"]
# Lista de las dificultades disponibles
# Fácil 60% de minimax, 40% random. Normal 75% minimax. Difícil 90% minimax.
dificultades = ["Fácil", "Normal", "Difícil"]
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
    # Genero el tablero llamando a la función y lo guardo en la variable tablero
    tablero = ttt_core.generarTablero()
    match opcion:
        # Jugador vs Jugador
        case 1:
            print("Has accedido al modo Jugador vs Jugador.")
            # Pido el nombre de los jugadores
            while len(jugadores) != 2:
                ttt_core.recogerNombre(jugadores)
            # Se elige quien va a poner una posición primero
            jugadorTurno = ttt_core.primerTurnoElegirJugador(jugadores)
            # Mientras el resultado sea "N/A" (ni empate, ni victoria):
            while resultado == "N/A":
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
                        tablero[ejeY,ejeX] = "O"
                    case 1:
                        tablero[ejeY,ejeX] = "X"
                resultado = ttt_core.comprobarResultado(tablero,jugadorTurno,jugadores)
        # Juego contra la IA
        case 2:
            # Añade el nombre del jugador
            ttt_core.recogerNombre(jugadores)
            # Añade "IA" a la lista jugadores
            jugadores.append("IA")
            # Esto llama a la función para declarar uno aleatoriamente
            jugadorTurno = ttt_core.primerTurnoElegirJugador(jugadores)
            opcionDificultad = ttt_core.menu(dificultades)
            while resultado == "N/A":
                linea()
                print(tablero)
                linea()
                # Cuando se ha declarado, se resta 1 o se suma 1, en cuestión de quien
                # haya sido el último jugador en tirar.
                jugadorTurno = comprobarSiguienteTurno(jugadorTurno,jugadores)
                match jugadorTurno:
                    case 0:
                        ejeY = ttt_core.comprobarPosicion("Y")
                        ejeX = ttt_core.comprobarPosicion("X")
                        tablero[ejeY,ejeX] = "O"
                    case 1:
                        probabilidad = ttt_core.probabilidadMax(opcionDificultad)
                        decisionFinal = ttt_core.calculoProbabilidad(probabilidad)
                        casillasLibres = ttt_core.posicionesLibres()
                        match decisionFinal:
                            case True:
                                # Aquí se ejecuta el algoritmo minimax, un movimiento perfecto.
                                ttt_core.algoritmoMinimax(tablero)
                            case False:
                                # Aqui se ejecuta un número de casilla aleatorio en el tablero
                                ttt_core.posicionRandom(casillasLibres,tablero)
                resultado = ttt_core.comprobarResultado(tablero,jugadorTurno,jugadores)
        # Has salido del juego.
        case 3:
            print("Has salido del juego.")
        case _:
            print("Has introducido un número fuera del rango.")
