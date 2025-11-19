# Importar librerias
import damas_core
# Variables
menuPrincipal = ["Jugador vs Jugador", "Jugador vs Máquina", "Salir"]
# Lógica
opcionPrincipal = 0
while opcionPrincipal != 3:
    damas_core.imprimirMenu(menuPrincipal)
