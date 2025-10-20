# Definir variables
# declarar numeroPrimo
numeroPrimo = int()

# Definir funciones
# calcular si el numero es primo
def pedirNumero():
    numeroIntroducir = int(input("Introduce el número a comprobar: "))
    return numeroIntroducir
numero = pedirNumero()
def comprobarNumero(numero):
    es_primo = False
    if numero <= 1:
        print("El número debe de ser mayor a 1.")
    elif numero == 2:
        es_primo = True
    else:
        for numeroPrimoCalcular in range(2, int(numero ** 0.5) + 1):
            if numero % numeroPrimoCalcular == 0:
                es_primo = False
            else:
                es_primo = True
    return es_primo
primo = comprobarNumero(numero)
# Lógica del programa
print(f"El número {numero} es primo: {primo}")
