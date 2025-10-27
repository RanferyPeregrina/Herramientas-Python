import os
import PyPDF2

Biblioteca = []
Libros_Rechazados = []

def Impresion(Texto):
    for Objeto in Texto:
        print(Objeto)
        print( " - - - - - - - - - - -")
        print()


def Libro_Admitido(Archivo):
    if not Archivo.lower().endswith(".pdf"):
        return False
    
    Guiones_Permitidos = [" -", " - ", "- ", "-"]
    return any(Guion in Archivo for Guion in Guiones_Permitidos)
      
def Procesar(Archivo):
    #Acomodar el nombre del documento ------------------------------------------
    Titulo_Archivo = Archivo
    Titulo_Archivo = Titulo_Archivo.replace(" -", " - ").replace("- ", " - ")
    Titulo_Archivo = Titulo_Archivo.replace("  ", " ")
    Titulo_Archivo = Titulo_Archivo.replace(".pdf", "")

    if " - " not in Titulo_Archivo:
        Titulo_Archivo += " - Autor desconocido"

    #Obtener los datos del documento ------------------------------------------
    Titulo_Separado = Titulo_Archivo.split(" - ")
    Libro_Titulo = Titulo_Separado[0]           #Obtener el título
    Libro_Autor = Titulo_Separado[1]            #Obtener el autor

    #Obtener la cantidad de páginas

    with open(Archivo, "r") as Archivo_PDF:
        Archivo_LecturaEnPDF = PyPDF2.PdfReader(Archivo_PDF)
        Cantidad_Paginas = len(Archivo_LecturaEnPDF.pages)
        print(f"Del archivo {Archivo_PDF} son {Cantidad_Paginas} páginas")


    return{
        'Titulo ': Libro_Titulo,
        "Autor": Libro_Autor,
        "Archivo_Original": Archivo
    }



def Formar_Biblioteca():
    Archivos = os.listdir()
    for Archivo in Archivos:
        if Libro_Admitido(Archivo) == True:
            Archivo = Procesar(Archivo)
            Biblioteca.append(Archivo)
        elif Libro_Admitido != True:
            Libros_Rechazados.append(Archivo)
    
    print("¿Imprimir lista de rechazados?")
    print("1.- Sí")
    print("2.- No")
    Imprimir = int(input("Respuesta:  "))
    
    if Imprimir == 1: Impresion(Libros_Rechazados)
    return Biblioteca



Directorio_Actual = os.getcwd()

print("Primero que nada, estamos trabajando en el directiorio:")
print(Directorio_Actual)
print()

print("¿Cambiar directorio?")
print("1.- Sí")
print("2.- No")
Cambiar_Directorio = int(input("Respuesta:  "))
if Cambiar_Directorio == 1: os.chdir("")

Biblioteca = Formar_Biblioteca()
print(f"La biblioteca se está formando de: {Directorio_Actual}")
print("¿Imprimir biblioteca?")
print("1.- Sí")
print("2.- No")
Imprimir = int(input("Respuesta:  "))

if Imprimir == 1: Impresion(Biblioteca)
elif Imprimir == 2: print("Pues nada.")

input()