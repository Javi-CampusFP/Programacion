print("Seleccione una operacion:")
print()
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print()
# 1. Saber qué tipo de operacion quiere realizar el usuario.
operacion = int(input("Seleccione la operacion deseada (numero): "))
# Mientras el número introducido por el usuario sea menor o igual a 0, y mayor a 4 se le pide el input otra vez.
while operacion <= 0 or operacion > 4:
    operacion = int(input("Error. Numero seleccionado no valido. Elija la operacion introduciendo un numero del 1 al 4: "))
# 2. Comprobar si el usuario eligio multiplicacion, resta, suma o division.
if operacion == 1 or operacion == 2 or operacion == 3:
    numero1 = int(input("Introduzca el primer numero de la operacion: "))
    numero2 = int(input("Introduzca el segundo numero de la operacion: "))

if operacion == 1:
    resultado = numero1 + numero2
elif operacion == 2:
    resultado = numero1 - numero2
elif operacion == 3:
    resultado = numero1 * numero2
# 3. Si se elijio division comprobar si el usuario ha metido un numero igual a 0 en alguno de los 2 numeros.
else:
    numero1 = int(input("Introduzca el primer numero de la operacion: "))
    while numero1 == 0:
        numero1 = int(input("Error. El numero no puede ser 0. Introduzca el primer numero de la operacion: "))
        numero2 = int(input("Introduce el segundo numero de la operacion: "))
    while numero2 == 0:
        numero2 = int(input("Error. El numero no puede ser 0. Introduzca el segundo numero de la operacion: "))
    resultado = numero1 / numero2
# 4. Imprimir el resultado en pantalla
print("El resultado de la operación es: ", resultado)