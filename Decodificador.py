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
    print("3.- Codificar texto.")
    Respuesta = int(input("Respuesta:  "))
    if Respuesta == 1: Algo = Traducir_ASCII(Algo)
    elif Respuesta == 2: Algo = Traducir_Texto(Algo)
    elif Respuesta == 3: Algo = Codificar(Algo)

    else:
        print("Respuesta no válida.")
        print("Ingrese de nuevo.\n")
        MenuOperacion(Algo)
    
    return Algo

def MenuPost(Algo):
    print("=" * 30)
    print("¿Desea hacer algo con este texto?")
    print("1.- Mostrarlo")
    print("2.- Traducirlo")
    print("3.- Modificarlo")

    Respuesta = int(input("Respuesta:  "))
    if Respuesta == 1: print(f"\n{Algo}")
    elif Respuesta == 2: Traducir_ASCII(Algo)
    elif Respuesta == 3: print("Función en desarrollo")



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

    

    Palabra = ""
    for Caracter in Palabra_ASCII:
        Letra = str(Caracter)
        Palabra += Letra
    print(f"La palabra leída es: {Palabra}")
    return Palabra
#Convierte de Texto a ASCII
def Traducir_Texto(Palabra):
    Palabra_ASCII = []
    for Letra in Palabra:
        Letra_ASCII = ord(Letra)
        Palabra_ASCII.append(Letra_ASCII)
    print(Palabra_ASCII)
    return Palabra_ASCII


def Codificar(Texto):
    Texto_Nuevo = []

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

    
Algo = MenuIngreso()
Algo = MenuOperacion(Algo)
MenuPost(Algo)