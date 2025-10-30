
# 1. Pedirle al usuario un número.
numero = int(input("Escribe un numero (>0): "))
# Comprobamos si el numero que han metido es un numero valido (mayor a 0) 

# 2. Comprobar si el resto de una división entre 2 da 0.
comprobacion = numero % 2
# 3. Si da 0 es par sino es impar. 
if comprobacion == 0:
# 4. Imprimir el resultado en pantalla. 
    print("El numero", numero, "es par.")
else:
    print("El numero", numero,"es impar.")
