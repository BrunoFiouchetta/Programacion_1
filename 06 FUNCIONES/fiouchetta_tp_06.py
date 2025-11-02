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

def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")
print()


print("=== EJERCICIO 5 ===")

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas} horas")
print()


print("=== EJERCICIO 6 ===")

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)
print()


print("=== EJERCICIO 7 ===")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
print()


print("=== EJERCICIO 8 ===")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal es: {imc:.2f}")
print()


print("=== EJERCICIO 9 ===")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit}°F")
print()


print("=== EJERCICIO 10 ===")

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio}")
print()

