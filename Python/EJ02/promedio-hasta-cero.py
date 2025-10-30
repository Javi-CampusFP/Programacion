# 1. Inicializar variables 
cero = False
suma = 0
cantidadNumeros = 0
# 2. Crear un bucle while y parar el bucle cuando se introduzca 0
while cero == False:
    numero = int(input("Introduce un numero. (Introduce 0 para parar de introducir numeros): "))
# 3. hacer el cálculo
    cantidadNumeros += 1
    if numero != 0:
        suma = suma + numero
    else:
        cero = True
resultado = suma / cantidadNumeros
# 4. Imprimir el resultado en pantalla
print("El promedio de los resultados es: ", resultado)
