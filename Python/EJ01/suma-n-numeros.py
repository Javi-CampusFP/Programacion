# 1. Decirle al usuario que introduzca un número y leerlo
numero = int(input("Introduce un numero mayor a 0 (> 0): "))
# 2. Comprobamos si el número ingresado es igual o menor
# a 0, si es, pedir al usuario que introduzca otra vez un número mayor a 0.
while numero <= 0:
    numero = int(input("Error. Introduce un numero mayor a 0 (> 0): "))

# 3. Declaramos variables necesarias para los bucles.
bucle = 0
suma = 0
# 4. Hacemos la suma de los números
while bucle != numero:
    bucle = bucle + 1
    suma = suma + bucle
# 5. Sacamos el resultado en pantalla
print("La suma del ", numero, " hasta X es: ", suma)
