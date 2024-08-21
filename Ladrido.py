import random

def Generar_LongitudAleatoria(Longitud_Minimo, Logitud_Maximo):
    Numero_Logitud = random.randint(Longitud_Minimo, Logitud_Maximo)
    return Numero_Logitud

def Probabilidad_Aleatoria(Probabilidad_Deseada):
    Probabilidad_Ocurrida = random.random()
    Probabilidad_Deseada = Probabilidad_Deseada / 100

    if Probabilidad_Deseada > Probabilidad_Ocurrida:
        # print(f"Deseada: {Probabilidad_Deseada}")
        # print(f"Ocurrida: {Probabilidad_Ocurrida}")
        # print("Sucedió")
        return True
    elif Probabilidad_Deseada < Probabilidad_Ocurrida:
        # print(f"Deseada: {Probabilidad_Deseada}")
        # print(f"Ocurrida: {Probabilidad_Ocurrida}")
        # print("No Sucedió")
        return False

def Generar_Grr():
    GR = "G"
    if Probabilidad_Aleatoria(10): GR += ("G")
    GR += ("R" * Generar_LongitudAleatoria(2, 5))
    return(GR)

def Generar_Woof():
    WOF = "WO"
    WOF += ("O"*Generar_LongitudAleatoria(1, 4))
    WOF += ("F"*Generar_LongitudAleatoria(1,2))
    return WOF

def Generar_Meow():
    MEOW = "ME"
    if Probabilidad_Aleatoria(30): MEOW += ("E")
    MEOW += ("O" * Generar_LongitudAleatoria( 1, 2))
    MEOW += ("W")
    return MEOW

def Generar_Arf():
    ARF = "AR"
    if Probabilidad_Aleatoria(20): ARF += ("R" * Generar_LongitudAleatoria(1, 2))
    ARF += ("F" * Generar_LongitudAleatoria(1, 2))
    return ARF

def Generar_Bark():
    BARK = "BARK"
    if Probabilidad_Aleatoria(30): BARK += (" BARK")
    return BARK

def Generar_Waw():
    WAW =("WAW" * Generar_LongitudAleatoria(1, 2))
    return WAW

print("=" * 50)
print("Programa que te ladra acá bien acá")
Repeticiones = int(input("Numero de repeticiones:  "))
print("=" * 50)
print()

Ladrido = ""
for _ in range(random.randint(1, 7)):
        Ladrido += Generar_Grr() + " "
for i in range(Repeticiones):
    if Probabilidad_Aleatoria(70): Ladrido += " " + Generar_Grr()
    if Probabilidad_Aleatoria(60): Ladrido += " " + Generar_Woof()
    if Probabilidad_Aleatoria(20): Ladrido += " " + Generar_Arf()
    if Probabilidad_Aleatoria(10): Ladrido += " " + Generar_Meow()
    if Probabilidad_Aleatoria(35): Ladrido += " " + Generar_Bark()
    if Probabilidad_Aleatoria(5): Ladrido += " " + Generar_Waw()
print(Ladrido)
print("\n\n")
input()