import os

def LeerDirectorio():
    Directorio_Actual = os.getcwd()
    return Directorio_Actual

def SubirDirectorio(Veces):
    if Veces == "": Veces = 1
    Veces = int(Veces)

    for i in range(Veces):
        Directorio_Actual = os.chdir("..")
    return Directorio_Actual

def EntrarDirectorio(Directorio_Actual):
    print("- " * 20)
    print("¿A qué carpeta?")
    print("- " * 20)
    print()
    Archivos = os.listdir()
    for Archivo in Archivos:
        print(Archivo)
    print()
    Archivo_Elegido = input(" - - - - - - - RESPUESTA:  ")

    Directorio_Actual = os.chdir(os.path.join(Directorio_Actual, Archivo_Elegido))
    

while True:
    Directorio_Actual = LeerDirectorio()
    print("=" * 40)
    print(f"Hola. Actualmente estás en el directorio: {Directorio_Actual}")
    print("1.- Imprimir directorio actual")
    print("2.- Entrar a otro directorio")
    print("3.- Subir directorios")
    Respuesta = int(input("Operación:  "))
    print()

    if Respuesta == 1: print(os.getcwd())
    elif Respuesta == 2: EntrarDirectorio(Directorio_Actual)
    elif Respuesta == 3:
        Veces = input("¿Cuántas veces?:  ") 
        SubirDirectorio(Veces)