def menu_usuarios():
    menu = ["1. Crear usuario","2. Listar usuarios","3. Buscar usuario por id","4. Actualizar usuario","5. Eliminar usuario","6. Alternar activo/inactivo","7. Volver"]
    for entrada in menu:
        print(entrada)
# Crear usuarios

# Crear usuarios
def crear_usuario(usuarios):
    # Pide los datos necesarios
    nombre = str(input("Introduce un nombre: "))
    email = str(input("Introduce un email: "))
    # Comprueba si el email cumple con los requisitos o no
    while ("@" not in email) or ("." not in email):
        # Sino se le pide otra vez al usuario
        email = str(input("Error. El email no contiene '@' o '.' . Inténtalo de nuevo: "))
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
                        nuevoValor = str(input("Error. El email no contiene '@' o '.' . Inténtalo de nuevo: "))
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
