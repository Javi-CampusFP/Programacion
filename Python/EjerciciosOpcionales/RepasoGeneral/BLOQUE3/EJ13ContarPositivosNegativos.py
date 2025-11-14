# Pide 6 números y guarda cada uno en una lista.
# Cuenta cuántos son positivos, negativos y ceros.
# Muestra los tres totales.
contador = 0
positivos = 0
negativos = 0
ceros = 0

listaNumeros = []
while contador != 6:
    numero = int(input("Introduce un número: "))
    listaNumeros.append(numero)
    contador = contador + 1 
for numeros in listaNumeros:
    if numeros < 0:
        negativos = negativos + 1
    elif numeros == 0:
        ceros = ceros + 1
    else:
        positivos = positivos + 1
print("Números positivos contados: {positivos}, Números negativos contados: {negativos}, Ceros contados: {ceros}")