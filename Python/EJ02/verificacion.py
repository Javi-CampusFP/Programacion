# 1. Declarar la variable contraseña como constante
CONTRASENA = "python123"
inputcontr = str(input("Escribe la contraseña correspondiente: "))
# 2. Comprobar si la contraseña es igual al input introducido
while CONTRASENA != inputcontr:
    inputcontr = str(input("Contraseña incorrecta. Inténtelo de nuevo: "))
# 3. Imprimir el acceso concedido en pantalla
print("Acceso concedido. ")
