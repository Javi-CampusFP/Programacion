negativo = False
suma = 0
while negativo == False:
	numero = int(input("Escribe un numero: "))
	if numero < 0:
		negativo = True
	else:
		suma = suma + numero
print("La suma total de los numeros introducidos es: ", suma)  