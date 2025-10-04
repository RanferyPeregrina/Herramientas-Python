#Programa que convierte una serie de tipo Item1, Item2, Item3
#En una lista de tipo:  Item1
#                       Item2
#                       Item3
def JuntarTexto(Texto1, Texto2):
    TextoJunto = Texto1 + Texto2
    return TextoJunto

def ConvertirTexto(Texto_Comas):
    Contador = 0
    Texto_Espacios = ""

    for letra in Texto_Comas:
        if letra == ",":
            letra = "\n"  # Reemplaza la coma por un salto de línea
        # if letra == " ":
        #     letra = ""
        Texto_Espacios = JuntarTexto(Texto_Espacios, letra)
        Contador += 1  # Incrementa el contador de letras

    print(f"El nuevo texto es:\n\n{Texto_Espacios}")
    print(f"\n - - - - - - - - -- - - - - - - - - - \nEl número de letras es: {Contador - 1}")

print("Programa que convierte una lista separa por comas en una lista separada por renglones.")
print("¿Quiere importar su lista de un .txt o escribirla aquí?")
print("1.- Importar de un archivo.txt")
print("2.- Escribir aquí")
Respuesta = int(input("Respuesta:  "))

if Respuesta == 1:
    print("NO DISPONIBLE POR AHORA")
elif Respuesta == 2:
    print("- " * 35)
    print("Ingrese su texto:  ")
    print("\n\n")
    Texto_Comas = input()

    ConvertirTexto(Texto_Comas)
elif Respuesta == 3:
    TexotInicial = ""
    while True:
        print("\n")
        print("- " * 20)
        TextoPedido = input("Ingrese texto a concatenar:  ") 
        TexotInicial = JuntarTexto(TexotInicial, TextoPedido)
        print(f"El texto hasta ahora es: {TexotInicial}")