# #Hola soy Ran.
# No olviden importar con "pip install PyPDF2 PyMuPDF docx docx2pdf pycryptodome python-docx"


import tkinter as tk
import os
import fitz  # PyMuPDF
import PyPDF2
from docx import Document
from tkinter import filedialog
from PyPDF2 import PdfReader , PdfWriter
from docx2pdf import convert


# Función para seleccionar un archivo PDF
def seleccionar_archivo(extension=".pdf"):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(filetypes=[(f"Archivos {extension.upper()}", f"*{extension}")])
    if file_path:
        print("Archivo encontrado")
        print("\n")
        return file_path
    else:
        print("No se seleccionó ningún archivo.")
        return None


def contar_paginas(archivo):
    with open(archivo, "rb") as Documento:
        Instancia_Lectura = PyPDF2.PdfReader(Documento)
        Numero_Paginas = len(Instancia_Lectura.pages)
        return Numero_Paginas


# Función para extraer un sub-PDF
def extraer_subpdf(archivo_original, primera_pagina, ultima_pagina, archivo_salida):
    try:
        pdf_reader = PdfReader (open(archivo_original, 'rb'))
        pdf_writer = PdfWriter()

        for pagina_num in range(primera_pagina - 1, ultima_pagina):  # Restamos 1 porque los índices comienzan desde 0
            pagina = pdf_reader.pages[pagina_num]
            pdf_writer.add_page(pagina)

        # Obtener el directorio actual del programa
        directorio_actual = os.getcwd()

        # Verificar si el nombre del archivo de salida tiene la extensión .pdf
        if not archivo_salida.lower().endswith('.pdf'):
            archivo_salida += '.pdf'
      
      # Ruta completa al archivo de salida
        ruta_completa = os.path.join(directorio_actual, archivo_salida)

        with open(archivo_salida, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        
        print(f"Se ha creado el sub-PDF '{archivo_salida}' con las páginas del {primera_pagina} al {ultima_pagina} del archivo original '{archivo_original}'.")
        print(f"Lo puedes encontrar en la ruta: {ruta_completa}")
    except Exception as e:
        print(f"Error al extraer el sub-PDF: {e}")

def QuitarPares(pdf, Cantidad_Paginas, archivo_salida):
    try:
        pdf_reader = PdfReader (open(pdf, 'rb'))
        pdf_writer = PdfWriter()

        print("\nEliminar pares o impares?:  ")
        print("1.- Pares")
        print("2.- Impares")
        Respuesta = int(input("Respuesta:  "))

        if Respuesta == 1:
            for pagina_num in range(0, Cantidad_Paginas):  # Restamos 1 porque los índices comienzan desde 0
                
                if pagina_num % 2 == 0:
                    pagina = pdf_reader.pages[pagina_num]
                    pdf_writer.add_page(pagina)
            print(f"Se han eliminado las páginas par.")
            # Obtener el directorio actual del programa
            directorio_actual = os.getcwd()

        elif Respuesta != 2:
            for pagina_num in range(primera_pagina - 1, Cantidad_Paginas):  # Restamos 1 porque los índices comienzan desde 0
                if pagina_num % 2 == 0:
                    pagina = pdf_reader.pages[pagina_num]
                    pdf_writer.add_page(pagina)
            print(f"Se han eliminado las páginas impares.")


        # Verificar si el nombre del archivo de salida tiene la extensión .pdf
        if not archivo_salida.lower().endswith('.pdf'):
            archivo_salida += '.pdf'
            # Obtener el directorio actual del programa
            directorio_actual = os.getcwd()

        # Verificar si el nombre del archivo de salida tiene la extensión .pdf
        if not archivo_salida.lower().endswith('.pdf'):
            archivo_salida += '.pdf'


      # Ruta completa al archivo de salida
        ruta_completa = os.path.join(directorio_actual, archivo_salida)

        with open(archivo_salida, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        

        print(f"Lo puedes encontrar en la ruta: {ruta_completa}")
    except Exception as e:
        print(f"Error al extraer el sub-PDF: {e}")

#Función para unor 2 PDFs en uno solo
def unir_pdfs(pdf1, pdf2, archivo_salida):
    try:
        pdf_writer = PdfWriter()

         # Agregar páginas del primer PDF
        with open(pdf1, 'rb') as pdf1_file:
            pdf1_reader = PdfReader(pdf1_file)
            for pagina_num in range(len(pdf1_reader.pages)):
                pagina = pdf1_reader.pages[pagina_num]
                pdf_writer.add_page(pagina)

        # Agregar páginas del segundo PDF
        with open(pdf2, 'rb') as pdf2_file:
            pdf2_reader = PdfReader(pdf2_file)
            for pagina_num in range(len(pdf2_reader.pages)):
                pagina = pdf2_reader.pages[pagina_num]
                pdf_writer.add_page(pagina)

    # Obtener el directorio actual del programa
        directorio_actual = os.getcwd()

        # Verificar si el nombre del archivo de salida tiene la extensión .pdf
        if not archivo_salida.lower().endswith('.pdf'):
            archivo_salida += '.pdf'
      
      # Ruta completa al archivo de salida
        ruta_completa = os.path.join(directorio_actual, archivo_salida)


        # Escribir el PDF combinado
        with open(archivo_salida, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        
        print(f"Se han unido los PDFs '{pdf1}' y '{pdf2}' en el archivo '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al unir los PDFs: {e}")

#Funcion para convertir un Word a PDF
def convertir_word(archivo_word, nombre_pdf):
    try:
        convert(archivo_word, nombre_pdf)
        print(f"Se ha convertido exitosamente el archivo Word '{archivo_word}' a PDF: '{nombre_pdf}'")
    except Exception as e:
        print(f"Error al convertir el archivo PDF a Word: {e}")

#Función para convertir un PDF a Word
def convertir_pdf_a_word(archivo_pdf, archivo_word):
    try:
        doc = fitz.open(archivo_pdf)
        doc_word = Document()

        for pagina_num in range(doc.page_count):
            pagina = doc[pagina_num]
            texto = pagina.get_text()
            doc_word.add_paragraph(texto)

        # Verificar si el nombre del archivo de salida tiene la extensión .docx
        if not archivo_word.lower().endswith('.docx'):
            archivo_word += '.docx'

        doc_word.save(archivo_word)
        
        print(f"Se ha convertido exitosamente el archivo PDF '{archivo_pdf}' a Word: '{archivo_word}'")
    except Exception as e:
        print(f"Error al convertir el archivo PDF a Word: {e}")

#Función para rotar un PDF entero (Todas sus páginas)
def GirarPDF_Entero(archivo_pdf, Grados):
    
    try:
        Archivo = fitz.open(archivo_pdf)
        
        for numero_pagina in range(Archivo.page_count):
            pagina = Archivo[numero_pagina]
            pagina.set_rotation(Grados)
            
        # Guardar el PDF modificado
        Archivo.save(archivo_pdf, incremental=True)
        Archivo.close()
        
        print(f"Se han girado todas las páginas del archivo PDF '{archivo_pdf}' en {Grados} grados.")
    except Exception as e:
        print(f"Error al girar todas las páginas del archivo PDF: {e}")

#Función para rotar una página de un PDF.
def GirarPDF_PaginaEspecifica(Archivo, Pagina_Girar, Grados):
    try:
        Documento = fitz.open(Archivo)
       
        if 0 <= Pagina_Girar - 1 < Documento.page_count:
            pagina = Documento[Pagina_Girar - 1]
            pagina.set_rotation(Grados)
            
            # Guardar el PDF modificado
            Documento.save(Archivo, incremental=True, encryption=0)
            Documento.close()
            
            print(f"Se ha girado la página {Pagina_Girar} del archivo PDF '{Archivo}' en {Grados} grados.")
        else:
            print(f"Número de página inválido. El PDF tiene {Documento.page_count} páginas.")
    except Exception as e:
        print(f"Error al girar la página del archivo PDF: {e}")


while(True):
    print("==================== MODIFICADOR DE PDFs ====================")
    print("Seleccione su operación con el PDF:")
    print("1.- Extraer un Sub-PDF")
    print("2.- Juntar 2 PDFs")
    print("3.- Convertir Word a PDF.")
    print("4.- Convertir PDF a Word")
    print("5.- Girar un PDF")
    print("6.- Quitarle portada a un PDF")
    print("7.- Quitar pares/impares blancos")
    print("8.- Dividir en fragmentos")
    Operación = int(input("  Respuesta:  "))

    if Operación == 1:
        print("Usted ha seleccionado la primera opción.")
        print("Para extraer páginas específicas de un PDF")
        print("")
        print("A continuación se seleccionará su archivo")
        archivo_pdf = seleccionar_archivo()
        if archivo_pdf:
            primera_pagina = int(input("Ingrese el número de la primera página a extraer: "))
            ultima_pagina = int(input("Ingrese el número de la última página a extraer: "))
            nombre_subPDF = input("Ingrese el nombre que le quiere poner a su nuevo PDF recortado:  ")
            extraer_subpdf(archivo_pdf, primera_pagina, ultima_pagina, nombre_subPDF)
            print(f"Extrayendo páginas del {primera_pagina} al {ultima_pagina} del archivo {archivo_pdf}.")

    if Operación == 2:
        print("Usted ha seleccionado la segunda opción.")
        print("Para unir dos PDFs")
        print("")
        print("A continuación se seleccionarán los archivos PDF")
        archivo_pdf1 = seleccionar_archivo()
        archivo_pdf2 = seleccionar_archivo()
        if archivo_pdf1 and archivo_pdf2:
            nombre_subPDF = input("Ingrese el nombre del archivo de salida del PDF combinado: ")
            unir_pdfs(archivo_pdf1, archivo_pdf2, nombre_subPDF)

    if Operación == 3:
        print("¿Quiere convertir uno o más de uno?")
        print("1.- Sólo uno")
        print("2.- Varios.")
        CantidadPDFs = int(input("Respuesta: "))
        if CantidadPDFs == 1:
            print("Se convertirá un Word a PDF.")
            print("Seleccione su archivo Word: ")
            archivoWord_a_convertir = seleccionar_archivo(".docx")
            if archivoWord_a_convertir:
                nombreFinal = input("Ingrese el nombre que tendrá su PDF al final: ")
                convertir_word(archivoWord_a_convertir, nombreFinal)
        if CantidadPDFs == 2:
            print("Se convertirán varios Word a PDF.")

    if Operación == 4:
        print("¿Quiere converir uno o más de uno?")
        print("1.- Sólo uno")
        print("2.- Varios.")
        CantidadPDFs = int(input("Respuesta: "))
        if CantidadPDFs == 1:
            print("Se convertirá un documento de PDF a Word.")
            print("Seleccione su archivo...")
            archivoPDF_a_convertir = seleccionar_archivo(".pdf")
            if archivoPDF_a_convertir:
                nombreFinal = input("Ingrese el nombre que tendrá su archivo Word al final: ")
                convertir_pdf_a_word(archivoPDF_a_convertir, nombreFinal)
        elif CantidadPDFs == 2:
            print("Las cosas de varios PDF.")

    if Operación == 5:
        print("Se girará su documento de PDF.")
        print("Seleccione su archivo...")
        archivo_pdf = seleccionar_archivo(".pdf")

        print("\n¿Desea girar todo el PDF o sólo una página del documento?")
        print("1.- Todo el PDF entero con todas sus páginas")
        print("2.- Una página específica de todo el PDF.")
        DecisionCuantasGirar = int(input("Respuesta:  "))

        print("\nAhora seleccione la cantidad de grados que quiere girar.")
        print("1.- 90° a la izquierda")
        print("2.- 90° a la derecha")
        print("3.- 180° (Vuelta vertical)")
        print("4.- Una cantidad específica de grados (A especificar)")
        GradosDecision = int(input("Respuesta:  "))
        if GradosDecision == 1: GradosGirar = 90
        elif GradosDecision == 2: GradosGirar = 270
        elif GradosDecision == 3: GradosGirar= 180
        elif GradosDecision == 4: GradosGirar = float(input("Ingrese los grados:  "))

        if DecisionCuantasGirar == 1:
            GirarPDF_Entero(archivo_pdf, GradosGirar)
        if DecisionCuantasGirar == 2:
            PaginaEspecifica = int(input("¿Qué página es la que quiere girar:  "))
            GirarPDF_PaginaEspecifica(archivo_pdf, PaginaEspecifica, GradosGirar)

    if Operación == 6:
        archivo_pdf = seleccionar_archivo()
        Cantidad_Paginas = contar_paginas(archivo_pdf)
        nombre_subPDF = input("Ingrese el nombre que le quiere poner a su nuevo PDF:  ")

        if archivo_pdf:
            extraer_subpdf(archivo_pdf, 2, Cantidad_Paginas, nombre_subPDF)

    if Operación == 7:
    
        archivo_pdf = seleccionar_archivo()
        Cantidad_Paginas = contar_paginas(archivo_pdf)
        nombre_subPDF = input("Nombre de su nuevo PDF:  ")

        if archivo_pdf:
            QuitarPares(archivo_pdf, Cantidad_Paginas, nombre_subPDF)
    
    if Operación == 8:
        print('\n' * 5)
        print("Seleccione su archivo.")
        archivo_pdf = seleccionar_archivo()
        if archivo_pdf:
            Cantidad_Paginas = contar_paginas(archivo_pdf)
            print(f"Su archivo tiene {Cantidad_Paginas}")
            Partes = int(input('¿En cuántas partes lo quieres dividir?  :  '))

            Division = int(Cantidad_Paginas/Partes)
            Residuo = Cantidad_Paginas % Partes
            Inicio = 0
            Final = Division

            for i in range(1, Partes+1):
                
                NuevoNombre =archivo_pdf = archivo_pdf + '_' + i
                Final = Division * i
                if i == Partes: Final = Cantidad_Paginas
                
                print()
                print(f'El archivo {archivo_pdf}_{i} es desde {Inicio + 1} hasta {Final}')
                extraer_subpdf(archivo_pdf, Inicio + 1, Final, archivo_pdf)
                print()

                if Final % 2 != 0: Final += 1
                Inicio = Final



