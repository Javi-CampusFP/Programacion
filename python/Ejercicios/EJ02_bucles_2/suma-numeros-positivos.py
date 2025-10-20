print("Programa de suma de numeros positivos.")
# Introducimos el numero en una variable
numero = int(input("Introduce un número positivo para sumarlo (0 finaliza el programa): "))
# Inicializamos la variable suma con un 0, donde almacenaremos toda la suma de los numeros.
suma = 0
# Inicializamos la variable cuentaNumerosSuma, la cual nos dirá cuántos números ha introducido el usuario (positivos)
cuentaNumerosSuma = 0
# Mientras el numero introducido no sea 0 hacer el bucle
while numero != 0:
# Condicionales para comprobar si el número es menor a 0
    if numero < 0:
        print(f"El numero {numero} no se ha sumado porque es menor a 0.")
    else:
# Si no es 0 sumar el número en la variable suma, indicar al usuario que se sumó, y sumar 1 a la variable cuentaNumerosSuma
        print(f"El numero {numero} se ha sumado.")
        suma = suma + numero
        cuentaNumerosSuma += 1
# Pedir otra vez un input, puesto que sino el bucle sería infinito.
    numero = int(input("Introduce un número positivo para sumarlo (0 finaliza el programa): "))
# Imprimir el resultado por pantalla
print(f"El número de números positivos introducidos ha sido: {cuentaNumerosSuma}")
print(f"La suma total de los numeros es: {suma}")
