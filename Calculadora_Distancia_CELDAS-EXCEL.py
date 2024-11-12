#Programa que calcula la distancia entre dos celdas en Excel.
print("Para salir escribe: SALIR")

while True:
    Numero1 = input("Ingrese el primer número de celda:  ")
    if Numero1.upper() == "SALIR":
        print("SALIDA DETECTADA")
        break
    Numero2 = input("Ingrese el segundo número de celda:  ")
    if Numero2.upper() == "SALIR":
        print("SALIDA DETECTADA")
        break

    Numero1 = int(Numero1)
    Numero2 = int(Numero2)

    if type(Numero1) != int: 
        print(f"Primer entrada no válida con valor: {Numero1} y tipo: {type(Numero2)}")
        Numero1 = 0
    if type(Numero2) != int: 
        print(f"Segunda entrada no válida con valor: {Numero2} y tipo: {type(Numero2)}")
        Numero2 = 0

    Distancia = Numero2 - Numero1
    if Distancia < 0:
        Distancia = Distancia * (-1)
    Distancia += 1
    print(f"La distancia es: {Distancia}")
    print("\n\n\n")

