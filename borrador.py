num_usuario = (input("ingrese un numero entero: "))

if num_usuario.isdigit():
    num_inverso = num_usuario[::-1]
    print(f"Su numero invertido es: {num_inverso}")
else:
    print("No ingreso un valor numerico. ")

