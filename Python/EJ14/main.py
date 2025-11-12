import biblioteca
from rich import print

tablero = biblioteca.generarTablero()
numeroBarcos = 0
guardar = False
contadorBarcos = 0

while numeroBarcos == 0 or guardar:
    print(tablero)
    while contadorBarcos != 3:
        orientacion = biblioteca.horizontalVertical()
        match contadorBarcos:
            case 0:
                biblioteca.barco1(orientacion,tablero)
                print("Se ha colocado el barco 1")
            case 1:
                #biblioteca.barco2(orientacion,tablero)
                print("Se ha colocado el barco 2")
            case 2:
                #biblioteca.barco3(orientacion,tablero)
                print("Se ha colocado el barco 3")
        contadorBarcos = contadorBarcos + 1
    int(input())