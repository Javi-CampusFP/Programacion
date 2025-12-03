# Importar librerias
import clientes_core
from rich import print
# Funciones

# Variables globales
# Opciones del menú
opciones_generales = ["Alta de cliente","Listar todos los clientes","Buscar cliente por DNI",
                      "Modificar teléfono de un cliente","Eliminar cliente","Guardar clientes en fichero",
                      "Cargar clientes desde fichero","Salir"]
# Declaro la variable para que no de error en el while.
opcionElegida = int()
# Crear la lista vacia
clientes = []
# Ruta del fichero donde se guardan los archivos (en el directorio de trabajo actual)
ruta = "registro.txt"
# Lógica del código
# El bucle principal del programa. Sale del bucle cuando se elige la opción "Salir"
while opcionElegida != 8:
    opcionElegida = clientes_core.imprimir_menu(opciones_generales)
    match opcionElegida:
        # Alta de cliente
        case 1:
            # Se llama a la función y se almacena el return en una variable
            cliente = clientes_core.alta_cliente(clientes)
            # Añadir el diccionario a la lista
            clientes.append(cliente)
        # Listar todos los clientes
        case 2:
            clientes_core.listar_clientes(clientes)
        # Buscar cliente por DNI
        case 3:
            clientes_core.buscar_cliente_dni(clientes)
        # Modificar teléfono de un cliente con el DNI
        case 4:
            clientes_core.modificar_telefono_dni(clientes)
        # Eliminar cliente por DNI
        case 5:
            clientes = clientes_core.eliminar_cliente_dni(clientes)
        # Guardar clientes en un fichero
        case 6:
            clientes_core.guardar_clientes_fichero(clientes,ruta)
        # Cargar clientes desde un fichero
        case 7:
            clientes = clientes_core.cargar_datos(clientes,ruta)
        # Salir del programa.
        case 8:
            print("Has salido del programa.")
        case _:
            print(f"El valor introducido '{opcionElegida}' está fuera del rángo.")
