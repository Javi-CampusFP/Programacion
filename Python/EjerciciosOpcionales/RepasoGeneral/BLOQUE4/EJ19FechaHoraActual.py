# Usa la librería datetime.
import datetime
# Muestra la fecha y hora actual con formato:
    # “Hoy es 15/04/2025 y son las 10:45:30”
ahora = datetime.datetime.now()

fecha_formateada = ahora.strftime("Hoy es %d/%m/%Y y son las %H:%M:%S")

print(fecha_formateada)
