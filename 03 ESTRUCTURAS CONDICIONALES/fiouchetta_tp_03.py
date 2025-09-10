
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
'''
edad = int(input("ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
'''
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
'''
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
'''
'''
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
'''
'''
num1 = int(input("Ingrese un numero par: "))

if num1 % 2 == 0:
    print("ha ingresado un numero par")
else:
    print("por favor ingrese un numero par")
'''

'''
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''
'''
edad = int(input("ingrese su edad: "))

if edad < 12:
    print("Usted es un niño/a.")
elif edad >= 12 and edad < 18:
    print("usted es un alolecente.")
elif edad >= 18 and edad < 30:
    print("usted es un adulto.")
else:
    print("usted es un adulto mayor")
'''
"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""
'''
contra = input("ingrese una contrasena de entre 8 y 14 caracteres: ")

if len(contra) >= 8 and len(contra) <= 14:
    print("ingreso una contrasena correcta")
else:
    print("por favor ingrese una contrasena de entre 8 y 14 caracteres")
'''
#6) Media, mediana y moda de una lista de números aleatorios

'''
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean


media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"LISTA DE NUMEROS ALEATORIOS: {numeros_aleatorios}")
print()

print(f"la media es: {media} ")
print(f"la mediana es: {mediana} ")
print(f"la moda es {moda}: ")
'''

"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""
'''
Frase = input("ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if Frase[-1] in vocales:
    Frase += "!"
    print(Frase)
else:
    print(Frase)
'''

"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""

Nombre = input("ingrese su nombre: ")

opcion = int(input("INGRESE UNA OPCION:\n1) si quiere su nombre en mayusculas:\n2) si lo quiere en minusculas:\n3) si lo quiere con la primer letra mayuscula: "))

if opcion == 1:
    print(Nombre.upper())
elif opcion == 2:
    print(Nombre.lower())
elif opcion == 3:
    print(Nombre.title())
else:
    print("opcion incorrecta")
