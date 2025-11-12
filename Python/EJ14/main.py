from pathlib import Path
import biblioteca
from rich import print

# Leyenda de los valores del tablero para el jugador
leyenda = [" '-1' Agua", " '0' Barco"]

tamanoTablero = 20
tableroBarcos = biblioteca.generarTablero(tamanoTablero)
tableroJugador = biblioteca.generarTablero(tamanoTablero)

cantidadBarcos = 0
guardar = False
primerBucle = True
primerIntento = True

# Comprueba si hay una partida guardada
archivoGuardado = biblioteca.comprobarGuardado("partida-guardata.txt",primerBucle)
golpeComprobado = bool()

# Barcos con sus respectivos tamaños
barcosTamano = {"barco1" : 2, "barco2" : 3, "barco3" : 4, "barco4" : 2}
posicionBarcos = {}
cantidadBarcos = len(barcosTamano)
# Bucle principal del juego
while not guardar and cantidadBarcos != 0:

    # Si existe un archivo de guardado y aún no se han colocado los barcos
    if archivoGuardado:
        # El usuario ha elegido continuar la partida
        print()

    else:
        print("-----------------------------------------")

    # Colocación de barcos en el primer bucle
    if primerBucle :
        cantidadBarcos = 0
        for barco,tamanoDelBarco in barcosTamano.items():
            cantidadBarcos = cantidadBarcos + 1
            orientacion = biblioteca.horizontalVertical()
            biblioteca.generarBarco(orientacion,tableroBarcos,tamanoDelBarco,tamanoTablero,posicionBarcos,barco)
        # Se actualiza a False para que no vuelva a colocar los barcos
        primerBucle = False
    else:
        print(tableroJugador)

        # Mensaje de resultado según el último disparo
        if golpeComprobado and not primerIntento:
            longitud = len(posicionBarcos)
            cantidadBarcos = longitud
            print("¡Le has dado a un barco!")

        if not golpeComprobado and not primerIntento:
            print("¡Mala suerte!. No le has dado a ningún barco.")

        # Muestra la cantidad de barcos restantes y la leyenda
        print(f"Quedan '{cantidadBarcos}' barcos restantes")
        print("- Leyenda: ")
        biblioteca.imprimirLista(leyenda)

        # Pide coordenadas al usuario
        ejeY = biblioteca.inputUsuario("Y",tamanoTablero)
        ejeX = biblioteca.inputUsuario("X",tamanoTablero)

        # Comprueba si se ha golpeado un barco
        golpeComprobado = biblioteca.comprobarGolpe(ejeY,ejeX,posicionBarcos,tableroJugador)
        primerIntento = False
        print(posicionBarcos)
# Cuando no quedan barcos, el jugador gana
print("¡Has ganado el juego de hundir la flota!")
