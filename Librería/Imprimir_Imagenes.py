import os
import sys
import time

# Extensiones de imagen comunes
EXTENSIONES_IMAGEN = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif')

def obtener_imagenes_ordenadas(directorio):
    """
    Devuelve lista de rutas de imágenes en el directorio, ordenadas por fecha de modificación
    (más antigua a más reciente, que es el orden natural de descarga).
    """
    imagenes = []
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        # Solo archivos, no directorios
        if os.path.isfile(ruta_completa) and archivo.lower().endswith(EXTENSIONES_IMAGEN):
            imagenes.append(ruta_completa)
    
    # Ordenar por fecha de modificación (mtime)
    imagenes.sort(key=os.path.getmtime)
    return imagenes

def imprimir_imagen(ruta):
    """
    Envía una imagen a la impresora predeterminada usando el comando 'print' del sistema.
    Windows ajusta la imagen al tamaño de la página por defecto.
    """
    try:
        os.startfile(ruta, "print")
        print(f"  Enviado: {os.path.basename(ruta)}")
        return True
    except Exception as e:
        print(f"  ERROR al enviar {os.path.basename(ruta)}: {e}")
        return False

def main():
    directorio_actual = os.getcwd()
    print(f"📁 Buscando imágenes en: {directorio_actual}")

    imagenes = obtener_imagenes_ordenadas(directorio_actual)
    if not imagenes:
        print("❌ No se encontraron imágenes en esta carpeta.")
        input("Presiona Enter para salir...")
        sys.exit(0)
    
    print(f"🖼️  Se encontraron {len(imagenes)} imágenes. Ordenadas por fecha de modificación.")
    print("🖨️  Comenzando impresión...")
    
    for i, ruta in enumerate(imagenes, start=1):
        print(f"[{i}/{len(imagenes)}] Imprimiendo...")
        imprimir_imagen(ruta)
        # Pequeña pausa para evitar saturar la cola de impresión
        time.sleep(0.5)
    
    print("✅ Todas las imágenes han sido enviadas a la impresora.")
    print("ℹ️  Verifica que la impresora esté encendida y con papel.")
    input("Presiona Enter para cerrar...")

if __name__ == "__main__":
    main()

input()