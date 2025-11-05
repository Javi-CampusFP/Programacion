# Declarar funciones
import datetime
from tabulate import tabulate
from utiles import leer_int_mayor
def menu():
    lista = ["Crear partido","Listar partidos","Reprogramar partido","Eliminar partido","Salir"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción del menú: "))
    return opcion
def crearPartido(id, partidos, equipos):
    # variables que después se van a necesitar
    localActivo = False
    localEncontrado = False
    visitanteActivo = False
    visitanteEncontrado = False
    idEquipoLocal = leer_int_mayor("id del equipo local", 0)
    idEquipoVisitante = leer_int_mayor("id del equipo visitante", 0)
    # comprobamos que el id local no sea el mismo que el id equipo
    while (idEquipoLocal == idEquipoVisitante):
        print("Error. El id del equipo local no puede ser igual al id del equipo visitante o viceversa")
        idEquipoLocal = leer_int_mayor("id del equipo local", 0)
        idEquipoVisitante = leer_int_mayor("id del equipo visitante", 0)
    # Recorrer la lista de equipos para comparar los ids, se actualizan los valores declarados
    # más arriba a lo que corresponda
    for equipo in equipos:
        if equipo["id"] == idEquipoLocal:
            localEncontrado = True
            if equipo["activo"]:
                localActivo = True
        if equipo["id"] == idEquipoVisitante:
            visitanteEncontrado = True
            if equipo["activo"]:
                visitanteActivo = True
    # Si alguno de los equipos no es activo o no ha sido encontrado, entonces
    # no se sigue con el programa y se le indica al usuario
    if not (localActivo or localEncontrado or visitanteActivo or visitanteEncontrado):
        print("Ha habido un error. El equipo local o visitante no ha sido encontrado o no estan activados")
    # Si han sido encontrados y están activos, entonces se ejecuta el siguiente trozo
    # de código
    else:
        print("Se han seleccionado el equipo local y visitante correctamente")
        # Cogemos el día actual
        dia = datetime.datetime.today()
        # Pedimos la fecha (día)
        fecha = str(input("Introduce la fecha en la que se realizara el partido (DD/MM/YYYY): "))
        # Convertimos de tipo string a formato tipo fecha
        fecha = datetime.datetime.strptime(fecha, "%d%m%Y")
        # Pedimos la hora y lo convertimos a formato tipo fecha
        hora = str(input("Introduce la hora en la que se realizara el partido (HH:MM): "))
        hora = datetime.datetime.strptime(hora, "%H:%M")
        # Comprobación de que la fecha no está en el pasado
        while fecha < dia:
            print("Error. La fecha no puede estar en pasado. ")
            fecha = str(input("Introduce la fecha en la que se realizara el partido (DD/MM/YYYY HH:MM): "))
            fecha = datetime.datetime.strptime(fecha, "%d%m%Y %H:%M")
            # Aquí vuelvo a asignar la fecha de ahora porque si se entra en el bucle y se espera un día
            # se podria poner una fecha en el pasado.
            dia = datetime.datetime.today()
        # Número de jornada actual luego sera usado en un bucle for
        jornadaActual = 0
        # Pedir el número de jornada que quiere el usuario
        jornada = int(input("Introduce la jornada del partido: "))
        # Sacar el número de jornada más alto recorriendo la lista del jugador
        for partido in partidos:
            # Si el número de jornada es más alto, actualizar número de jornadaActual al número mayor
            if partido["jornada"] > jornadaActual:
                jornadaActual = partido["jornada"]
        # Si el número de jornada es menor al número de jornadas jugadas, indicar (puede ser igual)
        while jornada < jornadaActual:
            jornada = int(input(f"Error. El número de la jornada no puede ser menor al de una jornada anterior (última jornada: {jornadaActual}): '"))
        # Añadir el partido
        partidos.append({"id" : id, "jornada" : jornada, "local_id" : idEquipoLocal, "visitante_id" : idEquipoVisitante, "fecha" : fecha, "hora" : hora, "jugado" : False, "resultado" : None})
# Listar partidos
def listarPartido(partidos, equipos):
    print("Listar los partidos por: ")
    # un pequeño menú
    lista = ["Todos", "Jornada"]
    indice = 1
    for entrada in lista:
        print(f"{indice}. {entrada}")
        indice = indice + 1
    opcion = int(input("Introduce una opción: "))
    lista = []
    # Un match case que contempla todas las opciones
    match opcion:
        # Todos
        case 1:
            # Recorrer la lista equipos
            for equipo in equipos:
                # Recorrer la lista partidos
                for partido in partidos:
                    # Si el id del equipo local coincide con equipo id
                    if partido["local_id"] == equipo["id"]:
                        # Para visitante en equipo
                        for visitante in equipos:
                            # Si visitante id coincide con el partido id
                            if visitante["id"] == partido["visitante_id"]:
                                # Asignar nombre a variable
                                nombreVisitante = visitante["nombre"]
                                # Agregar el resultado en la lista
                                lista.append(
                                    {
                                        "id" : partido["id"],
                                        "jornada" : partido["jornada"],
                                        "local" : equipo["nombre"],
                                        "visitante" : nombreVisitante,
                                        "fecha" : partido["fecha"],
                                        "hora" : partido["hora"],
                                        "jugado" : False,
                                        "resultado" : partido["resultado"]
                                    }
                                 )
            # Imprimir la tabla
            print(tabulate(lista, headers="keys", tablefmt="grid"))
        # Por jornada
        case 2:
            jornada = int(input("Introduce el número de jornada: "))
            # Recorremos equipos y partidos
            for equipo in equipos:
                for partido in partidos:
                    # comprobamos que el partido pertenezca a la jornada solicitada
                    if partido["jornada"] == jornada and partido["local_id"] == equipo["id"]:
                        # buscar al visitante dentro de equipos
                        nombreVisitante = str
                        for visitante in equipos:
                            if visitante["id"] == partido["visitante_id"]:
                                nombreVisitante = visitante["nombre"]
                        # añadir a la lista
                        lista.append(
                            {
                                "id": partido["id"],
                                "jornada": partido["jornada"],
                                "local": equipo["nombre"],
                                "visitante": nombreVisitante,
                                "fecha": partido["fecha"],
                                "hora": partido["hora"],
                                "jugado": partido["jugado"],
                                "resultado": partido["resultado"]
                            }
                        )
            # Imprimir la tabla
            print(tabulate(lista, headers="keys", tablefmt="grid"))
        case _:
            print("Error. El número introducido está fuera de rango. Introduzca un número válido")
def reprogramarPartido(partidos):
    # Id del partido a reprogramar
    idReprogramar = int(input("Introduce el id del partido a reprogramar: "))
    # Valores que luego se van a usar
    encontrado = False
    partidoJugado = True
    # Recorrer la lista partido hasta que el id coincida
    for partido in partidos:
        if partido["id"] == idReprogramar:
            encontrado = True
            # Si no esta jugado, continuar
            if not partido["jugado"] :
                partidoJugado = False
                # Preguntar al usuario lo qué quiere reprogramar
                print("¿Qué desea reprogramar?")
                # Un pequeño menú con las opciones
                lista = ["Fecha", "Hora"]
                indice = 1
                for entrada in lista:
                    print(f"{indice}. {entrada}")
                    # Introduce una opción
                opcion = int(input("Introduce una opción: "))
                match opcion:
                    case 1:
                        # Cogemos el día actual
                        dia = datetime.datetime.today()
                        # Pedimos la fecha (día)
                        fecha = str(input("Introduce la fecha en la que se realizara el partido (DD/MM/YYYY): "))
                        # Convertimos de tipo string a formato tipo fecha
                        fecha = datetime.datetime.strptime(fecha, "%d%m%Y")
                        while fecha < dia:
                            print("Error. La fecha no puede estar en pasado. ")
                            fecha = str(input("Introduce la fecha en la que se realizara el partido (DD/MM/YYYY HH:MM): "))
                            fecha = datetime.datetime.strptime(fecha, "%d%m%Y %H:%M")
                            # Aquí vuelvo a asignar la fecha de ahora porque si se entra en el bucle y se espera un día
                            # se podría poner una fecha en el pasado.
                            dia = datetime.datetime.today()
                        partido["fecha"] = fecha
                    case 2:
                        # Aquí se hace practicamente lo mismo que en el día
                        hora = str(input("Introduce la hora en la que se realizara el partido (HH:MM): "))
                        hora = datetime.datetime.strptime(hora, "%H:%M")
                        partido["hora"] = hora
                    case _:
                        print("Error. El número introducido está fuera de rango. Introduzca un número válido")
    if not encontrado or partidoJugado:
        print(f"El partido con id {idReprogramar} no ha sido encontrado o ya ha sido jugado.")

def eliminarPartido(partidos):
    idEliminar = int(input("Introduce el id del partido a eliminar: "))
    for partido in partidos:
        if idEliminar == partido["id"] and partido["jugado"] == False:
            partidos.remove(partido)
            print("El partido ha sido eliminado correctamente")
