def MenuIngreso():
    print("Código o palabra?")
    print("1.- Código")
    print("2.- Palabra")
    print("3.- Documento de texto")
    try: Respuesta = int(input("Respuesta:  "))
    except:
        print("Error, respuesta no válida.")
        print("Seleccione un número.\n")
        MenuIngreso()

    if Respuesta == 1:
        Algo = Pedir_Codigo()
    elif Respuesta == 2:
        Algo = Pedir_Palabra()
    elif Respuesta == 3:
        Algo = Pedir_Archivo()
    else:
        print("Error, respuesta no válida.")
        print("Seleccione un número válido.\n")
        MenuIngreso()
    return Algo

def MenuOperacion(Algo):
    print("\nIngrese la operación que hará con eso")
    print("1.- Traducor de ASCII a Texto")
    print("2.- Traducir de Texto a ASCII")
    print("3.- Codificar texto.")
    print("4.- Mostrar contenido.")
    Respuesta = int(input("Respuesta:  "))
    if Respuesta == 1: Algo = Traducir_ASCII(Algo)
    elif Respuesta == 2: Algo = Traducir_Texto(Algo)
    elif Respuesta == 3: Algo = Codificar(Algo)
    elif Respuesta == 4: Algo = Mostrar(Algo)

    else:
        print("Respuesta no válida.")
        print("Ingrese de nuevo.\n")
        MenuOperacion(Algo)
    
    return Algo


def Pedir_Codigo():
    
    print()
    print("Para detenerse,  sólo escriba un espacio vacío.")
    Palabra_ASCII = []
    i = 1
    try: 
        while True:
            #Validación 1: Comprobar si seguir
            Letra = input(f"Código de su caracter [{i}]:  ")
            if Letra == " ": break

            Caracter = int(Letra)

            #Validación 3: Comprobar si está dentro de los ASCII
            if Caracter > 255 or Caracter <0:
                print("Caracter no válido. Excede los ASCII")
                print("Vuelva a intentarlo TODO.\n")
                Pedir_Codigo()

            #Validación 4: Comprobar si ya llevas muchas letras... Por si a caso.
            if i > 30: 
                print("Su cadena lleva más de 30 caracteres.")
                print("Si quiere terminarlo, sólo escriba un espacio y presione Enter\n")
                i = 0

            #Añadirlo a la lista como número.
            Palabra_ASCII.append(Caracter)
            i+= 1

        print()
        print(f"El código recibido entonces fue: {Palabra_ASCII}")
        return Palabra_ASCII
    except:
        print("Oh, algo salió mal.")
        print("¿Estás seguro que lo que estás ingresando es un código de ASCII?")
        print("Regresando al menú inicial...")
        print()
        MenuIngreso()
        
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

    try:
        with open(Archivo, "r", encoding = "utf-8") as Archivo:
            TextoLeido = Archivo.read()

            print("\n¿Imprimir contenido leído?")
            print("1.- Sí")
            print("2.- No")
            Impresion = int(input("Respuesta:  "))
            print("===================================")
            print()

            if Impresion == 1:
                print(TextoLeido)
                print("\n====================================")

        return TextoLeido
    except FileNotFoundError:
        print("El archivo no existe.")
        print()
        MenuIngreso()


#Convierte de ASCII a Texto
def Traducir_ASCII(Palabra_ASCII):

    if type(Palabra_ASCII) == list:
        Palabra = ""
        for Caracter in Palabra_ASCII:
            Letra = chr(Caracter)
            Palabra += Letra
        print(f"\nLa palabra leída es: {Palabra}\n")
    else:
        print("Lo que ingresaste no es una lista.")
        print("Vuelve a intentar todo.")
        Palabra = Palabra_ASCII
        MenuOperacion(Palabra_ASCII)
    return Palabra
#Convierte de Texto a ASCII
def Traducir_Texto(Palabra):
    Palabra_ASCII = []
    for Letra in Palabra:
        Letra_ASCII = ord(Letra)
        Palabra_ASCII.append(Letra_ASCII)

    print("\nCadena convertida a ASCII con éxico.")
    print("¿Imprimir?")
    print("1.- Sí")
    print("2.- No")
    Respuesta = int(input("Respuesta:  "))
    if Respuesta == 1: print(Palabra_ASCII)
    return Palabra_ASCII


def Codificar(Texto):
    Texto_Nuevo = []
    Vector = input("Ingrese contraseña de codificación:  ")
    Vector = Traducir_Texto(Vector)
    print(f"Vector traducido como: {Vector}")

    if type(Texto) == str:
        print("El texto ingresado es texto.")
        print("Convirtiendo a ASCII...")
        Texto = Traducir_Texto(Texto)

    for Caracter in Texto:
        NuevoCaracter = Caracter + 1
        Texto_Nuevo.append(NuevoCaracter)

    print("\nNuevo texto:")
    print(Texto_Nuevo)
    return Texto_Nuevo

def Mostrar(Algo):
    print("\n================================================\n")

    #Si es una cadena, lo avisa y lo imprime
    if type(Algo) == str: 
        print("En este momento es una cadena")
        print(f"\n{Algo}")
    #Si es una lista y no es muy larga la imprime
    elif type(Algo) == list: 
        print("En este momento es una lista")
        if len(Algo) > 100:
            print("\nSon más de 100 caracteres. ¿Seguro que quieres imprimir?")
            print("1.- Sí")
            print("2.- No")
            Respuesta = int(input("Respuesta:  "))
            if Respuesta == 1: print(Algo)
            elif Respuesta != 1: print("Ok.")
    #Si no es nada... Algo salió mal y avisa.
    else:
        print("... Está en un estado desconocido")
        MenuIngreso()
    print("\n================================================\n")
    


Algo = MenuIngreso()
while True:
    Algo = MenuOperacion(Algo)



