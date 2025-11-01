# Declarar funciones
def menu():
    # Declarar una lista con las entradas
    lista = ["Alta de jugador","Listar jugadores","Buscar jugador por id",
    "Actualizar jugador","Desactivar jugador","Salir"]
    indice = 1
    # Recorrer la lista e imprimir el indice a su vez
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    # Pedir input del usuario y retornarlo
    opcion = int(input("Introduce una opción del menú: "))
    return opcion
