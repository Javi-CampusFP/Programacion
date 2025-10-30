nota = int(input("Escribe la nota del estudiante: "))

match nota:
    case _ if 90 <= nota <= 100:
        print("A")
    case _ if 80 <= nota <= 89:
        print("B")
    case _ if 70 <= nota <= 79:
        print("C")
    case _ if 61 <= nota <= 69:
        print("D")
    case _:
        print("F")

print("Fin del programa")
