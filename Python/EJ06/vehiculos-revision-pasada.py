# Variables
dicVehiculos = {"Toyota X modelo" : "revisado", "Mercedes X modelo" : "no revisado"}
# Funciones
def vehiculoRevisado(vehiculo):
    modelo,revision = vehiculo
    return revision == "revisado"
# Lógica del código
vehiculoRevisado = filter(vehiculoRevisado, dicVehiculos.items())
print(dict(vehiculoRevisado))