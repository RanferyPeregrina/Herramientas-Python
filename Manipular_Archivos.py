import os #Para moverle a los directorios
import time #Para hacer pausas. Cosas de depuración.
import tkinter as tk    #Para hacer ventanas, como la del visualizador.
from tkinter import filedialog  #Para abrir ventanas del sistema operativo.
from tkinter import Label  #Para hacer titulos en las ventanas
from PIL import Image, ImageTk  #Para hacer visualizaciones rápidas de las imágenes


def Directorio_Obtener():
    Directorio_Actual = os.getcwd()
    return Directorio_Actual

def Directorio_Cambiar():
    root = tk.Tk()
    root.withdraw()
    Directorio_Actual = filedialog.askdirectory()
    return Directorio_Actual

def Ventana(Directorio_Imagenes):
    root = tk.Tk()
    root.title("Imagenes en es ta carpeta")
    root.geometry("1000x800")

    # Obtener la lista de imágenes en el directorio
    imagenes = [f for f in os.listdir(Directorio_Imagenes) if f.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    print(f"{len(imagenes)} imágenes encontradas")
    print()

    for Imagen in imagenes: #Para cada imágen...
        print(f"Ahora mostrando {Imagen}")

    root.mainloop()

Directorio = Directorio_Obtener()
while True:
    print("="*50)
    print(f"El donde estamos trabajando es: {Directorio}")
    print("¿Desea cambiarlo?")
    print("1.- Sí")
    print("2.- No")
    Respuesta_CambiarDirectorio = int(input("Respuesta:  "))
   
    if Respuesta_CambiarDirectorio == 1:
        Directorio = Directorio_Cambiar()
    elif Respuesta_CambiarDirectorio == 2:
        print("\n"*10)
        Ventana(Directorio)


    else: break