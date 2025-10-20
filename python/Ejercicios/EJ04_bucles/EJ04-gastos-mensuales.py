# Menú de selección
print("1. Añadir gastos a un día")
print("2. Mostrar gastos de un día")
print("3. Ver gasto total semanal")
print("4. Día con mayor gasto")
print("5. Salir")
# Pedimos input al usuario
opcion = int(input("Introduce un número de índice: "))
# Declaramos la lista de la semana vacia
gastoSemanal = {
    "Lunes" : [],
    "Martes" : [],
    "Miércoles" : [],
    "Jueves" : [],
    "Viernes" : []}
while opcion != 5:
    match opcion:
        #Añadir gastos a un día
        case 1:
            # Pido input al usuario para que ponga el gasto semanal
            introduceNombreDia = str(input("Introduce el nombre del día para introducir un gasto: "))
            if introduceNombreDia not in gastoSemanal:
                print("El nombre introducido no es válido.")
            # Si el nombre es válido, se pide un valor tipo float y se mete dentro del diccionario[nombre].append(float)
            else:
                numeroGasto = float(input(f"Introduce el gasto del día {introduceNombreDia}: "))
                gastoSemanal[introduceNombreDia].append(numeroGasto)
        # Mostrar gastos de un día
        case 2:
            introduceNombreDia = str(input("Introduce el nombre del día a mostrar los gastos: "))
            if introduceNombreDia not in gastoSemanal:
                print("El nombre introducido no es válido")
                # Si introduceNombreDia esta dentro del diccionario ( clave válida ), se muestra el total
            else:
                for gastosTotalesDia in gastoSemanal[introduceNombreDia]:
                    print(f"- {gastosTotalesDia}")
        # Ver gasto total semanal
        case 3:
            # TotalSemanal a 0, y se calcula la suma de los items dentro del diccionario
            totalSemanal = 0
            for dia, gastos in gastoSemanal.items():
                totalSemanal = totalSemanal + sum(gastos)
            print(f"El total semanal es: {totalSemanal}")
        #Día con mayor gasto
        case 4:
            gastoMayor = 0
            diaMayor = ""
            # Se declaran dos variables, una mira en el diccionario y otra dentro de los items()
            # Se calcula el total del dia
            for dia, gastos in gastoSemanal.items():
                totalDia = sum(gastos)
                # Se compara si el total del dia es mayor al anterior, gastoMayor = totalDia
                # y diaMayor corresponde a la clave del diccionario, dia.
                if totalDia > gastoMayor:
                    gastoMayor = totalDia
                    diaMayor = dia
            print(f"El día con el mayor gasto es: {diaMayor} con {gastoMayor}")
        # Usuario introduce un número fuera de rango
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Añadir gastos a un día")
    print("2. Mostrar gastos de un día")
    print("3. Ver gasto total semanal")
    print("4. Día con mayor gasto")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
