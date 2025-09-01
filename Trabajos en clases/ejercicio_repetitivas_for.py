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