# Los dias de la semana puestos en una tupla, puesto que no van a cambiar
semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
# Declaramos las variables de las asistencias y de las ausencias
asistencias = 0
ausencias = 0
# Recorre cada dia de la semana y pregunta al usuario
for dia in semana:
	asiste = str(input(f"El alumno ha asistido el dia {dia} ('S' para sí, 'N' para no): "))
	# Comprobamos si el string introducido es s, y sumamos una a asistencia
	if asiste.lower() == "s":
		asistencias += 1
	# Comprobamos si el input es n, y sumamos a ausencia
	elif asiste.lower() == "n":
		ausencias += 1
	# Si el usuario introduce otro tipo de string no contemplado se le muestra el siguiente mensaje:
	else: 
		asiste = str(input("El programa no puede interpretar el valor introducido, intentalo de nuevo"))
# Calculamos el porcentaje
porcentaje = ( asistencias/5 ) * 100
# Mostramos el porcentaje en pantalla
print(f"El porcentaje de asistencias es: {porcentaje} %")
