import random

def Generar_LongitudAleatoria(Longitud_Minimo, Logitud_Maximo):
    Numero_Logitud = random.randint(Longitud_Minimo, Logitud_Maximo)
    return Numero_Logitud

def Generar_Grr():
    GR = "G"
    GR = GR + ("R"*Longitud_Aleatoria)
    return(GR)

Longitud_Minimo = 3
Longitud_Maximo = 9
Longitud_Aleatoria = Generar_LongitudAleatoria(Longitud_Minimo, Longitud_Maximo)