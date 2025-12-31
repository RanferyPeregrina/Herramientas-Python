#pip install pandas openpyxl tk
from tkinter import filedialog
import pandas as pd
import os
import tkinter as tk

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

def LeerBiblioteca_Excel():
    try:
        df_Biblioteca = pd.read_excel("Biblioteca_Cerda.xlsx")
        print(f"{len(df_Biblioteca)} registros leídos ✨")
        print(df_Biblioteca)
    except FileNotFoundError:
        print("El archivo 'Biblioteca_Cerda.xlsx' no se encontró en el directorio actual.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def LeerBiblioteca_Documentos():
    print("Hola")
PreguntarDirectorio()
LeerBiblioteca_Excel()

input()