
num_usuario = int(input("ingrese un numero entero entre 1 y 10: "))

if num_usuario >= 1 and num_usuario <= 10:
    for cont in range(1,11):
        result = num_usuario * cont
        print(num_usuario,"x",cont,"=",result)
else:
    print("no ingreso un numero entre 1 y 10.")