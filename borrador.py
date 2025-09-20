lista2 = []
lista = list(range(1,101))

for i in lista:
    if i % 4 == 0:
        lista2.append(i)

print("en una lista del 0 al 100; los multiplos de 4 son: ", lista2)

