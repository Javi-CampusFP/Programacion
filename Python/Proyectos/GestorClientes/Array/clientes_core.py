# Importar librerías

import numpy as np
from rich import print


# Funciones
# Una función que imprime una línea de texto de '-'
def linea():
    print("----------------------------------------------------")


# Una función que comprueba que la longitud mínima (por ejemplo, en un nombre) y para poderlo usar
# con más finalidades se le da un contexto, que puede ser "nombre", "apellidos"...
def longitudString(minimo,contexto):
    # Se pide un dato específico
    dato = str(input(f"Introduce un {contexto}: "))
    # Si la longitud es menor a la mínima
    while len(dato) < minimo:
        # Imprimir un error
        linea()
        print(f"Error. El campo '{contexto}' no puede tener una longitud menor a {minimo}")
        linea()
        # y volver a pedir el dato
        dato = str(input(f"Introduce un {contexto}: "))
    # Devolver el dato introducido
    return dato


# Función que imprime un menú y pide un input al usuario
def imprimir_menu(lista):
    # El número de índice de las opciones
    indice = 1
    # Para cada entrada en la lista
    linea()
    # Me ha costado bastante hacer que encaje bien este print, pero queda bonito
    print("|                  MENÚ PRINCIPAL                  |")
    linea()
    for entrada in lista:
        # Imprimir el indice y la lista
        print(f"{indice}. {entrada}")
        # Aumentar el índice en 1 para cada print
        indice = indice + 1
    linea()
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
        # Si da error de valor, vuelve a pedir un valor numérico al inicio del bucle
        except ValueError:
            linea()
            print("Error. Debe de introducir un número entero.")
            linea()


# Crear un array de 2 dimensiones con la librería numpy
def crear_array():
    # Creo un array con dtype = object, porque si no se pone nada, numpy trunca los campos
    # al número de caracteres más bajo posible (en este caso, 1)
    return np.array([["","","",""]], dtype=object)


# Calcular la letra del DNI automáticamente
def calcular_letra_DNI(dni):
    # Todas las letras posibles y su orden (T es 0 y E es 23)
    LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    # Hacer la división para saber qué letra corresponde
    return LETRAS[dni % 23]


# Función para comprobar que un valor no se repita en el array de los clientes
def valorUnico(posicion,array,valorComparar):
    # Recorrer una fila en el array
    for fila in array:
        # Si la posición X en la fila es igual al valor a comparar, entonces
        if fila[posicion] == valorComparar:
            # La función se detiene y devuelve False
            print(f"Error. El valor {valorComparar} ya existe en la lista.")
            return False
    # Si el valor es único, entonces devuelve True
    return True


# Función especializada para introducir los teléfonos
def introducirTelefono(clientes):
    # Formato correcto siempre por defecto es falso
    formatoCorrecto = False
    # Si el teléfono es único o no, por defecto es sí
    es_unico = True
    # Otra vez aquí tengo que declarar la variable teléfono de tipo string (pyright issues -> es muy pesao)
    telefono = ""
    NUMEROSDISPONIBLES = "0123456789"
    # Mientras no haya un formato correcto, repetir el bucle
    while not formatoCorrecto or not es_unico:
        # Contar las separaciones
        separaciones = 0
        numerosTotal = 0
        # Introducir un teléfono
        telefono = longitudString(11,"teléfono") # '111-222-333' <- 9+2=11
        # Contar separadores de tipo '-'
        for contar in telefono:
            if contar == "-":
                # Sumar contador si hay un separador '-'
                separaciones = separaciones + 1
            if contar in NUMEROSDISPONIBLES:
                numerosTotal = numerosTotal + 1
        if separaciones != 2 or numerosTotal != 9:
            linea()
            print("Error. El número de teléfono debe de contener 9 números y 2 separadores de tipo '-'")
            linea()
        else:
            formatoCorrecto = True
        es_unico = valorUnico(3,clientes,telefono)
    return telefono
