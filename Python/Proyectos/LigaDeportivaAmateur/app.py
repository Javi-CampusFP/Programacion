# Importar librerias
import equipos
import jugadores
import calendario
import ranking
import general
# Variables

# Inicializar variable opcion para que no de error en el while (variable opcion)
opcion = int
opcionGeneral = int
# Declarar ids de utilidad
idEquipo = 0
idJugador = 0
idPartido = 0
# Incializar variable de id general para cada equipo

# Declarar la lista de equipos
listaEquipos = []
# Declarar la X de partidos


# Lógica del código
while opcionGeneral != 5:
    # Resetear cada vez que se repite el bucle opcion = 0, sino, si nos salimos de una sección a otra
    # el programa hara directamente la opción que hayamos elegido antes en otra sección
    opcion = 0
    # Introduce lo que quiere hacer el usuario
    opcionGeneral = general.menu()
    # Comprueba matches y saca del programa si es necesario (menú general)
    match opcionGeneral:
        # Gestión de equipos
        case 1:
            # Si se añade alguna opción extra, cambiar el valor a comparar con el nuevo que corresponda
            while opcion != 6:
                # Opcion sera el número que elija el usuario
                opcion = equipos.menu()
                match opcion:
                    # Crear un equipo
                    case 1:
                        idEquipo = general.generarId(idEquipo)
                        equipos.agregarEquipo(idEquipo, listaEquipos)
                    # Listar equipos
                    case 2:
                        equipos.listarEquipos(listaEquipos)
                    # Buscar equipo por id
                    case 3:
                        equipos.buscarIdEquipo(listaEquipos)
                    # Actualizar datos de equipo
                    case 4:
                        equipos.actualizarDatos(listaEquipos)
                    # Desactivar equipo
                    case 5:
                        equipos.desactivarEquipo(listaEquipos)
                    # Indicarle al usuario que ha salido del apartado en el que se encontraba
                    case 6:
                        print("Has salido de la sección de gestión de equipos")
                    # Si se introduce un número fuera de rango imprimir en pantalla:
                    case _:
                        print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
        # Gestión de jugadores
        case 2:
            while opcion != 6:
                opcion = jugadores.menu()
                match opcion:
                    # Dar de alta a un jugador
                    case 1:
                        print()
                    # Listar jugadores
                    case 2:
                        print()
                    # Buscar jugador por id
                    case 3:
                        print()
                    # Actualizar jugador
                    case 4:
                        print()
                    # Desactivar jugador
                    case 5:
                        print()
                    # Indicarle al usuario que ha salido del apartado en el que se encontraba
                    case 6:
                        print("Has salido de la sección de gestión de jugadores")
                    # Si se introduce un número fuera de rango imprimir en pantalla:
                    case _:
                        print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
        # Calendario de partidos
        case 3:
            while opcion != 5:
                opcion = calendario.menu()
                match opcion:
                    # Crear partido
                    case 1:
                        print()
                    # Listar partido
                    case 2:
                        print()
                    # Reprogramar partido
                    case 3:
                        print()
                    # Eliminar partido
                    case 4:
                        print()
                    # Indicarle al usuario que ha salido del apartado en el que se encontraba
                    case 5:
                        print("Has salido de la sección del calendario de partidos")
                    # Si se introduce un número fuera de rango imprimir en pantalla:
                    case _:
                        print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
        # Resultados y calificaciones
        case 4:
            while opcion != 4:
                opcion = ranking.menu()
                match opcion:
                    # Registrar resultado de partido
                    case 1:
                        print()
                    # Clasificación de equipos
                    case 2:
                        print()
                    # Estadisticas por equipo
                    case 3:
                        print()
                    # Indicarle al usuario que ha salido del apartado en el que se encontraba
                    case 4:
                        print("Has salido de la sección del ranking de equipos")
                    # Si se introduce un número fuera de rango imprimir en pantalla:
                    case _:
                        print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
        # Salir del programa
        case 5:
            print("Ha salido del programa.")
        # Si se introduce un número fuera de rango imprimir en pantalla:
        case _:
            print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
