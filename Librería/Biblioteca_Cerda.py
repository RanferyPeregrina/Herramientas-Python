#pip install pandas openpyxl tk
from tkinter import filedialog
import PyPDF2
import pandas as pd
import os
import tkinter as tk

ListaDescartados = []
Diccionario_Biblioteca_Documentos = {}

def PreguntarDirectorio(): 
    while True:
        print()
        Directorio_Actual = os.getcwd()
        print(f"Estamos trabajando en el directorio: {Directorio_Actual}")
        print("¿Cambiar directorio? ")
        print("1.- Sí")
        print("2.- No")
        ActualizarDir = int(input("Respuesta:  "))

        if ActualizarDir == 1:
            print("Actualizando directorio")
            root = tk.Tk()  #Crea una ventana equis nomás para tener una excusa para abrir los archivos.
            root.withdraw()  # Oculta la ventana principal

            Directorio_Actual = filedialog.askdirectory()
            if Directorio_Actual:  # Si el usuario selecciona un directorio
                os.chdir(Directorio_Actual) #Cambia ese directorio
        else:
            print(f"Trabajando endonces en el directorio {Directorio_Actual}")
            break
        return Directorio_Actual

def ComprobarLibro(Archivo):
    if Archivo.lower().endswith('.pdf') and ' - ' in Archivo: return True

def ObtenerPaginas(Archivo):
        #Obtener la cantidad de páginas
    with open(Archivo, "rb") as Archivo_PDF:
        Instancia_Lectura = PyPDF2.PdfReader(Archivo_PDF)
        Numero_Paginas = len(Instancia_Lectura.pages)
        return Numero_Paginas
    Libro_Datos.append(Cantidad_Paginas)    #Las guarda también en esa lista, seguramente no se leerán desde aquí pero bueno


def ObtenerDatos(Archivo, Requerido):
    
    Libro_Datos = Archivo.split(" - ")
    Autor = Libro_Datos[0]
    Libro = Libro_Datos[1]
    Cantidad_Paginas = Libro_Datos.append(ObtenerPaginas(Archivo))

    if Requerido == 'Autor': return Autor
    elif Requerido == 'Libro': return Libro
    elif Requerido == 'Paginas': return Cantidad_Paginas
    else: return 'Error en la obtención de datos...'
    

def AgregarLibro(Archivo):
    Autor = ObtenerDatos(Archivo, 'Autor')
    Titulo = ObtenerDatos(Archivo, 'Libro')
    Paginas = ObtenerDatos(Archivo, 'Paginas')
    
    Libro_Nuevo = {
        
    }

def LeerBiblioteca_Excel():
    try:
        df_Biblioteca = pd.read_excel("Biblioteca_Cerda.xlsx")
        print(f"{len(df_Biblioteca)} registros leídos ✨")
        # print(df_Biblioteca)
        print()
    except FileNotFoundError:
        print("El archivo 'Biblioteca_Cerda.xlsx' no se encontró en el directorio actual.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def LeerBiblioteca_Documentos():
    for Archivo in os.listdir():
        if ComprobarLibro(Archivo): AgregarLibro(Archivo)
        else: ListaDescartados.append(Archivo)
        print(Archivo)
PreguntarDirectorio()
LeerBiblioteca_Excel()
LeerBiblioteca_Documentos()

input()