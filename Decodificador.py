import random

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
    print("4.- Decodificar texto.")
    print("0.- Reiniciar todo.")
    Respuesta = int(input("Respuesta:  "))

    if Respuesta == 1: #Traducir ASCII
        Algo = Traducir_ASCII(Algo)


    elif Respuesta == 2: #Traducir texto
        Algo = Traducir_Texto(Algo)
        if len(Algo) > 100:
            print("El contenido es algo largo. ¿Aún así quiere imprimirlo?")
            print("1.- Sí")
            print("2.- No")
            Respuesta = int(input("Respuesta:  "))
            if Respuesta == 1:
                print(Algo)
            elif Respuesta == 2: print("Ok")

    elif Respuesta == 3: #Codificar
        Algo = Codificar(Algo)
        print("¿Imprimir texto codificado?")
        print("1.- Sí")
        print("2.- No")
        Respuesta = int(input("Respuesta:  "))
        if Respuesta == 1:
            print("\n===================================\n")
            print(Algo)
            print("\n===================================\n")

    elif Respuesta == 4: #Decodificar
        Algo = Decodificar(Algo)
        print("¿Imprimir texto codificado?")
        print("1.- Sí")
        print("2.- No")
        Respuesta = int(input("Respuesta:  "))
        if Respuesta == 1:
            print("\n===================================\n")
            print(Algo)
            print("\n===================================\n")

    elif Respuesta == 5: Algo = Mostrar(Algo)

    elif Respuesta == 0:
        Main()
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

    if type(Palabra) == str:
        for Letra in Palabra:
            Letra_ASCII = ord(Letra)
            Palabra_ASCII.append(Letra_ASCII)
    else: 
        Palabra_ASCII = Palabra
        print(f"Esto ya es una lista: {Palabra}")
    return Palabra_ASCII


def Codificar(Texto):
    Texto_Nuevo = []
    
    while True:
        Vector = input("Ingrese contraseña de codificación:  ")
        if len(Vector) < 8: print("Contraseña muy pequeña. Intente de nuevo")
        else: break

    LongitudVector = int(len(Vector) * 7)
    Vector = Traducir_Texto(Vector)

    #El primer caracter nos da un factor de aleatorización
    EspaciosAleatorios1 = Vector[0] + Vector[3] + Vector[len(Vector) - 1]
    #El segundo caracter nos da un factor de aleatorización
    EspaciosAleatorios2 = Vector[1] + Vector[6]
    #La octava letra da un caracter aleatorio.
    EspaciosAleatorios3 = (Vector[6] + Vector[2] - Vector[1]) * EspaciosAleatorios1
    #Una frecuencia de espacios es la mitad de la longitud de la cadena
    EspaciosAleatorios4 = LongitudVector
    #El cuarto caracter nos da un número de suma
    Suma1 = Vector[3] + EspaciosAleatorios2 - (2 * (Vector[len(Vector) - 1]))
    #El sexto caracter nos da un número de resta
    Resta1 = Vector[5] * EspaciosAleatorios3 
    #El tercer caracter nos da una suma
    Suma2 = (Vector[2] + Vector[2]) * EspaciosAleatorios2 + Vector[0] * (Vector[len(Vector) - 1])
    #El quinto caracter nos da una resta
    Resta2 = Vector[4] + Vector[2] - (min(Vector))
    #La octava letra da un caracter aleatorio.
    CaracterAleatorio = Vector[7] + Vector[0] + max(Vector)
    #La octava letra da un caracter aleatorio.
    CaracterAleatorio2 = min(Vector)
    CaracterAleatorio3 = random.randint(32, 255)

    if type(Texto) == str:
        Texto = Traducir_Texto(Texto)
    
    Posicion = 0
    for Caracter in Texto:
        Posicion += 1

        Caracter = Caracter + Suma1 - Resta1

        if Posicion == EspaciosAleatorios1: Caracter = Caracter + Suma2
        if Posicion == EspaciosAleatorios2: Caracter = Caracter - Resta2

        Caracter = Caracter % 255
        Texto_Nuevo.append(Caracter)

        if (Posicion % EspaciosAleatorios1) == 0: Texto_Nuevo.append(CaracterAleatorio)
        if (Posicion % EspaciosAleatorios2) == 0: Texto_Nuevo.append(CaracterAleatorio2)
        if (Posicion % EspaciosAleatorios3) == 0: Texto_Nuevo.append(CaracterAleatorio3)
        if (Posicion % EspaciosAleatorios4) == 0: Texto_Nuevo.append(random.choice([10, CaracterAleatorio2, CaracterAleatorio, CaracterAleatorio3]))
        

    return Texto_Nuevo

