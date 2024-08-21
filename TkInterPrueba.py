import tkinter as tk
from tkinter import Label, Button



def Restar1(CuentaActual):
    CuentaActual = CuentaActual - 1
    return CuentaActual

def Sumar1(CuentaActual):
    CuentaActual = CuentaActual + 1
    return CuentaActual

def Ventana():
    Raiz = tk.Tk()
    Raiz.geometry("650x320")
    Raiz.title("Ventanita bonita")

    Titulo = Label(Raiz, text="Titulo1")
    Titulo.pack()

    Boton1 = Button(Raiz, text="Presiona aquí para sumar", command=Sumar1)
    Boton1.pack()

    Boton2 = Button(Raiz, text="Presiona aquí para restar", command=Restar1)
    Boton2.pack()

    Raiz.mainloop()

Ventana()