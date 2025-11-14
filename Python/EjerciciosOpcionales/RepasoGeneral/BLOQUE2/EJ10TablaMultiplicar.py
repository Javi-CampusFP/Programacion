# Pide un número del 1 al 10 y muestra su tabla de multiplicar.
# Usa un bucle for y f-strings.
print("Este programa muestra la tabla del 1 al 10 del número introducido")
numero = int(input("Introduce un número: "))
numeroDeMultiplicacion = 0
for numeroDeMultiplicacion in range(numero):
    numeroDeMultiplicacion = numeroDeMultiplicacion + 1
    print(f"{numeroDeMultiplicacion} x {numero} = {numeroDeMultiplicacion * numero}") 