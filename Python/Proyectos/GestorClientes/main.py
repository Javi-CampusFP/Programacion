# Importar librerias
import clientes_core
# Funciones

# Variables globales
# Opciones del menú 
opciones_generales = ["Alta de cliente","Listar todos los clientes","Buscar cliente por DNI",
                      "Modificar teléfono de un cliente","Eliminar cliente","Guardar clientes en fichero",
                      "Cargar clientes desde fichero","Salir"]
# Declaro la variable para que no de error en el while.
opcionElegida = int()
array_clientes = clientes_core.crear_array()
idCliente = 0
# Lógica del código
# El bucle principal del programa. Sale del bucle cuando se elige la opción "Salir"
while opcionElegida != 8:
    opcionElegida = clientes_core.imprimir_menu(opciones_generales)
    match opcionElegida:
        # Alta de cliente
        case 1:
            dni = clientes_core.alta_cliente(array_clientes)
            nombre = clientes_core.longitudString(2,"nombre")
            apellidos = clientes_core.longitudString(8,"apellidos")
            email = clientes_core.longitudString(14,"email")
            idCliente = idCliente + 1
            array_clientes[idCliente] 
        # Listar todos los clientes
        case 2:
            print()
        # Buscar cliente por DNI
        case 3:
            print()
        # Modificar teléfono de un cliente
        case 4:
            print()
        # Eliminar cliente
        case 5:
            print()
        # Guardar clientes en un fichero
        case 6:
            print()
        # Cargar clientes desde un fichero
        case 7:
            print()
        # Salir del programa.
        case 8:
            print("Has salido del programa.")
        case _:
            print(f"El valor introducido '{opcionElegida}' está fuera del rángo.")