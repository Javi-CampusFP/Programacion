frase = str(input("Introduce una frase para contar las vocales: "))
vocales = "aeiou, AEIOU"
nVocales = 0
for chr in frase:
	if chr in vocales:
		nVocales = nVocales + 1

print("La palabra", frase, "tiene ", nVocales, " vocales")