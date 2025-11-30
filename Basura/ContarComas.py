while True:
    contador = 0
    Texto = input('Ingrese su texto:  ')

    for caracter in Texto:
        if caracter == ",":
            contador += 1
    print(f"Los términos son: {contador + 1}")