# Pide tres números y muestra cuál es el mayor.
# Usa condicionales anidados (if, elif, else).
print("Este programa pide 3 números y calcula el mayor.")
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce un número: "))
numero3 = int(input("Introduce un número: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"El número '{numero1}' es el mayor.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número '{numero2}' es el mayor.")
else:
    print(f"El número {numero3} es el mayor.")