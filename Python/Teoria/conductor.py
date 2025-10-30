
# Pedir al usuario su edad
edad = int(input("Escribe tu edad: "))

# Si la edad es mayor de 80 sacaremos o mostraremos el mensaje "Ya es hora de que tus hijos te hagan de chofer"

if edad >= 80:
	print("Ya es hora de que tus hijos te hagan de chofer")

# Si la edad está entre los 18 y los 80, sacaremos el mensaje sacaremos el mensaje "Puedes tener el carnet de conducir"

elif edad >= 18:
	print("Puedes tener el carnet de conducir")

# Contemplamos un caso que este por debajo de 18.

else:
	print("No puedes tener el carnet de conducir")