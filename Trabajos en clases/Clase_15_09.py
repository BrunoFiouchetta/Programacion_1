#validacion .isdigit()

"""
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles.
#Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas 
#(una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente
de copias utilizando el mismo índice en ambas listas Se debe utilizar un bucle while para navegar
por las opciones del menú hasta que el usuario elija salir.
"""




titulos = []
ejemplares = []
opcion = 0 



while opcion != 10:
    print("\n=== BIBLIOTECA ESCOLAR ===")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar título")
    print("5. Ver agotados")
    print("6. Agregar título")
    print("7. Ver agotados")
    print("8. Préstamo/Devolución")
    print("9. Ver todos los títulos")
    print("10. Salir")
    

    opcion = int(input("Opción: "))
    
    
    if opcion == 1:
    titulos[]
    ejemplares[]

    cantidad = int(input("Cuántos títulos va a ingresar? "))

    for i in range(cantidad):
        titulo = input(f"Título {i+1}: ")
        