# Creamos una tupla para asignar los dias de la semana (siempre son los mismos)
diasSemana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo")
temperatura = []
mayorVeinticinco = 0
suma = 0
temperaturaMayor = 0
# Realizamos un bucle para meter la temperatura de cada uno de los dias de la semana

for dia in diasSemana:

    valorTemperatura = int(input(f"Escribe la temperatura del día {dia}: "))
    if valorTemperatura > 25:
        mayorVeinticinco = mayorVeinticinco + 1

    if valorTemperatura > temperaturaMayor:
# Almacenar el valor para luego compararlo en el siguiente loop
        temperaturaMayor = valorTemperatura
# Almacenar el nombre del dia en la variable diaTemperaturaMayor
        diaTemperaturaMayor = dia

    temperatura.append(valorTemperatura)

    suma = valorTemperatura + suma
media = suma / 7

print("La media de la temperatura final es: ", media)

print("Número de días que han superado la marca de los 25oC: ", mayorVeinticinco)

print("El día con la temperatura más alta es: ", diaTemperaturaMayor)