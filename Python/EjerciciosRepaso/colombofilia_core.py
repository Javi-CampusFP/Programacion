# importar librerias
# variables globales
# funciones
# menú general
def menuGeneral(lista):
    print("=== GESTOR DE COLOMBOFILIA ===")
    indice = 1
    for entrada in lista:
        print(f"{indice}) {entrada}")
        indice = indice + 1
    error = True
    opcion = 0
    while error:
        try:
            opcion = comprobarLongitudMinima(3)
            error = False
        except ValueError:
            print("Error. El valor introducido debe de ser un número.")
            error = True
        opcion = comprobarLongitudMinima(3)
    return opcion

def comprobarLongitudMinima(longitud):
    while True:
        try:
            entero = int(input("> "))
            if 1 <= entero <= longitud:
                return entero
            else:
                print(f"Error. El número debe estar entre 1 y {longitud}.")
        except ValueError:
            print("Error. Debe ser un número entero.")

# opción 1
def submenus(lista, numero):
    if numero == 1:
        letras = ["a","b","c"]
    else:
        letras = ["a","b","c","d","e"]
    for idx, entrada in enumerate(lista):
        print(f"{letras[idx]}) {entrada}")  # idx es el índice, entrada es el valor
    introduce = comprobarLetras(letras)
    return introduce


def comprobarLetras(letras_validas):
    while True:
        entrada = input("> ").lower()  # pasar a minúsculas
        if entrada in letras_validas:
            return entrada
        else:
            print("Error. Introduce una entrada válida.")


def registrarPalomas(palomas):
    anilla = longitudCorrecta("anilla",palomas)
    paloma = longitudCorrecta("nombre de paloma",palomas)
    propietario = longitudCorrecta("propietario",palomas)
    palomas.append({"Anilla" : anilla, "Paloma" : paloma, "Propietario" : propietario})
    print("Paloma añadida correctamente.")

def longitudCorrecta(cosas,palomas):
    cosa = str(input(f"Introduce un '{cosas}' para el programa. >"))
    while len(cosa) == 0:
        print("Error el campo no puede quedar vacio.")
        cosa = str(input(f"Introduce un '{cosas}' para el programa. >"))
    if cosas == "anilla":
        while len(cosa) != 11:
            print("Error. El campo de la anilla no puede medir menos de 11 carácteres.")
            cosa = str(input(f"Introduce un '{cosas}' para el programa. >"))
            while cosa in palomas:
                print("Error. La anilla no puede tener duplicados (Entrada duplicada)")
                cosa = str(input(f"Introduce un '{cosas}' para el programa. >"))
        return cosa.upper()
    else:
        return cosa.capitalize()
def registrarTiempo(anilla,palomas,tiempos):
    encontrado = False
    for paloma in palomas:
        if paloma["Anilla"] == anilla:
            encontrado = True
            minutos = int(input("Introduce los minutos: "))
            recorrido = 2.4
            horas = minutos / 60
            velocidad = recorrido / horas
            tiempos.append({"Anilla" : paloma[anilla], "Tiempo" : minutos,"Distancia (km)" : recorrido,"Velocidad" : velocidad, "Propietario" : paloma["Propietario"]})
            print(f"Velocidad calculada: {velocidad} km/h")
    if not encontrado:
        print(f"Error. La paloma con la anilla {anilla} no ha sido encontrada.")

def guardarDatos(palomas, tiempos, ruta="archivo.txt"):
    with open(ruta, "w") as archivo:
        archivo.write("PALOMAS\n")
        for paloma in palomas:
            archivo.write(f"{paloma['Anilla']},{paloma['Paloma']},{paloma['Propietario']}\n")
        archivo.write("TIEMPOS\n")
        for tiempo in tiempos:
            archivo.write(f"{tiempo['Anilla']},{tiempo['Tiempo']},{tiempo['Distancia (km)']},{tiempo['Velocidad']},{tiempo['Propietario']}\n")

def cargarDatos(ruta="archivo.txt"):
    palomas = []
    tiempos = []
    seccion = None  # Controla en qué sección estamos

    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()  # Quita saltos de línea y espacios
            if linea == "PALOMAS":
                seccion = "PALOMAS"
                continue
            elif linea == "TIEMPOS":
                seccion = "TIEMPOS"
                continue
            elif linea == "":
                continue  # Saltar líneas vacías

            if seccion == "PALOMAS":
                anilla, nombre, propietario = linea.split(",")
                palomas.append({
                    "Anilla": anilla,
                    "Paloma": nombre,
                    "Propietario": propietario
                })
            elif seccion == "TIEMPOS":
                anilla, tiempo, distancia, velocidad, propietario = linea.split(",")
                tiempos.append({
                    "Anilla": anilla,
                    "Tiempo": tiempo,
                    "Distancia (km)": float(distancia),
                    "Velocidad": float(velocidad),
                    "Propietario": propietario
                })

    return palomas, tiempos

# opción 2
def palomasRegistradas(palomas):
    for paloma in palomas:
        print(f"- {paloma["Anilla"] | {paloma["Nombre"]} | {paloma["Propietario"]}}")


def consultarDatosPaloma(anillaPaloma,registro):
    if len(anillaPaloma) != 0:
        encontrado = False
        for paloma in registro:
            if paloma["Anilla"] == anillaPaloma:
                encontrado = True
                print(f"Tiempo: {paloma["Tiempo"]} -- Velocidad: {paloma["Velocidad"]}")
        if not encontrado:
            print(f"La paloma con anilla {anillaPaloma} no ha sido encontrada.")
    else:
        print("Saltando paso.")
def palomasSegunRapidez(palomas):
    if len(palomas) != 3:
        print("Error. El top tiene que ejecutarse con un mínimo de 3 palomas")
    else:
        palomasDisponibles = palomas
        palomastop = []
        while len(palomasDisponibles) != 0:
            anilla = ""
            velocidadMayor = 0
            posicionLista = 0
            for paloma in palomasDisponibles:
                if paloma["Velocidad"] > velocidadMayor:
                    velocidadMayor = paloma["Velocidad"]
                    anilla = paloma["Anilla"]
                posicionLista = posicionLista + 1
            palomastop.append({"Anilla" : anilla, "Velocidad" : velocidadMayor})
            del palomasDisponibles[posicionLista]
        indice = 0
        for pal in palomastop:
            indice = indice + 1
            print(f"{indice}) {pal["Anilla"]} -- {pal["Velocidad"]} ")



def informacionAgrupadaPropietario(palomas,propietario):
    encontrado = False
    media = 0
    valores = 0
    for paloma in palomas:
        if paloma["Propietario"] == propietario:
            encontrado = True
            media = media + 1
            valores = valores + paloma["Velocidad"]
    if not encontrado:
        print("El propietario no se ha encontrado.")
    else:
        mediaFinal = valores / media
        print(f"{propietario} - {mediaFinal} km/h")
