print(" ======== PUNTO 1 ======== ")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


print(" ======== PUNTO 2 ======== ")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

print(precios_frutas)


print(" ======== PUNTO 3 ======== ")

frutas = precios_frutas.keys()

print(frutas)


print(" ======== PUNTO 4 ======== ")

telefonos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    telefonos[nombre] = numero

consulta = input("Ingrese el nombre del contacto a consultar: ")

if consulta in telefonos:
    print(f"El número de {consulta} es {telefonos[consulta]}")
else:
    print("Ese contacto no existe.")


print(" ======== PUNTO 5 ======== ")

frase = input("Ingrese una frase: ").lower().split()

palabras_unicas = set(frase)
print("Palabras únicas:", palabras_unicas)

frecuencias = {}
for palabra in frase:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencias)


print(" ======== PUNTO 6 ======== ")

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")


print(" ======== PUNTO 7 ======== ")

parcial1 = {"jose", "martin", "aldo", "miguel"}
parcial2 = {"martin", "jeronimo", "octavio", "jose"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)


print(" ======== PUNTO 8 ======== ")

productos = {
    "arroz": 10,
    "fideos": 8,
    "aceite": 5
}

producto = input("Ingrese el nombre del producto: ").lower()

if producto in productos:
    print(f"El stock actual de {producto} es: {productos[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar?: "))
    productos[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese el stock inicial: "))
    productos[producto] = nuevo_stock

print("Stock actualizado:", productos)


print(" ======== PUNTO 9 ======== ")

agenda = {}

for i in range(3):
    dia = input("Ingrese el día: ")
    hora = input("Ingrese la hora: ")
    evento = input("Ingrese el evento: ")
    agenda[(dia, hora)] = evento

consulta_dia = input("Ingrese el día a consultar: ")
consulta_hora = input("Ingrese la hora a consultar: ")

evento = agenda.get((consulta_dia, consulta_hora))
if evento:
    print(f"En {consulta_dia} a las {consulta_hora} hay: {evento}")
else:
    print("No hay eventos en ese horario.")


print(" ======== PUNTO 10 ======== ")

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}
print("Diccionario original (país → capital):")
print(paises)

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido (capital → país):")
print(capitales)

