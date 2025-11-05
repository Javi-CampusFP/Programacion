# Variables 
dicProductos = {"vegetales" : "perecedero", "frutas" : "perecedero", "carne" : "perecedero", "enlatados" : "no perecederos", "frutos secos" : "no perecederos"}
# Funciones
def esPerecedero (productos):
    producto, perecedero = productos
    return perecedero == "perecedero"
# Lógica del código
productosPerecederos = filter(esPerecedero,dicProductos.items())
print(dict(productosPerecederos))