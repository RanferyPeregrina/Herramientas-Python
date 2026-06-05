import os
import subprocess
import time
from pathlib import Path
import sys
import shutil
from PyPDF2 import PdfReader

def LeerDirectorio():
    Directorio_Actual = os.path.dirname(os.path.abspath(__file__))
    return Directorio_Actual

def imprimir_pdfs_individuales(carpeta_pdfs, impresora_nombre=None):
    """
    Imprime cada PDF de la carpeta individualmente
    
    Args:
        carpeta_pdfs: Ruta de la carpeta con los PDFs a imprimir
        impresora_nombre: Nombre de la impresora (opcional, usa la predeterminada si es None)
    """
    
    carpeta = Path(carpeta_pdfs)
    
    if not carpeta.exists():
        print(f"❌ La carpeta {carpeta} no existe")
        return
    
    # Obtener lista de PDFs
    pdfs = list(carpeta.glob("*.pdf"))
    
    if not pdfs:
        print(f"⚠️  No se encontraron PDFs en {carpeta}")
        return
    
    print(f"🖨️  Iniciando impresión de {len(pdfs)} documentos...")
    print("-" * 50)
    
    contador_exitos = 0
    contador_errores = 0
    
    for i, pdf in enumerate(pdfs, 1):
        try:
            print(f"\n📄 [{i}/{len(pdfs)}] Imprimiendo: {pdf.name}")
            
            # Método 1: Usar el comando de Windows (más confiable)
            if sys.platform == "win32":
                # Para Windows
                if impresora_nombre:
                    # Especificar impresora
                    subprocess.run([
                        "powershell", 
                        "-Command", 
                        f"Start-Process -FilePath '{pdf}' -Verb Print -WindowStyle Hidden"
                    ], timeout=30, check=True)
                else:
                    # Usar impresora predeterminada
                    subprocess.run([
                        "powershell", 
                        "-Command", 
                        f"Start-Process -FilePath '{pdf}' -Verb Print -WindowStyle Hidden"
                    ], timeout=30, check=True)
            
            # Esto está por si el programa se llega a ejecutar en MAC pero yo lo estoy haciendo en Windows
            elif sys.platform == "darwin":  # macOS
                subprocess.run(["lp", str(pdf)], timeout=30, check=True)
            
            else:  # Linux
                subprocess.run(["lp", str(pdf)], timeout=30, check=True)
            
            contador_exitos += 1
            print(f"✅ Impresión enviada correctamente")
            
            # Pequeña pausa para evitar saturar la cola de impresión
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
    print("=" * 50)

def imprimir_pdf_individual(pdf_path, impresora_nombre=None):
    """
    Función auxiliar para imprimir un solo PDF
    Útil para probar la impresión
    """
    try:
        if sys.platform == "win32":
            subprocess.run([
                "powershell", 
                "-Command", 
                f"Start-Process -FilePath '{pdf_path}' -Verb Print -WindowStyle Hidden"
            ], timeout=30, check=True)
            return True
        else:
            subprocess.run(["lp", pdf_path], timeout=30, check=True)
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # Ruta de la carpeta Extendidos
    # Esta carpeta se creó en el script anterior
    carpeta_origen = LeerDirectorio()
    carpeta_extendidos = carpeta_origen
    
    # Opcional: Especificar nombre de impresora
    # Para ver las impresoras disponibles en Windows:
    # Ejecuta en PowerShell: Get-Printer | Select-Object Name
    nombre_impresora = None  # Usa la impresora predeterminada
    
    print("🖨️  SCRIPT DE IMPRESIÓN DE CONTRATOS EXTENDIDOS")
    print("=" * 50)
    
    # Preguntar confirmación antes de imprimir muchos documentos
    print(f"\n⚠️  Se van a imprimir todos los PDFs en:")
    print(f"   {carpeta_extendidos}")
    
    respuesta = input("\n¿Deseas continuar? (s/n): ").lower()
    
    if respuesta == 's':
        imprimir_pdfs_individuales(carpeta_extendidos, nombre_impresora)
    else:
        print("❌ Impresión cancelada por el usuario")


input('Programa en espera de finalizar')