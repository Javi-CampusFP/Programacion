# importar librerias
from random import randrange
# definir funciones
def definirDificultad(listaMonstruos,monstruos):
    for monstruo in listaMonstruos:
        dificultad = randrange(1,5)
        monstruos.append({"nombre" : monstruo, "dificultad" : dificultad, "capturado" : False})
# Definir la función para elegir un monstruo de una lista
def elegirMonstruo(monstruos):
    longitud = len(monstruos) - 1
    elegido = randrange(0,longitud)
    return monstruos[elegido]
# Definir la función para imprimir los objetos disponibles
def imprimirObjetos(objetos):
    for objeto in objetos:
        print(f"- {objeto}")
# Definimos la función para calcular la captura
def calculoCaptura(objetos,monstruo):
    # Pedimos el objeto
    objeto = str(input("Introduce el objeto con el que deseas capturar al monstruo: "))
    # Mientras el objeto no sea existente en la lista, pedirselo otra vez al usuario
    while objeto not in objetos:
        objeto = str(input("Error. Introduce un objeto que este en la lista: "))
    # coger la dificultad y meterla en una variable
    dificultad = monstruo["dificultad"]
    # Si la captura fue exisota o no, depende de si captura es = a número de dificultad
    captura = randrange(0,dificultad + 1)
    # Si captura es igual a número de dificultad o mayor, entonces la captura fue exitosa.
    if captura >= dificultad:
        monstruo["capturado"] = True
        print(f"¡Has capturado a un/a {monstruo["nombre"]} con un/a {objeto}!")
    # Sino, no fue exitosa.
    else:
        print(f"Fallaste al intentar capturar un/a {monstruo["nombre"]} con un/a {objeto}.")
# definir variables
# Una lista de los monstruos disponibles a los que luego se le calculara la dificultad
listaMonstruos = ["vampiro", "momia", "bruja", "esqueleto", "fantasma"]
# Una lista de objetos disponibles para intentar atrapar al mounstruo
listaObjetos = ["estaca", "poción mágica", "hechizo"]
# La lista de monstruos finales con la dificultad calculada
monstruos = []
# Declaro elegido con clave valor, para que no de error en el bucle.
elegido = {"capturado" : False}
# lógica del código
definirDificultad(listaMonstruos,monstruos)
# Mientras elegido no sea capturado, ejecutar el bucle
while not elegido["capturado"]:
    # Llamar a la función elegir monstruo y lo guardamos en una variable
    elegido = elegirMonstruo(monstruos)
    # Imprimimos (en el primer intento) una bienvenida
    print("¡Bienvenido a la caza de monstruos de halloween!")
    print(f"¡Un monstruo ha aparecido! {elegido["nombre"]} de nivel {elegido["dificultad"]}")
    print()
    # Declaramos los intentos restantes
    intentosRestantes = 3
    # Mientras los intentos restantes no sean igual a 0
    while intentosRestantes != 0 and not elegido["capturado"]:
        # Imprimir en pantalla los intentos restantes
        print(f"Tiene '{intentosRestantes}' intento restante.")
        print("Elige un objeto para intentar capturar al monstruo: ")
        # Imprimir los objetos por pantalla
        imprimirObjetos(listaObjetos)
        # Si es capturado o no el monstruo
        calculoCaptura(listaObjetos,elegido)
        # Restar 1 a los intentos restantes
        intentosRestantes = intentosRestantes - 1
