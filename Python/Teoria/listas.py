lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print("Mi lista tiene ", len(lista1), "elementos.")
print("El elemento cuarto de mi lista es: ", lista1[3])
print("El elemento octavo de mi lista es: ", lista1[7])

print("Lista antes de añadir un valor", lista1)

lista1.append(9)

print("Lista despues de añadir un nuevo valor", lista1)

lista1.remove(lista1[4])

print("Lista despues de eliminar el elemento de orden 4", lista1)

