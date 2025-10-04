from os import read
from posixpath import split
import random

def Puntos_Suspensivos(Palabra):
    Probabilidad_Corregida = random.randint(1, 6)
    if Probabilidad_Corregida == 1:
        Palabra += "..."
    elif Probabilidad_Corregida == 2:
        Palabra += "💗"
    elif Probabilidad_Corregida == 3 or Probabilidad_Corregida == 4:
        Palabra = Guion(Palabra)
    else: Palabra = Gestito(Palabra)
    return Palabra
def Repetir_Inicial(Palabra):
    Palabra = Palabra[0] + "-"+Palabra
    return Palabra
def Gestito(Palabra):
    if (random.randint(1, 3)) == 1:
        #Elige hacerlo al principio.
        Palabra = Palabra + "~"
    else:
        #Elige hacerlo al final
        Palabra = "~" + Palabra
    return Palabra
def Guion(Palabra):
    Palabra += "-"
    return Palabra
def RepetirVocal(Palabra):
    if len(Palabra) >= 4:
        Vocales = ["a", "e", "o", "u"] 
        #Que se vaya a la verga la "i", queda fea
        VocalEncontrada = False
        Palabra2 = ""
        for Letra in reversed(Palabra):
            Palabra2 += Letra
            if VocalEncontrada != False:
                if Letra in Vocales:
                    Palabra2 += Letra
                    VocalEncontrada = True
        Palabra = "".join(reversed(Palabra2))
    else:
        Palabra = Gestito(Palabra)
    return Palabra          

Palabra_Original = input("Entrada:  ")
# Archivo = open("Pessoa.txt", "r", encoding="utf-8")
# Palabra_Original = Archivo.read()
print(Palabra_Original)
input()
Palabras_Separadas = Palabra_Original.split()

while True:
    Palabra_Nueva = ""
    for Palabra in Palabras_Separadas:
        Funcion = random.randint(1, 6)
        if Funcion == 1:
            Palabra= Puntos_Suspensivos(Palabra)
        elif Funcion == 2:
            Palabra = Repetir_Inicial(Palabra)
        elif Funcion == 3:
            Palabra = Gestito(Palabra)
        elif Funcion == 4:
            Palabra = Guion(Palabra)
        elif Funcion == 5:
            Palabra = RepetirVocal(Palabra)
        elif Funcion == 6:
            Palabra += "!"

        Palabra_Nueva += " " + Palabra
    
    Detenerse = input(Palabra_Nueva)
    if Detenerse == " ": break