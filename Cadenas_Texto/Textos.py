print("=" * 40)

def Menu_Texto():
    print("1.- Ingresar texto")
    print("2.- Leer archivo de texto")
    Respuesta_Texto = int(input("Respuesta:  "))

    if Respuesta_Texto == 1:
        Texto = input("Ingrese su texto escribiéndolo:  ")
    elif Respuesta_Texto == 2:
        Texto = Leer_Archivo()

    return Texto

def Menu_Operaciones():
    print("1.- Codificarlo")
    print("2.- Decodificarlo")
    print("3.- Modificarlo")
    print("4.- Buscar -ENTRADAS-")
    print("9.- Leer últimas letras")

    Operacion = int(input("Selección:  "))

    if Operacion == 4:
        Buscar_Entradas(Texto)
    if Operacion == 9:
        Numero_Letras = int(input("Cuántas letras quiere leer:  "))
        LeerCantidadLetras(Texto, Numero_Letras)


def Leer_Archivo():
    NombreArchivo = input("\nIngrese el nombre de su texto:  ")
    if NombreArchivo[-4:] != ".txt": NombreArchivo += ".txt"
    print(f"Buscando {NombreArchivo}")

    with open(NombreArchivo, "r", encoding= "utf-8") as Archivo:
        Contenido = Archivo.read()
        print("Contenido encontrado ==================================\n")
        print(Contenido)
        print("=======================================================")

    return Contenido

def LeerLongitud(Texto):
    Longitud = len(Texto)
    print(f"La palabra {Texto} tiene {Longitud} caracteres.")
    return Longitud

def LeerCantidadLetras(Texto, Caracteres):
    Texto_Extraido = ""
    Letra_Recorrida = 0
    Texto_Invertido = Texto[::-1]
    print(f"El texto invertido es: {Texto_Invertido}")
    for Letra in Texto_Invertido:
        Texto_Extraido += Letra
        Letra_Recorrida += 1
        if Letra_Recorrida == Caracteres: break
    Texto_Completo = Texto_Extraido[::-1]
    print(f"La palabra extraída fue: {Texto_Completo}")


def Buscar_Entradas(Texto):
    UltimaEntrada = 0

    while True:
        Inicio = Texto.find("&&&&&&&")
        if Inicio == -1: break

        Fin = Texto.find("&%&%&%&", Inicio) + len("&%&%&%&")
        Elemento = Texto[Inicio:Fin]
        print("\Elemento encontrado:  \n")
        print(Elemento)
        Inicio = Fin

Texto = Menu_Texto()
Menu_Operaciones()
