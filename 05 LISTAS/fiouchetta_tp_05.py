"""
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
"""
lista2 = []
lista = list(range(1,101))

for i in lista:
    if i % 4 == 0:
        lista2.append(i)

print("en una lista del 0 al 100; los multiplos de 4 son: ", lista2)


"""
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
"""
lista = [1, 2, 3, 4, 5]
lista_penultimo = lista[3]
print(lista_penultimo)


"""
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
"""
lista=[]
lista.append("perro")
lista.append("gato")
lista.append("pato")

print(lista)


