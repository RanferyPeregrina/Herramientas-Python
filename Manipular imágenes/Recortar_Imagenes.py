from PIL import image #Esta es una librería de Pillow para leer imágenes

print("Este programa es para tumbarle unos pixeles a tu imágen del lado que quieras.\n")
print("¿Quieres recortar imágen específica o todas las de esta carpeta?")
print("1.- Específica")
print("2.- Todas")
Respuesta = int(input("Respuesta:  "))


if Respuesta == 1:
    Nombre_Imagen = input("Ingrese el nombre de su imágen: ")
    IMAGEN = image.open(Nombre_Imagen)