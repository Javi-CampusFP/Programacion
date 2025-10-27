# Esto es introducir una libreria 1 a 1 
# from libreria import menu_general
# from libreria import generar_id
# from libreria import menu_ventas
# from libreria import menu_articulos
# from libreria import menu_usuarios

# Importar toda la libreria
import libreria


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


# Registrar las ventas dentro de una variable
ventas = []
ventasSnapshots = {}
# Registrar el carrito dentro de otra variable que sera una lista con tuplas dentro
# carrito_actual = [(articulo_id, cantidad)]
carrito_actual = []
# Meter el usuario activo actual dentro de una variable
usuario_activo = int
# Mínimo de la cantidad de venta
minimoVenta = 1
idVenta = 0

# ---------------------------- Lógica del código ----------------------------
# MENÚ GENERAL
while opcionGeneral != 4:
    # Llama a la función para imprimir el menú
    libreria.menu_general()
    # Pide una opción al usuario
    opcionGeneral = int(input("Introduce una opción: "))

    match opcionGeneral:
        # ---------------------------- PARTE 1 DEL EJERCICIO ----------------------------
        case 1:
            while opcion != 7:
                libreria.menu_articulos()
                opcion = int(input("Introduce una opción: "))
                match opcion:
                    # Crear artículo
                    case 1:
                        # Se piden los datos necesarios para crear un artículo
                        idArticulo = libreria.generar_id(idArticulo)
                        nombre = str(input("Introduce el nombre del artículo: "))
                        precio = libreria.leer_float(mensajeError, minimoPrecioStock)
                        stock = libreria.leer_int(mensajeError, minimoPrecioStock)
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
                        libreria.listar_articulos(articulos, buscar)
                    # Buscar artículo por id
                    case 3:
                        # Se pide primero un id y luego se le pasa como argumento a la función
                        idBusca = int(input("Introduce el id del artículo a buscar: "))
                        libreria.buscar_articulo_por_id(articulos, idBusca)
                    # Actualizar artículo
                    case 4:
                        # Se le pasa como argumento la lista de artículos
                        libreria.actualizar_articulo(articulos)
                    # Eliminar artículo
                    case 5:
                        libreria.eliminar_articulo(articulos)
                    # Alternar activo/inactivo
                    case 6:
                        libreria.alternar_activo(articulos)
                    # Si el usuario mete el número 7, se le indica que salió de la sección de artículos
                    case 7:
                        print("Has salido de la sección de artículos.")
                    # Si el usuario mete un número inválido, indicarselo. (Fuera de rango)
                    case _:
                        print("El número introducido está fuera de rango")
            # Aquí se pone opción a 0. Si no se estableciese cada vez que se realiza este bucle,
            # si salimos de una opción, no podemos irnos directamente a otra opción del menú, puesto
            # que opción = 7 y sale siempre.
            opcion = 0
        # ---------------------------- PARTE 2 DEL EJERCICIO ----------------------------
        case 2:
            while opcion != 7:
                libreria.menu_usuarios()
                opcion = int(input("Introduce un número: "))
                match opcion:
                    # Crear usuario
                    case 1:
                        # Generamos un id afuera
                        # Si se genera dentro de la función (lo he probado), da error. Puesto que idUsuario es una variable global y no especifíca de la función
                        idUsuario = libreria.generar_id(idUsuario)
                        libreria.crear_usuario(listaUsuarios)
                    # Listar usuarios
                    case 2:
                        # Pedimos al usuario si quiere buscar usuarios activos o inactivos, y se lo pasamos como argumento a la función
                        buscar = str(input("¿Desea buscar usuarios activos o inactivos?: "))
                        # La función también tiene como argumento la lista de los usuarios
                        libreria.listar_usuarios(listaUsuarios, buscar)
                    # Buscar usuario por id
                    case 3:
                        # Pide al usuario un id para buscar y lo pasa como argumento a la función
                        idBusca = int(input("Introduce el id del usuario a buscar: "))
                        libreria.buscar_usuario_por_id(listaUsuarios, idBusca)
                    # Actualizar usuario
                    case 4:
                        libreria.actualizar_usuario(listaUsuarios)
                    # Eliminar usuario
                    case 5:
                        libreria.eliminar_usuario(listaUsuarios)
                    # Alternar activo/inactivo
                    case 6:
                        libreria.alternar_activo_usuario(listaUsuarios)
                    # Volver al menú principal
                    case 7:
                        print("Has salido de la sección de usuarios.")
                    # Número introducido fuera de rango
                    case _:
                        print("El número introducido está fuera de rango")
            opcion = 0
        # ---------------------------- PARTE 3 DEL EJERCICIO ----------------------------
        case 3:
            while opcion != 8:
                libreria.menu_ventas()
                opcion = int(input("Introduce un número: "))
                match opcion:
                    # Seleccionar usuario activo
                    case 1:
                        usuario_activo = libreria.seleccionar_usuario_activo(listaUsuarios)
                    # Añadir artículo al carrito
                    case 2:
                        libreria.anadir_al_carrito(carrito_actual, articulos)
                    # Quitar artículo del carrito
                    case 3:
                        libreria.quitar_del_carrito(carrito_actual)
                    # Ver carrito (detalle y total)
                    case 4:
                        totalFinal = libreria.calcular_total_carrito(carrito_actual, articulos)
                        print("El total del carrito es: ",totalFinal)
                    # Confirmar compra (resta stock y registra venta)
                    case 5:
                        idVenta = libreria.generar_id(idVenta)
                        libreria.confirmar_compra(carrito_actual, articulos, usuario_activo, ventas)
                    # Historial de ventas por usuario
                    case 6:
                        libreria.historial_ventas_por_usuario(ventas,usuario_activo)
                    # Vaciar carrito
                    case 7:
                        carrito_actual = []
                    # Salir de la sección de ventas
                    case 8:
                        print("Has salido de la sección de ventas.")
                    case _:
                        print("El número introducido está fuera de rango")
            opcion = 0
        # SALIR DEL PROGRAMA
        case 4:
            print("Has salido del programa")
        case _:
            print("El número introducido está fuera de rango")
