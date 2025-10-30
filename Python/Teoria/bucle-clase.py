numero = int(input("Contar numeros pares desde 1 hasta X: "))

while numero <= 0:
	numero = int(input("Error. Introduce un numero mayor a 0. (>0): "))

par = 0

for numeros in range(numero):
	numeros += 1 
	if numeros % 2 == 0:
		par += 1
print("Hay", par, "pares entre 1 y ",numero)
