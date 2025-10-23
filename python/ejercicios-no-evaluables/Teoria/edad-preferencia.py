edad = int(input("Escribe tu edad: "))
calculoEdad = ""
while edad < 0:
	print("Error. La edad no puede ser menor a 0.")
	edad = int(input("Escribe tu edad: "))
if edad <= 12:
	calculoEdad = "Niño"
elif edad in range(13,19):
	calculoEdad = "Adolescente"
elif edad in range (19, 60):
	calculoEdad = "Adulto"
else:
	calculoEdad = "Adulto Mayor"

idioma = str(input("Introduzca un idioma preferido: "))
if idioma == "en":
	idioma = "Your selected language is English"
elif idioma == "es":
	idioma = "Tu lenguaje elegido es español."
elif idioma == "fr":
	idioma = "Votre langue sélectionnée est le français"
else:
	idioma = "Your current language is not supported"
print(f"Eres un {calculoEdad}")
print(idioma)
