# importación de librerias
import colombofilia_core
# variables globales
listaPrincipal = ["Gestión de carrera","Consultas","Salir"]
listaPrimera = ["Registrar paloma", "Registrar tiempo de llegada", "Volver"]
listaSegunda = ["Palomas registradas","Buscar por anilla","Top 3 palomas por velocidad","Velocidad media por propietario","Salir sección"]
opcionGeneral = 0
guardadoSiNo = ["Sí", "No"]
ruta = "archivo.txt"
print("¿Desea recuperar los datos de la anterior ejecución?")
for entrada in guardadoSiNo:
    print(f"- {entrada}")
opcion = str(input("Introduce una opción: ")).lower()
match opcion:
    case "sí":
        palomas,tiempos = colombofilia_core.cargarDatos(ruta)
    case "si":
        palomas,tiempos = colombofilia_core.cargarDatos(ruta)
    case "no":
        palomas = []
        tiempos = []
    case _:
        print("Asumiendo no.")
        print("Input no reconocido por el programa")
        palomas = []
        tiempos = []
guardar = False
# Lógica del código
while opcionGeneral != 3:
    opcionSubmenus = ""
    opcionGeneral = colombofilia_core.menuGeneral(listaPrincipal)
    match opcionGeneral:
        case 1:
            while opcionSubmenus != "c":
                opcionSubmenus = colombofilia_core.submenus(listaPrimera,1)
                match opcionSubmenus:
                    case "a":
                        colombofilia_core.registrarPalomas(palomas)
                    case "b":
                        anilla = str(input("Introduce la anilla de la paloma: "))
                        colombofilia_core.registrarTiempo(anilla,palomas,tiempos)
                    case "c":
                        print("Has salido de la sección de la gestión de carreras.")
            opcionGeneral = 0
        case 2:
            while opcionSubmenus != "e":
                opcionSubmenus = colombofilia_core.submenus(listaSegunda,2)
                match opcionSubmenus:
                    case "a":
                        colombofilia_core.palomasRegistradas(palomas)
                    case "b":
                        anillaPaloma = str(input("Introduce la anilla de la paloma: "))
                        colombofilia_core.consultarDatosPaloma(anillaPaloma,tiempos)
                    case "c":
                        colombofilia_core.palomasSegunRapidez(tiempos)
                    case "d":
                        propietario = str(input("Introduce el nombre del propietario: "))
                        colombofilia_core.informacionAgrupadaPropietario(tiempos,propietario)
                    case "e":
                        print("Has salido de la sección para gestionar los resultados.")
            opcionGeneral = 0
        case 3:
            print("Has salido del programa.")
if not guardar:
    siono = str(input("¿Quieres guardar los resultados?")).lower()
    match siono:
        case "sí":
            colombofilia_core.guardarDatos(palomas,tiempos,ruta)
        case "si":
            colombofilia_core.guardarDatos(palomas,tiempos,ruta)
        case "no":
            print("Saliendo del programa")
        case _:
            print("El programa no ha reconocido el valor correctamente.")
