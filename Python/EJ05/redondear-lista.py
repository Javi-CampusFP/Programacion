# Variables
listaNumeros = [1.3, 4.76, 23.65, 12.3, 12.5, 12.8]
# Funciones
def redondear(numero):
    return round(numero)
# Lógica del código
print(list(map(redondear,listaNumeros)))