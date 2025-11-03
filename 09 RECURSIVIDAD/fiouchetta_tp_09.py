# punto 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("=== ejercicio 1: factorial ===")
num = int(input("hasta que numero calcular factoriales? "))
print(f"\nfactoriales de 1 a {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")
print()

# punto 2
def fib(pos):
    if pos <= 1:
        return pos
    return fib(pos - 1) + fib(pos - 2)

print("=== ejercicio 2: fibonacci ===")
n = int(input("cuantos terminos mostrar? "))
print(f"\nserie fibonacci hasta posicion {n}:")
serie = [fib(i) for i in range(n)]
print(serie)
print()

# punto 3
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

print("=== ejercicio 3: potencia ===")
base = int(input("base: "))
exp = int(input("exponente: "))
print(f"\n{base}^{exp} = {potencia(base, exp)}")
print()

# punto 4
def a_binario(n):
    if n == 0:
        return ""
    return a_binario(n // 2) + str(n % 2)

print("=== ejercicio 4: decimal a binario ===")
num = int(input("numero decimal: "))
binario = "0" if num == 0 else a_binario(num)
print(f"\ndecimal: {num}")
print(f"binario: {binario}")
print()

# punto 5
def palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return palindromo(texto[1:-1])

print("=== ejercicio 5: palindromo ===")
palabra = input("ingresa una palabra: ").lower().replace(" ", "")
if palindromo(palabra):
    print(f"'{palabra}' es un palindromo")
else:
    print(f"'{palabra}' no es un palindromo")
print()

# punto 6
def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

print("=== ejercicio 6: suma de digitos ===")
num = int(input("ingresa un numero: "))
print(f"\nsuma de digitos de {num}: {suma_digitos(num)}")
print()

# punto 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print("=== ejercicio 7: bloques de piramide ===")
base = int(input("bloques en la base: "))
print(f"\ntotal de bloques: {contar_bloques(base)}")
print()

# punto 8 
def contar_digito(num, dig):
    if num == 0:
        return 0
    ultima_cifra = num % 10
    coincide = 1 if ultima_cifra == dig else 0
    return coincide + contar_digito(num // 10, dig)

print("=== ejercicio 8: contar digito ===")
num = int(input("numero: "))
dig = int(input("digito a buscar (0-9): "))
print(f"\nel digito {dig} aparece {contar_digito(num, dig)} veces en {num}")
print()

print("===============================")
print("programa completado")
print("===============================")