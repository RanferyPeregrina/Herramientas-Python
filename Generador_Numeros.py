Limite = int(input("Ingrese el número límite que quiere generar: "))

for i in range(Limite):
    with open("Numeros generados.txt", "a") as archivo:
        archivo.write(f"{i + 1} ")