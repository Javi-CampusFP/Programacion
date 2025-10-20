# Menú
print("1. Mostrar habitaciones")
print("2. Reservar habitación")
print("3. Ver reservas")
print("4. Calcular total a pagar")
print("5. Salir")
opcion = int(input("Introduce un número de índice: "))
# Declaramos las habitaciones disponibles
habitaciones = {1 : ("Normal", 100), 2 : ("Normal", 100), 3 : ("Suite", 200), 4 : ("Suite", 360), 5 : ("Normal", 200)}
# Almacenamos las reservas
reservadas = []
while opcion != 5:
    match opcion:
        # Mostrar habitaciones
        case 1:
            for habitacion in habitaciones:
                disponibilidad = "Disponible"
                if habitaciones in reservadas:
                    disponibilidad = "Ocupada"
                print(f"- Habitación número: {habitacion} Precio por noche: {habitaciones[habitacion][1]} Disponibilidad: {disponibilidad} Tipo: {habitaciones[habitacion][0]}")
        # Reservar habitación
        case 2:
            reserva = int(input("Introduce el número de habitación a reservar: "))
            # Si la habitacion ha sido ocupada, o si no esta dentro del rango da error.
            if reserva not in habitaciones:
                print("El número de habitación no existe. Introduzca un número válido.")
            elif reserva in reservadas:
                print("La habitación seleccionada ya esta ocupada. Elija otra habitación.")
                # Sino se actualiza la lista y se cambia a habitación ocupada
            else:
                reservadas.append(reserva)
                print("La habitación ha sido reservada con éxito.")
        # Ver reservas
        case 3:
            # Vemos las reservas de habitaciones en la lista con la variable "disponibilidad"
            for reserva in habitaciones:
                if reserva in reservadas:
                    print(f"La habitación {reserva} esta reservada.")
        # Calcular total a pagar
        case 4:
            totalPagar = 0
            # El total a pagar se calcula recorriendo toda la lista, si la habitacion esta reservada se suma
            for reserva in habitaciones:
                if reserva in reservadas:
                    totalPagar = habitaciones[reserva][1] + totalPagar
            print("El total a pagar es: ", totalPagar)
            # Número introducido fuera del rango
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Mostrar habitaciones")
    print("2. Reservar habitación")
    print("3. Ver reservas")
    print("4. Calcular total a pagar")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
