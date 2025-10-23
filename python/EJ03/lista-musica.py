# Declarar variables necesarias para la lista y el bucle
fin = False
listaCanciones = []
# Añadir cada una de ellas a la lista
while not fin:
    cancion = str(input("Escribe el nombre de una canción (introduce fin para salir): "))
# Comprobar si el usuario hizo input “fin” y finalizar el bucle
    while cancion == "fin" and len(listaCanciones) <= 0:
        cancion = str(input("La lista tiene que contener al menos 1 elemento. Intentalo de nuevo: "))
    listaCanciones.append(cancion)
    if cancion == "fin":
        fin = True
    else:
        listaCanciones.append(cancion)
print("Tu lista de reproducción: ")
indice = 1
for numero in listaCanciones:
    print(indice, ". ", numero)
    indice += 1
# Leer el input del usuario y que seleccione una canción por su índice y reproducirla.
introduce = int(input("Escribe el numero de indice de la canción a reproducir: "))
while introduce <= 0:
    introduce = int(input("Error. Intentalo de nuevo: "))
introduce -= 1
print("Reproduciendo: ", listaCanciones[introduce], "...")