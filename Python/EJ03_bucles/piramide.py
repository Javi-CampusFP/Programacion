# Pedimos al usuario la longitud de la altura de la pirámide
longitud = int(input("Introduce la longitud de la pirámide de asteriscos: "))
# Genera números del 1 hasta la longitud indicada.
for asterisco in range(longitud):
# Imprimimos el número multiplicado por los caracteres, +1, porque sino no se incluiría la última fila (en el caso en el que metieramos 7, solo haría print hasta la 6).
    print("*" * (asterisco + 1))