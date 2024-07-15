import random

Palabra = "Nigger"
Limite = 500000
Palabra_Longitud_MIN = 4

for i in range(Limite):
    Palabra_Longitud_MAX = len(Palabra)
    Cantidad_Aleatoria = random.randint(Palabra_Longitud_MIN, Palabra_Longitud_MAX)
    Palabra_Recortada = Palabra[:Cantidad_Aleatoria]
    print(Palabra_Recortada, end="")
    if Cantidad_Aleatoria == 6:
        print(Palabra_Recortada)