def Decodificar(Texto):
  
    #Convertimos el texto en una lista
    if type(Texto) == str:
        Texto = Traducir_Texto(Texto)

    #Preguntamos la contraseña
    while True:
        Vector = input("\nIngrese la contraseña con la que fue codificado su texto:  ")
        if len(Vector) < 8: print("Contraseña demasiado corta.")
        else: break
    LongitudVector = int(len(Vector) * 7)
    Vector = Traducir_Texto(Vector)

    #El primer caracter nos da un factor de aleatorización
    EspaciosAleatorios1 = Vector[0] + Vector[3] + Vector[len(Vector) - 1]
    #El segundo caracter nos da un factor de aleatorización
    EspaciosAleatorios2 = Vector[1] + Vector[6]
    #La octava letra da un caracter aleatorio.
    EspaciosAleatorios3 = (Vector[6] + Vector[2] - Vector[1]) * EspaciosAleatorios1
    #Una frecuencia de espacios es la mitad de la longitud de la cadena
    EspaciosAleatorios4 = LongitudVector
    #El cuarto caracter nos da un número de suma
    Suma1 = Vector[3] + EspaciosAleatorios2 - (2 * (Vector[len(Vector) - 1]))
    #El sexto caracter nos da un número de resta
    Resta1 = Vector[5] * EspaciosAleatorios3 
    #El tercer caracter nos da una suma
    Suma2 = (Vector[2] + Vector[2]) * EspaciosAleatorios2 + Vector[0] * (Vector[len(Vector) - 1])
    #El quinto caracter nos da una resta
    Resta2 = Vector[4] + Vector[2] - (min(Vector))
    #La octava letra da un caracter aleatorio.
    CaracterAleatorio = Vector[7] + Vector[0] + max(Vector)
    #La octava letra da un caracter aleatorio.
    CaracterAleatorio2 = min(Vector)
    CaracterAleatorio3 = random.randint(32, 255)


    Texto_Decodificado = []
    Posicion = 0
    for Letra in Texto:
        Posicion += 1
        Caracter_Original = (Letra - Suma1 + Resta1)
        if Posicion == EspaciosAleatorios1: Caracter_Original = Letra - Suma2
        if Posicion == EspaciosAleatorios2: Caracter_Original = Letra + Resta2
        Caracter_Original = Caracter_Original % 255
        Texto_Decodificado.append(Caracter_Original)

        #Si detecta que es donde se puso un caracter aleatorio, quita la última letra que se haya puesto
        if (Posicion % EspaciosAleatorios1) == 0: Texto_Decodificado.pop(len(Texto_Decodificado) - 1) 
        if (Posicion % EspaciosAleatorios2) == 0: Texto_Decodificado.pop(len(Texto_Decodificado) - 1)
        if (Posicion % EspaciosAleatorios3) == 0: Texto_Decodificado.pop(len(Texto_Decodificado) - 1)
        if (Posicion % EspaciosAleatorios4) == 0: Texto_Decodificado.pop(len(Texto_Decodificado) - 1)
        
    return Texto_Decodificado



def Mostrar(Algo):
    print("\n================================================\n")

    #Si es una cadena, lo avisa y lo imprime
    if type(Algo) == str: 
        print("En este momento es una cadena")
        print(f"\n{Algo}")
    #Si es una lista y no es muy larga la imprime
    elif type(Algo) == list: 
        print("En este momento es una lista")
        print(f"\n{Algo}")
    #Si no es nada... Algo salió mal y avisa.
    else:
        print("... Está en un estado desconocido")
        MenuIngreso()
    print("\n================================================\n")
    return Algo
    
def MostrarDigitos():
    Muchas_Letras = []
    for i in range(128000, 13000):
        Muchas_Letras.append(chr(i))
        print(f"Caracter {i}: {chr(i)}")

    Muchos_Numeros = []
    for j in range(128000, 13000):
        Muchos_Numeros.append(ord(Muchas_Letras[j]))
        print(f"Lectura de {Muchas_Letras[j]} = {Muchos_Numeros[j]}")
        if Muchos_Numeros[j] != j: print("\nERROR, este pinche número no va \n")


def Main():
    print("\n" * 5)
    Algo = MenuIngreso()
    while True:
        Algo = MenuOperacion(Algo)

Main()
input()

