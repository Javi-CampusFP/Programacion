# Menú
print("1. Mostrar catálogo")
print("2. Buscar juego por nombre")
print("3. Añadir nuevo juego")
print("4. Calcular precio medio")
print("5. Salir")
# Declaramos el catálogo de los juegos y esperamos el input del usuario
opcion = int(input("Introduce un número de índice: "))
catalogoJuegos = {"Elden Ring" : (49.00, "Acción"), "The Last of Us" : (29.00, "Acción"), "Tomb Raider" : (20.00, "Aventura")}

while opcion != 5:
    match opcion:
        # Opción 1, muestra el catalogo de todos los juegos junto con el precio y el genero
        case 1:
            print()
            for juego in catalogoJuegos:
                print(f"- {juego} Precio: {catalogoJuegos[juego][0]} Género: {catalogoJuegos[juego][1]}")
        # Pide un nombre al usuario y luego lo busca entre el catálogo
        case 2:
            buscar = str(input("Introduce el nombre del videojuego: "))
            if buscar not in catalogoJuegos:
                print(f"El videojuego {buscar} no esta en el catálogo de juegos.")
            else:
                print(f"- {buscar} Precio: {catalogoJuegos[buscar][0]} Género: {catalogoJuegos[buscar][1]}")
        # Añadir un nuevo juego dentro del catálogo
        case 3:
            nombreJuego = str(input("Introduce el nombre del juego: "))
            # Si el juego ya esta dentro del catalogo, le pide el nombre otra vez.
            while nombreJuego in catalogoJuegos:
                nombreJuego = str(input("Error. El nombre del videojuego ya existe en la lista. Intentálo de nuevo: "))
            # Declarar las variables necesarias y meterlas en una tupla dentro del diccionario
            precioJuego = float(input("Introduce el precio del videojuego: "))
            generoJuego = str(input("Introduce el género del videojuego: "))
            catalogoJuegos.update({nombreJuego : (precioJuego, generoJuego)})
        # for nombre, datos in juegos.items(): ...
        case 4:
            totalGeneral = 0
            # For dentro de un for en un for (?), calculamos la media total de todos
            for nombre, datos in catalogoJuegos.items():
                totalGeneral = datos[0] + totalGeneral
            medio = totalGeneral / len(catalogoJuegos)
            print(f"La media total de precio de todos los videojuegos es: {medio}")
        case _:
            print("Error. Número introducido incorrecto (1 al 5). Inténtalo de nuevo: ")
    print("1. Mostrar catálogo")
    print("2. Buscar juego por nombre")
    print("3. Añadir nuevo juego")
    print("4. Calcular precio medio")
    print("5. Salir")
    opcion = int(input("Introduce un número de índice: "))
else:
    print("Has salido del programa.")
