"""
Desarrollar un algoritmo que permita ingresar una cantidad de personas. La computadora debe
pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad.
"""

cant_pers = int(input("ingrese una cantidad de personas: "))
mayor_edad = 0

for i in range(1,cant_pers+1):
    edad = int(input(f"ingresela edad de la persona N{i}: "))
    if edad >= 18:
        mayor_edad += 1

porcent = (mayor_edad / cant_pers)*100
print("el porcentaje de personas mayores es:","%",porcent)
