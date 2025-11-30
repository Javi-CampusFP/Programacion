# importar librerias

# funciones

# variables globales
dias = ("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")
temperaturas = []
# lógica del código
# Recorro todos los días de la semana
for dia in dias:
    # Para cada día pido la temperatura
    tempHoy = float(input(f"Introduce la temperatura del dia {dia}: "))
    # Lo añado en la lista temperaturas
    temperaturas.append({"nombreDia" : dia, "temperatura" : tempHoy})
# Abro el archivo temperaturas.txt en modo write
with open("temperaturas.txt","w") as archivo:
    # Para cada temperatura en temperaturas
    for temperatura in temperaturas:
        # Escribir la temperatura y el día con un salto de línea al final
        archivo.write(f"{temperatura["nombreDia"]} : {temperatura["temperatura"]}\n")
# Indicación de que el archivo ha sido generado correctamente
print("El archivo ha sido generado correctamente.")
