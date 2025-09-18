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








