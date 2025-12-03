# Importar librerías
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



# Calcular la letra del DNI automáticamente
def calcular_letra_DNI(dni):
    # Todas las letras posibles y su orden (T es 0 y E es 23)
    LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    # Hacer la división para saber qué letra corresponde
    return LETRAS[dni % 23]


# Función para comprobar que un valor no se repita en la lista de los clientes
def valorUnico(contexto,clientes,valorComparar):
    # Recorrer una fila en el registro
    for registro in clientes:
        # Si la posición X en la fila es igual al valor a comparar, entonces
        if registro[contexto] == valorComparar:
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
        es_unico = valorUnico("Teléfono",clientes,telefono)
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
                dni_unico = valorUnico("DNI",clientes,dni_completo)
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
    cliente = {"DNI" : dni,"Nombre" : nombre ,"Apellidos" : apellidos,"Teléfono" : telefono}
    # retornar cliente y luego hacer un append 
    return cliente

# Función que lista a todos los clientes
def listar_clientes(clientes):
    # Si no hay registros, indicarlo
    if len(clientes) == 0:
        print("La lista no contiene ningun registro.")
    else:
        # Imprimir todos los registros 
        for registro in clientes:
            print(f"DNI : {registro["DNI"]} | Nombre : {registro["Nombre"]} | Apellidos : {registro["Apellidos"]} | Teléfono : {registro["Teléfono"]}")
        

# Función que busca a un cliente por un DNI en específico
def buscar_cliente_dni(clientes):
    # Introducir el DNI
    dni = str(input("Introduce el número y la letra del DNI a buscar: "))
    # Indicar si está encontrado o no (por defecto es False)
    encontrado = False
    # Para cada fila en la lista:
    for registro in clientes:
        # Si se encuentra el DNI
        if registro["DNI"] == dni:
            # Encontrado es True, y el valor se agrega a una lista aparte
            encontrado = True
            print(f"El cliente con DNI {dni} ha sido encontrado.")
            linea()
            print(f"DNI : {registro["DNI"]} | Nombre : {registro["Nombre"]} | Apellidos : {registro["Apellidos"]} | Teléfono : {registro["Teléfono"]}")
            linea()
    # Si el DNI no se ha encontrado, se le indica al usuario
    if not encontrado:
        linea()
        print(f"El cliente con el DNI {dni} no ha sido encontrado.")
        print("Por favor, revisa que estas usando el formato correcto o que el DNI sea existente.")
        linea()
# Modificar el número de teléfono de un cliente pidiendo el DNI
def modificar_telefono_dni(clientes):
    # Pedir el DNI
    dni = str(input("Introduce el número y la letra del DNI a buscar: "))
    # Saber si se ha encontrado o no el DNI
    encontrado = False
    # Si no se ha encontrado, entonces se avisa al usuario
    for registro in clientes:
        if registro["DNI"] == dni:
            encontrado = True
            # Indica el número de teléfono actual del cliente que se guarda la lista con posición número 3
            print(f"El cliente con DNI '{dni}' tiene el número de teléfono: {registro["Teléfono"]}")
            # Llamar a la función introducirTelefono, para que el nuevo teléfono introducido
            # sea único y tenga un formato correcto
            telefonoNuevo = introducirTelefono(clientes)
            registro["Teléfono"] = telefonoNuevo
            # Este return es para que la función finalice
            return
    if not encontrado:
        linea()
        print(f"El cliente con el DNI {dni} no ha sido encontrado.")
        print("Por favor, revisa que esta usando el formato correcto o que el DNI sea existente.")
        linea()
