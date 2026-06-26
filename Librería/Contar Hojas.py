import os
import argparse
from PyPDF2 import PdfReader

# Intentar importar openpyxl para leer Excel
try:
    import openpyxl
    EXCEL_SUPPORT = True
except ImportError:
    EXCEL_SUPPORT = False
    print("⚠️ openpyxl no está instalado. No se podrá contar hojas de Excel correctamente.")
    print("   Instálalo con: pip install openpyxl")

def contar_pdf(ruta_pdf):
    """Devuelve el número de páginas de un PDF."""
    try:
        with open(ruta_pdf, 'rb') as f:
            lector = PdfReader(f)
            return len(lector.pages)
    except Exception as e:
        print(f"   ❌ Error al leer PDF '{ruta_pdf}': {e}")
        return 0

def contar_excel(ruta_excel):
    """Devuelve el número de hojas de un libro Excel (.xlsx)."""
    if not EXCEL_SUPPORT:
        # Si no está openpyxl, asumimos 1 hoja (puedes cambiar a 0 o lanzar excepción)
        return 1
    try:
        libro = openpyxl.load_workbook(ruta_excel, read_only=True)
        hojas = len(libro.sheetnames)
        libro.close()
        return hojas
    except Exception as e:
        print(f"   ❌ Error al leer Excel '{ruta_excel}': {e}")
        return 0

def explorar_y_contar(carpeta_inicio):
    """Recorre recursivamente la carpeta y cuenta páginas/hojas de PDFs y Excels."""
    if not os.path.isdir(carpeta_inicio):
        print(f"❌ La ruta '{carpeta_inicio}' no es un directorio válido.")
        return

    print(f"🔍 Explorando directorio: {carpeta_inicio}")
    print("-" * 60)

    total_paginas_hojas = 0
    total_pdfs = 0
    total_excels = 0

    for raiz, dirs, archivos in os.walk(carpeta_inicio):
        print(f"\n📂 Entrando en: {raiz}")
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            if archivo.lower().endswith('.pdf'):
                paginas = contar_pdf(ruta_completa)
                total_paginas_hojas += paginas
                total_pdfs += 1
                print(f"   📄 PDF: {archivo} → {paginas} páginas")
            elif archivo.lower().endswith('.xlsx'):
                hojas = contar_excel(ruta_completa)
                total_paginas_hojas += hojas
                total_excels += 1
                print(f"   📊 Excel: {archivo} → {hojas} hojas")

    total_documentos = total_pdfs + total_excels
    if total_documentos == 0:
        print("\n⚠️ No se encontraron archivos PDF ni Excel.")
        return

    # Resumen final
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN FINAL")
    print(f"   📄 Total de documentos procesados: {total_documentos}")
    print(f"   📄 PDFs: {total_pdfs}")
    print(f"   📊 Excels: {total_excels}")
    print(f"   📝 Total de páginas/hojas sumadas: {total_paginas_hojas}")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(
        description="Recorre recursivamente un directorio y cuenta todas las páginas/hojas de PDFs y Excels."
    )
    parser.add_argument(
        "directorio",
        nargs="?",
        default=os.getcwd(),
        help="Directorio raíz a explorar (por defecto el actual)"
    )
    args = parser.parse_args()
    explorar_y_contar(args.directorio)

if __name__ == "__main__":
    main()
    input("\n✅ Terminado. Presiona ENTER para salir...")