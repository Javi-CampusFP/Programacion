# Importar libreria random
import random
# elegimos un numero del 1 al 100 y lo metemos dentro de la variable numero
numero = random.randint(1, 100)

# pedimos un numero al usuario y lo ponemos dentro de la variable "adivinar"
adivinar = int(input("Escribe un numero: "))

# Comprobar si el numero es menor, igual o mayor al numero introducido, si es u
while adivinar != numero:
	if adivinar < numero:
		numero = int(input("El numero introducido es menor al numero aleatorio. Intentalo de nuevo: "))
	elif adivinar <= 0 or adivinar > 100:
		numero = int(input("El numero introducido esta fuera del rango (1 a 100). Intentalo de nuevo: "))
	else:
		numero = int(input("El numero introducido es mayor al numero aleatorio. Intentalo de nuevo: "))
print("¡Felicidades! Has adivinado el número")
