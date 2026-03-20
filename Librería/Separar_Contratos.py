import os
import shutil
from PyPDF2 import PdfReader
from pathlib import Path

def LeerDirectorio():
    Directorio_Actual = os.getcwd()
    return Directorio_Actual

def clasificar_pdfs(carpeta_origen):
    """
    Clasifica PDFs según número de páginas.
    Los de 1 página van a un archivo combinado.
    Los de más páginas se mueven a carpeta 'Extendidos'
    """
    
    # Crear carpetas necesarias
    carpeta_origen = Path(carpeta_origen)
    carpeta_extendidos = carpeta_origen / 'Extendidos'
    carpeta_extendidos.mkdir(exist_ok=True)
    
    # Lista para almacenar rutas de PDFs de 1 página
    pdfs_una_pagina = []
    
    # Contadores para seguimiento
    total_procesados = 0
    movidos_extendidos = 0
    una_pagina = 0
    
    print("📄 Iniciando clasificación de PDFs...")
    print("-" * 50)
    
    # Recorrer todos los PDFs en la carpeta
    for archivo in carpeta_origen.glob("*.pdf"):
        try:
            # Leer el PDF para contar páginas
            with open(archivo, 'rb') as file:
                pdf = PdfReader(file)
                num_paginas = len(pdf.pages)
            
            if num_paginas == 1:
                # Contrato de 1 página
                pdfs_una_pagina.append(archivo)
                una_pagina += 1
                print(f"✅ {archivo.name} - {num_paginas} página - Para combinar")
                
            elif num_paginas > 1:
                # Contrato extendido
                destino = carpeta_extendidos / archivo.name
                shutil.move(str(archivo), str(destino))
                movidos_extendidos += 1
                print(f"📦 {archivo.name} - {num_paginas} páginas - Movido a Extendidos/")
            
            total_procesados += 1
            
        except Exception as e:
            print(f"❌ Error procesando {archivo.name}: {str(e)}")
    
    print("-" * 50)
    print(f"\n📊 Resumen:")
    print(f"   Total procesados: {total_procesados}")
    print(f"   Contratos de 1 página: {una_pagina}")
    print(f"   Contratos extendidos: {movidos_extendidos}")
    
    # Combinar PDFs de 1 página si hay alguno
    if pdfs_una_pagina:
        combinar_pdfs_una_pagina(pdfs_una_pagina, carpeta_origen)
    else:
        print("⚠️  No se encontraron contratos de 1 página para combinar")
    
    return pdfs_una_pagina

def combinar_pdfs_una_pagina(lista_pdfs, carpeta_destino):
    """
    Combina todos los PDFs de 1 página en un solo documento
    """
    from PyPDF2 import PdfMerger
    
    try:
        merger = PdfMerger()
        archivo_salida = carpeta_destino / "CONTRATOS_UNA_PAGINA_COMBINADOS.pdf"
        
        print(f"\n🔨 Combinando {len(lista_pdfs)} contratos de 1 página...")
        
        for pdf in lista_pdfs:
            merger.append(str(pdf))
            # Opcional: eliminar el archivo original después de combinarlo
            # pdf.unlink()
        
        merger.write(str(archivo_salida))
        merger.close()
        
        print(f"✅ Archivo combinado creado: {archivo_salida.name}")
        print(f"📄 Total de páginas en el documento combinado: {len(lista_pdfs)}")
        
    except Exception as e:
        print(f"❌ Error al combinar PDFs: {str(e)}")

if __name__ == "__main__":
    # Cambia esta ruta por la ubicación de tu carpeta
    carpeta_contratos = LeerDirectorio()
    
    # Verificar que la carpeta existe
    if os.path.exists(carpeta_contratos):
        clasificar_pdfs(carpeta_contratos)
    else:
        print(f"❌ La carpeta {carpeta_contratos} no existe")
        print("Por favor, actualiza la ruta en el script")


input('Programa en espera de finalizar')