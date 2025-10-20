lista = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo")
for dia in lista:
	print("- ",dia )
diaSemana = int(input("Escribe el indice del dia de la semana:"))

match diaSemana:
	case 1:
		print("Lunes")
	case 2:
		print("Martes")
	case 3:
		print("Miércoles")
	case 4:
		print("Jueves")
	case 5:
		print("Viernes")
	case 6:
		print("Sabado")
	case 7:
		print("Domingo")
	case _:
		print("Número fuera de rango")