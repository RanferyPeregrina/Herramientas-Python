#Este programa es para generar basura aleatoria.
#Para llenar rápido un directorio... De basura.
#Es prácticamente un virus.

#Pero sirve para probar por ejemplo, memorias USB
def Espacio_Llenar(Opcion):

    if Opcion == 1: Multiplicador = 1               #1Mb
    if Opcion == 2: Multiplicador = 100             #100Mbs
    if Opcion == 3: Multiplicador = 100 * 10        #1GBs
    if Opcion == 4: Multiplicador = 100 * 10 * 5    #5GBs
    if Opcion == 5: Multiplicador = 100 * 10 * 10   #10GBs
    if Opcion == 6: Multiplicador = 100 * 10 * 100  #100GBs
    if Opcion == 7: Multiplicador = 100 * 10 * 500  #500GBs
    if Opcion == 8: Multiplicador = 100 * 10 * 100 * 10     #1TB
    if Opcion == 9: Multiplicador = Opcion

    contenido = "1234567890" * (1024 * 1024 // 10) # 1 MB de contenido repetitivo
    for i in range(Multiplicador):
        with open(f"Basura{i}.txt", "w") as Archivo:
            Archivo.write((contenido))
    print(f"Llenado. {i + 1} archivos de basura generados.")
def Espacio_Vaciar():
    return 1
def Espacio_Leer(Opcion):
    if Opcion == 1: Multiplicador = 1               #1Mb
    if Opcion == 2: Multiplicador = 100             #100Mbs
    if Opcion == 3: Multiplicador = 100 * 10        #1GBs
    if Opcion == 4: Multiplicador = 100 * 10 * 5    #5GBs
    if Opcion == 5: Multiplicador = 100 * 10 * 10   #10GBs
    if Opcion == 6: Multiplicador = 100 * 10 * 100  #100GBs
    if Opcion == 7: Multiplicador = 100 * 10 * 500  #500GBs
    if Opcion == 8: Multiplicador = 100 * 10 * 100 * 10     #1TB
    if Opcion == 9: Multiplicador = Opcion
    

    print(f"Se espera encontrar {Opcion + 1} archivos.")
    contenido_Correcto = "1234567890" * (1024 * 1024 // 10)
    for i in range(Opcion):
        with open(f"Basura{i}.txt", "r") as Archivo:
            contenido_Leido = Archivo.read()
        if contenido_Correcto == contenido_Leido: print("Todo Bien")
        else: print("Todo mal.")


print("="*50)
print("Generador/Lector de basura")
print("1.- Generar Basura.")
print("2.- Corroborar integridad de la basura.")
print("3.- Salir.")
Respuesta = input("Respuesta:  ")
print("- "*17)

if Respuesta == "1":
    print("Ingrese la cantidad de espacio que quiere llenar: ")
    print("1.- 1MB")
    print("2.- 100MBs")
    print("3.- 1GB")
    print("4.- 5GBs")
    print("5.- 10GBs")
    print("6.- 100GBs")
    print("7.- 500GBs")
    print("8.- 1TB")
    Opcion = int(input("Respuesta:  "))
    print("Llenando...")
    Espacio_Llenar(Opcion)
    print("Finalizado...")
    print("="* 50)
elif Respuesta == "2":
    print("¿Qué cantidad de basura metió?")
    print("1.- 1MB")
    print("2.- 100MBs")
    print("3.- 1GB")
    print("4.- 5GBs")
    print("5.- 10GBs")
    print("6.- 100GBs")
    print("7.- 500GBs")
    print("8.- 1TB")
    Opcion = int(input("Respuesta:  "))
    Espacio_Leer(Opcion)

