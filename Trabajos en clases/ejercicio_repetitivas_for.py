def encriptar_cesar(mensaje, corrimiento):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ""

    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice = alfabeto.index(caracter.lower())
            nuevo_indice = (indice + corrimiento)%27
            if caracter.isupper():
                resultado += alfabeto[nuevo_indice].upper()
            else:
                resultado += alfabeto[nuevo_indice]
        else:
            resultado += caracter
    return resultado

corrimiento = int(input("ingrese el corrimiento (numero de lugares): "))


for i in range(5):
    mensaje = input(f"ingrese el mensaje {i+1}: ")
    mensaje_encriptado = encriptar_cesar(mensaje, corrimiento)
    print(f"el mensaje encriptado es: {mensaje_encriptado}")

print("FIN")