print("=== EJERCICIO 1 ===")

def imprimir_hola_mundo():
    print("Hola Mundo!")


imprimir_hola_mundo()
print()


print("=== EJERCICIO 2 ===")

def saludar(nombre):
    return f"hola {nombre}!"

nombre_usuario = input("ingrese su nombre: ")

saludo = saludar(nombre_usuario)
print(saludo)


print("=== EJERCICIO 3 ===")

def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
años = input("ingrese su edad: ")
direccion = input("ingrese su direccion: ")

presentacion = informacion_personal(nombre, apellido, años, direccion)
print(presentacion)


print("=== EJERCICIO 4 ===")