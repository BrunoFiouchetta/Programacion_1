#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


"""
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
"""
print("SALUDO_NOMBRE:")
print("hola, como te llamas?")
nombre_x = input("Ingresa tu nombre: ")
print(f"hola {nombre_x}")

"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""
print("PRESENTACION_PERSONAL:")
nombre_2 = input("ingresa tu nombre: ")
apellido_2 = input("ingresa tu apellido: ")
edad_2 = input("ingresa tu edad: ")
lugar_resi = input("ingresa tu lugar de residencia: ")
print(f"soy {nombre_2} {apellido_2}, tengo {edad_2} años y vivo en {lugar_resi}.")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("CALCULO_AREA_PERIMETRO:")
print("ingrese un radio de un circulo")
radio = float(input("radio: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"el area es {area} y el perimetro es {perimetro}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
print("CONVERSION_SEGUNDOS_HORAS:")
print("ingrese una cantidad de segundos")
segundos = int(input("segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("TABLA_MULTIPLICAR:")
print("ingrese un numero")
numero = int(input("numero: "))

print(f"tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("CALCULADORA_BASICA:")
print("ingrese dos numeros enteros distintos del 0")
numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))

suma = numero1 + numero2
rest = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2

print(f"la suma es {suma}")
print(f"la resta es {rest}")
print(f"la multiplicacion es {mult}")
print(f"la division es {div}")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2
print("CALCULO_IMC:")
print("ingrese su altura en metros")
altura = float(input("altura: "))

print("ingrese su peso en kg")
peso = float(input("peso: "))
imc = peso / (altura ** 2)
print(f"su indice de masa corporal es {imc}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
print("CONVERSION_TEMPERATURA:")
print("ingrese una temperatura en grados Celsius")
grados_celsius = float(input("grados Celsius: "))
grados_fahrenheit = (9/5) * grados_celsius + 32
print(f"la temperatura en grados Fahrenheit es {grados_fahrenheit}")


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("CALCULO_PROMEDIO:")
print("ingrese 3 numeros")
numero1 = float(input("primer numero: "))
numero2 = float(input("segundo numero: "))
numero3 = float(input("tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"el promedio de los numeros es {promedio}")



