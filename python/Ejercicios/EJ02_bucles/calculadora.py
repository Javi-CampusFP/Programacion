# Imprimimos el menú
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
# Pedimos una operación al usuario
operacion = int(input("Introduce el índice de la operación a realizar: "))
# Comprobar si no es 5, si es, no realizar el bucle
while operacion != 5:

# Pedir al usuario los 2 numeros
    if operacion > 0 and operacion < 5:
        numeroUno = int(input("Introduce el primer numero para la operación: "))
        numeroDos = int(input("Introduce el segundo numero para la operación: "))
# Hacer un switch con la variable operacion
    match operacion:
            case 1:
                resultado = numeroUno + numeroDos
            case 2:
                resultado = numeroUno - numeroDos
            case 3:
                resultado = numeroUno * numeroDos
            case 4:
                while numeroDos == 0:
                    numeroDos = int(input("Error. El segundo numero introducido, no puede ser 0. Introduce un numero mayor a 0: "))
                    resultado = numeroUno / numeroDos
            case _:
                operacion = int(input("Error. Introduce un numero de operación válido(1-5): "))
    print("El resultado final de la operación es: ", resultado)
    operacion = int(input("Introduce el indice de la operación a realizar: "))
else:
    print("Has salido del programa calculadora.")
