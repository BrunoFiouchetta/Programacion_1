# Inicialización de listas
especialidades = []
cupos = []

salir = False

while not salir:
    print("\nMenú:")
    print("1. Ingresar especialidades")
    print("2. Ingresar cupos por especialidad")
    print("3. Mostrar agenda")
    print("4. Consultar cupos disponibles") 
    print("5. Listar especialidades sin cupos")
    print("6. Agregar especialidad")
    print("7. Actualizar cupos (reservar/cancelar)")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    # Opción 1: Ingresar especialidades
    if opcion == "1":
        while True: 
            especialidad = input("Ingrese la especialidad: ").strip()
            if especialidad == "" or not all(c.isalpha() or c.isspace() for c in especialidad):
                print("La especialidad no puede estar vacía y debe contener solo letras.")
            elif especialidad.lower() in [e.lower() for e in especialidades]:
                print("Esa especialidad ya existe en la agenda.")
            else:
                especialidades.append(especialidad.title())
                cupos.append(0)
                print(f"Especialidad {especialidad.title()} agregada con éxito.")
                break

    # Opción 2: Ingresar cupos
    elif opcion == "2":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            for i, esp in enumerate(especialidades):
                while True:
                    cupo = input(f"Ingrese la cantidad de cupos para {esp}: ").strip()
                    if cupo == "" or not cupo.isdigit():
                        print("El cupo no puede estar vacío y debe contener solo números.")
                    else:
                        cupos[i] = int(cupo)
                        break

    # Opción 3: Mostrar agenda
    elif opcion == "3":
        if not especialidades: 
            print("No hay especialidades, agrega alguna para continuar.")
        else: 
            print("Agenda de especialidades y cupos:")
            for i, esp in enumerate(especialidades):
                print(f"{esp}: {cupos[i]} cupos")

    # Opción 4: Consultar cupos de una especialidad
    elif opcion == "4":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            consulta = input("Ingrese la especialidad a consultar: ").strip()
            coincidencias = [e for e in especialidades if e.lower() == consulta.lower()]
            if coincidencias:
                indice = especialidades.index(coincidencias[0])
                print(f"La especialidad {especialidades[indice]} tiene {cupos[indice]} cupos")
            else:
                print("No existe la especialidad")

    # Opción 5: Listar especialidades sin cupos
    elif opcion == "5":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            print("Especialidades sin cupos disponibles:")
            for i, esp in enumerate(especialidades):
                if cupos[i] == 0:
                    print(f"{esp}")

    # Opción 6: Agregar nueva especialidad
    elif opcion == "6":
        nueva_esp = input("Agregue una especialidad: ").strip()
        if nueva_esp.lower() in [e.lower() for e in especialidades]:
            print("Esa especialidad ya está cargada en el sistema.")
        elif nueva_esp == "" or not all(c.isalpha() or c.isspace() for c in nueva_esp):
            print("La nueva especialidad no puede estar vacía y debe contener solo letras.")
        else:
            especialidades.append(nueva_esp.title())
            cupos.append(0)
            print(f"Especialidad {nueva_esp.title()} agregada con éxito.")
            print("Lista actualizada:", especialidades)

    elif opcion == "7":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            
            print("Seleccione una opción:")
            print("1. Reservar cupo")
            print("2. Cancelar cupo")
            sub_opcion = input("Ingrese su opción: ").strip()
            if sub_opcion == "1":
                especialidad = input("Ingrese la especialidad para reservar: ").strip()
                if especialidad in especialidades:
                    indice = especialidades.index(especialidad)
                    if cupos[indice] > 0:
                        cupos[indice] -= 1
                        print(f"Cupo reservado para {especialidad}.")
                    else:
                        print(f"No hay cupos disponibles para {especialidad}.")
                else:
                    print("Especialidad no encontrada.")
            elif sub_opcion == "2":
                especialidad = input("Ingrese la especialidad para cancelar: ").strip()
                if especialidad in especialidades:
                    indice = especialidades.index(especialidad)
                    cupos[indice] += 1
                    print(f"Cupo cancelado para {especialidad}.")
                else:
                    print("Especialidad no encontrada.")

    # Opción 8: Salir
    elif opcion == "8":
        print("Saliendo del sistema...")
        salir = True

    else:
        print("Opción inválida, intente nuevamente.")
