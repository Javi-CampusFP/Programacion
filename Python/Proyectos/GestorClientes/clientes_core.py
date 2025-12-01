# Importar librerias
import numpy as np
# Funciones

def linea():
    print("---------------------------------------------------")
def longitudString(minimo,contexto):
    dato = str(input(f"Introduce un {contexto}: "))
    while len(dato) < minimo:
        print(f"Error. El campo '{contexto}' no puede tener una longitud menor a {minimo}")
        dato = str(input(f"Introduce un {contexto}: "))
    return dato
# Función que imprime un menú y pide un input al usuario
def imprimir_menu(lista):
    # El número de índice de las opciones
    indice = 1
    # Para cada entrada en la lista
    for entrada in lista:
        # Imprimir el indice y la lista
        print(f"{indice}. {entrada}")
        # Aumentar el índice en 1 para cada print
        indice = indice + 1
    # Comprobar si la entrada es correcta o no (si no se ha metido un float o un str en un campo int)
    entradaCorrecta = False
    # Se produce un bucle mientras no tenga un tipo de dato correcto
    while not entradaCorrecta:
        # Intenta pedir una opción al usuario
        try:
            opcion = int(input("Introduce una opción: "))
            # Si no da error, sale del bucle y devuelve el valor
            entradaCorrecta = True
            return opcion
        # Si da error de valor, vuelve a pedir un valor númerico al inicio del bucle 
        except ValueError:
            print("Error. Debe de introducir un número entero.")

def crear_array():
    return np.array(["","","",""]) 
# Función que da de alta a un cliente 
def alta_cliente(array_clientes):
    # Constante de las letras permitidas en un DNI
    LETRASVALIDAS = "ABCDEFGHJKLMNPQRSTVWXYZ"
    # Comprueba si la longitud es válida
    longitud_valida = False
    # Comprueba si el formato es el correcto
    formato_correcto = False
    # Comprobar si el DNI tiene más de 1 letra
    cantidad_letras_correctas = False
    # Comprobar si el DNI es uno que ya existe en el programa
    dni_no_repetido = False

    # Mientras ni el formato, ni la longitud, ni la cantidad de letras, y si el dni se repite, realizar el bucle
    while not longitud_valida or not formato_correcto or not cantidad_letras_correctas or not dni_no_repetido:
        # Pedir el DNI al cliente
        dni_introducido = str(input("Introduce el DNI del cliente: "))
        
        # Calcular la longitud del DNI
        longitud_dni = len(dni_introducido)
        # Si la longitud no es igual a 9, la longitud no es válida
        if len(longitud_dni) != 9:
            print("Error. El DNI debe de tener como máximo una longitud de 8 números y 1 letra.")
            longitud_valida = False
        else:
            # La longitud es igual a 9, entonces es válida
            longitud_valida = True
        
        # Comprobar que el DNI introducido solo tiene una letra
        letras_DNI = 0
        # Recorrer el string del DNI 
        for caracter in dni_introducido:
            # Si el caracter esta dentro de una letra válida se suma 1 a las letras
            if caracter in LETRASVALIDAS:
                letras_DNI = letras_DNI + 1
        
        # Comprobar si el DNI tiene más de una letra o no tiene ninguna
        if letras_DNI != 1:
            print("Error. El DNI debe de contener 1 letra.")
            cantidad_letras_correctas = False
        else:
            cantidad_letras_correctas = True
        
        # Comprobar por índices si el último cáracter es una letra permitida
        if dni_introducido[-1] not in LETRASVALIDAS:
            print(f"Error. El DNI '{dni_introducido}' tiene una letra no válida.")
            formato_correcto = False
        else:
            formato_correcto = True
        
        dnis_iguales = 0
        for dato in array_clientes[dato,0]:
            if array_clientes[dato,0] == dni_introducido:
                dnis_iguales = dnis_iguales + 1 
        if dnis_iguales > 0:
            print("Error. No pueden haber DNIs duplicados.")
            dni_no_repetido = False
        else:
            dni_no_repetido = True
    
    print("El DNI introducido es correcto.")
    # Despues de todas las comprobaciones, se devuelve el DNI final
    return dni_introducido

# Función que lista a todos los clientes
def listar_clientes(array_clientes):
    print()
# Función que busca a un cliente por un DNI en especifico
def buscar_cliente_dni(array_clientes):
    print()
# Modificar el número de teléfono de un cliente
def modificar_numero_dni(array_clientes):
    print()
# Eliminar cliente por DNI
def eliminar_cliente_dni(array_clientes):
    print()
# Función para guardar los clientes en un fichero
def guardar_clientes_fichero(array_clientes,ruta):
    print()
# Cargar datos de una ejecución anterior
def cargar_datos(array_clientes,ruta):
    print()

# Variables globales
