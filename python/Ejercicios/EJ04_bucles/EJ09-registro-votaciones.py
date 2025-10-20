# Lista de candidatos con los votos
candidatos = {"Ana" : 0, "Luis" : 0, "María": 0}
# Imprime los candidatos en pantalla
for candidato in candidatos:
    print(f"- {candidato}")
# Pide el input al usuario
voto = str(input("Introduzca un candidato a votar (introduce 'fin' para terminar): "))
while voto != "fin":
    # Si el nombre esta dentro de los candidatos se le suma 1 al entero del candidato
    if voto in candidatos:
        candidatos[voto] = candidatos[voto] + 1
    # Si el nombre del candidato introducido no esta dentro del diccionario se le indica al usuario
    else:
        print("Candidato no válido")
    # Bucle for para imprimir otra vez los usuarios
    for candidato in candidatos:
        print(f"- {candidato}")
    # Volver a pedirle un input al usuario
    voto = str(input("Introduzca un candidato a votar (introduce 'fin' para terminar): "))
# Busca el valor más alto, en el diccionario candidatos
# Valor clave = candidatos.get
# ganador = max(candidatos, key=candidatos.get)
# print("El ganador es: ", ganador)
