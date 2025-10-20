# Menú
print("1. Añadir alumno a un curso")
print("2. Mostrar todos los cursos y alumnos")
print("3. Buscar alumno por nombre")
print("4. Ver número total de alumnos")
print("5. Salir")
opcion = int(input("Introduce un número de índice: "))
clases = {"DAM1" : [], "DAM2" : []}
while opcion != 5:
    match opcion:
        # Añadir alumno a un curso
        case 1:
            # pedimos los datos necesarios para agregar al alumno
            nombreApellidos = str(input("Introduce el nombre y el apellido del alumno: "))
            agregarCurso = str(input("¿A qué curso le gustaría agregarle? (DAM1 o DAM2): "))
            # Si el alumno no esta agregado, lo agregamos, sino, advertimos y no agregamos
            if nombreApellidos in clases:
                print(f"El alumno {nombreApellidos} ya ha sido agregado anteriormente.")
            else:
                clases[agregarCurso].append(nombreApellidos)
                print(f"El alumno {nombreApellidos} ha sido agregado correctamente al curso {agregarCurso}")
        # Mostrar todos los cursos y alumnos
        case 2:
            for curso in clases:
                # Recorremos para cada elemento en curso
                print(curso)
                print("Alumnos: ")
                # Buscamos alumnos en la posicion clases[curso]
                for alumnos in clases[curso]:
                    print(f"- {alumnos}")
        # Buscar alumno por nombre
        case 3:
            alumno = str(input("Introduce el nombre del alumno a buscar: "))
            # Buscamos el alumno en la variable alumnos que busca en la lista del diccionario
            for curso,alumnos in clases.items():
                if alumno in alumnos:
                    print(f"El alumno {alumno} pertenece al curso {curso}. ")
        # Ver número total de alumnos
        case 4:
            total = 0
            # Sacamos la longitud de las listas y obtenemos los alumnos por cada clase, lo sumamos y tenemos el total.
            for curso in clases:
                total = total + len(clases[curso])
            print("El total de alumnos es: ", total)
        # Si el usuario mete un número fuera de rango:
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Añadir alumno a un curso")
    print("2. Mostrar todos los cursos y alumnos")
    print("3. Buscar alumno por nombre")
    print("4. Ver número total de alumnos")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
