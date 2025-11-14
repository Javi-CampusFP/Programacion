# Pide un número entero al usuario e indica si es par o impar.
# Usa el operador módulo (%).
print("Este programa indica si el número introducido es par o impar")
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número introducido es par.")
else:
    print("El número introducido es impar")