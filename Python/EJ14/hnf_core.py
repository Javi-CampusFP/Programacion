import random
import numpy as np
# Imprimir una linea
def linea():
    print("-----------------------------------")

# Imprime una lista con índice numerado
def imprimirLista(lista):
    indice = 1
    linea()
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    try:
        linea()
        opcion = int(input("Introduce un número de índice: "))
        return opcion
    # Si el usuario mete algo que no sea un número, se le indica.
    except ValueError:
        print("Error. Introduce un número valido. ")

# Genera el tablero inicial según el tamaño dado
def generarTablero (tamano):
    tablero = np.zeros((tamano,tamano))
    return tablero

# Decide aleatoriamente si el barco será horizontal o vertical
def horizontalVertical():
    # Genera un número aleatorio para decidir si es horizontal o vertical
    aleatorio = random.randint(0,1)
    match aleatorio:
        # Horizontal
        case 0:
            return True
        # Vertical
        case 1:
            return False
# Definir el tamaño del barco aleatoriamente entre los tamaños que estan permitidos
def decidirTamano(tamanoBarcos):
    longitud = len(tamanoBarcos) - 1
    tamanoFinal = random.randint(0,longitud)
    return tamanoFinal
# Genera un barco y lo coloca en el tablero según su tamaño y orientación
def generarBarco(tablero,tamanoTablero,orientacion,tamanoBarco,posicionesBarco):
    margenFinal = tamanoTablero - tamanoBarco
    margenInicio = 0 + tamanoBarco
    posicionInicial = random.randint(margenInicio,margenFinal)
    match orientacion:
        # Horizontal
        case True:
            print("")
        # Vertical
        case False:
            print("")

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
