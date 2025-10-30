menu = 0
dinero = 100
print("1. Consultar saldo")
print("2. Ingresar dinero")
print("3. Retirar dinero")


print("4. Salir")
elegido = int(input("Escribe el numero de indice de la opción: "))
while elegido != 4:
    match elegido:
        case 1:
            print("El saldo actual es: ",dinero)
        case 2:
            introduce = int(input("Introduce la cantidad a ingresar:"))
            dinero = dinero + introduce
            print("El dinero se ha ingresado correctamente")
        case 3:
            introduce = int(input("Introduce la cantidad a retirar:"))
            if introduce > dinero:
                print(f"El dinero a retirar {introduce} , y el saldo de la cuenta es: {dinero}")

                print("Operación fallida. Redirigiendo al menú de inicio.")
            else:
                dinero = dinero - introduce
                print("El dinero se ha retirado correctamente")

        case _:
            print("Opcion incorrecta intentalo de nuevo. ")
            elegido = int(input("Escribe el numero de indice de la opción: "))
else:
    print("Has salido de las operaciones de la cuenta.")