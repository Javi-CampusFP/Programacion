# 1. Escoger el número del 1 al 100
import random # Importar una librería que sirve para generar números "aleatorios".

adivinar = random.randrange(1, 100) # Almacenar el número random en la variable "adivinar" y darle un rango del 1 al 100.
# 2. Preguntar al usuario el numero que quiere escoger. 
numero = int(input("Introduce un numero del 1 al 100: "))
# 3. Hacer un bucle que compruebe que el número aleatorio no sea igual al introducido
while adivinar != numero:
# 3.a Si el usuario intenta meter un número mayor a 100 o menor a 1, recordarle el rango.
    if numero <= 0 or numero >= 101:
        numero = int(input("No pongas un numero menor a 1 o mayor a 100: "))
# 3.b Si es un número más grande al aleatorio, indicárselo al usuario y volver a pedirle el número.
    elif numero < adivinar:
        numero = int(input("El numero a adivinar esta por arriba del valor introducido. Intentalo de nuevo: "))
# 3.c Si es un número más pequeño al aleatorio, indicárselo al usuario y volver a pedirle el número.
    else:
        numero = int(input("El numero a adivinar esta por debajo del valor introducido. Intentalo de nuevo: "))
# 4. Imprimir que se ha ganado el juego por pantalla
print("¡Has ganado el juego!")
