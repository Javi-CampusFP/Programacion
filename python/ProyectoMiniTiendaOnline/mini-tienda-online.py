# Variables globales

# ---------------------------- EJERCICIO MINI TIENDA ONLINE - PARTE 1 ----------------------------

# Modelo de datos seleccionado: A
# Diccionario de artículos metido dentro de una lista
articulos = [{"id" : 1, "nombre" : "Ratón", "precio" : 12.5, "stock": 20, "activo": True}]

# Definir la variable opción.
opcion = int

# Variable para una opción general
opcionGeneral = int

# Declaramos id del artículo 1, porque ya hay uno con id 1
idArticulo = 1

# Mensaje de error en int y en float
mensajeError = "Error. El número introducido no es válido."

# Precio mínimo
minimoPrecioStock = 0


# ---------------------------- EJERCICIO MINI TIENDA ONLINE - PARTE 2 ----------------------------

# Lista de usuarios
listaUsuarios = [{"id" : 1, "nombre" : "Ana", "email" : "ana@example.com", "activo" : True}]
# Establezco id a numero 1 porque ya hay un usuario metido
idUsuario = 1

# ---------------------------- EJERCICIO MINI TIENDA ONLINE - PARTE 3 ----------------------------





# ---------------------------- Funciones | PARTE 1 ----------------------------
# Función de mostrar el menú
def menu_articulos():
    # Declaramos las opciones del menú
    menu = ["1. Crear artículo", "2. Listar artículos", "3. Buscar artículo", "4. Actualizar artículo", "5. Eliminar un artículo", "6. Alternar activo/inactivo", "7. Salir"]
    # Imprimimos todas las entradas del menú en pantalla
    for entrada in menu:
        print(entrada)

# Función para generar un id automáticamente
def generar_id(id):
    # Generar la id de un artículo nuevo
    id = id + 1
    # Devuelve el valor
    return id
# Leer float declarado en la función
def leer_float(mensaje, minimo=None):
    precio = float(input("Introduce un precio mayor a 0 (> 0): "))
    while precio <= minimo:
        print(mensaje)
        precio = float(input("Introduce un precio mayor a 0 (> 0): "))
    return precio
# Leer entero declarado en la función
def leer_int(mensaje, minimo=None):
    # Meter el stock en una variable
    stock = int(input("Introduce un stock mayor o igual a 0 (=> 0): "))
    # Si el stock es menor al minimo declarado, se muestra mensaje de error y se pide otra vez el stock
    while stock < minimo:
        print(mensaje)
        stock = int(input("Introduce un stock mayor o igual a 0 (=> 0): "))
    return stock


# Función para listar los artículos disponibles
def listar_articulos(listaArticulos, solo_activos=None):
    if solo_activos.lower() == "activos":
        solo_activos = True
    elif solo_activos.lower() == "inactivos":
        solo_activos = False
    else:
        print(f"Error. El valor {buscar} no ha sido reconocido por el sistema.")
        solo_activos = True
        print("Valor para buscar por defecto: Activos")
    # Listar los articulos recorriendo la lista
    for articulo in listaArticulos:
        # recorrer el diccionario clave valor e imprimirlo por pantalla
        if articulo["activo"] == solo_activos:
            for campoDato, dato in articulo.items():
                print(f"{campoDato}: {dato}")
        # Este print es para que quede más separado y sea más leible
        print()
# Función para listar artículos disponibles por la id introducida
def buscar_articulo_por_id(listaArticulos, id_busqueda):
    articuloEncontrado = False
    # Buscamos en cada entrada de la lista un campo "id" que coincida con el introducido
    for articulo in listaArticulos:
        if articulo["id"] == id_busqueda:
            # Si se encuentra se pone articuloEncontrado en true, y se imprime
            articuloEncontrado = True
            for campoDato, dato in articulo.items():
                print(f"{campoDato} : {dato}")
    # Si no se encontró el artículo se le indica al usuario
    if articuloEncontrado == False:
        print(f"El artículo con la id {id_busqueda} no ha sido encontrado.")

