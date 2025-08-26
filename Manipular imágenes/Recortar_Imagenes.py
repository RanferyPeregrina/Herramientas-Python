from PIL import image #Esta es una librería de Pillow para leer imágenes

def Recortar_Imagen(IMAGEN, Lado, Pixeles):
    IMAGEN_alto, IMAGEN_ancho = IMAGEN.size
    if Lado == 1:
        IMAGEN_Recortada = IMAGEN.crop(Pixeles, 0, IMAGEN_ancho, IMAGEN_alto)
    elif Lado == 2:
        IMAGEN_Recortada = IMAGEN.crop(0, Pixeles, IMAGEN_ancho, IMAGEN_alto)
    elif Lado == 3:
        IMAGEN_Recortada = IMAGEN.crop(0, 0, IMAGEN_ancho - Pixeles, IMAGEN_alto)
    elif Lado == 4:
        IMAGEN_Recortada = IMAGEN.crop(0, IMAGEN_alto - Pixeles, IMAGEN_ancho, IMAGEN_alto)



print("Este programa es para tumbarle unos pixeles a tu imágen del lado que quieras.\n")
print("¿Quieres recortar imágen específica o todas las de esta carpeta?")
print("1.- Específica")
print("2.- Todas")
Respuesta1 = int(input("Respuesta:  "))

print("¿Quieres recortar de: ")
print("1.- Izquierda")
print("2.- Arriba")
print("3.- Derecha")
print("4.- Abajo")
Respuesta2 = int(input("Respuesta:  "))

Pixeles = input("¿Cuántos pixeles va a recortar?:  ")
if Pixeles.lower() != "roblox":
    Pixeles = int(Pixeles)

if Respuesta1 == 1:
    Nombre_Imagen = input("Ingrese el nombre de su imágen: ")
    IMAGEN = image.open(Nombre_Imagen)
elif Respuesta1 == 2:
    print("Aún no está lista esta función")

Recortar_Imagen(IMAGEN, Respuesta2, Pixeles)