# Función para introducir el DNI
def introducirDNI (clientes):
    # Establecer variables que van a servir para el bucle principal
    formato_correcto = False
    dni_unico = True
    # Declaro dni_completo, pyright esta siendo pesado porque la variable puede 'no existir'
    dni_completo = str()
    # Mientras se cumpla que el formato no sea correcto y el dni este repetido:
    while not formato_correcto or not dni_unico:
        # Intentar pedir el DNI, calcular la letra
        try:
            # Pedir DNI
            dni = int(input("Introduce un número de DNI: "))
            # Calcular la letra del DNI
            letra_DNI = calcular_letra_DNI(dni)
            # Pasar el DNI a string y calcular la longitud
            dniString = str(dni)
            # Poner la longitud en una variable
            longitudDNI = len(dniString)
            # Si la longitud no es la correcta, indicarlo y poner formato_correcto a false
            if longitudDNI != 8:
                linea()
                print("Error. El DNI español no tiene más de 8 números.")
                linea()
                formato_correcto = False
            # Si el formato es correcto (Solo números y 8 números de largo) entonces
            # se adjunta la letra del DNI y el formato es correcto
            else:
                dni_completo = dniString+letra_DNI
                formato_correcto = True
                # Llamo a la función valor único que devuelve un boolean si el valor introducido es único, devuelve True
                dni_unico = valorUnico(0,clientes,dni_completo)
                # Si el contador de DNIs repetidos es 0, entonces esta correcto
                if dni_unico:
                    linea()
                    print("El DNI se ha introducido correctamente")
                    linea()
                else:
                    # Sino, se le indica al usuario que no se pudo agregar y que se repite el DNI en la lista
                    linea()
                    print(f"Error. El DNI {dni_completo} esta repetido en la lista de los clientes.")
                    linea()
        # Si el usuario se hace el gracioso y mete un string, lo atrapa y vuelve a comenzar el bucle
        except ValueError:
            linea()
            print("Error. El número del DNI solo contiene números enteros.")
            linea()
    # Devolver el DNI
    return dni_completo


def alta_cliente(clientes):
    # Pido el DNI del cliente
    dni = introducirDNI(clientes)
    # Pido el nombre del cliente
    nombre = longitudString(2,"nombre")
    # Pido los apellidos del cliente
    apellidos = longitudString(8,"apellidos")
    # Pido el teléfono del cliente
    telefono = introducirTelefono(clientes)
    # Agrego el cliente final en una lista
    cliente = [dni,nombre,apellidos,telefono]
    # Convierto la lista a un array
    cliente_final = np.array([cliente])
    return cliente_final
# Agregar un registro al array
def agregar_registro(cliente,clientes):
    # Retornar un append de numpy
    # El primer valor es el array sobre el que va a trabajar
    # El segundo valor es el valor que va a operar
    # El tercer valor indica que es una fila (0) no una columna (1)
    return np.append(clientes,cliente,axis=0)

# Función que lista a todos los clientes
def listar_clientes(array_clientes):
    # Si no hay registros, indicarlo
    if array_clientes[0][0] == "":
        linea()
        print("No hay registros en la lista. Está vacía.")
        linea()
    # Si hay registros, listarlos
    else:
        linea()
        # Para cliente en el array
        for cliente in array_clientes:
            # Imprimirlos por consola
            print(f"DNI : {cliente[0]} | Nombre : {cliente[1]} | Apellidos : {cliente[2]} | Teléfono : {cliente[3]}")
            linea()
# Función que busca a un cliente por un DNI en específico
def buscar_cliente_dni(array_clientes):
    # Introducir el DNI
    dni = str(input("Introduce el número y la letra del DNI a buscar: "))
    # Indicar si está encontrado o no (por defecto es False)
    encontrado = False
    # Para cada fila en array:
    for cliente in array_clientes:
        # Si se encuentra el DNI
        if cliente[0] == dni:
            # Encontrado es True, y el valor se agrega a una lista aparte
            encontrado = True
            print(f"El cliente con DNI {dni} ha sido encontrado.")
            linea()
            print(f"DNI : {cliente[0]} | Nombre : {cliente[1]} | Apellidos : {cliente[2]} | Teléfono : {cliente[3]}")
            linea()
    # Si el DNI no se ha encontrado, se le indica al usuario
    if not encontrado:
        linea()
        print(f"El cliente con el DNI {dni} no ha sido encontrado.")
        print("Por favor, revisa que estas usando el formato correcto o que el DNI sea existente.")
        linea()
