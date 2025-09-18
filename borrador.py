num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
suma=0

if num1 < num2:
    for n in range(num1 + 1, num2):
        suma += n
elif num2 < num1:
    for n in range(num2+1, num1):
        suma += n
else:
    print("ambos numeros son iguales")

print("la suma de los numeros es:",suma)
