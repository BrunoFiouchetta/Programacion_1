"""
1. Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse. 
2. Mostrá el cartón al jugador en forma de matriz. 
3. El programa debe sortear números al azar entre 1 y 50, uno por uno. 
4. Cada vez que salga un número: 
o Si está en el cartón, reemplazarlo por un 0. 
o Si no está, avisar que no aparece. 
o Mostrar el cartón actualizado después de cada sorteo. 
5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!). 
Desafío extra: Validar cuando haya una línea completa (una fila llena de ceros) y mostrar el 
mensaje "¡Línea!". 

Sugerencias para resolverlo:
• Usar random.sample(range(1,51), 25) para obtener 25 números únicos y luego 
acomodarlos en la matriz. 
• Representar el cartón como una lista anidada de 5x5. 
• Recorrer la matriz con bucles anidados para marcar los números. 
• Usar un while que termine cuando todos los valores de la matriz sean 0.
"""
import random

numeros_unicos = random.sample(range(1, 51), 25)
matriz = []

print("Su cartón es:")
for i in range(0, 25, 5):
    fila = numeros_unicos[i:i+5]
    matriz.append(fila)
    print(" ".join(f"{num:2}" for num in fila))


while True:
    numero_sorteo = random.randint(1, 50)
    print(f"\nSe sortea el número {numero_sorteo}")

    encontrado = False
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == numero_sorteo:
                matriz[i][j] = 0
                encontrado = True

    if encontrado:
        print("¡Felicidades! El número está en su cartón")
    else:
        print("Lo siento, el número no está en su cartón")

    print("Cartón actualizado:")
    for fila in matriz:
        print(" ".join(f"{num:2}" for num in fila))


    bingo = all(num == 0 for fila in matriz for num in fila)
    if bingo:
        print("\n¡BINGO! Todos los números han sido sorteados.")
        break


    opcion = input("\n¿Desea continuar? (1: Sí / 2: No): ")
    if opcion != "1":
        print("Gracias por jugar. Hasta luego.")
        break
