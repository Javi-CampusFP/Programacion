# Variables
listaFrases = ["hola", "como", "estas", "paco"]
# Funciones
def cambiarATitulo(frase):
    return frase.title()
# Lógica del código
listaTitulos = list(map(cambiarATitulo, listaFrases))
print(listaTitulos)