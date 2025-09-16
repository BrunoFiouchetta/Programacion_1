#validacion .isdigit()

"""
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles.
#Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas 
#(una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente
de copias utilizando el mismo índice en ambas listas Se debe utilizar un bucle while para navegar
por las opciones del menú hasta que el usuario elija salir.
"""


"""
1.	Ingresar lista de títulos:
o	Permite al usuario introducir los títulos de los libros en la biblioteca.
o	Ejemplo: El usuario introduce "1984", "Rebelión en la Granja".
"""

titulos = []
ejemplares = []
opcion = -1 



while opcion != 0:
    print("\n=== BIBLIOTECA ESCOLAR ===")
    print("1. Ingresar titulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar título")
    print("5. lista de agotados") #Muestra una lista de todos los títulos que tienen 0 copias disponibles.
    print("6. Agregar titulo")
    print("7. prestamo/devolucion")
    print("8. ver todos los titulos")
    print("0. salir")
    
    
    opcion = int(input("Opcion: "))
    
    
    if opcion == 1:
        cantidad = int(input("cuantos titulos va a ingresar? "))
        for i in range(cantidad):
            titulo = input(f"ingrese el título {i + 1}: ")
            titulos += [titulo]
            ejemplares += [0]

    elif opcion == 2:
        if not titulos:
            print("no hay titulos en el catalogo, ingrese titulos primero.")
        else:
            for i in range(len(titulos)):
                ejemplares_libro = int(input(f"ingrese la cantidad de ejemplares para '{titulos[i]}': "))
                ejemplares[i] += ejemplares_libro

    elif opcion == 3:
        if not titulos:
            print("no hay titulos en el catalogo.")
        else:
            print("\nCatalogo de libros:")
            for i in range(len(titulos)):
                print(f"{titulos[i]}: {ejemplares[i]} ejemplares")

    elif opcion == 4:
        if not titulos:
            print("No hay títulos en el catalogo.")
        else:
            titulo_consulta = input("Ingrese el titulo a consultar: ")
            if titulo_consulta in titulos:
                indice = titulos.index(titulo_consulta)
                print(f"{titulo_consulta} tiene {ejemplares[indice]} ejemplares disponibles.")
            else:
                print(f"'{titulo_consulta}' no esta en el catalogo.")

    elif opcion == 5:
        if not titulos:
            print("no hay titulos en el catalogo.")
        else:
            print("libros agotados:")
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"- {titulos[i]}")
                    agotados = True
            if not agotados:
                print("No hay libros agotados.")

    elif opcion == 6:
        nuevo_titulo = input("ingrese el nuevo titulo a agregar: ")
        if nuevo_titulo in titulos:
            print(f"{nuevo_titulo} ya esta en el catálogo.")
        else:
            titulos += [nuevo_titulo]
            ejemplares += [0]
            print(f"{nuevo_titulo} ha sido agregado al catalogo con 0 ejemplares.")



    elif opcion == 0:
        print("saliendo del programa...")