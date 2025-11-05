# Variables
dicLibros = {"libro1" : "ensayo", "libro2" : "novela", "libro3" : "novela", "libro4" : "ensayo", "libro5" : "novela", "libro6" : "poesía"}
# Funciones
def libroEnsayo (libro):
    titulo,categoria = libro
    return categoria == "novela"
# Lógica del código
dicEnsayo = filter(libroEnsayo,dicLibros.items())
print(dict(dicEnsayo))