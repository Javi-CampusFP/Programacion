# Se definen los 3 contadores en una variable
contador1 = 0
contador2 = 0
contador3 = 0
# Se define el diccionario clave valor como se pidió en el enunciado con cada candidato.
candidatosDiccionario = {"Ana" : contador1, "Luis" : contador2, "María" : contador3}
# Se le pregunta al usuario a qué candidato va a votar.
candidatoVoto = str(input("Introduce el nombre de los candidatos a votar ('fin' para finalizar el programa): "))
while candidatoVoto != "fin":
print("Candidatos a votar: Ana, Luis, María")
# Comprobamos que nombre se ha introducido y sumamos el contador correspondiente
if candidatoVoto.lower() == "ana":
    contador1 += 1
elif candidatoVoto.lower() == "luis":
    contador2 += 1
elif candidatoVoto.lower() == "maría":
    contador3 += 1
else:
    print("Voto introducido no válido.")
# Introducir un nuevo candidato para introducir más votos.
candidatoVoto = str(input("Introduce el nombre de los candidatos a votar ('fin' para finalizar el programa): "))
# Imprimir el resultado por pantalla
print(f"El número de votos que ha recibido Ana: {candidatosDiccionario["Ana"]} ")
print(f"El número de votos que ha recibido Luis: {candidatosDiccionario["Luis"]} ")
print(f"El número de votos que ha recibido María: {candidatosDiccionario["María"]} ")
# Comprobamos quién ha sido el ganador. Si ninguno es mayor a ninguno, es un empate.
if contador1 > contador2 and contador1 > contador3:
    print("El ganador o ganadora es Ana.")
elif contador2 > contador1 and contador2 > contador3:
    print("El ganador o ganadora es Luis.")
elif contador3 > contador1 and contador3 > contador2:
    print("El ganador o ganadora es María.")
else:
    print("Hay un empate entre los candidatos.")
