# Declaramos las variables globales
listaNumeros = []

# Declaramos las funciones
def agregarNumeros():
    numero = int(input("Introduce un número (introduce 0 para finalizar.): "))
    while numero != 0:
        listaNumeros.append(numero)
        numero = int(input("Introduce un número (introduce 0 para finalizar.): "))

def numeroGrande(numeroLista):
    maximo = 0
    for numeroGrande in numeroLista:
        if maximo < numeroGrande:
             maximo = numeroGrande
    return maximo


# Lógica del programa
agregarNumeros()
#contarPares(listaNumeros)
print(f"El número más grande introducido es: {numeroGrande(listaNumeros)}")
