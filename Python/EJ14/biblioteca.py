import random
import numpy as np

def generarTablero ():
    tablero = np.arange(1,401).reshape((20,20))
    return tablero

def horizontalVertical():
    # Genera un número aleatorio para decidir si es horizontal o vertical
    aleatorio = random.randrange(0,2)
    match aleatorio:
        # Horizontal
        case 0:
            return True
        # Vertical
        case 1:
            return False

def barco1(orientacion,tablero):
    # Definir la posición del barco
    vertical = random.randrange(1,19)
    horizontal = random.randrange(1,19)
    tablero[vertical,horizontal] = 0
    match orientacion:
        # Horizontal
        case True:
            horizontal = horizontal - 1
            tablero[vertical,horizontal] = 0
        # Vertical
        case False:
            vertical = vertical - 1
            tablero[vertical,horizontal] = 0


def barco2(orientacion):
    # Definir la posición del barco
    aleatorio = random.randrange(2,18)
    match orientacion:
        # Horizontal
        case True:
            print()
        # Vertical
        case False:
            print()

def barco3(orientacion):
    # Definir la posición del barco
    aleatorio = random.randrange(3,17)
    match orientacion:
        # Horizontal
        case True:
            print()
        # Vertical
        case False:
            print()