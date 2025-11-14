# Pide un número n y muestra los números desde n hasta 1 usando un bucle while.
print("Este programa pide un número y muestra todos los números hasta 0 entre medias")
numero = int(input("Introduce un número: "))
while numero != 0:
    numero = numero - 1
    print(numero)