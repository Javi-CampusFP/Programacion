# 1. Pedirle el input al usuario
palabra = str(input("Introduce una palabra: "))
# 2. Recorrer el string del revés

longitud = len(palabra)
while longitud < 2:
    palabra = str(input("No puedo invertir una palabra con 1 caracter. Intentalo de nuevo: "))
# 3. Concatenar el texto en una variable
invertida = ""
for invertir in range(len(palabra) - 1, -1, -1):
    invertida += palabra[invertir]
# 4. Mostrar el resultado final en pantalla
print(invertida)
