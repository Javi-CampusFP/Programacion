# Crea una lista con los nombres de tus compañeros.
# Pide un nombre y muestra si se encuentra en la lista o no.
finalizar = False
lista = []
while not finalizar:
    nombre = str(input("Introduce un nombre: "))
    if nombre.lower() == "fin":
        finalizar = True
    else:
        lista.append(nombre)
nombreBuscar = str(input("Introduce un nombre a encontrar: "))
encontrado = False
for nombres in lista:
    if nombres == nombreBuscar:
        encontrado = True
        print(f"El nombre {nombreBuscar} se encuentra en la lista.")
if not encontrado:
    print(f"El nombre {nombreBuscar} no se encuentra en la lista.")