# Modificar el número de teléfono de un cliente pidiendo el DNI
def modificar_telefono_dni(array_clientes):
    # Pedir el DNI
    dni = str(input("Introduce el número y la letra del DNI a buscar: "))
    # Saber si se ha encontrado o no el DNI
    encontrado = False
    # Si no se ha encontrado, entonces se avisa al usuario
    for cliente in array_clientes:
        if cliente[0] == dni:
            encontrado = True
            # Indica el número de teléfono actual del cliente que se guarda en el array posición número 3
            print(f"El cliente con DNI '{dni}' tiene el número de teléfono: {cliente[3]}")
            # Llamar a la función introducirTelefono, para que el nuevo teléfono introducido
            # sea único y tenga un formato correcto
            telefonoNuevo = introducirTelefono(array_clientes)
            cliente[3] = telefonoNuevo
            # Este return es para que la función finalice
            return
    if not encontrado:
        linea()
        print(f"El cliente con el DNI {dni} no ha sido encontrado.")
        print("Por favor, revisa que esta usando el formato correcto o que el DNI sea existente.")
        linea()
# Eliminar cliente por DNI
def eliminar_cliente_dni(array_clientes):
    # Pedir el DNI
    dni = str(input("Introduce el número y la letra del DNI a buscar: "))
    # Saber si se ha encontrado o no el DNI
    encontrado = False
    # Esto es para luego saber por qué fila voy
    contador = 0
    for cliente in array_clientes:

        if cliente[0] == dni:
            # Se indica que el cliente ha sido encontrado
            encontrado = True
            linea()
            print(f"El cliente con DNI '{dni}' ha sido encontrado.")
            # Se muestran los datos del cliente para asegurarse de que realmente es este cliente
            # el que se quiere eliminar
            print("--------     DATOS DEL CLIENTE   -------")
            print(f"DNI : {cliente[0]} | Nombre : {cliente[1]} | Apellidos : {cliente[2]} | Teléfono : {cliente[3]}")
            # Confirmación de seguridad para saber si se elimina o no
            print("------- CONFIRMACIÓN DE SEGURIDAD -------")
            print("Atención, después del borrado sera imposible recuperar los datos de este cliente y tendra que volverlos a introducir si quiere consultarlos.")
            linea()
            respuesta = str(input("Desea continuar? (S/N): "))
            # Podría hacer un ".upper", pero no hace gracia borrar algo por error, entonces
            # este match case es key sensitive
            match respuesta:
                case "S":
                    print("Eliminando cliente...")
                    # Eliminar en el array que estamos trabajando el campo cliente
                    array_nueva = np.delete(array_clientes,contador,axis=0)
                    print("Cliente eliminado con éxito.")
                    return array_nueva
                # Si el usuario cancela la operación, se indica por pantalla
                case "N":
                    print("Operación cancelada.")
                    return array_clientes
                case _:
                    print("Error. Cancelando operación por defecto.")
                    print(f"El valor '{respuesta}' no ha sido reconocido por el sistema.")
                    print("Recuerda en estas operaciones de importancía máxima, respetar las mayúsculas y las minúsculas ")
                    return array_clientes
        contador = contador + 1
    # Si no se ha encontrado, entonces se avisa al usuario
    if not encontrado:
        linea()
        print(f"El cliente con el DNI {dni} no ha sido encontrado.")
        print("Por favor, revisa que esta usando el formato correcto o que el DNI sea existente.")
        linea()
