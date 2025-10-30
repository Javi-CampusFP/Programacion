# 1. Pedirle la frase al usuario
frase = str(input("Introduce una frase para contar las vocales: "))
# 2. Saber la longitud de la frase
longitud = len(frase)
# 3. Declarar variables necesarias para hacer el bucle
bucle = 0
vocal = 0
# 4. Hacemos un bucle que recorra todos los caracteres y compruebe si es vocal o no.
while longitud != bucle:

    #if frase[bucle] == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U": <-- Esto no se porque no va (preguntar profe)
    
    # Comprobamos si el caracter que esta en la posicion bucle es una vocal, si es una vocal, añadimos 1 a vocal.
    # Repetir hasta que bucle sea igual que la longitud de la frase en caracteres
    if frase[bucle] in "aeiouAEIOU":
        vocal = vocal + 1
    bucle = bucle + 1 
# 5. Sacar el resultado por pantalla
print("El numero de vocales es: ", vocal)
