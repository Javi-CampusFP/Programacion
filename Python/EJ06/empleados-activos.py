# Variables
empleados = {"empleado1" : "activo", "empleado2" : "de baja", "empleado3" : "activo"}
# Funciones
def detectarActivos (empleado):
    nombre,estado = empleado
    return estado == "activo"
# Lógica del código
empleadosActivos = filter(detectarActivos, empleados.items())
print(dict(empleadosActivos))
