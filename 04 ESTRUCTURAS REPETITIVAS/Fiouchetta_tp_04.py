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


"""
4)	Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
"""
print("Este programa suma todos los numeros enteros que cargues en el:\n ")
corte=1
suma = 0

while corte != 0:
    num = int(input("ingrese un numero entero: "))
    suma = suma + num
    print(f"la suma es {suma}")


"""
5)	Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
num_usuario = 10

while num_usuario != numero_aleatorio:

    num_usuario = int(input("adivina el numero del 1 al 9: "))

    if num_usuario != numero_aleatorio:
        intentos = intentos +  1

print("ACERTASTE!")
print(f"tardaste {intentos+1} intentos en acertar: ")


"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
i = 0
suma = 0
num_usuario = int(input("ingrese un numero entero positivo: "))

while i != num_usuario:
    suma += i
    i+=1
    print(suma)


"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. 

Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

num_par = 0
num_impar = 0

num_posit = 0
num_neg = 0

for ingreso in range(1, 101):
    
    num_usuario = int(input("ingrese un numero entero: "))
    if num_usuario % 2 == 0 and num_usuario > 0:
        num_par += 1 
        num_posit += 1
    elif num_usuario % 2 != 0 and num_usuario > 0:
        num_impar += 1
        num_posit += 1
    else:
        num_neg += 1

print(f"ha ingresado {num_posit} numeros positivos.")
print(f"ha ingresado {num_neg} numeros negativos.")
print(f"ha ingresado {num_par} numeros pares.")
print(f"ha ingresado {num_impar} numeros impares.")


"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

import statistics
lista_nums = []

for ingreso in range(1,101):
    num_usuario = int(input("ingrese 1 numero entero: "))
    lista_nums.append(num_usuario)

media = statistics.mean(lista_nums)
print(f"la media de todos los numeros es {media}")


"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

num_usuario = (input("ingrese un numero entero: "))

if num_usuario.isdigit():
    num_inverso = num_usuario[::-1]
    print(f"Su numero invertido es: {num_inverso}")
else:
    print("No ingreso un valor numerico. ")