
def SaturacionDerecha(Xmax, Xmin, X):
    Y = ((1 / (Xmax - Xmin)) * X) - ((Xmin)/(Xmax-Xmin))
    print(f"Y = ( 1/(Xmax) - Xmin) * X )- Xmin / (Xmax - Xmin)")
    print(f"Y = ( 1/({Xmax}) - {Xmin}) * {X} )- {Xmin} / ({Xmax} - {Xmin})")
    print(f"Y = {Y}")
    return Y
def SaturacionIzquierda(Xmax, Xmin, X):
    Y = ((-1 / (Xmax - Xmin)) * X) + ((Xmax)/(Xmax-Xmin))
    print(f"Y = ( -1/(Xmax) - Xmin) * X ) + Xmax / (Xmax - Xmin)")
    print(f"Y = ( -1/({Xmax}) - {Xmin}) * {X} ) + {Xmax} / ({Xmax} - {Xmin})")
    print(f"Y = {Y}")
    return Y
def SaturacionTriangulo(Xmax, Xmin, X):
    Media = (Xmax + Xmin)/2
    print("")
    print(f"Media = (Xmax + Xmin)/2")
    print(f"Media = ({Xmax} + {Xmin})/2")
    print(f"Media = {Media}")

    if X < Media:
        print("")
        print(f"El dato {X} está por detrás de la media ({Media})")
        Y = ((2/(Xmax - Xmin)) * X) - ((2 * Xmin) / (Xmax - Xmin))
        print(f"Y = (2/(Xmax - Xmin) * X) - (2 * (Xmin) / Xmax - Xmin)")
        print(f"Y = (2/({Xmax} - {Xmin}) * {X}) - (2 * ({Xmin}) / {Xmax} - {Xmin})")
        print(f"Y = (2/({Xmax - Xmin}) * {X}) - ({2 * Xmin}) / {Xmax - Xmin})")
        print(f"Y = {Y}")
        return Y
    elif X > Media:
        print()
        print(f"El dato {X} está por delante de la media ({Media})")
        Y = ((2 * Xmax) / (Xmax - Xmin)) - ((2 * X) / (Xmax - Xmin))
        print(f"Y = (2(Xmax) /(Xmax - Xmin)) - (2(X) / Xmax - Xmin)")
        print(f"Y = (2 * {Xmax}) /{Xmax - Xmin}) - ({2 * X}) / {Xmax - Xmin})")
        print(f"Y = {Y}")

print()
print("==========================================================")
while(True):
    Xmax = float(input("Ingrese su X máxima:  "))
    Xmin = float(input("Ingrese su X mínima:  "))
    X = float(input("Ingrese la X que le piden:  "))
    print("------------------------------------------------")
    print("Seleccione la función de pertenencia que debe aplicar.  ")
    print("1.- Saturación derecha")
    print("2.- Saturación izquierda")
    print("3.- Función de trinángulo")
    Respuesta = int(input("Respuesta:  "))

    if Respuesta == 1:
        print()
        SaturacionDerecha(Xmax, Xmin, X)
    elif Respuesta == 2:
        print()
        SaturacionIzquierda(Xmax, Xmin, X)
    elif Respuesta == 3:
        SaturacionTriangulo(Xmax, Xmin, X)
    
    print("¿Repetir?")
    print("1.- Sí")
    print("2.- No")
    Repetir = int(input("Respuesta:  "))
    if Repetir == 1:
        print("===============================================")
        print("\n\n")
    else:
        break