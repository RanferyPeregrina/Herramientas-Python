#Cambiar estas variables cuando se ejecute el programa en otro local.
nombre_impresora = 'Canon 2'
limite_seguridad = 5
tiempo_espera = 8.0

# -------------------- Aquí empieza el programa y la declaración de cosas ----------------------------------------------------------------------------------

import os
import subprocess
import time
from pathlib import Path
import sys
from PyPDF2 import PdfReader
#Vamos a importar unas librerías para usar la impresora de windows
try:
    import win32print
    import win32api
    USAR_WIN32 = True
except ImportError:
    USAR_WIN32 = False

#Obtenemos la carpeta donde estamos trabajando.
def LeerDirectorio():
    Directorio_Actual = os.path.dirname(os.path.abspath(__file__))
    return Directorio_Actual

#Revisamos si la impresora existe. (Según el nombre de impresora declarado en la línea 2)
def verificar_y_configurar_impresora(nombre_deseado):
    #Verifica librerías.
    if not USAR_WIN32:
        print("⚠️ La librería 'pywin32' no está instalada. Se intentará impresión básica.")
        return False

    #Verifica impresoras.
    try:
        impresoras = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)]
        print(f"🖨️ Impresoras detectadas en el sistema: {impresoras}")                  #Enlista las que encontró.

        if nombre_deseado in impresoras:
            print(f"✅ ¡Impresora encontrada con éxito: '{nombre_deseado}'!")           #Y si la declarada está, avisa.
            return True
        else:                                                                           #Si no, usará la predeterminada.
            print(f"❌ ADVERTENCIA: No se encontró la impresora '{nombre_deseado}'.")
            print("   Se buscará usar la predeterminada del equipo.")
            return False
    except Exception as e:
        print(f"⚠️ Error al listar impresoras: {e}")
        return False


#Imprime una por una.
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

    #Obliga a imprimir ALFABÉTICAMENTE (Manejando números también)
    todos_pdfs = sorted(
        list(carpeta.glob("*.pdf")),
        key=lambda p: [int(x) if x.isdigit() else x.lower() for x in __import__('re').split(r'(\d+)', p.name)]
    )

    #Pregunta si quieres ver cómo quedaron ordenados todas las cosas
    imprimir_listota = input('\n¿Por motivos de depuración, imprimir toda la lista? de archivos con los que se va a trabajar (Si / No):  ')
    if imprimir_listota.lower() == 'si':
        for pdf in todos_pdfs:
            print(pdf.name)

    #Recolecta todos los PDFs en una lista.
    pdfs = [pdf for pdf in todos_pdfs if pdf.name not in Excluidos]
    if not pdfs:
        print(f"⚠️ No se encontraron PDFs en {carpeta}")
        return
    
    #Imprime.
    input("\nPresiona ENTER para comenzar la impresión...")
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
        if contador_global > 0 and contador_global % limite_seguridad == 0:
            print('\n⏸️ Límite de seguridad alcanzado.')
            print(f"   Total hechos hasta ahora: {contador_global}")
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
                        # Windows recurrirá al controlador de la impresora seleccionada y respetará el ajuste dúplex predeterminado del driver.
                    win32api.ShellExecute(0, "print", ruta_pdf_str, f'/d:"{target_printer}"', ".", 0)
                else:
                    # Respaldo por PowerShell si pywin32 tuviera algún inconveniente menor
                    comando = f"Start-Process -FilePath '{ruta_pdf_str}' -Verb Print -WindowStyle Hidden"
                        # Windows usará Powershell para pedir una impresión de sistema.
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
    print(f"   Total documentos requeridos: {len(pdfs)}")
    print(f"   Total documentos hechos: {contador_global}")
    print(f"   Impresiones exitosas: {contador_exitos}")
    print(f"   Errores: {contador_errores}")
    print(f"   Cantidad total de páginas (Sin contar hojas blancas): {PaginasLocales}")
    print("=" * 50)

if __name__ == "__main__":
    try:
        carpeta_origen = LeerDirectorio()
        carpeta_extendidos = carpeta_origen
        
        print("=" * 50)
        print("🖨️ SCRIPT DE IMPRESIÓN DUPLEX - CONTRATOS EXTENDIDOS")
        print(f"\n⚠️ Se van a imprimir a dos caras (Según esté configurada la impresora predeterminada), todos los archivos en lotes de {limite_seguridad} los PDFs de:")
        print(f"   {carpeta_extendidos}")
        respuesta = input("\n¿Deseas continuar? (s/n): ").lower()
        
        if respuesta == 's':
            imprimir_pdfs_individuales(carpeta_extendidos, nombre_impresora)
        else:
            print("❌ Impresión cancelada por el usuario")
        print("=" * 50)
    except Exception as e:
        print(f"\n💀 ERROR FATAL: {e}")
    
    finally:
        input('\nPrograma finalizado. Presiona ENTER para salir...')
