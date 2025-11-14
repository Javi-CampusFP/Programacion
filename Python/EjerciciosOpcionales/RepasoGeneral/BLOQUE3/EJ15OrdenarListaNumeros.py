# Pide 5 números, guárdalos en una lista y muestra:
    # La lista original
    # La lista ordenada
        # Usa los métodos de lista (append, sort).
listaNumeros = []
contador = 0

while contador != 5:
    contador += 1
    numeros = int(input("Introduce un número: "))
    listaNumeros.append(numeros)

print("Lista original:")
print(listaNumeros)

listaNumeros.sort()

print("Lista ordenada:")
print(listaNumeros)