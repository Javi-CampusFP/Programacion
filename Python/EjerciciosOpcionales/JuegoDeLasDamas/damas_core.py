import numpy as np
import random
def imprimirMenu(lista):
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del índice: "))
    return opcion