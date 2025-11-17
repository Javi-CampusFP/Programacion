# interfaz de consola y bucles de juego
# Importo la librería que he creado
import ttt_core
from ttt_core import linea
# Creo las variables correspondientes
# Genero el tablero llamando a la función y lo guardo en la variable tablero
tablero = ttt_core.generarTablero()
# Creo la variable opción para que no me de error en el while
opcion = 0
# Jugadores que hay en la partida, necesario para función
jugadores = []
# Saber si es el primer turno o no. Por defecto es "sí"
primerTurno = True
# Resultado de la partida por defecto es "N/A"
resultado = "N/A"
# Lista de las opciones del ménu
lista = ["Jugador vs Jugador","Jugador vs Máquina","Salir"]
# El turno del jugador, saber a que jugador le toca
jugadorTurno = 0
# Lógica del juego
# Mientras no se elija la opción para salir se repite
while opcion != 3:
    # Pedir la opción 
    opcion = ttt_core.menu(lista)

    match opcion:
        # Jugador vs Jugador
        case 1:
            # Mientras el resultado sea "N/A" (ni empate, ni victoria):
            while resultado == "N/A":
                print("Has accedido al modo Jugador vs Jugador.")
                # Si es el primer turno de la partida, pedir el nombre de los jugadores
                if primerTurno:
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
                    coordenada = int(input("Introduce la coordenada : "))
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
