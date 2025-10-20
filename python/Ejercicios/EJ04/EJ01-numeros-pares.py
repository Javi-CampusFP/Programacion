# Definir variables
listaNumeros = []
# Definir funciones
# Función para agregar los números que queramos
def agregarNumero():
    numero = int(input("Introduce los números (introduce 0 para finalizar): "))
    while numero != 0:
        listaNumeros.append(numero)
        numero = int(input("Introduce los números (introduce 0 para finalizar): "))
# Función que requiere un parametro (una lista) y la recorre
# Si el item de la lista divido entre 2 da 0, suma uno a pares
def recorrerLista(numeroLista):
    pares = 0
    for par in numeroLista:
        if par % 2 == 0:
            pares = pares + 1
    return pares
# Lógica del programa
# Llama a agregarNumero() para agregar números a la lista
agregarNumero()
# Imprime el valor de números pares en la lista
print(f"El número de pares es: {recorrerLista(listaNumeros)}")
