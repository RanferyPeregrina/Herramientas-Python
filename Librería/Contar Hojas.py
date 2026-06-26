import os
import sys
import subprocess
import time
import argparse
from PyPDF2 import PdfReader
import win32com.client  # Para controlar Excel

""" Programa hecho para contar toooodas las hojas que hay en un directorio incluyendo su subcarpetas
    Contando los PDFs y los XLSX"""


def contar_pdf(ruta_pdf):

    # Contar páginas 
    with open(ruta_pdf, 'rb') as f:
        lector = PdfReader(f)
        total_paginas = len(lector.pages)



def explorar_e_imprimir(carpeta_inicio):

    PaginasTotales = 0

    """Recorre recursivamente la carpeta e imprime todos los PDFs y Excel encontrados."""
    if not os.path.isdir(carpeta_inicio):
        print(f"❌ La ruta '{carpeta_inicio}' no es un directorio válido.")
        return

    print(f"🔍 Explorando directorio: {carpeta_inicio}")
    print("-" * 60)

    pdfs = []
    excels = []

    for raiz, dirs, archivos in os.walk(carpeta_inicio):
        print(f"\n📂 Entrando en: {raiz}")
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            if archivo.lower().endswith('.pdf'):
                pdfs.append(ruta_completa)
                print(f"   📄 PDF: {archivo}, {len(archivo.pages)}")
                PaginasTotales += len(archivo.pages)
            elif archivo.lower().endswith('.xlsx'):
                excels.append(ruta_completa)
                print(f"   📊 Excel: {archivo}")
                PaginasTotales += 1 #Asumiendo que todos los Excel miden 1 página de largo. Pero la verdad no sé cómo contar cuántas páginas le va a tomar imprimir un Excel.

    total = len(pdfs) + len(excels)
    if total == 0:
        print("\n⚠️ No se encontraron archivos PDF ni Excel.")
        return

    print(f"\n🖨️  Contados en esta subcarpeta {total} documentos: ({len(pdfs)} PDFs, {len(excels)} Excel)...")
    print("-" * 60)

    # Mezclar ambos tipos en una sola lista (primero PDFs, luego Excel, o el orden que quieras)
    documentos = [(r, 'pdf') for r in pdfs] + [(r, 'excel') for r in excels]

    exitos = 0
    errores = 0

    # Resumen final
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN FINAL")
    print(f"   📄 Total procesados: {total}")
    print(f'    {PaginasTotales} páginas en total.')
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Recorre recursivamente un directorio y cuenta todos los PDFs"
    )
    parser.add_argument(
        "directorio",
        nargs="?",
        default=os.getcwd(),
        help="Directorio raíz a explorar (por defecto el actual)"
    )
    args = parser.parse_args()
    explorar_e_imprimir(args.directorio)


if __name__ == "__main__":
    main()

input('Terminado. esperando ENTER')