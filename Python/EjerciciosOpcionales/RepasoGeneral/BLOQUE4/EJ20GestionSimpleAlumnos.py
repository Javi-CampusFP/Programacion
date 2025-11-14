# Crea un programa con un diccionario llamado alumnos, donde:
    # La clave sea el nombre del alumno.
    # El valor sea su nota.
alumnos = []
listaOpciones = ["Añadir un alumno y su nota.", "Consultar la nota de un alumno.", "Modificar una nota existente.", "Mostrar todos los alumnos.", "Salir del programa."]

def imprimirMenu(lista):
    indice = 0
    for entrada in lista:
        indice = indice + 1
        print(f"{indice}. {entrada}")
    opcion = int(input("Introduce un número de índice: "))
    return opcion
def meterNuevoAlumnoYNota(alumno):
    nombreAlumno = str(input("Introduce el nombre del nuevo alumno: "))
    notaAlumno = float(input("Introduce la nota del nuevo alumno: "))
    alumno.append({"nombre" : nombreAlumno, "nota" : notaAlumno})

def consultarNota(alumno):
    nombreAlumno = str(input("Introduce el nombre del alumno: "))
    encontrado = False
    for a in alumno:
        if a["nombre"] == nombreAlumno:
            encontrado = True
            print(f"La nota del alumno con nombre {nombreAlumno} es {a["nota"]}")
    if not encontrado:
        print(f"El alumno con nombre '{nombreAlumno}' no ha sido encontrado.")

def modificarNota(listaAlumnos):
    nombreAlumno = str(input("Introduce el nombre del alumno: "))
    encontrado = False
    for alumno in listaAlumnos:
        if alumno["nombre"] == nombreAlumno:
            encontrado = True
            nuevaNota = float(input("Introduce la nueva nota: "))
            alumno["nota"] = nuevaNota
    if not encontrado:
        print("El alumno con nombre {nombreAlumno} no ha sido encontrado.")

def mostrarTodosAlumnos(alumno):
    indice = 0
    for a in alumno:
        indice = indice + 1 
        for alu,nota in a.items():
            print(f"{indice}. {alu} : {nota}")
        

opcion = 0

while opcion != 5:
    opcion = imprimirMenu(listaOpciones)
    match opcion:
        # 1. Añadir un alumno y su nota.
        case 1:
            meterNuevoAlumnoYNota(alumnos)
        # 2. Consultar la nota de un alumno.
        case 2:
            consultarNota(alumnos)
        # 3. Modificar una nota existente.
        case 3:
            modificarNota(alumnos)
        # 4. Mostrar todos los alumnos.
        case 4:
            mostrarTodosAlumnos(alumnos)
        # 5. Salir del programa.
        case 5:
            print("Has salido del programa de gestión de alumnos.")
        case _:
            print("El número introducido no esta dentro del rango válido de opciones.")
