# 1. Inicializar las variables
nombre = ""
lista = []
# 2. Comprobar si el nombre es fin o no
while nombre != "fin":
# 3. Pedirle al usuario el nombre.
    nombre = str(input("Escribe un nombre para la lista: "))
# 4. Comprobar si el nombre introducido es “fin”, si es, no meter en la lista “lista”
    if nombre != "fin":
        lista.append(nombre)
# 5. Imprimir el resultado por pantalla
print()
print("Los nombres ingresados son: ", lista)
print()
print("La lista con los nombres:")
for nombresIntroducidos in lista:
    print(" - ", nombresIntroducidos)
