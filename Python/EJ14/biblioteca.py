import random
import numpy as np
from pathlib import Path

# Imprime una lista con índice numerado
def imprimirLista(lista):
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1

# Comprueba si hay una partida guardada en el archivo
# Si el usuario elige comenzar nueva partida, borra el archivo
def comprobarGuardado(ruta, bucle):
    ruta = Path(ruta)
    if ruta.exists():
        print("El archivo de una partida anterior ha sido encontrado.")
        # Pregunta al usuario si quiere comenzar una nueva partida o continuar la anterior
        guardadoOpcion = str(input("¿Quiere empezar una nueva partida (S/N)?: "))
        match guardadoOpcion.lower():
            case "s":
                # Elimina el archivo anterior
                ruta.unlink()
                print("El archivo de la partida guardada anterior fue eliminado con éxito.")
                return False
            case "n":
                return True

# Genera el tablero inicial según el tamaño dado
def generarTablero (tamano):
    calculo = tamano * tamano + 1
    tablero = np.arange(1,calculo).reshape((tamano,tamano))
    return tablero

# Decide aleatoriamente si el barco será horizontal o vertical
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

# Genera un barco y lo coloca en el tablero según su tamaño y orientación
def generarBarco(orientacion,tablero,tamano,tamanoTablero,posicionBarcos,nombreBarco):
    margen = tamano - 1
    rangoVertical = 0 + margen
    rangoHorizontal = tamanoTablero - margen
    soportado = True
    piezas = tamano - 1
    horizontal = random.randrange(rangoVertical,rangoHorizontal)
    vertical = random.randrange(rangoVertical,rangoHorizontal)

    # Repite hasta encontrar una posición válida
    while tablero[vertical,horizontal] == 0 and soportado:
        match tamano:
            case 1 | 2 | 3:
                vertical = random.randrange(rangoVertical,rangoHorizontal)
                horizontal = random.randrange(rangoHorizontal,rangoVertical)
            case _:
                print(f"El tamaño '{tamano}' no es soportado por el sistema.")
                soportado = False

    # Marca el primer punto del barco
    tablero[vertical,horizontal] = 0
    posicionBarcos[nombreBarco] = [(vertical, horizontal)]

    # Completa el resto del barco según la orientación
    while piezas != 0 and soportado:
        match orientacion:
            case True:
                horizontal = horizontal - 1
            case False:
                vertical = vertical - 1
        tablero[vertical,horizontal] = 0
        posicionBarcos[nombreBarco].append((vertical,horizontal))
        piezas = piezas - 1

# Pide al usuario una coordenada dentro del rango permitido
def inputUsuario(eje,tamano):
    posicion = int(input(f"Introduce un número en el {eje} :"))
    while posicion > tamano or posicion < 0:
        print(f"Error. El número debe de estar entre el 1 y el {tamano}")
        posicion = int(input(f"Introduce un número en el {eje} :"))
    return posicion

# Comprueba si el disparo del jugador ha golpeado algún barco
def comprobarGolpe(ejeY,ejeX,barcos,tablero):
    encontrado = False
    for barco,posicion in list(barcos.items()):
        if (ejeY,ejeX) in posicion:
            encontrado = True
            posicion.remove((ejeY,ejeX))
            if len(posicion) == 0:
                print("Un barco ha sido hundido.")
                del barcos[barco]

    if encontrado:
        tablero[ejeY,ejeX] = 0
        return True
    else:
        tablero[ejeY,ejeX] = -1
        return False

# Muestra aviso de que la función de guardado aún no está disponible
def guardarPartida (confirmacion):
    print("Esta opción no está implementada por el momento.")
    if confirmacion:
        print("¿Estás seguro de querer salir a pesar de no estar implementado?")
        print("Esto hará que tu progreso no se guarde y perderás tu partida actual.")
        opcion = str(input("Introduce (S/N): "))
        match opcion.lower():
            case "s":
                print("Saliendo de la partida...")
                confirmacion = True
            case "n":
                print("Continuando la partida...")
                confirmacion = False
