import os
import subprocess
import time
from pathlib import Path
import sys
from PyPDF2 import PdfReader

#Cambiar estas variables cuando se ejecute el programa en otro local.
nombre_impresora = 'Canon 2'
limite_seguridad = 5
tiempo_espera = 8.0

# Intentamos importar win32 para control avanzado de impresora
try:
    import win32print
    import win32api
    USAR_WIN32 = True
except ImportError:
    USAR_WIN32 = False

def LeerDirectorio():
    Directorio_Actual = os.path.dirname(os.path.abspath(__file__))
    return Directorio_Actual

def verificar_y_configurar_impresora(nombre_deseado):
    """Verifica si la impresora existe en el sistema y la muestra."""
    if not USAR_WIN32:
        print("⚠️ La librería 'pywin32' no está instalada. Se intentará impresión básica.")
        return False

    try:
        impresoras = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)]
        print(f"🖨️ Impresoras detectadas en el sistema: {impresoras}")

        if nombre_deseado in impresoras:
            print(f"✅ ¡Impresora encontrada con éxito: '{nombre_deseado}'!")
            return True
        else:
            print(f"❌ ADVERTENCIA: No se encontró la impresora '{nombre_deseado}'.")
            print("   Se buscará usar la predeterminada del equipo.")
            return False
    except Exception as e:
        print(f"⚠️ Error al listar impresoras: {e}")
        return False

def imprimir_pdfs_individuales(carpeta_pdfs, impresora_nombre=None):
    carpeta = Path(carpeta_pdfs)
    PaginasLocales = 0

    if not carpeta.exists():
        print(f"❌ La carpeta {carpeta} no existe")
        return
    
    # Validar Excluidos.txt
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

    todos_pdfs = sorted(
        list(carpeta.glob("*.pdf")),
        key=lambda p: [int(x) if x.isdigit() else x.lower() for x in __import__('re').split(r'(\d+)', p.name)]
    )

    imprimir_listota = input('\n¿Por motivos de depuración, imprimir toda la lista? (Si / No):  ')
    if imprimir_listota.lower() == 'si':
        for pdf in todos_pdfs:
            print(pdf.name)

    input("\nPresiona ENTER para comenzar la impresión...")

    pdfs = [pdf for pdf in todos_pdfs if pdf.name not in Excluidos]

    if not pdfs:
        print(f"⚠️ No se encontraron PDFs en {carpeta}")
        return
    
    # Validar la impresora al arrancar el proceso
    impresora_valida = verificar_y_configurar_impresora(impresora_nombre) if impresora_nombre else False
    target_printer = impresora_nombre if impresora_valida else (win32print.GetDefaultPrinter() if USAR_WIN32 else None)

    print(f"\n🖨️ Iniciando impresión DUPLEX (A dos caras) de {len(pdfs)} documentos...")
    print(f"🎯 Usando impresora activa: {target_printer}")
    print("-" * 50)
    
    contador_exitos = 0
    contador_errores = 0
    contador_global = 0
    
    for i, pdf in enumerate(pdfs, 1):
        #Modifiquen este parámetro para controlar el límite de impresiones de seguridad
        if contador_global > 0 and contador_global % limite_seguridad == 0:
            print('\n⏸️ Límite de seguridad alcanzado.')
            print(f"   Total procesados: {len(pdfs)}")
            print(f"   Correctas: {contador_exitos}")
            print(f"   Errores: {contador_errores}")
            input('Presiona Enter para continuar. . .')
        
        try:
            print(f"\n📄 [{i}/{len(pdfs)}] Imprimiendo a 2 caras: {pdf.name}")

            with open(pdf, 'rb') as ArchivoPDF:
                LecturaArchivoPDF = PdfReader(ArchivoPDF)
                PaginasLocales += len(LecturaArchivoPDF.pages)

            
            contador_global += 1
            
            if sys.platform == "win32":
                ruta_pdf_str = str(pdf.resolve())

                if USAR_WIN32 and target_printer:
                    # Método nativo mediante ShellExecute especificando la impresora exacta
                    # Windows recurrirá al controlador PCL6 de la Xerox y respetará el ajuste dúplex predeterminado del driver.
                    win32api.ShellExecute(0, "print", ruta_pdf_str, f'/d:"{target_printer}"', ".", 0)
                else:
                    # Respaldo por PowerShell si pywin32 tuviera algún inconveniente menor
                    comando = f"Start-Process -FilePath '{ruta_pdf_str}' -Verb Print -WindowStyle Hidden"
                    subprocess.run(["powershell", "-Command", comando], timeout=30, check=True)
            
            contador_exitos += 1
            with open("LogActual.txt", "a", encoding='utf-8') as Registro:
                                Registro.write(f'{pdf}\n')
            print(f"✅ Enviado a la cola de impresión de '{target_printer}'")
            time.sleep(tiempo_espera) # Pausa breve para evitar saturar el spooler de la impresora
            
        except subprocess.TimeoutExpired:
            print(f"⚠️ Timeout imprimiendo {pdf.name}")
            contador_errores += 1
        except Exception as e:
            print(f"❌ Error imprimiendo {pdf.name}: {str(e)}")
            contador_errores += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Resumen de impresión:")
    print(f"   Total documentos: {len(pdfs)}")
    print(f"   Impresiones exitosas: {contador_exitos}")
    print(f"   Errores: {contador_errores}")
    print(f"   Cantidad total de páginas: {PaginasLocales}")
    print("=" * 50)

if __name__ == "__main__":
    try:
        carpeta_origen = LeerDirectorio()
        carpeta_extendidos = carpeta_origen
        
        print("🖨️ SCRIPT DE IMPRESIÓN DUPLEX - CONTRATOS EXTENDIDOS")
        print("=" * 50)
        
        print(f"\n⚠️ Se van a imprimir a DOS CARAS todos los PDFs en:")
        print(f"   {carpeta_extendidos}")
        
        respuesta = input("\n¿Deseas continuar? (s/n): ").lower()
        
        if respuesta == 's':
            imprimir_pdfs_individuales(carpeta_extendidos, nombre_impresora)
        else:
            print("❌ Impresión cancelada por el usuario")

    except Exception as e:
        print(f"\n💀 ERROR FATAL: {e}")
    
    finally:
        input('\nPrograma finalizado. Presiona ENTER para salir...')
