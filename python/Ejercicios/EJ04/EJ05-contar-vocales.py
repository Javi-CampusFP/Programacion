# Definir variables
nombreIntroducido = str(input("Introduce un nombre: "))
# Definir funciones
def contarVocales(nombre):
    numeroVocales = 0
    vocales = "aeiouAEIOU"
    for letras in nombre:
        if letras in vocales:
            numeroVocales = numeroVocales + 1
    return numeroVocales
# Lógica del programa
print(f"La palabra {nombreIntroducido} tiene una cantidad de vocales de: {contarVocales(nombreIntroducido)}")
