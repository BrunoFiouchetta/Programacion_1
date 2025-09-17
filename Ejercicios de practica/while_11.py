CORTE = "*"
NOMBRE_INVALIDO = "XXXXXXXXXXXXXXX"
edad_minima = float("inf")
nombre_mas_joven = NOMBRE_INVALIDO

nombre = input("Ingrese un nombre (" + CORTE + " para cortar): ")
while nombre != CORTE:
    edad = int(input("Ingrese la edad de " + nombre + ": "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_mas_joven = nombre
    nombre = input("Ingrese otro nombre (" + CORTE + " para cortar): ")

if nombre_mas_joven == NOMBRE_INVALIDO:
    print("No se ingresaron personas")
else:
    print("La persona más joven (",edad_minima,"años) es",nombre_mas_joven)