# Función para actualizar X artículo
def actualizar_articulo(listaArticulos):
    # Parámetros que podemos actualizar
    camposArticulo = ["1. Nombre", "2. Precio", "3. Stock"]
    actualizarCampos = ["nombre", "precio", "stock"]

    # Id del artículo a actualizar
    id_buscar = int(input("Introduce el id del artículo a cambiar: "))
    articuloEncontrado = False

    for articulo in listaArticulos:
        if articulo["id"] == id_buscar:
            articuloEncontrado = True
            # Imprimir los parámetros actualizables
            for opcion in camposArticulo:        # <-- variable distinta para evitar shadowing
                print(f"- {opcion}")
            # Elegir la opción a actualizar
            actualizar = int(input("¿Qué desea actualizar? (introduzca un número): "))
            actualizar = actualizar - 1
            # Actualizar según lo elegido por el usuario
            match actualizar:
                case 0:
                    # Pedir el nuevo nombre
                    nuevoValor = input("Introduce el nombre nuevo: ")
                    # Actualizar el diccionario
                    articulo[actualizarCampos[actualizar]] = nuevoValor
                    print(f"El valor '{actualizar + 1}' del artículo '{id_buscar}' ha sido actualizado con el valor '{nuevoValor}' correctamente.")
                case 1:
                    nuevoValor = leer_float(mensajeError, minimoPrecioStock)
                    articulo[actualizarCampos[actualizar]] = nuevoValor
                    print(f"El valor '{actualizar + 1}' del artículo '{id_buscar}' ha sido actualizado con el valor '{nuevoValor}' correctamente.")
                case 2:
                    nuevoValor = leer_int(mensajeError, minimoPrecioStock)
                    # Si el nuevo stock es 0, cambiar de "activo" = True a False
                    if nuevoValor == 0:
                        articulo["activo"] = False
                    articulo[actualizarCampos[actualizar]] = nuevoValor
                    print(f"El valor '{actualizar + 1}' del artículo '{id_buscar}' ha sido actualizado con el valor '{nuevoValor}' correctamente.")
                case _:
                    print("El valor introducido no fue reconocido por el sistema. Inténtalo de nuevo.")
            break  # ya actualizamos, no hace falta seguir buscando
    if articuloEncontrado == False:
        print(f"El artículo con id {id_buscar} no ha sido encontrado.")

# Eliminar artículo
def eliminar_articulo(listaArticulos):
    # Introduce el id
    idArticulo = int(input("Introduzca el id del artículo a eliminar: "))
    articuloEncontrado = False
    # Para articulo en listaArticulos, comprobar si el campo "id" coincide con idArticulo
    for articulo in listaArticulos:
        if articulo["id"] == idArticulo:
            # Si coincide se elimina
            articuloEncontrado = True
            listaArticulos.remove(articulo)
            print(f"El artículo con id '{idArticulo}' ha sido eliminado correctamente.")
    if articuloEncontrado == False:
        print(f"El artículo con id {idArticulo} ha sido actualizado a {articulo["activo"]}")

# Función para alternar entre activo y desactivado X artículo
def alternar_activo(listaArticulos):
    # Declaramos la variable que necesita un input del usuario con el id
    idArticulo = int(input("Introduzca el id del artículo a activar / desactivar: "))
    articuloEncontrado = False
    # Recorremos la lista listaArticulos
    for articulo in listaArticulos:
        # Si un campo contiene el id se actualiza articuloEncontrado a true
        if articulo["id"] == idArticulo:
            articuloEncontrado = True
            # Si el campo "activo" era False, ahora se activa a true y viceversa
            if articulo["activo"] == False:
                articulo.update({"activo" : True})
            else:
                articulo.update({"activo" : False})
            # Indica el estado actual con un print
            print(f"El artículo con id {idArticulo} ha sido actualizado a {articulo["activo"]}")
    # Si no se encontró el producto se indica
    if articuloEncontrado == False:
        print(f"El artículo con id '{idArticulo}' no ha sido encontrado.")





# ----------------------------Funciones | PARTE 2----------------------------
def menu_general():
    menu = ["1. Gestionar productos", "2. Gestionar usuarios", "3. Carrito y ventas", "4. Salir del programa"]
    for entrada in menu:
        print(entrada)
# Menú de usuarios
def menu_usuarios():
    menu = ["1. Crear usuario","2. Listar usuarios","3. Buscar usuario por id","4. Actualizar usuario","5. Eliminar usuario","6. Alternar activo/inactivo","7. Volver"]
    for entrada in menu:
        print(entrada)
# Crear usuarios
def crear_usuario(usuarios):
    # Pide los datos necesarios
    nombre = str(input("Introduce un nombre: "))
    email = str(input("Introduce un email: "))
    # Comprueba si el email cumple con los requisitos o no
    while ("@" not in email) or ("." not in email):
        # Sino se le pide otra vez al usuario
        email = str(input("Error. El email no contiene '@' o '.' . Intentalo de nuevo: "))
    # pedirle al usuario un input de texto de sí o no
    activo = str(input("Introduce si se activa el usuario o no (sí o no): "))
    if activo.lower() == "si" or activo == "sí":
        activo = True
    elif activo.lower() == "no":
        activo = False
    else:
        print(f"El valor '{activo} no ha sido reconocido por el sistema. (Usando no por defecto)'")
        activo = False
    # Agregar el usuario e indicarlo
    usuarios.append({"id" : idUsuario, "nombre" : nombre, "email" : email, "activo" : activo})
    print(f"El usuario con id '{idUsuario}, nombre '{nombre}', email '{email}', con estado '{activo}' ha sido agregado correctamente.")

