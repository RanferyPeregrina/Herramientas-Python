#Para que estas importaciones funcionen tienes que usar:
#pip install PyPDF2 PyMuPDF 
import os               #Para la lógica de archivos y lectura de documentos
import PyPDF2           #Para la lectura de los PDFs
import tkinter as tk    #Para abrir una ventanita
from tkinter import filedialog

Biblioteca = []
Libros_Rechazados = []

def Impresion(Biblioteca):
    print(f"=" * 50, end = f"\n Libros encontrados: {len(Biblioteca)}")
    for Libro in Biblioteca:
        print(Libro)



def Libro_Admitido(Archivo):
    #Si su versión en minúsculas NO acaba con ".pdf" entonces no es un PDF, se rechaza.
    if not Archivo.lower().endswith(".pdf"):
        return False
    #Si no se rechazó y utiliza cualquiera de los formatos de guión permitido, se acepta.
    Guiones_Permitidos = [" -", " - ", "- ", "-"]
    return any(Guion in Archivo for Guion in Guiones_Permitidos)
      
def Procesar(Archivo):
    #Acomodar el nombre del documento ------------------------------------------
    Titulo_Archivo = Archivo
    Titulo_Archivo = Titulo_Archivo.replace(" -", " - ").replace("- ", " - ")   #Acomoda guiones
    Titulo_Archivo = Titulo_Archivo.replace("  ", " ")                          #Quita "Doble espacios"
    Titulo_Archivo = Titulo_Archivo.replace(".pdf", "")                         #Quita la extensión de archivo

    if " - " not in Titulo_Archivo:
        Titulo_Archivo += " - Autor desconocido" #Si no tiene autor, le pone autor desconocido.

    #Obtener los datos del documento ------------------------------------------
    Libro_Datos = Titulo_Archivo.split(" - ")   #En una lista llamada "Libro_Datos"
    Libro_Titulo = Libro_Datos[0]           #Obtener el título
    Libro_Autor = Libro_Datos[1]            #Obtener el autor

    #Obtener la cantidad de páginas
    with open(Archivo, "r") as Archivo_PDF:
        Instancia_Lectura = PyPDF2.PdfReader(Archivo_PDF)
        Numero_Paginas = len(Instancia_Lectura.pages)
        return Numero_Paginas
    Libro_Datos.append(Cantidad_Paginas)    #Las guarda también en esa lista, seguramente no se leerán desde aquí pero bueno

    return{
        'Titulo ': Libro_Titulo,
        "Autor": Libro_Autor,
        "Paginas": Cantidad_Paginas,
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
if Cambiar_Directorio == 1:
    root = tk.Tk()
    root.title("Cambiar directorio")
    Directorio_Actual = filedialog.askdirectory()
    if Directorio_Actual:  # Si el usuario selecciona un directorio
        os.chdir(Directorio_Actual)
        print("Directorio de trabajo cambiado a:", os.getcwd())

Biblioteca = Formar_Biblioteca()
print(f"La biblioteca se está formando de: {Directorio_Actual}")
print("¿Imprimir biblioteca?")
print("1.- Sí")
print("2.- No")
Imprimir = int(input("Respuesta:  "))

if Imprimir == 1: Impresion(Biblioteca) #Pasa una lista de diccionarios.
elif Imprimir == 2: print("Pues nada.")

input()