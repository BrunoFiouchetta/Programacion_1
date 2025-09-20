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


"""
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
"""
animales = ["perro", "gato", "conejo", "pez"]

animales[2] = "loro"
animales[3] = "oso"

print(animales)


"""
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
"""
#el codigo presentado lo que hace es eliminar el valor maximo dentro de una lista, en el caso del ejemplo elimina el numero 22.


"""
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""
lista = list(range(10,31))
primeros2 = []

for i in lista:
    if i % 5 == 0:
        print(i)
        if i <= 15:
            primeros2.append(i)

print(primeros2[0:2])



