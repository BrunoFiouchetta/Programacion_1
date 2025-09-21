# Biblioteca inicial
libros = ["1984", "El Principito", "Don Quijote"]
copias = [3, 0, 5]

while True:
    # Menú
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
    
    match opcion:
        case "1":
            # Completar: pedir cantidad de libros a agregar
            # Recorrer con un for y agregar cada libro a la lista libros
            # Agregar 0 copias por defecto en la lista copias
            cant_a_ingresar = int(input("cantidad de libros a ingresar: "))
            for i in range(cant_a_ingresar):
                libro_agregar = input("ingrese el nombre de libro a agregar: ")
                libros.append(libro_agregar)
                copias.append(0)
                print(libros, copias)
            pass
        
        case "2":
            # Completar: recorrer libros existentes y pedir cantidad de copias
            # Validar que el ingreso sea un número
            for i in range(len(libros)):
                copias_a_ingresar = int(input(f"ingrese la cantidad de copias para {libros[i]}: "))
                copias[i] = copias_a_ingresar
            pass
        
        case "3":
            # Mostrar todos los libros con sus copias
            for i in range(len(libros)):
                print(f"{libros[i]} - Copias disponibles: {copias[i]}")
        
        case "4":
            # Completar: pedir el nombre de un libro
            # Verificar si existe y mostrar la cantidad de copias
            pass
        
        case "5":
            # Completar: mostrar libros que tienen 0 copias
            pass
        
        case "6":
            # Completar: agregar un libro nuevo y cantidad de copias
            pass
        
        case "7":
            # Completar: pedir libro, verificar existencia
            # Preguntar si quiere prestar o devolver
            # Modificar la lista copias según corresponda
            pass
        
        case "8":
            # Completar: mostrar libros con al menos una copia disponible
            pass
        
        case "9":
            print("¡Hasta luego!")
            break
        
        case _:
            print("Opción inválida, ingrese un número del 1 al 9")
