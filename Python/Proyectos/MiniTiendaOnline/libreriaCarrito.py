# ---------------------------- Funciones PARTE 3 ----------------------------

# Menú de ventas (muestra las opciones disponibles para gestionar el proceso de compra)
def menu_ventas():
    menu = ["1. Seleccionar usuario activo.", "2. Añadir artículo al carrito", "3. Quitar artículo del carrito", "4. Ver carrito (detalle y total)",
        "5. Confirmar compra (resta stock y registra venta)", "6. Historial de ventas por usuario", "7. Vaciar carrito", "8. Salir"]
    for entrada in menu:
        print(entrada)
# Selecciona un usuario por id y lo marca como activo, devuelve el id si se encuentra
# (devuelve None implícitamente si no existe)
def seleccionar_usuario_activo(usuarios):
    encontrado = False
    idBuscar = int(input("Introduce un id de usuario: "))
    for usuario in usuarios:
        if usuario["id"] == idBuscar:
            encontrado = True
            usuario["activo"] = True
            # Mostrar los datos del usuario encontrado
            for campoDato, dato in usuario.items():
                print(f"{campoDato} : {dato}")
            print(f"El usuario con id {idBuscar} ha sido encontrado .")
            return idBuscar
    if encontrado == False:
        print(f"El usuario con id '{idBuscar}' no existe. Inténtalo de nuevo.")

# Añade un artículo al carrito comprobando existencia, estado y stock disponible
def anadir_al_carrito(carrito, articulos):
    idProducto = int(input("Introduce el id del artículo a introducir en el carrito: "))
    encontrado = False
    reemplazar = False
    activo = False
    for articulo in articulos:
        if articulo["id"] == idProducto:
            encontrado = True
            # Solo se puede añadir si el artículo está activo
            if articulo["activo"] == True:
                activo = True
                stockDisponible = articulo["stock"]
                # Si el producto ya está en el carrito, ajustar el stock disponible
                for producto in carrito:
                    if producto[0] == idProducto:
                        stockDisponible = stockDisponible - producto[1]
                        reemplazar = True
                        sacarIndice = producto
                print(f"Stock disponible del producto con id '{idProducto}' : {stockDisponible}")
                # Pedir cantidad (usa la función leer_int definida en otra parte del programa)
                cantidad = leer_int(mensajeError, minimoVenta)
                # Validar que la cantidad no supere el stock disponible
                while cantidad > stockDisponible:
                    print("La cantidad no puede ser mayor al stock disponible ", )
                    cantidad = leer_int(mensajeError, minimoVenta)
                # Si ya existía en el carrito, reemplazar la entrada; si no, añadir nueva tupla
                if reemplazar == True:
                    carrito[sacarIndice] = (idProducto, cantidad)
                else:
                    carritoFinal = (idProducto, cantidad)
                    carrito.append(carritoFinal)
    # Si no se encontró o no está activo, informar al usuario
    if encontrado == False or activo == False:
        print(f"El producto con id '{idProducto}', no ha sido encontrado o no esta activado.")

# Elimina un artículo del carrito por su id (si existe en el carrito)
def quitar_del_carrito(carrito):
    encontrado = False
    idBuscar = int(input("Introduce un id para eliminar de tu carrito: "))
    for articulo in carrito:
        if articulo[0] == idBuscar:
            encontrado = True
            carrito.remove(articulo)
            print(f"El artículo con id '{idBuscar}' ha sido eliminado con éxito del carrito.")
    if encontrado == False:
        print(f"El artículo con id '{idBuscar}' no ha sido encontrado.")

# Calcula el total del carrito recorriendo cada producto y sumando precio * cantidad
# Además imprime línea por línea id, precio y cantidad para revisión
def calcular_total_carrito(carrito, articulos):
    total = 0.0
    for producto in carrito:
        productoId = producto[0]
        productoCantidad = producto[1]
        for articulo in articulos:
            if articulo["id"] == productoId:
                precioPorUnidad = articulo["precio"]
                print(f"id: '{productoId}', Precio '{precioPorUnidad}', Cantidad '{productoCantidad}'")
                total = precioPorUnidad * productoCantidad + total
    return total

# Confirma la compra: valida cada artículo del carrito, procesa la venta (resta stock),
# crea un snapshot de la venta y lo añade a la lista de ventas.
def confirmar_compra(carrito, articulos, usuario_activo, ventas):
    # Validaciones básicas

    if len(carrito) == 0:
        print("El carrito está vacío. Añade productos antes de confirmar la compra.")

        # Comprobar existencia/estado/stock de todos los productos del carrito
    for producto in carrito:
        producto_id = producto[0]
        cantidad = producto[1]
        articuloEncontrado = False
        for articulo in articulos:
            if articulo["id"] == producto_id:
                articuloEncontrado = True
                # Informe si el artículo no está activo
                if articulo["activo"] == False:
                    print("El artículo con id", producto_id, "no está activo. No se puede confirmar la compra.")

                # Informe si la cantidad solicitada supera el stock
                if cantidad > articulo["stock"]:
                    print("No hay suficiente stock para el artículo", articulo["nombre"], "(id", producto_id, "). Stock disponible:", articulo["stock"], "Cantidad pedida:", cantidad)
            if not articuloEncontrado:
                print("El artículo con id", producto_id, "no existe. No se puede confirmar la compra.")

        # Procesar la venta (restar stock, crear snapshot, vaciar carrito)
        items_venta = []
        total_venta = 0.0

        for producto in carrito:
            producto_id = producto[0]
            cantidad = producto[1]
            # buscar el artículo otra vez y procesarlo
            for articulo in articulos:
                if articulo["id"] == producto_id:
                    precio_unitario = articulo["precio"]
                    subtotal = precio_unitario * cantidad
                    items_venta.append({
                        "id": producto_id,
                        "nombre": articulo["nombre"],
                        "cantidad": cantidad,
                        "precio_unitario": precio_unitario,
                        "subtotal": subtotal
                    })
                    total_venta = total_venta + subtotal
                    # restar stock
                    articulo["stock"] = articulo["stock"] - cantidad
                    if articulo["stock"] <= 0:
                        articulo["stock"] = 0
                        articulo["activo"] = False

        # snapshot de la venta
        ventasSnapshots_local = {
            "id_venta": idVenta,
            "usuario_id": usuario_activo,
            "items": items_venta,
            "total": total_venta
        }
        ventas.append(ventasSnapshots_local)

        # vaciar carrito
        print(f"Compra confirmada. ID venta: {idVenta} Usuario:, {usuario_activo}, Total: {total_venta}€")

# Muestra el historial de ventas filtrado por usuario (imprime cada venta y sus items)
def historial_ventas_por_usuario(ventas, usuario_id):
    encontrado = False
    for venta in ventas:
        if venta["usuario_id"] == usuario_id:
            encontrado = True
            print(f"Venta id: {venta["id_venta"]} | Total:{venta['total']}€")
            for item in venta["items"]:
                print(f"id:, {item["id"]}, nombre: {item["nombre"]}, cantidad: {item["cantidad"]}, precio_u: {item['precio_unitario']} subtotal: {item['subtotal']}")
    if encontrado == False:
        print("No hay ventas registradas para el usuario con id", usuario_id)