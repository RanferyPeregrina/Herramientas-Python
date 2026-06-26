import os
import sys
import subprocess
import time
import argparse
from PyPDF2 import PdfReader
import win32com.client  # Para controlar Excel


def imprimir_pdf(ruta_pdf):
    """Envía un PDF a la impresora predeterminada."""
    try:
        # Contar páginas (opcional, solo para información)
        with open(ruta_pdf, 'rb') as f:
            lector = PdfReader(f)
            total_paginas = len(lector.pages)

        # Impresión según SO
        if sys.platform == "win32":
            comando = [
                "powershell",
                "-Command",
                f"Start-Process -FilePath \"{ruta_pdf}\" -Verb Print -WindowStyle Hidden"
            ]
            subprocess.run(comando, timeout=30, check=True)
        elif sys.platform == "darwin":  # macOS
            subprocess.run(["lp", ruta_pdf], timeout=30, check=True)
        else:  # Linux
            subprocess.run(["lp", ruta_pdf], timeout=30, check=True)

        # Registrar en log
        with open('LogActual.txt', 'a', encoding='utf-8') as log:
            log.write(f'{ruta_pdf}\n')

        print(f"   ✅ Impresión PDF enviada ({total_paginas} páginas)")
        return True

    except subprocess.TimeoutExpired:
        print(f"   ⚠️  Timeout al imprimir {os.path.basename(ruta_pdf)}")
        return False
    except Exception as e:
        print(f"   ❌ Error al imprimir PDF {os.path.basename(ruta_pdf)}: {str(e)}")
        return False


def imprimir_excel(ruta_excel):
    """
    Abre el Excel, configura impresión horizontal, ajuste a una página,
    imprime solo la primera hoja y cierra.
    """
    excel = None
    try:
        # Iniciar Excel en segundo plano
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False
        workbook = excel.Workbooks.Open(ruta_excel)

        # Seleccionar la primera hoja
        sheet = workbook.Worksheets(1)
        sheet.Activate()

        # Configurar página: horizontal y ajustar a una página
        page_setup = sheet.PageSetup
        page_setup.Orientation = 2          # 2 = xlLandscape (horizontal)
        page_setup.Zoom = False             # Desactivar zoom manual
        page_setup.FitToPagesWide = 1       # Todas las columnas en 1 página
        page_setup.FitToPagesTall = 1       # Todas las filas en 1 página (opcional)

        # Imprimir
        workbook.PrintOut()

        # Cerrar sin guardar
        workbook.Close(SaveChanges=False)
        excel.Quit()

        # Registrar en log
        with open('LogActual.txt', 'a', encoding='utf-8') as log:
            log.write(f'{ruta_excel}\n')

        print(f"   ✅ Impresión Excel enviada (1ª hoja, horizontal, ajustada)")
        return True

    except Exception as e:
        print(f"   ❌ Error al imprimir Excel {os.path.basename(ruta_excel)}: {str(e)}")
        return False
    finally:
        # Asegurar que Excel se cierre incluso si hay error
        try:
            if excel:
                excel.Quit()
        except:
            pass


def explorar_e_imprimir(carpeta_inicio):
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
                # pdfs.append(ruta_completa)
                print(f"   📄 PDF: {archivo}")
            elif archivo.lower().endswith('.xlsx'):
                excels.append(ruta_completa)
                print(f"   📊 Excel: {archivo}")

    total = len(pdfs) + len(excels)
    if total == 0:
        print("\n⚠️  No se encontraron archivos PDF ni Excel.")
        return

    print(f"\n🖨️  Iniciando impresión de {total} documentos ({len(pdfs)} PDFs, {len(excels)} Excel)...")
    print("-" * 60)

    # Mezclar ambos tipos en una sola lista (primero PDFs, luego Excel, o el orden que quieras)
    documentos = [(r, 'excel') for r in excels]

    exitos = 0
    errores = 0

    for i, (ruta, tipo) in enumerate(documentos, 1):
        print(f"\n[{i}/{total}] Procesando: {ruta}")
        if tipo == 'pdf':
            exito = imprimir_pdf(ruta)
        else:
            exito = imprimir_excel(ruta)

        if exito:
            exitos += 1
        else:
            errores += 1

        # Pausa cada 2000 documentos procesados (suma de éxitos + errores)
        if (exitos + errores) % 2000 == 0:
            input("\n⏸️  Pausa de seguridad (2000 documentos procesados). Presiona ENTER para continuar...")

        time.sleep(1)  # Pequeña pausa entre documentos

    # Resumen final
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN FINAL")
    print(f"   ✅ Impresiones exitosas: {exitos}")
    print(f"   ❌ Fallos: {errores}")
    print(f"   📄 Total procesados: {total}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Recorre recursivamente un directorio e imprime todos los PDF y Excel encontrados."
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