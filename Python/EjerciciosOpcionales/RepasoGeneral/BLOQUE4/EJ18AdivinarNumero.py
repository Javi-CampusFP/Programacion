# Usa la librería random.
import random
# Genera un número aleatorio entre 1 y 10.
# Pide al usuario que adivine el número y da pistas (“más alto” o “más bajo”) hasta acertar.
numeroAleatorio = random.randint(1,10)
numeroEncontrado = False
while not numeroEncontrado:
    numero = int(input("Introduce un número: "))
    if numero > numeroAleatorio:
        print("El número es más bajo.")
    elif numero == numeroAleatorio:
        numeroEncontrado = True
        print("¡Has acertado!")
    else:
        print("El número es más alto.")