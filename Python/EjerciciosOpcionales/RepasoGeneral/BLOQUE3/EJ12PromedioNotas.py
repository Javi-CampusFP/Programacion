# Pide al usuario 4 notas (de 0 a 10) y calcula la media.
# Indica si está aprobado (≥5) o suspenso (<5).
contador = 0
listaNotas = []
while contador != 4:
    contador = contador + 1
    nota = float(input(f"Introduce la nota nº{contador}: "))
    listaNotas.append(nota)
indice = 1
for notas in listaNotas:
    if notas > 5:
        print(f"La nota nº {indice} con valor {notas} esta aprobada.")
    else:
        print(f"La nota nº {indice} con valor {notas} esta suspensa.")
    indice = indice + 1