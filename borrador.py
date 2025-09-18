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