# Declarar funciones
def menu():
    lista = ["Registrar resultado","Clasificación","Estádisticas por equipo","Salir"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion
def registrarResultado(lista):
    print()
def clasificacionEquipo(lista):
    print()
def estadisticasEquipo(lista):
    print()
