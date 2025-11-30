# importar librerias
import pickle  # Para guardar y recuperar listas de alumnos y notas en un archivo binario

# funciones
# (no hay funciones definidas en este script)

# variables globales
# Lista donde van todos los datos que se volcaran en el archivo de texto
notas = []
# Declarar la variable nombre
nombre = str()
# Declarar una variable que cambia según una condición para parar el bucle
pararBucle = False
# Indica si el script ya se ejecutó anteriormente
ejecutado = False

# lógica del código
# Intento abrir el archivo que indica si el script ya se ejecutó
try:
    with open("programaEjecutado.txt","r") as leerArchivo:
        # Leo el contenido del archivo
        contenido = leerArchivo.read()
        # Si el contenido es "1", significa que ya se ejecutó
        if contenido in "1":
            ejecutado = True
# Si el archivo no existe, consideramos que no se ha ejecutado
except FileNotFoundError:
    ejecutado = False

# Si el script ya se ejecutó
if ejecutado:
    # Informo al usuario
    print("El script ha sido ejecutado con anterioridad.")
    print("¿Desea recuperar los datos? (1 = Sí, 2 = No)")
    # Pido al usuario que decida si quiere recuperar los datos
    respuesta = int(input("Introduce una opción: "))
    # Evalúo la respuesta del usuario
    match respuesta:
        # Caso sí: recuperamos los datos
        case 1:
            print("Recuperando los datos...")
        # Caso no: ejecutamos desde cero
        case 2:
            print("Ejecutando desde 0...")
            ejecutado = False
        # Cualquier otro número: error
        case _:
            print("Error. El número introducido esta fuera del rango.")

# Si el script no se ha ejecutado o se decidió iniciar desde cero
if not ejecutado:
    # Bucle para introducir alumnos y notas
    while not pararBucle:
        # Pido el nombre del alumno
        nombre = str(input("Introduce el nombre de un alumno ('FIN para finalizar'): "))
        # Si el usuario escribe FIN, se termina el bucle
        if nombre == "FIN":
            pararBucle = True
        else:
            # Pido la nota del alumno
            nota = float(input(f"Introduce la nota del alumno con nombre '{nombre}': "))
            # Añado un diccionario con nombre y nota a la lista notas
            notas.append({"nombre" : nombre, "nota" : nota})

    # Marco que el script ya se ejecutó
    with open("programaEjecutado.txt","w") as scriptEjecutado:
        scriptEjecutado.write("1")

    # Guardo la lista de alumnos y notas en un archivo binario
    with open("alumnos.pkl","wb") as archivo:
        pickle.dump(notas,archivo)
        print("El archivo ha sido guardado correctamente")

# Si se decidió recuperar datos
else:
    # Informo que se va a recuperar datos
    print("El script ha sido ejecutado con anterioridad.")
    # Abro el archivo binario en modo lectura
    with open("alumnos.pkl","rb") as archivo:
        # Cargo los datos de alumnos y notas
        notas = pickle.load(archivo)
    # Muestro la lista de alumnos
    print("Lista de alumnos:")
    sumaNotas = 0
    notasTotales = 0
    # Recorro cada alumno
    for alumno in notas:
        # Muestro el nombre del alumno
        print(alumno["nombre"])
        # Incremento el contador de alumnos
        notasTotales = notasTotales + 1
        # Sumo la nota del alumno a la suma total
        sumaNotas = sumaNotas + alumno["nota"]
    # Calculo y muestro la media de las notas
    print(f"La media total de las notas es: {sumaNotas / notasTotales}")
