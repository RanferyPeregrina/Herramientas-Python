import os
def Leer_Directorio():
    Directorio_Actual = os.getcwd()
    return Directorio_Actual

def Entrar_Directorio(Carpeta):
    Directorio_Actual = Leer_Directorio()
    Directorio_Actual = Directorio_Actual + "\\" + Carpeta #Hay que usar Join en lugar de concatenar
    #Hay que usar chdir para mover el directorio
    return Directorio_Actual


def Subir_Directorio(Veces = 1):
    Veces = int(Veces)
    Directorio_Actual = Leer_Directorio()
    for i in range(Veces):
        os.chdir("..")
    return Directorio_Actual

def Enlistar_Directorio():
    Directorio_Actual = Leer_Directorio()
    Contenido = os.listdir()
    print("-"*20)
    for Archivo in Contenido:
        print(Archivo)
    print("-"*20)

while True:
    Directorio_Actual = Leer_Directorio()
    print(f"Estamos en: {Directorio_Actual}")

    print("-"*10)
    print("1.- Entrar carpeta.")
    print("2.- Subir directorio")
    print("3.- Enlistar documentos.")
    Operacion = int(input("Respuesta:  "))

    if Operacion == 1:
        Carpeta = input("¿A qué carpeta/archivo?:  ")
        Directorio_Actual = Entrar_Directorio(Carpeta)
    elif Operacion == 2:
        Veces = int(input("¿Cuántas veces?:  "))
        Subir_Directorio(Veces)
        print()
    elif Operacion == 3:
        Enlistar_Directorio()
