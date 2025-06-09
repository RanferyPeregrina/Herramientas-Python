#Programa para hacer conversiones de tiempo simples

print("=================================================")
print("1.- Convertir A SEGUNDOS")
print("2.- Convertir A MINUTOS")
print("3.- Conertir A HORAS")
MenuOpciones = int(input("Respuesta:  "))
print("\n=================================================")
print("\n NOTA: Si no hay horas o lo que sea, escriba '0' a continuación:")
Horas = int(input("Ingrese cantidad de HORAS:  "))
Minutos = int(input("Ingrese cantidad de MINUTOS:  "))
Segundos = int(input("Ingrese cantidad de SEGUNDOS:  "))
print("")
if MenuOpciones == 1:
    Segundos = (Horas * 60 * 60) + (Minutos * 60) + Segundos
    print(f"Son en total: {Segundos} segundos")

elif MenuOpciones == 2:
    if Segundos >= 60:
        Minutos = Minutos + (Segundos / 60)
        Segundos = Segundos % 60
    Minutos1 = (Horas * 60) + (Minutos)
    Minutos2 = (Horas * 60) + (Minutos) + ((Segundos * 100 / 60) / 100) #Se divide entre 100 porque es PORCENTAJE de minutos que es cada segundo.
    print(f"En notación sexagesimal:    {Minutos1}:{Segundos}")
    print(f"En notación decimal:    {Minutos2} minutos")

elif MenuOpciones == 3:
    if Segundos >= 60:
        Minutos += (Segundos / 60)
        Segundos = Segundos % 60
    if Minutos >= 60:
        Horas += (Minutos / 60)
        Minutos = Minutos % 60

    Horas1 = Horas + (Minutos * (100 / 60) / 100) + ((Segundos * 100 * 3600) / 100)
    print(f"En notación sexagesimal:    {Horas}:{Minutos}:{Segundos}   ... oh, eso ya lo sabías.")
    print(f"En notación decimal:    {Horas1}")
