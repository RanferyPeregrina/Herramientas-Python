import random
import time
import matplotlib as mapa

CoordenadaX = 0
CoordenadaY = 0
Intentos = 0
MensajeTiempo = False


def Mover(Direccion, CoordenadaX, CoordenadaY):
    if Direccion == "Arriba":
        CoordenadaY += 1
    elif Direccion == "Abajo":
        CoordenadaY -= 1
    elif Direccion == "Derecha":
        CoordenadaX += 1
    elif Direccion == "Izquierda":
        CoordenadaX -= 1

    return CoordenadaX, CoordenadaY

while True:
    Direccion = random.choice(["Arriba", "Abajo", "Izquierda", "Derecha"])

    CoordenadaX, CoordenadaY = Mover(Direccion, CoordenadaX, CoordenadaY)
    Intentos += 1

    if Intentos >= 1000000:
        if MensajeTiempo == False:
            MensajeTiempo = True
            print("Oh, estoy va a tardar mucho.")
            time.sleep(1)
            print("- - - - - - - -Imprimiendo coordenadas - - - - - - -")
            time.sleep(3)
            print()

        print(f"({CoordenadaX} , {CoordenadaY})")

    if CoordenadaX == 0 and CoordenadaY == 0:
        print(f"Tras {Intentos} intentos, se regresó al origen")
        break


