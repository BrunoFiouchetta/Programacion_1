"""
1)	Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
for i in range(101):
    print(i)


"""
2)	Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
"""
numero = int(input("ingrese un numero entero: "))
contador = 0

if numero == 0:
    contador = 1
else:
    while numero != 0:
        numero = numero//10
        contador += 1
print("la cantidad de digitos es:", contador)


"""
3)	Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
"""
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




