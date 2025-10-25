# Variables globales

# Modelo de datos seleccionado: A
# Diccionario de articulos metido dentro de una lista
articulos = [{"id" : 1, "nombre" : "Ratón", "precio" : 12.5, "stock": 20, "activo": True}]
# Definir la variable opcion.
opcion = int
# Declaramos id del artículo 1, porque ya hay uno con id 1
idArticulo = 1
# Mensaje de error en int y en float
mensajeError = "Error. El número introducido no es válido."
# Solo artículos activos
articulo_activo = True
minimoPrecioStock = 0

# Funciones
# Función de mostrar el menú
def menu_articulos():
    # Declaramos las opciones del menú
    menu = ["1. Crear artículo", "2. Listar artículos", "3. Buscar artículo", "4. Actualizar artículo", "5. Eliminar un artículo", "6. Alternar activo/inactivo", "7. Salir"]
    # Imprimimos todas las entradas del menú en pantalla
    for entrada in menu:
        print(entrada)

# Función para generar un id automáticamente
def generar_id(idArticulos):
    # Generar la id de un artículo nuevo
    idArticulos = idArticulos + 1
    # Devuelve el valor
    return idArticulos
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
    # Listar los articulos recorriendo la lista
    for articulo in listaArticulos:
        # recorrer el diccionario clave valor e imprimirlo por pantalla
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
    # Si no se encontro el artículo se le indica al usuario
    if articuloEncontrado == False:
        print(f"El artículo con la id {id_busqueda} no ha sido encontrado.")

# Función para actualizar X artículo
def actualizar_articulo(listaArticulos):
    # Parametros que podemos actualizar
    camposArticulo = ["Nombre", "Precio", "Stock"]
    # Id del artículo a actualizar
    idArticulo = int(input("Introduce el id del artículo a cambiar: "))
    # Imprimir los parametros actualizables
    for articulo in camposArticulo:
        print(f"- {articulo}")
    # Elegir la opción a actualizar
    actualizar = str(input("¿Qué desea actualizar?: "))
    # Declarar si encontramos el artículo o no
    articuloEncontrado = False
    # Para articulo en listaArticulos buscar si el valor "id" coincide con la id introducida
    for articulo in listaArticulos:
        if articulo["id"] == idArticulo:
            # Si coincide, actualizamos la variable articuloEncontrado para indicar que lo encontramos
            articuloEncontrado = True

            # Actualizar segun lo elegido por el usuario
            if actualizar.lower() == "nombre":
                nuevoValor = str(input("Introduce el nombre nuevo: "))
            elif actualizar.lower() == "precio":
                nuevoValor = leer_float(mensajeError)
            else:
                nuevoValor = leer_int(mensajeError)

            # Actualizar el diccionario con el nuevo valor en la posición que le corresponde
            articulo.update({actualizar : nuevoValor})
            # Indicarle al usuario que se actualizo correctamente
            print(f"El valor '{actualizar}' del artículo '{idArticulo}' ha sido actualizado con el valor '{nuevoValor}' correctamente.")
    # Si no se ha encontrado el artículo, el programa lo indica
    if articuloEncontrado == False:
        print(f"El artículo con id {idArticulo} no ha sido encontrado.")


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
    idArticulo = int(input("Introduzca el id del artículo a activar: "))
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
    # Si no se encontro el producto se indica
    if articuloEncontrado == False:
        print(f"El artículo con id '{idArticulo}' no ha sido encontrado.")


# Lógica del código
while opcion != 7:
    menu_articulos()
    opcion = int(input("Introduce una opción: "))
    match opcion:
        # Crear artículo
        case 1:
            # Se piden los datos necesarios para crear un articulo
            idArticulo = generar_id(idArticulo)
            nombre = str(input("Introduce el nombre del artículo: "))
            precio = leer_float(mensajeError, minimoPrecioStock)
            stock = leer_int(mensajeError, minimoPrecioStock)
            if stock == 0:
                activo = False
            else:
                activo = True
            articulos.append({"id" : idArticulo, "nombre" : nombre, "precio" : precio, "stock" : stock, "activo" : activo})
            # Indicarle al usuario que se realizo la operación correctamente
            print(f"El artículo '{nombre}' con id '{idArticulo}', precio '{precio}€' y stock '{stock}' en estado: '{activo}' ha sido agregado correctamente.")
        # Listar artículos
        case 2:
            listar_articulos(articulos)
        # Buscar artículo por id
        case 3:
            idBusca = int(input("Introduce el id del artículo a buscar: "))
            buscar_articulo_por_id(articulos, idBusca)
        # Actualizar artículo
        case 4:
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
