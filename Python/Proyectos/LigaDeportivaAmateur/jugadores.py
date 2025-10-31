# Declarar funciones
def menu():
    lista = ["Alta de jugador","Listar jugadores","Buscar jugador por id",
    "Actualizar jugador","Desactivar jugador","Salir"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion
