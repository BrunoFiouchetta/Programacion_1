

lista = list(range(10,31))
primeros2 = []

for i in lista:
    if i % 5 == 0:
        print(i)
        if i <= 15:
            primeros2.append(i)

print(primeros2[0:2])
