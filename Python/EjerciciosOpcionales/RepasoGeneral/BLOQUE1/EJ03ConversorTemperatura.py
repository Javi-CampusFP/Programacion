# Pide una temperatura en grados Celsius y muestra su equivalente en Fahrenheit.
# Fórmula:
# F = C × 1.8 + 32
temperatura = float(input("Introduce la temperatura: "))
conversion = temperatura * 1.8 + 32
print(f"La temperatura en celsius '{temperatura}' convertida a Fahrenheit es: {conversion}")