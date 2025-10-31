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
                        print()
                    # Actualizar datos de equipo
                    case 4:
                        print()
                    # Salir del programa
                    case 5:
                        print()
                    case 6:
                        print("Has salido de la sección de gestión de equipos")
                    # Si se introduce un número fuera de rango imprimir en pantalla:
                    case _:
                        print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
        # Gestión de jugadores
        case 2:
            print()
        # Calendario de partidos
        case 3:
            print()
        # Resultados y calificaciones
        case 4:
            print()
        # Salir del programa
        case 5:
            print("Ha salido del programa.")
        # Si se introduce un número fuera de rango imprimir en pantalla:
        case _:
            print("Error. El número introducido esta fuera de rango. Introduzca un número válido")
