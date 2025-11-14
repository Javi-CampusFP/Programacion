# Pide dos números y una operación (+, -, *, /).
# Muestra el resultado correspondiente usando if y elif.
listaOperaciones = ["Suma", "Restar", "Multiplicación", "División"]
indice = 1
for entrada in listaOperaciones:
    print(f"{indice}. {entrada}")
    indice = indice + 1
opcion = int(input("Introduce un número de índice: "))