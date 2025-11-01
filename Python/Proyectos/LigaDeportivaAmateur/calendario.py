# Declarar funciones
def menu():
    lista = ["Crear partido","Listar partidos","Reprogramar partido","Eliminar partido","Salir"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion
def crearPartido(id, lista):
    print()
def listarPartido(lista):
    print()
def reprogramarPartido(lista):
    print()
def eliminarPartido(lista):
    print()
