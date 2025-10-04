libros = ["1984", "El Principito", "Don Quijote"]
copias = [3, 0, 5]

while True:
    print("\nMenú Biblioteca:")
    print("1. Ingresar lista de nuevos libros")
    print("2. Ingresar cantidad de copias de los libros")
    print("3. Mostrar biblioteca completa")
    print("4. Consultar copias de un libro")
    print("5. Listar libros sin copias disponibles")
    print("6. Agregar un libro nuevo")
    print("7. Prestar o devolver un libro")
    print("8. Listar libros con copias disponibles")
    print("9. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        cant_a_ingresar = input("¿Cuántos libros desea agregar?: ")
        if not cant_a_ingresar.isdigit():   # Validar si es un número
            print("ERROR: Debe ingresar un número.")
            continue
        cant_a_ingresar = int(cant_a_ingresar)

        for i in range(cant_a_ingresar):
            libro_agregar = input("Ingrese el nombre del libro a agregar: ").strip().capitalize()
            libros.append(libro_agregar)
            copias.append(cant_a_ingresar)
        print("Libros agregados correctamente.")

    elif opcion == "2":
        if not libros:
            print("No hay libros en la biblioteca.")
            continue

        for i, libro in enumerate(libros):
            while True:
                entrada = input(f"Ingrese la cantidad de copias para '{libro}': ").strip()
                if entrada.isdigit():  # validar que sea número
                    copias[i] = int(entrada)
                    break
                else:
                    print("ERROR: Debe ingresar un número entero no negativo.")

    elif opcion == "3":
        if not libros:
            print("La biblioteca está vacía.")
            continue

        for i in range(len(libros)):
            print(f"{libros[i]} - Copias disponibles: {___}")

    elif opcion == "4":
        solicitud_libro = input("Ingrese el nombre del libro que quiere consultar: ").strip().capitalize()

        if solicitud_libro in ___:
            indice = libros.index(___)
            if copias[indice] > 0:
                print(f"Sí, '{solicitud_libro}' está disponible. Copias: {___}")
            else:
                print(f"'{solicitud_libro}' está en la biblioteca, pero no hay copias disponibles.")
        else:
            print(f"No, '{solicitud_libro}' no está en la biblioteca.")

    elif opcion == "5":
        print("Libros sin copias disponibles:")
        for i in range(len(libros)):
            if copias[i] == ___:
                print(f"- {libros[i]}")

    elif opcion == "6":
        nombre_libro = input("Ingrese el nombre del libro nuevo: ").strip().capitalize()
        cant_copias = input(f"Ingrese la cantidad de copias de '{nombre_libro}': ")

        if not ___:
            print("ERROR: Debe ingresar un número.")
            continue

        libros.append(___)
        copias.append(int(___))
        print(f"'{nombre_libro}' agregado correctamente.")

    elif opcion == "7":
        solicitud_libro = input("Ingrese el nombre del libro: ").strip().capitalize()

        if solicitud_libro in ___:
            indice = libros.index(solicitud_libro)
            print(f"Copias disponibles: {copias[indice]}")
            accion = input("Ingrese 'p' para prestar o 'd' para devolver: ").lower()

            if accion == "p":
                if copias[indice] > 0:
                    copias[indice] -= 1
                    print("Libro prestado con éxito.")
                else:
                    print("No hay copias disponibles para prestar.")
            elif accion == "d":
                copias[indice] += 1
                print("Libro devuelto con éxito.")
            else:
                print("Opción inválida.")
        else:
            print(f"'{solicitud_libro}' no está en la biblioteca.")

    elif opcion == "8":
        print("Libros con copias disponibles:")
        for i in range(len(libros)):
            if copias[i] > ___:
                print(f"- {libros[i]} ({copias[i]} disponibles)")

    elif opcion == "9":
        print("Hasta luego.")
        break

    else:
        print("Opción inválida, intente de nuevo.")

