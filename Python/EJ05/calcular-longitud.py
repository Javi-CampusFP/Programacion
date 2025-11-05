# Variables
listaPalabras = ["Hola", "como", "estas?", "genial. Y tú?"]
# Funciones
def longitud(palabra):
    return len(palabra)
# Lógica del código
caracteres = map(longitud,listaPalabras)
print(list(caracteres))