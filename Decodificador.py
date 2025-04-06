
def MenuIngreso():
    print("Código o palabra?")
    print("1.- Código")
    print("2.- Palabra")
    print("3.- Documento de texto")
    Respuesta = int(input("Respuesta:  "))

    if Respuesta == 1:
        Algo = Pedir_Codigo()
    if Respuesta == 2:
        Algo = Pedir_Palabra()
    if Respuesta == 3:
        Algo = Pedir_Archivo()
    return Algo


def MenuOperacion(Algo):
    print("\nIngrese la operación que hará con eso")
    print("1.- Traducor de ASCII a Texto")
    print("2.- Traducir de Texto a ASCII")
    Respuesta = int(input("Respuesta:  "))
    if Respuesta == 1: Convertir_Texto(Algo)
    elif Respuesta == 2: Convertir_ASCII(Algo)

def Pedir_Codigo():
    
    print()
    print("Para detenerse,  sólo escriba un espacio vacío.")
    Palabra_ASCII = []
    i = 1
    while True:
        Letra = input("Código de su caracter:  ")
        if Letra == " ": break
        Caracter = int(Letra)
        Palabra_ASCII.append(Caracter)
        if i > 30: 
            print("Su cadena lleva más de 30 caracteres.")
            print("Si quiere terminarlo, sólo escriba un espacio y presione Enter\n")
            i = 0
    print()
    print(f"El código recibido entonces fue: {Palabra_ASCII}")
    return Palabra_ASCII
        
def Pedir_Palabra():
    Palabra = input("Ingrese su palabra:  ")
    return Palabra

def Pedir_Archivo():
    Archivo = input("\nIngrese el nombre de su archivo:  ")
    Extension = Archivo[-4:]
    if Extension != ".txt":
        Archivo += ".txt"
        print(f"Nombre de archivo corregido como {Archivo}")
    print(f"Buscando {Archivo}")

    Archivo = open(Archivo)
    print(Archivo)

#Convierte de ASCII a Texto
def Convertir_Texto(Palabra_ASCII):
    Palabra = ""
    for Caracter in Palabra_ASCII:
        Letra = str(Caracter)
        Palabra += Letra
    print(f"La palabra leída es: {Palabra}")
    return Palabra
#Convierte de Texto a ASCII
def Convertir_ASCII(Palabra):
    Palabra_ASCII = []
    for Letra in Palabra:
        Letra_ASCII = ord(Letra)
        Palabra_ASCII.append(Letra_ASCII)
    print(Palabra_ASCII)
    return Palabra_ASCII

Algo = MenuIngreso()
Algo = MenuOperacion(Algo)