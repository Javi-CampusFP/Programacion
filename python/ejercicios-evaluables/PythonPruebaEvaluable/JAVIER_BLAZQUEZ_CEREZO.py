# PRUEBA EVALUABLE 1-1T-DAM1-GETAFE
# JAVIER BLÁZQUEZ CEREZO
# TIPO A
# Creamos un diccionario con el nombre de los alumnos y las 3 notas
# Declaramos variables necesarias:
eleccionUsuario = 0
alumnosDiccionario = {}
while eleccionUsuario != 5:
    # Este es el menú que se repetira cada vez que el usuario salga de un apartado
    print("1. Añadir alumno")
    print("2. Listar alumnos")
    print("3. Media de un alumno")
    print("4. Estadísticas de un grupo")
    print("5. Salir")
    eleccionUsuario = int(input("Escribe una de las opciones para continuar: "))
    match eleccionUsuario:
        case 1:
            # Pedimos el nombre del alumno
            nombreAlumno = str(input("Añade el nombre del alumno a evaluar (escribe 'fin' para volver al menú): "))
            # Hacemos un bucle while para comprobar si el input introducido es "fin"
            while nombreAlumno.lower() != "fin":

                # Pedimos las notas a calcular y comprobamos si el número esta entre el 0 y 10 para cada una de ellas, si no está entre el 0 y el 10, se pide otra vez.
                n1 = float(input(f"Introduce la nota número 1 de {nombreAlumno} : "))
                while n1 > 10 or n1 < 0:
                    n1 = float(input(f"Introduce una nota del 0 al 10. Vuelve a intentarlo: "))
                n2 = float(input(f"Introduce la nota número 2 de {nombreAlumno} : "))
                while n2 > 10 or n2 < 0:
                    n2= float(input(f"Introduce una nota del 0 al 10. Vuelve a intentarlo: "))
                n3 = float(input(f"Introduce la nota número 3 de {nombreAlumno} : "))
                while n3 > 10 or n3 < 0:
                    n3 = float(input(f"Introduce una nota del 0 al 10. Vuelve a intentarlo: "))
                
                # Actualizamos el diccionario con los datos agregados
                alumnosDiccionario.update({nombreAlumno : (n1, n2, n3)})
                print(alumnosDiccionario)
                
                # Volvemos a pedir el valor que comprueba el bucle, para que no sea un bucle infinito.
                nombreAlumno = str(input("Añade el nombre del alumno a evaluar (escribe 'fin' para volver al menú): "))
        case 2:
            
            # Mostramos los alumnos, en el orden en el que se metieron: 
            print("Lista de alumnos: ")
            
            # Hacemos un bucle for para recorrer el diccionario y hacer un print al valor del nombre del alumno
            for alumnos in alumnosDiccionario:
                print(f"- {alumnos}")
        case 3:
            # Media de un alumno
            evaluarAlumno = str(input("Escribe el nombre del alumno a calcular la media: "))
            if evaluarAlumno in alumnos:
                notas = alumnos[evaluarAlumno]
                media = sum(notas) / 3
                estado = "APROBADO" if media >= 5.0 else "SUSPENSO"
                print(f"{evaluarAlumno}: media = {media:.2f} -> {estado}")
            else:
                print(f"No se encontró al alumno '{evaluarAlumno}'.")
        case 4:
            totalAlumnos = len(alumnos)
            if totalAlumnos == 0:
                print("No hay alumnos para calcular estadísticas.")
            else:
                suma_total = 0.0
                aprobados = 0
                for notas in alumnos.values():
                    suma_total += sum(notas)
                    media_alumno = sum(notas) / 3
                    if media_alumno >= 5.0:
                        aprobados += 1
                media_global = suma_total / (totalAlumnos * 3)
                porcentaje_aprobados = (aprobados / totalAlumnos) * 100
                print(f"Total de alumnos: {totalAlumnos}")
                print(f"Media global del grupo: {media_global:.2f}")
                print(f"Aprobados (por media): {aprobados} -> {porcentaje_aprobados:.1f}%")
        case 5:
            print("Ha salido del programa")
        case _:
            print("Has introducido un número de índice inválido. Inténtalo de nuevo")
else:
    print("Ha salido el programa")