# Importar librerias
# Variables
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Funciones
def sumar_5(numero):
    return numero + 5
# Lógica del código
listaFinal = list(map(sumar_5, listaNumeros))
print(listaFinal)