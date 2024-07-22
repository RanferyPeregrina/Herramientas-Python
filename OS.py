import os

#  --------------------- Obtener un directorio de trabajo ----------------------
def seleccionar_directorio_actual():
    # Obtiene el directorio actual de trabajo
    directorio_actual = os.getcwd()
    print(f"El directorio actual es: {directorio_actual}")
    return directorio_actual

# Uso
directorio_actual = seleccionar_directorio_actual()

#  ---------------------- Cambiar un directorio de trabajo ----------------------

def cambiar_directorio(nuevo_directorio):
    # Cambia el directorio de trabajo al especificado
    os.chdir(nuevo_directorio)
    print(f"Se ha cambiado al directorio: {nuevo_directorio}")

# Uso
nuevo_directorio = "/ruta/a/tu/nuevo/directorio"
cambiar_directorio(nuevo_directorio)

#  ----------------------- Crear un directorio de trabajo ----------------------

def crear_directorio(nombre_directorio):
    # Crea un nuevo directorio con el nombre especificado
    os.makedirs(nombre_directorio, exist_ok=True)
    print(f"Se ha creado el directorio: {nombre_directorio}")

# Uso
nombre_directorio = "nuevo_directorio"
crear_directorio(nombre_directorio)

#  ----------------------- "dir" de  un directorio de trabajo ----------------------

def listar_archivos(directorio):
    # Lista todos los archivos y carpetas en el directorio especificado
    archivos = os.listdir(directorio)
    print(f"Archivos en el directorio {directorio}: {archivos}")
    return archivos

# Uso
directorio = "/ruta/a/tu/directorio"
listar_archivos(directorio)

#  ----------------------- Mover archivo de un directorio ----------------------

import shutil

def mover_archivo(ruta_archivo, directorio_destino):
    # Mueve un archivo a otro directorio
    shutil.move(ruta_archivo, directorio_destino)
    print(f"Se ha movido el archivo {ruta_archivo} a {directorio_destino}")

# Uso
ruta_archivo = "/ruta/a/tu/archivo.txt"
directorio_destino = "/ruta/a/tu/directorio_destino"
mover_archivo(ruta_archivo, directorio_destino)

#  ----------------------- Eliminar archivo de un directorio ----------------------

def eliminar_archivo(ruta_archivo):
    # Elimina el archivo especificado
    os.remove(ruta_archivo)
    print(f"Se ha eliminado el archivo: {ruta_archivo}")

# Uso
ruta_archivo = "/ruta/a/tu/archivo.txt"
eliminar_archivo(ruta_archivo)