# Función para escribir datos en X archivo
def escribir_datos(array_clientes,ruta):
    with open(ruta,"w") as archivo:
        for cliente in array_clientes:
            # Escribo todos los datos de todos los clientes en un archivo de texto plano con el formato:
            # DNI;Nombre;Apellidos;Teléfono salto de línea
            archivo.write(f"{cliente[0]};{cliente[1]};{cliente[2]};{cliente[3]};\n")
# Función para guardar los clientes en un fichero
def guardar_clientes_fichero(array_clientes,ruta):
    ficheroExiste = False
    try:
        with open(f"{ruta}","r"):
            ficheroExiste = True
    except FileNotFoundError:
        ficheroExiste = False
    if ficheroExiste:
        print("Hay datos guardados de una anterior ejecución.")
        print("¿Desea sobreescribirlos?")
        print("ATENCIÓN: Una vez sobreescritos los datos, no habra manera de volver a atras.")
        respuesta = str(input("¿Sobreescribir datos? (S/N): "))
        match respuesta:
            case "S":
                print("Sobreescribiendo datos...")
                # Llamo a la función que sobreescribe los datos anteriores y guarda los de ahora
                escribir_datos(array_clientes,ruta)
            # Si no se quieren sobreescribir los datos con los de la nueva ejecución, simplemente
            # paro la función
            case "N":
                print("Cancelando sobreescritura de datos...")
                return
            # Si el usuario ha introducido un carácter no reconocible por el sistema, se indica
            case _:
                print("Error. Cancelando operación por defecto.")
                print(f"El valor '{respuesta}' no ha sido reconocido por el sistema.")
                print("Recuerda en estas operaciones de importancía máxima, respetar las mayúsculas y las minúsculas en los diálogos.")
    else:
        # Llamo a la función que he creado para guardar los datos
        escribir_datos(array_clientes,ruta)


# Cargar datos de una ejecución anterior
def cargar_datos(array_clientes,ruta):
    # Se presupone que un archivo existe
    ficheroExiste = True
    try:
        with open(ruta,"r") as archivo:
            print("Fichero de anterior ejecución encontrado.")
            print("Advertencia: Si restaura estos datos perderá los de la ejecución actual.")
            respuesta = str(input("¿Restaurar datos? (S/N): "))
            match respuesta:
                # Si el usuario aun así quiere continuar:
                case "S":
                    lineas = archivo.readlines()
                    if not lineas:
                        print("No se ha encontrado ningun registro en la anterior ejecución, cancelando carga de datos...")
                        return array_clientes
                    # Esto es una lista temporal para cargar a los clientes
                    clientes_cargar = []
                    for lineaDatos in lineas:
                        # Me limpia la línea del \n (salto de línea)
                        datos = lineaDatos.strip().split(";")
                        # Si la longitud de los datos es mayor a 4
                        if len(datos) >= 4:
                            # Entonces agregar los últimos 4 datos a clientes_cargar
                            clientes_cargar.append(datos[:4])
                    # Cuando termine de leer el archivo:
                    array_nuevo = np.array(clientes_cargar, dtype=object)
                    print("Se han cargado los clientes desde el archivo correctamente.")
                    return array_nuevo
                # Si el usuario se niega a restaurar los datos una vez leída la advertencia
                case "N":
                    print("Cancelando carga de datos...")
                    return array_clientes
                case _:
                    print("Error. Cancelando operación por defecto.")
                    print(f"El valor '{respuesta}' no ha sido reconocido por el sistema.")
                    print("Recuerda en estas operaciones de importancía máxima, respetar las mayúsculas y las minúsculas en los diálogos.")
                    return array_clientes
    # Si da un error y el archivo no existe, se indica
    except FileNotFoundError:
        ficheroExiste = False
    # Si no existe se le indica al usuario por pantalla
    if not ficheroExiste:
        linea()
        print("Error. El fichero para cargar los datos de una anterior ejecución no existe o esta corrupto.")
        print("Recomiendo encarecidamente volver a ejecutar otra vez el programa desde 0 y usar la función para guardar los datos.")
        linea()
