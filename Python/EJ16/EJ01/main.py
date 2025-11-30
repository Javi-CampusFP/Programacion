# importar librerias

# funciones

# variables globales
nombres = []
# lógica del código
# Pedimos input al usuario
usuarioInput = str(input("Introduce un nombre (introduce 'fin' para finalizar): "))
# Realizar el while hasta que el usuario introduzca FIN
while usuarioInput.upper() != "FIN":
    # Meter el nombre del input anterior
    nombres.append(usuarioInput)
    # Pedir otra vez un input al usuario
    usuarioInput = str(input("Introduce un nombre (introduce 'FIN' para finalizar): "))
# Abrir en modo escritura el archivo nombres.txt
with open("nombres.txt","w") as archivo:
    # Para cada nombre en la lista nombres
    for nombre in nombres:
        # Escribir una linea en el archivo con el nombre
        archivo.write(f"{nombre}\n")
