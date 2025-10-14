import os

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
    Titulo_Archivo = Archivo
    Titulo_Archivo = Titulo_Archivo.replace(" -", " - ").replace("- ", " - ")
    Titulo_Archivo = Titulo_Archivo.replace("  ", " ")
    Titulo_Archivo = Titulo_Archivo.replace(".pdf", "")

    if " - " not in Titulo_Archivo:
        Titulo_Archivo += " - Autor desconocido"

    Titulo_Separado = Titulo_Archivo.split(" - ")
    Libro_Titulo = Titulo_Separado[0]
    Libro_Autor = Titulo_Separado[1]

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
Biblioteca = Formar_Biblioteca()
print(f"La biblioteca se está formando de: {Directorio_Actual}")
print("¿Imprimir biblioteca?")
print("1.- Sí")
print("2.- No")
Imprimir = int(input("Respuesta:  "))

if Imprimir == 1: Impresion(Biblioteca)
elif Imprimir == 2: print("Pues nada.")

input()