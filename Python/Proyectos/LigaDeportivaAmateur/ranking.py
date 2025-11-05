from utiles import leer_int_menor
# Declarar funciones
def menu():
    lista = ["Registrar resultado","Clasificación","Estádisticas por equipo","Salir"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion
# Registrar resultados por partido
def registrarResultado(partidos):
    idPartido = int(input("Introduce el id del partido a registrar: "))
    for partido in partidos:
        # Revisar si el id coincide y si el partido no se jugó
        if partido["id"] == idPartido and not partido["jugado"]:
            # Se piden los valores
            print("Goles del equipo local: ")
            golLocal = leer_int_menor(0)
            print("Goles del equipo visitante: ")
            golVisitante = leer_int_menor(0)
            # Se asignan los valores a la posición que corresponde
            partido["resultado"] = (golLocal, golVisitante)
            partido["jugado"] = True
            print("Registro completado.")
def clasificacionEquipo(partidos, equipos):
    tabla = []
    for equipo in equipos:
        for partido in partidos:
            # No se que estoy haciendo
            if partido["jugado"] == True:
                partidosJugados = 0
                partidosJugados = partidosJugados + 1
                partidosGanados = 0
                partidosEmpatados = 0
                partidosPerdidos = 0
                goles = 0
                golesContra = 0
                diferenciaGoles = 0
                puntos = 0
                if equipo["id"] == partido["local_id"]:
                    goles = partido["resultado"][0]
                    golesContra = partido["resultado"][1]
                    diferenciaGoles = goles - golesContra
                    if partido["resultado"][0] > partido["resultado"][1]:
                        partidosGanados = partidosGanados + 1
                    elif partido["resultado"][0] == partido["resultado"][1]:
                        partidosEmpatados = partidosEmpatados + 1
                    else:
                        partidosPerdidos = partidosPerdidos + 1
                elif equipo["id"] == partido["visitante_id"]:
                    goles = partido["resultado"][1]
                    golesContra = partido["resultado"][0]
                    diferenciaGoles = goles - golesContra
                    if partido["resultado"][1] > partido["resultado"][0]:
                        partidosGanados = partidosGanados + 1
                    elif partido["resultado"][1] == partido["resultado"][0]:
                        partidosEmpatados = partidosEmpatados + 1
                    else:
                        partidosPerdidos + 1
    print()
def estadisticasEquipo(partidos, equipo):
    print()
