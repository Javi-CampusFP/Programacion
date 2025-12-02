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
# Crear el array vacío
array_clientes = clientes_core.crear_array()
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
            cliente = clientes_core.alta_cliente(array_clientes)
            # Si el primer registro (necesario para crear el array) está vácio
            # poner en la posición [0] del array en 2D el valor de cliente
            if array_clientes[0][0] == "":
                array_clientes[0] = cliente
            # Sino, simplemente llamamos a la función agregar_registro
            # Que agrega el registro con un append de numpy en el axis 0
            else:
                array_clientes = clientes_core.agregar_registro(cliente,array_clientes)
        # Listar todos los clientes
        case 2:
            clientes_core.listar_clientes(array_clientes)
        # Buscar cliente por DNI
        case 3:
            clientes_core.buscar_cliente_dni(array_clientes)
        # Modificar teléfono de un cliente con el DNI
        case 4:
            clientes_core.modificar_telefono_dni(array_clientes)
        # Eliminar cliente por DNI
        case 5:
            array_clientes = clientes_core.eliminar_cliente_dni(array_clientes)
        # Guardar clientes en un fichero
        case 6:
            clientes_core.guardar_clientes_fichero(array_clientes,ruta)
        # Cargar clientes desde un fichero
        case 7:
            array_clientes = clientes_core.cargar_datos(array_clientes,ruta)
        # Salir del programa.
        case 8:
            print("Has salido del programa.")
        case _:
            print(f"El valor introducido '{opcionElegida}' está fuera del rángo.")
