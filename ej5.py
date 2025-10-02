escribir = ""
lista = []

while escribir != "hecho":
    escribir = input("Escribe un número, ")
    if escribir != "hecho":
        numero = int(escribir)
        lista.append(numero)

mayor = 0
for num in lista:
    if num > mayor:
        mayor = num 
print("El número mayor es:", mayor) 
