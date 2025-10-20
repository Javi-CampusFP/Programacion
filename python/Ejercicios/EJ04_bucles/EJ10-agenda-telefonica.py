print("1. Añadir contacto")
print("2. Buscar contacto")
print("3. Eliminar contacto")
print("4. Mostrar todos")
print("5. Salir")
opcion = int(input("Introduce un número de índice: "))
# Declaramos la agenda
agenda = {}
while opcion != 5:
    match opcion:
        # Añadir contacto
        case 1:
            # Pedimos input al usuario y comprobamos si el contacto existe
            nombre = str(input("Introduce el nombre del contacto: "))
            # Si existe se avisa, sino, se introduce en la agenda con los demas datos
            if nombre in agenda:
                print(f"El nombre {nombre} ya existe en la agenda.")
            else:
                telefono = str(input("Introduce el número de teléfono: "))
                email = str(input("Introduce el email del contacto: "))
                agenda.update({nombre : (telefono, email)})
                print(f"El contacto {nombre} ha sido agregado correctamente.")
        # Buscar contacto
        case 2:
            # Pedimos el nombre a buscar, y vemos si esta dentro de "agenda"
            # si esta dentro, sacamos los valores del nombre, el teléfono y el email
            nombre = str(input("Introduce el nombre para buscar al contacto: "))
            if nombre in agenda:
                print(f"- Nombre: {nombre} Teléfono: {agenda[nombre][0]} Email: {agenda[nombre][1]}")
        # Eliminar contacto
        case 3:
            nombre = str(input("Introduce el nombre para eliminar de contactos: "))
            # Eliminamos con del en la posicion agenda [ nombre ]. Si existe, sino, se avisa al usuario
            if nombre in agenda:
                del agenda[nombre]
                print(f"El contacto {nombre} ha sido eliminado correctamente.")
            else:
                print(f"El nombre {nombre} no se encuentra en la agenda de contactos.")
        # Mostrar todos
        case 4:
            # Hacemos un for que recorra todos los items para poder ver el nombre, el email y el teléfono
            print("Contactos: ")
            for nombres,telefonoEmailTodos in agenda.items():
                print(f"- Nombre: {nombres} Teléfono: {telefonoEmailTodos[0]} Email: {telefonoEmailTodos[1]}")
        # Número introducido fuera de rango
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