# Listar los usuarios de la lista 'listaUsuarios'
def listar_usuarios(usuarios, solo_activos=None):
    # Comprobar si el usuario quiere buscar usuarios activos o inactivos
    if solo_activos.lower() == "activos":
        solo_activos = True
    elif solo_activos.lower() == "inactivos":
        solo_activos = False
    else:
        print(f"Error. El valor {buscar} no ha sido reconocido por el sistema.")
        solo_activos = True
        print("Valor para buscar por defecto: Activos")
    # Recorrer cada elemento de la lista
    for usuario in usuarios:
        # Si el elemento cumple con el criterio, recorrer lo demás.
        if usuario["activo"] == solo_activos:
            for campoDato, dato in usuario.items():
                print(f"{campoDato} : {dato}")
            # Este print es para tener separacion entre usuarios (por si hay muchos)
            print()
# Buscar al usuario por id
def buscar_usuario_por_id(usuarios, idBusqueda):
    # Definimos si se encontro o no al usuario, sino, se le indica al final con un mensaje
    encontrado = False
    # Para cada usuario que cumpla el requisito, imprimirlo en pantalla
    for usuario in usuarios:
        if usuario["id"] == idBusqueda:
            encontrado = True
            for campoDato, dato in usuario.items():
                print(f"{campoDato} : {dato}")
    if encontrado == False:
        print(f"El usuario con '{idBusqueda}' no existe.")
# Actualizar X campo de información del usuario
def actualizar_usuario(usuarios):
    encontrado = False
    # Lista para indicarle al usuario que se puede actualizar y que no
    usuarioActualizarLista = ["1. Nombre", "2. Correo electrónico"]
    # Esta lista va a servir después para automatizar un poco
    actualizarCampos = ["nombre", "email"]
    # Pedir el id del usuario
    idBusqueda = int(input("Introduce el id del usuario a actualizar: "))
    # Si el elemento usuario coincide con los requisitos 'idBusqueda'
    # Se muestra el menú
    for usuario in usuarios:
        if usuario["id"] == idBusqueda:
            encontrado = True
            for opciones in usuarioActualizarLista:
                print(opciones)
            actualizar = int(input("¿Qué desea actualizar? (introduzca un número): "))
            # Restamos 1 para hacerlo coincidir con el índice de la lista
            actualizar = actualizar - 1
            # Match case (antes era un if statement)
            match actualizar:
                # Nombre
                case 0:
                    nuevoValor = str(input("Introduce el nuevo nombre: "))
                    usuario.update({actualizarCampos[actualizar] : nuevoValor})
                    print(f"El usuario con id '{idBusqueda}' se ha actualizado el valor correctamente a '{nuevoValor}'")
                # Correo electrónico
                case 1:
                    nuevoValor = str(input("Introduce el nuevo correo electrónico: "))
                    # Comprobar si el nuevo correo cumple los requisitos
                    while ("@" not in nuevoValor) or ("." not in nuevoValor):
                        nuevoValor = str(input("Error. El email no contiene '@' o '.' . Intentalo de nuevo: "))
                    usuario.update({actualizarCampos[actualizar] : nuevoValor})
                    print(f"El usuario con id '{idBusqueda}' se ha actualizado el valor correctamente a '{nuevoValor}'")
                # Opción fuera de rango
                case _:
                    print("El número introducido no esta dentro del rango (1 o 2)")
    # Si no se encontró se le indica al usuario
    if encontrado == False:
        print(f"El usuario con id '{idBusqueda}' no ha sido encontrado.")
# Eliminar X usuario
def eliminar_usuario(usuarios):
    encontrado = False
    idBuscar = int(input("Introduce el id del usuario a eliminar: "))
    for usuario in usuarios:
        if usuario["id"] == idBuscar:
            encontrado = True
            # Si el usuario se encuentra se quita de la lista
            usuarios.remove(usuario)
            # Se le da feedback al usuario
            print(f"El usuario con id '{idBuscar}' ha sido eliminado satisfactoriamente.")
    if encontrado == False:
        print(f"El usuario con la id '{idBuscar} no existe.'")
# Alternar usuario activo o inactivo
def alternar_activo_usuario(usuarios):
    encontrado = False
    idBuscar = int(input("Introduce el id del usuario a activar/desactivar: "))
    for usuario in usuarios:
        if usuario["id"] == idBuscar:
            encontrado = True
            # Si el usuario cumple con los requisitos de id, si estaba en activo se pone en inactivo y viceversa
            if usuario["activo"] == False:
                usuario["activo"] = True
                print(f"El usuario con id '{usuario["id"]}' ha sido activado")
            else:
                usuario["activo"] = False
                print(f"El usuario con id '{usuario["id"]}' ha sido desactivado")
    if encontrado == False:
        print(f"El usuario con el id '{idBuscar}' no existe")
