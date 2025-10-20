# Definir variables
numeroIntroduce = int(input("Introduce un número límite: "))
# Definir funciones
def suma(numero):
    # Declaramos las variables dentro de la función
    suma = 0
    resultado = 0
    # Mientras suma sea menor o igual a numero:
    while suma <= numero:
        # Sumar a la variable resultado la variable suma
        resultado = resultado + suma
        # Sumarle 1 a suma para que no sea bucle infinito
        suma = suma + 1
    return resultado
# Lógica del programa
print(f"La suma hasta el límite establecido es: {suma(numeroIntroduce)}")