# Eliminar cliente por DNI
def eliminar_cliente_dni(clientes):
    # Pedir el DNI
    dni = str(input("Introduce el número y la letra del DNI a buscar: "))
    # Saber si se ha encontrado o no el DNI
    encontrado = False
    # Esto es para luego saber por qué fila voy
    contador = 0
    for registro in clientes:

        if registro["DNI"] == dni:
            # Se indica que el cliente ha sido encontrado
            encontrado = True
            linea()
            print(f"El cliente con DNI '{dni}' ha sido encontrado.")
            # Se muestran los datos del cliente para asegurarse de que realmente es este cliente
            # el que se quiere eliminar
            print("--------     DATOS DEL CLIENTE   -------")
            print(f"DNI : {registro["DNI"]} | Nombre : {registro["Nombre"]} | Apellidos : {registro["Apellidos"]} | Teléfono : {registro["Teléfono"]}")
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
                    # Eliminar el registro 
                    nueva_lista = clientes
                    del nueva_lista[contador]
                    return nueva_lista
                # Si el usuario cancela la operación, se indica por pantalla
                case "N":
                    print("Operación cancelada.")
                    return clientes
                case _:
                    print("Error. Cancelando operación por defecto.")
                    print(f"El valor '{respuesta}' no ha sido reconocido por el sistema.")
                    print("Recuerda en estas operaciones de importancía máxima, respetar las mayúsculas y las minúsculas ")
                    return clientes
        contador = contador + 1
    # Si no se ha encontrado, entonces se avisa al usuario
    if not encontrado:
        linea()
        print(f"El cliente con el DNI {dni} no ha sido encontrado.")
        print("Por favor, revisa que esta usando el formato correcto o que el DNI sea existente.")
        linea()

# Función para escribir datos en X archivo
def escribir_datos(clientes,ruta):
    with open(ruta,"w") as archivo:
        for registro in clientes:
            # Escribo todos los datos de todos los clientes en un archivo de texto plano con el formato:
            # DNI;Nombre;Apellidos;Teléfono salto de línea
            archivo.write(f"{registro["DNI"]};{registro["Nombre"]};{registro["Apellidos"]};{registro["Teléfono"]}\n")

# Función para guardar los clientes en un fichero
def guardar_clientes_fichero(clientes,ruta):
    ficheroExiste = False
    try:
        with open(f"{ruta}","r"):
            ficheroExiste = True
    except FileNotFoundError:
        ficheroExiste = False
    if ficheroExiste:
        # Si el fichero existe, preguntar por confirmación
        print("Hay datos guardados de una anterior ejecución.")
        print("¿Desea sobreescribirlos?")
        print("ATENCIÓN: Una vez sobreescritos los datos, no habra manera de volver a atras.")
        respuesta = str(input("¿Sobreescribir datos? (S/N): "))
        match respuesta:
            # Si el usuario quiere seguir, se escriben los datos
            case "S":
                print("Sobreescribiendo datos...")
                # Llamo a la función que sobreescribe los datos anteriores y guarda los de ahora
                escribir_datos(clientes,ruta)
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
        escribir_datos(clientes,ruta)


# Cargar datos de una ejecución anterior
def cargar_datos(clientes, ruta):
    try:
        with open(ruta, "r") as archivo:
            print("Fichero de anterior ejecución encontrado.")
            print("Advertencia: Si restaura estos datos perderá los de la ejecución actual.")
            respuesta = str(input("¿Restaurar datos? (S/N): "))

            match respuesta:
                case "S":
                    # Almacenar las lineas del archivo en una lista
                    lineas = archivo.readlines()
                    # Si la lista tiene longitud 0 indicar que no hay registros
                    if len(lineas) == 0:
                        print("No se ha encontrado ningún registro en la anterior ejecución, cancelando carga de datos...")
                        return clientes
                    # Crear una lista de datos que luego voy a devolver
                    lista_datos = []
                    # Recorrer cada línea
                    for linea in lineas:
                        # Declarar dni,nombre,apellidos,telefono con los valores divididos 
                        dni,nombre,apellidos,telefono = linea.strip().split(";")
                        # Agregar el diccionario a la lista
                        lista_datos.append({"DNI" : dni, "Nombre" : nombre, "Apellidos" : apellidos, "Teléfono" : telefono})
                    print("Se han cargado los clientes desde el archivo correctamente.")
                    # Devolver 
                    return lista_datos
                # Si se cancela la carga de datos indicarlo y cancelar la carga de datos
                case "N":
                    print("Cancelando carga de datos...")
                    return clientes
                # Si se ha introducido un valor no reconocido por el match case
                case _:
                    print("Error. Cancelando operación por defecto.")
                    print(f"El valor '{respuesta}' no ha sido reconocido.")
                    return clientes
    # Si el archivo no se ha encontrado (no existe) se le indica al usuario
    except FileNotFoundError:
        linea()
        print("Error. El fichero para cargar los datos no existe.")
        linea()
        return clientes
