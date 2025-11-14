# Pide números al usuario hasta que escriba 0.
# Muestra la suma total de los números introducidos.
# No uses break; controla la condición con while.
listaNumeros = []
numero = int(input("Introduce un número: "))
suma = 0
while numero != 0:
    suma = suma + numero
    listaNumeros.append(numero)
    numero = int(input("Introduce un número: "))
print(f"La suma total de los números es: {suma}")