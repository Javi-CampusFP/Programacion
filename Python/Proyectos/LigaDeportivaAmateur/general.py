# Este es el módulo para funciones generales, que no van dentro de las demás
# para dejar el app.py más compacto

# Función del menú principal
def menu():
    lista = ["Gestión de equipos", "Gestión de jugadores",
    "Calendario de partidos", "Resultados y clasificación", "Salir"]
    # Pongo un índice automático porque esto a la larga es más fácil de mantener
    # que meter el número dentro del string
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion

# Función para generar un id
def generarId(id):
    id = id + 1
    return id
