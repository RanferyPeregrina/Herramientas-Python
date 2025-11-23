Indices = {}

for Numero in range(100000):
    print("-" * 20)
    Suma = 0
    Digito_Letra = f'{Numero:06d}'
    for Digito in Digito_Letra:
        Suma += int(Digito)
        
        if Suma in Indices:
            Indices[Suma] += 1
        else:
            Indices[Suma] = 1


    print(f"La suma de {Digito_Letra} es: {Suma}")


    print("Lista de índices:")
for suma, conteo in sorted(Indices.items()):
    print(f"Suma {suma}: {conteo} repeticiones")