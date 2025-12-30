from tkinter import filedialog
import pandas as pd
import os
import tkinter as tk

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


