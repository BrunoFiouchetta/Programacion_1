"""

Calculadora de propinas en un restaurante 
Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el 
monto de la cuenta. 
El programa debe: 
✓ Pedir al usuario el monto total de la cuenta. 
✓ Calcular la propina sugerida al 10%. 
✓ Calcular la propina sugerida al 15%. 
✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
✓ Mostrar todos los resultados en pantalla. 
Ejemplo de ejecución 
Ingrese el monto de la cuenta: 3500 
Propina sugerida (10%): 350.0 
Total a pagar (10%): 3850.0 
Propina sugerida (15%): 525.0 
Total a pagar (15%): 4025.0

"""

print("Calculadora de propinas")

monto_total = float(input("Ingrese el monto de la cuenta: "))

propina_10 = monto_total * 10 / 100
propina_15 = monto_total * 15 / 100

total_10 = monto_total + propina_10
total_15 = monto_total + propina_15

print(f"propina sugerida (10%): {propina_10}")
print(f"total a pagar (10%): {total_10}")

print(f"propina sugerida (15%): {propina_15}")
print(f"total a pagar (15%): {total_15}")


