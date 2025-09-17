
#hacer un programa que solicite un numero positivo y muestre todos los numeros pares desde el numero ingresado hasta el 0.

numero = int(input("ingrese un numero positivo:"))

if numero > 0:
    if numero % 2 != 0:
        numero = numero - 1
    cont = numero
    while cont >= 0:
        print(str(cont) + " ", end="")
        cont = cont - 2
else:
    print("el numero no es positivo")