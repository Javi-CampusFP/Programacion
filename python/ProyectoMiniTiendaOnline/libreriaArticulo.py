def menu_articulos():
    # Declaramos las opciones del menú
    menu = ["1. Crear artículo", "2. Listar artículos", "3. Buscar artículo", "4. Actualizar artículo", "5. Eliminar un artículo", "6. Alternar activo/inactivo", "7. Salir"]
    # Imprimimos todas las entradas del menú en pantalla
    for entrada in menu:
        print(entrada)

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
        print(f"El artículo con id {idArticulo} ha sido eliminado.")

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