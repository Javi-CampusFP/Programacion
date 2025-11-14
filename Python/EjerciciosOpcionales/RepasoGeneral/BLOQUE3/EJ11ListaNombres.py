# Pide al usuario 5 nombres y guárdalos en una lista.
# Después, muestra todos los nombres en mayúsculas.
contador = 0
listaNombres = []
while contador != 5:
    contador = contador + 1
    nombre = str(input(f"Introduce el nombre nº{contador}: "))
    listaNombres.append(nombre.capitalize())
print(listaNombres)