# Declaramos las variables globales
listaNumeros = []

# Declaramos las funciones
def agregarNumeros():
    numero = int(input("Introduce un número (introduce 0 para finalizar.): "))
    while numero != 0:
        listaNumeros.append(numero)
        numero = int(input("Introduce un número (introduce 0 para finalizar.): "))

def contarPares(numeroLista):
    pares = 0
    for numeroPar in numeroLista:
        if numeroPar % 2 == 0:
            pares = pares + 1
    return pares


# Lógica del programa
agregarNumeros()
#contarPares(listaNumeros)
print(f"El número de pares introducidos es: {contarPares(listaNumeros)}")
