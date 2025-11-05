# Variables
dicTarea = {"tarea1" : "urgente", "tarea2" : "leve", "tarea3" : "urgente"}
# Funciones
def tareasUrgente (tarea):
    nombre,prioridad = tarea
    return prioridad == "urgente"
# Lógica del código
dicUrgentes = filter(tareasUrgente, dicTarea.items())
print(dict(dicUrgentes))
