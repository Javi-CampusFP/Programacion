# menú
print("1. Añadir tarea")
print("2. Mostrar todas las tareas")
print("3. Marcar tarea como completada")
print("4. Eliminar tarea")
print("5. Salir")
# El usuario introduce una opción
opcion = int(input("Introduce un número de índice para realizar una operación: "))
# Lista de tareas declarada vacia
listaTareas = []
# While con match case
while opcion != 5:
    match opcion:
        # Comprueba si ya habia dentro una tarea con el nombre ídentico y se lo indica al usuario.
        # Sino, se añade la tarea
        case 1:
            tareaExtra = str(input("Introduce una nueva tarea extra a la lista de tareas: "))
            while tareaExtra in listaTareas:
                tareaExtra = str(input("Error. Tarea duplicada: Introduce una nueva tarea extra a la lista de tareas: "))
            else:
                listaTareas.append(tareaExtra)
                print(f"La tarea {tareaExtra} ha sido añadida con exito.")
        # Imprime en pantalla las tareas con el número de índice
        case 2:
            print()
            print("- Lista de tareas: ")
            for tareas in range(len(listaTareas)):
                print(f"{tareas + 1}. {listaTareas[tareas]}")
            print()
        case 3:
            # El usuario introduce un número que se comprueba si es un número válido, sino se vuelve a pedir
            completarTarea = int(input("¿Que tarea es la que desea completar? Introduce número de índice: "))
            completarTarea = completarTarea - 1
            if completarTarea not in range(len(listaTareas)):
                completarTarea = int(input("Error. Introduce un número de índice válido: "))
            else:
                # Si el número es válido se convierte el número de índice de la lista en una tupla
                # con el siguiente contenido: (nombreTarea, "Tarea completada.")
                listaTareas[completarTarea] = (listaTareas[completarTarea], "Tarea completada.")
                print(f"La tarea {listaTareas[completarTarea][0]} ha sido marcada como completada")
        case 4:
            # Introduce un número el usuario y se elimina la posición del número introducido dentro de la lista
            eliminarTarea = int(input("¿Qué tarea es la que desea eliminar? Introduce el número de índice: "))
            eliminarTarea = eliminarTarea - 1
            listaTareas.pop(eliminarTarea)
        case _:
            # Si el usuario introduce un número fuera del rango
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    # Mostrar otra vez el menú
    print("1. Añadir tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    # Pedir otra vez input, sino seria un while infinito
    opcion = int(input("Introduce un número de índice para realizar una operación: "))
else:
    print("Ha salido del programa.")
