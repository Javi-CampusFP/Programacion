# Importar las utilidades principales
import hnf_core

# Variables
# Menú principal
menu = ["Cargar partida anterior", "Empezar partida"]
# Leyenda de los valores del tablero para el jugador
leyenda = ["'-1' Agua", "'-2' Barco"]
# El tamaño de los barcos permitidos en el tablero
tamanoBarcos = [2,3,4]
# El número de los barcos que voy a agregar en el tablero
numeroBarcos = 4
# Esto indica si se han recuperado los datos o no, por defecto esta en 'No'.
datosRecuperados = False

guardar = False
# Lógica del código
opcion = int()
while opcion != 3:
    opcion = hnf_core.imprimirLista(menu)
    match opcion:
        case 1:
            try:
                with open('partida.json','r') as archivo:
                    lineas = archivo.readlines
                    for linea in lineas:
                        print()
                datosRecuperados = True
            except FileNotFoundError:
                print("Error. La partida anterior no existe o esta corrupta.")
        case 2:
            if datosRecuperados:
                print("¡Bienvenido de nuevo!")
            else:
                # Esto almacena la posición de los barcos
                barcos = []
                # El tamaño del tablero
                tamanoTablero = 20
                # Generar el tablero
                tablero = hnf_core.generarTablero(tamanoTablero)
                for barco in range(numeroBarcos):
                    tamanoFinal = hnf_core.decidirTamano()
                    orientacion = hnf_core.horizontalVertical()
                    hnf_core.generarBarco(tablero,tamanoTablero,orientacion,tamanoFinal,barcos)
                print("¡Bienvenido al juego de hundir la flota!")

                
        case 3:
            print("Has salido del programa de hundir la flota.")
        case _:
            print("Has introducido un número fuera del rango o un caracter inválido.")