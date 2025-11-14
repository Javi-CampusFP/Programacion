# Crea una función operar(a, b, op) que reciba dos números y el tipo de operación (+, -, *, /).
# Devuelve el resultado y pruébala pidiendo datos al usuario.
lista = ["Suma", "Resta", "Multiplicación", "Dividir"]
def calculo(valor1,valor2,operacion):
    match operacion:
        case 1:
            return valor1 + valor2
        case 2:
            return valor1 - valor2
        case 3:
            return valor1 * valor2
        case 4:
            while valor2 == 0:
                print("Error. La calculadora no puede dividir por 0.")
                valor2 = float(input("Introduce un número que no sea 0: "))
            return valor1 / valor2 
        case _:
            print("Error. Has elegido una operación fuera de rango.")
indice = 0
for opciones in lista:
    indice = indice + 1
    print(f"{indice}. {opciones}")
opcion = int(input("Introduce una opción: "))
numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce un número: "))
print(calculo(numero1,numero2,opcion))
