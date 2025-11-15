# Pide al usuario 4 notas (de 0 a 10) y calcula la media.
# Indica si está aprobado (≥5) o suspenso (<5).
contador = 0
listaNotas = []
while contador != 4:
    contador = contador + 1
    nota = float(input(f"Introduce la nota nº{contador}: "))
    listaNotas.append(nota)
indice = 1
media = 0
contador = 0
for notas in listaNotas:
    media = media + notas
    contador = contador + 1
mediaFinal = media / contador
if mediaFinal > 5:
    print(f"Has aprobado con un '{mediaFinal}' de media")
else:
    print(f"Has suspendido con un '{mediaFinal}' de media")
