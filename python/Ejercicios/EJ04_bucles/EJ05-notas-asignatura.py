# Menú
print("1. Añadir nota a una asignatura")
print("2. Ver notas de una asignatura")
print("3. Calcular media por asignatura")
print("4. Media general")
print("5. Salir")
# Pedirle la opción al usuario
opcion = int(input("Introduce un número de índice: "))
# Diccionario con las asignatuas y las listas que contendran las notas dentro
notas = {"Programación" : [], "Sistemas" : [], "Bases de datos" : []}
# Mientras la opción elegida no sea 5, continuar el bucle
while opcion != 5:
    match opcion:
        # Añadir nota a una asignatura
        case 1:
            # Se le pide la asignatura, si no esta dentro del diccionario se indica, y sino se agrega el valor de nota.
            nombreAsignatura = str(input("Introduce el nombre de la asignatura de la nota a añadir: "))
            notaAsignatura = 0
            if nombreAsignatura not in notas:
                print("Error. El nombre de la asignatura no es válido.")
            else:
                notaAsignatura = float(input(f"Introduce la nota de la asignatura {nombreAsignatura}: "))
                notas[nombreAsignatura].append(notaAsignatura)
        # Ver notas de una asignatura
        case 2:
            nombreAsignatura = str(input("Introduce el nombre de la asignatura para ver las notas: "))
            # Hago un for, porque pueden haber varias notas por asignatura (es una lista)
            for todasNotas in notas[nombreAsignatura]:
                print(f"- {todasNotas}")
        # Calcular media por asignatura
        case 3:
            # Esto en esencia es un for con 2 variables y un .items().
            # Calculamos el total de las notas en cada asignatura.
            # Para evitar que se calcule la media general, declaramos total y contador dentro del for
            for asignatura in notas:
                total = 0
                contador = 0
                for nota in notas[asignatura]:
                    total = total + nota
                    contador = contador + 1
                if total == 0 or contador == 0:
                    print(f"La asignatura {asignatura} no tiene notas disponibles o son 0.")
                else:
                    media = 0
                    media = total / contador
                    print(f"La media de la asignatura {asignatura} es {media}")
        # Media general
        # Declaramos total y contador fuera del for y recorremos las listas con 2 for, uno se encarga de
        # sumar el total de las notas, y el otro se encarga de calcular la media
        case 4:
            total = 0
            contador = 0
            for asignatura in notas:
                for nota in notas[asignatura]:
                    total = total + nota
                    contador = contador + 1
            if contador == 0 or total == 0:
                print("No hay notas disponibles, o la media es 0.")
            else:
                media = total / contador
                print(f"La media general es: {media}")
        # Número introducido fuera de rango
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Añadir nota a una asignatura")
    print("2. Ver notas de una asignatura")
    print("3. Calcular media por asignatura")
    print("4. Media general")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
