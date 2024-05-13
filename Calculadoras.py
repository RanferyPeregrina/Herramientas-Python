def PonerComa(Texto):
    Texto = str(Texto)
    Cadena = ""
    Contador = 0;
    for i in range(len(Texto) - 1, -1, -1):
        Cadena = Cadena + str(Texto[i])
        
        Contador += 1
        if Contador %3 == 0:
            Cadena = Cadena + "," 
    return Cadena[::-1]  

def QuitarComas(Texto):
    ContadorComas = 0
    CadenaNueva = []
    for Letra in Texto:
        if Letra != ",":
            CadenaNueva.append(Letra)
        else:
            ContadorComas = ContadorComas + 1
    return "".join(CadenaNueva)

def ConvertirFloat_Int(Numero_Float):
    Numero_Int = int(Numero_Float)
    ParteDecimal = Numero_Float - Numero_Int

    if ParteDecimal != 0:
        return Numero_Float
    elif ParteDecimal == 0:
        return Numero_Int

def Calculadora_Sumar():
    i = 1
    Numero = 0
    NumeroSumatoria = 0
    while True:
        TextoRecibido = input(f"Numero{i}:  ")
        Numero = float(QuitarComas(TextoRecibido))
        
        NumeroSumatoria = NumeroSumatoria + Numero
        i += 1

        print(f"El numero ahora es: {ConvertirFloat_Int(NumeroSumatoria)}")
        print

def Calculadora_Potencias():
        
    print("--------------------------------------")
    Base = float(input("Base:               "))
    Limite = int(input("Potencia Máxima:    "))
    print("--------------------------------------")
    
    Base = ConvertirFloat_Int(Base)
    
    for i in range(Limite + 1):
        Numero = Base ** i
        print(f"{Base} ^ {i}:   {Numero}")

def Main():
    print("==============================")
    print("Calculadora Sumar:       1")
    print("Calculadora Potencias:   2")
    print()
    Respuesta = int(input("Respuesta:  "))
    if(Respuesta == 1):
        Calculadora_Sumar()
    elif(Respuesta ==2):
        Calculadora_Potencias()

Main()
