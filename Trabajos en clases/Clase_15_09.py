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
opcion = 0 



while opcion != 10:
    print("\n=== BIBLIOTECA ESCOLAR ===")
    print("1. Ingresar titulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar título")
    print("5. Ver agotados")
    print("6. Agregar titulo")
    print("7. Ver agotados")
    print("8. Préstamo/Devolucion")
    print("9. Ver todos los títulos")
    print("10. Salir")
    
    
    opcion = int(input("Opcion: "))
    
    
    if opcion == 1:
        cantidad = int(input("cuantos titulos va a ingresar? "))
        for i in range(cantidad):
            titulo = input(f"ingrese el título {i + 1}: ")
            titulos += [titulo]
            ejemplares.append(0)  

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

