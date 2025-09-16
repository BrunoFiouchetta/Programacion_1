#validacion .isdigit()


titulos = []
ejemplares = []
opcion = 0


while opcion != 9:
    print("\n=== BIBLIOTECA ESCOLAR ===")
    print("1. Ingresar titulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar título")
    print("5. lista de agotados") #Muestra una lista de todos los títulos que tienen 0 copias disponibles.
    print("6. Agregar titulo")
    print("7. prestamo/devolucion")
    print("8. ver todos los titulos")
    print("9. salir")
    

    opcion = int(input("Opcion: "))
    
    
    if opcion == 1:
        cantidad = int(input("cuantos titulos va a ingresar? "))
        for i in range(cantidad):
            titulo = input(f"ingrese el título {i + 1}: ")
            if not titulo:
                print("El título no puede estar vacío.")
                continue
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
            titulo_consulta = input("Ingrese el titulo a consultar: ").strip().lower()
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

    elif opcion == 7:
        if not titulos:
            print("no hay titulos en el catalogo.")
        else:
            opcion_p_d = input("desea prestar (p) o devolver (d) un libro? ").lower()
            if opcion_p_d not in ['p', 'd']:
                print("accion invalida. use 'p' para prestar o 'd' para devolver.")
            else:
                titulo_prestamo = input("ingrese el titulo del libro: ")
                if titulo_prestamo in titulos:
                    indice = titulos.index(titulo_prestamo)
                    if opcion_p_d == 'p':
                        if ejemplares[indice] > 0:
                            ejemplares[indice] -= 1
                            print(f"Ha prestado {titulo_prestamo}. Quedan {ejemplares[indice]} ejemplares.")
                        else:
                            print(f"No hay ejemplares disponibles de {titulo_prestamo} para prestar.")
                    elif opcion_p_d == 'd':
                        ejemplares[indice] += 1
                        print(f"Ha devuelto {titulo_prestamo}. Ahora hay {ejemplares[indice]} ejemplares.")
                else:
                    print(f"{titulo_prestamo} no esta en el catalogo.")

    elif opcion == 8:
        if not titulos:
            print("no hay titulos en el catalogo.")
        else:
            print("todos los titulos en el catalogo:")
            for titulo in titulos:
                print(f"- {titulo}")



    elif opcion == 9:
        print("saliendo del programa...")