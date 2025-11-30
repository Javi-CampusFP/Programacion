# importar librerias
import pickle

# funciones

# clases

# Defino la clase Producto con nombre, precio y cantidad
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

# variables globales
# Lista donde se guardarán todos los productos del inventario
inventario = []

# lógica del código
# Intento abrir el archivo inventario.pkl para cargar productos previos
try:
    # Abrimos el archivo en modo lectura binaria
    with open("inventario.pkl","rb") as archivo:
        # Cargo los productos guardados en la lista inventario
        inventario = pickle.load(archivo)
    # Informo al usuario
    print("Inventario cargado correctamente.")
# Si el archivo no existe o está vacío, se crea un inventario nuevo
except (FileNotFoundError, EOFError):
    print("No existe un inventario previo. Se creará uno nuevo.")
    inventario = []

# Bucle para añadir productos al inventario
pararBucle = False  # Variable para controlar cuándo parar
while not pararBucle:
    # Pido al usuario el nombre del producto
    nombre = input("Introduce el nombre del producto ('FIN' para finalizar): ")
    # Si el usuario escribe FIN, se termina el bucle
    if nombre.upper() == "FIN":
        pararBucle = True
    else:
        # Pido el precio del producto
        precio = float(input(f"Introduce el precio del producto '{nombre}': "))
        # Pido la cantidad del producto
        cantidad = int(input(f"Introduce la cantidad del producto '{nombre}': "))
        # Creo un objeto Producto con los datos introducidos
        producto = Producto(nombre, precio, cantidad)
        # Lo añado a la lista inventario
        inventario.append(producto)

# Guardo la lista completa en inventario.pkl en modo escritura binaria
with open("inventario.pkl","wb") as archivo:
    pickle.dump(inventario, archivo)
# Informo al usuario de que se ha guardado correctamente
print("El inventario ha sido guardado correctamente.")

# Muestro todos los productos del inventario
print("Listado de productos en el inventario:")
for producto in inventario:
    # Formateo la salida según la consigna
    print(f"Producto: {producto.nombre} – Precio: {producto.precio} – Cantidad: {producto.cantidad}")