# ---------------------------- Funciones PARTE 3 ----------------------------

# ---------------------------- Lógica del código ----------------------------
# MENÚ GENERAL
while opcionGeneral != 4:
    # Llama a la función para imprimir el menú
    menu_general()
    # Pide una opción al usuario
    opcionGeneral = int(input("Introduce una opción: "))

    match opcionGeneral:
        # ---------------------------- PARTE 1 DEL EJERCICIO ----------------------------
        case 1:
            while opcion != 7:
                menu_articulos()
                opcion = int(input("Introduce una opción: "))
                match opcion:
                    # Crear artículo
                    case 1:
                        # Se piden los datos necesarios para crear un artículo
                        idArticulo = generar_id(idArticulo)
                        nombre = str(input("Introduce el nombre del artículo: "))
                        precio = leer_float(mensajeError, minimoPrecioStock)
                        stock = leer_int(mensajeError, minimoPrecioStock)
                        if stock == 0:
                            activo = False
                        else:
                            activo = True
                        articulos.append({"id" : idArticulo, "nombre" : nombre, "precio" : precio, "stock" : stock, "activo" : activo})
                        # Indicarle al usuario que se realizó la operación correctamente
                        print(f"El artículo '{nombre}' con id '{idArticulo}', precio '{precio}€' y stock '{stock}' en estado: '{activo}' ha sido agregado correctamente.")
                    # Listar artículos
                    case 2:
                        # Primero se pregunta si se desea buscar artículos activos o inactivos y luego se le pasa como argumento a la función
                        buscar = str(input("¿Desea buscar artículos activos o inactivos?: "))
                        listar_articulos(articulos, buscar)
                    # Buscar artículo por id
                    case 3:
                        # Se pide primero un id y luego se le pasa como argumento a la función
                        idBusca = int(input("Introduce el id del artículo a buscar: "))
                        buscar_articulo_por_id(articulos, idBusca)
                    # Actualizar artículo
                    case 4:
                        # Se le pasa como argumento la lista de artículos
                        actualizar_articulo(articulos)
                    # Eliminar artículo
                    case 5:
                        eliminar_articulo(articulos)
                    # Alternar activo/inactivo
                    case 6:
                        alternar_activo(articulos)
                    # Si el usuario mete el número 7, se le indica que salió del programa
                    case 7:
                        print("Has salido del programa.")
                    # Si el usuario mete un número inválido, indicarselo. (Fuera de rango)
                    case _:
                        print("Número introducido inválido. ")
            # Aquí se pone opción a 0. Si no se estableciese cada vez que se realiza este bucle,
            # si salimos de una opción, no podemos irnos directamente a otra opción del menú, puesto
            # que opción = 7 y sale siempre.
            opcion = 0
        # PARTE 2 DEL EJERCICIO
        case 2:
            while opcion != 7:
                menu_usuarios()
                opcion = int(input("Introduce un número: "))
                match opcion:
                    # Crear usuario
                    case 1:
                        # Generamos un id afuera
                        # Si se genera dentro de la función (lo he probado), da error. Puesto que idUsuario es una variable global y no especifíca de la función
                        idUsuario = generar_id(idUsuario)
                        crear_usuario(listaUsuarios)
                    # Listar usuarios
                    case 2:
                        # Pedimos al usuario si quiere buscar usuarios activos o inactivos, y se lo pasamos como argumento a la función
                        buscar = str(input("¿Desea buscar usuarios activos o inactivos?: "))
                        # La función también tiene como argumento la lista de los usuarios
                        listar_usuarios(listaUsuarios, buscar)
                    # Buscar usuario por id
                    case 3:
                        # Pide al usuario un id para buscar y lo pasa como argumento a la función
                        idBusca = int(input("Introduce el id del usuario a buscar: "))
                        buscar_usuario_por_id(listaUsuarios, idBusca)
                    # Actualizar usuario
                    case 4:
                        actualizar_usuario(listaUsuarios)
                    # Eliminar usuario
                    case 5:
                        eliminar_usuario(listaUsuarios)
                    # Alternar activo/inactivo
                    case 6:
                        alternar_activo_usuario(listaUsuarios)
                    # Volver al menú principal
                    case 7:
                        print("Has salido de la sección ")
                    # Número introducido fuera de rango
                    case _:
                        print("El número introducido está fuera de rango")
            opcion = 0
        # PARTE DEL EJERCICIO 3
        case 3:
            print()
        # SALIR DEL PROGRAMA
        case 4:
            print("Has salido del programa")
        case _:
            print("El número introducido está fuera de rango")
