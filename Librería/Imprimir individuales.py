import os
import subprocess
import time
from pathlib import Path
import sys
# import shutil # (No lo estás usando)
from PyPDF2 import PdfReader

def LeerDirectorio():
    Directorio_Actual = os.path.dirname(os.path.abspath(__file__))
    return Directorio_Actual

def imprimir_pdfs_individuales(carpeta_pdfs, impresora_nombre=None):
    carpeta = Path(carpeta_pdfs)
    PaginasLocales = 0

    if not carpeta.exists():
        print(f"❌ La carpeta {carpeta} no existe")
        return
    
    # 1. SOLUCIÓN: Validar que exista Excluidos.txt antes de abrirlo
    ArchivosExcluidos = Path('Excluidos.txt')
    Excluidos = set()
    
    if ArchivosExcluidos.exists():
        with open(ArchivosExcluidos, 'r', encoding='utf-8') as f:
            for linea in f:
                nombre = linea.strip()
                if nombre:
                    Excluidos.add(nombre)
    else:
        print("⚠️ No se encontró 'Excluidos.txt', se imprimirán todos los archivos.")

    # Obtener lista de PDFs ORDENADOS alfabéticamente
    todos_pdfs = sorted(list(carpeta.glob("*.pdf")))
    pdfs = [pdf for pdf in todos_pdfs if pdf.name not in Excluidos]

    if not pdfs:
        print(f"⚠️  No se encontraron PDFs en {carpeta}")
        return
    
    print(f"🖨️  Iniciando impresión de {len(pdfs)} documentos...")
    print("-" * 50)
    
    contador_exitos = 0
    contador_errores = 0
    contador_global = 0
    
    for i, pdf in enumerate(pdfs, 1):
        if contador_global > 0 and contador_global % 100 == 0:
            print('\n Límite de 100 páginas impresas.')
            print(f"   Total: {len(pdfs)}")
            print(f"   Correctas: {contador_exitos}")
            print(f"   Errores: {contador_errores}")
            input('Presiona Enter para continuar. . .')
        
        try:
            print(f"\n📄 [{i}/{len(pdfs)}] Imprimiendo: {pdf.name}")

            # Busca cada PDF y cuántas páginas tiene.
            with open(pdf, 'rb') as ArchivoPDF:
                LecturaArchivoPDF = PdfReader(ArchivoPDF)
                PaginasLocales += len(LecturaArchivoPDF.pages)

                # Crea un registro con los que va imprimiendo bien.
                with open('LogActual.txt', 'w', encoding='utf-8') as Registro:
                    Registro.write(f'{pdf.name}\n')
            
            contador_global += 1
            
            if sys.platform == "win32":
                comando = f"Start-Process -FilePath '{pdf}' -Verb Print -WindowStyle Hidden"
                subprocess.run(["powershell", "-Command", comando], timeout=30, check=True)
            
            contador_exitos += 1
            print(f"✅ Impresión enviada correctamente")
            time.sleep(1)
            
        except subprocess.TimeoutExpired:
            print(f"⚠️  Timeout imprimiendo {pdf.name}")
            contador_errores += 1
        except Exception as e:
            print(f"❌ Error imprimiendo {pdf.name}: {str(e)}")
            contador_errores += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Resumen de impresión:")
    print(f"   Total documentos: {len(pdfs)}")
    print(f"   Impresiones exitosas: {contador_exitos}")
    print(f"   Errores: {contador_errores}")
    print(f'   Cantidad de páginas impresas: {PaginasLocales}')
    print("=" * 50)

if __name__ == "__main__":
    # Truco para que NUNCA se te vuelva a cerrar la terminal si hay un error
    try:
        carpeta_origen = LeerDirectorio()
        carpeta_extendidos = carpeta_origen
        nombre_impresora = None
        
        print("🖨️  SCRIPT DE IMPRESIÓN DE CONTRATOS EXTENDIDOS")
        print("=" * 50)
        
        print(f"\n⚠️  Se van a imprimir todos los PDFs en:")
        print(f"   {carpeta_extendidos}")
        
        respuesta = input("\n¿Deseas continuar? (s/n): ").lower()
        
        if respuesta == 's':
            imprimir_pdfs_individuales(carpeta_extendidos, nombre_impresora)
        else:
            print("❌ Impresión cancelada por el usuario")

    except Exception as e:
        print(f"\n💀 ERROR FATAL QUE CERRABA TU TERMINAL: {e}")
    
    finally:
        input('\nPrograma finalizado. Presiona ENTER para salir...')