nombre = str(input("Escribir nombre del alumno (escriba 'fin' para terminar): "))
# Almacenamos el número de suspensos totales
suspensos = 0
# Almacenamos el número de aprobados totales
aprobados = 0
# Mientras nombre.lower() no es fin, realizar bucle
while nombre.lower() != "fin":
# Comprobamos si el número introducido es menor a 5, entonces sumamos uno a suspensos, sino, sumamos uno a aprobados, y lo comprobamos con los demás números también.
    numero1 = float(input("Escribe la primera nota del 1 al 10: "))
    if numero1 < 5:
        suspensos += 1
    else:
        aprobados += 1
        numero2 = float(input("Escribe la segunda nota del 1 al 10: "))
    if numero2 < 5:
            suspensos += 1
    else:
        aprobados += 1
    numero3 = float(input("Escribe la tercera nota del 1 al 10: "))
    if numero3 < 5:
        suspensos += 1
    else:
        aprobados += 1
# volvemos a pedir el input al usuario
nombre = str(input("Escribir nombre del alumno (escriba 'fin' para terminar): "))
# Imprimimos el resultado del programa por pantalla.
print("El número total de aprobados es: ", aprobados)
print("El número total de suspensos es: ", suspensos)
